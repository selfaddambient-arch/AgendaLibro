"""英題の案（各書3つ）・副題・ストア用の説明文・LP 用の説明文・一行紹介を作る（Claude Sonnet 5.5・同期の呼び出し1回ずつ）。
  python3 scripts/i18n/meta.py            → i18n/en/<slug>/work/meta.json
原文の事実だけを使う。LP の既存の説明文（Hub の content/books/<slug>/ja.json）を材料にする。
"""
import sys, json, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import translate as T

HUB = pathlib.Path.home() / 'AntiGravity/AgendaHub/content/books'
SYS = """You are a book marketing editor and translator (Japanese to English). From the Japanese book information below, write the English edition's metadata. Use only facts present in the material; never invent numbers, features or claims. Voice: warm, plain, honest, a little understated.
Do not use gendered pronouns (he, she, his, her) for the author; write "the owner", "the author", or use "they", or rephrase. The book itself is written in the first person.
Return ONLY a JSON object with these keys:
- "titles": array of exactly 3 objects {"title":..., "subtitle":..., "note":...}. The first is your recommended default. Titles should work for English readers, keep the spirit of the Japanese title, and not be longer than 70 characters. "note" is one short line on how it differs.
- "one_liner": one sentence, 160 characters at most, for the store listing and LP.
- "store_description": 150-220 words of plain text for Kindle and Google Play (no markdown; short paragraphs separated by a blank line). Mention that it is free to read (PDF, note, Google Play) and that the Kindle edition has a minimum price set by the store, only if the material says so.
- "lp_description": array of 4 to 5 short paragraphs (strings) for the book's landing page, mirroring the Japanese landing-page description.
- "keywords": array of 7 search keywords for the store listing."""


def one(slug):
    d = T.out_dir(slug)
    ja = json.loads((HUB / slug / 'ja.json').read_text())
    intro = (d / 'work/source.ja.md').read_text()
    heads = '\n'.join(l for l in intro.split('\n') if l.startswith('## ') or l.startswith('### '))[:6000]
    ctx = f"Japanese title: {ja['title']}\nSubtitle: {ja['subtitle']}\nAuthor: 本多楽 (Raku Bonta)\nOne-liner (ja): {ja['oneLiner']}\nLanding-page description (ja):\n" + '\n'.join(ja['description']) + f"\n\nTable of contents (ja):\n{heads}\n\nGlossary: 屯 = Tamuro; Agenda series; T-AI-MURO."
    if slug == 'hitori-de-mise':
        ctx += "\nThis is book 1. Book 2 is 'うちの店は、うちの仕様で'."
    c = T.client()
    with c.messages.stream(model=T.MODEL, max_tokens=8000, system=SYS, output_config={'effort': 'low'},
                           messages=[{'role': 'user', 'content': ctx}]) as s:
        m = s.get_final_message()
    txt = ''.join(b.text for b in m.content if b.type == 'text')
    j = json.loads(re.search(r'\{.*\}', txt, flags=re.S).group(0))
    (d / 'work/meta.json').write_text(json.dumps(j, ensure_ascii=False, indent=1))
    print(slug, m.usage.input_tokens, m.usage.output_tokens, [t['title'] for t in j['titles']])
    return m.usage.input_tokens, m.usage.output_tokens


if __name__ == '__main__':
    tot = [0, 0]
    for s in T.BOOKS:
        a, b = one(s); tot[0] += a; tot[1] += b
    print('usage', tot)
