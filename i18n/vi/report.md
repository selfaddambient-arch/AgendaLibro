# ベトナム語（vi）の報告

**状態：完了**。サブエージェントが作り、親の窓が `I18N_LANG=vi gate.py` を再実行して NG 0・epubcheck エラー0を確認した。表紙は Vision（vi-VT）で照合一致。

- **Google Play：本1・本2とも新規**。**Kindle：非対応**（KDP の一覧に無い。PDF と Google Play 用 EPUB のみ）

## 題名（既定は1案目）
| | 本1 | 本2 |
|---|---|---|
| 1（既定） | **Phó quản lý AI**（Chỉ cần trò chuyện, AI sẽ làm giúp. Nhiều hơn bạn tưởng.） | **Làm riêng cho quán bar của mình** |
| 2（直訳） | Một mình điều hành quán, và AI đã đến ngồi bên cạnh tôi | Quán của chúng tôi, theo yêu cầu của chính chúng tôi |
| 3（実践ガイド型） | Hướng dẫn thực hành AI cho chủ quán tự vận hành một mình | Hướng dẫn tự xây hệ thống đặt chỗ bằng AI cho chủ quán bar |

既定を3案目に変えるかは代表の判断。

## 決めたこと
- 手帳の名前：辞書（vi.ts）どおり Sổ chấm công・Sổ tính lãi・Sổ quán tiếp theo・Sổ hỗ trợ・Sổ tay ánh đèn・Sổ gợi chuyện。窓の案：Sổ giá vốn（原価）・Sổ khách quen（常連）・Sổ xếp ca（当番）
- 一人称 tôi、読者 bạn。性別を示す語は使わない。number_style=dot（¥8.500 (khoảng $57)）。書体 Latin
- 「空いてる？」＝Tối nay Tamuro còn chỗ không?（営業中かの取り違えを修正）

## ファイルの場所
- PDF：`i18n/vi/<slug>/build/bontaraku-0N_<slug>_vi.pdf`（本1 98ページ・本2 106ページ）／GP 用 EPUB：同じ場所の `_vi_gp.epub`
- 表紙 `cover/cover.png`／書誌 `metadata.yaml`／説明文ほか `work/store.json`／ストア文言 `i18n/vi/store-copy.part.html`
- リンクの印：`b1-vi-pdf`・`b1-vi-gp`・`b2-vi-pdf`・`b2-vi-gp`（受け口の許可リストには未登録）

## レビュー
`review-log.md`（未対応 0）。「最強の発注者」を客と誤訳、早割の条件が逆、「空いてる？」を営業中と誤訳、などを修正。Sổ quán tiếp theo を誤訳とする指摘、原文にない訳注を足す案、直訳題への差し戻しは採らなかった。

## 費用
翻訳：サブスク。レビュー：agy、停止したため一部（本1の5〜7章・本2の3〜6章）は Gemini API（入力約4.7万・出力約6千トークン、数円）。画像生成なし。

## 気づいた点
- agy は複数言語の同時実行で2時間応答が止まることがある（review-agy.sh のタイムアウトが望ましい）

- 2026-10-31 紹介制の表現を本1から削除（7か所。source.ja.md・work/part-*.md・manuscript を修正し再組版・gate 実施）。
