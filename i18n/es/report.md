# スペイン語版（es）報告

## 状態
- 本1・本2とも最後まで完了：翻訳 → ゲート → Gemini レビュー（agy -p、全20章の返事あり）→ 反映 → 表紙 → 組版（PDF・Google Play 用 EPUB・Kindle 用 EPUB）→ ストア文言。
- `gate.py`：NG 0（組版後の最終実行。epubcheck エラー0・警告0を含む）。
- PDF：本1 100ページ、本2 114ページ。
- 注意：PDF の目次が1行だけ次ページにはみ出し、4ページ目に「Colofón」だけの頁ができる（本1で確認）。スクリプトの課題の可能性。親の窓へ：目次の組みを確認してほしい。

## Google Play／Kindle
- 本1・本2とも Google Play は新規。Kindle は対応（lang.json の kindle=true。根拠 kdp.amazon.com/en_US/help/topic/G200673300）。Kindle 用 EPUB も作成済み。

## 題名の案
本1（既定＝1案目）
1. El subgerente de IA（英題を基にした既定）
2. Una persona sola atiende el local, y la IA llegó a su lado（日本語題の直訳に近い）
3. IA para pequeños negocios: guía práctica para quien atiende solo（実践ガイド型）

本2（既定＝1案目）
1. Hecho a la medida de nuestro bar（英題を基にした既定）
2. Nuestro local, a nuestra manera（日本語題の直訳に近い）
3. Cómo construir con IA las herramientas de su restaurante: guía práctica（実践ガイド型）

既定を実践ガイド型に変えるかどうかは決めていない（代表が決める）。

## 決めたこと
- 敬称：usted／ustedes に統一（vosotros は不使用。AI への指示文も usted）。特定の国に偏る語（ordenador／móvil／celular など）は避けた。性別を示す語は「la clientela」「quien dirige el local」「la autoría」などで回避。
- 数字：dot（1.000／0,5）。円は `¥8.500 (unos US$ 57)`。為替 1ドル=150円（2026-10-29）。
- 書体：Latin（Baskerville／Georgia）。右から左・縦書きなし。cjk=false。ocr_langs=es-ES, en-US。図の言葉：Figura。
- ハンバーグ：「hamburguesa」を使わず「hanbāgu」（初出に「日本式の焼いたひき肉ステーキ、hamburg steak に近い」の訳注）。用語集で hamburguesa を禁止語にした。
- 手帳の名前（辞書 es.ts の nick に合わせたもの）：Fichajes（Timbro）、Rentabilidad（Oro）、Guía de la Siguiente Parada（Bis）、Guía de Soporte（QA）、Cuaderno de Luces（Luce）、Temas de Conversación（Spunto）。Voce は辞書どおり Voce。
- 窓の案（辞書に無い3つ）：Cuaderno de Costos de Receta（Ricetta）、Cuaderno de Clientes Habituales（Nera）、Cuaderno de Turnos（Turno）。
- 副店長＝subgerente。屯＝Tamuro。コース＝「menú」「menú degustación」（curso は料理教室のみ）。
- リンクの印は b1-es／b2-es。

## ファイルの場所（Hub／LP 用）
- メタデータ：i18n/es/{hitori-de-mise,uchi-no-mise}/metadata.yaml
- 説明文・一行紹介・キーワード・ジャンル・Kindle カテゴリ：i18n/es/<slug>/work/store.json（1枚で確認：i18n/es/store-copy.part.html）
- 表紙：i18n/es/<slug>/cover/cover.png
- PDF・EPUB：i18n/es/<slug>/build/bontaraku-0{1,2}_<slug>_es.pdf、…_es_gp.epub、…_es_kindle.epub
- 原稿：i18n/es/<slug>/manuscript.md ／ 用語集：i18n/es/glossary.add.yaml ／ 文体の決め：i18n/es/work/style.md

## review-log の要約
- 指摘数：本1 約140件、本2 約195件（各 review-log.md に全件の採否つき）。未対応0。
- 主に採ったもの：直訳調の言い換え（primera línea→el local、hacer una mejora の自然化）、意味の取り違え（ortografía→sintaxis、「空いてる」を abierto でなく hay sitio）、スペインで性的含意のある「se corre」→「se extiende」、コース／curso→menú の統一、AI 指示文の tú→usted。
- 採らなかったもの：los clientes／gestor／dueño など性別のある語への置換、題名の変更、原文にない事実、数字の変更。

## 費用
- 翻訳：サブスクの枠（窓とサブエージェント）。レビュー：agy（Gemini）。Anthropic API・Gemini API は未使用。

## 気づいた点
- 英語版に無い誤植等は未確認。本2の part-01 見出し「¿Hay algún lugar abierto esta noche?」は原文（英語版）に合わせたまま。
- 書いたのは i18n/es/ の中だけ。git は使っていない。
