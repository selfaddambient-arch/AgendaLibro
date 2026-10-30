# インドネシア語（id）の報告

**状態：完了**（翻訳・レビュー反映・組版・表紙・ストア文言・引き渡しの材料まで）。機械ゲート `I18N_LANG=id python3 scripts/i18n/gate.py` は NG 0（epubcheck エラー0、リンクの印 `b?-id-pdf／-gp`、`{{FMT}}` 0件、表紙の文字を Apple Vision で照合して一致）。

## 重要
- **本1（一人で店を回す、その横にAIが来た。）は Google Play の既存の登録への「上げ直し」用のファイル**（インドネシア語版は今年の無料配布207件）。**本2は新規**
- **Kindle：非対応**（KDP の対応言語にインドネシア語なし。2026-10-30 確認）。Kindle 用 EPUB は作っていない。PDF と Google Play 用 EPUB だけ

## 題名（既定は1案目＝英題を基に）
| | 本1 | 本2 |
|---|---|---|
| 1（既定） | **Wakil Manajer AI**（副題：Cukup bicara, AI yang mengerjakannya. Lebih dari yang Anda kira.） | **Dibuat untuk Bar Kami**（副題：Catatan pemilik bar 19 kursi yang membangun sendiri sistem reservasi hingga berbagai alat dengan AI） |
| 2（日本語題の直訳） | Mengelola Kedai Sendirian, dan AI Hadir Mendampingi Saya | Kedai Kami, dengan Spesifikasi Kami Sendiri |
| 3（実践ガイド型の案） | Panduan Praktis AI untuk Pemilik Kedai yang Bekerja Sendirian | Panduan Membuat Sistem Reservasi Sendiri dengan AI untuk Pemilik Bar |

参考：Google Play Books の今年の無料配布数は、インドネシア語版（事業者のための実践ガイド型の題名）207件。**既定を3案目に変えるかは決めていない（案として並べるだけ。代表の判断）**。

## 決めたこと
- 手帳の名前：AgendaHub の `id.ts` に合わせた（打刻 Buku Absensi／採算 Buku Laba Rugi／2軒目 Buku Lanjutan／相談 Buku Bantuan／灯り Buku Lentera／話題 Catatan Obrolan）。辞書に無い3つは窓の案：原価 Buku Biaya Resep／常連 Buku Pelanggan Tetap／当番 Buku Giliran Kerja
- 店・お店は「kedai」（toko は物販店の語で、飲食店に使うと誤解されるため。レビューの指摘を採った）。日本の座敷は「tempat duduk … area tatami」（椅子を連想させる kursi を避ける）
- 数字は `number_style: dot`（¥8.500、$9,3）。円→米ドルは1ドル=150円（換算日 2026-10-29）で、英語版と同じ数値
- 性別を示す代名詞は使わない（インドネシア語の ia／dia は性別を示さないので、単数の人物は ia。mereka は複数のみ）
- 書体は Latin（Baskerville）。右から左・縦書きの特記なし

## ファイルの場所（Hub が LP の言語ページを作るとき）
- 書誌：`i18n/id/<slug>/metadata.yaml`（title・subtitle・author・publisher・lang）
- 一行紹介・説明文・キーワード・ジャンル：`i18n/id/<slug>/work/store.json`（`one_liner`・`description`・`keywords`・`gp_genres`）
- 表紙：`i18n/id/<slug>/cover/cover.png`（1600×2560）
- PDF（A5・QR入り）：`i18n/id/<slug>/build/bontaraku-0N_<slug>_id.pdf`（本1 99ページ、本2 116ページ）
- Google Play 用 EPUB：`i18n/id/<slug>/build/bontaraku-0N_<slug>_id_gp.epub`
- ストア文言：`books/store-copy.html`（本1・本2 × 日本語・英語・インドネシア語）
- リンクの印：`b1-id-pdf`・`b1-id-gp`・`b2-id-pdf`・`b2-id-gp`（Hub の `BOOK_SRC_ALLOWLIST`・屯の `FUNNEL_SRC_ALLOWLIST` には、まだ入っていない。親の窓の「未対応」に書いた）

## レビュー
`i18n/id/<slug>/review-log.md`（未対応 0）。agy（Gemini 3.8 Flash High）が出した指摘のうち、意味を取り違えた箇所（3章の「週に1回登録する」・「登録する（出願）」、6章の「誰にも責任を負わない」＝真逆、2章の「通す」を「飛ばす」と訳した逆、おわりにの「無料」の脱落）を直した。agy の指摘が外れたもの（日本語題の直訳に戻せ、など）は理由つきで採らなかった。

## 費用
翻訳：サブスクの枠（API 0円）。レビュー：agy（Gemini）で追加費用なし。画像生成：なし（英語版の絵を使い回し）。

## 気づいた点（親・他言語へ）
- 英語版の原稿は、日本語の2文「そんな孤独な「経営者としての私」の横に座ってくれた相談相手。／それがAIだったのです。」を1文に合わせている。英語版の見直しを推奨
- 「ありがとう！」のスタンプの文字は、日本語の原稿では「ありがとう！」。英語版は "Thank you!" と書いている（画像は日本語のまま）
