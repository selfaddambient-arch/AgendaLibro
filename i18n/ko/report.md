# 韓国語（ko）完了報告

（サブエージェントの返答から親の窓が作成）

## 状態
- 代表の回答（確認事項は既定のまま）に従って仕上げた。2026-10-31。
- gate.py（I18N_LANG=ko）NG 0（表紙の OCR 照合・epubcheck を含む）。
- Google Play は新規。Kindle は非対応（kindle=false、Kindle 用 EPUB なし）。
- 「紹介制」の表現は全言語から削除済み。「Kindle だけ最低価格」の注記は本1のおわりに残した。

## 題名（既定の1案目）
- 本1：AI 부점장（副題：말만 하면 알아서 해 줍니다. 생각보다 훨씬 많은 일을.）
- 本2：우리 가게에 맞춰 만들다（副題：19석 바의 주인이 예약 시스템부터 도구까지 AI로 직접 만든 기록）
- 本1と本2の相互参照はこの題名でそろっている。実践ガイド型への変更は行っていない。

## PDF ページ数
- 本1が88ページ、本2が96ページ。表紙・目次・本文・奥付・QR を画像で確認。ハングルの折り返し・字形に問題なし。

## 用語・書き方
- 屯は「타무로」。初出・著者紹介・3つの出口だけ「타무로(屯)」。
- 手帳名（辞書）：근태수첩・채산수첩・2차 수첩・상담수첩・등불 수첩・대화 수첩。窓の案：원가 수첩・단골 수첩・당번 수첩。
- 합니다体、数字は en 形式（1,000／0.5）、書体 Apple SD Gothic Neo。

## 表紙の特記
- 本1の題名「부점장」を Vision（ko-KR）が誤読して照合80%で落ちたため、本1だけ題名の書体を AppleMyungjo にした（「AI」は Apple SD Gothic Neo）。
- 手順は `i18n/ko/ko-cover-weight.mjs`：cover.mjs の後に `node i18n/ko/ko-cover-weight.mjs 700 AppleMyungjo` を続ける。本1の表紙を cover.mjs で作り直したら必ず続けて実行する。本2は標準書体で照合 OK。

## 費用
- 翻訳・組版はサブスク枠、レビューは agy。Anthropic API は不使用。

## 親への依頼・気づいた点
- cover.mjs に題名の書体・太さの指定（cover.json の font／weight）が付くと、上の後処理が不要になる。
- build 中の「name token is longer than…」警告は無害（PDF 正常・ゲート通過）。

## Hub への引き渡し
- 印：`b1-ko-pdf／-gp`、`b2-ko-pdf／-gp`。
- `i18n/ko/`：`lang.json`、`glossary.add.yaml`、`store-copy.part.html`、`<slug>/metadata.yaml`、`<slug>/work/store.json`、`<slug>/cover/cover.png`、`<slug>/build/*_ko.pdf`・`*_ko_gp.epub`、`<slug>/manuscript.md`、`<slug>/review-log.md`（未対応0）。
