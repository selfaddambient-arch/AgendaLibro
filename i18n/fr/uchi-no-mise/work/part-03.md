Ce qui semble fonctionner, mais dont le lien de causalité n'est pas encore prouvé. Que davantage de clients viennent en groupe grâce à la remise de groupe. Que les formules « Enchanté » et « Bon retour parmi nous » sont choisies. Que le sujet de l'e-mail de confirmation alimente les conversations au comptoir. Je le sens en salle, mais je ne peux pas dire « sans ce système, ils ne seraient pas venus ».

Ce qui a été construit, mais dont j'ignore encore l'effet. Combien de réservations anticipées supplémentaires la remise pour réservation anticipée apportera. Combien de réservations arriveront réellement par MCP. Je viens à peine de commencer à mesurer avec le rapport hebdomadaire, et les chiffres viendront plus tard.

Il faut regarder séparément l'émerveillement de « j'ai pu construire autant avec l'IA » et le résultat de « en quoi cela a changé l'activité ». Sans cette distinction, construire devient en soi le but. J'ai moi-même failli tomber dans ce piège (comme je l'ai écrit en 1-7).

L'histoire de ce qui se cache derrière ce système de réservation, la technique, continue au chapitre 2. Si la technologie ne vous intéresse pas, passez au chapitre 3. J'y raconte comment les petits outils nés autour de ce système de réservation sont aussi mis à la disposition d'autres commerces.

## Chapitre 2 : La technique – Les coulisses du système de réservation

Points clés de ce chapitre

- La qualité des conversations de l'IA dépendait moins de l'intelligence de l'IA que des « faits sur l'établissement que nous lui remettons » et de « la présence ou non d'un programme qui remplace arbitrairement les réponses de l'IA »
- Le système de réservation que j'avais construit au feeling comportait encore une faille qui laissait lire de l'extérieur les informations personnelles de la clientèle, et zéro test automatisé. J'ai fait auditer le système par l'IA pour les trouver, et je les ai fait corriger par l'IA
- Tirant les leçons de ces erreurs, j'ai changé ma façon de construire : définir les besoins en détail avant de construire, et remettre à l'IA la spécification elle-même pour qu'elle l'implémente

(Ce chapitre contient beaucoup de termes techniques. Si la technologie ne vous intéresse pas, vous pouvez passer directement au chapitre 3, et l'histoire se poursuit sans rupture.)

### 2-1 Comment fonctionne le serveur MCP

MCP (Model Context Protocol) est un ensemble commun de conventions permettant à l'IA d'utiliser des outils et des données extérieurs. Proposé par Anthropic, il est désormais pris en charge par de nombreuses IA, dont ChatGPT et Claude.

Pour faire une analogie, MCP est une norme de prises électriques, pour l'IA. Comme la forme de la prise est fixée, les appareils de n'importe quel fabricant fonctionnent une fois branchés. De la même façon, si vous construisez une fenêtre à la forme de MCP, n'importe quelle IA peut utiliser cette fenêtre.

Un serveur MCP indique à l'IA « ce qu'elle peut faire par cette fenêtre ». Le serveur MCP de Tamuro, par exemple, propose des outils comme les suivants.

- Lire les informations de l'établissement (horaires d'ouverture, nombre de places, règles de la maison, ambiance)
- Lire les formules et les prix (le résultat du calcul des remises selon le nombre de personnes et la date)
- Lire les créneaux libres (les horaires disponibles à la réservation un jour donné)
- Créer l'URL d'une page de réservation avec les critères déjà renseignés

Quand une personne demande à sa propre IA : « Y a-t-il de la place chez Tamuro ce soir ? », l'IA se connecte au serveur MCP de Tamuro, choisit « lire les créneaux libres » parmi les outils proposés, et l'appelle. Le serveur de Tamuro renvoie le résultat, et l'IA le met en mots pour la personne.

L'important, c'est que l'IA ne confirme pas les réservations de son propre chef. Dans la première version, j'ai délibérément laissé la confirmation de réservation hors des outils. Tout ce que l'IA peut faire, c'est lire et guider vers une page de réservation avec les critères déjà renseignés. C'est la personne elle-même qui clique sur le bouton de confirmation, sur la page de Tamuro. Le danger de voir l'IA créer en masse des réservations erronées ou des canulars est écarté dès le départ par la conception.

Le calcul des prix utilise le même mécanisme de calcul que le site de réservation. Les prix affichés dans le formulaire de réservation, dans la fenêtre de conversation et via MCP sortent tous d'un seul et même programme. C'est l'autre sens de la tâche dont je parlerai plus loin, « rassembler le calcul des remises en un seul endroit ».

【Figure 2-1】De l'IA de la clientèle à la page de réservation de Tamuro. La personne clique sur le bouton de confirmation

### 2-2 Comment fonctionne la fenêtre de conversation « T-AI-MURO »

#### Les prix viennent du programme, les mots de l'IA

T-AI-MURO sépare les rôles en deux. Le programme produit les prix et les créneaux libres par des calculs fixes, et l'IA les met en mots pour la clientèle.

L'IA est douée pour produire du texte, mais rien ne garantit qu'elle calcule correctement à chaque fois. Le cumul des remises, les paliers selon le nombre de personnes, le nombre de jours de la remise pour réservation anticipée, la possibilité de la combiner avec le happy hour. Si vous laissez toutes ces règles à l'IA, elle se trompera forcément quelque part. Et une erreur de prix nuit plus que tout à la confiance de la clientèle.

Ainsi, ce qui ne tolère aucune erreur est confié au programme, et ce qui demande de la douceur dans l'expression revient à l'IA. Cette répartition est le premier principe de la construction de la fenêtre de conversation.

#### Pour un petit commerce, nul besoin de RAG

Pour que l'IA réponde à propos de l'établissement, il faut lui remettre la connaissance de l'établissement. Une méthode couramment utilisée est le RAG (génération augmentée par récupération). On découpe la connaissance en petits morceaux que l'on stocke, et à chaque question qui arrive, on retrouve seulement les parties qui semblent pertinentes et on les remet à l'IA. Quand la connaissance est vaste, cette méthode est indispensable.

Mais la connaissance de Tamuro n'est pas si grande. L'histoire de l'établissement, la cuisine, les règles, l'ambiance, la pensée de la direction. Le tout tient aisément dans ce que l'IA peut lire en une fois.

À Tamuro, j'ai donc choisi de faire lire à l'IA tout le texte de la connaissance de l'établissement à chaque fois. Il n'y a pas besoin de construire de mécanisme de recherche comme l'exige le RAG, et aucune information ne risque d'échapper à la recherche. Au début, je prévoyais de réutiliser un mécanisme de RAG, mais en cours de route j'ai opté pour l'approche du texte intégral.

Lui faire lire tout le texte à chaque fois coûte plus cher en frais d'IA. J'utilise donc un mécanisme qui réutilise le même texte pour réduire les coûts d'entrée (le prompt caching : au lieu de faire relire à l'IA le même préambule à chaque fois, elle se souvient de ce qu'elle a déjà lu). Il suffira d'adopter le RAG quand la base de connaissances aura grossi.

#### Un programme qui remplace arbitrairement les réponses de l'IA

Au chapitre 1, j'ai écrit que seuls 9 sur 36 avaient réussi au premier test. Une partie de la cause tenait à la façon dont le programme était construit.

En enquêtant, j'ai trouvé un mécanisme resté en place où le programme jugeait par mots-clés la réponse produite par l'IA et la remplaçait par une phrase fixe. Quand des mots comme « réservation » ou « aujourd'hui » apparaissaient, il jetait la réponse de l'IA et la remplaçait par une liste de créneaux libres. Même quand l'IA répondait correctement, la réponse n'atteignait jamais la clientèle.

J'ai en outre découvert que le corps de la connaissance de l'établissement (33 sections) n'était pas inclus dans les instructions données à l'IA. L'IA répondait sans connaître l'établissement.

La qualité des conversations de l'IA dépendait moins de l'intelligence de l'IA elle-même que des faits sur l'établissement qu'on lui remettait et de la présence ou non d'un programme qui remplaçait arbitrairement les réponses de l'IA.

#### Compléter par le comptage les questions-réponses attendues

J'ai fait passer les scénarios de test des 36 initiaux à 110, puis à 355. Mais si l'on ajoute les scénarios au fil de ses idées, il n'y a aucun moyen de savoir s'il en manque. À la question « Est-ce exhaustif ? », la réponse honnête était « Non, ce ne l'est pas ».

Plutôt que d'élargir la couverture par l'imagination, j'en ai donc fait une affaire de comptage par machine des endroits où l'on n'est pas encore passé, pour les combler. Pour quatre choses : les 33 sections de la connaissance de l'établissement, les transitions entre les choix, les paliers des remises, et les combinaisons de créneaux horaires et de jours de la semaine. Je compte combien de fois chacun a été traversé pendant les tests, et j'ajoute automatiquement des scénarios là où le compte est zéro.

J'ai aussi utilisé une méthode croisant six axes (nombre de personnes, but, type de consommation, date et heure, formulation, menu) et créant des scénarios de sorte que toute combinaison de deux axes soit couverte au moins une fois.

J'ai aussi trouvé un angle mort lié au temps. « Aujourd'hui » et « à partir de maintenant » sont déterminés par l'heure réelle de l'exécution du test, de sorte que les résultats d'une exécution à midi et d'une exécution le soir diffèrent. J'ai donc figé l'horloge pendant les tests et je les ai fait tourner à cinq moments : avant l'ouverture, pendant les heures d'ouverture, juste avant la fermeture, un jour de repos habituel et un jour férié.

Les réponses de l'IA varient légèrement à chaque fois, même pour la même question. Pour les scénarios directement liés aux ventes, j'ai posé la condition de les réussir trois fois sur trois quand on les exécute trois fois.

#### Quand un mauvais chiffre sort, soupçonnez d'abord le test

Dans le test qui a fait tourner 355 scénarios à 5 moments, sur 1775 conversations, 28,5 % ont réussi.

Au lieu de commencer à corriger tout de suite, j'ai d'abord démêlé : « Ce chiffre est-il vraiment une faiblesse de T-AI-MURO, ou le test est-il faux ? » Si l'on corrige alors que le test est faux, on finit par « corriger » même les bonnes réponses.

| Cause de l'erreur | Nombre |
| --- | --- |
| Une phrase fixe détourne la question | 276 |
| Ne répond pas à la question, passe au parcours de réservation ou aux recommandations | 266 |
| Panne de l'environnement de test (T-AI-MURO n'a pas pu produire de réponse à cause du plafond de coût) | 211 |
| Erreurs sur les dates, les jours de la semaine, les jours fériés, les jours de repos | 142 |
| Invention ou affirmation de faits que l'établissement n'a pas, promesse de transmettre des messages | 119 |

Les deux premières partageaient la même racine : « réagir à des mots-clés et déclencher une action figée avant de répondre à la question de la clientèle ». Les 211 de la troisième place n'étaient pas des erreurs de T-AI-MURO. Le plafond de coût a été atteint en cours de test, et T-AI-MURO n'a simplement pas pu produire de réponses. Sans elles, le taux de réussite devient 32,4 %.

L'IA qui juge peut aussi se tromper. Quand j'ai extrait 20 cas pour les vérifier, 2 étaient des erreurs du côté du test. Dans l'un d'eux, le juge ne savait pas que « ce site de réservation propose une inscription de membres ». Le juge ne sait d'ailleurs rien au-delà des documents qu'on lui a remis. La justesse du test est décidée par l'exhaustivité des règles de l'établissement remises au juge.

Au nouveau test après corrections, le taux de réussite pour les indications de prix et de formules est passé de 29,4 % à 42,7 %. Je n'ai pas encore lancé le test final qui repasse tous les cas. Pour maîtriser les coûts, j'ai décidé que le test de tous les cas ne se lance qu'une fois, avant de mettre en production un changement majeur. Le taux de réussite continue de monter, même pendant que j'écris ce livre.

#### Le test a arrêté la production

Les tests d'IA coûtent de l'argent. Le premier test de 36 scénarios a coûté environ ¥426 (environ $2,8). L'essentiel est allé à l'« effort de réflexion » de l'IA jouant la clientèle, et quand je l'ai désactivé, 3 scénarios ont coûté environ ¥6 (environ $0,04).

Mais un jour, en plein test, le solde d'utilisation de l'IA s'est épuisé et tout s'est arrêté. En une seule journée, j'avais utilisé environ 35 millions de tokens (l'unité de texte qu'une IA lit et écrit). La cause : j'avais fait tourner le test de 221 scénarios encore et encore, et exécuté quatre fois chacun les scénarios directement liés aux ventes.

Ce qui faisait peur, c'est que le test et la production utilisaient le même portefeuille. Quand le solde est à sec, même la fenêtre de conversation de production s'arrête. Un autre jour, cette fois j'ai atteint le plafond mensuel prévu, et la fenêtre de conversation de production et l'IA qui crée les sujets de conversation pour la clientèle de l'établissement se sont arrêtées en même temps.

Le vrai danger d'un budget de test n'était pas la facture, mais que la production utilisait le même portefeuille.

À partir de là, les règles ont changé. Faire d'abord les vérifications qui ne coûtent rien (tests de programme et vérifications automatiques d'écran). Limiter les tests qui appellent l'IA à ceux liés à ce qui a été corrigé. Ne lancer le test de tous les cas qu'une fois, avant la mise en production. Écrire dans les instructions le coût estimé et un plafond, et s'arrêter s'il semble qu'il va être atteint. Pour préserver les fonds de la production, arrêter les tests quand l'utilisation à l'échelle de l'organisation approche du plafond.

Il y avait aussi une leçon sur la façon dont les coûts gonflent. Une fois, le coût de l'IA qui juge est arrivé à 2,6 fois l'estimation. La cause : le long préambule remis au juge à chaque fois (la connaissance de l'établissement et les règles) n'était pas réutilisé, si bien que le préambule était facturé de nouveau à chaque fois. Quand j'ai corrigé pour écrire le préambule une fois et le réutiliser, le coût par conversation est tombé à environ un tiers. Le coût de l'IA ne gonfle pas avec le nombre de fois où on l'appelle, mais avec le nombre de fois où l'on renvoie le même préambule.

Le même test complet de 221 scénarios est passé d'environ ¥1040 (environ $6,9) à environ ¥400 (environ $2,7) à force d'améliorations. J'ai remplacé l'IA jouant la clientèle par un script fixe, et j'ai séparé les informations remises à l'IA en un « noyau envoyé à chaque fois » et des « sections lues seulement en cas de besoin ».

À cause des contraintes de budget, la conception a évolué vers l'augmentation des parties vérifiables à coût zéro, c'est-à-dire les parties décidées par le programme. Résultat : la précision a augmenté aussi. L'argent change la conception.

【Figure 2-2】Résultats des tests d'IA. Le taux de réussite et la répartition des causes d'erreur

### 2-3 Faire auditer par l'IA ce que j'avais construit

#### Les noms de la clientèle pouvaient être lus de l'extérieur

En août 2026, en passant en revue le fonctionnement du système de réservation, j'ai fait une découverte qui m'a glacé le sang.

Les données de réservation de la clientèle pouvaient être lues par n'importe qui depuis l'extérieur. Les noms, les numéros de téléphone, les adresses e-mail, le champ des demandes. Tout ce qui était saisi dans une réservation pouvait être récupéré en entier, sans aucune authentification.

Il y a quelque chose que je dois dire honnêtement. Il est vrai que les données pouvaient être lues de l'extérieur. À l'époque, le site de réservation avait très peu de trafic, et je crois qu'il est improbable que quelqu'un les ait réellement lues. Mais je n'ai aucune trace qui puisse prouver qu'elles n'ont pas été lues. « Elles auraient pu être récupérées » et « elles ont été réellement récupérées » sont deux choses différentes, mais la première seule était une faute grave pour un commerce.

En remontant à la cause, tout tenait à la façon dont le formulaire de réservation était construit. Pour calculer les places libres, le formulaire chargeait 35 jours de données de réservation directement depuis la page. Si la page peut les lire, alors quiconque sait comment de telles pages sont construites peut lire les mêmes données. C'était le résultat d'une première base construite au feeling, qui atteignait l'objectif « afficher les places libres » par le chemin le plus court.

J'ai aussi constaté que l'adresse e-mail destinée à notifier l'établissement était publique, et que n'importe qui pouvait écrire à l'endroit où étaient stockées les traductions, ce qui signifiait que les données pouvaient être vandalisées ou les coûts gonflés.

L'ordre de la correction comptait. Si j'interdisais toute lecture d'un coup, le formulaire de réservation ne pourrait plus afficher les places libres et cesserait de fonctionner. J'ai donc d'abord déplacé le calcul des places libres vers un point d'accès côté serveur. Ensuite, j'ai modifié l'écran de réservation terminée pour qu'il n'obtienne lui aussi que les informations nécessaires depuis le serveur. Enfin, j'ai fermé la lecture depuis l'extérieur. J'ai fait la correction en quatre étapes dans cet ordre et je l'ai appliquée en production.

Après la correction, j'ai mis en place une vérification automatique pour confirmer que c'était réellement fermé. J'ai préparé un test qui tente de lire les données de réservation sans authentification, et je le lance automatiquement après chaque modification pour confirmer qu'il est toujours refusé. Je n'ai pas corrigé une fois en considérant que c'était fini. J'ai fait en sorte qu'une vérification veille à ce que cela ne s'ouvre plus jamais.

#### Des données réelles de la clientèle étaient restées dans l'historique de développement

Puis j'ai fait auditer par l'IA tout le dépôt (le lieu de stockage du programme), et un problème plus grave est apparu.

Pendant le développement, un fichier contenant des données réelles de clients (adresses e-mail et numéros de téléphone de 55 réservations) avait été envoyé au dépôt, et se trouvait toujours dans l'historique des modifications du programme. Le dépôt était privé, mais comme cela subsistait dans l'historique, je ne pouvais pas laisser les choses en l'état.

J'ai retiré le fichier de tout l'historique des modifications, réécrit l'historique et l'ai stocké à nouveau. Malgré cela, les anciennes traces d'avant la réécriture pouvaient encore subsister du côté de GitHub, qui héberge le dépôt. J'ai donc demandé au support de GitHub de les supprimer, et j'ai confirmé que c'était fait.

L'audit a aussi trouvé d'autres problèmes : le point d'accès de traduction pouvait être utilisé sans authentification, la connexion de l'administration pouvait être attaquée par force brute, et il existait une plage de temps pendant laquelle, si le paiement était réactivé, une réservation pouvait être confirmée alors qu'elle n'était pas encore payée. Je les ai corrigés un par un, en commençant par le plus grave.

#### Il y avait zéro test automatisé

L'audit a révélé un autre fait. Le système de réservation n'avait pas un seul test automatisé.

Les tests automatisés sont un mécanisme par lequel une machine vérifie automatiquement si le programme fonctionne correctement. Sans tests, quand on corrige quelque chose, on n'a aucun moyen de vérifier si autre chose s'est cassé. Chaque fois que l'on ajoute une fonction, quelque part quelque chose se brise discrètement. C'était exactement l'état des choses pendant la période où je construisais au feeling.

J'ai donc reconstruit les fondations des tests à partir de zéro. J'ai introduit un système (CI) qui lance automatiquement quatre vérifications après chaque modification : vérification des types, vérification du style, tests et compilation. Les décisions importantes comme le calcul des prix, la validation des réservations, le lien avec les membres et l'émission des coupons ont été séparées du code de l'interface afin de pouvoir être vérifiées isolément. Les règles de lecture et d'écriture de la base de données sont aussi vérifiées dans un environnement de test qui imite une vraie base de données. Les tests unitaires sont partis de 275 et ont ensuite dépassé 500.

J'impose toujours une condition aux tests : « casser le programme, et confirmer que le test échoue ». Même quand un test passe au vert (réussit), on ne sait pas si ce test peut réellement détecter un problème. Ce n'est qu'après avoir délibérément cassé le programme et confirmé que le test passe au rouge (échoue) que je fais confiance au test. Car les tests écrits par l'IA ne vérifient parfois rien du tout.

#### Huit failles dans le formulaire de réservation

Une fois les fondations des tests en place, j'ai fait examiner de nouveau par l'IA tout le parcours de réservation. Elle a trouvé huit problèmes qui causaient un vrai préjudice.

Le plus grave était qu'appuyer plusieurs fois sur le bouton d'envoi créait une double réservation. Cela se produisait réellement en production. Je l'ai corrigé avec un mécanisme qui traite la même action une seule fois même si elle arrive deux fois (l'idempotence). Les autres problèmes étaient les suivants : une réservation ne pouvait pas être confirmée si des informations sur un plat supprimé subsistaient ; il y avait une faille dans la vérification de salle pleine qui laissait la possibilité de dépasser la capacité ; personne ne remarquait quand l'envoi d'un e-mail de confirmation échouait ; la saisie n'était pas validée côté serveur ; un vocabulaire interne apparaissait à l'écran en cas d'erreur ; le texte des champs de saisie était si petit que l'écran zoomait de lui-même sur iPhone ; et la saisie automatique ne fonctionnait pas.

Pour les échecs d'e-mails, j'ai rendu possible leur détection dans l'écran d'administration et le renvoi. Pendant cette enquête, j'ai aussi constaté que l'écriture dans le journal d'audit des confirmations de réservation échouait à chaque fois, bien avant la correction, et que rien n'avait été enregistré.

Je les ai corrigés un par un et appliqués en production.

#### Ne jamais sauter la vérification d'un code écrit par l'IA

Ce que cette expérience m'a appris, c'est que précisément parce qu'un programme a été écrit par l'IA, il ne faut pas sauter la vérification.

L'IA donne vite forme à ce qu'on lui dit. Mais l'attention aux choses qu'on ne lui dit pas, comme « interdire la lecture depuis l'extérieur » ou « traiter une double soumission comme une seule », n'entre pas si on ne l'ordonne pas. Et de telles failles restent tapies en silence à l'intérieur de programmes qui ont l'air de fonctionner.

Il n'est pas nécessaire de lire tout le code. La justesse du programme est surveillée par des vérifications automatiques et par l'audit d'une autre IA. La question de savoir si le résultat convient à l'objectif de l'établissement est surveillée par la direction. On n'a pas besoin de lire, mais on ne doit pas sauter la vérification. C'est ce que je crois que signifie construire avec une IA agentique.

【Figure 2-3】Les règles lorsque la lecture était possible depuis l'extérieur, et les règles après la correction (extrait) *(L'écran est en japonais.)*

### 2-4 Construire au feeling multiplie les contradictions

Plus j'ajoutais de fonctions, plus il y avait de parties qui entraient en conflit avec ce que j'avais décidé plus tôt.

Le cas typique était le calcul des remises. Dans le formulaire de réservation, l'écran de confirmation, l'e-mail et l'écran d'administration, le calcul des remises était écrit séparément à chaque endroit. Si je changeais une règle de remise à un endroit, un autre endroit continuait de calculer avec l'ancienne règle. Pour une même réservation, l'écran et l'e-mail pouvaient afficher des montants différents.

Plus tard, j'ai rassemblé le calcul des prix dans un seul fichier. Le formulaire de réservation, la fenêtre de discussion et le serveur MCP produisent tous leurs prix à partir de là.

Les règles de cumul des remises ont elles aussi changé en cours de route. Comme je l'ai écrit au chapitre 1, le happy hour devait à l'origine pouvoir se cumuler avec d'autres remises, mais j'ai constaté qu'il ne dégagerait aucun profit et je l'ai changé en non cumulable. À chaque changement de règle, il fallait que quelqu'un se souvienne des endroits à corriger. C'était la faiblesse d'un système construit au feeling.

Il y avait aussi un décalage entre l'environnement de test et la production. En testant la fenêtre de discussion, une question, « N'y avait-il pas quelque chose comme 10 % de remise ? », a révélé que les règles de remise de l'environnement de test s'étaient écartées de celles de la production. Si les valeurs de l'environnement de test diffèrent de la production, on peut réussir les tests et se tromper quand même en production. Ce que j'ai alors décidé est le principe selon lequel « la production fait foi ». Depuis, avant chaque exécution de tests, je copie les réglages de production dans l'environnement de test et je confirme que l'écart est nul avant de lancer.

L'IA construit ce qu'on lui dit. Mais elle ne remarque pas les contradictions avec les décisions antérieures. Ce qui empêche les contradictions, ce n'est pas l'IA. C'est de décider à l'avance.

### 2-5 Réapprendre la définition des besoins

Après avoir réfléchi au système de réservation construit au feeling, j'ai réappris la définition des besoins. Définir les besoins, c'est décider avant de construire ce que l'on construira, ce que l'on ne construira pas, qui l'utilisera et comment, et l'écrire dans un document.

C'était une chose que je faisais tout naturellement du temps où j'étais ingénieur système. Mais une fois que j'ai pu construire avec l'IA, je l'avais sautée sans m'en apercevoir. Dites-lui une idée, et quelque chose qui fonctionne apparaît en quelques minutes. Dans cette vitesse, j'avais supprimé l'effort de décider.

Ma façon de construire comporte aujourd'hui trois étapes.

