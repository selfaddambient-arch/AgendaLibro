"""レビューの材料を作る（章ごと・長い章は番号を付けて分ける）。
  python3 scripts/i18n/review.py
出力：i18n/en/<slug>/review/<NN>-<章>[-<部>].md と、返事の置き場の空ファイル .gemini.md／.chatgpt.md
分ける基準：日本語の原文が PART_MAX 字を超えるとき、### の見出しの境目で分ける（日本語＋英訳を合わせて約3万字以内に収める）。
"""
import re, json, pathlib
import os
LG = os.environ.get('I18N_LANG', 'en')   # 言語コード（2文字）。i18n/<言語>/ を使う
ROOT = pathlib.Path(__file__).resolve().parents[2]
import os, json as _j
LG = os.environ.get('I18N_LANG', 'en')
_L = _j.load(open(ROOT / f'i18n/{LG}/lang.json'))
LNAME = _L['name']
PART_MAX = 6500
ASK = '次は日本語の本の一章と、その英訳です。英訳について、①意味の取り違え ②不自然な英語 ③英語圏の読者に伝わらない箇所 を、該当する英文の引用と直す案の形で一覧にしてください。書き直した全文は不要です。'
if LG != 'en':
    ASK = ASK.replace('英訳', _L['ja_name'] + '訳')
BOOKS = {'hitori-de-mise': '『一人で店を回す、その横にAIが来た。』', 'uchi-no-mise': '『うちの店は、うちの仕様で』'}


def split_h(t, level):
    pat = re.compile(r'^' + '#' * level + r' ', re.M)
    idx = [m.start() for m in pat.finditer(t)]
    if not idx: return [t]
    segs = ([t[:idx[0]]] if t[:idx[0]].strip() else []) + [t[a:b] for a, b in zip(idx, idx[1:] + [len(t)])]
    return segs


def parts_of(ja, en):
    """章（## 単位）の JA と EN を、### 単位で揃えて PART_MAX 以内の部に束ねる。"""
    js, es = split_h(ja, 3), split_h(en, 3)
    if len(js) != len(es):
        return [(ja, en)]
    out, bj, be = [], '', ''
    for j, e in zip(js, es):
        if bj and len(bj) + len(j) > PART_MAX:
            out.append((bj, be)); bj, be = '', ''
        bj += j; be += e
    if bj: out.append((bj, be))
    if len(out) > 1 and len(out[-1][0]) < 1500:
        out[-2] = (out[-2][0] + out[-1][0], out[-2][1] + out[-1][1]); out.pop()
    return out


def main():
    summary = {}
    for slug, title in BOOKS.items():
        d = ROOT / f'i18n/{LG}/{slug}'
        ja = (d / 'work/source.ja.md').read_text(); en = (d / 'manuscript.md').read_text()
        jc, ec = split_h(ja, 2), split_h(en, 2)
        assert len(jc) == len(ec), (slug, len(jc), len(ec))
        # 先頭の見出し前の断片（表紙まわり）は次の章に付ける
        if not jc[0].startswith('## '):
            jc[1] = jc[0] + jc[1]; ec[1] = ec[0] + ec[1]; jc, ec = jc[1:], ec[1:]
        rd = d / 'review'; rd.mkdir(exist_ok=True)
        files = []
        for n, (cj, ce) in enumerate(zip(jc, ec)):
            head_ja = re.search(r'^## (.*)$', cj, flags=re.M).group(1)
            head_en = re.search(r'^## (.*)$', ce, flags=re.M).group(1)
            parts = parts_of(cj, ce)
            for k, (pj, pe) in enumerate(parts, 1):
                name = f'{n:02d}' + (f'-{k}' if len(parts) > 1 else '')
                label = f'{n:02d}' + (f' part {k} of {len(parts)}' if len(parts) > 1 else '')
                body = (f'{ASK}\n\n---\n\n（本：{title}／{head_ja}'
                        + (f'／{k}/{len(parts)}' if len(parts) > 1 else '') + '）\n\n'
                        f'# 日本語の原文\n\n{pj.strip()}\n\n---\n\n# {LNAME} translation\n\n{pe.strip()}\n')
                (rd / f'{name}.md').write_text(body)
                for who in ('gemini', 'chatgpt'):
                    f = rd / f'{name}.{who}.md'
                    if not f.exists(): f.write_text('')
                files.append((name, head_ja, len(pj), len(body)))
        summary[slug] = files
    for slug, fs in summary.items():
        print(slug, len(fs), '本')
        for f in fs: print('  ', f)
    (ROOT / f'i18n/{LG}/work-review.json').write_text(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
