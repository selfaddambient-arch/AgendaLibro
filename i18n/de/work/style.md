# ドイツ語版の文体・訳語の決め（de）

- 敬称：**Sie**（読者＝飲食店の経営者・事業者。ビジネス実用書の標準）。呼びかけは Sie/Ihr/Ihnen で通す。du は使わない（引用された第三者の会話・AIへの指示文は原文の口調に合わせ、AIへのプロンプトは「Sie」形の丁寧な依頼ではなく、原文が丁寧語なら Sie 形）。
- 文体：著者の一人称（ich）の語り。やわらかい話し言葉に近い現代ドイツ語の散文。直訳調を避け、長い日本語の一文は2文に切ってよい。ですます調の温かさは保つ。
- 性別：人物・読者・職業名は中立に。「Inhaber/Inhaberin」の対ではなく「wer ein Lokal führt」「Betreiber*」は避け、「Team」「Gäste」「Personal」「Lokalleitung」「die Person, die …」「Menschen, die …」で言い換える。総称男性（der Gast, der Mitarbeiter）は使わない。ギュメ・シュテルンヒェン（Gast*innen）も使わない。複数形・中立の名詞（Gäste, Mitarbeitende, Stammkundschaft, Personal）で書く。著者のことは「ich」、他人は名前・役割・「die Person」。
- 数字：`number_style = dot`。1.000 / 0,5 / 12,5%（％はスペースなしで英語版・インドネシア語版と同じ `40%`）。円は `¥8.500 (ca. $57)` の形（括弧の中は英語版と同じ米ドル額。`about` → `ca.`）。範囲 `¥4.500–¥5.700 (ca. $30–$38)`。
- 引用符：ドイツ語の下付き開き „ ... “ を使う。
- 図：`【Abbildung 1-1】`。コラム：`Kolumne 1`。章：`Kapitel 1`。はじめに＝`Einleitung`、おわりに＝`Nachwort`。
- 題名：本1『Die KI-Stellvertretung』／本2『Gebaut für unsere Bar』。相互参照は `*Gebaut für unsere Bar*`／`*Die KI-Stellvertretung*`。
- 画面の注：`*(The screen is in Japanese.)*` → `*(Die Bildschirmanzeige ist auf Japanisch.)*`
- 日本の補足 `*(…)*` は英語版と同じ位置にドイツ語で。
- 用語：glossary.add.yaml のとおり。Vibe Coding（ハイフンなし・大文字C）、stellvertretende Lokalleitung（短くは Stellvertretung）、Tamuro、Notizbuch（手帳）。
- 製品の呼び名：AgendaTimbro（Zeiterfassung）、AgendaOro（Rentabilität）、AgendaBis（Zweites-Lokal-Heft）、AgendaQA（Hilfe-Center）、AgendaLuce（Licht-Notizbuch）、AgendaSpunto（Gesprächsthemen）、AgendaRicetta（Wareneinsatz-Heft／窓の案）、AgendaNera（Stammgast-Heft／窓の案）、AgendaTurno（Dienstplan-Heft／窓の案）。
- 相対日付：「去年」「今年」は年を添える（2026年10月時点の記録）。
- 例外：著者が AI に打ち込む指示文・AI との会話文（プロンプト）は du 形（AI は道具として duzen する）。読者への呼びかけは常に Sie。
