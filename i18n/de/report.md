# ドイツ語版（de）報告

## 状態
- 本1・本2とも、翻訳・レビュー反映・表紙・組版（PDF／Google Play 用 EPUB／Kindle 用 EPUB）・ストア文言まで完了。
- `I18N_LANG=de gate.py`：NG 0。epubcheck エラー0（4本とも）。表紙の題名・副題・著者名の OCR 照合 100%（de-DE）。
- Google Play：本1・本2とも新規。Kindle：可（lang.json の kindle=true。KDP はドイツ語対応）。
- PDF ページ数：本1＝100、本2＝118。

## 題名（案3つ）。既定は1案目。実践ガイド型への変更は代表が決める
- 本1：①『Die KI-Stellvertretung』（既定。副題「Einfach sprechen, den Rest erledigt die KI. Mehr, als Sie denken.」）／②『Allein im Lokal, und neben mir die KI』（日本語題の直訳に近い）／③『KI für kleine Betriebe: Der Praxisleitfaden für Gastronomie und Selbstständige』（実践ガイド型）
- 本2：①『Gebaut für unsere Bar』（既定。副題「Aufzeichnungen aus einer Bar mit 19 Plätzen: vom Reservierungssystem bis zu eigenen Werkzeugen, alles mit KI selbst gebaut」）／②『Unser Lokal, unsere Vorgaben』／③『Eigene Werkzeuge für kleine Betriebe: Der Praxisleitfaden zum Selbstbauen mit KI』
- 相互参照の題名は *Die KI-Stellvertretung*／*Gebaut für unsere Bar* にそろえてある。

## 決めたこと
- 敬称：Sie（読者への呼びかけ）。例外は、著者が AI に打ち込む指示文・AI との会話（du）。文体は一人称 ich の語り（work/style.md に記録）。
- 人物・職業は中立（Lokalleitung、Team、Gäste、Mitarbeitende、die Person）。総称男性・Gender-Stern は不使用。性別語への書き換え指摘は不採用。
- 数字：dot（¥8.500／ca. $57／12,5%）。書体：Baskerville／Georgia。特記（右から左・縦書き）なし。図：Abbildung。目次：Inhaltsverzeichnis。奥付：Impressum。
- 手帳の名前（辞書 de.ts）：Zeiterfassung（Timbro）、Rentabilität（Oro）、Zweites-Lokal-Heft（Bis）、Hilfe-Center（QA）、Licht-Notizbuch（Luce）、Gesprächsthemen（Spunto）、Voce。窓の案：Wareneinsatz-Heft（Ricetta）、Stammgast-Heft（Nera）、Dienstplan-Heft（Turno）。
- 副店長＝stellvertretende Lokalleitung（短く Stellvertretung）。Vibe Coding、Tamuro、Raku Bonta、Bonta LLC。リンクの印：b1-de／b2-de。

## 成果物の場所（/Users/keikawaguchi/AntiGravity/AgendaLibro/i18n/de/ 配下。slug＝hitori-de-mise／uchi-no-mise）
- 題名・書誌：<slug>/metadata.yaml
- 原稿：<slug>/manuscript.md（部品 <slug>/work/part-*.md）
- 説明文・一行紹介・キーワード・ジャンル・Kindle カテゴリ：<slug>/work/store.json（一行紹介160字以内、説明文 本1＝212語・本2＝205語）
- 表紙：<slug>/cover/cover.png
- PDF：hitori-de-mise/build/bontaraku-01_hitori-de-mise_de.pdf、uchi-no-mise/build/bontaraku-02_uchi-no-mise_de.pdf
- EPUB：<slug>/build/*_de_gp.epub（Google Play）、*_de_kindle.epub（Kindle）
- ストア用の1枚：store-copy.part.html。用語集 glossary.add.yaml、設定 lang.json、文体 work/style.md

## レビュー（agy／Gemini。API への切替は不要）
- 本1：指摘163件 → 採用144件（一部採用含む）・不採用19件。本2：指摘207件 → 採用189件・不採用18件。未対応0、未レビューの章なし。記録：<slug>/review-log.md
- 主に採った指摘：意味の取り違え（早割条件の逆転、「今夜空いてる？」の文脈、nicht einmal korrigiert の逆転、Kurs→Menü）、ハンバーグ→Hacksteak、「尖る」の訳の統一、wir→ich、不自然な語の言い換え。
- 不採用：性別語への書き換え、製品の呼び名の変更、Sie→du、原文にない補足、金額・訳注・題名への指摘。

## 費用
- 翻訳・反映：サブスクの枠（サブエージェント並列。Anthropic API 不使用）。レビュー：agy のみ。

## 親への依頼・気づいた点
- books/store-copy.html への store-copy.part.html の取り込み。
- 共有スクラッチパッドで他セッション（ヒンディー語とみられる）と一時スクリプト名（rep.py、p1.py〜p3.py）が衝突し、こちらの反映担当が上書きした可能性あり。他言語の作業物の確認を。
- <slug>/build/.tmp/ は組版の中間物として残っている（削除していない）。
- Hub：言語コード de、name＝Deutsch、ja_name＝ドイツ語、Kindle 対応あり、リンクの印 b1-de／b2-de、手帳の名前は上記。

## 追記 2026-10-31
本1から「紹介制」の表現を代表の指示で削除（8か所。source.ja.md・work/part-*.md・manuscript.md を修正し、再組版）。屯が今は予約なしで入れる旨は残した。
