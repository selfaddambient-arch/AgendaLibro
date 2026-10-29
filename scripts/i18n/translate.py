"""2冊の英訳（Claude Sonnet 5.5・Batch API）。
  python3 scripts/i18n/translate.py prepare            # 原稿を前処理して章ごとに割る（API は呼ばない）
  python3 scripts/i18n/translate.py submit [slug…]     # バッチを出す（費用が発生する）
  python3 scripts/i18n/translate.py status             # 進み具合
  python3 scripts/i18n/translate.py collect            # 結果を取り込み、後処理して manuscript.md を組む
  python3 scripts/i18n/translate.py retry <custom_id…> # 失敗した節だけ、同じ指示でもう一度（同期の呼び出し）

前処理（機械・日本語の原稿に対して）：
  ・リンクの印を「本-言語-形式」にする：?src=book1 → ?src=b1-en-{{FMT}}（本2は book → b2）。{{FMT}} は組版で pdf／kindle／gp に置く
  ・「3つの出口」とおわりにの順を Agenda → 活動を追う → 屯（東京に来たら）に入れ替える
後処理（機械・英訳に対して）：
  ・円の金額の後ろに米ドルの概算を括弧で足す（為替は i18n/glossary.yaml の固定値）
  ・補足の印 ⟦…⟧ を *(…)* にし、同じ補足の2回目以降を消す
鍵は secrets/.env の ANTHROPIC_API_KEY（値は出さない）。
"""
import sys, re, json, os, pathlib, time
import yaml

import os
LG = os.environ.get('I18N_LANG', 'en')   # 言語コード（2文字）。i18n/<言語>/ を使う
ROOT = pathlib.Path(__file__).resolve().parents[2]
MODEL = 'claude-sonnet-5-5'
BOOKS = {
    'hitori-de-mise': dict(ms='books/hitori-de-mise/bontaraku-01_hitori-de-mise_manuscript.md', code='b1', old='book1'),
    'uchi-no-mise': dict(ms='books/uchi-no-mise/bontaraku-02_uchi-no-mise_manuscript.md', code='b2', old='book'),
}
GLOSS = yaml.safe_load(open(ROOT / f'i18n/{LG}/glossary.yaml'))
RATE = GLOSS['usd_per_jpy_rate']
CHUNK_MAX = 11000   # 日本語の文字数。節の境目で割る
MAX_TOKENS = 32000


def env_key():
    for line in open(ROOT / 'secrets/.env'):
        if line.startswith('ANTHROPIC_API_KEY='):
            return line.split('=', 1)[1].strip()
    sys.exit('ANTHROPIC_API_KEY がありません')


def out_dir(slug):
    return ROOT / f'i18n/{LG}/{slug}'


# ───────── 前処理 ─────────
def reorder_exits(t, slug):
    """3つの出口とおわりにの順を Agenda → 活動を追う → 屯（東京に来たら）にする。"""
    # (1) 「この本の、3つの出口」の番号付き3項目
    m = re.search(r'^1\. 屯に行ってみる。(.*)\n2\. (自分の店で試してみる。.*)\n3\. (活動を追いかける。.*)$', t, flags=re.M)
    assert m, '3つの出口の3項目が見つからない'
    new = f'1. {m.group(2)}\n2. {m.group(3)}\n3. 東京に来たら、屯に行ってみる。{m.group(1)}'
    t = t[:m.start()] + new + t[m.end():]
    # (2) 表紙まわりの3行（2冊目のみ）：Agenda を先頭に
    m = re.search(r'(屯のInstagram：\S+)\n\n(屯の予約サイト：\S+)\n\n(Agendaシリーズ：\S+)\n', t)
    if m and slug == 'uchi-no-mise':
        t = t[:m.start()] + f'{m.group(3)}\n\n{m.group(1)}\n\n{m.group(2)}\n' + t[m.end():]
    # (3) 2冊目のおわりに：「もし東中野にお越しの際は」以降の屯の案内を、Agenda・活動の後ろへ
    m = re.search(r'(もし東中野にお越しの際は[^\n]*\n\n)(屯の予約サイト：\S+\n\n)(屯のInstagram：\S+\n\n)(Agendaシリーズ：\S+\n\n)(活動を追いかける：[^\n]*\n\n)', t)
    if slug == 'uchi-no-mise':
        assert m, 'おわりにの案内ブロックが見つからない'
        t = t[:m.start()] + m.group(4) + m.group(5) + m.group(1) + m.group(2) + m.group(3) + t[m.end():]
    return t


def prepare_source(slug):
    b = BOOKS[slug]
    t = (ROOT / b['ms']).read_text()
    code, old = b['code'], b['old']
    t = t.replace(f'?src={old}', f'?src={code}-{LG}-{{{{FMT}}}}').replace(f'?via={old}', f'?via={code}-{LG}-{{{{FMT}}}}')
    assert f'?src={old}' not in t and f'?via={old}' not in t
    t = reorder_exits(t, slug)
    return t


def split_chunks(t):
    """## / ### の見出しで節に割り、CHUNK_MAX を超えない範囲で束ねる。コードの囲みの中は割らない。"""
    lines = t.split('\n')
    sections, cur, fence = [], [], False
    for ln in lines:
        if ln.startswith('```'):
            fence = not fence
        if not fence and re.match(r'^#{2,3} ', ln) and cur:
            sections.append('\n'.join(cur)); cur = []
        cur.append(ln)
    sections.append('\n'.join(cur))
    chunks, buf = [], ''
    for s in sections:
        if buf and len(buf) + len(s) > CHUNK_MAX:
            chunks.append(buf); buf = ''
        buf += ('\n' if buf else '') + s
    if buf:
        chunks.append(buf)
    return chunks


def system_prompt(slug):
    rows = '\n'.join(f"- {g['ja']} → {g['to']}" + (f"  ({g['note']})" if g['note'] else '') for g in GLOSS['terms'])
    notes = '\n'.join(f"- {n['key']}: {n['note']}" for n in GLOSS['standard_notes'])
    return f"""You are a professional Japanese-to-English translator of narrative nonfiction and business books. You are translating a self-published Japanese book by Raku Bonta, a solo bar owner in Tokyo who builds tools with AI. The voice is warm, plain, first-person, and practical. Write natural, idiomatic English for readers in the US, UK and other English-speaking countries. Avoid translationese.

FAITHFULNESS
- Translate faithfully. Do not add, drop, soften or change any fact, number, date, name, quotation or claim. Keep every paragraph; do not merge, summarize or reorder.
- Keep the author's voice and rhythm; short sentences stay short.
- Japanese leaves pronouns out. Never use gendered pronouns (he, him, his, she, her) for any person, including the author and the owner, unless the source itself states the person's gender. Use the name, a role ("the owner", "the agent"), "they", or rephrase.

MARKDOWN STRUCTURE (must be identical to the source)
- Keep every heading with the same number of '#', every list, table, blockquote, code block, blank line, image line and HTML tag in the same place. Translate the text inside them. Do not translate or alter image paths, URLs, or the placeholder {{{{FMT}}}} inside URLs.
- Headings: translate the title, keep the numbering. "第1章　概念編 - …" becomes "Chapter 1: Concepts - …". "1-1. …" and "1-1　…" keep "1-1" followed by the translated title. Use the glossary words for はじめに / おわりに / コラム.
- Figure caption lines: "【図1-1】caption" becomes "【Figure 1-1】caption" (translate the caption). A line like "図1-9　caption" becomes "Figure 1-9: caption". Keep alt text of images translated in the same way ("![図1-9　x](…)" becomes "![Figure 1-9: x](…)").
- Japanese quotation marks 「 」 become English quotation marks. Full-width punctuation becomes normal punctuation. Keep emoji and symbols as they are.

YEN
- Write every amount in yen as "¥" plus digits with commas: "5000円" becomes "¥5,000", "1万円" becomes "¥10,000", "約3000円" becomes "about ¥3,000", "3000〜5000円" becomes "¥3,000–¥5,000", "月額500円" becomes "¥500 per month". Do not convert to dollars and do not add parentheses; the dollar estimate is added by a script later. Amounts already in dollars stay in dollars ("35ドル" becomes "$35").

GLOSSARY (use exactly these renderings every time)
{rows}

THE ONLY ADAPTATIONS ALLOWED
Everything else must follow the source. Do not add commentary of your own.
1. Japan notes: when an English-speaking reader would not know a Japanese place name, institution, system or restaurant custom, add one short gloss (a phrase or one sentence, 25 words at most) right after its FIRST mention in this passage, wrapped in the marks ⟦ and ⟧, for example: Higashi-Nakano ⟦a residential neighborhood in western Tokyo, just west of Shinjuku⟧. Use these exact wordings whenever the term occurs:
{notes}
   Add a note only when it truly helps, and only general facts you are sure of. Never add facts about the author, the bar or the products that are not in the source.
2. Screenshot captions: the screenshots are in Japanese and stay in Japanese. After a figure caption that describes a screen, append ⟦The screen is in Japanese.⟧ and, only if the caption or the surrounding text already says what to look at, one short clause saying so inside the same marks.
3. Links, QR labels and the order of the three exits have already been prepared in the source. Translate them as they stand. In the item that starts "東京に来たら、屯に行ってみる。" write "If you are ever in Tokyo, visit Tamuro." and continue faithfully.

OUTPUT
Return only the translated Markdown of the passage you are given. No preface, no notes, no code fence around it."""


def user_prompt(slug, idx, total, chunk):
    return f"This is passage {idx} of {total} of the book. Translate it.\n\n<passage>\n{chunk}\n</passage>"


def cmd_prepare():
    for slug in BOOKS:
        d = out_dir(slug); (d / 'work').mkdir(parents=True, exist_ok=True)
        src = prepare_source(slug)
        (d / 'work/source.ja.md').write_text(src)
        chunks = split_chunks(src)
        (d / 'work/chunks.json').write_text(json.dumps(chunks, ensure_ascii=False, indent=1))
        print(slug, '原稿', len(src), '字', '→', len(chunks), '節の束', [len(c) for c in chunks])


# ───────── バッチ ─────────
def client():
    import anthropic
    return anthropic.Anthropic(api_key=env_key())


def params_for(slug, text, idx, total, sysmsg):
    return dict(model=MODEL, max_tokens=MAX_TOKENS, system=sysmsg,
                output_config={'effort': 'low'},
                messages=[{'role': 'user', 'content': user_prompt(slug, idx, total, text)}])


def cmd_submit(slugs):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    c = client()
    reqs = []
    for slug in slugs:
        chunks = json.loads((out_dir(slug) / 'work/chunks.json').read_text())
        sysmsg = system_prompt(slug)
        for i, ch in enumerate(chunks, 1):
            reqs.append(Request(custom_id=f'{slug}-{i:02d}', params=MessageCreateParamsNonStreaming(**params_for(slug, ch, i, len(chunks), sysmsg))))
    b = c.messages.batches.create(requests=reqs)
    pathlib.Path(ROOT / f'i18n/{LG}/work-batch.json').write_text(json.dumps({'id': b.id, 'slugs': slugs, 'n': len(reqs)}))
    print('batch', b.id, len(reqs), '件')


def cmd_status():
    info = json.loads((ROOT / f'i18n/{LG}/work-batch.json').read_text())
    b = client().messages.batches.retrieve(info['id'])
    print(b.processing_status, b.request_counts)


# ───────── 後処理 ─────────
def yen_to_usd(t):
    def usd(v):
        d = v / RATE
        if d < 1:
            s = f'{d:.2f}'
        elif d < 10:
            s = f'{d:.1f}'.rstrip('0').rstrip('.')
        else:
            n = len(str(int(d)))
            q = 10 ** max(n - 2, 0)
            s = f'{int(round(d / q) * q):,}'
        return s
    n = r'(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?![\d,]*\d)'
    pat = re.compile(r'¥(' + n + r')\s*[–—-]\s*¥(' + n + r')(?! \(about \$)|¥(' + n + r')(?!\s*[–—-]\s*¥\d)(?! \(about \$)')
    def rep(m):
        if m.group(3) is None:
            a = float(m.group(1).replace(',', '')); b = float(m.group(2).replace(',', ''))
            return f'{m.group(0)} (about ${usd(a)}–${usd(b)})'
        return f'{m.group(0)} (about ${usd(float(m.group(3).replace(",", "")))})'
    return pat.sub(rep, t)


def post(t):
    t = re.sub(r'\s*⟦(.+?)⟧', r' *(\1)*', t, flags=re.S)
    # 画像の行の後ろに付いた画面の注は消す（キャプションの行だけに付ける）
    t = re.sub(r'^(!\[.*\]\([^)]*\)) \*\(The screen is in Japanese\.\)\*', r'\1', t, flags=re.M)
    t = t.replace('\u3000', ' ').replace('／', ' / ')
    seen, res = set(), []
    for part in re.split(r'( \*\(.+?\)\*)', t, flags=re.S):
        if part.startswith(' *(') and part.endswith(')*'):
            k = re.sub(r'\W+', '', part.lower())
            if k in seen and any(n['note'] in part for n in GLOSS['standard_notes']):
                continue
            seen.add(k)
        res.append(part)
    t = ''.join(res)
    t = yen_to_usd(t)
    return t


def cmd_collect():
    info = json.loads((ROOT / f'i18n/{LG}/work-batch.json').read_text())
    c = client()
    b = c.messages.batches.retrieve(info['id'])
    if b.processing_status != 'ended':
        sys.exit(f'まだ {b.processing_status}')
    usage = {}
    bad = []
    for r in c.messages.batches.results(info['id']):
        cid = r.custom_id; slug = cid.rsplit('-', 1)[0]
        if r.result.type != 'succeeded':
            bad.append((cid, r.result.type)); continue
        msg = r.result.message
        text = ''.join(bk.text for bk in msg.content if bk.type == 'text')
        d = out_dir(slug) / 'work/raw'; d.mkdir(parents=True, exist_ok=True)
        (d / f'{cid}.md').write_text(text)
        u = usage.setdefault(slug, dict(i=0, o=0))
        u['i'] += msg.usage.input_tokens; u['o'] += msg.usage.output_tokens
        if msg.stop_reason != 'end_turn':
            bad.append((cid, msg.stop_reason))
    (ROOT / f'i18n/{LG}/work-usage.json').write_text(json.dumps(usage))
    print('usage', usage, 'bad', bad)
    assemble()


def titles():
    out = {}
    for slug in BOOKS:
        m = json.loads((out_dir(slug) / 'work/meta.json').read_text())
        out[slug] = m['titles'][0]
    return out


def finalize(slug, t):
    """本どうしの参照の題名を、決めた英題にそろえる（訳の途中で作られた仮の題名を置き換える）。"""
    T = titles()
    other = 'hitori-de-mise' if slug == 'uchi-no-mise' else 'uchi-no-mise'
    # 「前作／2冊目」の題名：*…* の斜体（直後に『…』が付いていれば一緒に消す）
    pat = r'\*(?:Running|Our|The Shop)[^*]{3,80}\*(?:\s*\(『[^』]*』\))?' if slug == 'uchi-no-mise' else r'\*(?:Our|Running)[^*]{3,80}\*(?:\s*\(『[^』]*』\))?'
    if slug == 'uchi-no-mise':
        t = re.sub(r'\*Running[^*]{3,80}\*(?:\s*\(『[^』]*』\))?', '*' + T['hitori-de-mise']['title'] + '*', t)
    else:
        t = re.sub(r'\*Our [^*]{3,80}\*(?:\s*\(『[^』]*』\))?', '*' + T['uchi-no-mise']['title'] + '*', t)
    # 日本語の題名が残ったとき（『…』）は英題にする
    t = t.replace('『うちの店は、うちの仕様で』', '*' + T['uchi-no-mise']['title'] + '*').replace('『一人で店を回す、その横にAIが来た。』', '*' + T['hitori-de-mise']['title'] + '*')
    # 2冊目の冒頭（題名と副題）は決めた英題にする
    if slug == 'uchi-no-mise':
        t = re.sub(r'\A# [^\n]*\n\n[^\n]*\n', '# ' + T[slug]['title'] + '\n\n' + T[slug]['subtitle'] + '\n', t)
    t = re.sub(r'^the Agenda series:', 'The Agenda series:', t, flags=re.M)
    # 性別が原文に無い人物の代名詞（実在の人物の発言を引く箇所）
    for a, b in [('something he got into this year', 'something they got into this year'), ('His reasoning:', 'The reasoning:')]:
        t = t.replace(a, b)
    return t


def assemble():
    for slug in BOOKS:
        d = out_dir(slug)
        n = len(json.loads((d / 'work/chunks.json').read_text()))
        parts = []
        for i in range(1, n + 1):
            f = d / f'work/raw/{slug}-{i:02d}.md'
            if not f.exists():
                print('欠け', f.name); parts = None; break
            parts.append(f.read_text().strip('\n'))
        if parts is None:
            continue
        (d / 'manuscript.md').write_text(finalize(slug, post('\n\n'.join(parts))) + '\n')
        print('組んだ', slug, d / 'manuscript.md')


def cmd_retry(ids):
    c = client()
    for cid in ids:
        slug = cid.rsplit('-', 1)[0]; i = int(cid.rsplit('-', 1)[1])
        chunks = json.loads((out_dir(slug) / 'work/chunks.json').read_text())
        with c.messages.stream(**params_for(slug, chunks[i - 1], i, len(chunks), system_prompt(slug))) as s:
            m = s.get_final_message()
        text = ''.join(bk.text for bk in m.content if bk.type == 'text')
        (out_dir(slug) / f'work/raw/{cid}.md').write_text(text)
        print(cid, m.stop_reason, m.usage.input_tokens, m.usage.output_tokens)
    assemble()


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'prepare': cmd_prepare()
    elif cmd == 'submit': cmd_submit(sys.argv[2:] or list(BOOKS))
    elif cmd == 'status': cmd_status()
    elif cmd == 'collect': cmd_collect()
    elif cmd == 'retry': cmd_retry(sys.argv[2:])
