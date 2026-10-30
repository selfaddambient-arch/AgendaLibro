### 1-5 Les chiffres : environ 88 % des réservations sont pour le jour même

À mesure que j'ajoutais des mécanismes, j'ai remarqué quelque chose. Je ne savais pas lesquels fonctionnaient.

J'ai donc compté les données de réservation. Sur les 244 réservations des 90 derniers jours, 215 étaient des réservations du jour même. Cela fait 88,1 %. La moyenne est de 2,71 réservations par jour.

Tamuro n'était pas un endroit où l'on vient sur réservation, mais un endroit où l'on vient sur un coup de tête. Cela n'est devenu clair qu'une fois mis en chiffres.

Ces chiffres ont fait apparaître deux choses.

La première concerne la construction du formulaire de réservation. Si la plupart des réservations sont pour le jour même, il est plus pratique que le prochain créneau libre d'aujourd'hui soit déjà sélectionné à l'ouverture de l'écran de réservation. En revanche, certaines personnes qui veulent réserver à une date ultérieure l'enverront par étourderie pour aujourd'hui. J'ai donc mis aujourd'hui en évidence dans le calendrier, et sur l'écran de confirmation j'affiche la date et l'heure en grand avec « Aujourd'hui ». J'ai gardé la commodité de choisir le jour même, et j'ai fait en sorte que les erreurs se remarquent facilement.

La seconde est le sens de la remise pour réservation anticipée. Beaucoup de réservations le jour même signifie que nous ne pouvons pas anticiper les ventes à venir. Le mauvais temps suffit à faire baisser la fréquentation. Pour augmenter, même un peu, les réservations à l'avance, il faut que davantage de personnes utilisent la remise pour réservation anticipée. Cette prise de conscience a conduit plus tard à l'histoire de la construction d'une IA qui publie à la place de la direction.

Pour suivre les chiffres, il faut un système pour compter. Le site de réservation n'avait aucune analyse de fréquentation. Je ne pouvais pas savoir combien de personnes arrivaient sur la page de réservation, combien abandonnaient en route et combien allaient au bout. J'ai donc ajouté un système qui compte trois étapes : arrivée sur la page, choix des détails, réservation terminée. Il n'enregistre pas qui est venu, seulement l'étape et l'heure.

Plus tard encore, j'ai aussi construit un système qui envoie par e-mail un rapport hebdomadaire résumant les chiffres de réservation. Je décrirai comment cela s'est fait en 1-7.

【Figure 1-3a】Aujourd'hui est mis en évidence dans le calendrier *(L'écran est en japonais.)*

【Figure 1-3b】Sur l'écran de confirmation, la date et l'heure apparaissent en grand avec « Aujourd'hui » *(L'écran est en japonais.)*

### 1-6 Trop de formules parmi lesquelles choisir

Une fois le système de remises en place, j'ai voulu ensuite augmenter les créneaux et les formules qui se vendent.

Le créneau de 18h ne se remplissait pas, j'ai donc créé un happy hour jusqu'à 19h. Pour les personnes qui viennent après avoir mangé, j'ai créé une formule boissons seules, sans repas. Le menu à prix fixe et le cours de cuisine, autrefois mensuels, sont devenus des événements à la demande qui ouvrent quand quelqu'un s'inscrit, pris en charge par le site de réservation. Pour vendre le temps avant l'ouverture le week-end, à partir de 15h30, j'ai créé une formule fête pour les groupes de six personnes ou plus.

Chacune a sa raison. Prenons la formule fête : si je la faisais paraître comme une bonne affaire sur le prix, elle attirerait seulement la clientèle qui choisissait la formule standard, et les ventes baisseraient. J'ai donc placé la différenciation non pas sur le prix mais sur les heures d'avant l'ouverture, qui n'avaient jamais rapporté aucune vente. La remise du happy hour ne rapporte aucun profit si elle est cumulée avec d'autres remises ; j'ai donc décidé qu'elle ne se cumule pas.

Et ainsi les formules se sont multipliées. Standard, Premium, Enchanté, Bon retour parmi nous, Happy Hour, Boissons seules, Menu à prix fixe, Cours de cuisine, Fête. Chacune a des conditions sur le nombre de personnes, certaines acceptent les remises et d'autres non, et il y a des restrictions horaires.

Un jour, j'ai ouvert le formulaire de réservation et j'ai réalisé : dans ces conditions, la clientèle ne peut pas s'y retrouver.

Moi qui l'ai construit, je comprends chaque différence. Mais une personne qui ouvre le site de réservation pour la première fois pourrait-elle comparer neuf formules et leurs conditions de remise, puis choisir celle qui lui convient ? Si elle n'y arrive pas, elle abandonne en cours de réservation. Les formules que j'avais pris soin d'ajouter pouvaient finir par réduire les réservations.

J'aurais pu faire le tri. Mais chaque formule correspond à un moment que je veux vendre et à une clientèle que je veux accueillir. Je ne voulais en supprimer aucune.

J'ai donc pensé à un système où la clientèle consulte l'IA et décide d'une formule. On lui indique le nombre de personnes, la date et l'heure souhaitées et la façon dont on veut profiter de sa venue : l'IA indique la formule et le prix qui conviennent et conduit directement à la réservation. L'établissement prend en charge la complexité des formules. Il ne reste à la clientèle qu'une conversation.

Ce système est le « T-AI-MURO » dont je parle en 1-8. Avant cela, il y a encore une chose que j'ai remarquée durant cette période.

【Figure 1-2】Choix de la formule dans le formulaire de réservation. Voici tous les onglets alignés *(L'écran est en japonais.)*

### 1-7 « Est-ce que cela fait vraiment venir des clients ? »

Le jour où j'ai ajouté la formule fête, j'ai passé la journée entière à apporter amélioration sur amélioration au site de réservation. J'ai resserré l'en-tête, harmonisé le design des e-mails, et remplacé l'IA qui crée des sujets de conversation pour la clientèle dans l'établissement.

Le soir, une question m'est venue soudain.

« Est-ce que cela aide vraiment à faire venir plus de clients ? »

Quand je l'ai demandé à l'IA, elle a trié honnêtement les améliorations de ce jour-là.

| Catégorie | Améliorations de ce jour-là |
| --- | --- |
| Ce qui peut créer de nouvelles réservations | Formule fête, créneau de 15h30 les week-ends et jours fériés |
| Ce qui augmente le taux d'achèvement pour les visiteurs du site | Resserrement de l'en-tête, alignement des onglets |
| Ce qui encourage les retours | Uniformisation du design des e-mails |
| Ce qui n'aide pas à faire venir de la clientèle | Changement de l'IA qui crée des sujets de conversation, lien vers l'étape suivante, présentation d'Agenda |

Parmi les améliorations de ce jour-là, seules la formule fête et le créneau de 15h30 menaient directement à faire venir de la clientèle. Les autres visaient à ne pas perdre les visiteurs déjà arrivés sur le site. Elles comptent aussi, mais elles n'augmentent pas la clientèle.

Il y avait un problème plus grand. Pour aucune des améliorations je n'avais de moyen de mesurer si elle avait marché. Aucun chiffre ne reliait « j'ai amélioré » et « la clientèle a augmenté ».

Ma réponse a tenu en quelques mots : « Construisons-en un. »

J'ai donc commencé à créer un rapport hebdomadaire d'acquisition de clientèle. Le nombre de réservations, le nombre de convives, le montant total, les annulations. Les répartitions par jour de la semaine et par moment de la journée. La proportion de nouveaux clients et de clients qui reviennent. Les chiffres des formules fête et du créneau de 15h30. La provenance des réservations (le formulaire de réservation, la fenêtre de discussion, les réservations venant de l'IA, les saisies manuelles de l'établissement). Le nombre de clics dans les e-mails et le nombre de réservations dans les sept jours suivant ces clics.

Dès qu'il y a des chiffres, la dimension du temps s'impose. Le même jour, j'avais trouvé une autre lacune. J'avais défini le cours de cuisine et le créneau de 15h30 de la formule fête comme valables « le week-end », mais en me demandant « Que se passe-t-il les jours fériés ? » et en cherchant, j'ai constaté que le système de réservation n'avait aucune notion de jour férié. Un lundi férié, l'établissement est ouvert, et pourtant le créneau de 15h30 n'apparaissait pas. Je lui ai donné une liste des jours fériés et je l'ai corrigé pour les traiter comme des week-ends. C'était une lacune que seule la personne qui avait construit le système pouvait remarquer.

Avant de construire le rapport, j'ai d'abord comblé les lacunes liées au temps.

Même les habitués qui venaient avant que j'utilise le système de réservation apparaissent comme « nouveaux clients » dans les enregistrements. Dans le rapport, j'écris donc « première visite enregistrée » et j'y joins toujours la date de début des enregistrements. Pour juger si une amélioration a marché, il faut le tableau d'avant. Pour le premier rapport, j'ai fait le décompte sur les huit semaines précédentes et je l'ai pris comme base de référence. Une semaine où l'établissement ferme temporairement, pour un voyage ou autre chose, les réservations baissent naturellement. J'indique donc aussi le nombre de jours d'ouverture, afin de pouvoir comparer par jour d'ouverture.

La section « Changements notables », j'ai cessé de la faire écrire par l'IA, et je la fais produire par des calculs fixes et des phrases fixes. C'est pour que le coût hebdomadaire reste à zéro. Les noms et coordonnées des clients n'apparaissent pas dans le rapport ; seuls des nombres et des proportions y figurent.

Une fois construit un moyen de mesurer, ma façon de construire les améliorations a elle-même changé. J'ai commencé à définir conjointement, dès le départ, l'amélioration et la méthode pour en mesurer l'effet. La mesure n'est pas quelque chose à penser après une amélioration ; elle va dans le même document d'instructions que l'amélioration. Voilà ce que j'ai appris ce jour-là.

【Figure 1-6】Le rapport hebdomadaire d'acquisition de clientèle qui arrive chaque semaine (données fictives) *(L'écran est en japonais.)*

### 1-8 Une fenêtre qui parle au nom de l'établissement : « T-AI-MURO »

Comme je l'ai écrit en 1-6, les formules s'étaient multipliées et, sur le formulaire de réservation, il était devenu difficile de choisir pour une première visite. Et la clientèle qui vient pour la première fois veut en savoir plus que les formules et les dates. Quelle ambiance règne dans ce lieu ? Peut-on venir en solo sans se sentir à l'écart ? Quel genre de personne tient l'établissement ? Peut-on venir avec des enfants ? Si l'on aligne des boutons de réservation sans répondre à ce genre de questions, on ne peut pas donner à celles et ceux qui hésitent le coup de pouce dont ils ont besoin.

J'ai donc décidé de mettre sur le site de réservation une « fenêtre qui parle au nom de l'établissement ». Quand une personne écrit une question, l'IA répond au nom de l'établissement. Si le nombre de personnes et la date se précisent au cours de la conversation, on peut aller directement à l'écran de confirmation de la réservation. Elle s'appelle « T-AI-MURO », et dans la conversation elle se présente sous le nom de « Tamuro ». T-AI-MURO parle comme l'établissement lui-même, et évoque la direction à la troisième personne.

La clientèle ne tape presque rien. Elle touche simplement les choix proposés par T-AI-MURO, et la conversation avance. Cela signifie que les choix proposés ensuite décident de la qualité de la conversation. Je mélange toujours trois sortes de pistes dans les choix : celles qui mènent vers une réservation (nombre de personnes, prix, créneaux libres, date et heure), celles qui mènent à faire connaissance avec l'établissement (ambiance, direction, qui sont les clients, possibilité de parler avec la personne voisine), et celles qui naissent du fil de la conversation. Amener à une réservation n'est pas le seul but. Faire découvrir l'ambiance de l'établissement et la direction est aussi le cœur de cette fenêtre.

Seuls les prix, ai-je décidé, ne seraient pas calculés par l'IA. Rien ne garantit que l'IA sache calculer correctement, à chaque fois, le cumul des remises ou l'application des paliers selon le nombre de personnes. Le programme produit les prix et les créneaux libres par des calculs fixes, et l'IA s'en tient à la tâche de les mettre en mots.

#### Les premières connaissances venaient de mes propres anciennes publications

Pour que T-AI-MURO réponde aux questions sur l'établissement, il lui faut une connaissance de l'établissement. Comme matière, j'ai exporté toutes les publications que j'avais écrites jusque-là sur Instagram et sur X (anciennement Twitter) et je m'en suis servi. À partir d'elles, j'ai construit les questions que la clientèle était susceptible de poser, et les réponses.

À l'essai, les publications sur X se sont révélées plus utiles comme matière que celles d'Instagram. Instagram, c'est surtout des photos, avec peu de mots. Sur X, j'avais laissé des traces écrites, dans mes propres mots, sur la cuisine, l'établissement et ce que je pensais.

#### Seuls 9 sur 36 ont réussi

Avant de mettre T-AI-MURO en production, j'ai testé la justesse de ses réponses. J'ai fait exécuter les tests par une IA aussi. J'ai donné à une IA jouant la clientèle un personnage et un objectif, et je l'ai fait discuter avec T-AI-MURO. J'ai préparé 36 scénarios : « en solo ce soir », « 4 personnes dans deux semaines », « avec un enfant », « allergies », « privatisation », « prévenir d'un retard », « l'origine du nom de l'établissement », « quel genre de personne tient le lieu », et ainsi de suite.

Résultat du premier passage : 9 réussis sur 36.

La réponse la plus fréquente était « Toutes mes excuses, je n'ai pas bien su répondre ». Cette réponse apparaissait même pour des questions sur l'ambiance de l'établissement et sur la direction. Dès que des mots comme « réservation », « aujourd'hui », « privatisation » ou « responsable » apparaissaient, une liste de créneaux libres s'affichait, quel que soit le vrai sujet de la question. Dans certaines conversations, un message annonçant un retard était pris pour une nouvelle réservation. À une personne végétarienne, il donnait en exemple des plats sautés aux copeaux de bonite et de la soupe miso. Il a même donné en anglais des informations sur un achat groupé que nous avions déjà arrêté.

#### J'ai répondu à 11 questions en une ligne chacune

Une partie de la cause tenait à la façon dont le programme était construit. Je garde cette histoire pour le chapitre 2. L'autre cause était simple : les faits sur l'établissement étaient insuffisants. Une IA ne peut pas répondre à ce qu'elle ignore.

J'ai donc rassemblé les questions auxquelles l'IA ne savait pas répondre et j'ai décidé d'y répondre moi-même, une ligne chacune.

On peut entrer sans réservation. Pour les enfants qui n'ont pas encore l'âge d'aller à l'école primaire, c'est difficile. Annulations et modifications jusqu'à la veille, par e-mail, par téléphone ou par message sur les réseaux sociaux. Pour prévenir d'un retard, merci de téléphoner. Il y a un espace fumeurs à l'extérieur. Apporter ses propres boissons est permis moyennant un droit de bouchon. La privatisation est possible selon la gamme de prix et l'horaire, pour 19 personnes au maximum. Pour les restrictions alimentaires et les anniversaires, nous nous adaptons autant que possible, merci de nous consulter au préalable. La direction est dans l'établissement presque tous les jours d'ouverture. Une fête du yukata est prévue environ une fois par an.

C'est tout. Rien qu'en répondant à 11 questions en une ligne chacune, 24 sur 36 ont réussi au deuxième test.

| Question | Première réponse | Seconde réponse |
| --- | --- | --- |
| Les enfants sont-ils acceptés ? | Toutes mes excuses, je n'ai pas bien su répondre | Dès l'âge de l'école primaire, c'est possible en nous consultant. En dessous, c'est difficile |
| Peut-on entrer sans réservation ? | (liste de créneaux libres) | On peut entrer sans réservation |
| Le responsable est-il là aujourd'hui ? | (liste de créneaux libres) | La direction est dans l'établissement presque tous les jours d'ouverture. Aujourd'hui est un jour d'ouverture, elle prévoit d'être là |
| Est-ce un endroit calme ? Que des habitués ? | Toutes mes excuses, je n'ai pas bien su répondre | C'est un lieu où l'on se détend. La conversation entre clients s'engage facilement, et ce n'est pas un endroit bruyant |

Un schéma a alors commencé à se dessiner. L'IA crée les questions que nous attendons, T-AI-MURO y répond, et nous corrigeons les erreurs. Ensuite, seules les questions qui restent sans réponse faute de faits sur l'établissement sont transmises à la direction. L'effort demandé à la direction se limite à une ligne pour chaque question sans réponse. Tout le reste, l'IA s'en charge.

#### La scène où « budget de ¥5000 (environ $33) » a échoué

J'avais aussi ajouté un verdict d'IA aux tests d'IA. Une autre IA lit le journal de la conversation et décide de la réussite ou de l'échec.

Il y avait parmi eux un scénario avec une personne dont le « budget est de ¥5000 (environ $33) ». Le verdict de l'IA était une réussite. T-AI-MURO avait poliment présenté des formules dans le budget.

Mais à la lecture, c'était un échec. Il n'avait pas demandé le nombre de personnes. Tamuro a une remise de groupe. Selon la taille du groupe, les formules accessibles pour un même budget changent.

À ce moment-là, j'ai reformulé l'objectif.

« Viser un groupe aussi nombreux que possible, pour que le montant total soit au rendez-vous. Confirmer le nombre de personnes. Le but final est de faire venir la clientèle. Plus il y en a, mieux c'est. Pour augmenter les ventes. »

Avec cette seule phrase, toute la conception de la conversation a changé. Toujours confirmer le nombre de personnes avant de répondre sur les prix, et répondre avec le montant total. Juste avant un palier de la remise de groupe, ajouter « avec une personne de plus, vous avez tant de pour cent de remise ». Quand un budget est donné, montrer d'abord la formule la plus haute dans le budget. Cependant, la clientèle qui vient seule représente la moitié de l'établissement : pour une personne seule, ne pas proposer d'augmenter le nombre de convives.

Quand on fait exécuter les tests d'IA par une IA, ils tournent vite. Mais c'est un humain qui décide du critère de réussite. Peut-on énoncer l'objectif en une phrase ? C'est ce qui a décidé de la qualité des conversations de l'IA.

#### Les souhaits de la clientèle passent avant les recommandations de l'établissement

Il y a eu une autre scène où j'ai tracé une ligne importante.

Pendant les tests, j'ai trouvé un problème : toutes les réservations étaient aiguillées vers la formule la moins chère. Une fois corrigé, presque toutes sont devenues, cette fois, la formule Standard, et le montant total moyen a presque doublé. J'ai failli m'en réjouir, mais en y regardant de près, l'IA jouant la clientèle avait simplement appuyé sur le premier choix à chaque fois. Même celles et ceux qui disaient « la moins chère me convient » se voyaient recommander la Standard.

J'ai alors posé un principe. Ce que la clientèle énonce clairement comme souhait (l'option la moins chère, un budget, le nom d'une formule) passe toujours avant la recommandation de l'établissement. La recommandation de l'établissement ne vaut que lorsque la clientèle n'a rien dit.

Le but de l'établissement d'augmenter ses ventes et la confiance de la clientèle peuvent entrer en collision sur une simple façon de recommander. Si la confiance est perdue, les visites elles-mêmes diminuent. C'était la direction, et non l'IA, qui pouvait tracer cette ligne.

Plus tard, quand j'ai réentraîné T-AI-MURO avec un grand nombre de questions, la cause d'erreur la plus fréquente était « réagir à des mots-clés et déclencher une action figée avant de répondre à la question ». Dès qu'il entendait des mots comme « nombre de personnes », « combien » ou « en solo », il sautait la question et passait au parcours de réservation ou aux recommandations. En termes de service, c'est l'employé qui pousse une vente sans écouter la clientèle. Répondre d'abord à la question posée. Ce b.a.-ba de l'hospitalité a été le plus grand défi, même pour l'IA.

Dans la soirée du 6 octobre 2026, T-AI-MURO est apparu en haut du site de réservation comme véritable porte d'entrée. Comme certaines personnes ne veulent pas réserver par la conversation, j'ai conservé à côté l'ancien formulaire de réservation.

> Essayez : ouvrez le site de réservation de Tamuro (https://tamuroreservation.vercel.app/?src=b2-fr-{{FMT}}) et dites à T-AI-MURO « en solo ce soir ». La conversation vous mène jusqu'aux disponibilités et aux prix du jour.

【Figure 1-4】L'écran de conversation de T-AI-MURO. La conversation avance en touchant simplement les choix *(L'écran est en japonais.)*

【Figure 1-10】Les questions sans réponse s'accumulent dans l'écran d'administration (données fictives) *(L'écran est en japonais.)*

### 1-9 Et puis, depuis l'IA de la clientèle

Avec la construction de T-AI-MURO, le site de réservation de Tamuro a acquis la capacité de « répondre en conversation aux questions sur l'établissement, montrer les prix et les créneaux libres, et guider jusqu'à une réservation ».

Ce à quoi j'ai pensé ensuite, c'était de rendre possible la même chose depuis l'IA propre à chaque personne.

T-AI-MURO ne peut parler qu'avec les gens qui viennent sur le site de réservation de Tamuro. Mais beaucoup de personnes consultent d'abord l'IA qu'elles utilisent tous les jours. Si cette IA ne connaît pas Tamuro, Tamuro ne figurera même pas parmi les suggestions. Au lieu d'attendre que la clientèle vienne sur le site de Tamuro, ouvrir la fenêtre de Tamuro du côté de l'IA de la clientèle. C'est le serveur MCP.

À vrai dire, j'ai d'abord hésité à le construire. À ce stade, peu de gens réservent un restaurant depuis leur propre IA. Jugeant que je ne pouvais pas m'attendre à une augmentation directe des réservations, j'avais baissé sa priorité et mis le projet de côté.

J'ai décidé de le construire malgré tout parce que je pensais que ce n'était qu'une question de temps avant que la porte d'entrée change. Comme je l'ai écrit au début, en août 2026, il est devenu possible de réserver depuis ChatGPT via un grand service de réservation. Tôt ou tard, faire chercher un restaurant par l'IA sera la norme. Quand cela arrivera, les petits commerces qui ne sont pas inscrits auprès des grands services disparaîtront du champ de vision de l'IA. Alors, ouvrir la fenêtre avant que la porte d'entrée change.

Ce que j'ai arrêté pour la première version était très restreint. Il lui suffisait de faire la même chose que la fenêtre de conversation du site de réservation (T-AI-MURO). Tout ce qu'elle peut faire, c'est lire les informations de l'établissement, les créneaux libres et les prix, et transmettre l'URL d'une page de réservation avec les critères déjà renseignés. La confirmation de la réservation se fait par la personne elle-même sur la page de Tamuro. L'IA de la clientèle ne confirme pas une réservation de son propre chef. Le dernier geste est accompli par une personne.

Revenons à la scène d'ouverture.

Un vendredi soir, une personne demande à sa propre IA : « Y a-t-il un endroit à Higashi-Nakano où boire un verre en solo ce soir ? » L'IA interroge la fenêtre de Tamuro. Le système de réservation de Tamuro renvoie les créneaux libres de ce soir, ainsi que la formule et le prix qui conviennent à une personne seule. L'IA les transmet à la personne, et lui propose une page de réservation de Tamuro avec la date, l'heure et le nombre de personnes déjà remplis.

Tout ce que j'ai raconté dans ce chapitre soutient cette suite d'étapes. Le système de remises construit en même temps que la hausse de prix. Le système qui fidélise les habitués. Les données qui ont montré que la plupart des réservations se font le jour même. La connaissance de l'établissement née des réponses à 11 questions, une ligne chacune. Le principe de placer les souhaits de la clientèle avant les recommandations de l'établissement.

Un établissement réservable via l'IA ne s'est pas bâti en un jour. Il repose sur l'accumulation de petits systèmes ajoutés un à un, testés, jetés et corrigés.

> Essayez : enregistrez le serveur MCP de Tamuro (https://tamuroreservation.vercel.app/api/mcp) auprès de votre propre IA et demandez : « Y a-t-il de la place chez Tamuro ce soir ? » La façon de l'enregistrer est expliquée dans la Postface.

### 1-10 Ce que j'ai construit, et ce qui a fonctionné

Dans ce chapitre, j'ai parlé de la construction de nombreux systèmes. Mais « j'ai pu le construire » et « l'activité a changé » sont deux choses différentes. Pour finir le chapitre, je vais séparer les deux.

Ce qui a pu être confirmé par des chiffres. Que 88,1 % des réservations sont pour le jour même. Que le nombre de scénarios réussis par la fenêtre de conversation est passé de 9 à 24 rien qu'en ajoutant 11 faits sur l'établissement. Que le taux de réussite pour les indications de prix et de formules est passé de 29,4 % à 42,7 % après les corrections. Ce sont des faits documentés.

