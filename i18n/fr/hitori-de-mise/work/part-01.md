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

