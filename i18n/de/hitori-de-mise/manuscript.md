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

### 2-1. Niemand liest eine „lange LINE-Nachricht“. Die Magie eines „Schaubilds“ in nur 30 Sekunden

Zu sagen „Bauen Sie mit KI ein System“, fühlt sich vielleicht noch wie eine ziemlich hohe Hürde an.

Beginnen wir deshalb mit einer vertrauteren „Art, KI zu nutzen“, die Sie schon heute sofort einsetzen können.

Es ist eine Revolution beim „Erteilen von Anweisungen an das Team“.

Viele von uns, die ein Lokal führen, benutzen LINE *(Japans meistgenutzte Messaging-App)*, um das Personal zu erreichen.\
Ich führe das Lokal meist mit wenigen Leuten, und im Trubel des Services bleibt keine Zeit, in Ruhe Anweisungen zu geben.

So hängen Mitteilungen zwangsläufig von LINE-Nachrichten nach Feierabend ab.

Es ist aber extrem schwer, das Bild von „so soll es gemacht werden“, das nur in meinem eigenen Kopf existiert, allein mit Worten an weniger erfahrenes Personal oder an gelegentliche Aushilfen zu vermitteln.

Daher kommt die „lange LINE-Nachricht“.

Je sorgfältiger man zu erklären versucht, desto länger wird der Text, und das Ergebnis ist ...

„Oh, tut mir leid, so weit habe ich nicht gelesen.“

„Es war nur Text, und ich konnte nicht erkennen, welcher Teil wichtig ist.“

Kommen solche Fehler nicht auch bei Ihnen im Lokal vor?

Bei mir auch.

Eines Tages wollte ich für eine App, die ich entwickelte, eine Person aus dem Team bitten, „Fotos von Zutaten“ zu machen.

Die Bedingungen waren etwas kompliziert, und so wurde die Anweisung, die ich auf dem Smartphone tippte, zu einer langen Nachricht wie dieser.

![Die lange LINE-Nachricht, die ich tatsächlich ans Team geschickt habe, samt Tippfehlern](images/fig-03.jpg)

Selbst wenn sie das sehen, überfliegen beschäftigte Küchenkräfte es mit „Im Grunde soll ich also nur Fotos machen, oder?“ und übersehen die Vorgaben zu „Winkel“ und „Ausrichtung des Behälters“.

Ich habe aber keine Zeit, PowerPoint zu öffnen, Formen auszurichten und ein Anweisungsblatt zu erstellen.

Also habe ich diesen Text unverändert in eine KI gegeben (ein KI-Werkzeug wie Manus oder Gemini) und gebeten:

„Fasse den Inhalt dieses Textes auf einer Folie zusammen, als ‚Arbeitsanweisung‘, die das Personal auf einen Blick versteht.“

### 2-2. KI ist eine „hervorragende Übersetzungskraft“

Nach wenigen Sekunden Wartezeit hatte die KI eine überraschend gut verständliche „Diagramm-Folie“ erzeugt.

![Die von der KI automatisch erstellte Folie „Arbeitsanweisung zu Datenerfassung und Fotografie“](images/fig-04.jpg)

Ich habe nichts gestaltet. Ich habe nur gesagt: „Hier ist der Text, fass ihn zusammen.“

Aus meinem ausufernden Text erfasste die KI sofort, „was wichtig ist“ und „wie es einzuordnen ist“, und „übersetzte“ es in ein Layout, das Menschen intuitiv erfassen.

### 2-3. Befreit vom „Stress, nicht durchzudringen“

Ich habe dieses Bild in LINE eingefügt und abgeschickt.

Die Wirkung war sofort da.

Die Person aus dem Team stellte keine Rückfragen und schickte gleich beim ersten Mal perfekte Fotodaten im „Hochformat“ aus „3 Winkeln“ zurück.

Bis dahin hatte ich mich über das Personal geärgert, mit dem Gedanken „Warum lesen sie es nicht?“, und mir Sorgen gemacht: „Vielleicht erkläre ich es einfach schlecht.“

Aber schuld waren weder das Team noch ich. Schuld war die „Verständigung allein mit Text“.

Diese Erfahrung hat meinen Blick auf die KI verändert.

KI ist nicht nur ein Werkzeug, um neue Texte und Bilder „von Grund auf zu erschaffen“.

Sie ist „ein Werkzeug, das unsere ‚schwer vermittelbaren Worte‘ in eine Form ‚umwandelt‘, die beim Gegenüber auch ankommt“.

### 2-4. „Vibe Coding“, eine neue Art des Dialogs

Wenn Sie sich an Gespräche mit der KI gewöhnt haben, kommt als Nächstes endlich das „Werkzeuge bauen“.

Sie denken vielleicht: „Programmieren ist nichts für mich“, aber keine Sorge.

Unter Entwicklungsfachleuten ist derzeit ein Begriff namens „Vibe Coding“ ein heißes Thema.

Es ist eine Methode, bei der nicht Menschen schwierigen Code schreiben, sondern ein System im Gespräch mit der KI entsteht, als würde man sich auf die „Vibes“ (Gefühl und Stimmung) einstimmen.

Sota Fujii, Meister (Titelträger) im Shōgi, nannte „Vibe Coding“ als etwas, wofür sich Fujii in diesem Jahr, 2025, begeistert hat. Selbst jemand aus der Shōgi-Welt, die mit dem Bauen von Systemen scheinbar nichts zu tun hat, sagt der KI, wie es heißt, auf Japanisch, was gewünscht ist, und baut sich praktische Werkzeuge.

Im Gespräch mit der KI können auch wir Systeme ohne Fachwissen bauen.

Sie benutzen nur Ihre Alltagssprache (bei mir: „Japanisch“). Wenn Sie sagen: „Ich möchte, dass es so funktioniert“ oder „Diese Stelle ist schwer zu bedienen“, schreibt die Stellvertretung (KI) im Hintergrund den Code.

Mit anderen Worten: Sie müssen nicht zur „Programmierfachkraft“ werden.

Sie müssen nur zur „Bauleitung“ werden, die einer „hervorragenden Entwicklungsfachkraft (KI)“ Anweisungen gibt.

### 2-5. Die „Beschwerden“ aus Ihrem Lokal sind die stärksten Prompts

Anweisungen an die KI (Prompts) brauchen keine schicken Worte.

Der stärkste Prompt, den ich entdeckt habe, sind „die ‚Unannehmlichkeiten‘ und der ‚Frust‘ in Ihrem Lokal, also Ihre Beschwerden“.

- „Diese Berechnung jeden Tag zu machen, ist lästig.“

- „Ich möchte Bilder nicht von Hand in der Größe ändern.“

Für die KI sind das völlig brauchbare „Anforderungen an die Entwicklung“.

Ein Gefühl wie „Das nervt mich“ lockt leichter eine konkrete Lösung hervor als ein Ziel wie „Ich möchte das tun“.

### 2-6. Ein Fehler ist kein „Misserfolg“. Er ist der „Beginn eines Dialogs“.

Wenn Sie anfangen, mit KI etwas zu bauen, werden Sie ganz sicher auf einen „Fehler“ stoßen.

Beim Vibe Coding ist ein Fehler aber kein Misserfolg.

Er ist „das Signal, dass ein Ballwechsel mit der KI begonnen hat“.

Selbst unter Menschen kommt die eigene Absicht selten gleich beim ersten Mal perfekt an.

Wenn die KI einen Fehler meldet, wischen Sie ihn einfach leicht mit „Ah, das ist nicht angekommen“ beiseite und fragen zurück: „Nein, ich möchte Folgendes.“

Halten Sie den Ballwechsel am Laufen, ohne aufzugeben. Wenn Sie nur das schaffen, können auch Sie ohne Vorwissen ganz sicher „ein System bauen, das nur Ihres ist“.

### 2-7. Die Effizienz mit „physischen Tasten“ drastisch steigern - eine Zusatztastatur nutzen

Beim Vibe Coding ist das Wichtigste, „Wert auf die Eingabe zu legen“.

Je schneller Ihr Gespräch mit der KI wird, desto weniger stockt das Denken und desto schneller geht die Entwicklung voran. Umgekehrt kann selbst eine großartige Idee verschwinden, wenn Sie sich bei der Eingabe verheddern.

Vorhin habe ich Ihnen gesagt: „Wenn ein Fehler erscheint, ist das Richtige, einen Screenshot zu machen und ihn einzufügen.“

Aber dutzende Male am Tag [Windows] + [Shift] + [S] (Mac: [Cmd] + [Shift] + [4]) zu drücken, mit der Maus einen Bereich auszuwählen, zum Gemini-Fenster zurückzugehen und [Strg] + [V] (Mac: [Cmd] + [V]) zu drücken ...

Ehrlich gesagt, das ermüdet die Finger, nicht wahr?

Deshalb habe ich mir eine „Zusatztastatur mit 6 Tasten“ zugelegt.

Es ist eine kleine, in China hergestellte Tastatur, die ein paar hundert bis rund tausend Yen kostet und auftaucht, wenn Sie bei Amazon oder ähnlichen Seiten nach „programmierbare Tastatur“ suchen.

![Ein Foto der Zusatztastatur mit 6 Tasten, die ich benutze](images/fig-05.jpg)

Diesen sechs Tasten habe ich die folgenden Kurzbefehle zugewiesen.

1.  Screenshot starten

2.  Alles auswählen (Strg + A; Mac: Cmd + A)

3.  Kopieren (Strg + C; Mac: Cmd + C)

4.  Einfügen (Strg + V; Mac: Cmd + V)

5.  Eingabetaste (Senden)

6.  (Reserve)

Das ist alles. Aber die Wirkung ist drastisch.

Ein Fehler erscheint.

↓

Mit der linken Hand tippe ich auf „Taste 1 (Screenshot)“.

↓

Ich wähle den Bereich aus und tippe dann im Gemini-Fenster auf „Taste 4 (Einfügen)“.

↓

Tippen auf „Taste 5 (Senden)“.

All das dauert nur 2 Sekunden.

Sie müssen sich keine Tastenkürzel merken und Ihre Finger nicht kompliziert bewegen.

Sie können der KI Informationen zuwerfen, als würden Sie einen Game-Controller bedienen.

Wie Sie in späteren Kapiteln sehen werden, ist es praktisch: Wenn Sie den von der KI ausgegebenen Quellcode korrigieren, können Sie ihn mit Alles auswählen (Strg + A), Kopieren (Strg + C) und Einfügen (Strg + V) sofort wieder ausführen.

Bevor Sie sich fortgeschrittenes Programmierwissen aneignen, versuchen Sie bitte zuerst, sich dieses eine kleine Gerät zu besorgen.

Den „Aufwand der Eingabe“ physisch aus dem Weg zu räumen, ist die sicherste Abkürzung, um Gespräche mit Ihrer KI zu beschleunigen.

## Kapitel 3: Praxis 1 - Kreative Arbeit automatisieren und Gäste gewinnen

~ „Einen Screenshot einfügen und alles übergeben“ erwies sich als stärkste Entwicklungsmethode ~

### 3-1. Versuch und Irrtum, um den „KI-Look“ auszutreiben (LINE-Sticker)

Nachdem ich mich an den Dialog in Textform (Vibe Coding) gewöhnt hatte, wollte ich mich endlich an die „Bilderzeugung“ wagen.

Als Praxisprojekt wählte ich die Herstellung von „LINE-Stickern“, die auch helfen können, einen Kreis von Fans für das Lokal aufzubauen.

Doch die „glatten, CG-artigen Bilder“, die für KI-erzeugte Bilder typisch sind, passen nicht zur Atmosphäre meines Lokals.

Mir schwebte „ein Retro-Flat-Design im Stil der 1980er mit handgezeichneter Anmutung vor, das die Textur von Wachsmalstift und Pinsel bewahrt“.

Von da an begann ein langer „Dialog“ zwischen mir und der Stellvertretung (KI).

Zuerst begann ich mit Figuren von „zwei Jungen und einem Shiba Inu“.

„Gib mir 25 Muster für Alltagsgespräche.“

„Mach die Linienstärke zufällig, wie bei Pinselstrichen.“

Eins nach dem anderen, wie bei Korrekturanweisungen an eine menschliche Illustrationsfachkraft, brachte ich der KI geduldig den Geschmack bei, der mir gefällt.

![Für LINE-Sticker erzeugte Illustrationen](images/fig-06.png)

### 3-2. Die kühne Bitte: „Nur den Hund in eine Katze verwandeln“

Als die Sache etwas Gestalt angenommen hatte, entschied ich mich für eine große Kursänderung: „Eigentlich möchte ich Mädchen und eine Katze.“

Eine gewöhnliche illustrierende Person hätte wohl das Gesicht verzogen und gesagt: „Was, noch mal von vorn?“ Aber die Stellvertretung (KI) hat kein einziges Mal gemeckert.

„Ändere die Figuren in zwei Mädchen, eines mit langen und eines mit kurzen Haaren. Kleidung in Gelb und Grün, im selben handgezeichneten Stil wie zuvor.“

„Verwandle den Hund in eine Katze, tausche die Worte gegen die Katzensprache aus, die du vorhin erzeugt hast, und mach passende Posen.“

„Mach die Katze zu einer Siamkatze, nicht zu einer rot getigerten Katze.“

Obendrein stellte ich eine Bitte, die die Grenzen der KI austestete.

„Behalte die Komposition der ‚Jungen und des Shiba Inu‘, die du vorhin gemacht hast, genau bei und ersetze nur den Hund durch eine Siamkatze.“

Zu meiner Überraschung verstand die KI diese komplizierte Anweisung. Die Positionen und Posen der Jungen blieben gleich, während der Hund sauber durch eine „Siamkatze“ ersetzt wurde.

![Das fertige Illustrationsblatt für LINE-Sticker](images/fig-07.png)

Um sie jedoch als Sticker in LINE zu verwenden, müssen Sie die Illustrationen aufteilen, Vorschaubilder erstellen, alles in eine ZIP-Datei packen und hochladen.

Auch das lässt sich im Dialog mit Gemini erledigen, aber ich erkläre es später noch einmal in 3-6. Die erste Hürde: einfaches Aufteilen und die „Bildqualitätsfalle“.

### 3-3. Fall 2: Das „Weihnachtsbanner“ aus 22 Dialogrunden

Nach den LINE-Stickern gibt es noch ein größeres Werk, das ich Hand in Hand mit der KI geschaffen habe. Es ist das Ankündigungsbanner für das „Weihnachtsessen“, die größte Veranstaltung des Jahres für das Lokal.

Ich habe eine KI namens „Nano Banana“ verwendet (das in Googles Gemini eingebaute Modell zur Bilderzeugung).

#### Phase 1: Layout und Text anpassen

Zuerst platzierte ich die nötigen Elemente (Weihnachtsmann, Rentiere, Textinformationen) auf einer breiten Fläche.

Ich sah mir die entstandenen Bilder an und gab Anweisungen.

„Es wirkt ein bisschen leer. Füge Illustrationen eines Weihnachtsbaums und von Champagner hinzu.“

„Das Menü ist eine Aufzählung und schwer lesbar. Fasse es als ‚insgesamt sechs Gänge‘ zusammen und mach den Titel größer und auffälliger.“

![Das Bild aus der frühen Phase. Wirkt noch etwas leer](images/fig-08.png)

#### Phase 2: Die „Lebendigkeit“ abstimmen

Als das Layout stand, kam als Nächstes die Atmosphäre. Es fehlte das „Partygefühl“.

Ich wies an: „Mach es lebendiger! Verteile viele kleine Weihnachtsmänner und Rentiere, Luftballons und Konfetti.“

Diesmal wurde das Bild viel zu überladen.

„Entschuldigung, das waren zu viele Elemente. Reduziere die Figuren erst einmal und mach es aufgeräumt.“

Dieses Feinjustieren durch „Hinzufügen und Weglassen“ beliebig oft wiederholen zu können, ist die Stärke der KI.

#### Phase 3: Die unerwartete Idee eines „kompletten Neuanfangs“

Mitten in der Produktion beschlich mich ein Zweifel. „Würde es nicht leckerer aussehen, Bilder vom Essen zu zeigen, statt die Figuren in den Mittelpunkt zu stellen?“

Also wies ich kühn an: „Als Alternative: Mach ein Design, das Illustrationen der tatsächlichen Gerichte als Hauptelement zeigt.“

![Illustrationsvorschlag mit den Gerichten im Mittelpunkt (ein Teil des Textes ist verstümmelt)](images/fig-09.png)

Die KI kam sofort auf appetitliche Ideen für Essensillustrationen, aber nach dem Vergleich entschied ich mich doch für das ursprüngliche Figurendesign. Auch ein solches „Gehen wir zurück zum Stand von vorher“ können Sie der KI ohne Zögern abverlangen.

#### Phase 4: Die letzte Verteidigungslinie ist das „menschliche“ Auge

Nachdem das endgültige Design feststand, überließ ich der KI auch die Größenvarianten, für Instagram-Beiträge (Hochformat) und für Stories (ein noch schmaleres Hochformat).

Und gerade als es fertig werden sollte, bemerkte ich einen gravierenden Fehler.

„Moment, der Wochentag beim Datum stimmt nicht!“

KI kann gut Bilder zeichnen, versteht aber die Wochentage im Kalender nicht. Hätte ich es so veröffentlicht, wäre es ein Desaster geworden.

Hastig wies ich an: „Korrigiere das Datum auf ‚24.12. (Mi) und 25. (Do)‘!“ und stellte die endgültige Fassung fertig.

![Das endgültige Banner nach der Korrektur](images/fig-10.png)

Insgesamt 22 Runden mit Korrekturen und Dialog.

KI ist kein Zauberstab, aber wenn Sie geduldig mit ihr sprechen, gibt es keinen verlässlicheren Designpartner.

### 3-4. Fall 3: Eine Neujahrs-Öffnungsmitteilung, die sich mit der Lage weiterentwickelt

Die Aufregung um Weihnachten ist kaum verflogen, da steht schon das Nächste an: der Betrieb über den Jahreswechsel.

Für ein Restaurant oder eine Bar ist die Information in dieser Jahreszeit ein Wettlauf gegen die Uhr. „Bis wann haben Sie zum Jahresende geöffnet?“ „Wann öffnen Sie im neuen Jahr wieder?“ Die Gäste suchen ständig nach Informationen.

Doch Informationen ändern sich von Minute zu Minute.

„Wenn das Geschäft zum Jahresende vorbei ist, möchte ich es so umschreiben, dass nur noch die Neujahrsmitteilung zu sehen ist.“

„Ich habe es auf X (Querformat) veröffentlicht, möchte es aber auch auf Instagram (Hochformat) laufen lassen.“

Hätte ich eine externe Designagentur damit beauftragt, wären allein die Kosten für die Änderungen ein Albtraum gewesen, und vor allem wäre es nicht rechtzeitig fertig geworden.

Also tat ich mich wieder mit einer KI zur Bilderzeugung (Nano Banana) zusammen und machte mich an Banner, die mich durch die Zeit zwischen den Jahren tragen sollten.

#### Schritt 1: Der Stil ist „Wachsmalbild aus den 80ern“

Zuerst baute ich Look und Stimmung insgesamt auf.

Was zu meiner Bar passt, ist keine glänzende CG.

„Ein warmer Stil wie ein handgezeichnetes Wachsmalbild aus den 80er-Jahren, mit sichtbaren Pinselstrichen. Halte den Hintergrund schlicht weiß.“

Mit dieser Anweisung als Kern und mit Blick auf eine Ankündigung auf X (früher Twitter) begann ich die Arbeit auf einer Fläche im Querformat.

#### Schritt 2: Die scheidende Schlange und das kommende Pferd. Ein Prost zur Staffelübergabe

Zuerst dachte ich daran, nur ein Tier des Tierkreises zu zeichnen, aber es ging ja um den Jahreswechsel.

Ich hatte die Idee: „Ich möchte, dass sowohl das Tier des scheidenden Jahres (das Tierkreiszeichen dieses Jahres) als auch das Tier des kommenden Jahres (das des nächsten) erscheinen.“

Also gab ich der KI diese Anweisung:

„Setze eine Gruppe Schlangen (das Jahr der Schlange) auf die linke Seite des Bildes und eine Gruppe Pferde (das Jahr des Pferdes) auf die rechte. Lass sie jeweils einen Bierkrug halten und fröhlich anstoßen, wie bei einer Staffelübergabe zum Jahresende.“

Das Bild, das die KI erzeugte, entsprach genau dem, was ich mir vorgestellt hatte.

Liebenswerte Schlangen links, verlässlich wirkende Pferde rechts, die über die Artgrenze hinweg gemeinsam trinken.

Vom „Jahresende (Schlange)“ zum „Neuen Jahr (Pferd)“.

In einem einzigen Bild waren das Verstreichen der Zeit und die festliche Stimmung wunderbar verdichtet.

![Ein erzeugtes Bild, in dem links eine Schlange und rechts ein Pferd anstoßen und damit ausdrücken, dass das alte Jahr dem neuen weicht](images/fig-11.png)

#### Schritt 3: „Schauspielführung“ und „Kostümanprobe“ für die Tiere

Als die Komposition feststand, kam als Nächstes die feinere Inszenierung. Auch hier ging die KI geduldig auf meine Detailwünsche ein.

Auf den ersten Bildern standen die Tiere bloß in einer Reihe oder hielten ihre Krüge auf unnatürliche Weise.

„Lass sie glücklicher aussehen! Wie Stammgäste, die zusammen eine großartige Zeit haben.“

„Ich möchte auch ein Gefühl der Jahreszeit. Leg ihnen Schals und Fliegen um, gib ihnen einen Winterlook.“

Mit dieser einen Bemerkung hüllten sich die Tiere auf dem Bild in warm wirkende rote und grüne Schals und verwandelten sich im Nu in die Stars einer „Winterparty“.

„Ja, jetzt hat es dieses warme Gefühl vom Trinken tagsüber an einem kalten Tag.“

Bei genauem Hinsehen sind manche Handbewegungen und die Art, die Krüge zu halten, noch unnatürlich. Aber Pingeligkeit kostet mehr Zeit. Ich wäge Zeit gegen die Verständlichkeit der Botschaft ab und akzeptiere ein einigermaßen gutes Ergebnis.

#### Schritt 4: Mit der Zeit ändern sich die Informationen

Ab hier zeigt die KI wirklich, was sie wert ist.

Das ursprüngliche Banner zeigte sowohl den Dezember- als auch den Januarplan als „Öffnungsplan zum Jahresende und Jahreswechsel“.

Doch sobald der 31. Dezember vorbei ist, werden die Informationen zum Jahresende nicht mehr gebraucht.

Ich öffnete das Projekt, an dem ich gearbeitet hatte, und bat um eine größere Änderung des Textes.

1.  Titel ändern: von „Öffnungszeiten zum Jahresende und Jahreswechsel“ zu „Im neuen Jahr gibt es Drinks schon tagsüber“.

2.  Informationen aufräumen: den vergangenen Dezemberplan löschen und auf den „Neujahrsplan (2.–4.1.)“ eingrenzen.

3.  Tierkreisfiguren korrigieren: die Schlangen des scheidenden Jahres in Pferde ändern.

4.  Einen Anreiz ergänzen: ein attraktives Angebot, „Highballs und Frittiertes Hähnchen, so viel Sie essen und trinken können“, als neuen Anziehungspunkt für Gäste hinzufügen.

![Schritt 4: Mit der Zeit ändern sich die Informationen](images/fig-12.png)

Ohne das Bild von Grund auf neu zu erstellen, konnte ich die Informationen auffrischen, als würde ich eine Kreidetafel einfach neu beschriften. Das ist die Stärke von KI-Design.

#### Schritt 5: Von X zu Instagram. Ein Format, das sich nach Belieben ändert

Und nun der letzte Schliff.

„Ich habe es auf X angekündigt. Als Nächstes möchte ich es in Instagram Stories laufen lassen.“

Stories verwenden aber das „Hochformat“, das den ganzen Smartphone-Bildschirm ausfüllt. Wenn Sie ein Querformatbild unverändert einsetzen, entstehen leere Streifen oben und unten, und es sieht schlecht aus.

Bei einer gewöhnlichen Illustration wäre das eine Änderung, die ein Neuzeichnen bedeuten würde.

Ich habe der KI aber nur gesagt:

„Behalte dieses Design, ordne es aber in ein Hochformat für Instagram Stories um.“

Die KI ordnete die Tiere, die sich seitlich verteilt hatten, in einer senkrechten Anordnung neu, passte die Balance des Textes an und erzeugte im Nu ein auf Smartphones zugeschnittenes Design.

![Das fertige Hochformatbild für Instagram Stories](images/fig-13.png)

### 3-5. Fall 4: Das Logo der Bar entwerfen - ein Dialog, der „Bedeutung“ in „Form“ verwandelt

Über „Bilder“ wie Banner und Sticker hinaus nahm ich mit der KI auch eine abstraktere Herausforderung in Angriff: den Entwurf eines neuen Logos.

Es soll in Banner und Ähnliches eingebaut werden, damit man Tamuro auf einen Blick erkennt.

Gegenstand ist Tamuro, die Bar nur auf Empfehlung, die ich abends betreibe. Dieser Name trägt einen starken Wunsch in sich: „ein Ort zu sein, an dem sich ganz verschiedene Menschen frei und froh versammeln (tamuro-suru, abhängen) – in der Stadt Higashi-Nakano“.

Wie ließ sich diese unsichtbare „Geschichte“ in einem kleinen Logozeichen verdichten? Ein geduldiger Dialog mit der KI begann.

#### Schritt 1: Schriftzug und Designrichtung wählen

Zuerst warf ich der KI Ideen zu wie „ein gediegener Auftritt mit dem Kanji 屯“ und „etwas Poppiges in Katakana“ und ließ einige grobe Entwürfe anfertigen.

Aber keiner fühlte sich richtig an. Bei der Art dieser Bar wollte ich etwas Moderneres mit einer neutralen Anmutung, die Vielfalt willkommen heißt.

Also änderte ich den Kurs.

„Gehen wir vom vielseitig einsetzbaren Alphabet aus, ‚TAMURO‘. Der Stil soll ‚Flat Design‘ ohne komplizierte Verzierung sein. Und das Logo soll auch einfarbig stark wirken.“

Die KI schlug sofort ein schlichtes, kräftiges serifenloses „TAMURO“ vor.

![Das Logo in serifenloser Schrift](images/fig-14.png)

#### Schritt 2: Der Form „Bedeutung“ einhauchen

Jetzt kommt die eigentliche Bewährungsprobe. Nackte Buchstaben bedeuten nichts. Und nur das „M“ in der Mitte zu haben, vermittelt auch nicht viel.

„Ich möchte die Herkunft des Namens ausdrücken, ‚Menschen kommen zusammen‘. Könntest du das Ganze in einen freundlichen ‚Kreis‘ fassen und dabei jeden einzelnen Buchstaben des Namens so formen, dass er aussieht wie ein Mensch, der sich fröhlich bewegt?“

Das ist ein sehr abstrakter Auftrag. Aber die Vorstellungskraft meiner Stellvertretung (der KI) übertraf meine Erwartungen.

Die KI entwarf ein Design, in dem die Gerüste der Buchstaben „T“, „A“, „M“ und der übrigen in Silhouetten von tanzenden Menschen mit ausgestreckten Armen und Beinen verwandelt waren.

![Ein Logo, bei dem die Buchstaben als Menschen gestaltet sind](images/fig-15.png)

#### Schritt 3: Das Tauziehen zwischen Design und Lesbarkeit

„Interessant! Aber so kann man ‚TAMURO‘ nicht lesen ...“

Legt man zu viel Gewicht auf das Design, ist es nicht mehr als Schriftzug erkennbar, und legt man das Gewicht auf den Schriftzug, verliert er seinen Reiz. In dieses Dilemma geriet ich.

Von da an ging es um wiederholtes Feinjustieren.

„Der Buchstabe ‚A‘ sieht wie ein Mensch aus, das ist gut, aber betone seine Struktur als ‚A‘ ein wenig mehr. Zeichne den Querstrich deutlich ein.“

„Die Gesamtbalance ist gut, aber die Menschen stehen zu dicht gedrängt und wirken eng. Gib ihnen etwas mehr fröhlichen Freiraum.“

„Kombiniere die tanzenden Menschen von vorhin mit den TAMURO-Buchstaben und mach einen Kreis daraus!“

![Das nach Versuch und Irrtum fertiggestellte kreisförmige Logozeichen „TAMURO“](images/fig-16.png)

Obwohl es aus lebhaften Silhouetten von Menschen besteht, kann man im unteren Teil auf einen Blick deutlich „TAMURO“ lesen.

Indem ich mit der KI immer wieder Ideen hin- und herwarf, bekam ich ein Logo, mit dem ich zufrieden war: Es vereint Lesbarkeit, gestalterische Qualität und vor allem den „Wunsch“, den ich mit der Bar verbinde.

Es dient jetzt als Profilbild für die Accounts der Bar auf X (früher Twitter) und Instagram.

### 3-6. Die erste Hürde: einfaches Aufteilen und die „Bildqualitätsfalle“

Die kreative Herausforderung bei der Logoerstellung war vorbei.

Aber die Arbeit war noch nicht getan.

Zurück zu den LINE-Stickern. Was ich in der Hand hatte, war ein „Bogen“ mit 25 Illustrationen auf einer einzigen Seite.

Um sie als LINE-Sticker einzureichen, musste ich jede einzelne ausschneiden, den Hintergrund transparent machen und die Größe anpassen. Es war eine mühselige Arbeit, die ich vor mir hergeschoben hatte.

„Von Hand kann ich die unmöglich ausschneiden ...“

Ich fragte Gemini um Rat und bat um eine Lösung. Gemini sagte, als wäre es nichts:

„Automatisieren wir das mit einer Programmiersprache namens Python.“

Ehrlich gesagt hätte ich da fast aufgegeben.

„Python? Den Namen habe ich schon gehört, aber solche Software auf meinem Computer zu installieren, macht mir Angst. Und die Einrichtung klingt auch schwierig. Von jemandem, der eine Bar betreibt, kann man doch nicht so viel verlangen ...“

Doch das ist einer der Höhepunkte dieses Buches. Als hätte Gemini gespürt, was ich dachte, machte es einen überraschenden Vorschlag.

Gemini:

„Sie müssen überhaupt keine Umgebung einrichten. Nutzen Sie ein kostenloses Google-Werkzeug namens ‚Google Colab‘. Es läuft im Browser, Sie müssen also nur den Code, den ich schreibe, hineinkopieren und einfügen.“

„Was? So etwas gibt es?“

Ich traute meinen Ohren nicht. Ich hatte mir nie vorgestellt, dass es eine Umgebung gibt, in der Programmieren allein im Browser läuft und nichts auf meinem eigenen PC installiert werden muss.

Nicht erst „nachdem man Python gelernt hat“, sondern indem man sich „von der KI sogar die Existenz des Werkzeugs (Colab) beibringen lässt“.

In diesem Moment brach meine Annahme zusammen, dass „Programmieren viel Vorbereitung heißt“.

### 3-7. Den Fehlerbildschirm nicht „lesen“, sondern „knipsen und schicken“

Wie angewiesen öffnete ich Google Colab, fügte den Code ein und drückte auf die Play-Taste.

Doch die Wirklichkeit ist nicht so freundlich. Auf dem Bildschirm erschien eine Flut von leuchtend rotem Text ... eine Fehlermeldung.

„Error: Image file not found ...“

Das frühere Ich hätte schon beim Anblick dieses Fehlers eine allergische Reaktion gehabt und den Browser still geschlossen.

Aber jetzt hatte ich einen Verbündeten: die „multimodale“ KI, eine KI mit Augen.

Ich versuchte gar nicht erst, die Fehlermeldung zu lesen.

Ich machte einfach einen Screenshot des Bildschirms und fügte ihn mit einem Handgriff ins Chatfeld von Gemini ein.

Und ich schrieb eine einzige Zeile dazu: „Irgendein Fehler ist aufgetaucht.“

![Der Fehlerbildschirm von Google Colab, unverändert in Gemini eingefügt](images/fig-17.png)

Gemini analysierte das Bild sofort und schickte eine Antwort zurück.

Gemini:

„Ah, der Dateiname des einzulesenden Bildes ist falsch. Ich habe den Code so korrigiert, dass er ‚.jpg‘ verwendet. Bitte führen Sie ihn mit dieser Fassung noch einmal aus.“

„... Wow, das macht Spaß!“

Dieser Austausch fühlte sich weniger wie Programmieren an, sondern eher wie ein Suchbild-Spiel oder ein Hin und Her mit dem Ball.

- Ich: (fügt einen Screenshot ein) „Es bricht schon wieder ab.“

- Gemini: „Die Bildgröße passt nicht. Ich füge eine Funktion hinzu, die sie automatisch anpasst.“

- Ich: (fügt einen Screenshot ein) „Diesmal wirkt das Bild irgendwie grobkörnig.“

- Gemini: „Ich habe vergessen, den Vorgang namens ‚LANCZOS‘ hinzuzufügen, der die Bildqualität bewahrt. Ich korrigiere das.“

Ich verstehe keine einzige Zeile des Codes. Wenn ein Fehler erscheint, mache ich einfach einen Screenshot und werfe ihn mit „Schau!“ der KI zu.

Dieses „Übergeben der Fehleranalyse“ war das größte Geheimnis, wie es mir ohne Vorwissen gelang, ein System zu bauen, und zugleich die aufregendste Erfahrung von allen.

### 3-8. Die größte Hürde: „handgezeichneter Versatz“ und „Überstehendes“

Während ich dieses „Gespräch namens Fehler“ weiterführte, wurde das System immer ausgereifter.

Und endlich kam ich zur größten Herausforderung: „Phase 2: Automatisches Ausschneiden handgezeichneter Layouts“.

Ich wurde ehrgeiziger.

„Machen wir einen Bogen mit 5×5, also 25 Stickern. Und weil ich mehr handgezeichnete Anmutung möchte, will ich sie frei platzieren, ohne an die Rasterlinien gebunden zu sein.“

Bei Code, der den Bogen einfach gleichmäßig teilt, ragt die Hand einer Figur oder ein Schriftzug in die nächste Zelle hinein und wird kläglich abgeschnitten.

Ich probierte auch eine Methode, „alles außer dem weißen Hintergrund auszuschneiden“, aber die Ränder wurden ungleichmäßig, und sie scheiterte.

Ich wollte schon aufgeben. Da sagte ich, gestützt auf meine Instinkte aus meiner Zeit als Systemmensch, zu Gemini:

„Ich möchte, dass du die Idee aufgibst, das Bild mit der Schere zu schneiden. Schau stattdessen, in welcher Zelle der ‚Mittelpunkt‘ jedes Bildes liegt. Wenn der Mittelpunkt in dieser Zelle liegt, behandle das ganze Bild als ‚zu dieser Zelle gehörig‘, auch wenn es ein wenig übersteht, und wirf es in den Eimer dieser Zelle.“

Das war die Lösung, die ich „Raster-Eimer-Methode“ nannte.

Warum bin ich darauf gekommen, es „nach Mittelpunkt in einen Eimer zu legen“ statt „mit der Schere zu schneiden“?

Die Denkweise der Laien (analog): Man stellt sich vor, „ein einzelnes Bild mit der Schere auszuschneiden“. So schneidet man genau an der Linie entlang, und die Hände und Füße der Figur werden abgetrennt.

Die Denkweise eines Systemmenschen (digital): Ein Computer hat kein physisches Gespür für „Schneiden“. Stattdessen hat er „Koordinaten (Positionen)“. So sah ich es: „Auch wenn es ein wenig übersteht, können wir das ganze Bild einfach als ‚zu dieser Zelle gehörig‘ betrachten, solange der ‚Bauchnabel (Mittelpunkt)‘ des Bildes in der Zelle liegt.“

![Die analoge Idee „entlang von Linien schneiden“ und die digitale Idee „nach einem Punkt auswählen“](images/fig-18.png)

Das heißt es, „vage analoge Arbeit in klare digitale Regeln zu übersetzen“. Wenn Sie einer KI Anweisungen geben, funktioniert es gut, sich eine solche Regel auszudenken, bei der das Ergebnis „egal, wer hinsieht (oder rechnet)“ dasselbe ist.

Gemini verwandelte diese abstrakte Bitte hervorragend in Code. Das Ergebnis war perfekt.

Der Schriftzug „Danke!“ und die Schwänze, die in Nachbarzellen geragt hatten, wurden alle sauber erkannt und zu einem einzigen Sticker zusammengefasst.

Sogar meinen Sonderwunsch „Der letzte (der 25.) wird nicht gebraucht, überspring ihn“ erfüllte es. Endlich hatte ich ein Werkzeug, bei dem man „nur das Bild hineinlegt und einen Knopf drückt, und ein vollständiger Satz Bilder für die Einreichung bei LINE entsteht“.

Ich habe lediglich das „Problem vor Ort (die Bilder werden abgeschnitten)“ vermittelt und eine „logische Lösung (nach dem Mittelpunkt entscheiden)“ vorgeschlagen. Den ganzen schwierigen Code hat die KI geschrieben.

Das ist die Essenz von „Vibe Coding“, dem Bauen von Systemen von null Vorwissen aus.

#### Zusammenfassung von Kapitel 3

1.  KI-Zeichnen ist nicht „einmal und fertig“. Sie können es beliebig oft der Lage entsprechend neu machen: Figuren ändern, eine saisonale Note hinzufügen, das Medium wechseln.

2.  Selbst ein abstraktes „Konzept (Menschen kommen zusammen)“ lässt sich durch wiederholten Dialog in eine „Form (ein Logo)“ verwandeln.

3.  Gerade mühselige Arbeiten (Bilder ausschneiden) lassen sich mit Gemini × Google Colab hervorragend automatisieren. Fehler lassen sich mit Screenshots lösen.

#### Kolumne 1: Ein Crashkurs in „Google Colab“ für alle, die ein Lokal führen, ohne technischen Hintergrund

~Nutzen Sie eine „Mietküche“ und lassen Sie Ihren eigenen PC, wie er ist~

„Google Colab“, das im Haupttext vorkam. Auf dem eigenen Computer zu programmieren (Python), ist, als würde man „in der heimischen Küche echtes Ramen von Grund auf zubereiten, angefangen bei der Brühe“. Die Vorbereitung ist sehr aufwendig.

Google Colab dagegen ist „eine kostenlose Mietküche, die mit Kochwerkzeugen voll ausgestattet ist“. Öffnen Sie einfach den Browser, und die besten Werkzeuge stehen bereit. Sie müssen an Ihrem Computer keine Einstellung ändern. Sie können allein mit einem Browser programmieren und Ihre Umgebung sauber halten. Suchen Sie zuerst nach „Google Colab“ und werfen Sie einen Blick in diese Mietküche.

#### Kolumne 2: Fehlerbildschirme nicht zu „lesen“, ist genau richtig

~Beherrschen Sie die ultimative Waffe: den Screenshot~

Wenn ein Fehler erscheint, versuchen Sie dann ernsthaft, die englische Meldung zu entziffern? Das ist Zeitverschwendung.

Wenn beim Kochen etwas komisch schmeckt, lassen Sie die Küchenleitung probieren. Zeigen Sie der KI genauso einfach einen „Screenshot (Bildschirmfoto)“.

- Windows: \[Win\] + \[Shift\] + \[S\]

- Mac: \[Cmd\] + \[Shift\] + \[4\]\
  Drücken Sie diese Tasten, ziehen Sie einen Rahmen um den Fehler und fügen Sie ihn in Gemini ein. Das ist alles. „Den Fehler nicht lesen“, sondern „den Fehler zeigen“. Allein durch diese Änderung der Denkweise verdreifacht sich Ihr Entwicklungstempo.

Ich habe bisher mehrere Beispiele vorgestellt, und alles, was ich tue, läuft auf die folgenden drei Punkte hinaus.

・Die fertige Form nicht auf einmal verlangen (ein Dialog darf eingeplant sein)\
・Ohne Zögern sagen: „Nein, das ist noch nicht ganz richtig“\
・Davon ausgehen, dass Korrekturen nichts kosten, und Wünsche lässig hinwerfen

Sie brauchen kein Designtalent. Sie brauchen nur den Mut, „etwas stört mich“ in Worte zu fassen.

## Kapitel 4: Praxis Teil 2 - Die tägliche Arbeit effizienter machen (mit multimodaler KI)

~Erledigen Sie „mühselige Dateneingabe“ mit einem einzigen Smartphone~

### 4-1. Der Ärger mit der Aktualisierung der Weinkarte

Für alle, die eine Bar oder ein Restaurant führen, ist das Aktualisieren der Speisekarte eine unscheinbare, aber schwere Last.

Am meisten Mühe machte mir die „Weinkarte“.

Jedes Mal, wenn ein neuer Wein eintrifft, fallen die folgenden Arbeiten an.

1.  Das Etikett der Flasche ansehen (fremdsprachige Schreibschrift, schwer zu lesen).

2.  Markennamen und Jahrgang (Vintage) fehlerfrei in den PC tippen.

3.  Die Eigenschaften und den Geschmack des Weins im Internet nachschlagen.

4.  Eine „Beschreibung“ schreiben, die Gäste neugierig aufs Lesen macht.

5.  Gerichte überlegen, die gut zu dem Wein passen (Pairings).

All das mit dem Wörterbuch in der Hand zwischen zwei Stoßzeiten zu erledigen, ist fast unmöglich. Ich schob es mit „mache ich später“ auf, und die Empfehlungsliste blieb oft unaktualisiert.

### 4-2. Einfach fotografieren. Die Überraschung der „Weinkarten-Gem“

Also beschloss ich, die „multimodale Funktion (Bilderkennung)“ von Gemini auszuprobieren.

Die Methode ist so einfach, dass man fast stutzt.

1.  Fotografieren Sie die Weinflasche mit Ihrem Smartphone.

2.  Schicken Sie das Foto an Gemini.

3.  Fügen Sie eine Zeile hinzu: „Mach daraus eine Liste.“

Das ist alles.

![Ein Foto eines echten Weinflaschenetiketts, mit einem Smartphone aufgenommen](images/fig-19.jpg)

Gemini liest daraufhin sofort die Etikettendaten aus dem Foto.

Es schreibt nicht nur den Markennamen ab, etwa „Cave d'Occi Winery, Tsukimi de Ippai 2024“, sondern durchsucht auch eine riesige Online-Datenbank nach den Eigenschaften des Weins und erzeugt automatisch eine ansprechende Beschreibung.

Noch mehr überraschte mich, dass es gleich „Pairing-Vorschläge“ mitlieferte.

Vorschläge wie „Das füllige Aroma dieses Weins passt gut zu ○○“ erschienen innerhalb weniger Sekunden auf dem Bildschirm.

Die Stunden, die ich früher im Kampf mit dem Wörterbuch verbracht hatte, schrumpften auf einen einzigen Druck auf den Auslöser des Smartphones.

### 4-3. Die eigene „Gem“ bauen

Um diese Arbeit noch einmal deutlich effizienter zu machen, nutzte ich weiter eine Funktion namens „Gems“.

Das ist eine „eigene, maßgeschneiderte KI-Funktion“, der man vorab eine bestimmte Rolle und feste Regeln beibringen kann.

Jedes Mal alles von vorn zu erklären – „Du bist ein Sommelier. Sieh dir dieses Foto an und …“ – ist mühsam.

Deshalb habe ich bei Gemini vorab die folgenden „Anweisungen (Prompt)“ hinterlegt. Das ist sozusagen das Gehirn der „hauseigenen Sommelier-KI“ meiner Bar.

#### Die Anweisungen, die ich tatsächlich hinterlegt habe

> Lies das Bild ein und erstelle eine Weinkarte im folgenden Format.
>
> Verwende bei den Preisen keine Marktpreise. Berechne sie unter der Annahme des Flaschenpreises in einem üblichen Restaurant (etwa das 2,5- bis 3-Fache des Einkaufspreises).
>
> Verwende kein Tabellenformat. Erstelle die Karte so, dass sie auf ein oder zwei Blätter A4 passt.
>
> Das Format dient nur als Anhaltspunkt; erstelle die Karte ausschließlich aus dem, was eingegeben wurde.
>
> Das Format sieht so aus.
>
> Vereinigtes Königreich 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8.500 (ca. $57)
>
>  Helles Gold mit angenehmer Perlage. Anklänge von Melone und Honig im Zitrusduft … (der Rest ist ausgelassen)

Zur unteren Hälfte dieses Prompts, dem Teil „Format (Muster)“:

Den habe ich nicht aus dem Nichts erfunden.

Als ich früher im Internet nach Weininformationen suchte, dachte ich oft: „Diese Beschreibung des Händlers ist gut verständlich“ oder „So, wie diese Seite schreibt, klingt der Wein köstlich“, und ich hatte solche Passagen immer wieder einfach in ein Notizprogramm kopiert.

Dieses „Flickwerk-Memo“ warf ich Gemini unverändert hin.

„Das sind Passagen, die ich vor einiger Zeit zusammenkopiert habe. Ahme diesen Ton nach und schreibe auch über den Wein auf dem neuen Foto.“

Mehr habe ich nicht gesagt.

Und doch stecken in dieser Anweisung drei Kniffe, die die Last im Lokal verringern.

① „Die Logik der Preisberechnung“

Das spart am meisten Zeit. Weil ich nicht den „Marktpreis“, sondern „den Preis, den ein Restaurant verlangen würde“ verlangt habe, rechnet die KI von den üblichen Einkaufspreisen rückwärts und nennt mir eine Zahl wie „¥8.500 (ca. $57)“, die direkt auf die Karte kann. (Die endgültige Entscheidung liegt natürlich bei Ihnen, aber mit einem Richtwert fällt sie leichter.)

② „Kein Tabellenformat, sondern passend auf A4“

Kommt die Ausgabe als Tabelle wie in Excel, fällt das Layout auseinander, sobald man sie in die Speisekarte einfügt. Indem ich von Anfang an im „A4-Kartenformat“ schreiben lasse, will ich eine Ausgabe erhalten, die sich so drucken und verwenden lässt.

③ Aus dem Web kopierte Texte als „Muster“ verwenden

Statt vage zu bitten: „Schreib eine schöne Beschreibung“, zeige ich ein konkretes Beispiel (mein zusammenkopiertes Memo): „🇬🇧-Flagge + Weinname + Preis + bildhafte Beschreibung“.

Wenn man einer KI ein Beispiel zeigt, versteht sie: „Aha, in diesem Ton und dieser Art soll ich schreiben“, und die Genauigkeit der Ausgabe springt nach oben. Fachlich heißt das „Few-Shot-Prompting“, im Kern ist es aber dasselbe wie „durch Zuschauen beibringen“.

Und dieses „Vorbild“ darf ganz selbstverständlich aus gefundenem Text bestehen, dem schriftlichen Gegenstück zu einem im Web gefundenen Foto.

![Der von Gemini ausgegebene fertige Weinkartentext](images/fig-20.png)

### 4-4. Es muss nicht einmal ein Bild sein. Die Copy-and-paste-Revolution aus LINE

Das Schöne an dieser „Weinkarten-Gem“ ist, dass die Eingabe nicht auf Fotos beschränkt ist.

Tatsächlich bestellt man in einer Bar oft per LINE beim Getränkehändler, nicht wahr?

Ist die Bestellung erledigt, kommt vom Händler eine Nachricht wie diese.

> „Vielen Dank wie immer. Wir haben Ihre Bestellung wie folgt erhalten.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 Flaschen
>
> ・Ridgeview Bloomsbury 6 Flaschen
>
> ・○○ (neuer Wein) 2 Flaschen
>
> Wir liefern morgen.“

Eines Tages kam mir plötzlich der Gedanke: „Könnte ich diesen Text nicht einfach so verwenden?“

Zum Test kopierte ich diese LINE-Nachricht mit dem Finger und warf sie direkt in Gemini.

Das Ergebnis war perfekt.

Gemini erkannte in der LINE-Nachricht nur die „Produktnamen“, suchte online nach Informationen und erstellte eine Liste im gewohnten Format (Flagge + Preis + Beschreibung).

Ich muss also nicht einmal auf die Flaschen warten und sie fotografieren.

In dem Moment, in dem ich bestelle, ist die Karte allein durch Kopieren und Einfügen im Smartphone fertig, noch bevor die Ware eintrifft.

Man braucht keinen PC aufzuklappen und keine Kamera zu starten.

In einer Ecke der Küche oder in der Bahn ist die Arbeit allein mit dem Smartphone erledigt.

Ist das nicht genau die „echte Effizienz“, die jemand verdient, der ein Lokal allein führt?

### 4-5. Der Vorschlag der KI × das Urteil vor Ort (die Wirklichkeit)

Trotzdem schlucke ich die Vorschläge der KI nicht einfach. Entscheidend ist hier unser „menschliches Urteil vor Ort“.

Einmal machte die KI zu einem Wein diesen Vorschlag:

KI: „Zu diesem Rotwein passt gebratene Ente mit Orangensauce perfekt.“

Ein wunderbarer Vorschlag, aber leider war an diesem Tag keine Ente im Kühlschrank des Lokals.

Ich denke nicht: „Die KI sagt es, also muss ich Ente kaufen.“ So denke ich stattdessen:

Ich (im Lokal): „Ente haben wir nicht, aber heute ist gutes Freilandhuhn gekommen. Es hat ähnlich viel Fett wie Ente, also brate ich dieses Huhn auf der Haut knusprig an und gebe eine Sauce mit Orangenaroma dazu, ganz so, wie die KI es sagt.“

„Das Wissen der KI (Ente und Orange passen zusammen)“ × „der Bestand im Lokal (wir haben Huhn)“ = „ein neues Gericht, das ohne Zögern umsetzbar und realistisch ist“.

Diese Kombination ist die eigentliche Freude an der Menüentwicklung mit KI.

Die KI liefert die Lehrbuchantwort, aber sie weiß nicht, was heute im Kühlschrank liegt. Diese Lücke zu füllen, ist Ihre Aufgabe als Lokalleitung.

### 4-6. Die letzte Meile: Die KI kann nicht „verkosten“

Und noch eine Sache dürfen Sie nie der KI überlassen.

Das ist die Verkostung, bevor etwas zu den Gästen geht.

Die Beschreibungen und Pairings der KI beruhen auf „allgemeinen Standarddaten“.

Wein aber ist etwas Lebendiges. Selbst bei demselben Etikett ändert sich der Geschmack mit dem Jahrgang und der Art der Lagerung.

Einmal schrieb die KI zu einem Weißwein: „Ein frischer, leichter, trockener Wein. Perfekt zu Meeresfrüchte-Carpaccio.“

Als ich die Flasche aber tatsächlich öffnete und probierte, war er reifer als erwartet, mit satten, honigartigen Noten.

„Wenn ich das als ‚leichten, trockenen Wein‘ serviere, sind die Gäste enttäuscht … Zu Hühnchen in Sahnesauce würde er besser passen als zu Carpaccio.“

Ich korrigierte den von Gemini erzeugten Text sofort.

- Vorher (KI): „Frisch und leicht. Gut zur Vorspeise“

- Nachher (Mensch): „Durch die Reifung reicher, vollmundiger Körper. Kräftig genug für ein Hauptgericht“

Die KI erstellt 90% des Entwurfs, und der Mensch verkostet und fügt „die letzten 10% (die Seele)“ hinzu.

Diese Prüfung liegt in der Verantwortung der Menschen, die ein Lokal führen, und die KI kann sie niemals nachahmen.

Nicht „weil die KI es gesagt hat“, sondern „weil ich ihn getrunken habe und er köstlich war“.

Um mit dieser Überzeugung servieren zu können, probiere ich auch heute frisch geöffneten Wein, die von der KI erstellte Karte in der einen Hand.

#### Kolumne 3: Tipps, damit die KI Fotos „richtig“ sieht

~ Als würde man einem Sommelier-Profi ein Etikett zeigen ~

Wenn Sie Gemini ein Foto schicken, verbessern ein paar kleine Kniffe die Erkennung deutlich.

1.  Spiegelungen vermeiden: Flaschenetiketten reflektieren leicht Licht. Ändern Sie beim Fotografieren den Winkel ein wenig oder werfen Sie mit dem Körper einen Schatten.

2.  Mehrere Aufnahmen gemeinsam schicken: Bei Dingen wie dem Inhalt eines Kühlschranks schicken Sie eine Übersichtsaufnahme und Nahaufnahmen zusammen, dann erkennt die KI auch Zutaten im toten Winkel.

3.  Mit dem Finger zeigen: Es hilft auch, beim Fotografieren mit dem Finger auf die Stelle zu zeigen, die die KI ansehen soll. Schreiben Sie in den Prompt etwa „Ich zeige mit dem Finger darauf“. Das ist dasselbe, wie in einem Restaurant im Ausland auf die Speisekarte zu zeigen.

## Kapitel 5: Anwendungen – Geschäftsanalyse und Gewinnsteigerung

~ Heben Sie die „unsichtbare Goldmine“. Eine Strategiesitzung mit Ihrer KI-Beraterin oder Ihrem KI-Berater ~

### 5-1. Die Nacht, in der ich mir an jedem Monatsende über dem Taschenrechner den Kopf zerbreche

Wer ein kleines, unabhängiges Lokal führt, empfindet keine Zeit als so bedrückend wie die des Monatsabschlusses.

In der nächtlichen Stille die Kassendaten zusammenzählen und in Excel eintippen – man hört nur den eigenen Seufzer.

„Das Umsatzziel dieses Monats waren ○○0.000 Yen. … Verfehlt.“

„Die Gästezahl ist nicht schlecht. Am Wochenende war es voll. Aber aus irgendeinem Grund steigt der Umsatz pro Gast nicht.“

Warum erreiche ich das Ziel nicht? Am Essen kann es nicht liegen, das ist schließlich gut. Ich gebe mir beim Service Mühe.

„Sind die Preise vielleicht zu hoch?“

„Nein, wenn ich noch günstiger werde, mache ich keinen Gewinn. Und die Wareneinkaufskosten steigen auch.“

Fragen ohne Antwort drehen sich im Kopf im Kreis, und am Ende flüchte ich mich in Durchhalteparolen: „Nächsten Monat hänge ich mich mehr rein und empfehle gezielter.“ Das war meine schlechte Angewohnheit, und die vieler anderer, die ein Lokal führen.

Aber jetzt habe ich eine Beraterin ohne Gefühle an meiner Seite.

Ich legte Gemini die Umsatzdaten dieses Monats und die Daten der Speisekarte meines Lokals vor.

### 5-2. Ein Experiment: Die KI „Optik“ und „Zahlen“ gleichzeitig lesen lassen

Diesmal gab ich Gemini drei Informationen.

Das „Design (rechte Gehirnhälfte)“ und die „Zahlen (linke Gehirnhälfte)“, die ich bisher immer getrennt verwaltet hatte, warf ich alles zusammen hinein.

1.  „Das Umsatzziel dieses Monats“

- Mein inständiger Wunsch. Die Zahl, die ich unbedingt erreichen muss.

2.  „Alle Daten der jüngsten Kassenbons (CSV/Excel)“

- Das Ergebnis in der Wirklichkeit. Die nüchternen Fakten darüber, wer was zu welchem Preis bestellt hat.

3.  „Eine PDF-Datei der aktuellen Speisekarte“

- Die Welt, die die Gäste sehen. Visuelle Informationen wie die Platzierung der Fotos sowie Schriftgröße und -farbe.

Und dann stellte ich diese Frage.

Es war kein Arbeitsauftrag wie das frühere „Mach ein Bild“. Es war eine Frage, wie sie jemand stellt, der ein Lokal führt.

> „Vergleiche die aktuellen Umsatzdaten (Wirklichkeit) mit dem Layout der Speisekarte (Erscheinungsbild).
>
> Zeige den Engpass auf: Was fehlt uns, um das Ziel von ○○0.000 Yen zu erreichen?“

### 5-3. Die „Annahme der Lokalleitung“, die die KI durchschaute

Wenige Sekunden später kam Geminis Antwort, und sie traf genau meinen blinden Fleck.

Ich hatte allgemeine Ratschläge erwartet wie „Entwickeln wir ein neues Gericht“ oder „Machen wir Werbung in den sozialen Medien“.

Aber die KI wies auf eine Tatsache hin, die ich unbewusst zu verbergen versucht hatte.

Geminis Antwort:

> „Beim Abgleich der Daten mit der Speisekarte habe ich eine große verpasste Chance gefunden.
>
> Das All-you-can-drink-Angebot, das eine hohe Marge hat und den Umsatz pro Gast zuverlässig steigern kann, steht auf der Speisekarte (Vorher) derzeit nur als Text, unscheinbar ganz unten links.
>
> Dagegen steht auf dem besten Platz der Karte, ganz oben, das günstige ‚Menü ¥2.200 (ca. $15)‘. So wandern die Gäste zum günstigeren Angebot ab und bemerken die teurere Option mit All-you-can-drink gar nicht.“

Beim Blick auf den Bildschirm musste ich aufstöhnen. Es stimmte genau.

Wir haben ein All-you-can-drink-Angebot. Aber irgendwo in meinem Kopf hatte ich Folgendes gedacht:

„Wir sind keine Kette von Izakaya *(einfache japanische Kneipen mit Essen und Getränken)*. Groß mit All-you-can-drink zu werben, wirkt billig.“

„Ich möchte, dass die Leute den Geschmack des Weins genießen, also sollen es nur diejenigen bestellen, die davon wissen.“

Diese „Annahme“ von mir zeigte sich im Layout der Speisekarte, in dem Text ganz unten.

![Die Speisekarte „Vorher“. Das All-you-can-drink-Angebot steht unten links und fällt nicht auf. Auch ist schwer zu erkennen, dass das Essen separat ist](images/fig-21.png)

Der KI entging das nicht.

„Sie wollen Ihre Zielzahl erreichen, nicht wahr? Dann sollten Sie das Menü, das Sie am liebsten verkaufen würden, das mit All-you-can-drink, stolz ganz oben platzieren.“

### 5-4. Kein Bildmaterial? Dann lassen wir die KI auch das zeichnen

Ich fasste einen Entschluss. „Wenn cooles Aussehen nur den Umsatz drückt, probiere ich es, koste es, was es wolle.“

Aber hier tauchte ein Problem auf.

„Selbst wenn ich es groß oben platziere, ist Text allein schwach …“

Und wenn ich von einer Gratis-Fotoseite ein Foto von Menschen nehme, die mit Bier anstoßen, sieht es sofort nach Restaurantkette aus. Es passt nicht zur Atmosphäre meines Lokals.

Zum Zeichnen habe ich kein Talent, und eine Illustration in Auftrag zu geben, kostet Geld und Zeit.

Ich fing an, mir Sorgen zu machen: „Was tun …?“, doch dann fiel es mir sofort ein.

„Richtig, ich habe ja eine stellvertretende Lokalleitung (die KI), die zeichnen kann.“

Auf einer Seite für Bildmaterial hatte ich etwas gefunden, das dem gewünschten Bild nahekam. Dort stand, dass Bearbeitung erlaubt ist.

Ich tippte weiter Folgendes ins Chatfeld:

> „Zeichne eine Illustration für den oberen Teil der Speisekarte. Nimm das angehängte Bild als Grundlage.
>
> Ich möchte Menschen, die fröhlich anstoßen – aber so, dass es nicht billig wirkt.
>
> Bitte im schlichten Strichzeichnungsstil.“

Wenige Sekunden später erschienen vier Illustrationsvorschläge auf dem Bildschirm.

Daraus wählte ich die schlichte, warme „Cheers!“-Illustration, die am besten zur Atmosphäre des Lokals passte.

![Die „Cheers!“-Illustration, die die KI in nur 10 Sekunden erzeugt hat](images/fig-22.png)

Es dauerte nur 10 Sekunden.

Nicht nur die Analyse: Auch das „Material“, das für die Verbesserung nötig ist, lässt sich auf der Stelle beschaffen.

Das ist die eigentliche Stärke, wenn man generative KI in die Betriebsführung einbaut.

### 5-5. Allein durch das geänderte Layout stieg der Umsatz pro Gast um etwa 40%

Also gestaltete ich die Speisekarte neu.

#### Vorher: Die Speisekarte, wie sie war

- Bester Platz (ganz oben): Günstige Angebote wie „Menü ¥2.200 (ca. $15)“ und „Menü mit mehreren Gängen ¥3.300 (ca. $22)“.

- All-you-can-drink: Nur als Text in der unteren linken Ecke aufgeführt, als „All-you-can-drink ab ¥3.000 (ca. $20)“. Es ging völlig unter.

#### Nachher: Die überarbeitete Speisekarte

- Bester Platz (ganz oben): Hochpreisige Angebote von ¥4.500–¥5.700 (ca. $30–$38), präsentiert als „Unsere Empfehlung! Das Menü für den vollen Genuss (mit All-you-can-drink)“.

- Design: Die von der KI erzeugte „Cheers!“-Illustration lenkt den Blick optisch stark auf das Angebot: „Schauen Sie zuerst hierher!“

- Layout-Änderung: Die günstigen Menüs, die früher die Hauptrolle spielten, rutschten nach unten.

![Die Speisekarte „Nachher“. Das All-you-can-drink-Menü steht ganz oben](images/fig-23.png)

Das Essen, die Preise und die Qualität der Getränke sind im Grunde fast unverändert. Ich habe nur geändert, „wie“ und „wo“ es gezeigt wird.

Und das Ergebnis?

Schon ab dem nächsten Tag änderte sich das Bestellverhalten der Gäste deutlich.

Die ersten Worte der Gäste, die die Karte aufschlugen, waren nicht mehr „Erst mal ein Bier“, sondern „Dann nehmen wir diesen ‚Empfehlungsmenü (¥4.900 (ca. $33))‘ mit der Illustration“.

Gäste, die früher mit „dem Menü (¥2.200 (ca. $15)) plus zwei Getränken“ abschlossen (ein Umsatz von etwa ¥3.500 (ca. $23) pro Gast), wählten nun von Anfang an das Menü für ¥4.900 (ca. $33).

Allein dadurch sprang der Umsatz pro Gast um ¥1.400 (ca. $9,3).

Hinzu kam, dass die Gäste auch den Vorteil hatten, „trinken zu können, ohne an die Rechnung zu denken“, sodass die Zufriedenheit nicht sank, sondern sogar stieg.

### 5-6. Erfolgskontrolle mit dem Dezember-Umsatz-PDF (PDCA)

Einen Monat war es her, dass ich die Maßnahme umgesetzt hatte.

Hier nicht aufzuhören, ist das Wesentliche am Einsatz von KI.

Viele, die ein Lokal führen, beurteilen Ergebnisse nach Gefühl und lassen es dabei bewenden: „Es war viel los, also hat es wohl gewirkt“ oder „Der Umsatz ist gestiegen, das ist gut“.

Aber ich wandte mich wieder an Gemini.

Diesmal lud ich das „PDF der Umsatzdaten vom Dezember“ hoch, in dem die Ergebnisse standen, und fragte Folgendes:

> „Die Ergebnisse der Maßnahme vom letzten Monat (Änderung der Speisekarte) liegen vor.
>
> Sieh dir diese Umsatzdaten vom Dezember an und kontrolliere den Erfolg (bewerte): Haben die Bestellungen des ‚Empfehlungsmenüs‘ wie beabsichtigt zugenommen, und wie hat sich das auf den Umsatz pro Gast ausgewirkt?“

Gemini analysierte die Daten sofort und schickte mir einen Bericht zurück.

![Geminis Bildschirm mit dem Umsatzanalysebericht: Ich habe für die Veröffentlichung eine Zusammenfassung erstellt, daher weicht der Inhalt teilweise vom folgenden Text ab](images/fig-24.png)

Geminis Analyse:

> „Das sind hervorragende Ergebnisse. Der Trend in den Daten zeigt, dass die Bestellungen des ‚Menüs für den vollen Genuss‘ auf etwa das 1,8-Fache des Vormonats gestiegen sind.
>
> Dadurch ist der Umsatz pro Gast insgesamt im Durchschnitt um ○○ Yen gestiegen.
>
> Der Hauptfaktor ist, dass die höhere Platzierung des All-you-can-drink-Angebots den Bestellwert erhöht hat, besonders bei Gruppen.“

Als ich diese Worte hörte, fühlte ich mich zum ersten Mal wirklich erleichtert.

Nicht „irgendwie haben wir Geld verdient“, sondern die Gewissheit: „Ich habe gezielt gehandelt, und ich habe das Ergebnis planmäßig erreicht.“

Das wird zur Triebkraft für die nächste Maßnahme.

1.  Plan (Planung): Umsatzdaten und Speisekarte ansehen und das Problem finden (das All-you-can-drink-Angebot ist versteckt).

2.  Do (Umsetzung): Die KI eine Illustration zeichnen lassen und das Layout der Speisekarte ändern.

3.  Check (Erfolgskontrolle): Das Dezember-Umsatz-PDF einlesen lassen und die Ergebnisse überprüfen.

4.  Act (Verbesserung): Als Nächstes überlegen, das Layout der Speisekarte für das Essen zu überarbeiten.

Den „PDCA-Zyklus“, den große Unternehmen mit enormem Aufwand betreiben, kann ich als Einzelperson mit nur einem Smartphone durchlaufen, wenn ich die KI als Partnerin habe.

## Kapitel 6: Herausforderungen – ein System allein für mein eigenes Lokal entwickeln

~ „Wenn es das nicht gibt, baue es.“ Ein Systementwicklungsprojekt ohne Fachleute ~

※Nur zur Information: Sie müssen nicht alles in diesem Buch tun.

・Ein Bild senden und die KI einen Text schreiben lassen\
・Eine lange LINE-Nachricht in ein Diagramm verwandeln

Diese beiden genügen für den Anfang. Schon das wird Ihre Arbeit ganz sicher erleichtern.\
Es genügt auch, dies einfach als Geschichte zu lesen und zu denken: „So viel geht also mit KI.“

### 6-1. Fertige Apps lösen die Probleme nicht, die mir konkret „auf den Nägeln brennen“

Bisher habe ich davon erzählt, KI auf bestehenden Plattformen zu nutzen, etwa für Bildgenerierung und Speisekartenanalyse.

Doch wenn man ein Geschäft weiterführt, tauchen Sorgen auf, die „fertige Apps“ schlicht nicht lösen können.

Besonders bei einem unregelmäßigen Geschäftsmodell wie unserem – „tagsüber Curry, abends Bar“ – ist auch der Geldfluss kompliziert.

„Ich möchte meinen Kontostand bei PayPay Bank mit den anstehenden Zahlungen abgleichen und wissen, wie viel am Monatsende übrig bleibt.“

„Die Zahlungstermine verteilen sich auf den 10. und den 25. Das möchte ich simulieren.“

Die Buchhaltungssoftware da draußen ist sehr leistungsfähig, aber keine traf genau „die Sorge, die mir heute im Kopf herumgeht“.

Also fasste ich einen Entschluss.

„Wenn es das nicht gibt, baue ich es. Ich habe ja Gemini, den stärksten Entwicklungspartner.“

### 6-2. Phasen 1–3: Von hingekritzelten Notizen in die „Cloud“

Die Entwicklung begann damit, dass ich Gemini meine Notizen in Google Keep zeigte.

![Die Keep-Notiz, die der Ausgangspunkt der Entwicklung war](images/fig-25.png)

#### Phase 1: Die Logik bauen

„Ich möchte die Berechnungen in dieser Notiz automatisieren.“

Auf meine Bitte hin stellte Gemini schnell die Berechnungslogik zusammen.

- Ändere ich den Betrag eines Postens, berechnet sie sofort den Endsaldo.

- Wenn die Mittel knapp zu werden drohen, zeigt sie eine „Warnung“ in Rot.

- Sie simuliert den Zahlungszeitpunkt, aufgeteilt in „den 10.“ und „den 25. / das Monatsende“.

- Die Daten werden im Browser (Cache) gespeichert.

Schon das war bequem genug, doch dann wollte ich mehr. „Ich möchte, dass die Daten auch nach dem Schließen des Browsers bleiben. Ich möchte sie auch auf dem Smartphone ansehen.“

#### Phase 2: Ein unbekanntes Werkzeug übernehmen – „Firebase“

Ich hatte daran gedacht, es mit einer Tabelle zu verknüpfen, doch Geminis Vorschlag kam unerwartet.

„Wenn man an Echtzeit und Effizienz denkt, nehmen wir Googles ‚Firebase‘. Das kostenlose Kontingent reicht für den Betrieb aus.“

„Firebase …?“ Das Wort hatte ich noch nie gehört. Aber mit dem Instinkt aus meiner Zeit als Systemkoordinator entschied ich: „Wenn die KI es so nachdrücklich empfiehlt, machen wir es so.“

Dank einer Datenbank namens Firestore wurden die Daten dadurch sicher in der Cloud gespeichert.

#### Phase 3: Google-Anmeldung und ein Freigabesystem

Es geht um Geld, da ist es schlecht, wenn alle es sehen können.

Zuerst dachte ich an so etwas wie ein „Passwort“, doch Gemini schlug vor: „Wenn Sie mehr Sicherheit wollen, nehmen wir die Google-Anmeldung.“

Als ich dann sagte: „Ich möchte, dass nur das Personal es sehen kann, das ich freigebe“, baute sie sogar „ein System, in dem die Administration Mitglieder am Bildschirm freigeben und entfernen kann“.

### 6-3. Phasen 4–5: Dem schwarzen Bildschirm (dem Terminal) die Stirn bieten

Ab hier kam die größte Hürde beim Vibe Coding: die App im Internet zu veröffentlichen (Deployment).

#### Warnung: Ab hier beginnt der „Schwarzgurt“-Kurs

Die nächsten Seiten sind der schwierigste „praktische“ Teil dieses Buchs. Sie bedienen einen „schwarzen Bildschirm (Terminal)“, wie ihn Hacker in Filmen benutzen.

Ich sage es ehrlich. Hier werden Sie ganz sicher auf Fehler stoßen. Mir ging es genauso. Sie laufen gegen Wände wie einen „PowerShell-Berechtigungsfehler“, der sich wie ein Zauberspruch liest. Aber haben Sie keine Angst. Was Sie hier tun, ist immer dasselbe: einfach „einen Screenshot vom Fehlerbildschirm machen und der KI hinwerfen“.

Die Wahrheit, die ich in meiner Zeit in der Systembranche gelernt habe, lautet: „Auch Profis bekommen Fehler. Der einzige Unterschied ist, ob man aufgibt, wenn einer erscheint, oder nach Hilfe sucht (fragt).“ Wenn es Ihnen zu schwer erscheint, überspringen Sie diesen Abschnitt und nehmen Sie nur die Möglichkeit mit: „So viel geht also mit KI.“

Gemini sagte:

„Wir richten die Entwicklungsumgebung auf Ihrem Windows-PC ein. Installieren Sie ‚Node.js‘ und geben Sie in ‚VS Code‘ die folgenden Befehle ein.“

Ich öffnete den schwarzen Bildschirm (das Terminal) wie angewiesen und bekam sofort einen Fehler.

„Kann wegen der Sicherheitsbeschränkungen von PowerShell nicht ausgeführt werden.“

Eine gewöhnliche Lokalleitung hätte hier den Mut verloren.

Ich aber kopierte den Fehlerbildschirm und warf ihn der KI hin.

Die KI antwortete sofort: „Heben Sie die Beschränkung mit einem Befehl namens ‚Set-ExecutionPolicy‘ auf.“

Ohne zu verstehen, was das bedeutete, tippte ich den Befehl ein, dann npm run build, firebase deploy …

Jedes Mal, wenn ich diese zauberspruchartigen Zeichen eintippte, lief Text über den Bildschirm, und der Vorgang kam voran.

Und schließlich erschien meine App im Web.

#### Phase 5: Daraus eine Smartphone-App machen (PWA)

Die veröffentlichte App war zunächst in einem „ungeschminkten“ Rohzustand, ganz ohne Gestaltung, doch auch das ließ sich lösen, indem eine Einstellung namens „Tailwind CSS“ ergänzt wurde.

Dann fragte ich: „Ich möchte ein Symbol auf den Startbildschirm meines Smartphones legen und es wie eine App benutzen“, und sie brachte mir die Einstellungen bei, um daraus eine „PWA (Progressive Web App)“ zu machen.

So entstand in meinem Smartphone eine eigene App, die ich (ohne eine einzige Zeile Code zu schreiben) gebaut hatte.

![Der Bildschirm der fertigen App zur Liquiditätsverwaltung](images/fig-26.png)

### 6-4. Phase 6: Das Problem nach 30 Tagen und die Lösung

Etwa einen Monat nach Beginn der Nutzung trat ein Problem auf.

„Bis gestern ging es, und plötzlich komme ich nicht mehr drauf!“

Ich geriet in Panik und fragte Gemini, und die Ursache lag an unerwarteter Stelle.

„Die Einstellungen der Datenbank (Firestore) standen noch im ‚Testmodus (auf 30 Tage begrenzt)‘. Er ist abgelaufen.“

Um die Mühe der Einrichtung zu Beginn der Entwicklung zu sparen, hatte die KI absichtlich eine Regel mit Ablaufdatum gesetzt.

„Schreiben wir die Sicherheitsregeln so um, dass ‚jede angemeldete Person sie weiter nutzen kann‘.“

Als ich einige Zeilen der Einstellungsdatei wie von der KI angewiesen umschrieb, funktionierte die App wieder einwandfrei.

Auch dieser Zwischenfall war für mich eine gute Erfahrung.

Ich lernte, dass „ein System etwas Lebendiges ist und Pflege braucht“.

Und ich gewann die Beruhigung, dass es „selbst bei Problemen immer eine Antwort gibt, wenn ich die KI frage“.

### 6-5. Fallbeispiel 2: Das „Gesichtserkennungsprojekt“, das mit einem Demovideo auf X (ehemals Twitter) begann

Hier ist eine weitere Systementwicklung, die ich in Angriff nahm, und die größte.

Es ist „ein System, das Gäste, die hereinkommen, über eine Kamera erkennt und mir diskret Namen, Daten und Vorlieben mitteilt“.

Es begann auf der Social-Media-Seite X, durch die ich beiläufig scrollte.

In meinem Feed tauchte ein Demovideo auf, das ein Entwickler gepostet hatte: Mit der in Google Chrome eingebauten KI (Built-in AI) wurde in Echtzeit erklärt, was eine Webcam sah.

Mein Instinkt als ehemalige Systemfachkraft meldete sich.

„Das ist ‚multimodal‘. Und wenn es im Browser eingebaut ist, könnte es dann nicht vollständig auf meinem eigenen PC laufen, ohne für die Cloud zu zahlen?“

Wenn das funktionierte, könnte ich ein Gastfreundschaftssystem nur für mein Lokal bauen, ohne ein teures System zu installieren.

Ich kopierte die URL und warf sie Gemini hin.

„Ich möchte dasselbe wie hier machen. Sag mir, wie man es umsetzt.“

#### Phase 1: Es funktionierte – doch das System erkannte nicht, „wer“ es war

Ich änderte die Chrome-Einstellungen (Flags) wie von Gemini angewiesen und fügte den Code ein, und dasselbe System wie in der Demo lief ohne Probleme.

Als ich vor der Kamera erschien, zeigte der Bildschirm Folgendes an:

„Eine Person mit Brille sitzt vor einem PC.“

Verwendet wird eine in den Browser eingebaute KI namens GeminiNano. Ihr Vorteil ist, dass sie komplett im Browser arbeitet, ohne sich mit der Cloud zu verbinden, aber sie erkennt nur allgemeine Dinge wie „Brille“ und „Person“. Bis zur Bestimmung, wer die Person ist, geht sie nicht.

Es ist eine erstaunliche Technologie. Aber als Betreiber eines Lokals war ich sofort enttäuscht.

„So geht das nicht.“

Ich will nicht ein allgemeines Merkmal wie „eine Person mit Brille“ wissen, sondern die Identifizierung der einzelnen Person: „Ist das A oder B?“

#### Phase 2: Die Hürde der Google-Fotos-Anbindung und die Antwort der KI

Also trug ich Gemini eine naive Idee vor.

„Verbinde dieses System mit meinen Google Fotos. Dort sind Gesichtsgruppierungsdaten von meinen Freundinnen, Freunden und Stammgästen, wenn man damit abgleicht, bekommt man die Namen, oder?“

Geminis Antwort war kühl, aber richtig.

„Es tut mir leid, aber das ist nicht möglich. Die Gesichtserkennungsdaten in Google Fotos sind hochsensible Privatsphäre-Informationen, und aus Sicherheitsgründen dürfen sie nicht von externen Programmen verwendet werden.“

Verständlich. Der Weg schien hier zu enden.

Doch ab hier kam das eigentliche Wesen von „Vibe Coding (Entwicklung im Dialog)“. Die KI lehnte nicht einfach nur ab.

#### Phase 3: Eine Alternative und ein Kurswechsel

Gemini schlug weiter Folgendes vor:

„Google Fotos können wir nicht verwenden, aber mit Open-Source-Bibliotheken (etwa OpenCV oder face_recognition) lässt sich in einer lokalen Umgebung ein eigenes Gesichtserkennungssystem bauen. Probieren wir es?“

Ich antwortete sofort mit „Ja“.

Von da an änderte sich der Entwicklungsplan komplett. Statt die Funktionen von Chrome zu nutzen, würde ich ein Gesichtserkennungssystem mit einer Programmiersprache namens Python von Grund auf bauen.

#### Phase 4: Der Kampf mit dem schwarzen Bildschirm und die Anbindung an eine Tabelle

Was ich tun musste, änderte sich nicht. Ich fragte Gemini, „wie man die nötigen Bibliotheken installiert“, und fügte die Antwort in den schwarzen Bildschirm (die Eingabeaufforderung) ein.

Als ein Fehler erschien, warf ich den roten Text unverändert zurück an Gemini.

Einige Stunden später war das System endlich fertig.

1.  Die Webcam erfasst mein Gesicht.

2.  Sie gleicht es mit den „Gesichtsfotodaten“ in einem Ordner auf dem PC ab.

3.  Bei einem Treffer schlägt sie in der Gästeliste in einer Google-Tabelle nach.

4.  Der Bildschirm zeigt: „Bonta: Restmenge der Vierkantflasche ○○ g.“

![Das laufende Gesichtserkennungssystem. Es erkennt das Gesicht des Autors und zeigt Informationen an. Das aufgenommene Bild wurde mit Gemini verpixelt](images/fig-27.png)

Kosten für Auftragsvergabe: ¥0 (ca. $0,00). Meine eigene Programmierarbeit: null.

Es war der Moment, in dem in einer Ecke von Higashi-Nakano ein einzigartiges „CRM-System mit Gesichtserkennung“ entstand.

#### Phase 5: Und dann wird mir die „Verantwortung zum Schutz“ bewusst

Das System war fertig. Doch mit der Freude lief mir ein Schauer über den Rücken.

„Moment mal. Auf diesem Computer liegen doch jetzt die Gesichtsdaten (biometrische Daten) von Gästen …?“

Bis dahin hatte ich gedacht: „Hauptsache, es funktioniert.“ Aber im echten Betrieb ist das etwas anderes.

Was, wenn sich dieser Computer mit einem Virus infiziert? Die Gesichtsdaten der Gäste und ihre Vorlieben (personenbezogene Daten) könnten zusammen abfließen.

Ein eigenständiger PC ohne Internetverbindung wäre sicher, aber solange ich Reservierungen und soziale Medien bearbeite, ist eine Internetverbindung unverzichtbar.

„Ein nützliches Werkzeug bauen zu können“ und „es sicher verwalten zu können“ sind zwei verschiedene Dinge.

Erst hier spürte ich wirklich, wie wichtig die „Cyberrisiko-Versicherung“ ist, von der eine Versicherungsvertretung gesprochen hatte, als sie mir früher ihr Angebot vorstellte.

Ich hatte gelacht: „Ein kleines Lokal wie unseres wird nicht Opfer von Cyberangriffen“, doch nun, da wir mit KI fortgeschrittene Systeme bauen können, tragen auch wir einzelnen Betreibenden die Verantwortung, ordentliche „Datenverwaltende“ zu sein.

Mit KI bekommt man magische Werkzeuge.

Aber ich lernte: Auch den „Zauberstab (Kompetenz)“ und den „Schild (Sicherheitsmaßnahmen)“ zu führen, um diese Magie zu nutzen, gehört künftig zu den Aufgaben derer, die ein Lokal führen.

### 6-6. Die „Verantwortung“ und die „Versicherung“, die mit der Freiheit kommen

#### Wichtig: Datenschutz und personenbezogene Daten

Dieses „Gesichtserkennungssystem“ ist ein experimenteller Prototyp, den ich gebaut habe, um zu testen, was technisch möglich ist. Würden Sie es in einem echten Lokal einsetzen, zählten die Gesichtsdaten Ihrer Gäste zu den „personenbezogenen Daten (biometrische Daten)“ und müssten nach dem Gesetz (dem japanischen Gesetz zum Schutz personenbezogener Daten) streng geschützt werden.

Wenn Sie erwägen, so etwas einzuführen, beachten Sie bitte unbedingt diese zwei Punkte.

Gäste informieren und ihre Einwilligung einholen: Es braucht ein Verfahren, etwa einen Aushang am Eingang mit dem Hinweis „Wir setzen KI-Gesichtserkennung ein“ und das Einholen der Einwilligung bei der Anmeldung als Mitglied. Heimliches Filmen ist unter keinen Umständen erlaubt.

Die Daten schützen: Es braucht Maßnahmen, die das Risiko eines Abflusses auf null bringen, etwa die Verwaltung der Daten in einer vom Internet getrennten Umgebung.

Etwas bauen zu können heißt nicht, es auch tun zu dürfen. Wenn Sie über technische Fähigkeiten verfügen und ein Lokal führen, denken Sie bitte daran, dass mit dieser Technik auch die Verantwortung für ihren Einsatz verbunden ist.

Bisher habe ich davon erzählt, wie wunderbar ein selbst gebautes System sein kann. Doch als Geschäftsführung muss ich Ihnen auch eine harte Wirklichkeit erzählen.

Sie lautet: „Für alles, was Sie selbst bauen, sind Sie selbst verantwortlich.“

Bei einem Dienst im Monatsabo (SaaS) entschuldigt sich das Unternehmen, wenn der Server ausfällt, und bringt ihn wieder zum Laufen.

Ein mit Vibe Coding gebautes System aber hat keinen „Kundendienst“.

Wenn Ihre App mitten in der Mittagsspitze plötzlich nicht mehr funktioniert, kommt niemand zu Hilfe.

Wenn Google eine Spezifikation ändert und Code, der gestern noch einwandfrei lief, heute Fehler wirft, ist das alltäglich.

Deshalb treffe ich zwei Vorkehrungen.

Die eine ist ein „analoges Backup“.

„Wenn die Gesichtserkennung ausfällt, schaue ich ins Gästebuch auf Papier.“ „Wenn die Kassen-App ausfällt, nehme ich einen Taschenrechner und handgeschriebene Zettel.“

Digitale Werkzeuge sind nur „praktische Hilfsmittel“. Man darf sich nicht so sehr auf sie verlassen, dass das Lokal stillsteht, wenn sie ausfallen.

Die andere ist die „Versicherung“, die ich vorhin erwähnt habe.

Eine Cyber-Haftpflichtversicherung deckt nicht nur das Risiko eines Datenlecks ab, sondern auch den Ersatz für entgangene Geschäfte, wenn das System durch eigene Fehler ausfällt. Für eine einzelne Person, die sich mit IT wappnet, gehört sie zum verantwortungsvollen Erwachsensein.

„Manchmal wird etwas ausfallen. Manchmal werde ich Fehler machen.“

Das als gegeben nehmen, das Risiko annehmen und dagegen Vorkehrungen treffen.

Nur mit dieser Entschlossenheit können wir ein „freies System“, das an niemanden gebunden ist, wirklich nutzen.

### 6-7. Sie brauchen keine Fachleute. Sie brauchen Beharrlichkeit

Für die Entwicklung dieser beiden Systeme habe ich keinen einzigen Yen an Auftragskosten gezahlt.

Ich habe nur ein KI-Abonnement für einige tausend Yen im Monat genutzt und die Beharrlichkeit von jemandem, der dachte: „Diese Sorge (um den Geldfluss) muss unbedingt weg“ und „Ich möchte meine Gäste glücklich machen“.

Es geht nicht darum: „Ich kann es nicht, weil ich nicht programmieren kann.“

Wenn Sie etwas bauen möchten (das Was), bringt die KI Ihnen bei, wie man es baut (das Wie).

Selbst wenn Wörter auftauchen, die Sie nicht verstehen (Node.js, PowerShell, Firestore …), gibt es nichts zu fürchten.

Wir haben den stärksten Partner, den es gibt, „Gemini“, der sie übersetzt und uns anleitet.

#### Kolumne 4: Was ist der Unterschied zwischen Excel und einer Datenbank (Firestore)?

~ Ist es eine „Notiz zum Lesen für Menschen“ oder ein „Register zum Lesen für das System“? ~

In der Entwicklung der App zur Liquiditätsverwaltung tauchte Firebase (Firestore) auf. Vielleicht haben Sie sich gefragt, warum nicht Excel?

Eine Tabellenkalkulation (Excel) ist ein „Notizbuch, das Menschen ansehen und in das sie tippen“. Sie ist sehr flexibel, aber für ein System bleibt unklar, „was wo steht“.

Eine Datenbank (Firestore) dagegen ist ein „sauber geordnetes Schließfach, das für das System gemacht ist“. Weil festgelegt ist, dass „das Datum in Fach 1 und der Betrag in Fach 2 liegt“, kann ein Programm es sofort verarbeiten. Sie geht auch nicht kaputt, wenn mehrere Personen gleichzeitig darauf zugreifen.

„Wenn Sie eine App bauen, nehmen Sie eine Datenbank, nicht Excel.“ Allein dieses Wissen hebt das Niveau Ihrer Anweisungen an die KI.

## Nachwort: Ein „Rezept für die Zukunft“, das es nur in Ihrem Lokal gibt

~ KI ist keine schwierige Technik. Sie ist ein neuer Partner für das „Gespräch“ ~

Vielen Dank, dass Sie dieses Buch bis zum Ende gelesen haben.

Wenn Sie aus diesem Buch nur eines ausprobieren, dann dies: „Fügen Sie diese lästige LINE-Nachricht direkt in die KI ein und bitten Sie sie, sie ‚in ein Diagramm zu verwandeln‘.“

Ich bin keine besondere KI-Fachperson. Ich habe lediglich jeden Tag geübt, „mit der KI in der Sprache der Praxis zu sprechen“, \
auf dem Schlachtfeld eines Restaurants.

Deshalb genügt es meiner Ansicht nach, wenn Sie aus diesem Buch nicht eine „Sammlung richtiger Antworten“, sondern nur eine „Denkweise“ mitnehmen.

Als Sie die erste Seite aufschlugen, welches Bild hatten Sie von den Worten „KI nutzen“?

„Klingt schwierig.“ „Man braucht Programmierkenntnisse, oder?“ „Das hat mit einem kleinen Lokal wie meinem nichts zu tun.“

Vielleicht haben Sie so etwas gedacht.

Aber nachdem Sie diese Aufzeichnung meines „Ausprobierens“ bis hierher gelesen haben, hat sich dieses Bild vielleicht ein wenig gewandelt.

Was ich getan habe, war nicht, fortgeschrittene IT-Technik voll auszuschöpfen.

Ich habe gemurrt: „Das schaffe ich von Hand nicht.“ Ich habe geklagt: „Das ist schwer zu bedienen.“ Und ich habe Extrawünsche geäußert: „Ich möchte, dass es eher so funktioniert.“

Heutzutage ist in der Welt der Entwickelnden der Begriff „Vibe Coding“ ein Trend.

Das ist eine Methode, im Gespräch mit KI ein System nach Gefühl zu bauen.

So wie Shogi-Profis im Gespräch mit KI die nächsten Züge durchdenken, können auch wir mit der KI sprechen und die „Zukunft unserer Lokale“ bauen.

Wie man dem Küchenteam sagt: „Gib noch etwas mehr Salz dazu.“

Wie man auf dem Markt im Fischhandel fragt: „Gibt es heute guten Fisch?“

Mit der KI zu sprechen und zu sagen: „Mach mir diese Arbeit leichter.“ Dort beginnt alles.

Ich habe einmal in der Systemabteilung eines Unternehmens gearbeitet und zwischen der „Praxis“ und den „Entwickelnden“ vermittelt.

Jetzt tue ich dasselbe zwischen „meinem eigenen Lokal“ und der „KI“.

Und von einem bin ich überzeugt:

„Wer die Sorgen der Praxis kennt und ein Lokal führt, kann zur stärksten KI-Kommandozentrale werden.“

Fangen auch Sie noch heute damit an.

Zuerst holen Sie Ihr Smartphone heraus und sprechen mit Gemini.

„Hallo, wo fange ich bei der heutigen Vorbereitung an?“

„Wie kann ich dieses Gericht besser verkaufen?“

„Dieser Papierkram nervt. Kannst du da etwas tun?“

Machen Sie sich keine Sorgen, wenn ein Fehler erscheint. Er ist ein Zeichen, dass das „Gespräch“ begonnen hat.

Machen Sie einfach einen Screenshot und schicken Sie ihn mit „irgendetwas stimmt nicht“ zurück.

Am Ende dieser vielen aufeinander aufbauenden Gespräche warten „Zeit“ und „Luft zum Atmen“, die Sie sich nie hätten vorstellen können, und „eine Zukunft, die nur Ihrem Lokal gehört“.

Nun, stellen wir auch für Ihr Lokal eine verlässliche „stellvertretende Lokalleitung“ ein.

Denn das Rezept für die Zukunft entsteht im Gespräch zwischen Ihnen und der KI.

### Drei Wege, wie es nach diesem Buch weitergehen kann

Dieses Buch ist kostenlos als PDF, auf note und bei Google Play zu lesen. (Nur bei Kindle verlangen die Regeln des Stores einen Mindestpreis.) Stattdessen habe ich drei Anlaufstellen vorbereitet, die Sie nach der Lektüre nutzen können. Wenn Sie auch nur einen davon nutzen, hat sich das Schreiben dieses Buchs gelohnt.

1. Probieren Sie es in Ihrem eigenen Lokal aus. Die Agenda-Reihe lässt sich mit einem kostenlosen Notizbuch beginnen. https://bontallc.com/agenda?via=b1-de-{{FMT}}
2. Verfolgen Sie, was ich tue. Auf note und X schreibe ich über die Werkzeuge, die ich als Nächstes baue, und über den Alltag in der Bar. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Wenn Sie einmal in Tokio sind, besuchen Sie Tamuro. Eine Minute vom Osteingang des Bahnhofs Higashi-Nakano. Sie können ohne Reservierung hereinkommen. Als dieses Buch zuerst geschrieben wurde, war Tamuro nur auf Empfehlung zugänglich. Heute ist jede Person willkommen, ohne Reservierung. Reservierungsseite https://tamuroreservation.vercel.app/?src=b1-de-{{FMT}}

An alle, die wegen dieses Buchs zu uns kommen: Geben Sie bei der Reservierung bitte den Gutscheincode „BOOK“ ein. Beim ersten Besuch spendieren wir Ihnen ein Getränk. Wenn Sie ohne Reservierung gekommen sind, sagen Sie bei der ersten Bestellung einfach „Ich komme wegen des Buchs“. Wir servieren Ihnen dasselbe Getränk. Es ist ein kleiner Kniff, damit ich zählen kann, wie viele Menschen wegen des Buchs gekommen sind.

### Über den Autor

Raku Bonta

Betreibt allein ein Restaurant mit 11 Theken- und 8 Tatami-Plätzen in Higashi-Nakano, Tokio.

Tagsüber ist es ein Hamburger-Curry-Laden, in dem es nach Gewürzen duftet. Abends ist es eine Dining-Bar nur auf Empfehlung mit täglich wechselndem Menü.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry](images/fig-28.png)

▼ Bar nur auf Empfehlung „Tamuro“

https://www.instagram.com/tamuro.higashinakano/

![Bar nur auf Empfehlung „Tamuro“](images/fig-29.png)

Das Lokal engagiert sich auch für den Aufbau von Gemeinschaft durch Essen, mit Weinveranstaltungen alle zwei Wochen, einem monatlichen Kochkurs und mehrgängigen Dinnern.

Vor der Eröffnung des eigenen Lokals vor 12 Jahren arbeitete Raku Bonta in einem Unternehmen in der „Systemplanung“ und der „Lösungsarchitektur“.

Die Titel klingen schwierig, aber die eigentliche Arbeit war die einer „Koordination, die die Wünsche der Praxis – ‚Wir wollen das tun‘ – genau an IT-Dienstleister weitergibt und umsetzen lässt“. Kein Entwickeln mit fortgeschrittener Programmierung, sondern ein Werdegang im „Übersetzen“, das Menschen und Technik verbindet.

Heute nutzt Raku Bonta diese Erfahrung und betreibt das eigene Lokal mit generativer KI wie Google Gemini, setzt „eine Betriebsverbesserung, die auch ohne Fachwissen funktioniert“ in die Praxis um und gibt sie öffentlich weiter.
