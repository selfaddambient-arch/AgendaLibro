# フランス語版（fr）本2『Sur mesure pour notre bar』Gemini 校閲の採否ログ

対象：`i18n/fr/uchi-no-mise/review/*.gemini.md` 11ファイル（00, 01-1, 01-2, 01-3, 02-1, 02-2, 03-1, 03-2, 04, 05, 06）。`*.chatgpt.md` は全て空のため「非レビュー」。
修正先：`i18n/fr/uchi-no-mise/work/part-01..06.md`（`manuscript.md` は未編集）。

## 集計

- 指摘の総数：189点（「該当なし」と報告された確認項目は別掲し、数に含めない）
- 採用：174点（うち完全採用143点、一部採用31点）
- 不採用：15点

凡例：採用＝指摘どおり修正／一部採用＝指摘は認めたが、性別語を避ける・用語集に従うなどの理由で文言を変えて修正／不採用＝修正せず。

## 不採用にした基準

- 性別語の回避：`le patron`、`le gérant`、`cuisinier`、`curateur`、`seul(e)` などは中立方針に反するため採らない。`la direction` は style.md の決めで、性別語に直す指摘は採らない。
- 用語集・Hub辞書の訳語（Guide de la Prochaine Étape など）と、`【Figure …】` の印は style.md が固定している。
- 原文にない情報の追加は採らない。

## 00.gemini.md（はじめに・本の案内、part-01）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「Offrir」は無償に読めるため、章題を第3章の見出しと同じ「Partager les outils de mon établissement avec d'autres」に統一した（part-04 の「offrez-les」「rien à offrir」も「partagez」「partager」に揃えた） |
| 2 | 採用 | 「la prise en charge de chaque entreprise」を「l'état des fonctionnalités selon les fournisseurs」に直した |
| 3 | 一部採用 | 「faits」を「affirmé comme des faits des choses… jamais dites」にし、「事実を書いてしまった」という皮肉を残しつつ論理の破綻を解いた |
| 4 | 採用 | 「avant de me tourner vers la restauration」に直した（être 助動詞の過去分詞を避けた） |
| 5 | 採用 | 章題と表を「Un établissement réservé par l'IA」に統一した（書名ではなく章題のため、(a) には当たらない） |
| 6 | 採用 | 「bâtisseurs」を「créateurs」「passionnés de technologie」に直した |
| 7 | 採用 | 「versant professionnel」を「volet gestion」「volet entrepreneurial」に直した |
| 8 | 採用 | 「construire au feeling」に直した（2-4 の見出しと語を揃えた） |
| 9 | 採用 | 「en salle」を「tout en tenant mon bar au quotidien」に直した |
| 10 | 採用 | 「Ce livre aussi a été réalisé avec l'IA.」に直した |
| 11 | 採用 | 初出を「curry au steak haché (hambāgu)」にした |
| 12 | 採用 | 見出しを「Trois façons de prolonger ce livre」に直した |
| 13 | 採用 | 「trois suites possibles」に直した |
| 14 | 該当なし | 見出し・番号の不一致なし |
| 15 | 該当なし | 事実・数字の変更なし |
| 16 | 該当なし | 文の脱落なし |
| 17 | 該当なし | 日本語の残りなし |

## 01-1.gemini.md（1-1〜1-5、part-01・part-02）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「Ce n'est pas de la science-fiction.」に直した |
| 2 | 採用 | 「lui poser des questions」に直した（原文は利用者が質問できる意味） |
| 3 | 採用 | 「ma propre IA」を「leur propre IA」に直した |
| 4 | 採用 | 「空いてる」は空席の意味のため、「Y a-t-il de la place chez Tamuro ce soir ?」に直した（part-01・02・03・06 の全箇所） |
| 5 | 採用 | 「je n'ai pas obtenu ce résultat dès le départ」に直した（être 助動詞を避けた） |
| 6 | 採用 | 「légèrement sucré et bien relevé à l'ail」に直した |
| 7 | 採用 | 地の文を「On peut aussi venir sans réservation.」に直した |
| 8 | 採用 | 回想文に合わせ「Il suffisait de décrire…」「Si je demandais…」に直した |
| 9 | 採用 | 「viennent sans avoir réservé」に直した |
| 10 | 採用 | 「n'est pas qu'une simple prise de réservations」に直した |
| 11 | 採用 | 「remise pour réservation anticipée」に全箇所統一した |
| 12 | 採用 | 「au moins une semaine / deux semaines à l'avance」に直した（「jusqu'à」は条件が逆に読める） |
| 13 | 採用 | 「carte de fidélité à tampons」に直した（図の題も同様） |
| 14 | 採用 | 「je cherche d'abord à me rappeler à son bon souvenir」に直した |
| 15 | 採用 | 「plusieurs messages doivent partir le même jour」に直した |
| 16 | 採用 | 「relance des membres inactifs」に直した |
| 17 | 採用 | 「amorce de conversation」に直した |
| 18 | 採用 | 「j'ai voulu qu'il transmette à l'avance…」に直した |
| 19 | 採用 | 「Bon retour」は見送りに読めるため「Bon retour parmi nous」に直した（1-6・1-10 の同名も） |
| 20 | 採用 | 「le lien peut se nouer après coup」に直した |
| 21 | 採用 | 「où l'on vient sur réservation」に直した |
| 22 | 採用 | 「le prochain créneau libre d'aujourd'hui」に直した（本日中の枠の意味） |
| 23 | 採用 | 「anticiper les ventes à venir」に直した |
| 24 | 不採用 | 「la direction」は style.md の中立方針。「le gérant」「patron」は性別語のため採らない |
| 25 | 採用 | 「Pour suivre les chiffres」に直した |
| 26 | 該当なし | 見出し・番号の不一致なし |
| 27 | 該当なし | 事実・数字の改変なし |
| 28 | 該当なし | 文の脱落なし |
| 29 | 該当なし | 日本語の残りなし |

## 01-2.gemini.md（1-6〜1-8、part-02）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「personnes déjà arrivées」は来店客に読めるため、「visiteurs du site」「arrivés sur le site」に直した |
| 2 | 不採用 | 「lien vers l'étape suivante」は Hub 辞書の「Guide de la Prochaine Étape」（2軒目手帳）に揃えた訳語。3-3 で意味が説明される |
| 3 | 採用 | 「avis Agenda」を「présentation d'Agenda」に直した |
| 4 | 一部採用 | 「Peut-on venir en solo sans se sentir à l'écart ?」に直した（案の「seul」「elle」は性・人称が出るため避けた） |
| 5 | 採用 | 「geste fixe」を「mots-clés」「déclencher une action figée」に直した（part-02・03 の全箇所） |
| 6 | 採用 | 「je la fais produire par des calculs fixes et des phrases fixes」に直した |
| 7 | 採用 | 「définir conjointement… l'amélioration et la méthode pour en mesurer l'effet」に直した |
| 8 | 不採用 | 「la direction」は style.md の決め。「le patron」「il」は性別語のため採らない |
| 9 | 採用 | 「dans ces conditions, la clientèle ne peut pas s'y retrouver」に直した |
| 10 | 採用 | 「J'aurais pu faire le tri.」に直した |
| 11 | 採用 | 「la dimension du temps s'impose」に直した |
| 12 | 一部採用 | 「trou」を「lacune」に直した。「seule la personne qui avait construit le système」と性別語を避けた |
| 13 | 採用 | 「sur le formulaire de réservation, il était devenu difficile de choisir」に直した |
| 14 | 一部採用 | 「Pour les enfants qui n'ont pas encore l'âge d'aller à l'école primaire」に直した（「préscolaire」は年齢が曖昧なため採らず） |
| 15 | 一部採用 | 三人称の説明に合わせ「On lui indique…」に直した。「soirée」を外し「façon dont on veut profiter de sa venue」にした |
| 16 | 採用 | 「Dans la soirée du 6 octobre 2026」に直した |
| 17 | 採用 | 「J'ai failli m'en réjouir」に直した |
| 18 | 該当なし | 見出し・番号の不一致なし |
| 19 | 採用 | 「一言」を「quelques mots」に直した（「phrase」は誤り） |
| 20 | 該当なし | 訳抜けなし |
| 21 | 該当なし | 日本語の残りなし |

## 01-3.gemini.md（1-9〜1-10、part-02・part-03）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 01-1 の4と同じ（空席の意味） |
| 2 | 採用 | 「critères déjà renseignés」に直した（part-02・03） |
| 3 | 採用 | 「le lien de causalité n'est pas encore prouvé」に直した |
| 4 | 採用 | 「mis à la disposition d'autres commerces」に直した |
| 5 | 採用 | 「Un établissement réservable via l'IA ne s'est pas bâti en un jour.」に直した |
| 6 | 採用 | 「parmi les suggestions」に直した |
| 7 | 採用 | 語り手は単独のため、見出しと本文の「nous」を「j'ai」に直した |
| 8 | 採用 | 「m'attendre à une augmentation directe」に直した |
| 9 | 採用 | 「réservations anticipées supplémentaires」「remise pour réservation anticipée」に直した |
| 10 | 採用 | 「alimente les conversations au comptoir」に直した |
| 11 | 採用 | 「J'ai moi-même failli tomber dans ce piège」に直した |
| 12 | 一部採用 | 「faits documentés」に直した（「avérés」は原文にない断定のため避けた） |
| 13 | 一部採用 | 商品名として「Enchanté」「Bon retour parmi nous」と明示した。「Bienvenue」は原文「はじめまして」と合わないため採らない |
| 14 | 一部採用 | 「nombre de scénarios réussis… de 9 à 24」「11 faits」に直した。分母の「sur 36」は足さなかった |
| 15 | 該当なし | 1-9、1-10 の見出しは整合 |
| 16 | 該当なし | 数字の変更なし（「ouvert」の件は1で対応済み） |
| 17 | 該当なし | 訳抜けなし |
| 18 | 該当なし | 日本語の残りなし |

## 02-1.gemini.md（2-1〜2-2、part-03）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「dépendait moins de… que de…」に直した（要点と本文の両方） |
| 2 | 採用 | 「Tirant les leçons de ces erreurs」に直した（être 助動詞を避けた） |
| 3 | 採用 | 「ce qu'elle peut faire par cette fenêtre」に直した |
| 4 | 採用 | 「propose des outils」「les outils proposés」に直した |
| 5 | 採用 | 空席の意味（01-1 の4と同じ） |
| 6 | 採用 | 「clique sur le bouton de confirmation」に直した（図の題も） |
| 7 | 採用 | 「ce qui ne tolère aucune erreur est confié au programme…」に直した |
| 8 | 不採用 | 「la direction」は style.md の決め。「vision du patron」「propriétaire」は性別語 |
| 9 | 採用 | 「aucune information ne risque d'échapper à la recherche」に直した |
| 10 | 採用 | 「Il suffira d'adopter le RAG quand la base de connaissances aura grossi.」に直した |
| 11 | 採用 | 「remplace arbitrairement」に直した（見出し・要点・本文） |
| 12 | 採用 | 「au fil de ses idées」に直した |
| 13 | 採用 | 「type de consommation」に直した |
| 14 | 採用 | 「toute combinaison de deux axes soit couverte au moins une fois」に直した |
| 15 | 採用 | 「angle mort lié au temps」に直した |
| 16 | 採用 | 「geste fixe」の置き換え（01-2 の5と同じ） |
| 17 | 採用 | 「propose une inscription de membres」に直した |
| 18 | 一部採用 | 「préambule était facturé de nouveau」「renvoie le même préambule」に直した。案の「plein tarif」は原文にない情報のため足さなかった |
| 総括 | 該当なし | 見出し・数字・脱落・日本語の残りはいずれも問題なし |

## 02-2.gemini.md（2-3〜2-6、part-03・part-04）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 不採用 | 「Guide de la Prochaine Étape」は Hub 辞書の正式な手帳名（用語集）。架空の名前ではない |
| 2 | 採用 | 「interdire la lecture depuis l'extérieur」に直した |
| 3 | 一部採用 | 「画面から」は原文のとおり「la page」に直した。「côté client」は原文にない技術説明のため足さなかった |
| 4 | 採用 | 「casser le programme, et confirmer que le test échoue」に直した |
| 5 | 採用 | 「la validation des réservations」に直した |
| 6 | 一部採用 | 「l'administration de l'établissement」だけ「notifier l'établissement」に直した。「la direction」は style.md の決めで維持。「patron」「gérant」は性別語 |
| 7 | 採用 | 「bottom sheets」に直した |
| 8 | 採用 | 「données réelles de clients」に直した |
| 9 | 採用 | 「l'historique」「anciennes traces」に直した |
| 10 | 採用 | 「failles」「restent tapies en silence」に直した（part-04 の「trous」も「lacunes」に揃えた） |
| 11 | 採用 | 「vérification automatique」に直した |
| 12 | 採用 | 「haut et imposant」「volumineux, chargé de longues explications」「Trop chargé」に直した |
| 13 | 採用 | 「l'écriture dans le journal d'audit… échouait」に直した |
| 14 | 採用 | 「n'avait pas su produire d'images」に直した |
| 15 | 採用 | 「séparées du code de l'interface」に直した |
| 16 | 採用 | 「ne se confient pas à la génération de texte de l'IA」に直した |
| 17 | 該当なし | 見出し・番号の不一致なし |
| 18 | 該当なし | 数値の変更なし（「2軒目」の件は1で不採用） |
| 19 | 該当なし | 脱落文なし |
| 20 | 該当なし | 日本語の取り残しなし（【Figure】は style.md のとおり） |

## 03-1.gemini.md（3-1〜3-5、part-04）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 不採用 | 「la direction」は style.md の決め。「le patron」「l'exploitant」は性別語 |
| 2 | 採用 | 「la dernière commande de 22h30」に直した |
| 3 | 採用 | 「est repoussée de 30 minutes」に直した（本文と図の題） |
| 4 | 採用 | 「fermer exceptionnellement」に直した（臨時休業の意味） |
| 5 | 不採用 | 「état de la lumière」は原文の「灯り」の表現どおり。直前に「panneau」「OPEN/CLOSED」の説明がある |
| 6 | 採用 | 「J'ai conçu un widget compact」に直した（13と合わせて「widget」に統一） |
| 7 | 採用 | 「le mal est irréparable」に直した |
| 8 | 一部採用 | 「Un carnet qui… fait basculer la vie et la mort des gens」に直した |
| 9 | 一部採用 | 手帳名は用語集で固定のため表は変えず、導入文を「un surnom qui, en japonais, se termine par « techō » (carnet)」に直した |
| 10 | 採用 | 「dont le personnel compte au moins deux personnes」に直した |
| 11 | 採用 | 「la solution la plus robuste」に直した |
| 12 | 採用 | 「où finir la soirée」に直した |
| 13 | 不採用 | 「force empruntée」は直後の文で定義済み。他力の比喩を残す |
| 14 | 一部採用 | 「la lumière」を「le panneau」に直した。案の「en ligne」は足さなかった |
| 15 | 一部採用 | 「chat」が猫と読める点だけ、「la fenêtre de conversation recommande」に直した。案の「susciter la conversation」は原文の意味と違う |
| 16 | 採用 | 「vend ce qu'il propose」に直した |
| 17 | 採用 | 「intégrable」に直した |
| 18 | 採用 | 「lancer un produit sur le marché」に直した |
| 19 | 採用 | 「le seuil d'entrée s'est assurément abaissé」に直した |
| 補1 | 採用 | 総括欄の指摘（3-4 の「屯の店主だけではない」の脱落）。「Tamuro n'est pas le seul établissement…」に直した |

## 03-2.gemini.md（3-6〜3-7、part-04・part-05）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「a pris beaucoup d'ampleur」に直した |
| 2 | 不採用 | 原文の「中間層」自体が曖昧。「milieu de gamme」とすると解釈の追加になり、直後の説明とも噛み合う直訳を残した |
| 3 | 採用 | 「se sert d'un écran」に直した |
| 4 | 不採用 | 「la direction」は style.md の決め。「gérant」「patron」は性別語 |
| 5 | 採用 | 「plus proche de leur quotidien」に直した |
| 6 | 採用 | 「sites d'avis sur les restaurants」に直した（5-5 の「sites d'avis gastronomiques」も） |
| 7 | 採用 | 「commission pour chaque réservation apportée」に直した |
| 8 | 採用 | 「tout le modèle」に直した |
| 9 | 採用 | 「Si je traduis… dans le langage d'un établissement indépendant」に直した |
| 10 | 一部採用 | 本文を「Je fixe des prix bas, pour de petits montants.」に直した。節の見出しは標語のため据え置き |
| 11 | 採用 | 「activité viable à part entière」に直した |
| 12 | 採用 | 「sert à ce que l'outil continue d'être utilisé」に直した |
| 13 | 採用 | 「composant de panneau」を「widget du panneau」に統一した |
| 14 | 採用 | 「distribution」に直した |
| 15 | 一部採用 | 「développé par une seule personne… disponible dans le monde entier」に直した（「patron de bar」は性別語のため避けた） |
| 16 | 一部採用 | 「un seul établissement… une seule personne aux commandes」に直した |
| 17 | 採用 | 「fait l'objet du chapitre 4」に直した |

## 04.gemini.md（第4章、part-05・part-06）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「parcours du regard」に直した |
| 2 | 採用 | 「apparence par défaut」に直した |
| 3 | 一部採用 | 「colonne « gérant »」は性別語のため採らず、「toute ligne où l'on inscrit « direction » comme exécutant, sans pouvoir en donner la raison」に直した |
| 4 | 採用 | 「redéfini les principes」に直した |
| 5 | 採用 | 「liens vers les autres produits」に直した（要点と4-2） |
| 6 | 採用 | 「avance de façon autonome」に直した |
| 7 | 一部採用 | 「une direction de bar」は「une personne qui tient un bar」に直した。他の「la direction」は style.md の決めで維持 |
| 8 | 不採用 | 「faits sur l'établissement」は第1・2章からの統一用語。原文も「店の事実」 |
| 9 | 不採用 | 「les mots mêmes de la direction」は style.md の決め。「patron」は性別語 |
| 10 | 一部採用 | 「fabrique」を「conçoit」に直した。案の「concepteur」は男性形のため避けた |
| 11 | 採用 | 「le faible coût」に直した |
| 12 | 採用 | 「référentiel」に直した |
| 13 | 採用 | 「quatre couleurs candidates bien distinctes」に直した |
| 14 | 採用 | 「les cinq propositions」に直した |
| 15 | 採用 | 「le neuvième produit ainsi que les suivants」に直した |
| 16 | 一部採用 | 「démenti」を「J'ai écarté ce diagnostic.」に直した |
| 17 | 採用 | 「générées」に直した |
| 18 | 採用 | 「espace de stockage」に直した |
| 19 | 該当なし | 見出し・数値・脱落・日本語の残りはいずれも問題なし |

## 05.gemini.md（第5章、part-06）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「expérience fondatrice」に直した |
| 2 | 採用 | 「presque sans se mouiller」に直した |
| 3 | 不採用 | 原文は「屯一本になりました」で、決意の表明ではない。「pour me consacrer exclusivement」は原文にない意図の追加 |
| 4 | 一部採用 | 「Avant même de cuisiner, je veux faire de la curation.」に直した。案の「cuisinier」「curateur」は性別語 |
| 5 | 採用 | 「ingrédients abordables」に直した |
| 6 | 採用 | 「maîtriser la cuisson」「le soir」に直した |
| 7 | 採用 | 「nappé d'une sauce légèrement sucrée… bien relevée à l'ail」に直した |
| 8 | 採用 | 「steak haché」に直した（5-2 の見出し・本文） |
| 9 | 一部採用 | 「lié uniquement par le velouté naturel」に直した。案の「réduction」は原文にない工程のため採らない |
| 10 | 採用 | 「trois critères」に直した |
| 11 | 一部採用 | 「journées pour boire un verre en journée」に直した |
| 12 | 一部採用 | 「une seule personne」だけ直した。「la direction」は style.md の決め。「patron」は性別語 |
| 13 | 採用 | 「génèrent pas leurs revenus」に直した |
| 14 | 採用 | 「se nourrissent mutuellement」に直した |
| 15 | 一部採用 | この箇所だけ「fermetures qui se prolongent」に直した（他の「déborde」は据え置き） |
| 16 | 採用 | 「Le point d'entrée」に直した（3-6 も） |
| 17 | 採用 | 「les grands services de réservation」に直した |
| 18 | 一部採用 | 「尖る」を「affirmer sa singularité」に直した。案の「identité pointue」は足さなかった |
| 19 | 該当なし | 見出し・番号の不一致なし |
| 20 | 該当なし | 事実・数字の変更なし |
| 21 | 該当なし | 訳抜けなし |
| 22 | 不採用 | 「【Figure 5-1】」は style.md が固定した図の印 |

## 06.gemini.md（おわりに、part-06）

| 点 | 判定 | 理由 |
|---|---|---|
| 1 | 採用 | 「état des lieux arrêté à octobre 2026」に直した |
| 2 | 採用 | 「de la manière dont il s'y est pris, de ses échecs et des leçons qu'il en a tirées」に直した |
| 3 | 採用 | 「venez faire un tour chez Tamuro」に直した（part-01 の同文も） |
| 4 | 採用 | 空席の意味（01-1 の4と同じ） |
| 5 | 採用 | 「Votre premier verre vous sera offert.」に直した（「nous」の唐突さも解消） |
| 6 | 不採用 | ローマ字の「Hon o mita」は原文にない情報の追加。直訳を残す |
| 7 | 一部採用 | 「Il vous sera offert de la même façon.」に直した |
| 8 | 一部採用 | 「ne vous sentirez pas à l'écart」に直した（案の「déplacé(e)」は性別が出る） |
| 9 | 一部採用 | 「La conversation s'engagera… avec la personne à côté de vous」に直した（「voisin(e)」は避けた） |
| 10 | 一部採用 | 「dans un bar où les gens se rassemblent」に直した |
| 11 | 採用 | 「dans le podcast BG2」「actions des éditeurs de logiciels」に直した |

## 主な修正（5行）

1. 「Tamuro est-il ouvert ce soir ?」を空席の問い「Y a-t-il de la place chez Tamuro ce soir ?」に直した（4件の指摘・4箇所、part-01/02/03/06）。
2. 「trou」を「faille」「lacune」「angle mort」に、「geste fixe」を「action figée」に、「écrase de lui-même」を「remplace arbitrairement」に統一した。
3. 「remise pour réservation anticipée」「Bon retour parmi nous」「carte de fidélité à tampons」「steak haché」「widget」「point d'entrée」など、直訳調の語を全箇所そろえた。
4. 「Offrir」を「Partager」に、「Un commerce que l'IA réserve」を「Un établissement réservé par l'IA」に直し、章題・表・本文の整合を取った。
5. 「la direction」「Guide de la Prochaine Étape」「【Figure】」は style.md と用語集に従って維持し、性別語（patron、gérant、seul(e)）を入れる案は全て避けた。

## 検証

- 6ファイルとも行数は修正前と同じ（168、190、201、214、199、161行）。
- ¥・$ の金額と URL は修正前と完全一致。
- 不可分スペース（U+00A0）：通常スペースが « の後、» の前、`: ; ! ?` の前に残っていないことを確認した。
