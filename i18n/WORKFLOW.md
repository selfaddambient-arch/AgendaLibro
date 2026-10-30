# 1言語を最後まで仕上げる手順（サブエージェント用）

あなたは、2冊の本（『一人で店を回す、その横にAIが来た。』＝本1 `hitori-de-mise`、『うちの店は、うちの仕様で』＝本2 `uchi-no-mise`）を **1つの言語** に翻訳・翻案し、レビュー・組版・表紙・ストア文言・引き渡しの材料まで仕上げる担当です。受け持つ言語コードを `<L>`（例 `ms`）と書きます。リポジトリは `/Users/keikawaguchi/AntiGravity/AgendaLibro`。

## 守ること（破ると作業は無効）

- **書いてよいのは `i18n/<L>/` の中だけ。** `scripts/`・`books/`・`i18n/en/`・`i18n/id/`・ほかの言語・`i18n/WORKFLOW.md` は読むだけ。スクリプトは直さない（直す必要が出たら、報告に「親の窓へ：〜を直してほしい」と書く）
- **git は使わない**（add・commit・push・stash・checkout いずれも）。コミットは親の窓がまとめて行う
- **翻訳は自分で書く。Anthropic API は呼ばない。** 使ってよい API は、レビューの予備経路（`review-api.mjs`、Gemini）だけ
- `secrets/` の中身を画面・ログ・成果物に出さない
- 原文にない事実を足さない。日本語の原稿（`i18n/<L>/<slug>/work/source.ja.md`）が正。足してよい翻案は下の4つだけ
- 他の言語のサブエージェントも同時に動いている。`scripts/i18n/*` は読み取りだけ。ファイルの置き場が重ならないよう、**自分の `i18n/<L>/` の外には何も作らない**
- 一時ファイルも `i18n/<L>/` の中（例 `i18n/<L>/work/tmp/`）に置き、使い終わったら自分で消す

## 材料

- 日本語の原稿（正）：`i18n/<L>/<slug>/work/source.ja.md`（`init-lang.py` が作る。リンクの印は `b1-<印>-{{FMT}}`・`b2-<印>-{{FMT}}` 済み、「3つの出口」とおわりにの順は Agenda→活動→屯（東京に来たら）に入れ替え済み）
- 英語版（構造の土台・参考）：`i18n/en/<slug>/manuscript.md`。**円の金額と米ドルの概算、日本の補足 `*(…)*`、画面の注 `*(The screen is in Japanese.)*`、図のキャプションの形はこの英語版と同じにする**。日本語の意味に迷ったら `source.ja.md` を見る
- 完成例（インドネシア語）：`i18n/id/<slug>/manuscript.md`・`work/part-*.md`・`lang.json`・`glossary.yaml`・`cover/cover.json`・`work/store.json`・`metadata.yaml`・`review-log.md`（あれば）
- 手帳の名前：`/Users/keikawaguchi/AntiGravity/AgendaHub/lib/i18n/dictionaries/<辞書の言語コード>.ts` の `hub.product.<timbro|oro|bis|qa|luce|spunto|voce>.nick`。辞書に無い3つ（原価手帳 Ricetta・常連手帳 Nera・当番手帳 Turno）はその言語の自然な名前を提案する（報告に「窓の案」と書く）。辞書に無い言語（例 bn）は全部「窓の案」

## 手順

### 0. 置き場を作る

```
python3 scripts/i18n/init-lang.py <L> <印>      # 印＝リンクの印の言語（2文字の英小文字）。指示された値を使う
```

`i18n/<L>/lang.json`（雛形）・`glossary.add.yaml`（雛形）・`<slug>/{work,cover,review,build}/`・`work/source.ja.md` ができる。**`lang.json` の TODO を全部埋める**：
- `bcp47`（例 `ms`）、`name`（その言語の自称）、`ja_name`（日本語での言語名）、`dir`（右から左なら `rtl`。辞書の言語はすべて `ltr`）
- `kindle`：指示された値（KDP が対応していなければ `false`）
- `fig_label`（図の言葉。例 Gambar）、`number_style`：`en`（1,000／0.5）・`dot`（1.000／0,5）・`space`（1 000／0,5）。**その言語の普通の書き方**に合わせる
- `font`：**その文字が正しく出る macOS の書体**（Latin は `'Baskerville','Georgia',serif`。タイ語 `'Thonburi'`、ミャンマー語 `'Myanmar MN'`、ベンガル語 `'Bangla MN'`、デーヴァナーガリー `'Devanagari Sangam MN'`、韓国語 `'Apple SD Gothic Neo'`、中国語 `'PingFang SC'`（繁体字は `'PingFang TC'`）など。`fc-list : family` で確かめる）
- `cjk`：中国語なら true（日本語の文字が残っていないかの検査を外す）。それ以外は false
- `ocr_langs`：表紙を読む言語（`swift scripts/i18n/ocr-cover.swift --langs` に出るもの。例 `["ms-MY","en-US"]`、ko は `["ko-KR","en-US"]`）。Vision が対応していない文字（ベンガル語・ネパール語・ミャンマー語・ヒンディー語など）は **この行ごと消す**（表紙は画像を自分で見て確かめる）
- `toc_title`（目次）、`qr_labels`（QR の3つの見出し：Agenda を試す／活動を追う（note）／東京で屯を訪ねる。`id/lang.json` を訳す）、`colophon`（奥付。`id/lang.json` の colophon をその言語に訳す。`{title}` などの波括弧はそのまま残す）
- 奥付には必ず「AI で翻訳し、AI のレビューを経た」旨と、円→米ドルの概算（1ドル=150円・換算日）、日本の補足は翻訳者が足した旨を入れる

`glossary.add.yaml` の `to:` を埋める（`id/glossary.yaml` が完成例）。`forbid` はその言語で揺れやすい綴りに直す。**同じ語の訳を本文で揺らさない**（検査される）。

### 1. 翻訳（本1・本2）

- 英語版を **約200行ずつ** 読み、その分を訳して `i18n/<L>/<slug>/work/part-01.md`、`part-02.md`… に書く。本1は8部品前後、本2は6部品前後。章の見出しの切れ目に合わせると組みやすい
- **Markdown の構造は英語版と1行も違わせない**：見出しの `#` の数、表（行・列とも）、箇条書き、引用、画像の行、行末の `\`（強制改行）、空行、`【<図の言葉> X-Y】キャプション` の行、リンクの URL（`{{FMT}}` を含めてそのまま）
- 図の印は `【図1-1】` → `【<fig_label> 1-1】`。画面の注 `*(The screen is in Japanese.)*` はその言語に訳す（本2の約28か所すべて）
- **円の金額**：`¥` ＋数字。数字の書き方は `number_style` に合わせる。直後の括弧に英語版と同じ米ドルの概算を `$` で書く（例 `¥8.500 (sekitar $57)`）。**金額の並び・米ドルの並びは英語版と数値が一致すること**（検査される）。範囲は `¥4.500–¥5.700 (… $30–$38)`
- 日本の補足 `*(…)*`（東中野・LINE・居酒屋）は英語版と同じ位置に、その言語で書く
- 性別を示す代名詞は使わない（著者・店主・実在の人物とも）。原文に性別が無い。名前・役割・「they」に相当する言い方・言い換えで書く
- 著者名は **Raku Bonta**（その言語の表記が通常 Latin なら Latin のまま。ハングルなど別の文字では、その言語での表記と Latin を併記してよい）。会社名は Bonta LLC
- 用語は用語集どおり。`屯`＝Tamuro、`T-AI-MURO`はそのまま、`Agenda`の製品名（AgendaTimbro など）はそのまま
- 相互参照の題名：本1の本文が本2を、本2の本文が本1を参照する箇所は、**その言語の決めた題名**にする（`*題名*`）。題名が決まるまでは仮でよいが、最後にそろえる
- 自己点検（英語版のレビューで多かった指摘）：①直訳調で不自然な文 ②見出しと本文の数字の食い違い（例 5-5 の見出しは「約4割」）③相対的な日付（「去年」「今年」など。原文は2026年10月時点の記録なので、必要なら年を添える）
- 全部書いたら `I18N_LANG=<L> python3 scripts/i18n/assemble.py` で `manuscript.md` を組む。`<slug>/manuscript.md` の先頭は、本1は `## 〈はじめにの訳〉`、本2は `# 題名` ＋副題＋著者＋3行のリンクのあと `## 〈はじめにの訳〉`

### 2. 題名・書誌

- `i18n/<L>/<slug>/metadata.yaml`：`title`、`subtitle`、`author`（Raku Bonta）、`publisher`（Bonta LLC）、`lang`
- **題名は「英題を基に」**：本1の英題は *The AI Deputy Manager*、本2は *Built for Our Bar*。その言語で内容が伝わる題名にする
- 題名の案を **3つずつ** 報告に書く。1案目＝英題を基にした既定。2案目＝日本語の題の直訳に近い案。3案目＝「事業者のための実践ガイド」型の案。参考：Google Play Books の今年の無料配布数は、インドネシア語版（実践ガイド型の題名）207件、マレー語版（物語型の題名）48件、ベンガル語版23件。**既定を実践ガイド型に変えるかどうかは決めない**（案として並べるだけ。決めるのは代表）
- 本1の題名にある言い回しが、本2の本文の「前作」の参照と合っていること

### 3. 機械ゲート（翻訳のあと・レビューのあと・組版のあと）

```
I18N_LANG=<L> python3 scripts/i18n/gate.py          # 終了コード 0 まで直す
```

（`python3` ではなく `/private/tmp/claude-502/-Users-keikawaguchi-AntiGravity-AgendaLibro/441d50a6-9423-46bd-b06c-f8a7a50a3bef/scratchpad/venv/bin/python3` を使う。pyyaml と pymupdf が入っている）

見出し数・画像・図・表・リンクの数と中身・リンクの印・`{{FMT}}`・円と米ドルの並び・用語・日本語の文字の残り・（組版後）EPUB の epubcheck・リンクの印・図と見出しの数・表紙の文字、が検査される。

### 4. レビュー（Gemini）

```
I18N_LANG=<L> python3 scripts/i18n/review.py                 # 章ごとのレビュー用ファイル（原文＋訳）を作る
I18N_LANG=<L> bash scripts/i18n/review-agy.sh                # agy -p（Gemini）に章ごとに出す。返事は <名前>.gemini.md
```

- agy の枠が尽きたら（`NG` で止まる）、残りは `I18N_LANG=<L> node scripts/i18n/review-api.mjs`（Gemini API）に切り替える
- `.chatgpt.md` の空ファイルは要らないので消してよい
- 指摘（①意味の取り違え ②不自然な表現 ③その言語の読者に伝わらない箇所）を読み、**まとめて直す**（`work/part-*.md` を直して assemble し直す）。agy の指摘は外れることもある（例 英題を基にした題名を、日本語の題の直訳に戻せという指摘は採らない。原文にない事実を足す案は採らない）
- `i18n/<L>/<slug>/review-log.md` に **全部の指摘について**「採った／採らなかった」と理由を書く。**未対応（返事が無い・判断していない指摘）は0**。章の返事が空だったら「未レビュー」と書く
- レビューで直したら、もう一度 assemble してゲートを通す

### 5. 組版（ko だけは別。下の「ko」を見る）

```
I18N_LANG=<L> node scripts/i18n/cover.mjs            # 表紙：英語版の文字なしの絵（i18n/en/<slug>/cover/art.png）に題名を重ねる。画像の生成はしない
I18N_LANG=<L> node scripts/i18n/build.mjs            # PDF 1本・Google Play 用 EPUB・Kindle 用 EPUB（lang.json の kindle が true のときだけ）
I18N_LANG=<L> python3 scripts/i18n/gate.py
```

- 表紙は `i18n/<L>/<slug>/cover/cover.json`（`lines`＝題名の行分け、`size`、`tag`＝下の帯、`subsize`、`italic`：false にするとイタリックにしない。非 Latin の文字ではイタリックにしない）を書いてから cover.mjs。**画像を自分で開いて、文字化け・はみ出し・重なりがないか確かめる**（`Read` で画像を見る）。Vision が対応する言語は gate が自動で照合する
- epubcheck は gate が回す（エラー0・警告0にする）。PDF は 2冊とも 100ページ前後になる。ページ数が極端に違うときは書体や CSS（`lang.json` の `font`）を見直す
- PDF の表紙ページ・目次・本文・奥付・QR（3つの出口の直後）を、`pymupdf` で数ページ画像にして目で確かめる

### 6. ストア文言

- `i18n/<L>/<slug>/work/store.json`：`{"one_liner": "一行紹介（160字以内）", "description": "ストア用の説明文（150〜220語。改行は空行で段落）", "keywords": ["7つ"], "gp_genres": ["Google Play のジャンルの候補"], "kindle_categories": ["Kindle のカテゴリの候補（kindle が true の言語だけ）"]}`。`id/<slug>/work/store.json` が完成例。**原文にない事実を足さない**。説明文の最後は「無料で読める・共有してよい」旨（Kindle のある言語は Kindle だけ最低価格が付く旨）
- `python3 scripts/i18n/store-copy.py --part <L>`（`I18N_LANG` は不要）で `i18n/<L>/store-copy.part.html` ができる（その言語の欄だけの1枚。ブラウザで開いて確かめる）。**`books/store-copy.html` は親が取り込む（触らない）**

### 7. 報告と引き渡しの材料：`i18n/<L>/report.md`

日本語で、短く。次を書く：
- 状態（どこまで終わったか）。ゲートの結果（`gate.py` の NG が0であること、epubcheck の結果）
- **Google Play の上げ直しか新規か**（本1の id・ms・bn は「上げ直し」。それ以外は新規）。Kindle 対応の可否と根拠（lang.json の kindle）
- 題名の案（本1・本2 各3つ。上の「題名・書誌」の決まり）。既定
- 用語の決め（手帳の名前＝辞書のものと窓の案を分けて）、数字の書き方、書体、特記（右から左・縦書き等）
- ファイルの場所（metadata・説明文・一行紹介・表紙・PDF・EPUB）。Hub が LP の言語ページを作るときに必要な一覧
- review-log の要約（採った指摘の主なもの。未対応0）
- 費用（翻訳＝サブスクの枠、レビュー＝agy。API を使ったなら量）
- 気づいた点・親の窓への依頼

## ko（韓国語）だけの違い

レビュー（手順 4）まで済ませて直したら、**ここで止まる**。組版（5）はしない。代わりに代表が読むための材料を `i18n/ko/owner-check/` に作る：
- `README.md`（日本語）：読む順・各ファイルの意味・Gemini の指摘の要約・直した主な箇所・迷った箇所（訳が分かれる語、題名の案）
- 章ごとの対訳（日本語の原文と韓国語の訳を並べた Markdown）は `i18n/ko/<slug>/review/<名前>.md` がそのまま使える。読む順の一覧を README に書く
- 代表の確認が済むまで、組版・表紙・ストア文言は作らない（その分は報告に「確認待ち」と書く）

## 途中の注意

- 長い作業なので、部品ごとに保存しながら進める（途中で止まっても、できたところが残る）
- 時間の目安：翻訳 30〜40分、レビュー 40〜60分（agy の返事待ちが長い）、組版 10分。agy は1回に2〜3分かかる
- 迷って止まらない。決められることは自分で決めて報告に書く。**止まってよいのは、原文にない事実が要るときだけ**（そのときは報告に理由を書いて終わる）
