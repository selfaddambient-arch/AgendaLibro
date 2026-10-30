1. D'abord, fixer les exigences dans le détail. Ce qu'il faut construire, ce qu'il ne faut pas construire, qui s'en servira. Le comportement de chaque écran. La façon de traiter les cas limites (erreurs, double appui, expiration). Les règles qui finissent facilement par se contredire plus tard, comme les prix et les remises, je les décide avec un soin particulier. Ce travail se fait lui aussi en dialogue avec l'IA de chat. Je lui fais chercher à l'avance les lacunes et les contradictions, puis la direction tranche.
2. Écrire ce qui a été décidé dans un « cahier des charges ». Pas des instructions orales ou données au fil de l'eau, mais un seul document. Il devient l'unique référence pour vérifier plus tard ce qui est correct.
3. Remettre le document entier à l'IA et lui faire réaliser l'implémentation. Je donne le document complet à l'IA qui écrit le programme (Claude Code), avec les conditions de réussite (tous les tests passent, vérification dans l'environnement de test avant la production, etc.). L'IA construit seule jusqu'à remplir ces conditions, et se vérifie seule. La direction ne regarde qu'en cas d'arrêt en cours de route, et pour le contrôle final.

Par exemple, le cahier des charges de la fenêtre de chat « T-AI-MURO » a été réécrit de la première à la troisième version. Dans la deuxième, j'ai décidé « ne pas laisser l'IA calculer les prix », « réunir dans une seule fenêtre les connaissances de l'établissement et le calcul des prix » et « garder aussi le formulaire, pour les personnes qui ne veulent pas réserver par chat ». Dans la troisième, j'ai décidé « où conserver l'exemplaire de référence des connaissances de l'établissement », « cette fenêtre seule affiche les créneaux libres », « faire du premier échange une question à quatre choix » et « ne pas enregistrer les conversations, mais seulement les questions restées sans réponse ». Comme les décisions restent dans un document, je peux retrouver plus tard pourquoi les choses sont ainsi.

Avec cette façon de construire, même quand j'ajoute des fonctions, je repère tout de suite les contradictions en vérifiant par rapport au document. C'est justement à l'époque où l'IA construit qu'il faut la « capacité de décider » avant de construire. Ce fut la plus grande leçon du système de réservation.

J'ai aussi mis au point un mécanisme qui met la procédure elle-même dans un document et la confie à l'IA, pour que cette façon de construire se déroule de la même manière à chaque lancement d'un nouveau produit. J'en parlerai au chapitre 4.

【Figure 2-4】Sommaire du cahier des charges de T-AI-MURO (version 3) *(L'écran est en japonais.)*

### 2-6 Apprendre le langage de l'interface

Il y a encore une chose que j'ai dû réapprendre : le nom des éléments d'écran.

Même quand je disais à l'IA « fais ceci ici », l'écran ne ressemblait souvent pas à ce que j'attendais. En cherchant la cause, j'ai compris que je ne connaissais pas le nom des éléments d'écran. J'avais beau décrire « une petite fenêtre qui s'affiche par-dessus » ou « un avis qui disparaît au bout de quelques secondes », l'IA avait du mal à savoir ce que je voulais dire.

J'ai donc lu un ouvrage de référence sur l'UI (interface utilisateur, l'aspect et le fonctionnement d'un écran) et appris le nom des éléments et les termes techniques du design.

| Élément | De quoi il s'agit |
| --- | --- |
| Modale | Une petite fenêtre qui s'affiche par-dessus l'écran. Tant qu'on ne l'a pas fermée, on ne peut pas utiliser l'écran qui se trouve derrière |
| Toast | Une notification qui apparaît quelques secondes au bord de l'écran, puis disparaît d'elle-même |
| Onglet | Un mécanisme où l'on change de contenu en appuyant sur un intitulé |
| Accordéon | Un mécanisme où l'on ouvre et ferme un contenu en appuyant sur un intitulé |
| Tiroir | Un menu qui coulisse depuis le côté de l'écran, comme un tiroir |
| Autres | Fil d'Ariane (un chemin qui indique où l'on se trouve), carrousels (éléments qui défilent horizontalement), bottom sheets (un panneau qui monte depuis le bas de l'écran), etc. Chaque nom appris permet de donner une consigne à l'IA en une seule expression |

Quand on communique par les noms, les écrans produits par l'IA sont presque bons du premier coup. Si vous dites : « Affiche l'écran de confirmation de réservation sous forme de modale », l'IA n'hésite pas.

#### L'IA oscille d'un extrême à l'autre entre ajouter et retrancher

Même après avoir appris les mots, construire des écrans avec l'IA posait une difficulté d'un autre genre. L'IA oscille fortement.

Quand j'ai demandé un en-tête « élégant » pour le site de réservation, j'ai obtenu un en-tête haut et imposant. Or un site de réservation sert avant tout à réserver. Pour les habitués qui réservent à chaque fois, un en-tête volumineux, chargé de longues explications n'est qu'une gêne. Je l'ai fait réduire de moitié environ en hauteur, avec la même quantité d'informations.

Quand j'ai uniformisé le pied de page des e-mails et ajouté un lien vers le Guide de la Prochaine Étape, le corps du texte paraissait soudain terne et pauvre en comparaison. J'ai donc ajouté au corps du texte aussi un intitulé, un tableau des points clés et un bouton sur lequel appuyer. Quand j'ai ajouté dans le pied de page une entrée vers la fenêtre de chat, l'ensemble faisait chargé. En la glissant dans deux lignes de liens séparées par des filets, c'était net mais discret. Finalement, tout s'est stabilisé sur deux cartes qui montrent leur rôle par « le moment où s'en servir ». À gauche « pour votre prochaine réservation », à droite « après votre repas ».

Trop chargé, trop dépouillé, trop voyant. Ce qui fixait la bonne mesure, c'était à chaque fois le mot de la direction.

#### Une proposition de design sans images

Cela m'est arrivé aussi. J'avais demandé à l'IA qui écrit les programmes de créer des propositions d'amélioration pour la fenêtre de chat avec une IA de design (Claude Design), et un rapport est revenu : « J'ai fait des propositions pour huit écrans. » Mais en l'ouvrant, je n'ai trouvé qu'une description en texte. L'IA n'avait pas su produire d'images, et pourtant seul le rapport « terminé » restait.

Finalement, c'est l'IA de chat qui a dessiné directement quatre propositions dans l'écran de design. Elle a repris les couleurs de l'écran actuel à partir d'une capture d'écran, mis l'histoire de l'établissement en frise chronologique, séparé l'assaisonnement en deux cadres, « mode de cuisson » et « goût », transformé les formules en cartes explicatives et regroupé les prix dans un récapitulatif de réservation.

Quand on fait lancer un test à l'IA, elle dit « réussi ». Quand on lui demande un design, elle dit « terminé ». Vérifier ce qu'il y a dedans est le travail d'un humain. Le critère de jugement, seuls les humains peuvent continuer à le tenir.

#### Ce que vous pouvez retenir de ce chapitre

- Construire quelque chose qui fonctionne et pouvoir l'exploiter en sécurité sont deux choses différentes.
- Vérifiez le résultat de l'IA non pas sur ses paroles, mais par des tests. Un test n'est digne de confiance qu'une fois vérifié qu'il échoue quand on casse quelque chose.
- Les calculs qui ne doivent pas être faux, comme les prix, ne se confient pas à la génération de texte de l'IA. Confiez-les au programme.

La suite de ce chapitre (les nouvelles failles découvertes et les étapes suivies pour les corriger) se trouve sur note et X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Chapitre 3 : Partager les outils de mon établissement avec d'autres

### 3-1 Le petit panneau vert de la page de réservation

Ouvrez la page de réservation de Tamuro et vous verrez, près du haut, un petit panneau vert. Tant que l'établissement est ouvert, il indique « OPEN », et à la fermeture « CLOSED ». Quand la direction appuie sur le bouton de prolongation, l'heure de fermeture est repoussée de 30 minutes et une touche de vermillon apparaît sur le panneau.

Les établissements indépendants ont un trait commun. Ils ouvrent presque à l'heure exacte, mais la fermeture déborde souvent. Quand la conversation avec la clientèle est animée, les lumières restent allumées bien après la dernière commande de 22h30.

Seulement, côté clientèle, on ne voit rien de tout cela. L'affichage « Ouvert » de Google Maps se base uniquement sur les horaires enregistrés : il ne tient compte ni des prolongations, ni des fermetures anticipées, ni des fermetures exceptionnelles. Personne ne marche jusqu'à un établissement passé l'heure de fermeture en se disant : « Il est peut-être encore ouvert. » Appeler pour vérifier est gênant aussi.

Ce panneau est un outil qui répond à cette question : « Est-ce encore ouvert ? » Il s'appelle « AgendaLuce (Carnet de Lumière) ». Luce signifie « lumière » en italien.

Carnet de Lumière est conçu pour fonctionner presque sans attention de la direction. Enregistrez une fois les heures d'ouverture et de fermeture de chaque jour de la semaine, et le panneau s'allume et s'éteint automatiquement. La direction n'y touche que pour prolonger, fermer plus tôt ou fermer exceptionnellement. Pour prolonger, il suffit d'appuyer sur un bouton de son smartphone. Le personnel peut aussi s'en servir depuis un lien dédié, qui fonctionne sans connexion.

La clientèle n'a besoin ni de se connecter ni de s'inscrire. En ouvrant la page publique, on voit l'état actuel de la lumière. Ajoutée à l'écran d'accueil du smartphone, elle fonctionne comme une application. Le petit widget du panneau peut aussi être intégré à d'autres sites web. Ce qui s'affiche sur la page de réservation de Tamuro, c'est ce widget.

Carnet de Lumière est gratuit. Si vous vous contentez d'intégrer le widget du panneau à votre site web, la mise en place prend environ 10 minutes.

Et voici le point important. Ce Carnet de Lumière n'est pas réservé à Tamuro. N'importe quel établissement peut l'utiliser.

J'ai volontairement laissé le nom de l'établissement hors de la conception du panneau. Si j'y mettais un nom, ce serait un panneau pour Tamuro. On peut aussi choisir la langue d'affichage. J'ai conçu un widget compact pour qu'il s'intègre au site web de n'importe quel établissement.

Un outil né du problème de Tamuro, « la fermeture déborde », conçu dès le départ sous une forme que tout le monde peut utiliser. Voilà Carnet de Lumière. Et l'ensemble des outils de ce genre, c'est la « série Agenda ».

【Figure 3-1a】Le panneau de Carnet de Lumière en haut de la page de réservation (ouvert) *(L'écran est en japonais.)*

【Figure 3-1b】Une touche de vermillon apparaît pendant une prolongation *(L'écran est en japonais.)*

【Figure 3-6a】L'écran de la direction. Pour prolonger, un seul appui sur le bouton *(L'écran est en japonais.)*

【Figure 3-6b】Juste après l'appui sur prolonger. L'heure de fermeture est repoussée de 30 minutes *(L'écran est en japonais.)*

【Figure 3-6c】La page publique que voit la clientèle (pendant une prolongation) *(L'écran est en japonais.)*

### 3-2 Tout a commencé par le carnet en cuir noir

La série Agenda n'était pas prévue comme une série. Elle a commencé par un seul système, qui n'est même pas encore sorti.

Ce que j'avais d'abord voulu construire, c'était un mécanisme qui reconnaît le visage des clients et accueille les habitués. Une caméra à l'entrée distingue les visiteurs par leur visage et prévient la direction : « Voilà la personne qui avait pris le tonteki la dernière fois, celle qu'on n'a pas vue depuis trois mois. » Je voulais qu'une machine aide à faire le travail que la direction d'un petit établissement fait de tête : retenir les visages, les noms et les préférences.

Mais peu après avoir commencé à construire, j'ai compris que ce système portait une charge très lourde. Les visages. Les caractéristiques. L'historique des visites. Le caractère d'un client. Pour toutes ces informations, une fois la fuite survenue, le mal est irréparable.

Ce qui m'est alors venu à l'esprit, c'est « Le Carnet en cuir noir » (« Kuroi techō ») de Seichō Matsumoto. Un registre qu'on ne montre à personne, mais qui existe bel et bien. Un carnet qui, une fois ouvert, fait basculer la vie et la mort des gens. N'est-ce pas exactement ce que je suis en train de construire ?

En italien, « carnet » se dit Agenda, et « noir » se dit Nera. Mis ensemble : AgendaNera. Le carnet en cuir noir. C'est ainsi que ce nom a été choisi en premier.

AgendaNera est toujours en cours de construction. C'est celui que je construis avec le plus de soin dans la série.

Et ce nom a été le déclencheur. S'il existe un carnet noir, il peut exister des carnets d'autres couleurs. Je reconstruirais les mécanismes que j'utilisais chaque jour dans mon propre établissement sous une forme que tout établissement peut utiliser, et je les publierais un carnet à la fois. C'est la [série Agenda](https://bontallc.com/agenda?via=b2-fr-{{FMT}}).

### 3-3 Ajouter les carnets, un à la fois

La série Agenda est un ensemble de petites applications web, dont chacune répond à un problème de restaurant avec un seul outil. Chacune a un nom italien et un surnom qui, en japonais, se termine par « techō » (carnet). Chaque nom a son origine propre.

| Nom | Surnom | Origine du nom | Ce qu'il fait |
| --- | --- | --- | --- |
| AgendaTimbro | Pointages | Timbro signifie « tampon ». C'est le pointage lui-même | Enregistre l'arrivée et le départ du personnel |
| AgendaOro | Rentabilité | Oro signifie « or ». Le carnet de l'argent | Estime la rentabilité d'une ouverture d'établissement ou d'un nouveau plat (gratuit) |
| AgendaBis | Guide de la Prochaine Étape | Bis signifie « bis ». Le « Bis ! » lancé par le public d'un concert | Oriente la clientèle vers une prochaine étape à proximité (gratuit) |
| AgendaQA | Guide d'assistance | Qua signifie « ici ». En cas de difficulté, ici | Le centre d'aide commun de la série (gratuit) |
| AgendaLuce | Carnet de Lumière | Luce signifie « lumière » | Indique si l'établissement est ouvert (gratuit) |
| AgendaRicetta | Prix de revient | Ricetta signifie « recette » | Calcule le coût d'une recette et son ratio de coût (gratuit) |
| AgendaNera | Carnet des habitués | Nera signifie « noir ». Le carnet en cuir noir | Accueille les habitués par reconnaissance faciale (en construction) |
| AgendaTurno | Planning d'équipe | Turno signifie « tour » ou « service » en italien | Recueille les souhaits de planning du personnel et distribue le planning que l'IA de la direction a établi (bientôt disponible) |

Quel carnet convient à quel type d'établissement ? Pointages s'adresse aux établissements dont le personnel compte au moins deux personnes et qui gèrent les présences sur papier ou par LINE *(l'application de messagerie la plus répandue au Japon)*. Rentabilité s'adresse aux personnes sur le point d'ouvrir un établissement, et à celles qui veulent revoir leurs chiffres parce que le loyer ou les coûts ont changé. Guide de la Prochaine Étape s'adresse aux établissements axés sur le repas qui veulent envoyer tôt leur clientèle vers l'étape suivante. Carnet de Lumière s'adresse aux établissements indépendants dont la fermeture est plus tardive ou plus précoce que prévu. Prix de revient s'adresse aux établissements où les recettes sont dans la tête, mais où l'on n'a jamais calculé de ratio de coût.

#### Pointages ne calcule pas la paie

Pointages transforme tel quel la tablette de l'établissement ou les smartphones du personnel en pointeuse. Il suffit de toucher son nom. La feuille de présence est totalisée automatiquement et peut être exportée en CSV (un format qui s'ouvre dans un tableur). La journée d'activité commence à 5h du matin, de sorte que même avec des horaires tardifs, la date ne change pas en cours de service.

Mais ce Pointages ne calcule volontairement pas la paie.

Les salaires horaires, les primes et les dates de clôture varient trop d'un établissement à l'autre. Nuit majorée de 25 %, jours fériés en catégorie à part, transport au montant journalier. Quelle que soit la façon dont je le construisais, il ne conviendrait pas à l'établissement de quelqu'un.

Alors, au lieu de calculer, j'ai préparé « un modèle de consignes à remettre à une IA ». La direction colle tel quel le CSV de présences téléchargé et ce modèle dans l'IA qu'elle utilise d'habitude, que ce soit ChatGPT, Claude ou Gemini. L'IA calcule alors les majorations de nuit, la paie des jours fériés et les transports, et les présente sous forme de liste. Les règles propres à chaque établissement, comme « on clôture en fin de mois, la nuit est majorée de 25 %, le dimanche est une catégorie à part », peuvent être ajoutées au modèle et seront prises en compte telles quelles. Le CSV comporte des colonnes pour le jour de la semaine et le nom du jour férié afin que l'IA calcule correctement.

Je ne détiens pas moi-même le mécanisme de calcul ; chaque établissement garde ses règles entre ses propres mains. J'ai estimé que c'est la solution la plus robuste.

#### Orienter vers une prochaine étape, et laisser votre établissement en mémoire

Guide de la Prochaine Étape est un outil pour créer une « page de guide de la prochaine étape » à remettre à la clientèle. Aux clients qui ont fini leur repas, il indique un bar ou un lieu où finir la soirée à proximité, avec le nombre de minutes à pied.

On dirait un outil pour envoyer la clientèle ailleurs, mais il contient une petite astuce. Orienter quelqu'un vers une deuxième étape, c'est sous-entendre que la première était votre établissement. Tout en ayant l'air d'envoyer les clients ailleurs, il grave en réalité dans leur mémoire que « la première étape, c'était cet établissement ». C'est ainsi qu'il est conçu.

#### Trois principes de conception : automatique, force empruntée, fonction unique

Tous les carnets de la série Agenda partagent trois principes.

Le premier est l'« automatique ». Il doit fonctionner sans que la direction y touche chaque jour. Avec Carnet de Lumière, une fois les horaires enregistrés, le panneau s'allume et s'éteint de lui-même. Pendant le service, la direction d'un restaurant n'a pas le temps de toucher un écran. Un outil qui ne marche pas sans qu'on y touche finira par ne plus servir.

Le deuxième est la « force empruntée ». Ne pas tout construire soi-même, mais s'en remettre aux outils et à l'IA que la direction utilise déjà. La paie de Pointages en est le cas d'école. Planning d'équipe suit la même logique : il se limite à recueillir les souhaits du personnel et laisse la construction des plannings à l'IA de la direction. Il ne porte ni mécanisme compliqué qui lui soit propre, ni le coût d'appel d'une IA. C'est pourquoi le prix peut rester bas.

Le troisième est la « fonction unique ». Un carnet ne fait qu'une seule chose, mais la fait de façon fiable. Un système multifonction est trop lourd pour un établissement indépendant. À force d'ajouter des fonctions, il devient plus difficile à utiliser, et les contradictions du côté de la conception se multiplient. C'est ce que j'ai appris de première main avec le système de réservation au chapitre 2. J'ajoute donc les carnets un par un, chacun faisant « juste cette seule chose, correctement ».

#### Pourquoi le système de réservation ne fait pas partie de la série

À ce stade, je m'attends à une question évidente. Ce sur quoi Tamuro a le plus travaillé, c'est le système de réservation. Pourquoi ne pas le mettre dans la série Agenda ?

En fait, j'en avais eu l'intention. Le projet était de mettre le système de réservation sous une forme utilisable par d'autres restaurants et de le publier comme un carnet de la série. Mais en août 2026, j'ai abandonné ce projet.

La raison est exactement ce que j'ai écrit au chapitre 1. Le système de réservation de Tamuro est plein de la façon de faire de Tamuro. Les clients seuls représentent la moitié de la clientèle. Près de 90 % des réservations se font le jour même. Je veux vendre le temps avant l'ouverture. Je veux que les gens viennent en groupe. Je veux faire grandir le nombre d'habitués. J'ai construit les combinaisons de remises, l'ordre des e-mails et la façon dont la fenêtre de conversation recommande, le tout pour correspondre à cela.

Si je l'allégeais pour en faire quelque chose que tout le monde peut utiliser, il deviendrait un système de réservation ordinaire qui convient à tous les établissements de façon médiocre. La force de Tamuro disparaîtrait alors. Le système de réservation et la gestion de la relation client sont la manière dont l'établissement vend ce qu'il propose. Plutôt que d'adapter l'établissement à un système générique, adaptez le système à l'établissement. Notre établissement, selon nos propres spécifications. J'ai donc décidé de garder le système de réservation de Tamuro pour Tamuro seul.

Alors, n'y a-t-il rien à partager au-delà de l'établissement ? Si. Autour du système de réservation, il y a beaucoup de petits problèmes communs à tous les établissements. Gardez le cœur de l'établissement selon vos propres spécifications. Construisez dès le départ, sous une forme que tout le monde peut utiliser, les outils qui règlent les problèmes alentour, et partagez-les. La page de réservation de Tamuro est un exemple qui réunit les deux sur un seul écran. Au-dessus d'un système de réservation réservé à Tamuro se trouve le panneau de Carnet de Lumière, que tout le monde peut utiliser.

【Figure 3-2】La page de présentation de la série Agenda *(L'écran est en japonais.)*

【Figure 3-3a】Présentation de Pointages *(L'écran est en japonais.)*

【Figure 3-3b】Présentation de Rentabilité *(L'écran est en japonais.)*

【Figure 3-3c】Présentation du Guide de la Prochaine Étape *(L'écran est en japonais.)*

【Figure 3-4】L'écran de pointage de Pointages. Il suffit de toucher son nom (données de synthèse) *(L'écran est en japonais.)*

### 3-4 Construire pour tout le monde dès le départ

Je fabrique un outil pour mon propre établissement, puis je le distribue aussi à d'autres établissements. Dit ainsi, cela paraît simple, mais pour y arriver, la façon de décider avant de commencer à construire doit changer.

Si je construisais seulement pour Tamuro, le plus rapide serait d'écrire directement dans le programme les horaires de Tamuro et le nom de Tamuro. Mais alors aucun autre établissement ne pourrait s'en servir. Si l'on essaie de le généraliser plus tard, on se retrouve à traquer chaque endroit écrit en dur pour le corriger un par un.

Les outils de la série Agenda sont donc spécifiés dès le départ en partant du principe que tout le monde peut les utiliser. Je pars d'un problème de Tamuro, mais au stade des exigences, je sépare deux questions : « Est-ce vrai seulement de Tamuro, ou de tous les établissements ? » Ne pas mettre le nom de l'établissement sur le panneau. Laisser les gens choisir la langue. Le rendre intégrable à n'importe quel site web. J'ai arrêté des décisions de ce genre en rédigeant le cahier des charges de Carnet de Lumière.

C'est un autre usage de la définition des exigences que j'ai réapprise au chapitre 2. Si l'on décide ces choses d'abord, on peut se servir de l'outil à Tamuro et le distribuer tel quel à d'autres établissements.

Les problèmes de mon établissement sont aussi ceux des autres. Tamuro n'est pas le seul établissement à vouloir dire à la clientèle que la fermeture est repoussée. Dans un établissement indépendant, on construit un outil à partir de son propre problème, puis on le distribue à d'autres établissements. Telle est l'idée de la série Agenda.

### 3-5 La démocratisation de la technologie

La série Agenda compte désormais plus de 10 produits. Je les construis et je les exploite seul, derrière le comptoir.

Il y a quelques années, cela aurait été impensable. Pour construire un produit, il fallait quelqu'un pour le planifier, quelqu'un pour concevoir les écrans, quelqu'un pour écrire le code, quelqu'un pour le tester et quelqu'un pour l'exploiter. Sans équipe ni financement, on ne pouvait pas lancer un produit sur le marché.

Ce n'est plus vrai. La direction énonce les exigences à l'IA, l'IA écrit le code, l'IA le teste, et une autre IA l'audite. Ce que fait la direction, c'est décider quoi construire, juger si les résultats de l'IA correspondent à l'objectif de l'établissement, et accomplir seulement les opérations que les humains seuls peuvent faire.

Ce genre de changement s'appelle généralement la « démocratisation de la technologie ». Le pouvoir de construire n'est plus la propriété de quelques personnes ou entreprises.

Mais soyons honnêtes ici. Comme je l'ai écrit dans l'Introduction, j'ai travaillé dans l'informatique pendant environ 16 ans, surtout à la planification de systèmes et à la coordination entre les gens du terrain et les prestataires de développement. Je connaissais la définition des exigences, la façon de penser les bases de données et la conduite des tests, le tout par l'expérience. Je ne prétendrai donc pas que quelqu'un qui n'a jamais écrit une ligne de code pourrait faire la même chose dès demain.

Malgré tout, beaucoup de choses ont changé. Je peux désormais construire seul, entre deux moments de mon activité principale, ce qui demandait autrefois une équipe. Et pour les personnes sans expérience, le seuil d'entrée s'est assurément abaissé. L'IA vous explique si vous l'interrogez sur ce que vous ne comprenez pas. Elle donne forme à ce que vous lui dites avec des mots. Ce qui manque, ce n'est pas la technique, mais la capacité de décider quoi construire et les mots pour le dire à l'IA. Ce sont des capacités que les gens qui tiennent un établissement utilisent de toute façon tous les jours.

### 3-6 Le débat sur la « mort du SaaS »

Les logiciels qu'on utilise par internet moyennant un abonnement mensuel, comme la série Agenda, s'appellent des SaaS (Software as a Service, logiciel en tant que service). Logiciel de comptabilité, gestion des temps et présences, gestion des réservations. Les restaurants d'aujourd'hui fonctionnent avec beaucoup de SaaS.

L'IA mettra-t-elle fin au SaaS ? En 2026, ce débat a pris beaucoup d'ampleur.

Un des déclencheurs a été une remarque du PDG de Microsoft, Satya Nadella. Dans un podcast en décembre 2024, Nadella a dit que les applications SaaS s'effondreraient à l'ère des agents IA. Son raisonnement : une fois que les agents IA auront repris la partie décisionnelle du travail, les logiciels conçus pour être manipulés par des personnes à travers des écrans ne seront plus nécessaires.

Puis, en février 2026, Anthropic a annoncé Claude Cowork (un outil d'IA qui exécute de façon autonome des tâches professionnelles), et les actions des entreprises de logiciels américaines ont fortement chuté. À Wall Street, cette chute a fini par s'appeler la « SaaSpocalypse ». Ce que craignaient les investisseurs, c'était que, si les agents IA font le travail, le modèle SaaS qui gagne une redevance par personne (la tarification par siège) s'effondre.

Il y a aussi des contre-arguments. Le PDG de Nvidia, Jensen Huang, a dit que les agents IA ne remplaceront pas les logiciels mais s'en serviront à la place des gens, et il a qualifié la chute d'excessive. Bon nombre d'autres voix voient même les SaaS qui absorbent l'IA en sortir plutôt renforcés.

Le SaaS va-t-il vraiment mourir ? Voici ce que j'en pense.

