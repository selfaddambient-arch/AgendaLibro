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

