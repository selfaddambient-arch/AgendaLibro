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

