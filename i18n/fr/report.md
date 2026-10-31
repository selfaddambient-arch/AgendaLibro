# フランス語（fr）報告

（サブエージェントの返答から親の窓が作成）

## 状態
- 翻訳、Gemini レビュー反映、表紙、組版（PDF・Google Play 用 EPUB・Kindle 用 EPUB）、ストア文言まで完了。
- gate.py（I18N_LANG=fr）NG 0。epubcheck は4本ともエラー0。表紙の題名・副題・著者名は OCR（fr-FR）で一致100%。
- PDF：本1が99ページ、本2が115ページ。
- Google Play は本1・本2とも新規。Kindle は対応（kindle=true、Kindle 用 EPUB は2冊とも作成）。

## 題名の案（既定は1案目）
- 本1：①L'adjoint IA（副題：Il suffit de lui parler, l'IA s'occupe du reste. Bien plus que je ne l'imaginais.）／②Un commerce en solo, et l'IA à mes côtés／③L'IA pour les petits commerces : guide pratique pour restaurateurs indépendants
- 本2：①Sur mesure pour notre bar（副題：Comment un bar de 19 places a tout construit avec l'IA, des réservations aux outils）／②Notre bar, nos règles／③Créer ses propres outils avec l'IA : guide pratique pour un bar ou un restaurant
- 既定を実践ガイド型に変えるかは代表の判断。本文中の相互参照は既定題名にそろえてある。

## 決めたこと
- 文体：読者へは vous、著者は je（`work/style.md`）。人物は「la clientèle」「la direction」「la personne」「on」など。性別を示す言い換え（patron／il／traductrice）は不採用。
- 数字：千の位は空白、小数はコンマ。¥ と $ は数字の前。円は4桁以内のため `¥8500 (environ $57)`。5桁以上は不可分スペース。
- 記号：引用符は « »、`: ; ! ?` の前と « » の内側は不可分スペース。アポストロフィは ASCII。
- 書体：'Baskerville','Georgia','Times New Roman',serif。
- 語：Figure、Table des matières、Encadré、Postface、adjoint（初出 adjoint de direction）、屯＝Tamuro。
- 手帳の名前（辞書）：Pointages、Rentabilité、Guide de la Prochaine Étape、Guide d'assistance、Carnet de Lumière、Sujets de conversation、Voce。窓の案（辞書に無い3つ）：Prix de revient、Carnet des habitués、Planning d'équipe。

## レビュー（agy／Gemini）
- 全章を agy で回し、Gemini API への切替なし。未対応0。全点の採否を `*/review-log.md` に記録（本1：195点中 採用161・不採用34、本2：189点中 採用174・不採用15）。
- 不採用：原文にない補足（LINE・APPI・note）の追加、性別語への言い換え、題名の直訳への戻し、Postface への「Hon o mita」追加。
- 費用：Anthropic API・Gemini API とも不使用（サブスク枠）。

## 親への依頼・気づいた点
1. gate.py の円の米ドル併記の検査（`YEN` 正規表現）が、number_style=space で千の位が空白のとき（`¥8 500`）、「¥8」だけに一致して誤って NG になる。今回は金額が4桁以内で回避。空白区切りの言語（it・tr・ru が候補）の前に修正が必要。
2. 本1 第3章（03-1 付近）：原文が「人と動物が」シャム猫に置き換わると書いていて直前と矛盾して読める。仏訳は「le chien」だけが置き換わる形にした。原文側の確認を。
3. 本1 第2章の Mac ショートカット併記は日本語原文に無く英語版にある。fr も英語版に合わせて残した（既出の 2-7 の確認事項と同じ）。
4. 画像の alt は fr ではフランス語（英語版は英語のまま）。
5. 本1の「12月」「先月」に年は足していない（英語版に合わせた）。

## Hub への引き渡し
- ルート `i18n/fr/`：`lang.json`、`glossary.add.yaml`、`work/style.md`、`<slug>/metadata.yaml`、`<slug>/work/store.json`、`store-copy.part.html`、`<slug>/cover/cover.png`、`<slug>/build/bontaraku-0{1,2}_*_fr.pdf`、`*_fr_gp.epub`、`*_fr_kindle.epub`、`<slug>/manuscript.md`、`<slug>/review-log.md`。

## 追記 2026-10-31
本1から「紹介制」の表現を代表の指示で削除（8か所。source.ja.md・work/part-*.md・manuscript.md を修正し、再組版）。屯が今は予約なしで入れる旨は残した。
