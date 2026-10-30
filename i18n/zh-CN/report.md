# zh-CN（簡体字中国語）報告

## 状態
- 本1『AI副店长』・本2『为我们的店量身打造』とも、翻訳→ゲート→Geminiレビュー→反映→表紙→組版→ストア文言まで完了。
- gate.py：2冊とも NG 0。epubcheck エラー0。表紙の文字は Vision で照合済み。日本語の文字の残りは仮名0。
- PDF：本1が89ページ、本2が94ページ。表紙・目次・本文・QR・奥付を画像で確認（はみ出し・文字化けなし）。
- リンクの印は **cn（仮）**。決定したら lang.json の mark と原稿のリンクを揃えて作り直す。

## Google Play・Kindle
- Google Play：本1・本2とも新規。
- Kindle：不可（lang.json の kindle=false。KDP の対応一覧に簡体字中国語が無い）。Kindle 用 EPUB は作っていない。

## 題名の案（既定は1案目。変更は代表が決める）
本1：1. AI副店长（既定）／2. 一个人撑起一家店，AI来到了我身边／3. 小店老板的AI实战指南：零基础让AI当你的副店长
本2：1. 为我们的店量身打造（既定）／2. 我们的店，按我们的规格来／3. 小店老板用AI自建预约系统与工具实战手记
- 副題：本1「只要开口说，AI就会动手。比想象的更能干。」／本2「一位19席酒吧店主，用AI从预约系统到各种工具全部亲手做出来的记录」
- 本1が本2を《为我们的店量身打造》、本2が本1を《AI副店长》と参照。題名を変えるときは両冊の本文の参照も直す。

## 用語・書き方・書体
- 手帳の名前（辞書 zh-CN.ts の nick）：打卡手账／采算手账／续摊手账／咨询手账／灯火手账／话题手账。
- 窓の案（辞書に無い3つ）：成本手账（Ricetta）／常客手账（Nera）／值班手账（Turno）。
- 屯＝Tamuro（初出に Tamuro（屯）を併記）。氛围编程（Vibe Coding）、副店长、玄关、专栏、后记、前言。
- 数字は number_style=en。円は ¥8,500(约$57)。米ドルの括弧は半角（ゲートが半角前提のため）。
- 句読点・引用符は中国語の標準（“ ”）。書体 'PingFang SC' 系、ocr_langs=["zh-Hans","en-US"]、cjk=true。右から左・縦書きの特記なし。
- 図の言葉「图」（【图 1-1】）。画面の注は *(画面为日语。)*（本2の28か所すべて）。性別を示す代名詞は不使用。
- 訳語：19座→19席（「座」は建物の量詞）、座敷→榻榻米座席、ハンバーグ→汉堡排、トンテキ→猪排、highball→嗨棒、UI の画面→界面、管理画面→管理后台、手順書→流程文档。
- 相対的な日付に年を添えた（今年（2026年）、2025年・2026年の生肖）。

## ファイルの場所（本1：i18n/zh-CN/hitori-de-mise/、本2：i18n/zh-CN/uchi-no-mise/、絶対パスは /Users/keikawaguchi/AntiGravity/AgendaLibro/ 以下）
- 書誌 metadata.yaml／原稿 manuscript.md（部品 work/part-*.md）
- 一行紹介・説明文・キーワード・ジャンル work/store.json
- 表紙 cover/cover.png（cover.json、cover.html）
- PDF build/bontaraku-01_hitori-de-mise_zh-CN.pdf、build/bontaraku-02_uchi-no-mise_zh-CN.pdf
- Google Play 用 EPUB build/bontaraku-01_hitori-de-mise_zh-CN_gp.epub、build/bontaraku-02_uchi-no-mise_zh-CN_gp.epub
- レビュー review/*.gemini.md、review-log.md
- 言語設定 i18n/zh-CN/lang.json、用語集 glossary.add.yaml、ストア文言の1枚 i18n/zh-CN/store-copy.part.html

## review-log の要約（未対応0）
- 本1は8ファイル、本2は11ファイルの Gemini の返事を全部読み、各指摘に採否を記録。
- 採った主なもの：誤訳（扫兴／同一个标签／不对任何人负责／模拟备份／改写／重写费用／做大／开门吗）、不自然な表現（倾诉对象→商量对象、小键盘→副键盘、锐利→特色鲜明、画面→界面、挑剔→独到、登录→入驻）、事実（年末年始のタイトル変更を日本語原文に合わせる、○○万日元、独り経営に合わない「我们」の削除）。
- 採らなかったもの：英語版の構造に合わせる案（章・コラム番号の丸数字化）、原文にない筆名の漢字併記、Gemini の誤読（「の」「予约」「サーバー」が残っているとの指摘は実際には無い）、辞書の名称を変える案（采算手账→核算手账）。

## 費用
- 翻訳はサブスクの枠（自分で執筆）。レビューは agy（Gemini）のみ。API は不使用。

## 気づいた点・親の窓への依頼
- リンクの印 cn は仮。
- scripts/i18n/store-copy.py --part は、他言語で store.json だけがあり metadata.yaml が無い途中状態（作業中の ne）のとき落ちる。再実行で通った。
- 本1 2-7 の Mac ショートカット [Cmd]+[Shift]+[4] は既定ではファイル保存（クリップボードは Ctrl も押す）。Gemini の指摘。日本語原文どおりに訳した。確認依頼。
- 本1 5-3 の図キャプションの一部（「餐点是分开的」）は原文の意味を確定できず英語版に合わせた。
- 空の review/*.chatgpt.md は、削除コマンドが環境のフックで止まったため残している（内容は空）。
- 「采算手账」は中国語圏で通じにくいと Gemini が指摘したが、Hub の辞書に合わせた。Hub 側の判断に任せる。
