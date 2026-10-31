# Google Play Books 一括登録の準備

20言語（ja 除く。指示の「19言語」は bn を足して実数 20）× 2冊 = 40冊。生成は `python3 build_bulk.py`（冪等・Google へは接続しない）。

## 中身

| ファイル | 内容 |
|---|---|
| `bulk_new.csv` | 新規 37 行（en を含む。en は report.md で「新規」） |
| `bulk_update.csv` | 上げ直し 3 行（本1の id・ms・bn）。Identifier = 既存の GGKEY（**空欄**） |
| `bulk_overview.csv` | 管理用の全件一覧（区分・ファイルの場所・ジャンル案・キーワード案）。Partner Center には上げない |
| `files/epub/<ID>.epub` | Google Play 用 EPUB（40） |
| `files/cover/<ID>_frontcover.png` | 表紙（40） |
| `files/pdf/<ID>.pdf` | PDF（40。ダウンロード許可用） |
| `check_report.txt` | 機械検査の結果 |

`<ID>` = `bontaraku-0N_<slug>_<言語>`。列：価格 0（USD, `WORLD`＝全世界、自動換算を使う）、DRM なし、`Enable for Sale?`=Yes。

## 代表の手順

1. `bulk_update.csv` の Identifier 3 つに、Partner Center の書籍一覧から id・ms・bn 本1の GGKEY をコピーして貼る（1回）。
2. Partner Center > Book Catalog > Advanced options > 「Upload content files」で `files/epub/` と `files/cover/` を上げる（新規はこの時点で書籍が作られる）。
3. 同じ Advanced options > 「Upload book list」で `bulk_new.csv`、続けて `bulk_update.csv` を上げる（View uploaded lists で結果確認）。
4. 価格の列名が合わないと言われたら、Download template（価格列つき・通貨換算ON）の列名に `bulk_*.csv` の列名を合わせる。
5. 上げ直し 3 件は既存の書籍に新ファイルを差し替え、題名が変わる ms を確認。

## 形式の出典と判断

- [Add multiple books](https://support.google.com/books/partner/answer/3289689)：テンプレートは Book Catalog > Advanced options > Download template。必須は Identifier と Title。空欄はテンプレートの既定値。アップロードは CSV／TSV、UTF-8 か UTF-16、拡張子 .csv／.txt。
- [Change book settings in bulk](https://support.google.com/books/partner/answer/3058975)：列名（Identifier, Enable for Sale?, Title, Subtitle, Book Format, Contributor [Role], Language(ISO 639-2/B), Description(基本HTML・リンク不可), Publisher Name, DRM Enabled?, PDF Download Allowed? ほか）。更新は Identifier が一致する行。価格は「数値の列」と「適用国の列（WORLD 可）」の対で、通貨換算が有効なら他通貨の国へ自動換算。**列名は変わりうる、と Google 自身が明記**。
- ファイル名の規則（同 3289689）：`[ID].epub`、`[ID]_frontcover.(png|jpg)`、`[ID].pdf`（補助 PDF）。

### 判断できなかった点・要確認

- **ISBN が無い本は表だけでは新規追加できない**（3058975 に明記。GGKEY は一括では作れない）。このため新規の Identifier は自前のファイル名の基底（`<ID>`）にし、**手順2でファイルを先に上げて書籍を作る流れ**にした。ここで Google が付ける GGKEY と表が結びつかない場合は、手順3の新規分は Partner Center が拒否する可能性がある（その場合は作られた書籍の GGKEY に差し替えて再アップロード）。
- 価格の列名（`Price in USD` / `Countries for USD Price`）は、公式の説明から組んだ仮の名前。実テンプレートの名前に合わせる（手順4）。
- 題名・説明文の字数上限は Google が公表していない。検査は仮の上限（題名・副題255、説明文4000）。最長は題名37字・副題122字・説明文1491字で、非公式の目安 3000 字にも収まる。
- ジャンル（Subject Code = BISAC 等）は store.json の案が文章で、コードではないため列に入れていない（`bulk_overview.csv` に参考で出力）。
- 発行日（On Sale Date）は未設定（即時公開）。
- en は report.md で新規扱いだが、出ている版があるかはリポからは確認できない。あれば上げ直しに移す（`build_bulk.py` の `UPDATE`／`GGKEY`）。
- GGKEY：リポ内（docs・books・i18n の各 report）と AgendaHub を grep したが、id・ms・bn とも**見つからない**。代表が Partner Center の書籍一覧から1回コピー。分かれば `build_bulk.py` の `GGKEY` に入れて再実行。
