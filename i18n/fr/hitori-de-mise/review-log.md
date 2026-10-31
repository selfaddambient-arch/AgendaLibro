# フランス語版 本1 Gemini 校閲の採否ログ（fr / hitori-de-mise）

対象：`review/*.gemini.md`（00, 01, 02, 03-1, 03-2, 04, 05, 06, 07 の9ファイル）。空ファイル（`*.chatgpt.md` 9本）は「非レビュー」。
修正先：`work/part-01..08.md`（`manuscript.md` は未編集）。行数・Markdown構造・金額・URLは不変。
凡例：採用＝修正を反映（一部＝提案の一部のみ、または自案に置換）／非採用＝反映せず（「指摘なし」を含む）。
通し番号は各 gemini.md の番号付きリスト順（05 と 06 は 1 つにまとめて出力されていたため、05＝項目1〜20、06＝項目1〜32 に分割）。03-1 の末尾「全体確認」と 03-2 の「その他の確認事項」は a, b, c… で番号を付けた。

## 集計

| ファイル | 点数 | 採用 | 非採用 |
|---|---|---|---|
| 00 | 20 | 18 | 2 |
| 01 | 18 | 13 | 5 |
| 02 | 21 | 16 | 5 |
| 03-1 | 23 | 19 | 4 |
| 03-2 | 21 | 18 | 3 |
| 04 | 17 | 13 | 4 |
| 05 | 20 | 18 | 2 |
| 06 | 32 | 27 | 5 |
| 07 | 23 | 19 | 4 |
| 合計 | 195 | 161 | 34 |

「非採用」34 件のうち、指摘なし（報告事項なし）が 15 件、実質的に退けたのが 19 件。

## 00.gemini.md（はじめに）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 採用 | 書名の「à ses côtés」と引用内の「à vos côtés」を揃えた。 |
| 2 | 採用 | 「curry-hamburger」はパンのバーガーと誤読されるため「curry au steak haché japonais (hambāgu)」に変更。 |
| 3 | 採用 | お酒が落ちていたため「des boissons」を「de l'alcool」に変更。 |
| 4 | 採用 | 画像 alt の英語（fig-01, fig-02）をフランス語化。 |
| 5 | 採用 | 一人営業の文脈で「nous」が浮くため「je」に統一し、「en mouvement」を「mes journées sont rythmées et bien remplies」に変更。 |
| 6 | 採用 | 「12年目」に合わせ「j'entame ma douzième année」に変更。「il y a douze ans」は原文が12年前なので変更なし。 |
| 7 | 採用 | 「Mon travail s'appelait」を「J'y occupais des fonctions de」に変更。 |
| 8 | 採用 | 「faisais construire」を「pour donner forme au projet」に変更。 |
| 9 | 採用 | 英語「systems guy」を原文の「システム屋」に戻し、「shisutemu-ya（métier des systèmes）」と表記。「gars」は性別語なので使わず。part-04 の2箇所も同様に修正。 |
| 10 | 採用 | 「le côté informatique」を「les équipes informatiques」に変更。 |
| 11 | 一部採用 | 「sans partage」の独裁的な響きは直した。ただし「seul」は je に掛かる性数一致になるため、「en solitaire」にした。 |
| 12 | 採用 | 「personnel sous contrat」を「prestataires externes」、「après tout」を「ne sont que」に変更。 |
| 13 | 採用 | 「orthographe」を「syntaxe」、「retenir」を「apprendre par cœur」に変更。 |
| 14 | 採用 | 「dessiner」を「concevoir」に変更。 |
| 15 | 採用 | 「sans rien garder」を「sans rien vous cacher」に変更。 |
| 16 | 採用 | 「mots rangés dans un ordre」を「une suite de mots bien ordonnés」に変更。 |
| 17 | 非採用 | 見出し不一致なし。指摘事項なし。 |
| 18 | 採用 | 項目6の再掲（12年目）。項目6で対応済み。 |
| 19 | 非採用 | 訳抜けなし。指摘事項なし。 |
| 20 | 採用 | 項目4（alt の英語）と項目9（systems guy）の再掲。両方で対応済み。 |

## 01.gemini.md（第1章）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 一部採用 | 「confident à qui parler」は誤り。「partenaire de discussion」にして「partenaire de travail」と対にした（章題・1-1・1-2 の3箇所）。 |
| 2 | 採用 | 「exploitation à une seule personne」を「les seuls à la barre」に変更。nous の複数なので性別問題なし。 |
| 3 | 採用 | 「directeurs de magasin」を「directeurs de restaurant」に変更。 |
| 4 | 採用 | 「traitement mental」を「charge mentale」に変更（Toute cette）。 |
| 5 | 採用 | 「fabriquer」を「créer」、「du commerce」を「de votre établissement」に変更。 |
| 6 | 採用 | 「fabrique」を「réalise concrètement」に変更。 |
| 7 | 採用 | 「énonce des évidences」（正論の誤訳）を「débite de belles théories」に変更。 |
| 8 | 非採用 | 「adjoint de direction」は用語集で固定済み。「second」「bras droit」への変更は不可。 |
| 9 | 採用 | 「salle de restaurant」だと厨房が抜けるため「le quotidien d'un restaurant ne se résume pas à…」に変更。 |
| 10 | 採用 | 「Le dessin de l'étiquette」を「Le graphisme de l'étiquette」に変更。 |
| 11 | 採用 | 「pénible」を「fastidieux」に変更。 |
| 12 | 採用 | 「Nous, commerces indépendants」を「Dans nos établissements indépendants, vous avez…」に変更。 |
| 13 | 採用 | 「complaisante」（独りよがり）を「manquer d'objectivité」に、「l'incertitude」を「vous laisser dans le doute」に変更。 |
| 14 | 採用 | 「individualité」を「personnalité」に変更。「commerce indépendant」は残した。 |
| 15 | 非採用 | 見出し不一致なし。指摘事項なし。 |
| 16 | 非採用 | 数字の変更なし。指摘事項なし。 |
| 17 | 非採用 | 訳抜けなし。指摘事項なし。 |
| 18 | 非採用 | 日本語の残りなし。指摘事項なし。 |

## 02.gemini.md（第2章）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 採用 | 「obstacle un peu haut」を「défi intimidant」に変更。 |
| 2 | 採用 | 「annonces」を「consignes et transmissions」に変更。 |
| 3 | 採用 | 「dans votre salle」を「sur votre lieu de travail」に変更（厨房も含める）。 |
| 4 | 採用 | 目的の関係節なので「comprenne」（接続法）に変更。 |
| 5 | 非採用 | 「traductrice」は人物の性別語になる。AI の役割名は男性形（adjoint 同様）で保つ方針。 |
| 6 | 採用 | 見出しを名詞句「Libération du…」に変更。 |
| 7 | 採用 | 「atteint l'autre personne」（害を及ぼす響き）を「parvient à l'autre personne」に、「que nous avons」を「nos」に変更。 |
| 8 | 採用 | 「fait beaucoup parler de lui」に変更。 |
| 9 | 採用 | 「accordait des « vibes »」を「se synchronisait sur les mêmes « vibes »」に変更。 |
| 10 | 非採用 | 修正案が「Même lui … il」で性別語を導入する。現行の「une personne issue du monde du shogi」は中立なので維持。 |
| 11 | 非採用 | 原文は「日本語」と明記。「langage naturel」や「votre propre langue」を足すのは原文にない補足になるため不可。 |
| 12 | 採用 | 「fait sortir」を「permet de faire émerger」に変更。 |
| 13 | 採用 | 「partie de balle」を「échange … vient de s'engager」に変更。 |
| 14 | 採用 | 「Je vous ai présenté」は誤訳。「C'est alors que j'ai adopté」に変更。 |
| 15 | 採用 | 「De réserve」を「En réserve」に変更。 |
| 16 | 採用 | 主語の取り違えを直し「quand l'IA vous fournit un code source corrigé」に変更。 |
| 17 | 採用 | 「étudier」を「acquérir」に変更。 |
| 18 | 採用 | 項目6の再掲（2-3 見出し）。項目6で対応済み。 |
| 19 | 非採用 | Mac の併記は英語版にも同じ併記がある（全言語共通の方針）。原文にはない追記だが、英語版との整合のため据え置いた。要確認として報告。 |
| 20 | 非採用 | 訳抜けなし。指摘事項なし。 |
| 21 | 採用 | alt 3箇所（fig-03〜05）をフランス語化。 |

## 03-1.gemini.md（第3章前半）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 採用 | 原文は「人と動物が」だが、直前の「男の子たちのポーズはそのまま」と矛盾するため「le chien était proprement remplacé」に変更。原文側の不整合なので要確認。 |
| 2 | 採用 | 「réécris」を「redessine」に変更。 |
| 3 | 採用 | 「Ouverture des verres」を「Ouvert en journée pour trinquer à la nouvelle année」に変更。 |
| 4 | 採用 | 「dessin plat / design plat」を「flat design」に変更（part-03 と part-04 の2箇所）。 |
| 5 | 採用 | 「modèles de conversations」を「expressions pour les conversations de tous les jours」に変更。 |
| 6 | 採用 | 3箇所の「commerce」を「établissement」に変更。「bar」は昼営業の店と合わないため使わず。 |
| 7 | 採用 | 見出しを「ajuster la « vivacité »」に変更（原文は「賑やかさ」）。 |
| 8 | 採用 | 「rends le tout net」を「épurer l'ensemble」に変更。 |
| 9 | 採用 | 「a supporté」（我慢した、と読める）を「s'est prêtée de bonne grâce」に変更。 |
| 10 | 採用 | 「à l'air chaud」を「bien chaudes」に変更。 |
| 11 | 採用 | 「couleur」の重複を解消し「le rendu doit rester fort même en monochrome」に変更。 |
| 12 | 採用 | 「squelettes」を「ossature」に変更し、動詞を単数に直した。 |
| 13 | 採用 | 「espace joyeux」を「espace, pour une impression plus légère et joyeuse」に変更。 |
| 14 | 一部採用 | 「mettre un vœu」は不自然。「l'intention que j'ai voulu donner à mon bar」に変更（提案の「âme」は意味を足すため不採用）。 |
| 15 | 非採用 | 「(la messagerie la plus populaire au Japon)」は原文にない事実の追加に当たる。 |
| 16 | 一部採用 | 見出しの「Un toast」を「Trinquer」に変更。「zodiaque oriental」への置換は原文の干支に説明を足す形になるため据え置き。 |
| 17 | 採用 | 「highballs (whisky-soda)」と補った。 |
| 18 | 非採用 | 「sur recommandation」は書名・用語集・図キャプションで固定済み。「parrainage」は制度の中身を変えてしまう。 |
| 19 | 採用 | alt 英語（fig-06〜13、全8点。part-03 の分）をフランス語化。fig-14〜16 は part-04 側で対応。 |
| a（全体確認：見出し・番号） | 非採用 | 不一致なし。指摘事項なし。 |
| b（全体確認：事実・数値） | 採用 | 項目1の再掲（人と動物の置換）。項目1で対応済み。 |
| c（全体確認：訳抜け） | 非採用 | 訳抜けなし。指摘事項なし。 |
| d（全体確認：alt の英語11点） | 採用 | 項目19の再掲。fig-06〜16 を全てフランス語化。 |

## 03-2.gemini.md（第3章後半）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 採用 | 「pour l'application LINE」（申請の取り違え）を「pour la soumission à LINE」に変更。 |
| 2 | 採用 | 「grossière」を「pixélisée」に変更。 |
| 3 | 採用 | 「pas si gentille」を「pas si rose」に変更。 |
| 4 | 採用 | 「fabrication du logo」を「création du logo」に変更。 |
| 5 | 採用 | 「sans bruit」を「discrètement refermé」に変更。 |
| 6 | 採用 | 「partie de balle」を「échange de balles」に変更（part-04）。 |
| 7 | 採用 | 「le plus grand mur」を「le plus grand obstacle」に変更。 |
| 8 | 採用 | 「lamentable」を「affreusement tronquée」に変更。 |
| 9 | 採用 | 「seau de grille」を「méthode de la grille et du seau」に変更。 |
| 10 | 採用 | 「stickers uniques」を「récupérés chacun sous la forme d'un sticker à part entière」に変更。 |
| 11 | 採用 | 「bouton de lecture」を「bouton d'exécution」に変更。 |
| 12 | 採用 | 「photographiez-le」を「capturez-le」に変更。 |
| 13 | 採用 | 「de formation littéraire」を「sans bagage technique」に変更。 |
| 14 | 採用 | 「systems guy」2箇所を「dans le domaine des systèmes」「du monde des systèmes」に変更（00 の項目9と同じ）。 |
| 15 | 採用 | 「transfert」を「délégation totale」に変更（丸投げ）。 |
| a（見出し・番号） | 非採用 | 不一致なし。指摘事項なし。 |
| b（事実・数字） | 非採用 | 変更なし。指摘事項なし。 |
| c（脱落：Gemini の台詞「動く」） | 採用 | 「pour qu'il s'exécute」を補った。 |
| d（脱落：コラム①冒頭の述語なし） | 採用 | 「Revenons sur « Google Colab », évoqué dans le texte principal.」に変更。 |
| e（日本語の残り） | 非採用 | 残りなし。指摘事項なし。 |
| f（英語の残り：fig-17, fig-18 の alt） | 採用 | 2点ともフランス語化。 |

## 04.gemini.md（第4章）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 採用 | 「perle」は誤訳（Gem の取り違え）。「Gem de la carte des vins」に変更し 4-3 の表記と揃えた。 |
| 2 | 採用 | 「déçu」（がっかり）を「d'une simplicité désarmante」に変更。 |
| 3 | 採用 | 「décisif」を「décidé sans hésiter, et réaliste」に変更（原文は「迷わず」）。 |
| 4 | 採用 | 「du monde entier」を「générales et conventionnelles」に変更（世間一般的）。 |
| 5 | 採用 | 「regarder votre dos」の比喩が通じないため「former en montrant l'exemple」に変更。次行の「dos」も「exemple」に揃えた。 |
| 6 | 非採用 | 「(sur LINE, l'équivalent de WhatsApp au Japon)」は原文にない説明の追加に当たる。 |
| 7 | 採用 | 「fabrication」を「élaboration」に変更。 |
| 8 | 一部採用 | 「moitié basse」を「moitié inférieure」に変更。提案の文の結合は行数が変わるため見送り（原文も体言止め）。 |
| 9 | 採用 | 「la manière dans lesquels」を「le style à adopter」に変更。 |
| 10 | 採用 | 「graisse comparable」を「gras savoureux, comparable」に変更。 |
| 11 | 一部採用 | 「des propriétaires」を「votre travail de propriétaire」「La décision finale vous revient」に変更。「patron」「gérant」は性別語なので使わず。 |
| 12 | 採用 | 「parte chez la clientèle」を「avant de servir quoi que ce soit à la clientèle」に変更。 |
| 13 | 採用 | 「chose vivante」を「matière vivante」に変更。 |
| 14 | 採用 | 項目1の再掲（見出し）。項目1で対応済み。 |
| 15 | 非採用 | 数字の変更なし。指摘事項なし。 |
| 16 | 非採用 | 訳抜けなし。指摘事項なし。 |
| 17 | 非採用 | 日本語の残りなし。指摘事項なし。 |

## 05.gemini.md（第5章）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 採用 | 条件法「devrait」だと自信が疑いに読めるため「Ma cuisine est pourtant bonne.」に変更。 |
| 2 | 採用 | 「discours d'encouragement」を「m'en remettre à du pur volontarisme」に変更（精神論）。 |
| 3 | 採用 | 「sincère」を「pressant」に変更（切実）。 |
| 4 | 採用 | 「Les faits froids」を「La froide réalité des faits」に変更。 |
| 5 | 非採用 | 提案の「patron」は性別語。「propriétaire」単数も le/la が付いて性別が出る。「la direction」は style.md が中立語として認めている。 |
| 6 | 採用 | 「occasion manquée」を「manque à gagner」に変更（機会損失）。 |
| 7 | 採用 | 名詞扱いの「à volonté」を直した（「La formule boissons à volonté」「l'offre à volonté」「Afficher une formule à volonté」）。 |
| 8 | 採用 | 「Pendant ce temps」を「En revanche」に変更。 |
| 9 | 採用 | 「fait bon marché」を「fait bas de gamme」に変更（安っぽい）。 |
| 10 | 採用 | 「exactement juste」を「en plein dans le mille」に変更（図星）。 |
| 11 | 採用 | 「ne l'a pas manqué」を「Cela n'a pas échappé à l'IA」に変更。 |
| 12 | 採用 | 比較構文に合わせて「Plutôt que de faire le cool et de voir mes ventes baisser, autant tout tenter」に変更。 |
| 13 | 採用 | 「y ai repensé」を「l'idée m'est aussitôt revenue」に変更（revenue は「idée」に一致するので性別問題なし）。 |
| 14 | 採用 | 「matériel」を「éléments visuels」に変更し、動詞・形容詞を複数に直した。 |
| 15 | 採用 | 「Menu Course」を「Menu dégustation」に変更（金額は不変）。 |
| 16 | 採用 | 「la dépense par client」を「le ticket moyen」に統一（5箇所＋「dépense globale」1箇所。part-05 と part-06）。 |
| 17 | 採用 | 「Vérifier les réponses」を「Évaluer les résultats」に変更（見出しと本文）。 |
| 18 | 採用 | 「C'était chargé」を「Il y a eu du monde」に変更。 |
| 19 | 採用 | 「fait les chiffres」を「j'ai fait mon chiffre」（成句）に変更。 |
| 20 | 非採用 | 「○○0000 yens」は原文「○○万円」の伏字展開で、金額表記は変更しない方針。提案の「○○0 000」は桁区切りが誤り。他の項目は指摘なし。 |

## 06.gemini.md（第6章）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 採用 | 「sûrement」を「assurément」、「Même cela」を「Rien que cela」に変更。 |
| 2 | 採用 | 「comme une histoire」を「comme une simple lecture」、台詞を「On peut aller jusque-là avec l'IA.」に変更。 |
| 3 | 採用 | 見出しを「ne répondent pas à mes besoins précis」に変更（痒いところの比喩が通じない）。 |
| 4 | 採用 | 「par-dessus des plateformes」を「sur des plateformes」に変更。 |
| 5 | 採用 | 「atterrirai」を「solde prévisionnel de fin de mois」に変更。 |
| 6 | 採用 | 「Cela suffisait déjà à être pratique」を「C'était déjà très pratique en soi」に変更。 |
| 7 | 採用 | 「ce serait mauvais」を「il ne faut pas que」に変更。 |
| 8 | 採用 | 原文は「最大の山場」。「plus gros obstacle」を「passage le plus décisif」に変更。 |
| 9 | 採用 | 原文は「必ず」。「sûrement」を「inévitablement」に変更。 |
| 10 | 採用 | 「ont des erreurs」を「font des erreurs」に、文末の構文を「tient à ce que l'on renonce … ou que l'on cherche」に変更。 |
| 11 | 採用 | 「l'écran d'erreur」を「le message d'erreur」に変更（コピペ対象）。 |
| 12 | 採用 | 「design cassé」を「mise en page complètement brute」に変更。 |
| 13 | 採用 | 「jusqu'à hier」を「encore hier」に変更。 |
| 14 | 採用 | 「Il a expiré」を「Ce mode est arrivé à expiration」に変更（代名詞の曖昧さ解消）。 |
| 15 | 採用 | 「est revenue sans encombre」を「s'est remise à fonctionner sans problème」に変更。 |
| 16 | 採用 | 「GeminiNano」を「Gemini Nano」にして、主語を「Ce système」にした。 |
| 17 | 非採用 | 「en tant que restaurateur」は自己言及で性別が出る（単数、冠詞なしの呼びかけではない）。現行の言い換えを維持。 |
| 18 | 非採用 | 「Kakubin（サントリー）」の補足は原文にない事実の追加に当たる。 |
| 19 | 一部採用 | 原文は「店主の顔」。「du propriétaire du bar」は性別が出るため、「la personne qui tient le commerce」に変更（fig-27 の alt）。 |
| 20 | 採用 | 「bâton」を「bâton de magicien」に変更（杖の比喩）。 |
| 21 | 非採用 | 「APPI」「RGPD の同等物」は原文にない説明の追加に当たる。 |
| 22 | 採用 | 「personne ne viendra aider」を「vous aider」に変更。 |
| 23 | 採用 | 「sauvegarde analogique」を「solution de secours analogique」に変更（IT のバックアップと混同されるため）。 |
| 24 | 採用 | 「comportement d'adulte responsable」を「relève du savoir-vivre」に変更（大人の嗜み）。 |
| 25 | 採用 | 「ne répond à personne」を「ne dépend de personne」に変更。 |
| 26 | 一部採用 | 「店主としての」が落ちていたため「quelqu'un qui, à la tête de son commerce, pensait」に変更。「commerçant」は性別語なので使わず。 |
| 27 | 採用 | 「pourquoi pas Excel」を「pourquoi Excel ne ferait pas l'affaire」に変更。 |
| 28 | 採用 | 「ne casse pas」を「ne plante pas」に変更。 |
| 29 | 非採用 | 見出し・番号の不一致なし。指摘事項なし。 |
| 30 | 採用 | 項目9（必ず）と項目19（店主の顔）の再掲。両方で対応済み。 |
| 31 | 採用 | 項目26（店主としての）の再掲。項目26で対応済み。 |
| 32 | 非採用 | 「○○」は原文の伏字記号をそのまま残す方針。「XX」に変えると数値表記の置換になる。項目18の Kakubin 補足も不採用のため行は不変。 |

## 07.gemini.md（おわりに）

| 点 | 採否 | 理由 |
|---|---|---|
| 1 | 一部採用 | 「agaçant」を「fastidieux」に変更（面倒な）。「(reçu sur LINE ou WhatsApp)」は原文にない追加なので不採用。 |
| 2 | 一部採用 | 「hors du commun」の誇張を直し、「Mon expertise en IA n'a rien d'exceptionnel」に変更。「spécialiste/expert」単数は性別が出るため避けた。 |
| 3 | 採用 | 綴りの誤り「reameniez」を「reteniez」に変更。 |
| 4 | 採用 | 「égoïsme」を「j'ai fait des caprices」に変更（ワガママ）。 |
| 5 | 一部採用 | 「lire les coups」を「anticiper les coups」に変更。「(les échecs japonais)」は原文にない説明なので不採用（第2章で shogi は既出）。 |
| 6 | 採用 | 「Remets」を「Rajoute」、「Comme dire」を「Comme lorsqu'on dit」に変更。 |
| 7 | 採用 | 「ligne de front」3箇所を「terrain」に変更（le « terrain » / les réalités du terrain / le souhait du terrain）。 |
| 8 | 採用 | 「chef de l'IA」を「chef d'orchestre de l'IA」に変更。 |
| 9 | 採用 | 「faire mieux vendre」を「faire pour que ce plat se vende mieux」に変更。 |
| 10 | 採用 | 「aisance」（裕福さ）を「sérénité」に変更（ゆとり）。 |
| 11 | 採用 | 「sorties」を「prolongements」に変更（出口）。 |
| 12 | 非採用 | 「plateforme japonaise note」は原文にない説明の追加に当たる。固有名と URL はそのまま。 |
| 13 | 採用 | 「que je construis ensuite」を「que je construirai ensuite」に変更（次に作る道具）。 |
| 14 | 採用 | 「pour la première fois」は原文にない。「Quand j'ai écrit ce livre」に変更。 |
| 15 | 採用 | 「venues」を「qui viennent」、「Nous vous offrirons」を「Je vous offrirai」（2箇所）に変更し、前後の je に揃えた。 |
| 16 | 採用 | 合言葉を「Je viens de la part du livre」に変更（「J'ai vu le livre」は目撃報告に読める）。 |
| 17 | 採用 | 「curry hamburger」を「curry au steak haché japonais (hambāgu)」に変更。part-08 の alt（fig-28）も揃えた。 |
| 18 | 採用 | 「menu du jour changeant chaque jour」の重複を「menu fixe différent chaque soir」に変更。 |
| 19 | 採用 | 「forte」「la direction du commerce」は女性形・主語のすり替え。「riche de cette expérience, Raku Bonta utilise … pour gérer son propre commerce」に変更（提案の「il」は性別語なので不採用）。 |
| 20 | 非採用 | 見出し・番号の不一致なし。指摘事項なし。 |
| 21 | 採用 | 項目14（pour la première fois）の再掲。項目14で対応済み。 |
| 22 | 非採用 | 訳抜けなし。指摘事項なし。 |
| 23 | 非採用 | 日本語の残りなし。指摘事項なし。 |

## 付記（校閲外で直した箇所）

- part-01：「tenu le commerce seul」を「tenu le commerce à moi seul」に変更。je に掛かる男性形の一致を避けるため。
- part-08：項目19で述べたとおり、「forte」も同じ理由で除去。

## 主な修正の要約（5行）

1. 画像 alt の英語残りを全てフランス語化（fig-01〜18, 28）。「systems guy」は「システム屋」に戻した（shisutemu-ya）。
2. 「hamburger」の誤解を解消（hambāgu）。「ligne de front」「confident」「dessin plat」など直訳のずれを訂正。
3. 誤訳の修正：12年目、perle→Gem、déçu→désarmante、bâton、ticket moyen、manque à gagner、Check（評価）など。
4. 性別語は導入せず中立を維持（patron、il、traductrice、restaurateur は不採用）。je への性数一致も除去（seul、forte）。
5. 原文にない補足（LINE、APPI、Kakubin、note、shogi、zodiaque）は不採用。金額・URL・行数は不変。

## 紹介制の表現の削除（2026-10-31）
紹介制の表現を代表の指示で全言語から削除（本1のみ。過去の採否の記録は書き換えていない）。
