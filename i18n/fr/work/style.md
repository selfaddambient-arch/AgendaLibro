# フランス語版の文体・表記の決め（fr）

担当言語 `fr`（リンクの印 `fr`）。訳者は全員この決めに従う。

## 敬称・文体
- 読者への呼びかけは **vouvoiement（vous）**。丁寧だが硬すぎない、現場の店主に話しかける実用書の口調。
- 語り手（著者）は **je**。過去の出来事は passé composé を基本にし、背景は imparfait。
- 「です・ます」の温度感を保ち、広告調・大げさな形容は避ける。英語版より少し短く、自然なフランス語の文にする（直訳調を避ける）。

## 性別を示さない書き方（人物の代名詞は they 相当の中立）
- 著者・店主・スタッフ・お客様・実在の人物について、性別が出る語を使わない。
- **je / vous が主語の être 助動詞の過去分詞・形容詞の一致を避ける**。例：「je suis devenu(e)」「vous êtes occupé(e)」は書かない。
  avoir 助動詞の動詞（j'ai fini, j'ai décidé）、名詞（ce fut une joie）、非人称（il m'a semblé）、言い換え（「je me suis mis à」→「j'ai commencé à」）で避ける。(e) や中黒の併記もしない。
- 第三者は総称の複数形（les clients, la clientèle, l'équipe, les gens）か、名前・役割を表す無性の言い方（le commerce, l'établissement, la direction, le personnel, la personne）で書く。
  単数でどうしても指す必要があるときは **「la personne」「quelqu'un」「on」**。性別の語（propriétaire 単数の le/la、patron/patronne、serveur/serveuse 等）に直す指摘は採らない。
  「propriétaire」「exploitant」「restaurateur」を **複数形（les propriétaires, les restaurateurs）や、無冠詞の呼びかけ** で使うのは可。
- 「ancien informaticien」などの職歴は「issu de l'informatique」「qui venait de l'informatique」と言い換える。
- 副店長（AI）は役割の名詞 **adjoint**（AI は人ではないので男性形の役割名でよい）。初出は「adjoint de direction」、以後「adjoint」。

## 記号・引用
- 引用符は **« … »**（内側は半角スペースで書いてよい。後で組版用に不可分スペースへ一括変換する）。入れ子は “ ”。
- アポストロフィは **ASCII の ' のまま**（用語集の `Guide d'assistance` などと一致させるため）。
- コロン・セミコロン・! ・? の前、« の後と » の前は半角スペースを 1 つ入れる（後で U+00A0 に一括変換）。ただし URL・画像行・表の中の `|` は触れない。
- 破折りの長い ― は使わず、必要なら「 – 」（半角スペースつきのen dash）か、文を分ける。英語版の em dash は自然な句読点に直してよい。
- 英語版のイタリック `*…*`・太字・括弧の補足 `*(…)*` の位置は英語版と同じ。

## 数字・金額
- `number_style = space`：千の位は **不可分スペース（U+00A0）**、小数は **コンマ**。例 `¥8 500`、`0,5`、`$1 200`、`3,5 %`。
  4桁の数も `¥2 200`（英語版 `¥2,200` と同じ値）。年号（2026）・ページ番号・番号は区切らない。
- 金額は **英語版と同じ並び**：`¥8 500 (environ $57)`。¥ と $ は **数字の前**（gate が検査）。範囲は `¥4 500–¥5 700 (environ $30–$38)`。
  英語版の `(about $57)` は `(environ $57)`、`(roughly $…)` も `(environ $…)`。入れ子の括弧は英語版と同じ形のまま。
- パーセントは `88 %`（前に不可分スペース）。時刻は `19 h 30` ではなく `19h30`。月・日は `le 10 octobre 2026`、`1er novembre`。

## 見出し・図・用語
- `## Chapter 2: …` → `## Chapitre 2 : …`（コロンの前にスペース）。`Column 1` → `Encadré 1`。`Introduction` → `Introduction`、`Afterword` → `Postface`。
- 図の印 `【Figure 1-1】` はそのまま `【Figure 1-1】`（fig_label は Figure）。画面の注 `*(The screen is in Japanese.)*` → `*(L'écran est en japonais.)*`。
- 商品名 AgendaTimbro などは変えない。手帳の名前は `glossary.add.yaml`：Pointages／Rentabilité／Guide de la Prochaine Étape／Guide d'assistance／Carnet de Lumière／Sujets de conversation（以上は Hub 辞書）、Prix de revient／Carnet des habitués／Planning d'équipe（窓の案）、Voce。
- `屯` ＝ Tamuro。T-AI-MURO・Quatre Épices はそのまま。
- 日本の補足 `*(…)*`（東中野・LINE・居酒屋）は英語版と同じ位置にフランス語で。
- 相互参照の題名：本1 = *L'adjoint IA*、本2 = *Sur mesure pour notre bar*（本文中ではこの題名を `*…*` で）。
- 「前作」「去年」など相対的な日付は、英語版の書き方に従う（必要なら年を添える）。

## 題名（既定）
- 本1：**L'adjoint IA** ／ 副題：Il suffit de lui parler, l'IA s'occupe du reste. Bien plus que je ne l'imaginais.
- 本2：**Sur mesure pour notre bar** ／ 副題：Comment un bar de 19 places a tout construit avec l'IA, des réservations aux outils
