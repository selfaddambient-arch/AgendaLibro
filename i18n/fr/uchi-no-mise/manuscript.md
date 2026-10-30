# Sur mesure pour notre bar

Comment un bar de 19 places a tout construit avec l'IA, des réservations aux outils

Raku Bonta

La série Agenda : https://bontallc.com/agenda?via=b2-fr-{{FMT}}

Instagram de Tamuro : https://www.instagram.com/tamuro.higashinakano/

Site de réservation de Tamuro : https://tamuroreservation.vercel.app/?src=b2-fr-{{FMT}}

## Introduction

Ce livre est le récit simple de la façon dont un bar de 19 places à Higashi-Nakano *(un quartier résidentiel de l'ouest de Tokyo, juste à l'ouest de Shinjuku)*, à Tokyo, fonctionne avec l'aide de l'IA.

Le bar s'appelle « Tamuro ». Le nom désigne un lieu où l'on se rassemble. Il a ouvert en novembre 2018, un petit établissement de 11 places au comptoir et 8 places sur tatami. En journée, dans le même espace, un membre de l'équipe tient un restaurant de curry au steak haché (hambāgu) appelé « Quatre Épices ».

Dans mon livre précédent, *L'adjoint IA*, je parlais de l'IA générative elle-même. En un an environ, l'IA est passée d'un outil qui répond aux questions à un outil qui fait le travail à votre place. Vous lui donnez une instruction, elle écrit le programme, le teste, corrige ses erreurs et mène la tâche à terme. Nous appelons ce type d'IA l'IA agentique.

Grâce à l'IA agentique, j'ai construit moi-même le système de réservation de Tamuro. J'ai construit un système de remises accompagnant une hausse de prix. J'ai construit un système pour fidéliser les habitués. J'ai construit une IA qui répond aux questions de la clientèle. Et au bout du compte, j'ai fini par atteindre ce point : une personne peut poser une question sur Tamuro depuis sa propre IA, puis aller jusqu'à réserver.

J'ai aussi pris les outils pratiques que j'avais conçus pour mon propre commerce, je les ai adaptés pour que d'autres établissements puissent s'en servir, et j'ai commencé à les proposer pour quelques centaines de yens par mois. C'est la série Agenda.

Ce livre décrit ce que j'ai construit en chemin, ce que j'ai raté et ce qu'il m'a fallu réapprendre. Il ne contient pas seulement des réussites. J'ai continué à construire au feeling des choses qui tournaient, et les contradictions se sont accumulées. J'ai découvert plus tard que des informations personnelles de clients pouvaient être lues depuis l'extérieur. L'IA a affirmé comme des faits des choses que l'établissement n'avait jamais dites. J'ai inclus ces échecs tels qu'ils se sont produits.

### Comment lire ce livre

Ce livre compte cinq chapitres.

| Chapitre | Contenu | À qui il s'adresse |
| --- | --- | --- |
| Chapitre 1 | Un établissement réservé par l'IA (le volet gestion du système de réservation) | Tout le monde |
| Chapitre 2 | Les coulisses du système de réservation (technique) | Les créateurs et les passionnés de technologie |
| Chapitre 3 | Partager les outils de mon établissement avec d'autres (le volet entrepreneurial de la série Agenda) | Tout le monde |
| Chapitre 4 | Un système pour construire des produits en solo (technique) | Les créateurs et les passionnés de technologie |
| Chapitre 5 | L'avenir des petits commerces | Tout le monde |

Les chapitres 2 et 4 sont techniques et emploient davantage de termes spécialisés. Chacun s'ouvre sur un résumé en trois lignes des points essentiels : si la technologie ne vous intéresse pas, lisez seulement ces lignes et passez au chapitre suivant. En lisant les chapitres 1, 3 et 5 dans l'ordre, l'histoire tient toujours comme un fil continu.

Chaque fois que j'ai pu, j'ai ajouté une explication en langage simple à côté de chaque terme technique. Même si vous n'avez jamais écrit un programme, j'espère que vous aurez une idée de ce que signifie faire tourner un commerce avec l'IA.

### À propos de l'auteur

J'ai travaillé environ 16 ans dans l'informatique, surtout dans la planification de systèmes et comme intermédiaire entre les équipes sur le terrain et les prestataires de développement, avant de me tourner vers la restauration. Ce n'est donc pas l'histoire de quelqu'un qui n'aurait jamais écrit une ligne de code et aurait tout construit avec l'IA sans aucune aide. Je tiens à être honnête là-dessus.

Cela dit, je peux aujourd'hui construire et exploiter à moi seul, tout en tenant mon bar au quotidien, un outil d'une ampleur qui exigeait autrefois une équipe et des fonds. Il y a quelques années, c'était impensable. Je veux décrire aussi concrètement que possible la réalité de ce changement.

### Comment ce livre a été fabriqué

Ce livre aussi a été réalisé avec l'IA. À partir des notes que je tiens pendant mon travail de développement quotidien, l'IA a rédigé les brouillons, et j'ai relu, révisé et pris les décisions. J'ai aussi demandé à l'IA de réaliser les captures d'écran qui servent d'illustrations.

J'ai tout relu, mais un texte écrit par l'IA peut contenir des choses qui ne sont pas vraies. Comme je l'explique dans le corps du livre, l'IA dit « c'est fait », et le vérifier est le travail d'un humain. Il se peut que ce livre contienne des erreurs qui m'ont échappé.

Par ailleurs, les spécifications des outils et services d'IA changent en quelques mois. Les étapes, les prix et l'état des fonctionnalités selon les fournisseurs décrits dans ce livre sont ceux d'octobre 2026. Quand vous essaierez par vous-même, vérifiez les informations officielles du moment.

Si vous repérez une erreur, cela me ferait plaisir que vous me la signaliez sur note ou sur X. Je corrigerai au fur et à mesure.

### Trois façons de prolonger ce livre

Ce livre se lit gratuitement en PDF, sur note et sur Google Play. (Seul Kindle impose un prix minimum, selon les règles de la boutique.) En contrepartie, j'ai préparé trois suites possibles une fois la lecture terminée. Si un seul d'entre eux vous est utile, écrire ce livre en valait la peine.

1. Essayez dans votre propre commerce. Vous pouvez commencer la série Agenda avec le carnet gratuit. https://bontallc.com/agenda?via=b2-fr-{{FMT}}
2. Suivez ce que je fais. J'écris sur note et sur X à propos des prochains outils que je construis et de la vie quotidienne du commerce. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Si vous passez un jour par Tokyo, venez faire un tour chez Tamuro. À une minute de la sortie est de la gare de Higashi-Nakano. Vous pouvez entrer sans réservation. Site de réservation https://tamuroreservation.vercel.app/?src=b2-fr-{{FMT}}

## Chapitre 1 : Un établissement réservé par l'IA

### 1-1 « Y a-t-il une table ce soir ? » On le demande à l'IA

Un vendredi soir, une personne qui vient de finir sa journée parle à son smartphone.

« Y a-t-il un endroit à Higashi-Nakano où boire un verre en solo ce soir ? Pas trop bruyant. »

Ce n'est pas une connaissance qui répond. C'est l'IA que cette personne utilise tous les jours. L'IA dresse la liste des établissements possibles, décrit l'ambiance de chacun, et indique les horaires disponibles ce soir ainsi que les prix. Si quelque chose retient l'attention, on peut passer directement à l'écran de réservation.

Ce n'est pas de la science-fiction.

Le 10 août 2026, OpenAI a ajouté une fonction de réservation de restaurant à ChatGPT. D'après les notes de version officielles, elle se connecte aux services de réservation OpenTable, Resy et Yelp, et les créneaux disponibles s'affichent directement dans les réponses de ChatGPT. On peut aussi lui poser des questions pour affiner les options, puis, une fois choisi un créneau qui convient, passer directement à la réservation. Elle couvre OpenTable dans le monde entier, Resy aux États-Unis, et Yelp aux États-Unis et au Canada.

Autrement dit, la porte d'entrée par laquelle les gens cherchent où manger commence à passer des moteurs de recherche et des sites d'avis sur les restaurants à « leur propre IA ».

Mais il y a une condition. Les seuls établissements que l'on peut réserver via ChatGPT sont ceux inscrits auprès des grands services de réservation. Les petits commerces qui n'y figurent pas sont invisibles pour l'IA.

Alors que doit faire un bar de 19 places à Higashi-Nakano qui n'utilise pas les grands services de réservation ?

Tamuro a choisi une autre voie. Sans passer par les grands services, il a connecté directement son propre système de réservation à l'IA.

Quand une personne demande à son propre ChatGPT ou à Claude : « Y a-t-il de la place chez Tamuro ce soir ? », l'IA interroge directement le système de réservation de Tamuro, vérifie les horaires disponibles et les prix, puis répond. Une fois les conditions arrêtées, elle oriente vers la page de réservation de Tamuro, avec le nombre de personnes, la date et l'heure déjà remplis. C'est la clientèle elle-même qui appuie sur le bouton de confirmation final.

Ce « point de connexion entre l'IA et le système d'un commerce » s'appelle un serveur MCP. MCP signifie Model Context Protocol, un ensemble commun de conventions qui permet à l'IA d'utiliser des outils et des données extérieurs. J'en explique les détails au chapitre 2.

Les grands services de réservation, d'ailleurs, redirigent eux aussi la clientèle vers leurs propres écrans à la fin. Pour les réservations qui exigent une carte bancaire, la démarche se termine sur l'écran d'OpenTable, et les modifications ou annulations après la réservation se gèrent du côté de chaque service. L'IA est la porte d'entrée, et l'écran du service de réservation est l'endroit où l'on confirme. Ce que fait Tamuro suit la même structure. La seule différence, c'est qu'aucune grande entreprise ne s'interpose.

Et celui qui a construit ce système n'était pas une société de développement extérieure. C'était moi, qui tiens l'établissement. J'ai donné des instructions à l'IA, je lui ai fait écrire les programmes, et je lui ai fait lancer les tests.

Bien sûr, je n'ai pas obtenu ce résultat dès le départ. Tout a commencé par un formulaire de réservation très simple. Puis sont venues une hausse de prix, puis des idées de remises, puis un système pour fidéliser les habitués, puis des échecs et des reconstructions.

Je commence par décrire en cinq lignes quel genre d'endroit est Tamuro. À une minute à pied de la sortie est de la gare de Higashi-Nakano. 19 places, dont 11 au comptoir et 8 sur tatami. Environ la moitié de la clientèle vient seule, et le comptoir facilite la conversation avec la personne voisine. La cuisine associe quatre entrées et un plat, et le plat le plus populaire est un tonteki (steak de porc) légèrement sucré et bien relevé à l'ail. Les vins viennent surtout d'Espagne et d'Italie, et il y a une vingtaine de gins artisanaux japonais. On peut aussi venir sans réservation.

Je dois aussi dire ce que je visais. Je ne voulais pas me contenter de prendre des réservations. Je voulais que même un petit commerce puisse construire de ses propres mains tout le parcours : se faire connaître, faire venir du monde, faire revenir. Les remises, les e-mails et la fenêtre de discussion qui apparaissent dans ce chapitre sont tous des éléments au service de ce seul objectif.

Dans ce chapitre, je remonte le temps pour retracer comment le système de réservation de Tamuro s'est développé.

【Figure 1-1】L'écran après la connexion de ChatGPT au serveur MCP de Tamuro (10 octobre 2026). Il lit les informations de l'établissement et répond qu'il sait traiter les horaires disponibles, les menus, les prix et l'orientation vers la page de réservation *(L'écran est en japonais.)*

### 1-2 Le point de départ : prendre seulement des réservations

[Le site de réservation de Tamuro](https://tamuroreservation.vercel.app/?src=b2-fr-{{FMT}}) était très simple au début. On choisit une date, une heure et un nombre de personnes, on saisit un nom et des coordonnées, et on envoie. Une notification arrive à l'établissement. C'est tout.

J'ai construit la première base avec l'outil de développement par IA de Google (Antigravity). Je décrivais à l'IA chaque fonction qui me venait à l'esprit, et quand quelque chose marchait, je passais à la suivante. C'est ce qu'on appelle le vibe coding (dire à l'IA tout ce qui vous passe par la tête et la laisser construire au feeling).

Pour moi, à l'époque, c'était une surprise après l'autre. Il suffisait de décrire en mots la disposition d'un écran pour qu'il prenne forme en quelques minutes. Si je demandais un calendrier, un calendrier apparaissait. Dans les creux du service, un site de réservation a vu le jour.

Tamuro est un endroit où l'on peut entrer sans réservation. En réalité, la plupart des réservations se font le jour même, et beaucoup de clients viennent sans avoir réservé. Malgré cela, j'ai construit un système de réservation parce que je voulais un moyen de rester en lien avec la clientèle avant sa venue. Une fois qu'une personne a réservé, son nom et ses coordonnées restent. Une fois les coordonnées conservées, je peux l'inviter à revenir.

Un système de réservation n'est pas qu'une simple prise de réservations. Il devient la porte d'entrée d'une relation avec la clientèle. Cette idée a mené plus tard au système de remises et au système de fidélisation des habitués.

Mais pour une base construite à l'instinct, j'ai fini par payer un lourd tribut plus tard. J'en parlerai au chapitre 2.

### 1-3 Construire en même temps une hausse de prix et des remises

Pour un restaurant ou un bar, une hausse de prix est une décision inévitable. Les ingrédients, l'énergie et la main-d'œuvre renchérissent sans cesse. Tamuro a augmenté ses prix aussi. J'ai relevé chaque menu d'environ ¥400–¥500 (environ $2,7–$3,3).

La hausse était importante, et il était évident qu'en l'annonçant telle quelle, les habitués s'éloigneraient. Alors, en même temps que la hausse des prix, j'ai décidé d'intégrer un système de remises au système de réservation. Il ne se contente pas de baisser les prix. Il récompense par des remises la clientèle dont le comportement est bénéfique pour l'établissement.

La première est la remise de groupe. Plus le groupe est nombreux, plus le prix par personne baisse. Environ la moitié de la clientèle de Tamuro vient seule, mais quand elle vient en groupe, les ventes de l'établissement augmentent beaucoup. Même après déduction de la remise, l'établissement y gagne. Pour la clientèle aussi, c'est une raison d'inviter des amis. De fait, le nombre de clients venant en groupe grâce à la remise selon le nombre de personnes du site de réservation a augmenté.

La deuxième est la remise pour réservation anticipée. En réservant au moins une semaine à l'avance, on obtient 2 % de remise ; au moins deux semaines à l'avance, 4 %. La plupart des réservations de Tamuro se font le jour même, ce qui m'empêche de prévoir la suite. La remise pour réservation anticipée est un mécanisme pour sécuriser les ventes futures. Les jours de pluie et les jours de froid, si des réservations sont déjà là, l'établissement peut se préparer l'esprit tranquille.

Troisièmement, j'ai aussi construit un mécanisme d'achat groupé. Si un nombre donné de personnes se réunissait à une date et une heure données, un menu à prix fixe serait proposé à un prix réduit. C'était censé être un mécanisme dans l'esprit de Tamuro, où des inconnus se retrouvent en même temps.

Mais l'offre d'achat groupé n'a jamais été utilisée. Résultat nul. En août 2026, j'ai arrêté cette offre et décidé de ne plus l'utiliser.

Jeter ce que l'on a fabriqué donne une impression de gâchis. Mais si l'on construit avec l'IA, le coût et le temps de construction sont faibles. On construit petit, on essaie, et si cela ne marche pas, on jette. Je crois que cette rapidité est le plus grand avantage de faire tourner un commerce avec l'IA.

Il y a encore une astuce dans la tarification. Parmi les formules, je place volontairement une formule premium chère. Peu importe que presque personne ne la choisisse. À côté d'une formule chère, la formule standard paraît abordable. Elle joue le rôle de ce qu'on appelle une ancre (un point de référence pour comparer).

【Figure 1-7】Plus il y a de monde, plus le prix par personne baisse (comparaison pour 1, 4 et 6 personnes)

### 1-4 Un système pour fidéliser les habitués

Une fois que les noms et les coordonnées sont conservés dans le système de réservation, la chose suivante que l'on veut faire est de cultiver la relation avec la clientèle. Un système qui gère les informations des clients et approfondit les relations s'appelle un CRM (gestion de la relation client). Petit à petit, j'ai ajouté des fonctions de CRM au système de réservation de Tamuro.

Quand les clients s'inscrivent comme membres, ils peuvent consulter leur historique de réservations sur une page personnelle. S'ils enregistrent leur anniversaire, un petit cadeau d'anniversaire leur parvient. Les membres qui ne sont pas venus depuis un moment reçoivent un message pour les rappeler. Il y a aussi une carte de fidélité à tampons. Trois visites donnent droit à un verre, cinq à un steak et à d'autres avantages, et après cinq le compte repart de zéro. Il y a aussi une fonction de parrainage d'amis.

J'ai conçu avec un soin particulier le mécanisme qui invite à une deuxième visite. Dans les restaurants et les bars, on dit que le retour d'une personne pour une deuxième visite décide de sa fidélisation. À Tamuro, j'envoie deux e-mails d'invitation, sept jours et 21 jours après la première visite. Le premier ne contient pas de coupon ; seul le second en contient un. Plutôt que d'attirer par une remise dès le départ, je cherche d'abord à me rappeler à son bon souvenir. Si la personne ne vient toujours pas, je lui donne un petit coup de pouce.

J'ai aussi veillé à ce que les e-mails ne s'accumulent pas. La clientèle reçoit au plus un message par jour. Quand plusieurs messages doivent partir le même jour, la priorité suit cet ordre : anniversaire, invitation à la deuxième visite, relance des membres inactifs, autres avis. Les membres qui ont déjà leur prochaine réservation ne reçoivent pas d'e-mails les invitant à venir.

Le consentement à recevoir des e-mails est désactivé par défaut. Le laisser activé augmenterait le nombre de destinataires, mais une conception où les gens consentent sans le savoir pourrait poser problème au regard du droit de la consommation. Gagner la confiance plutôt que les chiffres. C'était mon jugement.

Il y a une autre petite attention dans les e-mails. Un « Sujet du jour » figure dans l'e-mail de confirmation de réservation. Quelque chose sur la saison, le vin ou la cuisine. L'IA rédige automatiquement chaque jour un court sujet.

L'objectif est de remettre à la personne une amorce de conversation avant sa venue. Tamuro est un établissement où l'on discute beaucoup entre clients. Un sujet lu dans l'e-mail devient la première chose que l'on dit à la personne voisine au comptoir. Je n'ai donc pas laissé l'e-mail de confirmation se limiter à « Votre réservation a bien été reçue » ; j'ai voulu qu'il transmette à l'avance un peu de l'atmosphère de l'établissement.

J'ai changé une fois l'IA qui rédige les sujets. J'ai opté pour une IA qui produit des sujets plus naturels et plus proches du ton de l'établissement. Cependant, ce n'est pas un mécanisme pour augmenter la fréquentation. C'est un mécanisme pour rendre un peu meilleure l'expérience de celles et ceux qui viennent. Je reparlerai de cette distinction dans la seconde moitié de ce chapitre.

Parmi ces mécanismes, celui dont les résultats sont devenus peu à peu visibles est le duo des formules « Enchanté » et « Bon retour parmi nous ». Ce sont des formules d'accès facile, à prix raisonnable, que seuls les nouveaux clients et les clients qui ne sont pas venus depuis plus d'un an peuvent choisir. Elles donnent une raison de venir à la clientèle nouvelle comme à celle qui s'éloigne.

En revanche, il y avait aussi un problème. Beaucoup de clients réservent en invités sans s'inscrire comme membres. Si j'exigeais l'inscription à chaque réservation, certains pourraient renoncer à réserver. Alors, une fois la réservation terminée, j'affiche une invitation : « Souhaitez-vous associer cette réservation à un compte membre ? », et j'ai prévu un moyen de devenir membre après coup. Cela n'érige aucun obstacle à la réservation, et le lien peut se nouer après coup.

【Figure 1-8】Formules que seuls les nouveaux clients et les personnes qui ne sont pas venues depuis plus d'un an peuvent choisir *(L'écran est en japonais.)*

【Figure 1-9】La carte de fidélité à tampons sur la page personnelle (données fictives) *(L'écran est en japonais.)*

【Figure 1-5】E-mail de confirmation de réservation. Un « Sujet du jour » y figure (données fictives) *(L'écran est en japonais.)*

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

Ce qui meurt, c'est la couche intermédiaire du SaaS : celle qui facture un abonnement mensuel élevé par siège et suppose que des personnes l'utilisent à travers des écrans. Si l'IA fait le travail à la place des gens, on n'a plus besoin d'un siège par personne. Si plus personne ne se sert d'un écran, on n'a plus besoin d'un écran élaboré.

Ce qui reste, ce sont des outils bon marché qui font une seule chose de façon fiable. Et des outils faciles à utiliser pour une IA.

C'est exactement la définition des trois principes de la série Agenda. Elle fonctionne automatiquement, elle s'en remet à l'IA de la direction (force empruntée) et elle ne fait qu'une seule chose (fonction unique). Planning d'équipe laisse la construction du planning à l'IA de la direction, ce qui correspond tout à fait à la forme « l'IA utilise le logiciel » que décrit Huang. Le système de réservation de Tamuro ouvre une fenêtre via MCP aux IA de la clientèle, et c'est la même idée.

Il peut certes sembler y avoir ici une contradiction. Je parle de la mort du SaaS, alors que la série Agenda est elle-même un SaaS. Mais la série Agenda est un ensemble d'outils construits par une direction pour son propre établissement, puis rendus publics à bas prix. Ce n'est pas un modèle qui facture un abonnement mensuel élevé par siège, et il ne suppose pas que des personnes restent rivées chaque jour à un écran. Il est conçu dès le départ en partant du principe que l'IA l'utilisera.

#### La « mort du SaaS » pour les restaurants

Ce débat peut ressembler à une histoire d'investisseurs et d'industrie informatique. Mais pour les restaurants, la même chose est sur le point d'arriver sous une forme bien plus proche de leur quotidien.

De nombreux établissements indépendants paient un abonnement mensuel à des sites d'avis sur les restaurants et à des sites de réservation, et paient en plus une commission pour chaque réservation apportée. En échange de l'apport de clientèle, le site détient le lien avec les clients, et il n'est pas rare que l'établissement n'ait même pas leurs coordonnées. Si les prix augmentent, l'établissement n'a d'autre choix que de suivre, et si le système de classement change, le flux de clientèle change.

Comme je l'ai écrit au chapitre 1, en 2026 s'est ouverte l'époque où les clients font chercher les établissements par leur propre IA. Si le point d'entrée se déplace vers l'IA, tout le modèle qui consiste à payer abonnements et commissions à un site pour figurer en bonne place dans ses listes commence à vaciller. Si un établissement ouvre de lui-même une fenêtre vers l'IA, la clientèle peut le joindre sans passer par les grands sites. Les registres de réservation et la relation avec la clientèle restent entre les mains de l'établissement.

Si je traduis « la mort du SaaS » dans le langage d'un établissement indépendant, cela donne « la fin de l'époque où payer suffisait pour être référencé ». Tamuro a ouvert sa fenêtre via MCP et garde ses réservations et sa gestion de la relation client selon ses propres spécifications, en préparation de cela.

Le SaaS va-t-il mourir ? Personne ne le sait encore. Mais la forme des outils qui subsisteront à l'ère de l'IA se dessine peu à peu. Voilà ce que je pense.

### 3-7 Monétisation : petit, nombreux, bon marché

Je construis la série Agenda pour en faire une activité viable à part entière. L'objectif : un deuxième pilier de revenus, distinct du restaurant.

Je fixe des prix bas, pour de petits montants. Les abonnements mensuels commencent à quelques centaines de yens. Pointages, par exemple, coûte ¥500 (environ $3,3) par mois. Je mêle aussi des outils gratuits, comme Rentabilité, Carnet de Lumière et Prix de revient. Les outils gratuits servent de porte d'entrée pour faire connaître la série Agenda. Carnet de Lumière n'utilise ni API de cartographie ni IA générative, de sorte qu'il ne coûte presque rien à faire tourner. C'est pourquoi je peux l'offrir gratuitement.

Il n'y a qu'un seul compte. Avec un compte commun appelé AgendaID, on peut utiliser tous les outils de la série. Pas besoin de s'inscrire de nouveau pour chaque outil. Les outils payants offrent trois mois gratuits et peuvent être démarrés sans enregistrer de carte. La période gratuite n'est accordée qu'une seule fois par combinaison d'établissement et de produit. Si vous parrainez un autre établissement, vous recevez un bonus.

La raison pour laquelle je peux garder des prix bas tient à ma façon de construire. Je construis seul, je fais construire par l'IA, et je réutilise une base commune. Le coût de la base de données est maintenu à environ $35 par mois pour l'ensemble de la série. Si le coût de construction et le coût d'exploitation sont tous deux faibles, une activité peut tenir même avec de petites ventes.

Soyons honnêtes. Au moment où j'écris ce livre, quelques établissements ont essayé les outils, mais il n'y a presque aucune inscription payante. Le système pour construire est en place, mais le système pour se faire connaître reste à venir. Ce livre est aussi destiné à servir à cela, à se faire connaître.

#### Construire quelque chose et le faire utiliser durablement sont deux choses différentes

Soyons honnêtes sur un autre point. Pouvoir construire un outil et faire en sorte que quelqu'un continue de s'en servir sont deux sujets distincts.

Construire est devenu plus rapide grâce à l'IA. Mais faire en sorte que les gens continuent à l'utiliser demande un autre travail. Répondre aux questions sur la façon de s'en servir (le Guide d'assistance existe pour cela). Envoyer un avis avant la fin de la période gratuite. Expliquer la raison d'une hausse de prix. Supprimer correctement les données quand quelqu'un demande à résilier. Et surtout, le maintenir en marche sans que la direction y touche.

Parmi les trois principes de la série Agenda, l'« automatique » est le principe qui sert à ce que l'outil continue d'être utilisé. Un outil qui ne marche pas sans que la direction y touche chaque jour finira résilié. Ce n'est pas fini quand c'est construit. Cela ne devient une activité que lorsque l'outil continue d'être utilisé. Ajouter, un par un, des établissements qui continuent à s'en servir : c'est mon travail après la publication de ce livre.

#### Si vous voulez commencer dans votre propre établissement

Pour celles et ceux qui, après avoir lu ce livre, veulent essayer dans leur établissement, il y a trois étapes.

1. Ouvrez https://bontallc.com/agenda?via=b2-fr-{{FMT}} et connectez-vous avec un compte Google (AgendaID sera créé. Aucune carte à enregistrer)
2. Commencez par ajouter un carnet gratuit. Je recommande Carnet de Lumière. Il suffit de coller le widget du panneau dans votre site web, et cela fonctionne en 10 minutes. Si vous n'avez pas encore ouvert, essayez Rentabilité
3. Si cela vous semble convenir, essayez Pointages gratuitement pendant trois mois. Un avis arrive à l'approche de l'échéance, vous n'aurez rien à payer même si vous laissez les choses en l'état

Si vous avez des questions, posez-les via le Guide d'assistance (AgendaQA). L'IA répond instantanément aux questions de fonctionnement, et je lis moi-même les questions sur les spécifications et les bogues.

Le chiffre d'affaires d'un restaurant dépend de la météo et de la saison. Le nombre de places et les horaires d'ouverture ont tous deux des limites. Les ventes d'outils, elles, n'ont pas de limite de places. Tenir un établissement tout en distribuant des outils nés des problèmes de son propre établissement, et voir cela devenir lentement un revenu : je crois que cela peut devenir une autre façon de gagner sa vie pour un établissement indépendant.

#### Rester une petite entreprise, aller à l'international

Il y a encore une chose que j'ai décidée dès le départ pour la série Agenda. Je ne la construirais pas en japonais seulement.

Pointages, Rentabilité et le Guide d'assistance peuvent tous s'utiliser en 20 langues. Les textes d'écran et les questions fréquentes, tout. Un outil conçu pour un bar de 19 places à Tokyo fonctionne de la même façon en anglais, en coréen, en vietnamien.

Il y a deux raisons. La première, c'est que les problèmes des restaurants ne changent pas quand on change de pays. On veut enregistrer les arrivées et les départs du personnel. On veut connaître sa rentabilité avant d'ouvrir. On veut dire à la clientèle que l'heure de fermeture est repoussée. Ce sont tous des problèmes que les établissements indépendants du monde entier partagent. La seconde, c'est que le nombre d'établissements indépendants au Japon continue de baisser. Si je ne servais que le marché japonophone, les ventes d'outils auraient un plafond.

Autrefois, pour qu'une petite entreprise vende ses produits à l'étranger, il lui fallait des agents locaux, des sociétés de traduction et des entités juridiques. Aujourd'hui, l'IA aide à la traduction et à la relecture. Des systèmes de paiement communs fonctionnent partout dans le monde. Pour la distribution, il suffit d'un serveur, et il n'y a ni stock ni entrepôt dans chaque pays. Un outil développé par une seule personne peut être disponible dans le monde entier, en 20 langues, dès le lendemain de sa création. Autrefois, seules les grandes entreprises pouvaient le faire.

Une toute petite entreprise qui travaille avec plusieurs pays dès le départ : on appelle parfois ces entreprises des micro-multinationales (de minuscules entreprises multinationales). Bonta LLC vise exactement cela, avec un seul établissement à Higashi-Nakano et une seule personne aux commandes.

Bien sûr, traduire en 20 langues ne veut pas dire que les établissements à l'étranger vont se mettre à l'utiliser tout de suite. Certaines traductions attendent encore la relecture de locuteurs natifs pour sonner naturellement. Malgré tout, en supprimant dès le départ la barrière de la langue, le plafond de ce que les outils peuvent atteindre disparaît, tout comme le plafond du nombre de places.

La façon dont je construis cette base fait l'objet du chapitre 4.

【Figure 3-5】Le changement de langue dans le Guide d'assistance. 20 langues sont proposées *(L'écran est en japonais.)*

## Chapitre 4 : La technologie – un système pour construire des produits seul, en continu

Points clés de ce chapitre

- J'ai mis dans un document la procédure de lancement d'un nouveau produit, sous une forme (une compétence, ou « skill ») qu'une IA peut lire et exécuter. Les humains ne font que juger et accomplir les opérations que seuls les humains peuvent faire
- Les parties communes, comme la connexion, la facturation, les pages de présentation et les liens vers les autres produits, sont construites une seule fois et réutilisées dans tous les produits. Le coût de base de données de cette fondation est d'environ $35 par mois
- Le système continue de se développer. J'ajoute sans cesse au document de procédure les échecs, comme un design rejeté cinq fois de suite

(Ce chapitre contient beaucoup de termes techniques. Si la technologie ne vous intéresse pas, vous pouvez passer directement au chapitre 5, le récit se suit quand même.)

### 4-1 ProductBootstrap : confier à l'IA la procédure de lancement elle-même

À chaque produit construit, je répétais les mêmes préparatifs et les mêmes erreurs. Créer un dépôt (un espace de stockage pour les programmes). Brancher la connexion. Décider des couleurs du design. Mettre en place le système de tests. Préparer l'environnement de production. Je l'avais certainement fait pour le produit précédent, mais j'en avais oublié les détails et je butais aux mêmes endroits.

J'ai donc mis dans un document la procédure de lancement d'un nouveau produit. J'appelle « skill » la forme de ce document que l'IA qui écrit le code (Claude Code) peut lire et exécuter. Cette skill s'appelle ProductBootstrap. « Bootstrap » est un terme courant en informatique pour désigner le démarrage autonome à partir d'un mécanisme minimal, et je l'ai appliqué au lancement de produits.

Je ne garde aucun programme modèle. Je copie le dernier produit achevé et je démarre le nouveau produit à partir de lui. Ainsi, les leçons les plus récentes passent automatiquement au produit suivant. Il n'y a pas non plus à entretenir un vieux modèle.

#### Le déroulement de la procédure

1. Remettre le cahier des charges. Si les champs obligatoires (nom du produit, ce qu'il fait, qui l'utilise, prix, unité de tarification, couleur d'identification, emplacement du design de référence, etc.) restent vides, l'IA ne démarre pas. La règle est qu'elle ne pose pas de questions à la direction en cours de route. Si tout n'est pas réuni au départ, elle ne commence pas
2. Décider de la couleur du produit. Chaque produit de la série Agenda a une couleur d'identification. L'IA mesure les couleurs des produits existants, propose environ quatre couleurs candidates bien distinctes, et la direction choisit
3. Fixer le design. Je fais créer des propositions d'écrans par une IA de design (Claude Design). L'IA mène son autocontrôle jusqu'à trois tours, et seules les propositions qui passent le contrôle sont présentées à la direction
4. Laisser l'implémentation à l'IA jusqu'au bout. L'IA construit et corrige seule jusqu'à remplir les conditions de recette fixées (vérification des types, vérification du style, tous les tests au vert, réussite de tous les contrôles d'écran, et changements de base de données passant sans accroc dans l'environnement de test)
5. La direction n'approuve qu'au passage en production. Tout ce qui précède, jusqu'à l'environnement de test, avance de façon autonome, et la direction ne juge que l'opération de production

J'ai construit l'étape d'implémentation pour qu'elle ne s'arrête pas en route afin d'attendre l'approbation de la direction. Au début, j'avançais en demandant l'approbation à chaque étape, mais rien n'avançait ainsi. Quand il y a plusieurs fenêtres de travail d'IA, chacune s'arrête en attendant l'approbation, et la direction doit faire le tour de toutes les fenêtres pour juger. J'ai donc changé : je remets à l'avance le périmètre déjà approuvé et les conditions de recette qu'une machine peut juger, et elle ne s'arrête qu'en cas d'échec.

Les conditions d'arrêt sont fixées aussi. Quand le document de procédure et la décision de la direction se contredisent. Quand une opération que seul un humain peut faire devient nécessaire. Quand elle n'avance pas sur la même erreur trois fois de suite. Quand l'authentification expire, que les droits sont insuffisants ou qu'une opération irréversible est requise. Sinon, l'IA avance seule. L'état du travail est consigné dans un petit fichier, de sorte qu'en cas de plantage en cours de route, elle peut reprendre à partir de là.

#### Les humains ne font que deux choses

Je l'ai écrit dans le document de procédure : l'IA exécute toutes les étapes. On ne peut demander à la direction que les deux choses suivantes.

- Le jugement lui-même. Approuver, trancher, décider laquelle de deux options retenir
- Les opérations que seul un humain peut faire. Des clés qui ne peuvent être générées que depuis l'écran d'administration d'un service externe, des démarches impliquant une vérification d'identité, des opérations sur un appareil réel et des jugements visuels

Si l'IA confie autre chose à la direction, c'est une violation du document de procédure. Dans le tableau de la procédure, j'ai ajouté à chaque ligne une colonne « exécutant », et toute ligne où l'on inscrit « direction » comme exécutant, sans pouvoir en donner la raison, passe du côté de l'IA.

J'avais une raison d'instaurer cette règle. En triant le travail restant pour un produit, l'IA avait aligné « créer le projet serveur », « enregistrer la destination de connexion », « saisir les variables d'environnement » et « construire l'environnement de test », tous comme des tâches pour la direction. Chacune était une opération que l'IA pouvait réaliser elle-même. « Pourquoi est-ce moi qui fais ça ? » fut ma réaction sincère à ce moment-là. L'IA le fait elle-même si on le lui demande. Mais si on ne le lui demande pas, elle le passe à une personne. C'est pourquoi il a fallu l'écrire dans le document de procédure.

J'ai mis dans la liste de contrôle de ce document de procédure tous les échecs du système de réservation que j'ai décrits au chapitre 2. Mettre d'abord les tests. Ne pas garder de données de production dans l'environnement de développement. Construire d'abord l'environnement de test. Le produit suivant évite dès le départ les mêmes douleurs.

#### Toujours en croissance

Ce document de procédure n'est pas un produit fini. J'y ajoute quelque chose chaque fois qu'un échec survient.

Par exemple, il y a eu un moment où j'ai fait créer par l'IA de design l'écran d'un produit cinq fois de suite, et les cinq propositions ont été rejetées. Cela inclut les tours où je lui avais remis les règles de design de toute la série (DESIGN.md).

Au début, l'IA a diagnostiqué la cause comme étant « la palette de couleurs elle-même ». J'ai écarté ce diagnostic. Les causes réelles étaient au nombre de deux. La première : des couleurs sans définition dans les règles étaient utilisées librement. La seconde : trois sections de rôles différents étaient empilées verticalement avec la même couleur de fond et les mêmes marges, sans frontière entre elles. Aucune règle n'avait été violée, et pourtant les rôles avaient disparu de l'apparence.

J'ai donc ajouté des clauses aux règles de design. Ne pas donner la même apparence à des choses de rôles différents. Ne pas les séparer par la seule couleur. Le plus important vient en premier dans le parcours du regard. Seules les choses vraiment égales peuvent être alignées avec le même poids. Ne pas faire une mise en page qui se contente d'empiler les choses à la verticale.

Il y a eu une autre leçon tirée de l'échec. Si l'on ne transmet que sous forme de liste d'interdictions l'« apparence par défaut à éviter », l'IA bascule entièrement vers une autre apparence par défaut qui ne figure pas dans la liste. Quand j'ai interdit d'un coup les cartes, les ombres et les coins arrondis, ce qui est revenu était un écran de type journal, fait uniquement de filets et de marges. Depuis, je fais rédiger les documents de demande en trois colonnes : « le motif à éviter », « ce que je voulais interdire » et « quoi faire à la place ».

J'ai aussi changé en cours de route ma façon de décider les couleurs d'identification. Vers le moment où les produits ont dépassé huit, la plage des couleurs sombres était occupée par les produits existants, et le neuvième produit ainsi que les suivants ne pouvaient plus obtenir de couleur sombre pour les traits et les boutons sans entrer en collision avec celles qui existaient. J'ai donc révisé la règle : la couleur d'identification d'un produit n'est utilisée que pour les couleurs de surface claires, et les traits, filets, icônes et boutons principaux sont tous unifiés dans la couleur d'encre commune à la série. C'était une contrainte qui n'est apparue qu'une fois les produits multipliés.

Chaque fois qu'une chose échoue, je corrige le document de procédure. Le produit suivant en devient d'autant plus facile. Je crois que faire croître le document de procédure est le meilleur investissement pour continuer à construire des produits seul.

【Figure 4-2】Les étapes de la procédure de lancement, et qui les exécute (l'IA ou la direction) *(L'écran est en japonais.)*

【Figure 4-3】Les couleurs d'identification de la série Agenda. Une couleur par produit, utilisée uniquement sur les surfaces *(L'écran est en japonais.)*

### 4-2 AgendaHub : la porte d'entrée

À mesure que les produits se multiplient, on finit par construire sans cesse les mêmes choses. La connexion, la facturation, les pages de présentation, les liens vers les autres produits. Pour gérer tout cela seul, il faut construire les parties communes une seule fois et les réutiliser dans tous les produits.

AgendaHub est l'endroit où ces parties communes sont rassemblées. Je l'appelle la « porte d'entrée ».

D'abord, c'est l'entrée qui aiguille depuis une seule adresse vers chaque produit. Sous un seul domaine, bontallc.com, une entrée par produit est alignée : /agendatimbro, /agendaoro, /agendaluce. Pour la clientèle, on dirait que les produits se trouvent dans un seul site, mais en réalité un programme distinct fonctionne derrière chacun.

Ensuite, c'est l'endroit où sont placées les pages de présentation des produits. Il y a une page de présentation pour la série, et dedans une section pour chaque produit. Chaque section contient le nom du produit et son surnom, le prix, un problème énoncé dans les mots mêmes de la direction en commençant par « Quand vous... », une description de ce qu'il sait faire, et un lien vers la page de détail. Quand je publie un nouveau produit, l'ajout de cette section fait partie de la procédure de lancement.

Enfin, c'est le référentiel des règles de design et des procédures de lancement. La référence des couleurs d'identification, les règles d'écran (DESIGN.md), la skill ProductBootstrap que j'ai décrite en 4-1, la skill qui vérifie les écrans et la skill qui fait les changements de base de données en sécurité. Pour toutes les règles qui traversent la série, le contenu réel se trouve ici, et chaque produit le lit par référence.

【Figure 4-1】La structure de la série Agenda. De la porte d'entrée (AgendaHub) à chaque carnet, et chaque carnet se relie à un seul compte (AgendaID) *(L'écran est en japonais.)*

### 4-3 AgendaID : comptes et facturation communs

AgendaID est le système commun de la série pour les comptes et la facturation.

Il suffit de se connecter une fois avec un compte Google pour utiliser tous les produits. Pas besoin de créer un compte pour chaque produit. Je prévois aussi, à terme, de reporter les réglages de langue d'un produit à l'autre.

La facturation aussi est un système unique. Au lieu de construire pour chaque produit la liaison avec le service de paiement (Stripe), AgendaID prend tout en charge. Il y a quatre catégories de tarification : un produit léger à ¥300 (environ $2) par mois, un produit à l'usage, un produit à achat unique à ¥600 (environ $4) et un produit gratuit. Les produits payants offrent trois mois gratuits sans enregistrement de carte, utilisables une fois par combinaison d'établissement et de produit. Il existe aussi un mécanisme qui ajoute trois mois de période gratuite à la personne qui parraine et à la personne parrainée.

Avant la fin de la période gratuite, des e-mails de notification arrivent sept jours et un jour avant. J'avais d'abord construit ces e-mails à l'intérieur de Pointages aussi, mais, les produits se multipliant, j'ai compris qu'il était inutile de donner le même mécanisme à chaque produit, et je l'ai donc regroupé du côté d'AgendaID.

#### Résiliation et suppression sous des règles communes, elles aussi

Il y a un volet discret mais important : la résiliation et la suppression des données.

Quand un client résilie, quelles données sont supprimées, et quand ? Si on le construit séparément pour chaque produit, quelque chose sera forcément oublié quelque part. De plus, la série Agenda comprend des produits qui traitent des données particulièrement sensibles, comme celui qui identifie les habitués par reconnaissance faciale.

J'ai donc divisé la granularité de la suppression en quatre niveaux et j'en ai fait une règle commune à la série. Ce sont la résiliation d'un produit, la suppression d'un établissement, le retrait d'un compte (quitter toute la série) et une demande de suppression émanant d'un membre du personnel à titre individuel. Les niveaux supérieurs se répercutent sur les inférieurs, et chaque produit enregistre auprès du système commun sa propre procédure de suppression des données. Le délai de grâce avant suppression est de 30 jours, et pendant ce temps on peut l'annuler.

Un axe temporel s'y ajoute. Les registres de présence, par exemple, doivent être conservés cinq ans selon la loi. Même si un ancien membre du personnel demande la suppression, pendant la période de conservation, il faut garder le registre, avec les noms et autres informations anonymisés, plutôt que de l'effacer physiquement. Il m'a fallu décider la frontière entre « supprimer » et « conserver » en la vérifiant au regard de la loi.

#### Une connexion de test pour que l'IA ne contamine pas la production

J'ai ajouté à AgendaID un mécanisme de plus, pour l'IA : une entrée de connexion de test.

Pour faire vérifier à l'IA que les choses fonctionnent, il faut que l'IA se connecte et manipule les écrans. Mais la connexion se fait avec un compte Google, donc l'IA ne peut pas se connecter seule. Et je ne peux pas non plus remettre à l'IA le compte de la direction. Il y a un risque que les tests de l'IA contaminent les données de production.

J'ai donc construit une entrée qui délivre des comptes synthétiques (des personas) utilisables uniquement dans l'environnement de test. Elle ne fonctionne pas en production. La base de données de l'environnement de test est un projet distinct de celui de la production et ne contient que des données synthétiques. L'IA se connecte par cette entrée, manipule les écrans et confirme que les choses fonctionnent. Les comptes de test sont reconstruits chaque jour, et les anciens sont supprimés.

Ainsi, l'IA peut mener seule même le contrôle final, dans un environnement construit exactement comme la production, sans toucher à la production.

### 4-4 La navigation commune, et l'échec du mot « porte d'entrée »

Pour que les utilisateurs puissent passer de n'importe quel produit aux autres, j'ai donné à chaque produit un menu de navigation commun. C'est le chemin qui permet à une personne qui tient un bar et utilise Pointages de poser une question dans le Guide d'assistance, ou d'aller voir les autres carnets.

Il y a derrière cette navigation commune une petite histoire d'échec.

Dans la première version, j'avais placé un lien disant « Retour à la porte d'entrée ». C'était parce qu'en interne, j'appelais AgendaHub la « porte d'entrée ». Mais en vérifiant sur un appareil réel, quelque chose clochait. Deux liens, « Retour à la porte d'entrée » et « Voir la série Agenda », menaient au même endroit. De plus, le lien d'assistance se trouvait au-dessus du menu du travail quotidien, de sorte que l'ordre d'importance était inversé. Et surtout, les mots « porte d'entrée » ne veulent rien dire pour une direction qui utilise le produit pour la première fois. C'était le jargon interne de la personne qui conçoit.

J'ai donc redéfini les principes. Ordonner les éléments selon leur proximité avec l'objectif de l'utilisateur : le travail quotidien tout en haut, les liens qui mènent à l'extérieur tout en bas. Même un lien destiné à attirer de nouveaux utilisateurs ne passe jamais au-dessus du travail. La frontière doit pouvoir s'expliquer en une seule ligne. Écrire les libellés dans la langue de l'utilisateur, pas dans le langage interne. Ne jamais mettre plus d'un lien menant au même endroit. J'ai supprimé « Retour à la porte d'entrée » et tout fusionné en un seul lien, « Voir les autres carnets Agenda ».

Au chapitre 2, j'ai écrit sur l'apprentissage du langage de l'interface. C'était le langage que la direction utilise pour parler à l'IA. Ici, c'est l'inverse : le langage que la personne qui conçoit utilise pour parler à l'utilisateur. Dans les deux cas, il s'agissait d'adapter ses mots à la personne à qui l'on parle.

【Figure 4-4】La navigation commune après correction. Le travail est en haut, et les liens qui mènent à l'extérieur tout en bas *(L'écran est en japonais.)*

### 4-5 La fondation coûte $35 par mois

Le coût de base de données de l'ensemble de la fondation décrite dans ce chapitre est d'environ $35 par mois. Le forfait payant qui inclut le projet de production est à $25, et le projet de l'environnement de test à $10.

Ce n'était pas non plus le montant du début. À un moment, je payais $45 par mois. La base de données de développement d'un produit de reconnaissance faciale était toujours facturée alors que je ne m'en servais pas. Je l'ai passée au niveau gratuit en l'arrêtant, j'ai supprimé un autre projet inutilisé, et c'est ainsi que j'ai atteint le montant actuel.

Je surveille aussi le coût de l'IA. Le travail de l'IA qui écrit les programmes est facturé selon la quantité de jetons (l'unité de texte que l'IA lit et écrit). J'évite de concentrer les coûts en faisant tenir à la fenêtre de travail le rôle de coordination, et en laissant l'implémentation elle-même à une autre IA avec une enveloppe de coûts distincte. Pour le modèle génératif de la fenêtre de chat aussi, je regarde le prix et je choisis le nécessaire et suffisant. Même si un modèle de gamme supérieure ne coûte que $1 de plus par mois, je choisis en me demandant : « est-ce suffisant ? »

Si l'on construit petit, même de petites ventes peuvent suffire à faire vivre l'ensemble. L'histoire de la monétisation du chapitre 3 repose sur le faible coût de cette fondation.

### 4-6 L'IA de coordination, et la personne qui tranche

Pour finir, voici la forme de ma journée de travail.

Je garde plusieurs fenêtres de travail d'IA ouvertes en même temps. Il y a une fenêtre pour le système de réservation, une fenêtre par produit, et une fenêtre de coordination qui leur envoie les instructions et rassemble les résultats. J'ai nommé la fenêtre de coordination AgendaRegia (le carnet de coordination).

Les décisions, c'est-à-dire « dans quel sens aller », reviennent à moi et à l'IA côté chat. L'IA côté chat repère à l'avance les lacunes et les contradictions des spécifications, joint à chacune une décision par défaut et les propose toutes d'un coup. Je les lis et je décide. Ce qui est décidé est rassemblé dans une feuille d'instructions appelée Goal, collée dans la fenêtre de travail. Elle comprend des approbations préalables et des conditions de réussite qu'une machine peut juger. La fenêtre de travail la lit et va jusqu'au bout, en ne s'arrêtant qu'en cas d'échec.

Je fais aussi figurer dans la feuille d'instructions une estimation du moment où le travail sera terminé. Je glisse ce travail entre les heures d'ouverture du bar ; si je ne sais pas combien de temps une chose prendra, je ne peux pas planifier ma journée.

Le rôle de la direction n'est pas de lire, mais de décider. Je n'ai pas besoin de lire les 1775 journaux de conversation. Je réponds aux questions sur les faits du bar. Je tranche ce que seule la politique du bar peut décider. Une fois que quelque chose est en ligne, je le manipule moi-même cinq ou six fois pour voir si quelque chose cloche. C'est tout.

Avant d'arriver à cette forme, j'ai refait le travail bien des fois. L'IA ajoutait des fonctions de sa propre initiative et les écrans devenaient instables. Le travail enflait sans limite à partir d'une seule instruction. Attendre l'approbation à chaque étape empêchait tout progrès. À chaque fois, j'ai ajouté une règle, et c'est ainsi que l'on est arrivé à la forme actuelle. Cela aussi continue de se développer.

#### Ce que vous pouvez retenir de ce chapitre

- Pour un travail répété, mettez la procédure elle-même dans un document et confiez-la à l'IA. Si vous corrigez le manuel à chaque échec, la fois suivante devient plus facile
- Construisez les parties communes (connexion, facturation, navigation) une seule fois et réutilisez-les dans tous les produits. Si la fondation est petite, même de petites ventes peuvent suffire à vous faire vivre
- Les humains ne font que le jugement et les opérations que seuls les humains peuvent faire. Si l'IA vous confie autre chose, ajoutez-le au manuel

La suite de ce chapitre (les prochains carnets que je construis, et les leçons que j'ai ajoutées au manuel) se trouve sur note et X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Chapitre 5 : L'avenir d'un petit bar

### 5-1 De Zatta Gohan à Tamuro

J'ai fait mon entrée dans la restauration à 39 ans.

Le déclencheur a été un bar de quartier nommé Zatta. Une fois par mois, parfois toutes les deux semaines, on m'y laissait servir des repas. Pendant longtemps, j'avais appris la cuisine en autodidacte, mais j'avais désormais un lieu où des gens mangeaient ma cuisine et en étaient heureux. Telle fut mon expérience fondatrice.

En 2014, j'ai ouvert à Arai-Yakushi un restaurant appelé Zatta Gohan. C'était un petit lieu qui servait des menus du jour. Je l'ai tenu pendant sept ans.

À Arai-Yakushi, cependant, j'ai senti une limite au nombre de clients. J'ai alors trouvé un local à Higashi-Nakano. Il faut moins d'une minute à pied depuis la sortie est de la gare. Même par temps de pluie, on y arrive presque sans se mouiller.

En novembre 2018, j'y ai ouvert Tamuro. « Tamuro » désigne un endroit où les gens se rassemblent. Il compte 11 places au comptoir et 8 places sur tatami, soit 19 en tout. Pendant trois ans, j'ai tenu deux lieux en parallèle, Arai-Yakushi et Higashi-Nakano. Pendant la période du COVID, garder les deux est devenu difficile ; j'ai donc fermé l'établissement d'Arai-Yakushi et il ne m'est resté que Tamuro.

#### Le bar de curation

Tamuro se présente comme un « bar de curation ».

La curation, c'est avoir l'œil exigeant. Avant même de cuisiner, je veux faire de la curation. La cuisine, les boissons, l'atmosphère du bar : je fais tout en sélectionnant avec un œil exigeant. Voilà Tamuro.

Je voyage souvent pour manger, à l'étranger comme au Japon. Vietnam, Cambodge, Italie, Shanghai, Pékin, Mexique. Manger au fil des étapes est un plaisir et, en même temps, une façon de trouver quoi servir à Tamuro. Je recrée des ingrédients chers avec des ingrédients abordables. Par exemple, si l'on fait sécher un jaune d'œuf et qu'on le râpe, on obtient une saveur proche de la poutargue. Je considère ce genre de substitution (la localisation) comme mon rôle.

J'ai de nouveau étudié la cuisine pendant la période du COVID. J'ai suivi un cours de cuisine française de huit séances au total, et aussi un cours de cuisine japonaise. Comment gérer l'umami, et comment maîtriser la cuisson. Ce que j'y ai appris est le fondement de ma cuisine d'aujourd'hui.

Le menu de Tamuro se compose de quatre entrées et d'un plat principal. Je lui donne une variété d'ingrédients pour que les clients qui vivent seuls puissent manger beaucoup de légumes. Je le compose de façon que les modes de cuisson (frit, au vinaigre, mijoté, grillé) et les saveurs (sucré, épicé, acide) ne se recouvrent pas. Le plat le plus populaire est le tonteki, un steak de porc. Il est nappé d'une sauce légèrement sucrée à base de sauce soja de Kyushu, bien relevée à l'ail.

#### Un lieu où les gens se rassemblent

Environ la moitié de la clientèle de Tamuro vient seule. Ce sont surtout des personnes de 30 à 50 ans, dont beaucoup habitent le quartier de Higashi-Nakano, mais d'autres viennent des alentours d'Akabane, de Shinjuku, de Nishi-Ogikubo, d'Ogikubo et d'Eifukucho.

Ce qui distingue le bar, c'est à quel point les clients se parlent entre eux. J'ai conçu le comptoir pour qu'il soit facile de parler à la personne voisine, et l'équipe et moi décidons du placement en jugeant qui s'entendra bien. Les clients venus seuls reviennent parfois ensemble par la suite. Comme son nom l'indique, il est devenu un lieu où les gens se rassemblent. Je publie sur [Instagram](https://www.instagram.com/tamuro.higashinakano/) ce à quoi ressemblent les journées du bar.

Lors du dîner à thème organisé environ une fois par mois, je sers sept à huit plats en deux à trois heures, avec des accords de vins. Chaque mois, le thème change : italien, français, japonais. Les cours de cuisine sont des ateliers de trois heures, et après la cuisine, tout le monde trinque, mange et rentre chez soi. Il y a l'apéritif, avec du vin et de petites assiettes en début de soirée avant l'ouverture. Il y a un barbecue environ deux fois par an. Il y a une fête de fin d'année une fois par an. Et il y a la fête du yukata dont j'ai parlé au chapitre 1.

Le système de réservation dont j'ai parlé au chapitre 1, la fenêtre de chat et MCP sont tous des outils pour amener les gens à ce bar. L'IA est un moyen de rassembler les gens, pas le but.

### 5-2 Le curry au steak haché de Quatre Épices

Tamuro est un bar de nuit. En journée, le lieu est vide.

En profitant de ce temps, j'ai lancé Quatre Épices en janvier 2024. C'est une boutique de curry au steak haché qui ne fonctionne qu'au déjeuner dans le même lieu, et c'est l'équipe qui la tient.

Quatre Épices, ce sont littéralement quatre épices. Fidèle à son nom, plutôt que d'empiler beaucoup d'épices, on les choisit et on les restreint pour que le contour de la saveur soit net. Le curry n'utilise pas de farine ; il est lié uniquement par le velouté naturel des légumes et de la viande eux-mêmes. La satisfaction quand on a fini de manger, et aucune lourdeur à l'estomac. Et l'harmonie avec le steak haché. Je l'ai conçu autour de ces trois critères.

Nous sommes exigeants sur la cuisson du steak haché. Nous réglons le mélange pour qu'il sorte croustillant dehors et moelleux dedans, et nous cuisons en fonction de ce mélange. La maîtrise de la cuisson que j'ai apprise le soir à Tamuro sert aussi l'assiette du midi.

Les prix, les jours et les horaires d'ouverture peuvent changer ; pour les informations les plus récentes, consultez l'Instagram de Tamuro (https://www.instagram.com/tamuro.higashinakano/).

Quatre Épices tient aussi une cantine pour enfants dans le même lieu. C'est une activité qui utilise les installations et les achats du bar existant pour servir des repas aux enfants du quartier. Grâce à ce lien, nous avons aussi noué une relation avec le centre communautaire local. Nous servons parfois du curry et des sandwichs lors d'événements sportifs locaux, d'événements du centre communautaire et de fêtes de danse Bon.

Pour être honnête, l'usage des heures de la journée ne s'est pas entièrement bien passé. J'ai créé des journées pour boire un verre en journée et loué le lieu à d'autres personnes, mais la clientèle n'est pas venue comme je l'espérais. L'attrait du bar ne se perçoit pas de la même manière quand la direction est là le soir et quand seule l'équipe de jour est présente. Faire grandir la boutique de jour avec un attrait différent de celui de la boutique du soir reste une tâche inachevée.

### 5-3 Bonta LLC : deux piliers

La petite entreprise qui exploite Tamuro et Quatre Épices est Bonta LLC. J'en assure la gérance.

L'entreprise a deux piliers. L'un est la restauration et les boissons : Tamuro et Quatre Épices. L'autre est l'informatique : le développement de la série Agenda, et le conseil.

La restauration et les outils ne génèrent pas leurs revenus de la même façon. Faire tenir l'entreprise sur deux piliers de natures différentes est la forme que j'ai en tête.

Et les deux piliers se nourrissent mutuellement. Un problème au bar devient la graine d'un outil. Ce que j'apprends en construisant des outils revient dans la gestion du bar. Carnet de Lumière est né de fermetures qui se prolongent, et les enregistrements de prolongations issus de Carnet de Lumière deviennent la base des estimations de rentabilité et des plannings. Les « questions auxquelles nous n'avons pas su répondre » qui s'accumulent dans la fenêtre de chat améliorent l'accueil du bar. Ce cycle est la raison pour laquelle je peux gérer à la fois le bar et le développement tout seul.

Je ne pense pas agrandir l'entreprise. Petit, nombreux et bon marché. Voilà la forme de cette entreprise.

### 5-4 Écrire sous le nom de Raku Bonta

Quand j'écris et publie, j'utilise le pseudonyme « Raku Bonta ». J'ai écrit ce livre sous ce nom aussi.

Mon livre précédent, *L'adjoint IA*, portait sur l'IA générative. Il s'est classé numéro un dans la catégorie gestion du temps d'Amazon et a été lu par beaucoup de monde. Ce livre en est la suite.

Outre les livres, j'écris aussi sur note. J'y écris sur les efforts du bar avec l'IA, sur ce que j'ai trouvé lors d'un voyage de formation, sur l'avancement de la publication de mes livres et sur la série Agenda. Vous pouvez suivre sur note (https://note.com/bontallc) la suite que je n'ai pas pu faire tenir dans ce livre.

Pour moi, écrire est aussi une façon de mettre en mots à la fois le bar et le développement, et de les vérifier. Comme je l'ai écrit au chapitre 1, les premières connaissances de la fenêtre de chat « T-AI-MURO » ont été construites à partir de mots que je laissais sur X. Ce que j'avais écrit est devenu matière pour l'IA. À l'avenir aussi, ce que j'écrirai reviendra au bar comme à l'IA.

Il y a encore une chose que j'ai décidée au sujet de l'écriture. Je n'annonce pas les choses inachevées par un « bientôt disponible ». Je termine, je fabrique une page de présentation, et seulement alors je publie. Je crois que respecter cet ordre est ce qui fait gagner la confiance à une petite entreprise.

### 5-5 L'avenir de l'établissement indépendant

Pour finir, je vais rassembler ce que j'ai écrit dans ce livre en un seul tableau.

【Figure 5-1】Vue d'ensemble de ce que décrit ce livre. Un petit bar ouvre sa propre fenêtre (la première histoire), et transforme ses problèmes en outils à remettre à d'autres bars (la seconde histoire) *(L'écran est en japonais.)*

La clientèle va se mettre à faire chercher un bar et faire la réservation par sa propre IA. En août 2026, il est devenu possible de réserver des restaurants depuis ChatGPT via un grand service de réservation. Le point d'entrée se déplace des moteurs de recherche et des sites d'avis sur les restaurants vers l'IA personnelle de chacun.

À ce moment-là, un bar qui ne figure pas sur les grands services de réservation est invisible pour l'IA. Mais même si l'on n'est pas sur les grands services, il existe une voie pour qu'un bar se connecte directement à l'IA. Tamuro a choisi cette voie en ouvrant une fenêtre appelée MCP. Un petit bar qui ouvre lui-même sa propre fenêtre. C'est la première histoire de ce livre.

Les propriétaires de bar pourront transformer leurs propres problèmes en outils et les distribuer à d'autres bars. Carnet de Lumière est né du souci de Tamuro de vouloir dire que la fermeture allait déborder, et il peut s'utiliser dans n'importe quel bar. Le pouvoir de construire cesse peu à peu d'être réservé à certaines personnes ou entreprises. La direction d'un petit bar passe du côté de ceux qui utilisent les outils à celui de ceux qui les construisent et les distribuent. C'est la seconde histoire de ce livre.

Ce que ces deux histoires ont en commun, c'est que plus un bar est petit, plus il peut affirmer sa singularité.

Les grandes chaînes généralisent leurs systèmes pour que chaque point de vente offre la même qualité. Tamuro est l'inverse. Les clients seuls en forment la moitié, près de 90 % des réservations se font le jour même, et les clients se parlent entre eux. Pour correspondre à ce caractère de Tamuro, j'ai construit dans le détail le système de réservation, les remises et la fenêtre de chat. Parce qu'il ne généralise pas, il affirme sa singularité. Parce qu'il affirme sa singularité, il devient une raison pour la clientèle de le choisir.

Et plus un bar affirme sa singularité, plus il trouve de graines d'outils. Plus on se confronte au caractère du bar, plus les problèmes deviennent précis. Des problèmes précis deviennent des outils précis. Des outils précis aident d'autres bars qui ont le même problème.

L'IA a rendu possible pour une seule personne de faire les deux. Affirmer la singularité du bar, et distribuer des outils. Autrefois, il fallait choisir l'un ou l'autre. Aujourd'hui, on peut faire les deux.

Bien sûr, tout cela reste en cours de construction. Le taux de réussite de la fenêtre de chat continue d'être relevé. Le manuel s'enrichit à chaque échec. La manière de faire grandir la boutique de jour reste un défi. Les personnes qui réservent par l'IA ne sont toujours pas nombreuses.

Malgré tout, je crois que l'avenir du petit bar est radieux. Être petit n'est pas une faiblesse. Parce que nous sommes petits, nous pouvons tester vite, abandonner vite et corriger vite. Parce que nous sommes petits, nous pouvons affirmer notre singularité. Et les problèmes d'un bar à la singularité affirmée deviennent des outils et se transmettent à d'autres petits bars.

J'ai écrit ce livre depuis un bar de 19 places à Higashi-Nakano.

## Postface

Merci de m'avoir lu jusqu'ici.

Ce que j'ai écrit dans ce livre est un état des lieux arrêté à octobre 2026. Les outils d'IA changent de forme en quelques mois. Certains des mécanismes que j'ai décrits auront peut-être déjà pris une autre forme au moment de la publication. Malgré tout, je l'ai écrit, en pensant que le récit de ce qu'un petit bar a construit avec l'IA, de la manière dont il s'y est pris, de ses échecs et des leçons qu'il en a tirées devrait rester utile un certain temps.

La série Agenda : https://bontallc.com/agenda?via=b2-fr-{{FMT}}

Suivre mes activités : note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Si vous passez un jour par Higashi-Nakano, venez faire un tour chez Tamuro. Vous pouvez réserver par le site de réservation, par la fenêtre de chat « T-AI-MURO » du site, et bien sûr par votre propre IA.

Site de réservation de Tamuro : https://tamuroreservation.vercel.app/?src=b2-fr-{{FMT}}

Instagram de Tamuro : https://www.instagram.com/tamuro.higashinakano/

Pour celles et ceux qui veulent essayer de réserver depuis l'IA. L'adresse de connexion du serveur MCP de Tamuro est l'URL suivante.

https://tamuroreservation.vercel.app/api/mcp

Dans les réglages de votre IA (comme Claude ou ChatGPT), ouvrez l'écran d'ajout d'outils externes (connecteurs, serveurs MCP) et enregistrez cette URL. La façon de l'enregistrer varie selon l'IA et au fil du temps ; le plus sûr est donc de chercher « MCP » ou « connecteur » dans l'aide de chaque IA. Selon votre forfait, il se peut que vous ne puissiez pas connecter un serveur MCP de votre choix. Une fois l'enregistrement fait, demandez à votre IA : « Y a-t-il de la place chez Tamuro ce soir ? » Elle vérifiera les créneaux libres et les prix, et vous guidera vers la page de réservation. C'est vous qui appuyez sur le bouton de confirmation.

Pour celles et ceux qui viennent après avoir lu le livre. Au moment de réserver, saisissez le code promo « BOOK ». Votre premier verre vous sera offert. Si vous venez sans avoir réservé, dites simplement « j'ai vu le livre » en passant votre première commande. Il vous sera offert de la même façon. C'est un petit dispositif qui me permet de compter combien de personnes sont venues grâce au livre.

Vous pouvez venir sans réservation. Même en venant sans compagnie, vous ne vous sentirez pas à l'écart. La conversation s'engagera peut-être tout naturellement avec la personne à côté de vous.

Je vous attends dans un bar où les gens se rassemblent.

Raku Bonta

### Références

- OpenAI Help Center, « ChatGPT — Release Notes », 10 août 2026, « Restaurant reservations in ChatGPT » https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, « Alpaca MCP Server » (un exemple de serveur MCP aux États-Unis qui permet à l'IA de passer des ordres d'achat d'actions et d'autres titres) https://docs.alpaca.markets/docs/alpaca-mcp-server
- Le débat sur la « mort du SaaS » : les propos de Satya Nadella dans le podcast BG2 (décembre 2024), la forte chute des actions des éditeurs de logiciels en février 2026 et son appellation, ainsi que la réfutation de Jensen Huang, ont été tirés des reportages et commentaires suivants. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
