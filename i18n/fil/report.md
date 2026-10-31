# フィリピン語（fil）報告

（サブエージェントの返答から親の窓が作成）

## 状態
- 翻訳、agy レビュー、反映、表紙、PDF、Google Play 用 EPUB、ストア文言まで完了。
- gate.py（I18N_LANG=fil）NG 0。epubcheck は両 EPUB ともエラー0。
- Google Play は本1・本2とも新規。Kindle は非対応（kindle=false、Kindle 用 EPUB なし）。
- PDF：本1が101ページ、本2が120ページ。
- OCR 非対応のため表紙・PDF（表紙・目次・図ページ・奥付）を画像で目視確認。文字化け・はみ出しなし。

## 題名の案（既定は1案目）
- 本1：①Ang AI Assistant Manager（副題：Kausapin lang ninyo, at siya na ang gagawa. Mas higit pa sa inaasahan ninyo.）／②Mag-isa sa Tindahan, May AI sa Tabi Ko／③Gabay ng May-ari ng Maliit na Negosyo sa Paggamit ng AI
- 本2：①Gawa para sa Aming Bar（副題：Ang kuwento ng may-ari ng bar na may 19 na upuan na gumawa ng lahat, mula reservation hanggang mga tool, gamit ang AI）／②Ang Aming Tindahan, Ayon sa Aming Sariling Disenyo／③Gumawa ng Sarili Ninyong Sistema gamit ang AI: Gabay para sa mga May-ari ng Maliit na Negosyo
- 既定を実践ガイド型に変えるかは代表の判断。

## 口調・用語・数字・書体
- 標準フィリピン語の丁寧な書き言葉。語り手 ako、読者 kayo/ninyo。po は多用しない。shop・staff・reservation・system などは英語のまま。本2の tindahan は雑貨店を連想させるため shop に統一。
- 手帳の名前（辞書）：Talaan ng Oras、Talaan ng Kita、Gabay sa Susunod na Tambayan、Gabay sa Suporta、Talaan ng Ilaw、Tala ng Usapan。窓の案（辞書に無い3つ）：Talaan ng Gastos sa Resipe、Talaan ng mga Suki、Talaan ng Duty。
- 副店長＝assistant manager、屯＝Tamuro、図＝Larawan、コラム＝Kolum、はじめに＝Panimula、おわりに＝Pangwakas。手帳を説明する箇所は planner app。
- 数字は英語式。円は `¥8,500 (humigit-kumulang $57)`。書体 Baskerville, Georgia, Times New Roman。

## レビュー（agy）
- 全章に返事あり、API 切替なし。指摘計390件（本1が173、本2が217）、採用 本1:145／本2:179、不採用 28／38、未対応0。全件を `*/review-log.md` に記録。
- 主な採用：「空き枠」を営業時間と訳した箇所、「ノリで」「送客」の取り違え、ipapatay（殺させる）の重大誤訳、不適切な連想の語（Labasan・katulong など）の置換。
- 主な不採用：伏せ字 ○○0,000 yen の変更、PDCA への補足追加、namin の単数化、合言葉の日本語化。
- 費用：Anthropic API・Gemini API とも不使用（サブスク枠）。

## 親への依頼・気づいた点
1. **リンクの印は `tl`（代表確定。旧 fil）**（`b1-tl-pdf/gp`、`b2-tl-pdf/gp`）。決まりは「言語2文字」なので、**代表判断が必要**（2文字にすると fi＝フィンランド語と紛らわしい。ph なども案）。gate.py は3文字を許す。init-lang.py の2文字限定の検査は、親の窓が 2〜3 文字に直した。
2. OCR 非対応のため gate の表紙文字照合は働かない（目視で確認）。
3. 作業中に作った `i18n/_fil_init.tmp.py` は削除済み。

## Hub への引き渡し
- `i18n/fil/`：`lang.json`、`glossary.add.yaml`、`work/style.md`、`store-copy.part.html`、`<slug>/metadata.yaml`、`<slug>/work/store.json`、`<slug>/cover/cover.png`、`<slug>/build/bontaraku-0{1,2}_*_fil.pdf`、`*_fil_gp.epub`、`<slug>/manuscript.md`、`<slug>/review-log.md`。

- 2026-10-31：本1から「紹介制」の表現を削除（代表の指示）。再組版し、gate は NG 0、PDF は 101 ページ。

- 2026-10-31 リンクの印を代表確定の値に差し替えて作り直した（zh-CN: cn→zh、fil: fil→tl）。原稿・lang.json・report を更新し、PDF・EPUB を再組版。gate NG 0・epubcheck エラー0。
