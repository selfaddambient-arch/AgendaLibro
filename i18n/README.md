# i18n：言語ごとの翻訳・翻案

言語ごとにディレクトリを切る：`i18n/<言語コード（2文字）>/`。英語は `i18n/en/`。次の言語（id・ms・bn …）も同じ形で `i18n/id/` などを作る。

```
i18n/<言語>/
  README.md            その言語の状態・決めたこと（任意）
  glossary.yaml        用語集・為替の固定値（to: がその言語の訳語）
  report.md            その言語の報告（レビューに貼る順・英題の案・費用・未対応）
  nano-usage.log       画像生成の使用量
  work-*.json          途中の記録（バッチ・使用量・レビューの一覧）
  <本の略名>/          hitori-de-mise（1冊目）／uchi-no-mise（2冊目）
    manuscript.md      その言語の正本（窓が直接編集する）
    metadata.yaml      題名・副題・著者・発行・言語
    cover/             art.png（文字なしの絵・英語版のものを使い回す）／cover.png（完成）／cover.html
    review/            <章>.md（原文＋訳）と、返事の置き場 <章>.gemini.md・.chatgpt.md
    work/              前処理した日本語・分割・生の出力・題名と説明文
    build/             組版の出力（PDF・Kindle 用 EPUB・Google Play 用 EPUB）
    trial/             試しの置き場（使わないと決めたものも残す）
```

- 日本語版の正本は `books/<略名>/`。ここ（`i18n/`）には置かない
- ストアに貼る文言は全言語まとめて `books/store-copy.html`（`scripts/i18n/store-copy.py`）
- リンクの印は外国語版は「本-言語-形式」：`b1`／`b2` - 言語2文字 - `pdf`／`kindle`／`gp`（例 `?src=b2-en-pdf`・`?via=b1-id-gp`）。`{{FMT}}` は組版で置き換える
- 方針：翻訳・訳し直し・レビューの反映は窓が自分で書く。Anthropic API は呼ばない（週間の使用量が 80% 以上のときだけ Batch に切り替える）。API は Nano Banana（`nano.mjs`・`cover.mjs`）だけ
- スクリプトは `scripts/i18n/`。言語は環境変数 `I18N_LANG`（既定 `en`）で切り替える：`I18N_LANG=id python3 scripts/i18n/gate.py`
