"""note 記事の md に、PDF の導線を足す（代表承認 2026-10-28）。何度流しても同じ結果になる。
  python3 scripts/note-links-patch.py
- 冒頭（題名・本文の最初の行の上）：この本は PDF でも無料で読めます（再配布自由）→ <PDF>
- 末尾「この本の、ほかの読み方」の先頭：PDF・Kindle・Google Play・本のページ（URL単独の行＝リンクカード）・再配布の一文
- 「出版の経緯」（b-keii.md）：末尾に本の一覧のリンク
"""
import re, pathlib
BOOKS = {
    'hitori-de-mise': dict(
        slugs=['intro', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ep'],
        kindle='https://www.amazon.co.jp/dp/B0GFY4WW4Y',
        gplay='https://play.google.com/store/books/details?id=4dUiEgAAQBAJ'),
    'uchi-no-mise': dict(
        slugs=['a-hajimeni', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ep'],
        kindle='https://www.amazon.co.jp/dp/B0HPJY4NRR',
        gplay='https://play.google.com/store/books/details?id=WdUiEgAAQBAJ'),
}
PRICE = 'この本は note・PDF・Google Play で無料で読めます。Kindle 版のみ 99円です。'
SENT = 'PDF は再配布自由です。周りの店主仲間や、AI に興味のある方に、そのまま送ってください。'
for slug, c in BOOKS.items():
    pdf = f'https://bontallc.com/books/{slug}/pdf?via=note'
    page = f'https://bontallc.com/books/{slug}?via=note'
    top = f'この本は PDF・Google Play でも無料で読めます（PDF は再配布自由）→ [{pdf}]({pdf})'
    lines = [PRICE, f'PDF（無料・再配布自由）：[{pdf}]({pdf})', f'Google Play（無料）：[{c["gplay"]}]({c["gplay"]})', f'Kindle（99円）：[{c["kindle"]}]({c["kindle"]})']
    lines += ['本のページ：', page, SENT]
    foot = '\n\n'.join(lines)
    for s in c['slugs']:
        p = pathlib.Path(f'books/{slug}/note/{s}.md')
        t = p.read_text()
        # 古い版（このスクリプトが前に入れた分）を除いてから入れ直す
        t = re.sub(r'^この本は PDF(・Google Play)? でも無料で読めます.*\n\n', '', t, flags=re.M)
        head, rest = t.split('\n\n', 1)
        t = head + '\n\n' + top + '\n\n' + rest
        marker = '## この本の、ほかの読み方\n\n'
        i = t.index(marker) + len(marker)
        j = t.index('\n\n', t.index('屯の予約サイト：', i) - 1) if False else None
        # 既存の入れ込みを除く：marker の直後から「屯の予約サイト：」の手前まで（Kindle 行は1冊目の既存行なので含めて入れ直す）
        k = t.index('屯の予約サイト：', i)
        t = t[:i] + foot + '\n\n' + t[k:]
        p.write_text(t)
p = pathlib.Path('books/uchi-no-mise/note/b-keii.md')
t = p.read_text()
if 'bontallc.com/books?via=note' not in t:
    t = t.rstrip('\n') + '\n\n本の一覧：\n\nhttps://bontallc.com/books?via=note\n'
    # 署名の位置：署名「本多楽」を最後に残す
    t = t.replace('\n\n本多楽\n\n本の一覧：', '\n\n本の一覧：') if False else t
p.write_text(t)
