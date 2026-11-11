# 2027年カレンダー紹介シリーズ（note）の作り方

1. `designs.py`（デザインごとの紹介文）と `gen.py` で、各回の原稿 `NN/article.md` と見本画像を作る（見本は AgendaHub の `public/cal/images`、/cal と同じもの）。
2. `node scripts/note-series-header.mjs NN` で見出し画像（1280×670）を作り、`node scripts/note-article.mjs --article …/NN/article.md --header …/NN/header.png` で note に下書きを作る（`--url <編集URL>` を付けると既存の記事を原稿から作り直す）。
3. 公開は `NOMAG=1 KEY=<記事キー> TAGS='[…]' node scripts/note-publish.mjs x`。公開前に、リンクが全部 200 で開くこと、`?design=` が番号だけ（`design=14`）で選ばれるデザインと一致することを確かめる。
4. 全回の公開後に `scripts/note-magazine-new.mjs` でマガジンを作り、`scripts/note-series-links.mjs` で他の回とマガジンへのリンクを足し、`MAGAZINE='<マガジン名>' … note-publish.mjs x --update` で公開してマガジンに入れる。並びは `並び替え・削除` で直す。
5. 実際の写真を足すときは `scripts/note-series-photo.mjs`、崩れた段落の貼り直しは `scripts/note-series-photo-fix.mjs`（段落の途中への貼り付けは前後の段落と混ざる。段落ごと貼り替える）。

注意：公開済みの記事の本文を全選択（Ctrl+A）して上書きしない。下書きが自動保存され、本文がすべて消える。直すときは対象の段落だけを選んで貼り替える。
