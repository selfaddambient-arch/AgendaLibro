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

