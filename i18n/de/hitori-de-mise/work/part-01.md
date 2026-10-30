## Einleitung

Dieses Buch hält den Stand von Januar 2026 fest. Manches an der Art, wie ich mein Lokal führe, und einige Namen und Funktionen der KI-Werkzeuge haben sich seither geändert. Die Fortsetzung, *Gebaut für unsere Bar*, erzählt die Geschichte weiter.

### Warum ein ehemaliger Systemmensch in einem Kellerlokal mit KI spricht

Schön, dass Sie dieses Buch in die Hand genommen haben.

*Eine Person führt das Lokal, und die KI setzt sich dazu.*

Beim Lesen dieses Titels denken manche von Ihnen vielleicht: „Das bin ja genau ich.“ Andere fragen sich: „Was heißt das, die KI setzt sich dazu?“

Dies ist kein Fachbuch über schwieriges Programmieren. Es ist ein Buch für Menschen wie Sie, die ein Lokal führen, jeden Tag in der Küche stehen, die Vorbereitungen treffen und alle Hände voll mit den Gästen zu tun haben.

Ein paar Worte zu mir.

Ich führe heute ein kleines Lokal im Untergeschoss eines Gebäudes in Higashi-Nakano *(ein Wohnviertel im Westen Tokios, gleich westlich von Shinjuku)*, Tokio.

Das Lokal hat zwei Gesichter. Tagsüber ist es ein Spezialitätenlokal für Hamburger-Curry mit dem Duft vieler Gewürze. Abends wird es zu einer Esskneipe, in die man nur auf Empfehlung kommt, mit einem täglich wechselnden Menü und Getränken.

▼ Quatre Epice Hamburger Curry (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry (Instagram)](images/fig-01.png)

▼ Bar „Tamuro“, nur auf Empfehlung (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Bar „Tamuro“, nur auf Empfehlung (Instagram)](images/fig-02.png)

Es ist ein gemütlicher Raum mit nur 11 Plätzen am Tresen und 8 Plätzen auf einem erhöhten Tatami-Podest.

Doch bei uns gibt es nicht nur Essen.

Alle zwei Wochen veranstalte ich einen Weinabend, und einmal im Monat plane ich einen Kochkurs oder einen besonderen Menütag. Auch in einem engen Keller bin ich jeden Tag beschäftigt und in Bewegung.

Ich führe das Lokal nun schon im zwölften Jahr.

Davor habe ich als angestellte Person in einer Firma gearbeitet. Meine Aufgabe war „Systemplanung“ und „Lösungsarchitektur“.

Wenn ich das erzähle, sagen manche: „Sie haben also beeindruckende Systeme entwickelt.“ So war es aber nicht.

Ich habe keinen schwierigen Programmcode geschrieben. Ich habe zugehört, was die Menschen vor Ort brauchten, es genau an IT-Dienstleister (Entwicklungsfirmen) weitergegeben und es bauen lassen. Ich übernahm die Rolle der „Koordination“. In Japan nennt man diese Rolle „Systemmensch“.

Die Leute vor Ort wünschten sich: „Meine Arbeit soll leichter werden.“ Die Entwicklung sagte: „Wir brauchen logisch definierte Anforderungen.“

Meine Aufgabe war es, zwischen beiden zu stehen, die Sprache der einen Seite für die andere zu übersetzen und alle ans Ziel zu führen.

Deshalb verstehe ich die Unannehmlichkeiten und Sorgen von Menschen wie Ihnen, die Systeme nutzen, und ich verstehe auch ein wenig, was auf der IT-Seite gedacht wird.

Vor zwölf Jahren habe ich die Firma verlassen und mein eigenes Lokal eröffnet. Seitdem kenne ich dieselben Sorgen wie Sie.

Vorbereitung, die nie endet, Personalmangel, die Sorge, ob genug Gäste kommen, und Entscheidungen, die ich allein trage ...

Wenn viel los ist, helfen mir natürlich manchmal verlässliche Teilzeitkräfte und Aushilfen.

Aber sie sind letztlich Partner für „Aufgaben“.

Für schwere „Entscheidungen der Unternehmensführung“ wie „Wie gehe ich im nächsten Monat mit der Liquidität um?“ oder „Soll ich auf dieses neue Gericht setzen?“ gibt es niemanden, den ich fragen könnte.

Ich mache mir Sorgen, entscheide und trage die volle Verantwortung. In diesem Sinne habe ich das Lokal immer „allein geführt“. Und was mir als Vertraute für mein einsames Ich an der Spitze des Lokals zur Seite saß, war die KI.

In dieser Lage trat die generative KI in mein Leben, und vor allem ein Partner namens „Google Gemini“.

Die „Koordination“, die ich früher zwischen „der Praxis“ und „IT-Dienstleistern“ geleistet habe, mache ich jetzt selbst zwischen „den Problemen des Lokals“ und „der KI“. Und dabei ist mir etwas klar geworden.

Sie müssen die Schreibweise schwieriger Programmiersprachen (wie Python) nicht auswendig lernen.\
Das weiß die KI. Aber den Bauplan davon, „was erledigt werden soll und in welcher Reihenfolge“, kann nur ein Mensch zeichnen.\
Was ich als Systemmensch aufgebaut habe, war genau diese „Fähigkeit, die Wünsche der Praxis in logische Schritte zu übersetzen“.\
In diesem Buch gebe ich nicht nur weiter, wie man die KI bedient, sondern auch dieses „logische Gespür, um eine KI zu steuern (Systemdenken)“, und halte nichts zurück.\
Wenn Sie es haben, können Sie schon „ohne Vorwissen“ der KI die besten Aufträge erteilen, die es gibt.

※ Eines möchte ich hier ehrlich sagen.

Ich bin ein ehemaliger Systemmensch. Aber bei den in diesem Buch vorgestellten Einsatzweisen der KI gab es tatsächlich kaum Momente, in denen mir das Wissen aus meinem früheren Beruf direkt geholfen hat.

Geholfen hat nicht „die Fähigkeit, Programme zu schreiben“.\
Es war allein „die Gewohnheit, den diffusen Frust im Arbeitsalltag in Schritte mit einer klaren Reihenfolge zu fassen“.

Und diese Gewohnheit ist keine besondere Begabung.\
Es ist „ein Gespür, das alle schon haben, die ein Lokal jeden Tag führen“.

In diesem Buch trenne ich bewusst, was nur ich konnte,\
von dem, was Sie schon heute eins zu eins übernehmen können.

## Kapitel 1: Konzepte - KI-Agenten, die neue Art von Mitarbeitenden

~ Stellen Sie die KI als „Arbeitspartner“ ein, nicht als bloßen „Gesprächspartner“ ~

### 1-1. Die Grenzen des Alleinbetriebs und Missverständnisse über KI

Ein eigenständiges Restaurant wie unseres zu führen, ist ein ständiger Wettlauf gegen die Zeit. Vorbereitung, Kochen, Servieren, Kassieren, Putzen ... das alles muss von einer Person oder einem kleinen Team bewältigt werden.\
Selbst wenn wir Personal einstellen, führen wir als unabhängige Lokale faktisch einen „Ein-Personen-Betrieb“.

Denn wir haben keine „Filialleitungen“ oder „Ausbildende“ wie die großen Ketten.

Sie kochen und geben dabei dem Service Anweisungen, lernen neue Kräfte an und planen die Dienste.

All diese „gedankliche Arbeit“ konzentriert sich auf eine einzige Person: auf Sie.

Sie bekommen vielleicht mehr Hände, aber Sie haben immer noch nur einen Kopf. Genau deshalb brauchen Sie die KI als Unterstützung für diesen „Kopf“.

„Hätte ich doch nur eine gute Kraft mehr ...“

Diesen Gedanken haben Sie bestimmt mehrmals am Tag.

Wenn ich sage: „Nutzen wir doch KI“, antworten viele, die ein Lokal führen, etwa so:

„Sie meinen ChatGPT? Ich habe es probiert, aber das schreibt ja nur Texte, oder? Für die Arbeit im Lokal taugt das nicht.“

Hier liegt tatsächlich ein großes Missverständnis.

Die meiste KI, mit der wir bisher zu tun hatten, war ein „Chatbot (ein Gesprächspartner)“. Was die neueste KI, allen voran Google Gemini, jetzt anstrebt, ist aber die Form eines „KI-Agenten (eines Arbeitspartners)“.

Beide wirken auf den ersten Blick ähnlich, sind aber grundverschieden. Vergleichen wir sie an einer konkreten Aufgabe.

### 1-2. Vom „Wörterbuch“ zur „Fachkraft“

Angenommen, Sie möchten ein Plakat für eine Veranstaltung im Lokal gestalten.

Mit der KI von früher (einem Chatbot):

Wenn Sie fragen: „Sagen Sie mir, wie man ein Plakat macht“, erklärt die KI die Schritte wie ein Wörterbuch oder Lehrbuch: „Halten Sie den Slogan kurz“, „Wählen Sie die Farben so aus.“

Aber wer das Plakat tatsächlich mit den eigenen Händen macht, sind Sie. Ihr Wissen ist gewachsen, Ihre Arbeitszeit aber nicht kürzer geworden.

Mit der KI der Zukunft (einem KI-Agenten):

Sie sagen einfach: „Mach ein Plakat.“

Dann überlegt die KI selbst, wie sie das Ziel erreicht. Sie denkt sich den Slogan aus, erzeugt das Hintergrundbild und schlägt sogar das Layout vor.

Wie eine hervorragende Fachkraft setzt sie Werkzeuge ein, plant und führt die Arbeit selbstständig aus.

Was wir wollen, ist keine beratende Instanz, die nur kluge Ratschläge erteilt, sondern ein Partner, der an unserer Seite mit anpackt.

※ In diesem Buch nenne ich diesen verlässlichen Partner (generative KI wie Google Gemini) liebevoll die „Stellvertretung (KI)“.

※ In diesem Buch verwende ich als Beispiel „Google Gemini“, das ich hauptsächlich nutze. Die meisten hier vorgestellten Ideen lassen sich aber mit anderer generativer KI wie ChatGPT und Claude fast genauso umsetzen.

Wichtig ist nicht der Name des Werkzeugs, sondern „die Haltung, die KI nicht als bloßen Gesprächspartner, sondern als Partner zu behandeln, dem man Arbeit übergeben kann“.

### 1-3. „Multimodal“ wird Restaurants retten

Es gibt noch ein weiteres Schlagwort, das für den Restaurantbetrieb entscheidend ist. Es lautet „multimodal“.

Das Wort klingt etwas technisch, die Bedeutung ist aber einfach.

Es heißt: „mehrere Arten von Information gleichzeitig verstehen zu können, nicht nur Text (Lesen und Schreiben), sondern auch Bilder (Sehen und Zeichnen) und Ton (Hören und Sprechen)“.

Herkömmliche KI konnte nur „Text“ verstehen. Doch ein Restaurantbetrieb läuft nicht allein über „Text“.

- Wie die Lebensmittel im Kühlschrank aussehen

- Die Handschrift auf Bestellzetteln

- Die Stimmen der Gäste und die Stimmung im Raum

- Das Etikettendesign auf einer Weinflasche

All das sind „nichtsprachliche Informationen“, die mühsam in Worte zu fassen sind.

Die Stellvertretung (KI) kann sie ebenso erkennen wie ein Mensch.

Wenn Sie mit dem Smartphone ein Foto vom Inneren Ihres Kühlschranks machen und es zeigen, erkennt die KI: „Ah, von diesem Gemüse und diesem Fleisch ist noch etwas übrig“, und kann daraus ein Menü entwickeln.

Mit anderen Worten: Die heutige KI ist „eine hervorragende Stellvertretung, die sehen, hören und sprechen kann“.

※ Eines sollten Sie aber nicht missverstehen.\
KI ist besser darin, Dinge zu sagen, die plausibel klingen, als Dinge zu sagen, die richtig sind. Bei Bilderkennung, Zahlen, Datumsangaben und Eigennamen\
nutzen Sie sie bitte unter der Voraussetzung, dass immer ein Mensch die letzte Prüfung übernimmt.

Der Grund, warum die KI in diesem Buch gut funktioniert,\
ist, dass ich „nicht alles aus der Hand gebe und immer vor Ort nachprüfe“.

### 1-4. Das „Bauchgefühl“ mit Daten untermauern

Große Ketten haben riesige Mengen an Kassendaten (POS) und Marketingteams.

Wer ein unabhängiges Lokal führt, hat dagegen sein „Bauchgefühl“ und seine „Erfahrung“. Das ist die stärkste Waffe, kann aber manchmal dazu führen, dass man sich verrennt oder ins Zweifeln gerät.

Holen wir also eine „Stellvertretung“ dazu.

Lassen Sie die KI Ihre Intuition (Ihr Bauchgefühl) „Ich glaube, die Gäste werden dieses Gericht lieben“ mit „Verkaufsdaten aus der Vergangenheit“ und „Trendinformationen“ vergleichen.

So behalten Sie die „Wärme“ und die „persönliche Note“, die nur ein unabhängiges Lokal hat, und führen trotzdem einen starken Betrieb auf Grundlage von Daten.

## Kapitel 2: Grundlagen - „Vibe Coding“ ohne Vorwissen

~ Programme „schreibt“ man nicht. Man „lässt sie von der KI im Gespräch bauen“. ~

