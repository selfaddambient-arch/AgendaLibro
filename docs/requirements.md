# AgendaLibro（出版手帳）要件

本の組版と配信を担う製品。1冊目は『うちの店は、うちの仕様で』。

## 命名規則

原稿は `著者-巻数_本の略名_manuscript.md`（例：`bontaraku-02_uchi-no-mise_manuscript.md`）。
組版・note・検査のすべてでこの名前を参照する。以後の本も同じ型にそろえる。

## 今回やったこと

- リポジトリの土台（books/・scripts/・secrets/・docs/・i18n/）
- 原稿と挿絵の取り込み（旧 ~/AntiGravity/Books から、ファイル数・ハッシュ一致を確認して移行）
- EPUB3（横書き・リフロー・書体埋め込みなし）と PDF（A5・QR3つ）の組版
- note への接続（ログイン状態の保存）と、下書き2本の保存

## 今回やらないこと

- 翻訳・翻案（置き場 i18n/ だけ作る）
- Kindle（KDP）・Google Play への登録
- note の公開操作（下書き保存まで）
- product-bootstrap／agy 委譲：本リポジトリは Goal 指定の構成で立ち上げた。src/・app/・lib/ を持たない

## 将来

- 翻訳・翻案（i18n/<言語>/ に原稿を置く）
- KDP・Google Play 登録（必要なものは build/../report.md）
- 2冊目以降の本の追加（books/<略名>/）
