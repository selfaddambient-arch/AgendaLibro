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

