# イタリア語（it）報告

（サブエージェントの返答から親の窓が作成）

## 状態
- 翻訳、レビュー反映、表紙、組版（PDF・Google Play 用 EPUB・Kindle 用 EPUB）、ストア文言まで完了。
- gate.py（I18N_LANG=it）NG 0、epubcheck エラー0。表紙の題名・副題・著者名は Apple Vision（it-IT）で100%一致。
- PDF：本1が98ページ、本2が111ページ。
- Google Play は本1・本2とも新規。Kindle は対応（kindle=true、Kindle 用 EPUB 作成済み）。

## 題名の案（既定は1案目）
- 本1：①Il vice responsabile IA（副題：Basta parlare, e l'IA lo fa. Molto più di quanto immaginassi.）／②Il locale lo gestisco da solo, e l'IA è arrivata al mio fianco／③Guida pratica all'IA per chi gestisce un locale senza altro aiuto
- 本2：①Costruito per il nostro bar（副題：Come il titolare di un bar da 19 posti ha costruito con l'IA tutto, dalle prenotazioni agli strumenti）／②Il nostro locale, con le nostre specifiche／③Guida per costruire con l'IA il proprio sistema di prenotazione, per chi ha un bar
- 既定を実践ガイド型に変えるかは代表の判断。

## 文体・用語
- 読者へは Lei。筆者・店主・実在の人物に性別を示す語は使わない。数字は dot（¥8.500）。書体 Baskerville。
- 手帳の名前（辞書）：Timbrature、Redditività、Guida al Secondo Locale、Guida al Supporto、Taccuino della Luce、Spunti di Conversazione。窓の案（辞書に無い3つ）：Taccuino dei Costi、Taccuino dei Clienti Abituali、Taccuino dei Turni。
- 副店長＝vice responsabile、コラム＝Rubrica、おわりに＝Postfazione、「今夜空いてる？」＝「C'è posto da Tamuro stasera?」。

## レビュー
- agy は3章で止め、残りは review-api.mjs（Gemini API）に切替。指摘は本1約60件・本2約50件、不採用は約8件・約6件、未対応0。全件を `*/review-log.md` に記録。
- 費用：翻訳は API 不使用。Gemini API は入力約10万・出力約1.4万トークン（数円）。

## 親への依頼・気づいた点
1. サブエージェントが一度 `I18N_LANG` を付けずに build.mjs を走らせ、`i18n/en/*/build/` が作り直された。原稿は同じで、en の gate は NG 0 のまま。git 上は en の build が M になっているが、コミットには入れていない（戻すなら git restore は代表の承認が要る）。
2. 共有 venv（scratchpad/venv）が壊れて yaml が無くなっていた（原因不明）。scratchpad/venv-it を代わりに使用。
3. 本1 2-7 の `[Cmd]+[Shift]+[4]` はそのままではクリップボードに入らない（代表の裁定どおり原文のまま）。zh-CN で既出の確認事項。
4. 本2 3-1「Luce は、イタリア語で『灯り』」はイタリア語読者には同語反復（原文のまま訳した）。言い回しを変えるかは判断。
5. Hub の BOOK_SRC_ALLOWLIST・屯の FUNNEL_SRC_ALLOWLIST に `b1-it-*`／`b2-it-*` の追記が必要（親の仕事）。

## Hub への引き渡し
- 印：`b1-it-pdf／-gp／-kindle`、`b2-it-pdf／-gp／-kindle`。
- `i18n/it/`：`lang.json`、`glossary.add.yaml`、`store-copy.part.html`、`<slug>/metadata.yaml`、`<slug>/work/store.json`（one_liner・description・keywords・gp_genres・kindle_categories。説明文 本1:218語／本2:219語）、`<slug>/cover/cover.png`、`<slug>/build/*_it.pdf`・`*_it_gp.epub`・`*_it_kindle.epub`、`<slug>/manuscript.md`、`<slug>/review-log.md`。
