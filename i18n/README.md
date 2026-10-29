翻訳・翻案の置き場。`i18n/<言語コード>/<本の略名>/` に原稿を置く。

- `i18n/glossary.yaml`：用語集・為替の固定値（英訳の system と検査に使う）
- `i18n/en/<slug>/manuscript.md`・`metadata.yaml`：英語版の正本
- `i18n/en/<slug>/review/`：レビューの材料と返事の置き場（`<章>.md`・`.gemini.md`・`.chatgpt.md`）
- `i18n/en/<slug>/work/`：途中の生成物（前処理した日本語・分割・モデルの生の出力・英題と説明文）
- `i18n/en/report.md`：英語版の報告
- 作り方：`scripts/i18n/`（translate.py・gate.py・meta.py・review.py）。鍵は secrets/.env の ANTHROPIC_API_KEY
- 方針（2026-10-29）：翻訳・訳し直し・レビューの反映は窓が自分で書く。Anthropic API を呼ぶ `translate.py` の submit／retry と `meta.py` は使わない。API は Nano Banana（`nano.mjs`・`cover.mjs`）だけ
- `i18n/en/<slug>/cover/`：英語版の表紙（`art.png` は文字なしの絵、`cover.png` は完成）。`i18n/en/uchi-no-mise/trial/`：画面写真の英語化の試し
- `books/store-copy.html`：ストアに貼る文言のページ（`scripts/i18n/store-copy.py` で作る）
