## Introduction

Ce livre est un témoignage qui date de janvier 2026. Depuis, certaines de mes façons de tenir le commerce, ainsi que certains noms et caractéristiques des outils d'IA, ont changé. La suite, *Sur mesure pour notre bar*, reprend le récit là où celui-ci s'arrête.

### Pourquoi un ancien de l'informatique de gestion parle à une IA dans un restaurant en sous-sol

Merci d'avoir ouvert ce livre.

*Une seule personne fait tourner le commerce, et l'IA est apparue à ses côtés.*

En lisant ce titre, certains d'entre vous penseront peut-être : « C'est exactement moi. » D'autres se demanderont : « Que veut dire "l'IA est apparue à ses côtés" ? »

Ce n'est pas un livre technique sur une programmation difficile. C'est un livre pour des gens comme vous, des restaurateurs qui sont en cuisine tous les jours, qui font la préparation et qui ne s'arrêtent jamais avec la clientèle.

Permettez-moi de me présenter un peu.

Je tiens aujourd'hui un petit restaurant au sous-sol d'un immeuble de Higashi-Nakano *(un quartier résidentiel de l'ouest de Tokyo, juste à l'ouest de Shinjuku)*, à Tokyo.

Il a deux visages. Le jour, c'est une adresse spécialisée dans le curry au steak haché japonais (hambāgu) parfumé aux épices. Le soir, c'est un bar-restaurant, qui propose un menu du jour et de l'alcool.

▼ Quatre Épices, curry-hamburger (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Épices, curry au steak haché (Instagram)](images/fig-01.png)

▼ Bar « Tamuro » (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Bar "Tamuro" (Instagram)](images/fig-02.png)

C'est un lieu chaleureux, avec seulement 11 places au comptoir et 8 places sur une estrade en tatami.

Mais je ne me contente pas de servir à manger.

J'organise une soirée vin tous les quinze jours, et une fois par mois je prépare un cours de cuisine ou une journée de menu spécial. Même dans un sous-sol exigu, mes journées sont rythmées et bien remplies.

Cette année, j'entame ma douzième année à la tête du commerce.

Avant cela, je travaillais en entreprise. J'y occupais des fonctions de « planification de systèmes » et d'« architecture de solutions ».

Quand je le dis, on me répond parfois : « Vous développiez donc des systèmes impressionnants. » Ce n'est pas vraiment le cas.

Je n'écrivais pas de code difficile. J'écoutais ce que voulaient les gens de terrain, je le transmettais fidèlement aux prestataires informatiques (les sociétés de développement) pour donner forme au projet. J'étais un « coordinateur ». Au Japon, on appelle familièrement ce poste « shisutemu-ya » (littéralement le « métier des systèmes »).

Le personnel de terrain souhaitait : « Je voudrais que mon travail soit plus facile. » Les ingénieurs disaient : « Il nous faut des exigences définies de façon logique. »

Mon travail consistait à me placer entre les deux, à traduire le langage de chacun et à mener tout le monde vers l'objectif.

C'est pourquoi je comprends les désagréments et les soucis de celles et ceux qui utilisent les systèmes, comme vous, et je comprends aussi un peu comment raisonnent les équipes informatiques.

J'ai quitté l'entreprise il y a douze ans et j'ai ouvert mon propre commerce. Depuis, j'ai les mêmes soucis que vous.

Une préparation qui n'en finit jamais, le manque de personnel, l'inquiétude pour attirer la clientèle, des décisions de gestion que je dois prendre en solitaire...

Bien sûr, quand il y a beaucoup de monde, des extras fiables et des prestataires externes me prêtent parfois main-forte.

Mais ils ne sont que des partenaires pour les « tâches ».

Je n'ai personne à qui demander conseil pour les lourdes « décisions de gestion », comme « Comment gérer la trésorerie du mois prochain ? » ou « Dois-je parier sur ce nouveau plat ? »

Je m'inquiète, je décide et j'assume toute la responsabilité. En ce sens, j'ai toujours « tenu le commerce à moi seul ». Et c'est l'IA qui s'est assise à mes côtés, comme confidente de « moi, chef d'entreprise », dans ma solitude.

C'est dans ce contexte qu'est arrivée l'IA générative, et en particulier un partenaire appelé « Google Gemini ».

La « coordination » que je faisais autrefois entre « le terrain » et « les prestataires informatiques », je la fais maintenant moi-même entre « les problèmes du commerce » et « l'IA ». Et j'ai compris quelque chose.

Vous n'avez pas besoin d'apprendre par cœur la syntaxe de langages de programmation difficiles (comme Python).\
L'IA les connaît. Mais le plan de « ce que vous voulez faire, et dans quel ordre » est une chose que seul un humain peut concevoir.\
Ce que j'ai acquis dans le métier de « shisutemu-ya », c'était justement cette « capacité à traduire ce que veut le terrain en étapes logiques ».\
Dans ce livre, je partagerai sans rien vous cacher non seulement la manière d'utiliser l'IA, mais aussi cet « instinct logique pour faire travailler l'IA (la pensée systémique) ».\
Avec cela, vous passez de « zéro connaissance » à « meilleur donneur d'ordres qui soit ».

※ Je dois être honnête sur un point.

Je viens de l'informatique de gestion. Mais dans les usages de l'IA présentés dans ce livre, il n'y a en réalité presque eu aucun moment où les connaissances de mon ancien métier ont directement servi.

Ce qui a servi, ce n'est pas « la compétence pour écrire des programmes ».\
C'est seulement « l'habitude de traduire les vagues frustrations du terrain en une suite de mots bien ordonnés ».

Et cette habitude n'est pas un talent particulier.\
C'est « un sens que possèdent déjà tous les propriétaires qui font tourner un commerce au quotidien ».

Dans ce livre, je séparerai volontairement ce que moi seul pouvais faire\
de ce que vous pouvez copier tel quel, dès aujourd'hui.

## Chapitre 1 : Concepts – les agents IA, une nouvelle sorte de collaborateur

~ Engagez l'IA comme « partenaire de travail », et non comme « partenaire de discussion » ~

### 1-1. Les limites d'une exploitation en solo, et les malentendus sur l'IA

Tenir un restaurant indépendant comme le nôtre, c'est une course permanente contre la montre. Préparation, cuisson, service, encaissement, nettoyage... tout doit être assuré par une seule personne, ou par une petite équipe.\
Même quand nous embauchons, nous, propriétaires indépendants, restons en réalité « les seuls à la barre ».

C'est parce que nous n'avons pas de « directeurs de restaurant » ni de « formateurs » comme les grandes chaînes.

Vous cuisinez tout en donnant des consignes à l'équipe de salle, vous formez les nouvelles recrues et vous gérez les plannings.

Toute cette « charge mentale » se concentre sur une seule personne : vous.

Vous pouvez avoir plus de bras, mais vous n'avez toujours qu'une seule tête. C'est précisément pour cela que vous avez besoin de l'IA pour soutenir cette « tête ».

« Si seulement j'avais un bon collaborateur de plus... »

Vous devez avoir cette pensée plusieurs fois par jour.

Quand je dis : « Utilisons l'IA », beaucoup de propriétaires répondent ceci :

« Vous parlez de ChatGPT ? J'ai essayé, mais il ne fait qu'écrire du texte, non ? Ça ne sert à rien sur le terrain. »

En fait, il y a ici un gros malentendu.

La plupart des IA que nous avons utilisées jusqu'ici étaient des « chatbots (des partenaires de discussion) ». Mais ce que visent les IA les plus récentes, à commencer par Google Gemini, c'est la forme d'un « agent IA (un partenaire de travail) ».

Les deux se ressemblent, mais ce sont des choses différentes. Comparons-les à partir d'une tâche concrète.

### 1-2. Du « dictionnaire » au « membre de l'équipe »

Imaginons que vous vouliez créer une affiche pour un événement de votre établissement.

Avec l'IA d'hier (un chatbot) :

Si vous demandez : « Dis-moi comment faire une affiche », l'IA explique les étapes comme un dictionnaire ou un manuel : « Gardez l'accroche courte », « Choisissez les couleurs ainsi ».

Mais celui qui réalise concrètement l'affiche de ses mains, c'est vous. Vos connaissances ont grandi, mais votre temps de travail n'a pas diminué.

Avec l'IA de demain (un agent IA) :

Vous donnez simplement la consigne : « Fais une affiche. »

L'IA réfléchit alors par elle-même pour atteindre l'objectif. Elle trouve l'accroche, génère l'image de fond et propose même la mise en page.

Comme un excellent collaborateur, elle utilise des outils, planifie et mène le travail à bien toute seule.

Ce que nous voulons, ce n'est pas un conseiller qui débite de belles théories, mais un partenaire qui transpire à nos côtés.

※ Dans ce livre, j'appellerai avec affection ce partenaire fiable (une IA générative telle que Google Gemini) l'« adjoint de direction (IA) ».

※ Dans ce livre, je prends comme exemple « Google Gemini », que j'utilise principalement, mais la plupart des idées présentées ici peuvent se reproduire à peu près à l'identique avec d'autres IA génératives comme ChatGPT et Claude.

L'essentiel n'est pas le nom de l'outil, mais « l'attitude qui consiste à traiter l'IA non comme un partenaire de discussion, mais comme un partenaire à qui l'on peut confier du travail ».

### 1-3. Le « multimodal » va sauver les restaurants

Il y a un autre mot-clé d'une importance capitale pour tenir un restaurant. C'est « multimodal ».

C'est un mot un peu technique, mais son sens est simple.

Il veut dire « être capable de comprendre plusieurs types d'informations à la fois : non seulement le texte (lire et écrire), mais aussi les images (voir et dessiner) et le son (écouter et parler) ».

Les IA classiques ne comprenaient que les « mots ». Mais le quotidien d'un restaurant ne se résume pas à des « mots ».

- L'aspect des aliments qui restent dans le réfrigérateur

- L'écriture manuscrite sur les bons de commande

- Les voix des clients et l'ambiance de la salle

- Le graphisme de l'étiquette d'une bouteille de vin

Tout cela, ce sont des « informations non verbales » qu'il est fastidieux de mettre en mots.

L'adjoint de direction (IA) peut les reconnaître comme le ferait un humain.

Si vous prenez avec votre téléphone une photo de l'intérieur de votre réfrigérateur et que vous la montrez, l'IA reconnaît : « Ah, il vous reste ce légume et cette viande en surplus », et peut en tirer un menu.

Autrement dit, l'IA d'aujourd'hui est « un excellent adjoint de direction qui peut voir, entendre et parler ».

※ Mais je ne voudrais pas que vous vous mépreniez sur un point.\
L'IA est plus douée pour dire des choses qui paraissent plausibles que des choses exactes. Pour la reconnaissance d'images, les chiffres, les dates et les noms propres,\
utilisez-la en partant du principe qu'un humain fait toujours la vérification finale.

Si l'IA fonctionne bien dans ce livre, c'est parce que\
je « ne lui confie pas tout, et je vérifie toujours sur place ».

### 1-4. Appuyer votre « intuition » sur des données

Les grandes chaînes disposent d'énormes quantités de données de caisse (POS) et d'équipes marketing.

Dans nos établissements indépendants, vous avez votre « intuition » et votre « expérience » de propriétaire. C'est l'arme la plus solide, mais elle peut parfois manquer d'objectivité ou vous laisser dans le doute.

Ajoutons donc un « adjoint de direction ».

Demandez à l'IA de comparer votre intuition, « Je pense que les clients vont adorer ce plat », avec les « données de ventes passées » et les « informations sur les tendances ».

Ainsi, vous gardez la « chaleur » et la « personnalité » que seul un commerce indépendant possède, tout en menant une activité solide, fondée sur les données.

## Chapitre 2 : Les bases – le « vibe coding » à partir de zéro connaissance

~ Un programme ne s'« écrit » pas. On le « fait construire par l'IA en lui parlant ». ~

### 2-1. Personne ne lit un « long message LINE ». La magie d'un « schéma » en 30 secondes

Parler de « créer un système avec l'IA » peut encore sembler un défi intimidant.

Commençons donc par une « façon d'utiliser l'IA » plus familière, que vous pouvez appliquer dès aujourd'hui.

C'est une révolution dans la manière de « donner des consignes à votre équipe ».

Beaucoup d'entre nous, propriétaires, utilisent LINE *(l'application de messagerie la plus répandue au Japon)* pour joindre le personnel.\
Je fais d'ordinaire tourner le commerce avec peu de monde, et pendant le service il n'y a pas le temps de donner des consignes calmement.

Les consignes et les transmissions passent donc forcément par des messages LINE après la fermeture.

Or il est extrêmement difficile de transmettre par les seuls mots l'image de « voilà comment je veux que ce soit fait », qui n'existe que dans ma tête, à du personnel peu expérimenté ou à un renfort occasionnel.

C'est de là que vient le « long message LINE ».

Plus on s'efforce d'expliquer avec soin, plus le texte s'allonge, et du coup...

« Ah, pardon, je n'ai pas lu jusque-là. »

« C'était un bloc de texte, je n'ai pas vu quelle partie était importante. »

Ce genre d'erreurs ne se produit-il pas aussi sur votre lieu de travail ?

Chez moi aussi, cela s'est produit.

Un jour, pour une application que je développais, j'ai voulu demander à un membre du personnel de prendre des « photos d'ingrédients ».

Les conditions étaient un peu compliquées, et les consignes que j'ai tapées sur mon téléphone sont devenues un long message comme celui-ci.

![Le long message LINE que j'ai réellement envoyé à l'équipe, avec ses fautes de frappe d'origine](images/fig-03.jpg)

Même en voyant cela, le personnel de cuisine, occupé, le survole en se disant « En gros, il faut juste prendre des photos, non ? » et passe à côté des précisions sur l'« angle » et le « sens du récipient ».

Mais je n'ai pas le temps d'ouvrir PowerPoint, d'aligner des formes et de fabriquer une fiche de consignes.

J'ai donc donné ce texte tel quel à une IA (un outil d'IA comme Manus, ou Gemini) et j'ai demandé :

« Résume le contenu de ce texte sur une diapositive, sous forme de "fiche de consignes de travail" que le personnel comprenne d'un coup d'œil. »

### 2-2. L'IA est un « excellent traducteur »

Après quelques secondes d'attente, l'IA a produit une « diapositive-schéma » étonnamment facile à comprendre.

![Diapositive de consignes de travail pour la collecte de données et la prise de photos, générée automatiquement par l'IA](images/fig-04.jpg)

Je n'ai rien conçu. J'ai seulement dit : « Voici le texte, résume-le. »

À partir de mon texte décousu, l'IA a compris instantanément « ce qui est important » et « comment il faut le classer », puis l'a « traduit » dans une mise en page que les humains saisissent intuitivement.

### 2-3. Libération du « stress de ne pas se faire comprendre »

J'ai collé cette image dans LINE et je l'ai envoyée.

L'effet a été immédiat.

La personne n'a posé aucune question et a renvoyé du premier coup des photos parfaites, en « orientation portrait » et sous « 3 angles ».

Jusque-là, je m'agaçais contre le personnel en me disant « Pourquoi ne lisent-ils pas ? » et je m'inquiétais : « C'est peut-être simplement moi qui explique mal. »

Mais le coupable n'était ni le personnel ni moi. C'était la « communication par le seul texte ».

Cette expérience a changé mon regard sur l'IA.

L'IA n'est pas seulement un outil pour « créer de zéro » de nouveaux textes et de nouvelles images.

C'est « un outil qui "convertit" nos "mots qui passent mal" en une forme qui parvient à l'autre personne ».

### 2-4. Le « vibe coding », une nouvelle sorte de dialogue

Une fois à l'aise pour parler avec l'IA, vient enfin l'étape de la « construction d'outils ».

Vous pensez peut-être : « La programmation, c'est impossible pour moi », mais ne vous inquiétez pas.

En ce moment, chez les ingénieurs, un terme fait beaucoup parler de lui : le « vibe coding ».

C'est une méthode où, au lieu que des humains écrivent du code difficile, on construit un système en dialoguant avec l'IA, comme si l'on se synchronisait sur les mêmes « vibes » (le ressenti et l'ambiance).

Sota Fujii, titulaire du titre de Meijin au shogi, a cité le « vibe coding » parmi ses nouvelles passions de cette année, en 2025. Même une personne issue du monde du shogi, qui semble n'avoir aucun rapport avec la construction de systèmes, dit-on, explique en japonais à l'IA ce qu'elle veut et fabrique des outils pratiques.

En parlant avec l'IA, nous aussi, nous pouvons construire des systèmes sans connaissances spécialisées.

Tout ce que vous utilisez, c'est le « japonais ». Quand vous dites : « Je veux que ça fonctionne comme ça » ou « Cette partie est difficile à utiliser », l'adjoint de direction (IA) écrit le code en coulisses.

Autrement dit, vous n'avez pas besoin de devenir un « programmeur ».

Il vous suffit de devenir le « chef de chantier » qui donne des instructions à un « excellent ingénieur (IA) ».

### 2-5. Les « doléances » de votre commerce font les prompts les plus efficaces

Les instructions données à l'IA (les prompts) n'ont pas besoin de belles formules.

Le prompt le plus efficace que j'ai découvert, ce sont les « désagréments » et les « agacements » de votre commerce, autrement dit vos doléances.

- « Faire ce calcul tous les jours, quelle corvée. »

- « Je ne veux pas redimensionner les images à la main. »

Pour l'IA, ce sont de parfaites « exigences de développement ».

Un sentiment du type « je déteste ça » permet de faire émerger plus facilement une solution concrète qu'un objectif du type « je veux faire ça ».

### 2-6. Une erreur n'est pas un « échec ». C'est le « début d'un dialogue ».

Quand vous commencerez à fabriquer quelque chose avec l'IA, vous tomberez forcément sur une « erreur ».

Mais en vibe coding, une erreur n'est pas un échec.

C'est « le signal qu'un véritable échange avec l'IA vient de s'engager ».

Même entre humains, il est rare que l'intention passe parfaitement du premier coup.

Quand l'IA affiche une erreur, balayez-la d'un simple « Ah, ça n'est pas passé », et reformulez : « Non, ce que je veux, c'est ceci. »

Gardez l'échange en cours sans abandonner. Si vous y parvenez, même avec zéro connaissance, vous pourrez sûrement construire « un système qui n'appartient qu'à vous ».

### 2-7. Gagner énormément en efficacité avec des « boutons physiques » – utiliser un mini-clavier

En vibe coding, le plus important est de « soigner la saisie ».

Plus votre conversation avec l'IA est rapide, moins votre réflexion s'interrompt, et plus le développement avance vite. À l'inverse, si vous peinez à saisir, même une excellente idée peut s'évaporer.

Je vous ai dit tout à l'heure : « Quand une erreur s'affiche, la bonne manœuvre est de faire une capture d'écran et de la coller. »

Mais appuyer des dizaines de fois par jour sur [Windows] + [Maj] + [S] (Mac : [Cmd] + [Maj] + [4]), sélectionner une zone à la souris, revenir à l'écran de Gemini et appuyer sur [Ctrl] + [V] (Mac : [Cmd] + [V])...

Franchement, cela fatigue les doigts, non ?

C'est alors que j'ai adopté un « mini-clavier à 6 boutons ».

C'est un petit clavier fabriqué en Chine, qui coûte de quelques centaines de yens à environ mille yens, et qui apparaît quand on cherche « clavier programmable » sur Amazon ou des sites similaires.

![Photo du mini-clavier à 6 boutons que j'utilise au quotidien](images/fig-05.jpg)

J'ai attribué les raccourcis suivants à ces six boutons.

1.  Lancer la capture d'écran

2.  Tout sélectionner (Ctrl + A ; Mac : Cmd + A)

3.  Copier (Ctrl + C ; Mac : Cmd + C)

4.  Coller (Ctrl + V ; Mac : Cmd + V)

5.  Entrée (envoyer)

6.  (En réserve)

C'est tout. Mais l'effet est spectaculaire.

Une erreur s'affiche.

↓

De la main gauche, j'appuie sur le « bouton 1 (capture d'écran) ».

↓

Je sélectionne la zone, puis j'appuie sur le « bouton 4 (coller) » sur l'écran de Gemini.

↓

J'appuie sur le « bouton 5 (envoyer) ».

Tout cela prend seulement 2 secondes.

Vous n'avez pas besoin de retenir des raccourcis clavier ni de contorsionner vos doigts.

Vous pouvez envoyer l'information à l'IA comme si vous manipuliez une manette de jeu.

Comme vous le verrez dans les chapitres suivants, quand l'IA vous fournit un code source corrigé, tout sélectionner (Ctrl + A), copier (Ctrl + C) et coller (Ctrl + V) permettent de le relancer aussitôt, ce qui est pratique.

Avant d'acquérir des connaissances avancées en programmation, essayez d'abord de vous procurer ce petit appareil.

Éliminer physiquement la « corvée de saisie ». C'est le raccourci le plus sûr pour accélérer vos conversations avec votre partenaire IA.

## Chapitre 3 : Pratique 1 – automatiser le travail de création et attirer la clientèle

~ « Coller une capture d'écran et tout confier » s'est révélé la méthode de développement la plus efficace ~

### 3-1. Les tâtonnements pour effacer le « look IA » (stickers LINE)

Une fois à l'aise avec le dialogue par écrit (le vibe coding), j'ai décidé de m'attaquer enfin à la « génération d'images ».

Pour m'exercer, j'ai choisi de fabriquer des « stickers LINE », qui peuvent aussi aider à fidéliser des fans de l'établissement.

Mais les « images lisses, façon images de synthèse » typiques des images générées par l'IA ne conviennent pas à l'atmosphère de mon établissement.

Ce que je visais, c'était « un flat design rétro, dans le style des années 1980, avec une touche dessinée à la main, qui garde la texture du crayon gras et du pinceau ».

C'est là qu'a commencé un long « dialogue » entre moi et l'adjoint de direction (IA).

Au début, j'ai commencé avec des personnages : « deux garçons et un Shiba Inu ».

« Donne-moi 25 expressions pour les conversations de tous les jours. »

« Rends l'épaisseur des traits aléatoire, comme des coups de pinceau. »

Un par un, comme si je donnais des consignes de correction à un illustrateur humain, je lui ai appris patiemment le style que j'aimais.

![Illustrations générées pour les stickers LINE](images/fig-06.png)

### 3-2. La demande audacieuse : « changer seulement le chien en chat »

Quand les choses ont pris forme, j'ai décidé d'un changement de cap majeur : « En fait, je voudrais des filles et un chat. »

Un illustrateur ordinaire aurait fait la grimace en disant : « Quoi, tout recommencer depuis le début ? » Mais l'adjoint de direction (IA) ne s'est pas plaint une seule fois.

« Change les personnages en deux filles, l'une aux cheveux longs et l'autre aux cheveux courts. Des vêtements jaunes et verts, dans le même style dessiné à la main que tout à l'heure. »

« Change le chien en chat, remplace les mots par le parler de chat que tu as généré tout à l'heure, et fais des poses assorties. »

« Fais un chat siamois, pas un roux tigré. »

En plus, j'ai fait une demande qui mettait l'IA à l'épreuve.

« Garde exactement la composition des "garçons et du Shiba Inu" que tu as faite tout à l'heure, et redessine seulement la partie du chien en chat siamois. »

À ma surprise, l'IA a compris cette consigne compliquée. Les positions et les poses des garçons sont restées les mêmes, tandis que le chien était proprement remplacé par un « chat siamois ».

![Planche d'illustrations finale pour les stickers LINE](images/fig-07.png)

Cependant, pour les utiliser comme stickers sur LINE, il faut découper les illustrations, créer des miniatures, tout compresser dans un ZIP et le téléverser.

Cela aussi peut se faire par un dialogue avec Gemini, mais je l'expliquerai de nouveau en 3-6. Premier obstacle : le découpage simple et le « piège de la qualité d'image ».

### 3-3. Cas 2 : la « bannière de Noël » réalisée en 22 échanges

Après les stickers LINE, il y a une autre grande œuvre que j'ai réalisée main dans la main avec l'IA. C'est la bannière d'annonce du « dîner de Noël », le plus gros événement de l'année pour l'établissement.

J'ai utilisé une IA appelée « Nano Banana » (le modèle de génération d'images intégré à Gemini, de Google).

#### Phase 1 : ajuster la mise en page et le texte

Au début, j'ai commencé par placer les éléments nécessaires (le père Noël, les rennes, les informations écrites) sur une toile en format large.

En regardant les images obtenues, j'ai donné des consignes.

« Ça fait un peu vide. Ajoute des illustrations d'un sapin de Noël et de champagne. »

« Le menu est une liste à puces et c'est difficile à lire. Résume-le en "six plats au total", et agrandis le titre pour qu'il attire davantage l'œil. »

![Image générée au début du processus, encore un peu vide](images/fig-08.png)

#### Phase 2 : régler l'« animation »

Une fois la mise en page fixée, vint ensuite l'ambiance. Il manquait un « esprit de fête ».

J'ai demandé : « Rends ça plus animé ! Disperse plein de petits pères Noël et de rennes, des ballons et des confettis. »

Cette fois, l'écran est devenu beaucoup trop chargé.

« Désolé, il y avait trop d'éléments. Réduis le nombre de personnages pour épurer l'ensemble. »

Pouvoir répéter ce réglage fin d'« ajouts et de retraits », c'est la force de l'IA.

#### Phase 3 : l'idée inattendue d'une « refonte complète »

En cours de production, un doute s'est glissé. « Ne serait-ce pas plus appétissant de montrer des images des plats plutôt que de faire des personnages l'élément principal ? »

J'ai donc demandé sans détour : « Comme variante, fais un design qui met en vedette des illustrations des vrais plats. »

![Proposition illustrée mettant en avant les plats (certains caractères sont déformés)](images/fig-09.png)

L'IA a aussitôt imaginé des illustrations de plats appétissantes, mais après comparaison, j'ai décidé de garder finalement le design d'origine avec les personnages. Même un « revenons à ce qu'on avait » de ce genre, on peut le demander à l'IA sans hésiter.

#### Phase 4 : le dernier rempart, c'est le regard « humain »

Une fois le design final arrêté, j'ai aussi confié à l'IA les variantes de taille, pour les publications Instagram (verticales) et pour les Stories (encore plus hautes).

Et puis, juste au moment où tout allait être terminé, j'ai remarqué une grave erreur.

« Attends, le jour de la semaine est faux sur la date ! »

L'IA est douée pour dessiner des images, mais elle ne comprend pas les jours de la semaine d'un calendrier. Si je l'avais publiée telle quelle, cela aurait été un désastre.

J'ai vite demandé : « Corrige la date en "24/12 (mer.) et 25 (jeu.)" ! » et terminé la version finale.

![Version finale de la bannière après corrections](images/fig-10.png)

Au total, 22 tours de corrections et de dialogue.

L'IA n'est pas une baguette magique, mais si vous lui parlez avec patience, il n'existe pas de partenaire de design plus fiable.

### 3-4. Cas 3 : un avis d'ouverture du Nouvel An qui évolue avec la situation

L'effervescence de Noël s'est à peine éteinte que l'événement suivant arrive : l'activité de fin d'année et du Nouvel An.

Pour un restaurant ou un bar, faire passer le message à cette période est une course contre la montre. « Jusqu'à quand êtes-vous ouverts en fin d'année ? » « Quand rouvrez-vous après le Nouvel An ? » La clientèle cherche toujours des informations.

Mais les informations changent de minute en minute.

« Quand le service de fin d'année sera passé, je veux le réécrire pour qu'il n'affiche plus que l'avis du Nouvel An. »

« Je l'ai publié sur X (en paysage), mais je veux aussi le diffuser sur Instagram (en portrait). »

Si j'avais confié cela à un designer extérieur, les frais de retouche seuls auraient été un cauchemar, et surtout cela n'aurait pas été prêt à temps.

J'ai donc une fois de plus fait équipe avec une IA de génération d'images (Nano Banana) et j'ai commencé à travailler sur des bannières pour passer la fin d'année et le Nouvel An.

#### Étape 1 : le style « dessin au crayon gras des années 80 »

D'abord, j'ai construit l'allure générale.

Ce qui convient à mon bar, ce ne sont pas des images de synthèse brillantes.

« Un style chaleureux, comme un dessin au crayon gras fait à la main dans les années 80, avec des coups de pinceau visibles. Garde le fond blanc uni. »

Avec cette consigne comme noyau, et en pensant à une annonce sur X (anciennement Twitter), j'ai commencé à travailler sur une toile en paysage.

#### Étape 2 : le Serpent qui s'en va et le Cheval qui arrive. Trinquer pour se passer le relais

Au début, j'avais pensé ne dessiner qu'un seul animal du zodiaque, mais c'était après tout le passage d'une année à l'autre.

Une idée m'est venue : « Je voudrais que l'animal de l'année qui s'achève (le signe du zodiaque de cette année) et celui de l'année qui commence (celui de l'an prochain) apparaissent tous les deux. »

J'ai donc donné cette consigne à l'IA :

« Mets un groupe de serpents (l'année du Serpent) sur le côté gauche de l'écran et un groupe de chevaux (l'année du Cheval) sur le côté droit. Fais-les tenir chacun une chope de bière et trinquer joyeusement, comme pour se passer le relais à la fin de l'année. »

L'image générée par l'IA correspondait exactement à ce que j'avais imaginé.

Des serpents charmants à gauche, des chevaux à l'air fiable à droite, qui boivent ensemble par-delà la frontière entre les espèces.

De la « fin d'année (Serpent) » au « Nouvel An (Cheval) ».

En une seule image, le passage du temps et l'esprit de fête se trouvaient superbement condensés.

![Le serpent à gauche et le cheval à droite trinquent pour symboliser le passage à la nouvelle année](images/fig-11.png)

#### Étape 3 : la « direction d'acteurs » et l'« essayage des costumes » pour les animaux

Une fois la composition arrêtée, le travail suivant a été la mise en scène plus fine. Là encore, l'IA s'est prêtée de bonne grâce à mes exigences pointilleuses.

Sur les premières images, les animaux étaient simplement alignés, ou tenaient leur chope de façon peu naturelle.

« Fais-les paraître plus heureux ! Comme des habitués qui passent un super moment ensemble. »

« Je veux aussi une impression de saison. Mets-leur des écharpes et des nœuds papillon, donne-leur un air d'hiver. »

Avec cette seule remarque, les animaux à l'écran se sont enveloppés d'écharpes rouges et vertes bien chaudes et sont aussitôt devenus les vedettes d'une « fête d'hiver ».

« Oui, voilà, on retrouve cette chaleur d'un verre en plein jour par temps froid. »

En regardant de près, certains mouvements de mains et certaines façons de tenir les chopes restent peu naturels. Mais être pointilleux demande plus de temps. En arbitrant entre le temps passé et la qualité du message transmis, j'accepte un résultat raisonnablement bon.

#### Étape 4 : au fil du temps, les informations changent

C'est à partir d'ici que l'IA montre vraiment sa valeur.

La bannière d'origine affichait à la fois le calendrier de décembre et celui de janvier, sous le titre « Calendrier d'ouverture de fin d'année et du Nouvel An ».

Mais une fois le 31 décembre passé, les informations de fin d'année ne sont plus nécessaires.

J'ai rouvert le projet sur lequel je travaillais et demandé une importante modification du texte.

1.  Changer le titre : de « Horaires de fin d'année et du Nouvel An » à « Ouvert en journée pour trinquer à la nouvelle année ».

2.  Épurer les informations : supprimer le calendrier de décembre, désormais passé, et se limiter au « calendrier du Nouvel An (du 2 au 4 janvier) ».

3.  Corriger les personnages du zodiaque : transformer en chevaux les serpents de l'année qui s'achève.

4.  Ajouter un argument : ajouter une offre attrayante, « highballs (whisky-soda) et poulet frit à volonté », comme nouvel attrait pour la clientèle.

![Étape 4 : au fil du temps, les informations changent](images/fig-12.png)

Sans recréer l'image de zéro, j'ai pu renouveler les informations comme on réécrit des mots sur un tableau noir. C'est la force du design par l'IA.

#### Étape 5 : de X à Instagram. Un format qui change à volonté

Et maintenant, la touche finale.

« Je l'ai annoncé sur X. Ensuite, je veux le diffuser dans les Stories Instagram. »

Mais les Stories utilisent le format « portrait », qui remplit tout l'écran du téléphone. Si l'on y place telle quelle une image en paysage, on obtient des bandes vides en haut et en bas, et le rendu est mauvais.

Avec une illustration ordinaire, ce genre de changement obligerait à tout redessiner.

Mais je n'ai fait que dire à l'IA :

« Garde ce design, mais réorganise-le en mise en page portrait pour les Stories Instagram. »

L'IA a réorganisé les animaux, qui étaient répartis à l'horizontale, en une disposition verticale, ajusté l'équilibre du texte et généré aussitôt un design adapté aux smartphones.

![Image finale au format portrait pour les Stories Instagram](images/fig-13.png)

### 3-5. Cas 4 : créer le logo du bar – un dialogue qui transforme le « sens » en « forme »

Au-delà des « images » comme les bannières et les stickers, j'ai aussi relevé avec l'IA un défi plus abstrait : concevoir un nouveau logo.

Il est destiné à être intégré aux bannières et autres supports, pour que l'on reconnaisse Tamuro au premier coup d'œil.

Le sujet, c'est Tamuro, le bar que je tiens le soir. Ce nom porte un vœu fort : « être un lieu où toutes sortes de gens se retrouvent librement et joyeusement (tamuro-suru, se retrouver) dans le quartier de Higashi-Nakano ».

Comment condenser cette « histoire » invisible en un petit logo ? Un patient dialogue avec l'IA a commencé.

#### Étape 1 : choisir la typographie et l'orientation du design

Au début, j'ai lancé à l'IA des idées comme « un look sobre avec le kanji 屯 » et « quelque chose de pop en katakana », et je lui ai fait produire quelques ébauches.

Mais aucune ne me convenait. Vu la nature du bar, je voulais quelque chose de plus moderne, avec un côté neutre qui accueille la diversité.

J'ai donc changé de cap.

« Partons de l'alphabet, très polyvalent : "TAMURO". Le style doit être du "flat design", sans décoration compliquée. Et le rendu doit rester fort même en monochrome. »

L'IA m'a immédiatement proposé un "TAMURO" simple et gras, en sans-serif.

![Logo en typographie sans-serif](images/fig-14.png)

#### Étape 2 : donner du « sens » à la forme

C'est ici que commence la véritable épreuve. Des lettres toutes simples ne signifient rien. Et avoir seulement le "M" au centre ne dit pas grand-chose non plus.

« Je veux exprimer l'origine du nom, "des gens qui se rassemblent". Pourrais-tu ramener l'ensemble dans un "cercle" chaleureux, tout en donnant à chaque lettre de l'alphabet une forme qui ressemble à une personne qui bouge joyeusement ? »

C'est une commande très abstraite. Mais l'imagination de mon adjoint de direction (l'IA) a dépassé mes attentes.

L'IA a proposé un design où l'ossature des lettres "T", "A", "M" et des autres était transformée en silhouettes de gens qui dansent, bras et jambes déployés.

![Logo associant les lettres de l'alphabet à des silhouettes humaines](images/fig-15.png)

#### Étape 3 : le bras de fer entre design et lisibilité

« Intéressant ! Mais comme ça, on ne peut pas lire "TAMURO"... »

Si l'on donne trop de poids au design, cela cesse d'être reconnaissable comme du lettrage, et si l'on met le poids sur le lettrage, cela perd son charme. J'ai buté sur ce dilemme.

À partir de là, ce furent des réglages fins répétés.

« La lettre "A" ressemble à une personne, c'est bien, mais accentue un peu plus sa structure de "A". Mets bien la barre transversale. »

« L'équilibre général est bon, mais les personnages sont trop serrés et paraissent à l'étroit. Laisse un peu plus d'espace, pour une impression plus légère et joyeuse. »

« Combine les gens qui dansent de tout à l'heure avec les lettres TAMURO, et fais-en un cercle ! »

![Logo circulaire "TAMURO" abouti après plusieurs essais](images/fig-16.png)

Bien qu'il soit fait de silhouettes de gens pleines de vie, un coup d'œil sur la partie basse suffit pour lire clairement "TAMURO".

À force de renvoyer des idées à l'IA, encore et encore, j'ai obtenu un logo qui me plaît, un logo qui réunit la lisibilité, la qualité du design et, surtout, l'« intention » que j'ai voulu donner à mon bar.

Il sert désormais d'icône aux comptes X (anciennement Twitter) et Instagram du bar.

### 3-6. Premier obstacle : le découpage simple et le « piège de la qualité d'image »

Le défi créatif de la création du logo était terminé.

Mais le travail n'était pas fini.

Retour aux stickers LINE. Ce que j'avais en main, c'était une « planche » de 25 illustrations dessinées sur une seule page.

Pour les soumettre comme stickers LINE, il fallait découper chacune, rendre le fond transparent et la redimensionner. C'était une tâche fastidieuse que je repoussais.

« Pas question de les découper à la main... »

J'ai consulté Gemini pour demander une solution. Gemini a dit, comme si de rien n'était :

« Automatisons cela avec un langage de programmation appelé Python. »

Franchement, j'ai failli abandonner sur-le-champ.

« Python ? J'ai déjà entendu ce nom, mais installer ce genre de logiciel sur mon ordinateur me fait peur. La configuration doit aussi être difficile. N'attendez pas autant de quelqu'un qui tient un bar... »

Mais c'est l'un des temps forts de ce livre. Comme s'il avait senti ce que je pensais, Gemini m'a fait une proposition surprenante.

Gemini :

« Vous n'avez besoin de configurer aucun environnement. Utilisez un outil gratuit de Google appelé "Google Colab". Il fonctionne dans votre navigateur, il vous suffit donc d'y copier-coller le code que j'écris pour qu'il s'exécute. »

« Quoi ? Ça existe, un truc pareil ? »

Je n'en croyais pas mes oreilles. Je n'avais jamais imaginé qu'il existe un environnement où la programmation tourne dans un simple navigateur, sans rien installer sur mon propre PC.

Pas « après avoir étudié Python », mais « en laissant l'IA m'apprendre jusqu'à l'existence de l'outil (Colab) ».

À cet instant, mon idée reçue selon laquelle « programmer, c'est énormément de préparation » s'est effondrée.

### 3-7. Ne « lisez » pas l'écran d'erreur, « capturez-le et envoyez-le »

Comme indiqué, j'ai ouvert Google Colab, collé le code et appuyé sur le bouton d'exécution.

Mais la réalité n'est pas si rose. Ce qui est apparu à l'écran, c'était une suite de texte rouge vif... un message d'erreur.

« Error: Image file not found... »

Le moi d'avant aurait eu une réaction allergique rien qu'en voyant cette erreur et aurait discrètement refermé le navigateur.

Mais maintenant, j'avais un allié : l'IA « multimodale », une IA qui a des yeux.

Je n'ai même pas essayé de lire le message d'erreur.

J'ai simplement pris une capture d'écran et je l'ai collée, hop, dans la zone de saisie de Gemini.

Et j'ai ajouté une seule ligne : « Une erreur s'est affichée. »

![Capture d'écran de l'erreur Google Colab telle quelle collée dans Gemini](images/fig-17.png)

Gemini a analysé l'image tout de suite et m'a renvoyé une réponse.

Gemini :

« Ah, le nom de fichier de l'image chargée est faux. J'ai corrigé le code pour utiliser ".jpg". Relancez-le avec cette version. »

« ...Waouh, c'est amusant ! »

Cet échange ressemblait moins à de la programmation qu'à un jeu des sept erreurs ou à un échange de balles.

- Moi : (je colle une capture d'écran) « Ça s'est encore arrêté. »

- Gemini : « La taille de l'image ne correspond pas. J'ajoute une fonction qui l'ajuste automatiquement. »

- Moi : (je colle une capture d'écran) « Cette fois, l'image paraît pixélisée. »

- Gemini : « J'ai oublié d'ajouter le traitement appelé "LANCZOS", qui préserve la qualité de l'image. Je corrige. »

Je ne comprends pas une seule ligne du code. Quand une erreur s'affiche, je prends simplement une capture d'écran et je la lance à l'IA en disant « Regarde ! »

Cette « délégation totale de l'analyse des erreurs » a été le plus grand secret de la façon dont j'ai réussi, avec zéro connaissance, à construire un système, et en même temps l'expérience la plus enthousiasmante de toutes.

### 3-8. Le plus grand obstacle : le « décalage du dessin à la main » et le « débordement »

En poursuivant cette « conversation faite d'erreurs », le système s'est affiné de plus en plus.

Et j'ai enfin abordé le plus grand défi : la « Phase 2 : découpe automatique des mises en page dessinées à la main ».

J'ai voulu aller plus loin.

« Faisons une planche de 5×5, soit 25 stickers. Et comme je veux un rendu plus artisanal, je veux les placer librement, sans que la grille m'impose ses lignes. »

Avec un code qui divise simplement la planche en parts égales, la main d'un personnage ou une lettre déborde dans la case voisine et se retrouve affreusement tronquée.

J'ai aussi essayé une méthode qui consiste à « tout découper sauf le fond blanc », mais les marges sortaient inégales et cela a échoué.

J'étais sur le point d'abandonner. Puis, en puisant dans mes réflexes de l'époque où je travaillais dans le domaine des systèmes, j'ai dit à Gemini :

« Je veux que tu abandonnes l'idée de découper l'image aux ciseaux. À la place, regarde dans quelle case se trouve le "point central" de chaque dessin. Si le centre est dans cette case, alors même si cela déborde un peu, considère le dessin entier comme "appartenant à cette case" et dépose-le dans le seau de cette case. »

C'est la solution que j'ai baptisée la « méthode de la grille et du seau ».

Pourquoi ai-je pensé à « mettre dans un seau selon le point central » plutôt qu'à « découper aux ciseaux » ?

La façon de penser d'un amateur (analogique) : on imagine « détacher un seul dessin aux ciseaux ». Ainsi, on coupe pile le long de la ligne, et les mains et les pieds du personnage sont tronqués.

La façon de penser du monde des systèmes (numérique) : un ordinateur n'a aucun sens physique du « découpage ». Il a en revanche des « coordonnées (des positions) ». Voici comment je voyais les choses : « Même si cela déborde un peu, tant que le "nombril (point central)" du dessin est dans la case, on peut considérer tout le dessin comme "appartenant à cette case". »

![L'approche analogique "couper le long des lignes" et l'approche numérique "choisir par le point central"](images/fig-18.png)

C'est cela, « traduire un travail analogique flou en règles numériques claires ». Quand vous donnez des instructions à une IA, il est efficace d'imaginer une règle de ce genre, dont la réponse sort identique « quelle que soit la personne qui regarde (ou qui calcule) ».

Gemini a transformé cette demande abstraite en code de façon superbe. Le résultat était parfait.

Le lettrage « Merci ! » et les queues qui avaient débordé dans les cases voisines ont tous été proprement reconnus et récupérés chacun sous la forme d'un sticker à part entière.

Il a même respecté ma demande égoïste : « Le dernier (le 25e) n'est pas nécessaire, saute-le. » J'avais enfin un outil où « on dépose l'image, on appuie sur un bouton, et l'on obtient un jeu complet d'images pour la soumission à LINE ».

Tout ce que j'ai fait, c'est transmettre le « problème du terrain (les dessins sont coupés) » et proposer une « solution logique (décider selon le point central) ». L'IA a écrit tout le code difficile.

C'est l'essence même du « vibe coding » : construire des systèmes à partir de zéro connaissance.

#### Résumé du chapitre 3

1.  Dessiner avec l'IA, ce n'est pas « une fois et c'est fini ». On peut refaire autant de fois qu'on veut selon la situation : changer de personnages, ajouter une touche de saison, changer de support.

2.  Même un « concept » abstrait (des gens qui se rassemblent) peut être transformé en « forme » (un logo) par un dialogue répété.

3.  Les tâches fastidieuses (découper des images) sont exactement ce que Gemini × Google Colab peut automatiser. Les erreurs se résolvent avec des captures d'écran.

#### Encadré 1 : cours accéléré de « Google Colab » pour les propriétaires sans bagage technique

~Utilisez une « cuisine en location » et laissez votre propre PC tel quel~

Revenons sur « Google Colab », évoqué dans le texte principal. Faire de la programmation (Python) sur son propre ordinateur, c'est comme « préparer de vrais ramen à partir de zéro, en commençant par le bouillon, dans la cuisine de votre domicile ». La préparation demande énormément de travail.

Google Colab, en revanche, c'est « une cuisine en location gratuite, entièrement équipée en ustensiles de cuisine ». Il suffit d'ouvrir votre navigateur et les meilleurs outils sont prêts. Vous n'avez à modifier aucun réglage de votre ordinateur. Vous pouvez programmer avec un simple navigateur tout en gardant votre environnement propre. Commencez par chercher « Google Colab » et jetez un œil à cette cuisine en location.

#### Encadré 2 : ne pas « lire » l'écran d'erreur est la bonne réponse

~Maîtrisez l'arme ultime : la capture d'écran~

Quand une erreur s'affiche, essayez-vous consciencieusement de déchiffrer le message en anglais ? C'est une perte de temps.

Quand un plat a un goût bizarre pendant que vous cuisinez, vous demandez au chef de goûter. De la même façon, montrez simplement à l'IA une « capture d'écran ».

- Windows : \[Win\] + \[Maj\] + \[S\]

- Mac : \[Cmd\] + \[Maj\] + \[4\]\
  Appuyez sur ces touches, tracez un cadre autour de l'erreur et collez-le dans Gemini. C'est tout. Ne « lisez » pas l'erreur, « montrez » l'erreur. Ce simple changement d'état d'esprit triplera votre vitesse de développement.

Je vous ai présenté plusieurs exemples jusqu'ici, et tout ce que je fais se résume aux trois points suivants.

・Ne pas exiger la forme finale d'un seul coup (on peut partir du principe qu'il y aura un dialogue)\
・Dire sans hésiter « non, ce n'est pas tout à fait ça »\
・Partir du principe que le coût des corrections est nul et lancer ses demandes avec désinvolture

Nul besoin de talent pour le design. Il suffit d'avoir le courage de mettre en mots « quelque chose me gêne ».

## Chapitre 4 : Pratique, deuxième partie – alléger le travail quotidien (avec l'IA multimodale)

~Venez à bout de la « saisie de données fastidieuse » avec un seul smartphone~

### 4-1. Le casse-tête de la mise à jour de la carte des vins

Pour un bar ou un restaurant, mettre à jour la carte est une charge peu glorieuse mais lourde.

Ce qui m'a causé le plus de soucis, c'était l'élaboration de la « carte des vins ».

Chaque fois qu'un nouveau vin arrive, il faut faire tout ce travail.

1.  Regarder l'étiquette de la bouteille (une écriture cursive étrangère, difficile à lire).

2.  Saisir sans faute le nom de la cuvée et le millésime (l'année) sur l'ordinateur.

3.  Chercher en ligne les caractéristiques et le goût du vin.

4.  Rédiger une « présentation » qui donne envie à la clientèle de la lire.

5.  Réfléchir aux plats qui s'accordent avec le vin (les accords).

Faire tout cela dictionnaire en main, dans les creux d'un service chargé, est presque impossible. Je remettais à plus tard en me disant « je le ferai après », et la liste des recommandations finissait souvent par ne jamais être mise à jour.

### 4-2. Une simple photo. Le choc du « Gem de la carte des vins »

J'ai donc décidé d'essayer la « fonction multimodale (reconnaissance d'images) » de Gemini.

La méthode est d'une simplicité désarmante.

1.  Prendre la bouteille de vin en photo avec le smartphone.

2.  Envoyer cette photo à Gemini.

3.  Ajouter une seule ligne : « Fais-en une liste. »

C'est tout.

![Photo d'une véritable étiquette de bouteille de vin, prise avec un smartphone](images/fig-19.jpg)

Gemini lit alors instantanément les informations de l'étiquette sur la photo.

Il ne se contente pas de recopier le nom de la cuvée, par exemple « Cave d'Occi Winery, Tsukimi de Ippai 2024 » : il cherche aussi ses caractéristiques dans une immense base de données en ligne et rédige automatiquement une présentation attrayante.

Ce qui m'a encore plus surpris, c'est qu'il a aussi fourni des « suggestions d'accords » en même temps.

Des propositions comme « Le riche arôme de ce vin se marie bien avec ○○ » se sont affichées à l'écran en quelques secondes.

Les heures que je passais à me battre avec un dictionnaire s'étaient réduites à un seul clic sur le déclencheur du téléphone.

### 4-3. Créer votre propre « Gem »

Pour rendre ce travail bien plus efficace, j'ai ensuite utilisé une fonction appelée « Gems ».

C'est une « fonction d'IA personnalisée » à laquelle on peut faire mémoriser à l'avance un rôle et des règles.

Tout réexpliquer à chaque fois, « Tu es sommelier. Regarde cette photo et… », est fastidieux.

J'ai donc enregistré à l'avance les « instructions (prompt) » suivantes dans Gemini. C'est l'intérieur de la tête du « sommelier IA dédié » de mon bar.

#### Les instructions que j'ai réellement enregistrées

> Lis l'image et crée une carte des vins au format suivant.
>
> Pour les prix, n'utilise pas les prix du marché. Calcule-les en supposant le prix de la bouteille dans un restaurant ordinaire (environ 2,5 à 3 fois le prix d'achat).
>
> N'utilise pas de tableau. Fais en sorte que cela tienne sur une ou deux feuilles A4.
>
> Le format n'est qu'une référence ; crée la liste uniquement à partir de ce qui a été saisi.
>
> Le format est ci-dessous.
>
> Royaume-Uni 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8500 (environ $57)
>
>  Or pâle aux bulles agréables. Notes de melon et de miel parmi des arômes d'agrumes… (le reste est omis)

En réalité, la moitié inférieure de ce prompt, la partie « format (exemple) ».

Je ne l'ai pas inventée de toutes pièces.

Auparavant, quand je cherchais des informations sur le vin en ligne, je me disais « tiens, la description de cette boutique est facile à comprendre » ou « cette façon d'écrire sur ce site donne vraiment envie de goûter », et je copiais-collais simplement ces passages dans un bloc-notes, encore et encore.

J'ai envoyé ce « mémo patchwork » tel quel à Gemini.

« Ce sont des passages que j'ai copiés et rassemblés il y a un moment. Imite cette tonalité et rédige de la même façon la présentation du vin de la nouvelle photo. »

Je ne lui ai rien dit de plus.

Même ainsi, cette instruction contient trois astuces qui allègent la charge sur le terrain.

① « La logique de calcul du prix »

C'est le plus grand gain de temps. Comme je demande « le prix qu'un restaurant afficherait » plutôt que « le prix du marché », l'IA remonte à partir des prix d'achat habituels et me donne un chiffre comme « ¥8500 (environ $57) » qui peut aller directement sur la carte. (La décision finale vous revient bien sûr, mais disposer d'un repère facilite les choses.)

② « Pas de tableau, mais un format qui tient sur une feuille A4 »

Si le résultat arrive sous forme de tableau, comme dans Excel, la mise en page se disloque quand on le colle dans le menu. En demandant dès le départ un « format de carte A4 », je vise un résultat qui s'imprime et s'utilise tel quel.

③ Utiliser un texte copié-collé du web comme « exemple »

Au lieu de demander vaguement « Écris une jolie présentation », je lui montre un exemple concret (mon mémo copié-collé) : « drapeau 🇬🇧 + nom du vin + prix + description sensorielle ».

Quand on montre un exemple à une IA, elle comprend « ah, voilà le ton et le style à adopter », et la précision du résultat fait un bond. En termes techniques, cela s'appelle le « few-shot prompting », mais c'est au fond la même chose que de « former en montrant l'exemple ».

Et pour cet « exemple », des textes trouvés peuvent parfaitement suffire, l'équivalent écrit d'une photo trouvée sur le web.

![Le texte de la carte des vins terminée, produit par Gemini](images/fig-20.png)

### 4-4. Même pas besoin d'une image. La révolution du copier-coller depuis LINE

Ce qui est formidable avec ce « Gem de la carte des vins », c'est que l'entrée ne se limite pas aux photos.

En réalité, dans un bar, on passe souvent les commandes au caviste par LINE, n'est-ce pas ?

Une fois la commande passée, un message comme celui-ci arrive du caviste.

> « Merci pour votre fidélité. Nous avons bien reçu votre commande comme suit.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 bouteilles
>
> ・Ridgeview Bloomsbury 6 bouteilles
>
> ・○○ (nouveau vin) 2 bouteilles
>
> Nous livrerons demain. »

Un jour, l'idée m'est venue d'un coup : « Et si j'utilisais ce texte tel quel ? »

Pour essayer, j'ai copié ce message LINE du bout du doigt et je l'ai collé directement dans Gemini.

Le résultat était parfait.

Gemini a reconnu uniquement les « noms de produits » dans le message LINE, a cherché les informations en ligne et a créé une liste dans le format habituel (drapeau + prix + description).

Autrement dit, je n'ai même plus besoin d'attendre l'arrivée des bouteilles pour les photographier.

Au moment précis où je passe la commande, par un simple copier-coller dans mon téléphone, la liste de la carte est terminée avant même que les produits arrivent.

Pas besoin d'ouvrir un ordinateur, pas besoin de lancer l'appareil photo.

Dans un coin de la cuisine ou dans le train, le travail se fait avec le seul téléphone.

N'est-ce pas là l'« efficacité réelle » à laquelle ont droit les propriétaires qui travaillent seuls ?

### 4-5. Les suggestions de l'IA × le jugement du terrain (la réalité)

Cela dit, je n'avale pas les suggestions de l'IA sans réfléchir. Ce qui compte ici, c'est notre « jugement humain sur le terrain ».

Une fois, l'IA a fait cette suggestion pour accompagner un vin :

IA : « Avec ce vin rouge, le canard rôti sauce à l'orange est un accord parfait. »

Une suggestion merveilleuse, mais ce jour-là, il n'y avait malheureusement pas de canard dans le réfrigérateur du bar.

Je ne me dis pas « l'IA le dit, donc je dois acheter du canard ». Voici comment je raisonne :

Moi (sur le terrain) : « On n'a pas de canard, mais il est arrivé aujourd'hui du bon poulet fermier. Il a un gras savoureux, comparable à celui du canard, alors je vais saisir ce poulet jusqu'à ce que la peau soit croustillante et le finir avec une sauce à l'orange, comme le dit l'IA. »

« Le savoir de l'IA (le canard et l'orange vont ensemble) » × « le stock du terrain (nous avons du poulet) » = « un nouveau plat décidé sans hésiter, et réaliste ».

Cette combinaison est le vrai plaisir de développer des plats avec l'IA.

L'IA donne la réponse du manuel, mais elle ne sait pas ce qu'il y a aujourd'hui dans le réfrigérateur. Combler cet écart, c'est votre travail de propriétaire.

### 4-6. Le dernier kilomètre : l'IA ne peut pas « goûter »

Il y a encore une chose que vous ne devez jamais confier à l'IA.

C'est la dégustation que vous faites avant de servir quoi que ce soit à la clientèle.

Les présentations et les accords que l'IA écrit reposent sur des « données générales et conventionnelles ».

Mais le vin est une matière vivante. Même avec la même étiquette, la saveur change selon le millésime et la façon dont il a été conservé.

Une fois, l'IA avait écrit pour un vin blanc : « Un vin sec, frais et léger. Parfait avec un carpaccio de fruits de mer. »

Mais en ouvrant réellement la bouteille et en la goûtant, il était plus évolué que prévu, avec des notes riches, proches du miel.

« Si je le sers comme un “vin sec et léger”, la clientèle sera déçue… Il irait mieux avec un poulet à la crème qu'avec un carpaccio. »

J'ai aussitôt corrigé le texte produit par Gemini.

- Avant (IA) : « Frais et léger. Bien pour les entrées »

- Après (humain) : « Riche, ample grâce à l'évolution. Assez solide pour tenir tête à un plat principal »

L'IA fait 90 % du brouillon, et l'humain goûte et ajoute les « 10 % restants (l'âme) ».

Cette vérification relève de la responsabilité de la personne qui tient le restaurant, et c'est quelque chose que l'IA ne pourra jamais imiter.

Pas « parce que l'IA l'a dit », mais « parce que j'en ai bu et que c'était bon ».

Pour servir avec cette assurance, aujourd'hui encore, je goûte le vin fraîchement ouvert, une carte faite par l'IA dans une main.

#### Encadré 3 : Conseils pour photographier afin que l'IA voie « correctement »

~ Comme montrer une étiquette à un sommelier ~

Quand vous envoyez une photo à Gemini, quelques petites astuces peuvent améliorer considérablement la qualité de sa reconnaissance.

1.  Éviter les reflets : les étiquettes de bouteille réfléchissent facilement la lumière ; changez un peu l'angle, ou faites de l'ombre avec votre corps en prenant la photo.

2.  Prendre plusieurs clichés et les envoyer ensemble : pour le contenu d'un réfrigérateur par exemple, envoyez une vue d'ensemble et des gros plans, et l'IA reconnaîtra même les produits dans les angles morts.

3.  Pointer du doigt : il est aussi utile de pointer du doigt l'endroit que vous voulez que l'IA regarde en prenant la photo. Mettez quelque chose comme « Je pointe du doigt » dans le prompt. C'est comme montrer un plat sur la carte dans un restaurant à l'étranger.

## Chapitre 5 : Applications – Analyse de l'activité et amélioration de la rentabilité

~ Déterrez la « mine d'or invisible ». Une réunion de direction avec votre consultant IA ~

### 5-1. La nuit où je me casse la tête sur une calculatrice à chaque fin de mois

Pour nous qui tenons de petits restaurants indépendants, aucun moment ne pèse autant que la clôture mensuelle.

Dans le calme de la nuit, à additionner les données de la caisse et à les saisir dans Excel, on n'entend que son propre soupir.

« L'objectif de chiffre d'affaires de ce mois était de ○○0000 yens. … Je ne l'ai pas atteint. »

« Le nombre de clients n'est pas mauvais. C'était plein le week-end. Mais, pour une raison inconnue, le ticket moyen n'augmente pas. »

Pourquoi n'arrive-t-on pas à atteindre l'objectif ? Ma cuisine est pourtant bonne. Je me donne du mal pour le service.

« Peut-être que les prix sont trop élevés ? »

« Non, si on baisse encore, on ne fera plus de bénéfice. Et le coût des ingrédients augmente aussi. »

Des questions sans réponse tournent et retournent dans ma tête, et je finis par m'en remettre à du pur volontarisme : « Le mois prochain, je mettrai plus d'énergie et je pousserai davantage les recommandations. » C'était ma mauvaise habitude, et celle de nombreux propriétaires.

Mais j'ai maintenant un conseiller sans émotions.

J'ai présenté à Gemini les données de ventes de ce mois-là et celles du menu du bar.

### 5-2. Une expérience : faire lire à l'IA les « visuels » et les « chiffres » en même temps

Cette fois, j'ai donné trois informations à Gemini.

J'ai tout jeté en vrac : le « design (cerveau droit) » et les « chiffres (cerveau gauche) » que je gérais toujours séparément.

1.  « L'objectif de chiffre d'affaires de ce mois »

- Mon souhait le plus pressant. Le chiffre que je dois absolument atteindre.

2.  « Toutes les données récentes des tickets de caisse (CSV/Excel) »

- Le résultat dans la réalité. La froide réalité des faits : qui a commandé quoi, et à quel prix.

3.  « Un fichier PDF du menu actuel »

- Le monde que voit la clientèle. Des informations visuelles : placement des photos, taille et couleur du texte.

Et ensuite, j'ai posé cette question.

Ce n'était pas un ordre de travail comme le précédent « fais une image ». C'était une question, de celles que posent les propriétaires.

> « Compare les données de ventes actuelles (la réalité) avec la mise en page du menu (l'apparence).
>
> Indique le goulot d'étranglement : que nous manque-t-il pour atteindre l'objectif de ○○0000 yens ? »

### 5-3. L'« idée reçue de la direction » que l'IA a percée à jour

Quelques secondes plus tard, la réponse de Gemini est arrivée, et elle a frappé en plein dans mon angle mort.

Je m'attendais à des conseils généraux comme « Développons un nouveau plat » ou « Faisons de la promotion sur les réseaux sociaux ».

Mais ce que l'IA a relevé, c'était un fait que j'essayais inconsciemment de cacher.

La réponse de Gemini :

> « En croisant les données avec le menu, j'ai relevé un important manque à gagner.
>
> La formule boissons à volonté, qui a une marge élevée et peut relever de façon fiable le ticket moyen, est actuellement indiquée sur le menu (Avant) uniquement en texte, discrètement, tout en bas à gauche.
>
> En revanche, la meilleure place du menu, tout en haut, est occupée par le “Set ¥2200 (environ $15)” à petit prix. Ainsi, la clientèle glisse vers la formule la moins chère et ne remarque même pas la formule à volonté plus chère. »

En regardant l'écran, je n'ai pas pu m'empêcher de grogner. C'était en plein dans le mille.

Nous avons bien une formule à volonté. Mais quelque part dans mon esprit, je pensais ceci :

« Nous ne sommes pas un izakaya de chaîne *(un pub japonais décontracté qui sert à manger et à boire)*. Afficher une formule à volonté en gros caractères fait bas de gamme. »

« Je veux qu'on savoure le goût du vin, donc seules les personnes qui connaissent cette formule devraient la commander. »

Cette « idée reçue » de ma part apparaissait dans la mise en page du menu, dans le texte tout en bas.

![Le menu Avant. L'offre à volonté est en bas à gauche et ne se remarque pas. On distingue aussi mal que la nourriture est à part](images/fig-21.png)

Cela n'a pas échappé à l'IA.

« Vous voulez atteindre votre objectif chiffré, n'est-ce pas ? Alors il faut mettre tout en haut, fièrement, la formule que vous voulez le plus vendre, celle avec l'offre à volonté. »

### 5-4. Pas d'image sous la main ? Laissons l'IA la dessiner aussi

J'ai pris ma décision. « Plutôt que de faire le cool et de voir mes ventes baisser, autant tout tenter, quoi qu'il en coûte. »

Mais un problème s'est alors posé.

« Même si je le mets en grand en haut, le texte seul est faible… »

Et si je prends sur un site d'images libres de droits une photo de gens qui trinquent à la bière, cela a tout de suite l'air d'un restaurant de chaîne. Cela ne convient pas à l'ambiance de mon bar.

Je n'ai aucun talent pour le dessin, et engager un illustrateur coûte du temps et de l'argent.

J'ai commencé à m'inquiéter, « que faire… ? », mais l'idée m'est aussitôt revenue :

« C'est vrai, j'ai un adjoint (l'IA) qui sait dessiner. »

J'avais trouvé sur un site de ressources libres une image proche de ce que je voulais. Il était indiqué que la modification était autorisée.

J'ai ensuite tapé ceci dans la zone de discussion :

> « Dessine une illustration à placer en haut du menu. Prends l'image jointe comme base.
>
> Je veux l'impression de gens qui trinquent joyeusement, mais sans faire bon marché.
>
> Fais-le dans un style simple, au trait. »

Quelques secondes plus tard, quatre propositions d'illustration sont apparues à l'écran.

Parmi elles, j'ai choisi l'illustration « Santé ! » simple et chaleureuse qui correspondait le mieux à l'ambiance du bar.

![L'illustration « Santé ! » générée par l'IA en seulement 10 secondes](images/fig-22.png)

Cela n'a pris que 10 secondes.

Pas seulement l'analyse : les « éléments visuels » nécessaires à l'amélioration peuvent être obtenus sur-le-champ.

C'est la vraie force d'intégrer l'IA générative à la gestion.

### 5-5. Rien qu'en changeant la mise en page, le ticket moyen a augmenté d'environ 40 %

J'ai donc refait le menu.

#### Avant : le menu tel qu'il était

- Meilleure place (tout en haut) : des articles à petit prix comme « Set ¥2200 (environ $15) » et « Menu dégustation ¥3300 (environ $22) ».

- À volonté : indiqué en texte seulement, dans le coin inférieur gauche, comme « À volonté à partir de ¥3000 (environ $20) ». Il était complètement noyé.

#### Après : le menu révisé

- Meilleure place (tout en haut) : des formules à prix élevé de ¥4500–¥5700 (environ $30–$38), présentées comme « Notre coup de cœur ! Menu Plaisir Complet (avec à volonté) ».

- Design : avec l'illustration « Santé ! » générée par l'IA, il guide fortement le regard, visuellement, vers « Regardez ici d'abord ».

- Changement de mise en page : les sets bon marché qui étaient les vedettes ont été déplacés plus bas.

![Le menu Après. Le menu à volonté est placé tout en haut](images/fig-23.png)

La nourriture, les prix et la qualité des boissons sont en fait presque inchangés. Tout ce que j'ai changé, c'est « la façon de présenter » et « l'endroit ».

Et le résultat ?

Dès le lendemain, le comportement de commande de la clientèle a changé de façon spectaculaire.

Les premiers mots des clients qui ouvraient le menu n'étaient plus « Une bière pour commencer », mais « Alors on prend ce “Menu Coup de cœur (¥4900 (environ $33))” avec l'illustration ».

La clientèle qui terminait auparavant avec « le Set (¥2200 (environ $15)) plus deux boissons » (une dépense d'environ ¥3500 (environ $23) par client) choisissait désormais dès le départ le menu à ¥4900 (environ $33).

Rien qu'avec cela, le ticket moyen a bondi de ¥1400 (environ $9,3).

De plus, la clientèle y gagnait aussi de « pouvoir boire sans se soucier de l'addition », si bien que la satisfaction a augmenté au lieu de baisser.

### 5-6. Évaluer les résultats avec le PDF des ventes de décembre (PDCA)

Un mois s'était écoulé depuis la mise en œuvre de la mesure.

Ne pas s'arrêter là, c'est l'essence de l'usage de l'IA.

Beaucoup de propriétaires jugent les résultats au ressenti et en restent là : « Il y a eu du monde, donc ça a dû marcher » ou « Les ventes ont augmenté, c'est bien ».

Mais j'ai de nouveau fait appel à Gemini.

Cette fois, j'ai téléversé le « PDF des données de ventes de décembre », où les résultats étaient là, et j'ai posé cette question :

> « Les résultats de la mesure du mois dernier (le changement de menu) sont arrivés.
>
> Regarde ces données de ventes de décembre et évalue les résultats : le nombre de commandes du “Menu Coup de cœur” a-t-il augmenté comme prévu, et quel effet cela a-t-il eu sur le ticket moyen ? »

Gemini a analysé les données instantanément et m'a renvoyé un rapport.

![L'écran du rapport d'analyse des ventes de Gemini : j'ai fait un résumé pour la publication, donc le contenu diffère en partie du texte ci-dessous](images/fig-24.png)

L'analyse de Gemini :

> « Ce sont d'excellents résultats. D'après la tendance des données, le nombre de commandes du “Menu Plaisir Complet” est passé à environ 1,8 fois celui du mois précédent.
>
> En conséquence, le ticket moyen global a augmenté de ○○ yens.
>
> Le facteur principal est que placer la formule à volonté plus haut a fait monter la valeur des commandes, en particulier pour les groupes. »

En entendant ces mots, j'ai ressenti pour la première fois un vrai soulagement.

Pas « on a gagné de l'argent on ne sait trop comment », mais la confiance de « j'ai visé, et j'ai fait mon chiffre ».

Cela devient la force motrice de la mesure suivante.

1.  Plan : regarder les données de ventes et le menu, et trouver le problème (la formule à volonté est cachée).

2.  Do : faire dessiner une illustration par l'IA et changer la mise en page du menu.

3.  Check : lui faire lire le PDF des ventes de décembre et vérifier les résultats.

4.  Act : réfléchir ensuite à revoir la mise en page de la carte des plats.

Le « cycle PDCA » que les grandes entreprises font tourner à grands frais peut être mené par un commerce indépendant comme le mien, avec seulement un smartphone, si j'ai l'IA comme partenaire.

## Chapitre 6 : Défis – Développer un système rien que pour mon bar

~ « Si ça n'existe pas, construisez-le. » Un projet de développement de système sans expert ~

※Pour information, vous n'avez pas besoin de tout faire dans ce livre.

・Envoyer une image et faire écrire un texte à l'IA\
・Transformer un long message LINE en schéma

Ces deux-là suffisent pour commencer. Rien que cela vous facilitera assurément le travail.\
Il suffit aussi de lire ceci comme une simple lecture et de vous dire : « On peut aller jusque-là avec l'IA. »

### 6-1. Les applis toutes faites ne répondent pas à mes besoins précis

Jusqu'ici, j'ai parlé de l'usage de l'IA sur des plateformes existantes, comme la génération d'images et l'analyse du menu.

Mais en continuant à exploiter un commerce, des soucis surgissent que les « applis toutes faites » ne peuvent tout simplement pas résoudre.

En particulier, pour un modèle d'activité irrégulier comme le nôtre, « curry le jour, bar le soir », les flux d'argent entrants et sortants sont aussi compliqués.

« Je veux rapprocher le solde de mon compte PayPay Bank des paiements à venir et connaître le solde prévisionnel de fin de mois. »

« Les dates de paiement sont réparties entre le 10 et le 25. Je veux simuler cela. »

Les logiciels de comptabilité existants sont très performants, mais aucun ne visait précisément « le souci que j'avais en tête à ce moment-là ».

J'ai donc pris ma décision.

« Si ça n'existe pas, je le construis. J'ai Gemini, le meilleur ingénieur. »

### 6-2. Phases 1 à 3 : des notes griffonnées au « cloud »

Le développement a commencé en montrant à Gemini mes notes dans Google Keep.

![La note Keep qui a été le point de départ du développement](images/fig-25.png)

#### Phase 1 : construire la logique

« Je veux automatiser les calculs de cette note. »

En réponse à ma demande, Gemini a rapidement mis au point la logique de calcul.

- Quand je change le montant d'un poste, il calcule instantanément le solde final.

- Si les fonds risquent de manquer, il affiche un « avertissement » en rouge.

- Il simule le calendrier des paiements répartis entre « le 10 » et « le 25 / fin de mois ».

- Les données sont enregistrées dans le navigateur (cache).

C'était déjà très pratique en soi, mais j'ai voulu aller plus loin. « Je veux que les données restent même quand je ferme le navigateur. Je veux aussi pouvoir les consulter sur mon téléphone. »

#### Phase 2 : adopter un outil inconnu, « Firebase »

Je pensais faire un lien avec un tableur, mais la suggestion de Gemini m'a pris au dépourvu.

« Si l'on pense à la performance en temps réel et à l'efficacité, utilisons “Firebase” de Google. L'offre gratuite suffit pour le faire tourner. »

« Firebase… ? » Je n'avais jamais entendu ce mot. Mais avec l'instinct de mes années de coordination de systèmes, j'ai décidé : « Si l'IA le recommande avec autant de force, allons-y. »

Résultat : grâce à une base de données appelée Firestore, les données ont fini par être stockées en sécurité dans le cloud.

#### Phase 3 : connexion Google et système d'approbation

Il s'agit d'argent, donc il ne faut pas que n'importe qui puisse le voir.

Au début, j'ai pensé à quelque chose comme une « phrase de passe », mais Gemini a suggéré : « Si vous voulez une sécurité plus solide, utilisons la connexion Google. »

Puis, quand j'ai dit : « Je veux que seul le personnel que j'approuve puisse le voir », il a même construit « un système où un administrateur peut approuver et retirer des membres à l'écran ».

### 6-3. Phases 4 et 5 : s'attaquer à l'écran noir (le terminal)

À partir de là est venu le passage le plus décisif du vibe coding : publier l'appli sur internet (le déploiement).

#### Avertissement : à partir d'ici, c'est le cours « ceinture noire »

Les prochaines pages sont la partie « pratique » la plus difficile de ce livre. Vous allez manipuler un « écran noir (terminal) » comme ceux des hackers dans les films.

Parlons franchement. Vous rencontrerez inévitablement des erreurs ici. Moi aussi. Vous vous heurterez à des murs comme une « erreur d'autorisation PowerShell » qui se lit comme une formule magique. Mais n'ayez pas peur. Ce que vous faites ici reste pareil : « prendre une capture d'écran de l'erreur et la lancer à l'IA ».

La vérité que j'ai apprise à l'époque où je travaillais dans les systèmes est la suivante : « Même les professionnels font des erreurs. La seule différence tient à ce que l'on renonce quand l'une apparaît, ou que l'on cherche (demande) de l'aide. » Si cela vous semble trop difficile, sautez cette section et retenez seulement la possibilité : « On peut faire même cela avec l'IA. »

Gemini a dit :

« Nous allons installer l'environnement de développement sur votre PC Windows. Installez “Node.js” et tapez les commandes suivantes dans “VS Code”. »

J'ai ouvert l'écran noir (le terminal) comme indiqué, et j'ai immédiatement obtenu une erreur.

« Exécution impossible à cause des restrictions de sécurité de PowerShell. »

Un propriétaire ordinaire aurait perdu courage ici.

Mais j'ai copié-collé le message d'erreur et je l'ai lancé à l'IA.

L'IA a répondu aussitôt : « Levez la restriction avec une commande appelée “Set-ExecutionPolicy”. »

Sans comprendre ce que cela voulait dire, j'ai tapé la commande, puis npm run build, firebase deploy…

Chaque fois que je tapais ces caractères dignes de formules magiques, du texte défilait à l'écran et le processus avançait.

Et enfin, mon appli est apparue sur le web.

#### Phase 5 : en faire une appli pour smartphone (PWA)

L'appli publiée était d'abord « à nu », avec une mise en page complètement brute, mais cela aussi a été résolu en ajoutant un réglage appelé « Tailwind CSS ».

Ensuite, quand j'ai demandé : « Je veux mettre une icône sur l'écran d'accueil de mon téléphone et l'utiliser comme une appli », il m'a appris les réglages pour en faire une « PWA (Progressive Web App) ».

Et ainsi, une appli dédiée que j'avais faite (sans écrire une seule ligne de code) est née dans mon téléphone.

![L'écran de l'appli de gestion de trésorerie terminée](images/fig-26.png)

### 6-4. Phase 6 : le problème après 30 jours, et la solution

Environ un mois après avoir commencé à l'utiliser, un problème est survenu.

« Ça marchait encore hier, et soudain je ne peux plus y accéder ! »

J'ai paniqué et consulté Gemini, et la cause se trouvait à un endroit inattendu.

« Les réglages de la base de données (Firestore) étaient restés en “mode test (limité à 30 jours)”. Ce mode est arrivé à expiration. »

Pour épargner la peine de la configuration au début du développement, l'IA avait délibérément défini une règle avec une date d'expiration.

« Réécrivons les règles de sécurité pour que “tout utilisateur connecté puisse continuer à l'utiliser”. »

Quand j'ai réécrit quelques lignes du fichier de réglages comme l'IA me l'indiquait, l'appli s'est remise à fonctionner sans problème.

Ce problème aussi a été une bonne expérience pour moi.

J'ai appris qu'« un système est une chose vivante et demande de la maintenance ».

Et j'ai gagné l'assurance que « même si un problème survient, il y a toujours une réponse si je demande à l'IA ».

### 6-5. Étude de cas 2 : le « projet de reconnaissance faciale » né d'une vidéo de démonstration sur X (anciennement Twitter)

Voici un autre développement de système que j'ai entrepris, et le plus gros.

C'est « un système qui reconnaît par une caméra les clients qui entrent, et qui me dit discrètement leur nom, leurs données et leurs préférences ».

Tout a commencé sur le réseau social X, que je faisais défiler sans y penser.

Une vidéo de démonstration publiée par un ingénieur est passée dans mon fil : elle utilisait l'IA intégrée à Google Chrome (Built-in AI) pour expliquer en temps réel ce que voyait une webcam.

Mon instinct issu de l'informatique s'est mis en marche.

« C'est du “multimodal”. Et si c'est intégré au navigateur, cela ne pourrait-il pas tourner entièrement sur mon propre PC, sans payer le cloud ? »

Si cela fonctionnait, je pourrais peut-être construire un système d'accueil rien que pour mon bar, sans installer de système coûteux.

J'ai copié l'URL et je l'ai lancée à Gemini.

« Je veux faire la même chose que ça. Dis-moi comment le mettre en œuvre. »

#### Phase 1 : ça marchait, mais je ne pouvais pas savoir « qui »

J'ai changé les réglages (flags) de Chrome comme Gemini l'indiquait et collé le code, et le même système que dans la démonstration a tourné sans problème.

Quand j'apparaissais à la caméra, l'écran affichait ceci :

« Un homme portant des lunettes est assis devant un PC. »

Ce système utilise une IA intégrée au navigateur, appelée Gemini Nano. Son avantage est de fonctionner entièrement dans le navigateur sans se connecter au cloud, mais elle ne reconnaît que des choses générales comme « lunettes » et « homme ». Elle ne peut pas aller jusqu'à déterminer qui est la personne.

C'est une technologie étonnante. Mais en tant que personne qui tient un restaurant, la déception est venue aussitôt.

« Ça ne va pas. »

Ce que je veux savoir, ce n'est pas une caractéristique générale comme « une personne à lunettes », mais l'identification de l'individu : « Est-ce A ou B ? »

#### Phase 2 : le mur de l'intégration à Google Photos, et la réponse de l'IA

J'ai donc soumis une idée naïve à Gemini.

« Connecte ce système à mon Google Photos. Il contient des données de regroupement de visages pour mes amis et mes habitués, donc si tu fais la comparaison avec elles, tu peux obtenir les noms, non ? »

La réponse de Gemini a été froide, mais juste.

« Désolé, mais ce n'est pas possible. Les données de reconnaissance faciale de Google Photos sont des informations privées très sensibles et, pour des raisons de sécurité, les programmes extérieurs n'ont pas le droit de les utiliser. »

Logique. La route semblait s'arrêter là.

Mais c'est là qu'est venue la vraie essence du « vibe coding (développement par le dialogue) ». L'IA ne s'est pas contentée de refuser.

#### Phase 3 : une alternative et un virage

Gemini a ensuite suggéré ceci :

« Nous ne pouvons pas utiliser Google Photos, mais il est possible de construire votre propre système de reconnaissance faciale dans un environnement local avec des bibliothèques open source (comme OpenCV ou face_recognition). On essaie ? »

J'ai répondu « Oui » immédiatement.

À partir de là, le plan de développement a complètement changé. Au lieu d'utiliser les fonctions de Chrome, je construirais un système de reconnaissance faciale de zéro avec un langage de programmation appelé Python.

#### Phase 4 : se battre avec l'écran noir et se connecter à un tableur

Ce que j'avais à faire n'a pas changé. J'ai demandé à Gemini « comment installer les bibliothèques nécessaires » et collé la réponse dans l'écran noir (l'invite de commandes).

Quand une erreur apparaissait, je renvoyais le texte rouge tel quel à Gemini.

Quelques heures plus tard, le système était enfin terminé.

1.  La webcam capture mon visage.

2.  Il compare avec les « données de photos de visages » d'un dossier du PC.

3.  Quand il trouve une correspondance, il consulte la liste des clients dans un tableur Google.

4.  L'écran affiche « Bonta : reste de la bouteille carrée ○○ g ».

![Le système de reconnaissance faciale en fonctionnement. Il reconnaît le visage de la personne qui tient le commerce et affiche des informations. L'image capturée a été floutée en mosaïque avec Gemini](images/fig-27.png)

Coût de sous-traitance : ¥0 (environ $0,00). Mon propre travail de codage : zéro.

C'est le moment où un « système CRM de reconnaissance faciale » unique en son genre est né dans un coin de Higashi-Nakano.

#### Phase 5 : puis je prends conscience de la « responsabilité de protéger »

Le système était terminé. Mais avec la joie, j'ai senti un frisson me parcourir l'échine.

« Attendez un instant. En ce moment, cet ordinateur détient les données de visage (informations biométriques) des clients, non… ? »

Jusque-là, je pensais : « Tant que ça marche, ça va. » Mais une fois en exploitation réelle, c'est une autre histoire.

Et si cet ordinateur était infecté par un virus ? Les données de visage des clients et leurs informations de préférences (données personnelles) pourraient fuiter ensemble.

Un PC autonome non relié à internet serait sûr, mais tant que je gère les réservations et les réseaux sociaux, une connexion internet est indispensable.

« Pouvoir construire un outil utile » et « pouvoir le gérer en sécurité » sont deux choses distinctes.

C'est ici que j'ai vraiment ressenti pour la première fois l'importance de l'« assurance cyber-risques » dont m'avait parlé auparavant la personne de l'assurance venue me faire sa présentation.

J'en avais ri : « Un petit commerce comme le nôtre ne subira pas de cyberattaques », mais maintenant que l'IA nous permet de construire des systèmes avancés, nous aussi, propriétaires individuels, assumons la responsabilité d'être de véritables « gestionnaires de données ».

Avec l'IA, on peut obtenir des outils magiques.

Mais j'ai appris que porter le « bâton de magicien (la culture numérique) » et le « bouclier (les mesures de sécurité) » pour user de cette magie fait désormais aussi partie du travail des propriétaires.

### 6-6. La « responsabilité » et l'« assurance » qui accompagnent la liberté

#### Important : vie privée et données personnelles

Ce « système de reconnaissance faciale » est un prototype expérimental que j'ai construit pour tester ce qui est techniquement possible. Si vous l'utilisiez dans un vrai commerce, les données de visage de votre clientèle compteraient comme des « données personnelles (données biométriques) » et devraient être strictement protégées par la loi (la loi sur la protection des informations personnelles).

Si vous pensez adopter quelque chose de ce genre, retenez sans faute ces deux points.

Informer la clientèle et obtenir son consentement : il vous faut une procédure, comme afficher à l'entrée un panneau « Nous utilisons la reconnaissance faciale par IA » et recueillir le consentement lors de l'inscription comme membre. Filmer en cachette est absolument interdit.

Protéger les données : il vous faut des mesures qui ramènent le risque de fuite à zéro, comme gérer les données dans un environnement coupé d'internet.

Être capable de construire quelque chose ne veut pas dire avoir le droit de le faire. Si vous avez des compétences techniques, souvenez-vous que la responsabilité d'employer cette technologie va avec.

Jusqu'ici, j'ai parlé de la merveille que peut être un système fait maison. Mais en tant que personne qui dirige un commerce, je dois aussi vous parler d'une dure réalité.

La voici : « Tout ce que vous construisez vous-même relève de votre propre responsabilité. »

Avec un service par abonnement mensuel (SaaS), si le serveur tombe, l'entreprise présente ses excuses et le remet en marche.

Mais un système construit avec le vibe coding n'a pas de « support client ».

Si votre appli cesse soudain de fonctionner au pic du déjeuner, personne ne viendra vous aider.

Quand Google change une spécification, il est courant qu'un code qui marchait très bien hier produise des erreurs aujourd'hui.

C'est pourquoi je fais deux préparatifs.

Le premier est une « solution de secours analogique ».

« Si la reconnaissance faciale s'arrête, regarder le registre papier des clients. » « Si l'appli de caisse tombe, utiliser une calculatrice et des notes manuscrites. »

Les outils numériques ne sont que des « outils pratiques ». Il ne faut pas en dépendre au point que, lorsqu'ils s'arrêtent, votre commerce s'arrête aussi.

Le second est l'« assurance » dont j'ai parlé plus haut.

L'assurance responsabilité cyber couvre non seulement le risque de fuite d'informations, mais aussi l'indemnisation de la perte d'activité quand une erreur de votre part arrête le système. Pour des propriétaires qui s'arment avec l'informatique, elle relève du savoir-vivre.

« Il arrivera que les choses s'arrêtent. Il m'arrivera de faire des erreurs. »

Prenez cela comme acquis, acceptez le risque et prenez des mesures contre lui.

C'est seulement avec cette détermination que nous pouvons vraiment utiliser un « système libre » qui ne dépend de personne.

### 6-7. Pas besoin d'expert. Il faut de la persévérance

Je n'ai pas payé un seul yen de frais de sous-traitance pour le développement de ces deux systèmes.

Tout ce que j'ai employé, c'est un abonnement d'IA de quelques milliers de yens par mois, et la persévérance de quelqu'un qui, à la tête de son commerce, pensait : « Je dois absolument me débarrasser de ce souci (de trésorerie) » et « Je veux rendre ma clientèle heureuse ».

Il ne s'agit pas de dire « je ne peux pas, parce que je ne sais pas programmer ».

Si vous avez quelque chose que vous voulez construire (le Want), l'IA vous apprendra comment le construire (le How).

Même quand des mots que vous ne comprenez pas apparaissent (Node.js, PowerShell, Firestore…), il n'y a rien à craindre.

Nous avons le meilleur partenaire qui soit, « Gemini », pour les traduire et nous guider.

#### Encadré 4 : quelle différence entre Excel et une base de données (Firestore) ?

~ Est-ce un « mémo à lire par vous » ou un « registre à lire par le système » ? ~

Firebase (Firestore) est apparu dans le développement de l'appli de trésorerie. Vous vous êtes peut-être demandé pourquoi Excel ne ferait pas l'affaire.

Un tableur (Excel) est un « carnet que les gens regardent et dans lequel ils tapent ». Il est très souple, mais pour un système, il est flou sur « ce qui se trouve où ».

Une base de données (Firestore), en revanche, est un « casier bien rangé conçu pour le système ». Comme il est fixé que « la date va dans la case 1 et le montant dans la case 2 », un programme peut la traiter instantanément. Elle ne plante pas non plus quand plusieurs personnes y accèdent en même temps.

« Si vous construisez une appli, utilisez une base de données, pas Excel. » Rien que le savoir élèvera le niveau de vos instructions à l'IA.

## Postface : une « recette de l'avenir » qui n'appartient qu'à votre commerce

~ L'IA n'est pas une technologie difficile. C'est un nouveau partenaire de « conversation » ~

Merci d'avoir lu ce livre jusqu'au bout.

Si vous n'essayez qu'une seule chose de ce livre, essayez ceci : « Collez ce message LINE fastidieux directement dans l'IA et demandez-lui de le “transformer en schéma”. »

Mon expertise en IA n'a rien d'exceptionnel. J'ai simplement répété chaque jour la pratique de « parler à l'IA avec les mots du terrain », \
sur le champ de bataille d'un restaurant.

C'est pourquoi je pense qu'il suffit que vous reteniez de ce livre non pas une « collection de bonnes réponses », mais seulement une « façon de penser ».

Quand vous avez ouvert la première page, quelle image aviez-vous des mots « utiliser l'IA » ?

« Ça a l'air difficile. » « Il faut des connaissances en programmation, non ? » « Cela n'a rien à voir avec un petit commerce comme le mien. »

Vous avez peut-être pensé quelque chose de ce genre.

Mais maintenant que vous avez lu jusqu'ici ce récit de mes « essais et erreurs », peut-être cette image a-t-elle un peu changé.

Ce que j'ai fait, ce n'était pas exploiter à fond une technologie informatique avancée.

J'ai râlé : « Je ne peux pas faire ça à la main. » J'ai protesté : « C'est difficile à utiliser. » Et j'ai fait des caprices en disant : « Je voudrais que ça marche plutôt comme ceci. »

Aujourd'hui, dans le monde des ingénieurs, le terme « vibe coding » est à la mode.

C'est une méthode pour construire un système à l'instinct, en discutant avec l'IA.

Tout comme un joueur de shogi discute avec l'IA pour anticiper les coups suivants, nous aussi pouvons discuter avec l'IA et construire l'« avenir de nos commerces ».

Comme lorsqu'on dit à l'équipe de cuisine : « Rajoute un peu de sel. »

Comme demander au poissonnier du marché : « Vous avez du bon poisson aujourd'hui ? »

Parler à l'IA et dire : « Rends ce travail plus facile. » C'est là que tout commence.

J'ai travaillé autrefois dans le service informatique d'une entreprise, à coordonner le « terrain » et les « développeurs ».

Je fais maintenant la même chose entre « mon propre commerce » et l'« IA ».

Et j'en suis convaincu :

« Un propriétaire qui connaît les réalités du terrain peut devenir le meilleur chef d'orchestre de l'IA. »

Commencez aujourd'hui, vous aussi.

D'abord, sortez votre téléphone et parlez à Gemini.

« Dis-moi, par où commencer la préparation d'aujourd'hui ? »

« Comment faire pour que ce plat se vende mieux ? »

« Cette paperasse est pénible. Tu peux faire quelque chose ? »

Ne vous inquiétez pas si une erreur apparaît. C'est le signe que la « conversation » a commencé.

Prenez simplement une capture d'écran et renvoyez-la avec « il y a quelque chose qui cloche ».

Au bout de ces conversations accumulées, vous attendent du « temps » et de la « sérénité » que vous n'auriez jamais imaginés, et « un avenir qui n'appartient qu'à votre commerce ».

Alors, engageons aussi pour votre commerce un « adjoint » fiable.

Car la recette de l'avenir naîtra de la conversation entre vous et l'IA.

### Les trois prolongements de ce livre

Ce livre se lit gratuitement en PDF, sur note et sur Google Play. (Sur Kindle seulement, les règles de la boutique imposent un prix minimum.) En échange, j'ai préparé trois endroits où aller une fois la lecture terminée. Si vous en utilisez ne serait-ce qu'un, écrire ce livre aura valu la peine.

1. Essayez dans votre propre commerce. La série Agenda peut se commencer avec un carnet gratuit. https://bontallc.com/agenda?via=b1-fr-{{FMT}}
2. Suivez ce que je fais. J'écris sur les outils que je construirai ensuite, et sur le quotidien du bar, sur note et X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Si vous passez un jour à Tokyo, venez à Tamuro. À une minute de la sortie est de la gare de Higashi-Nakano. Vous pouvez entrer sans réservation. Site de réservation https://tamuroreservation.vercel.app/?src=b1-fr-{{FMT}}

Aux personnes qui viennent grâce à ce livre : lorsque vous réservez, saisissez le code promo « BOOK ». Je vous offrirai une boisson lors de votre première visite. Sans réservation, dites simplement « Je viens de la part du livre » en passant votre première commande. Je vous offrirai la même boisson. C'est un petit dispositif pour que je puisse compter combien de personnes sont venues grâce au livre.

### À propos de l'auteur

Raku Bonta

Propriétaire exploitant seul un restaurant de 11 places au comptoir et 8 places dans la salle à tatamis à Higashi-Nakano, à Tokyo.

Le jour, c'est un restaurant de curry au steak haché japonais (hambāgu) parfumé d'épices. Le soir, c'est un bar-restaurant qui sert un menu fixe différent chaque soir.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Épices, curry au steak haché](images/fig-28.png)

▼ Bar « Tamuro »

https://www.instagram.com/tamuro.higashinakano/

![Bar « Tamuro »](images/fig-29.png)

Le commerce s'investit aussi dans la création d'une communauté autour de la cuisine, avec des soirées vin toutes les deux semaines, un cours de cuisine mensuel et des dîners de plusieurs plats.

Avant d'ouvrir son propre commerce il y a 12 ans, Raku Bonta travaillait dans une entreprise en « planification de systèmes » et « architecture de solutions ».

Les intitulés semblent difficiles, mais le vrai travail était celui d'« une personne de coordination qui transmet avec exactitude aux prestataires informatiques le souhait du terrain, “nous voulons faire ceci”, et le fait construire ». Pas un travail d'ingénierie en programmation avancée : un parcours de « traduction » qui relie les personnes et la technologie.

Aujourd'hui, riche de cette expérience, Raku Bonta utilise l'IA générative comme Google Gemini pour gérer son propre commerce, en pratiquant et en partageant une « réforme de l'activité qui fonctionne même sans aucune connaissance spécialisée ».
