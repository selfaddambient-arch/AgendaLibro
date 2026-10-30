# 繁体字中国語・台湾（zh-TW）の報告

**状態：完了**。サブエージェントが作り、親の窓が `I18N_LANG=zh-TW gate.py` を再実行して NG 0（epubcheck エラー0・警告0、表紙は Vision zh-Hant で照合一致）を確認した。PDF は本1が89ページ・本2が92ページ。

## 重要
- **リンクの印は `tw`（仮）**。確定したら `lang.json` の `mark` と原稿の `-tw-{{FMT}}` を差し替えて作り直す
- **Google Play：2冊とも新規**
- **Kindle：対応**（KDP は繁体字中国語を eBook のみ対応。出典 kdp.amazon.com/en_US/help/topic/G200673300、2026-10-30確認）。Kindle 用 EPUB を2冊とも作成

## 題名（既定は1案目）
| | 本1 | 本2 |
|---|---|---|
| 1（既定） | **AI副店長**（只要開口說，AI就會動手。遠超乎我的預期。） | **為自家酒吧量身打造** |
| 2（直訳） | 一個人顧店，身邊來了AI | 我們的店，照我們自己的規格 |
| 3（実践ガイド型） | 一人店主的AI實戰指南：不寫程式也能把工作交給AI | 酒吧老闆的AI自建預約系統實戰指南 |

既定を3案目に変えるかは代表の判断。

## 決めたこと
- 手帳の名前：辞書どおり 打卡手帳・採算手帳・續攤手帳・諮詢手帳・燈火手帳・話題手帳。窓の案：成本手帳（原価）・常客手帳（常連）・值班手帳（当番）
- 台湾の語彙。句読点は全角、引用は「」『』。漢堡排咖哩に統一。性別を示す単数代名詞は使わない。number_style=en（¥8,500 (約 $57)）。書体 PingFang TC

## ファイルの場所
- PDF：`i18n/zh-TW/<slug>/build/bontaraku-0N_<slug>_zh-TW.pdf`／GP 用：`_zh-TW_gp.epub`／Kindle 用：`_zh-TW_kindle.epub`
- 表紙 `cover/cover.png`／書誌 `metadata.yaml`／説明文ほか `work/store.json`（Kindle カテゴリ含む）／ストア文言 `i18n/zh-TW/store-copy.part.html`
- リンクの印：`b1-tw-pdf／kindle／gp`、`b2-tw-pdf／kindle／gp`（受け口の許可リストには未登録）

## レビュー
`review-log.md`（未対応 0）。「こぢんまり」「ワンオペ」の誤訳、5-4 の逆の意味の文、「空いてる？」→有位子嗎、「解約」→退會、一人営業文脈の「我們」などを修正。「屯」の漢字併記、手帳名や著者名の訳の変更、好みの言い換えは採らなかった。

## 費用
翻訳：サブスク。レビュー：agy のみ。API 0円。画像生成なし。

## 気づいた点
- build で pandoc の警告（`translations/zh.yaml` が zh-TW を読めず「Abstract」に訳がない）。epubcheck は警告0
