# 多言語版（2冊 × 全言語）の報告

作り方・置き場の決まりは `README.md`。1言語を最後まで仕上げてから次へ進む（並行しない）。

## 対象の言語と順番

AgendaHub の多言語辞書（`lib/i18n/types.ts` の LANGS、20言語）から ja を除いた19言語に、辞書にない **bn（ベンガル語）** を足した。代表の指定の順は「en（仕上げ）→ id → ms → bn → 以降は辞書の並び順」。

| 順 | 言語 | コード | Google Play | 注 |
|---|---|---|---|---|
| 1 | 英語 | en | 新規 | 仕上げ済み（下の「en」） |
| 2 | インドネシア語 | id | 出ている（上げ直し） | |
| 3 | マレー語 | ms | 出ている（上げ直し） | |
| 4 | ベンガル語 | bn | 出ている（上げ直し） | **辞書に無い**。手帳の名前は辞書に合わせられないので窓の案 |
| 5 | ベトナム語 | vi | | |
| 6 | 簡体字中国語 | zh-CN | | |
| 7 | 繁体字中国語 | zh-TW | | |
| 8 | 韓国語 | ko | | **レビューのあと、代表が読む材料を作って止まる** |
| 9 | ネパール語 | ne | | |
| 10 | ミャンマー語 | my | | |
| 11 | タイ語 | th | | |
| 12 | ポルトガル語（ブラジル） | pt-BR | | |
| 13 | スペイン語 | es | | |
| 14 | フランス語 | fr | | |
| 15 | ドイツ語 | de | | |
| 16 | ヒンディー語 | hi | | |
| 17 | フィリピノ語 | fil | | |
| 18 | イタリア語 | it | | |
| 19 | トルコ語 | tr | | |
| 20 | ロシア語 | ru | | |

辞書の並び（ja・en・vi・zh-CN・zh-TW・ko・ne・my・id・th・pt-BR・es・fr・de・hi・fil・it・tr・ru・ms）のうち、id・ms は先頭に出したので辞書の順では飛ばしている。言語コードの2文字ルール：zh-CN／zh-TW／pt-BR はリンクの印の言語を `zh`／`zh`／`pt` にするとぶつかるので、印は `zhcn`・`zhtw`・`ptbr`（英数字のみ）とする（要確認）。

## KDP（Kindle）の対応（2026-10-30 確認）

出典：[KDP ヘルプ「Language & Reading direction」](https://kdp.amazon.com/en_US/help/topic/G200673300) の「対応言語」の一覧。

- 対応（eBook）：英語・ドイツ語・フランス語・イタリア語・ポルトガル語・スペイン語・ヒンディー語（eBook のみ）・繁体字中国語（eBook のみ）
- 一覧に無い（Kindle 用 EPUB は作らず、Google Play 用 EPUB と PDF だけ）：インドネシア語・マレー語・ベンガル語・ベトナム語・簡体字中国語・韓国語・ネパール語・ミャンマー語・タイ語・フィリピノ語・トルコ語・ロシア語
- 注意：ポルトガル語は「Portuguese」とだけ書かれ、ブラジルの区別は無い。簡体字は一覧に無く、繁体字だけがある

## 手順 0（済ませたこと）

- 英語版：Gemini（両書）の裁定を反映済み（`i18n/en/*/review-log.md`）。ChatGPT（1冊目）のレビューは無いとの回答（2026-10-30）。1冊目の裁定は Gemini のみ
- 英題：代表の指示で **1冊目 The AI Deputy Manager／2冊目 Built for Our Bar** に変更（本文の相互参照・表紙・ストア文言も直した）。副題は据え置き
- 日本語版：
  - 1冊目の見出し「5-5」を、本文の数字（客単価約3,500円→＋1,400円＝約4割）に合わせて「客単価が約4割上がった」に直した（原稿・PDF・note 第5章・英訳）
  - 紹介制の一文・2冊目の経歴・AgendaTurno の行・無料の一文：原稿・PDF・note に入れ済み（前回）
  - **未反映**：1冊目の「著者紹介」と「2026年10月の追記」。ChatGPT の裁定が無く、書き換える文面が窓に無い（原文にない事実が要るため入れていない）
- 日本語版 PDF の差し替え（Hub）：`books/hitori-de-mise/build/bontaraku-01_hitori-de-mise_A5.pdf`（sha256 先頭 f8453382）、`books/uchi-no-mise/build/bontaraku-02_uchi-no-mise_A5.pdf`（前回のまま）

## en（英語）：仕上げ

- 組版（`i18n/en/<slug>/build/`）：PDF 1本、Kindle 用 EPUB、Google Play 用 EPUB（`…_en.pdf`・`…_en_kindle.epub`・`…_en_gp.epub`）。epubcheck エラー0・警告0
- 機械ゲート（`I18N_LANG=en python3 scripts/i18n/gate.py`）：すべて合格。リンクの印は pdf／kindle／gp ごとに b?-en-pdf／-kindle／-gp、`{{FMT}}` 0件、図の数・見出しの数は日本語版の EPUB と一致
- 表紙（文字なしの絵に題名を重ねたもの）：`i18n/en/<slug>/cover/cover.png`
- Hub への引き渡し（英語）：`i18n/en/<slug>/metadata.yaml`（題名・副題・著者・発行）／説明文・一行紹介・キーワードは `i18n/en/<slug>/work/meta.json`／ストア用の文言は `books/store-copy.html`／PDF・EPUB は `i18n/en/<slug>/build/`
- Kindle：対応（英語）


## 言語×形式の一覧（2026-10-31 時点）

「○」＝成果物あり。PDF・Google Play 用 EPUB・表紙は 本1・本2 の両方。Kindle は Kindle 用 EPUB。リンクの印は 本-印-形式（印が「仮」のものは代表の確定待ち）。Google Play は en 以外すべて新規（id・ms・bn の本1は上げ直し用）。

| 言語 | 印 | PDF | Google Play | Kindle | 表紙 | 本1の題名（既定） |
|---|---|---|---|---|---|---|
| en | en | ○ | ○ | ○ | ○ | The AI Deputy Manager |
| id | id | ○ | ○（本1は上げ直し） | 非対応 | ○ | Wakil Manajer AI |
| ms | ms | ○ | ○（本1は上げ直し・題名変更） | 非対応 | ○ | （report 参照） |
| bn | bn | ○ | ○（本1は上げ直し） | 非対応 | ○ | （report 参照） |
| ko | ko | 未（代表確認待ち） | 未 | 非対応 | 未 | AI 부점장（案） |
| vi | vi | ○ | ○ | 非対応 | ○ | Phó quản lý AI |
| zh-CN | cn（仮） | ○ | ○ | 非対応 | ○ | AI副店长 |
| zh-TW | tw（仮） | ○ | ○ | ○ | ○ | AI副店長 |
| ne | ne | ○ | ○ | 非対応 | ○ | एआई डेपुटी म्यानेजर |
| my | my | ○ | ○ | 非対応 | ○ | AI ဒုမန်နေဂျာ |
| th | th | ○ | ○ | 非対応 | ○ | รองผู้จัดการ AI |
| pt-BR | pt（仮） | ○ | ○ | ○ | ○ | Subgerente de IA |
| es | es | ○ | ○ | ○ | ○ | El subgerente de IA |
| fr | fr | ○ | ○ | ○ | ○ | L'adjoint IA |
| de | de | ○ | ○ | ○ | ○ | Die KI-Stellvertretung |
| hi | hi | ○ | ○ | ○（eBook のみ） | ○ | AI डिप्टी मैनेजर |
| fil | fil（3文字・要判断） | ○ | ○ | 非対応 | ○ | Ang AI Assistant Manager |
| it | it | ○ | ○ | ○ | ○ | Il vice responsabile IA |
| tr | tr | ○ | ○ | 非対応 | ○ | Yapay Zekâ Müdür Yardımcısı |
| ru | ru | ○ | ○ | 非対応 | ○ | ИИ в роли заместителя управляющего |

各言語の詳細（題名案・用語・レビュー・親への依頼）は `i18n/<言語>/report.md`。ko の組版・表紙・ストア文言は、代表の確認（`i18n/ko/owner-check/README.md`）が済んでから行う。
