# ブラジルポルトガル語（pt-BR）の報告

**状態：完了**。サブエージェントが作り、親の窓が `I18N_LANG=pt-BR gate.py` を再実行して NG 0（epubcheck エラー0・警告0、表紙照合一致）を確認した。PDF は本1が98ページ・本2が112ページ。

## 重要
- **リンクの印は `pt`（仮）**。確定したら `lang.json` の `mark` と原稿の `-pt-{{FMT}}` を差し替えて作り直す
- **Google Play：2冊とも新規**。**Kindle：対応**（KDP はポルトガル語に対応。出典 kdp.amazon.com/en_US/help/topic/G200673300）。Kindle 用 EPUB も作成

## 題名（既定は1案目）
| | 本1 | 本2 |
|---|---|---|
| 1（既定） | **Subgerente de IA**（É só conversar, e ela faz. Muito mais do que eu esperava.） | **Feito para o Nosso Bar** |
| 2（直訳） | Uma Pessoa Toca o Estabelecimento, e a IA Chegou ao Lado | O Nosso Bar, do Nosso Jeito |
| 3（実践ガイド型） | IA no Restaurante: Guia Prático para Quem Toca um Pequeno Negócio | Sistema de Reservas com IA para Bares e Restaurantes: Guia Prático |

既定を3案目に変えるかは代表の判断。

## 決めたこと
- 手帳の名前：辞書どおり Livro de Ponto・Livro de Lucros・Guia da Próxima Parada・Guia de Suporte・Caderno de Luzes・Assuntos。窓の案：Livro de Custos（原価）・Livro de Clientes Fiéis（常連）・Livro de Escalas（当番）
- ハンバーグ＝bife de hambúrguer estilo japonês（初出）。コース＝menu（curso は講座と取り違えられる）。number_style=dot（¥8.500 (cerca de US$ 57)）。人物名詞は中立な言い方。書体 Latin

## ファイルの場所
- PDF：`i18n/pt-BR/<slug>/build/bontaraku-0N_<slug>_pt-BR.pdf`／GP 用 `_pt-BR_gp.epub`／Kindle 用 `_pt-BR_kindle.epub`
- 表紙 `cover/cover.png`／書誌 `metadata.yaml`／説明文ほか `work/store.json`／ストア文言 `i18n/pt-BR/store-copy.part.html`
- リンクの印：`b1-pt-pdf／kindle／gp`、`b2-pt-pdf／kindle／gp`（受け口の許可リストには未登録）

## レビュー
`review-log.md`（未対応 0）。「ter duas caras」→duas faces、「curso」→menu、「está aberto」→Tem mesa、「tonkatsu」→tonteki など。性別の語に戻す案、原文にない語を足す案は採らなかった。agy が遅く、一部は Gemini API に切り替えた。

## 費用
翻訳：サブスク。レビュー：agy＋Gemini API（入力約10万・出力約1.3万トークン、数十円）。画像生成なし。
