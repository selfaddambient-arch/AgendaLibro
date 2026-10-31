# マレー語（ms）の報告

**状態：完了**（翻訳・レビュー反映・組版・表紙・ストア文言まで）。サブエージェントが作り、親の窓が `I18N_LANG=ms python3 scripts/i18n/gate.py` を再実行して NG 0・epubcheck エラー0を確認した。

## 重要
- **本1は Google Play の既存の登録（マレー語版・物語型の題名・今年の無料配布48件）への「上げ直し」用。題名が変わる**（Penolong Pengurus AI）ので、差し替えるかは代表の判断。**本2は新規**
- **Kindle：非対応**（KDP の対応言語にマレー語なし。2026-10-30 確認）。Kindle 用 EPUB は作っていない

## 題名（既定は1案目＝英題を基に）
| | 本1 | 本2 |
|---|---|---|
| 1（既定） | **Penolong Pengurus AI**（副題 Cukup bercakap, AI yang buat. Lebih daripada yang anda sangka.） | **Dibina untuk Bar Kami** |
| 2（日本語題の直訳） | Mengurus Kedai Seorang Diri, dan AI Datang di Sisi Saya | Kedai Kami, Spesifikasi Kami |
| 3（実践ガイド型の案） | Panduan Praktikal AI untuk Pemilik Kedai dan Restoran Kecil | Panduan Praktikal Membina Sistem Sendiri dengan AI untuk Pemilik Bar |

参考：マレー語版は物語型の題名で今年の無料配布48件（インドネシア語の実践ガイド型は207件）。既定を3案目に変えるかは決めていない（代表の判断）。

## 決めたこと
- 手帳の名前：辞書（`ms.ts`）どおり Buku Kehadiran・Buku Untung Rugi・Buku Destinasi Seterusnya・Buku Bantuan・Buku Lampu・Nota Sembang。辞書に無い3つは窓の案：Buku Kos Resipi（原価）・Buku Pelanggan Tetap（常連）・Buku Giliran Kerja（当番）
- 数字は `number_style: en`（1,000／0.5）。書体は Latin。左から右。性別を示す語は使わない
- ハンバーグ＝hamburg（burger はバンズの料理と読まれるため）。kursus（講座）でなく set hidangan。インドネシア語的な語をマレーシア標準に（baton など）

## ファイルの場所
- PDF：`i18n/ms/<slug>/build/bontaraku-0N_<slug>_ms.pdf`（本1 98ページ・本2 116ページ）／Google Play 用 EPUB：同じ場所の `_ms_gp.epub`
- 表紙：`i18n/ms/<slug>/cover/cover.png`／書誌：`metadata.yaml`／説明文・一行紹介・キーワード・ジャンル：`work/store.json`
- リンクの印：`b1-ms-pdf`・`b1-ms-gp`・`b2-ms-pdf`・`b2-ms-gp`（受け口の許可リストにはまだ入っていない）

## レビュー
`i18n/ms/<slug>/review-log.md`（未対応 0）。agy（Gemini）で本1が9本・本2が11本。意味の取り違え（kursus、「杖」を kakitangan と訳した箇所、「空いてる」を buka と訳した箇所など）を直した。題名を直訳に戻す案、米ドル・図の注を消す案、Mac の併記を消す案などは理由つきで採らなかった。

## 費用
翻訳：サブスクの枠。レビュー：agy。API 0円。画像生成なし。

## 気づいた点
- 英語版の「Is Tamuro open tonight?」は日本語の「空いてる？（席が空いているか）」とずれる（英語版の見直しを推奨）
- 英語版の「それがAIだったのです。」の独立文が前の文に吸収されている

本1から「紹介制」の表現を代表の指示で削除（8か所。source.ja.md・work/part-*.md（enは manuscript.md と work/raw）・manuscript.md を修正し、再組版）。屯が今は予約なしで入れる旨は残した。
