翻訳・翻案の置き場。`i18n/<言語コード>/<本の略名>/` に原稿を置く。

- `i18n/glossary.yaml`：用語集・為替の固定値（英訳の system と検査に使う）
- `i18n/en/<slug>/manuscript.md`・`metadata.yaml`：英語版の正本
- `i18n/en/<slug>/review/`：レビューの材料と返事の置き場（`<章>.md`・`.gemini.md`・`.chatgpt.md`）
- `i18n/en/<slug>/work/`：途中の生成物（前処理した日本語・分割・モデルの生の出力・英題と説明文）
- `i18n/en/report.md`：英語版の報告
- 作り方：`scripts/i18n/`（translate.py・gate.py・meta.py・review.py）。鍵は secrets/.env の ANTHROPIC_API_KEY
