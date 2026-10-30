### 1-6 Zu viele Angebote zur Auswahl

Als das Rabattsystem stand, wollte ich als Nächstes die Zeiten und Angebote ausbauen, die sich verkaufen.

Die Stunde um 18 Uhr füllte sich nicht, also schuf ich eine Happy Hour bis 19 Uhr. Für Menschen, die nach dem Essen kommen, schuf ich ein Angebot nur zum Trinken, ohne Essen. Das Menü-Dinner und den Kochkurs, die früher monatlich stattfanden, machte ich zu Veranstaltungen auf Anfrage, die zustande kommen, sobald sich jemand anmeldet, und nahm sie über die Reservierungsseite entgegen. Um die Zeit vor der Öffnung an Wochenenden ab 15:30 Uhr zu verkaufen, schuf ich ein Party-Angebot für Gruppen ab sechs Personen.

Jedes hat seinen Grund. Beim Party-Angebot zum Beispiel: Hätte ich es preislich wie ein Schnäppchen aussehen lassen, hätte es nur Gäste angezogen, die bisher das Standardangebot gewählt hatten, und der Umsatz wäre gesunken. Also habe ich die Abgrenzung nicht über den Preis gezogen, sondern über die Zeit vor der Öffnung, in der es bisher nie Umsatz gab. Der Happy-Hour-Rabatt bringt keinen Gewinn, wenn er mit anderen Rabatten kombiniert wird, also habe ich festgelegt, dass er sich nicht kombinieren lässt.

So vermehrten sich die Angebote. Standard, Premium, Erstes Mal, Willkommen zurück, Happy Hour, Nur Trinken, Menü-Dinner, Kochkurs, Party. Für jedes gelten Bedingungen zur Personenzahl, bei manchen greifen Rabatte und bei manchen nicht, und es gibt zeitliche Einschränkungen.

Eines Tages öffnete ich das Reservierungsformular und merkte: Damit können Gäste nicht auswählen.

Da ich alles selbst gebaut habe, verstehe ich jeden Unterschied. Aber kann jemand, der die Reservierungsseite zum ersten Mal öffnet, neun Angebote und ihre Rabattbedingungen vergleichen und das passende wählen? Wenn nicht, geben die Leute mitten in der Buchung auf. Die Angebote, die ich mühsam ergänzt hatte, könnten am Ende die Reservierungen verringern.

Ich hätte aufräumen können. Aber jedes Angebot hat eine Zeit, die ich verkaufen möchte, und Gäste, die ich gern im Lokal hätte. Ich wollte keines streichen.

Da kam ich auf ein System, in dem die Gäste die KI um Rat fragen und sich so für ein Angebot entscheiden. Man nennt die Personenzahl, Datum und Uhrzeit, zu der man kommen möchte, und wie man den Abend genießen will, und die KI nennt das passende Angebot samt Preis und führt direkt zur Buchung. Die Komplexität der Angebote trägt das Lokal. Für die Gäste bleibt nur ein Gespräch.

Dieses System ist das „T-AI-MURO“, über das ich in 1-8 schreibe. Davor gibt es noch etwas, das mir in dieser Zeit aufgefallen ist.

【Abbildung 1-2】Angebotsauswahl im Reservierungsformular. So viele Tabs stehen nebeneinander *(Die Bildschirmanzeige ist auf Japanisch.)*

### 1-7 „Bringt das wirklich Gäste?“

An dem Tag, an dem ich das Party-Angebot ergänzte, verbrachte ich den ganzen Tag damit, die Reservierungsseite Schritt für Schritt zu verbessern. Ich straffte den Kopfbereich, glich das E-Mail-Design an und tauschte die KI aus, die Gesprächsthemen für die Gäste im Lokal erstellt.

Am Abend kam mir plötzlich eine Frage.

„Hilft das wirklich dabei, mehr Gäste zu gewinnen?“

Als ich die KI fragte, sortierte sie die Verbesserungen dieses Tages ehrlich.

| Kategorie | Verbesserungen an diesem Tag |
| --- | --- |
| Was neue Reservierungen schaffen kann | Party-Angebot, der Zeitraum ab 15:30 Uhr an Wochenenden und Feiertagen |
| Was die Abschlussquote der Besucher der Reservierungsseite erhöht | Straffung des Kopfbereichs, Angleichung der Tabs |
| Was zu Wiederholungsbesuchen anregt | Vereinheitlichung des E-Mail-Designs |
| Was nicht dabei hilft, Gäste zu gewinnen | Wechsel der KI für Gesprächsthemen, der Link zum zweiten Lokal, der Agenda-Hinweis |

Von den Verbesserungen dieses Tages führten nur das Party-Angebot und der Zeitraum ab 15:30 Uhr direkt dazu, Gäste zu gewinnen. Der Rest waren Verbesserungen, damit man Interessierte auf der Reservierungsseite nicht verliert. Auch sie sind wichtig, aber sie vermehren die Gäste nicht.

Es gab ein größeres Problem. Bei keiner der Verbesserungen hatte ich eine Möglichkeit zu messen, ob sie gewirkt hat. Es gab keine Zahl, die „Ich habe es verbessert“ und „Es kamen mehr Gäste“ miteinander verbindet.

Meine Antwort war kurz: „Dann bauen wir eine.“

So machte ich mich daran, einen wöchentlichen Bericht zur Gästegewinnung zu erstellen. Die Zahl der Reservierungen, die Zahl der Gäste, der Gesamtbetrag, Stornierungen. Aufschlüsselungen nach Wochentag und nach Tageszeit. Das Verhältnis von Erstgästen zu wiederkehrenden Gästen. Die Zahlen für Party und die Zeit ab 15:30 Uhr. Woher die Reservierungen kamen (Reservierungsformular, Chatfenster, Reservierungen über KI, manuelle Eingaben durch das Lokal). Klickzahlen in E-Mails und die Zahl der Reservierungen innerhalb von sieben Tagen nach diesen Klicks.

Wo es Zahlen gibt, folgen Zeitfragen. Am selben Tag hatte ich noch ein Loch gefunden. Ich hatte den Kochkurs und den Zeitraum ab 15:30 Uhr für Partys als „Wochenenden“ festgelegt, aber als ich mich fragte „Was passiert an Feiertagen?“ und nachsah, kannte das Reservierungssystem gar keinen Begriff von Feiertagen. An einem Feiertagsmontag hat das Lokal geöffnet, doch der Zeitraum ab 15:30 Uhr erschien nicht. Ich gab dem System eine Liste der Feiertage und korrigierte es so, dass sie wie Wochenenden behandelt werden. Es war eine Lücke, die niemandem auffällt, bevor die Person, die das System gebaut hat, sie selbst bemerkt.

Bevor ich den Bericht baute, stopfte ich zuerst die Lücken rund um die Zeit.

Selbst Stammgäste, die schon kamen, bevor ich das Reservierungssystem nutzte, erscheinen in den Aufzeichnungen wie „Erstgäste“. Deshalb schreibe ich im Bericht „erster Besuch in den Aufzeichnungen“ und füge immer das Datum an, ab dem die Aufzeichnungen beginnen. Um zu beurteilen, ob eine Verbesserung gewirkt hat, braucht man das Bild davor. Für den ersten Bericht habe ich die letzten acht Wochen rückwirkend ausgezählt und als Ausgangswert genommen. In einer Woche, in der das Lokal vorübergehend schloss, etwa wegen einer Reise, sinken die Reservierungen naturgemäß. Deshalb führe ich auch die Zahl der Öffnungstage auf, damit man pro Öffnungstag vergleichen kann.

Den Abschnitt „Auffällige Veränderungen“ lasse ich nicht von der KI schreiben, sondern nach festen Berechnungen und festen Sätzen erzeugen. So bleiben die wöchentlichen Kosten bei null. Namen und Kontaktdaten der Gäste erscheinen nicht im Bericht, es werden nur Anzahlen und Verhältnisse gezeigt.

Nachdem ich eine Möglichkeit zum Messen gebaut hatte, veränderte sich die Art, wie ich Verbesserungen baue, selbst. Ich begann, eine Verbesserung und die Methode zur Messung ihrer Wirkung von Anfang an gemeinsam festzulegen. Messen ist nichts, worüber man nach der Verbesserung nachdenkt, es gehört in dasselbe Auftragsdokument wie die Verbesserung. Das habe ich an diesem Tag gelernt.

【Abbildung 1-6】Der Bericht zur Gästegewinnung, der jede Woche eintrifft (synthetische Daten) *(Die Bildschirmanzeige ist auf Japanisch.)*

### 1-8 Ein Fenster, um mit dem Lokal zu sprechen: „T-AI-MURO“

Wie ich in 1-6 geschrieben habe, hatten sich die Angebote vermehrt, und das Reservierungsformular war für Erstbesuchende schwer zu überblicken. Und Erstgäste wollen mehr wissen als Angebote und Termine. Was für eine Atmosphäre hat der Ort? Fühle ich mich allein fehl am Platz? Was für ein Mensch führt das Lokal? Darf ich Kinder mitbringen? Reiht man Reservierungsknöpfe aneinander, ohne solche Fragen zu beantworten, kann man Zögernden nicht den nötigen Anstoß geben.

Also beschloss ich, auf der Reservierungsseite ein „Fenster, um mit dem Lokal zu sprechen“ einzurichten. Schreiben Gäste eine Frage, antwortet die KI als das Lokal. Klären sich im Gespräch Personenzahl und Datum, können die Gäste direkt zum Bestätigungsbildschirm der Reservierung gehen. Es heißt „T-AI-MURO“ und stellt sich im Gespräch als „Tamuro“ vor. T-AI-MURO spricht als das Lokal selbst und redet über die Lokalleitung in der dritten Person.

Die Gäste tippen kaum etwas. Sie tippen nur die Auswahlmöglichkeiten an, die T-AI-MURO anbietet, und das Gespräch geht voran. Das heißt, die Auswahlmöglichkeiten, die als Nächstes angeboten werden, entscheiden über die Qualität des Gesprächs. In die Auswahl mische ich immer drei Arten von Schritten: Schritte hin zu einer Reservierung (Personenzahl, Preis, freie Zeiten, Datum und Uhrzeit), Schritte, um das Lokal kennenzulernen (Atmosphäre, die Lokalleitung, wer die Gäste sind, ob man mit der Person nebenan reden kann) und Schritte, die sich aus dem Gesprächsverlauf ergeben. Menschen zur Reservierung zu bringen ist nicht das einzige Ziel. Sie die Atmosphäre des Lokals und die Lokalleitung kennenlernen zu lassen, ist ebenfalls der Kern dieses Fensters.

Nur Preise, so entschied ich, soll die KI nicht berechnen. Es gibt keine Garantie, dass die KI jedes Mal richtig ausrechnet, wie Rabatte zusammenwirken oder wie die Stufen nach Personenzahl greifen. Das Programm erzeugt Preise und freie Zeiten mit festen Berechnungen, und die KI bleibt bei der Aufgabe, sie in Worte zu fassen.

#### Das erste Wissen stammte aus meinen eigenen früheren Beiträgen

Damit T-AI-MURO Fragen zum Lokal beantworten kann, braucht es Wissen über das Lokal. Als Material habe ich alle Beiträge exportiert, die ich bis dahin auf Instagram und X (früher Twitter) geschrieben hatte, und sie verwendet. Daraus habe ich die Fragen gebaut, die Gäste wahrscheinlich stellen, und die Antworten.

Beim Ausprobieren zeigte sich, dass sich X-Beiträge besser als Material eigneten als Instagram. Instagram besteht überwiegend aus Fotos und hat wenig Worte. Auf X hatte ich in eigenen Worten schriftliche Aufzeichnungen zum Essen, zum Lokal und zu meinen Gedanken hinterlassen.

#### Nur 9 von 36 bestanden

Bevor ich T-AI-MURO in Betrieb nahm, testete ich, wie korrekt es antworten kann. Auch die Tests ließ ich von KI durchführen. Ich gab einer KI, die einen Gast spielt, eine Rolle und ein Anliegen und ließ sie mit T-AI-MURO sprechen. Ich bereitete 36 Szenarien vor: „allein heute Abend“, „4 Personen in zwei Wochen“, „mit Kind“, „Allergien“, „geschlossene Gesellschaft“, „Hinweis auf Verspätung“, „Herkunft des Namens des Lokals“, „was für ein Mensch die Lokalleitung ist“ und so weiter.

Das Ergebnis der ersten Runde: 9 von 36 bestanden.

Am häufigsten war die Antwort „Es tut mir leid, das konnte ich nicht gut beantworten.“ Diese Antwort kam sogar bei Fragen zur Atmosphäre des Lokals und zur Lokalleitung. Sobald Wörter wie „Reservierung“, „heute“, „geschlossene Gesellschaft“ oder „Chef“ vorkamen, erschien eine Liste freier Zeiten, ganz gleich, worum es in der Frage eigentlich ging. In manchen Gesprächen wurde die Nachricht über eine Verspätung als neue Reservierung aufgefasst. Einem vegetarischen Gast nannte es gebratene Gerichte mit Bonitoflocken und Misosuppe als Beispiele. Es gab sogar auf Englisch Auskunft zu einem Gruppenkauf, den wir längst eingestellt hatten.

#### Ich beantwortete 11 Fragen mit je einer Zeile

Ein Teil der Ursache lag in der Bauweise des Programms. Diese Geschichte hebe ich mir für Kapitel 2 auf. Die andere Ursache war einfach: Es fehlten Tatsachen über das Lokal. Eine KI kann nicht beantworten, was sie nicht weiß.

Also sammelte ich die Fragen, die die KI nicht beantworten konnte, und beschloss, sie selbst zu beantworten, jeweils in einer Zeile.

Sie können ohne Reservierung hereinkommen. Mit Kindern unter Grundschulalter ist ein Besuch leider schwierig. Stornierungen und Änderungen bis zum Vortag, per E-Mail, Telefon oder Nachricht in sozialen Medien. Bei Verspätung bitte anrufen. Vor dem Lokal gibt es einen Raucherbereich. Eigene Getränke mitzubringen ist gegen Korkgeld erlaubt. Eine Buchung des ganzen Lokals ist je nach Preisklasse und Zeit möglich, höchstens 19 Personen. Auf Ernährungseinschränkungen und Jubiläen gehen wir so weit wie möglich ein, bitte sprechen Sie uns vorher an. Die Lokalleitung ist an fast jedem Öffnungstag im Lokal. Etwa einmal im Jahr ist ein Yukata-Fest geplant.

Das ist alles. Allein dadurch, dass ich 11 Fragen mit je einer Zeile beantwortete, bestanden im zweiten Test 24 von 36.

| Frage | Erste Antwort | Zweite Antwort |
| --- | --- | --- |
| Geht es mit Kindern? | Es tut mir leid, das konnte ich nicht gut beantworten | Ab Grundschulalter ist es nach Absprache möglich. Mit Kindern unter Grundschulalter ist ein Besuch leider schwierig |
| Komme ich ohne Reservierung hinein? | (Liste freier Zeiten) | Sie können ohne Reservierung hereinkommen |
| Ist die Lokalleitung heute da? | (Liste freier Zeiten) | Die Lokalleitung ist an fast jedem Öffnungstag im Lokal. Heute ist ein Öffnungstag, daher ist sie voraussichtlich da |
| Ist es ein ruhiger Ort? Alles Stammgäste? | Es tut mir leid, das konnte ich nicht gut beantworten | Es ist ein Ort zum Entspannen. Man kommt leicht ins Gespräch mit anderen Gästen, und es geht nicht laut zu |

Hier begann sich ein Muster abzuzeichnen. Die KI erstellt die Fragen, die wir erwarten, T-AI-MURO beantwortet sie, und wir korrigieren die Fehler. Dann werden nur die Fragen an die Lokalleitung weitergegeben, die sich nicht beantworten lassen, weil Tatsachen über das Lokal fehlen. Der Aufwand der Lokalleitung besteht nur aus einer Zeile für jede unbeantwortbare Frage. Alles andere erledigt die KI.

#### Die Szene, in der „Budget ¥5.000 (ca. $33)“ scheiterte

Auch den KI-Tests hatte ich ein KI-Urteil beigegeben. Eine andere KI liest das Gesprächsprotokoll und entscheidet über bestanden oder durchgefallen.

Darunter war ein Szenario mit einem Gast, dessen „Budget ¥5.000 (ca. $33)“ beträgt. Das Urteil der KI lautete: bestanden. T-AI-MURO hatte höflich Angebote innerhalb des Budgets vorgestellt.

Als ich es aber las, war es durchgefallen. Es hatte nicht nach der Personenzahl gefragt. Tamuro hat einen Gruppenrabatt. Je nach Personenzahl ändern sich die Angebote, die man mit demselben Budget wählen kann.

An diesem Punkt formulierte ich das Ziel neu.

„Ziel ist eine möglichst große Gruppe, damit ein möglichst hoher Gesamtbetrag zusammenkommt. Frage nach der Personenzahl. Das Endziel ist, dass Gäste kommen. Je mehr, desto besser. Um den Umsatz zu steigern.“

Mit diesem einen Satz änderte sich der gesamte Aufbau des Gesprächs. Vor der Antwort auf Fragen zu Preisen immer die Personenzahl erfragen und mit dem Gesamtbetrag antworten. Kurz vor einer Stufe des Gruppenrabatts den Hinweis ergänzen, „mit einer weiteren Person erhalten Sie so und so viel Prozent Nachlass“. Wird ein Budget genannt, zuerst das höchste Angebot innerhalb des Budgets zeigen. Da Gäste, die allein kommen, aber die Hälfte des Lokals ausmachen, schlägt man Einzelgästen nicht vor, die Gruppe zu vergrößern.

Lässt man KI die KI-Tests durchführen, laufen sie schnell. Aber den Maßstab für das Bestehen legt ein Mensch fest. Ob man das Ziel in einem Satz sagen kann. Das entschied über die Qualität der Gespräche der KI.

#### Der Wunsch der Gäste hat Vorrang vor der Empfehlung des Lokals

Es gab noch eine Szene, in der ich eine wichtige Grenze zog.

Beim Testen fand ich ein Problem: Jede Reservierung wurde auf das günstigste Angebot geleitet. Als ich das korrigierte, wurde diesmal fast alles zum Standardangebot, und der durchschnittliche Gesamtbetrag sprang auf etwa das Doppelte. Ich wollte mich schon freuen, aber bei genauerem Hinsehen hatte die als Gast auftretende KI jedes Mal einfach die erste Auswahl gedrückt. Selbst Gästen, die sagten „das Günstigste genügt“, wurde das Standardangebot empfohlen.

Hier legte ich einen Grundsatz fest. Was Gäste ausdrücklich wünschen (das Günstigste, ein Budget, der Name eines Angebots), hat immer Vorrang vor der Empfehlung des Lokals. Die Empfehlung des Lokals gilt nur, wenn die Gäste nichts gesagt haben.

Das Ziel des Lokals, den Umsatz zu steigern, und das Vertrauen der Gäste können schon durch die bloße Art der Empfehlung aufeinanderprallen. Geht das Vertrauen verloren, sinken die Besuche selbst. Diese Grenze konnte nicht die KI ziehen, sondern nur die Lokalleitung.

Als ich T-AI-MURO später mit einer großen Zahl von Fragen nachtrainierte, war die häufigste Fehlerursache, „auf Wörter zu reagieren und ein festes Schema abzuspulen, bevor die Frage beantwortet ist“. Sobald es Wörter wie „Personenzahl“, „wie viel“ oder „allein“ hörte, übersprang es die Frage und ging zum Reservierungsablauf oder zu Empfehlungen über. Im Service entspricht das einer Servicekraft, die einen Verkauf durchdrückt, ohne den Gästen zuzuhören. Zuerst die Frage der Gäste beantworten. Diese Grundregel der Gastfreundschaft war selbst für KI die größte Herausforderung.

Am Abend des 6. Oktober 2026 erschien T-AI-MURO ganz oben auf der Reservierungsseite als der eigentliche Eingang. Da manche Gäste nicht im Gespräch buchen möchten, habe ich das bisherige Reservierungsformular daneben beibehalten.

> Probieren Sie es aus: Öffnen Sie die Reservierungsseite von Tamuro (https://tamuroreservation.vercel.app/?src=b2-de-{{FMT}}) und sagen Sie T-AI-MURO „allein heute Abend“. Das Gespräch führt Sie bis zu den heutigen freien Plätzen und Preisen.

【Abbildung 1-4】Der Gesprächsbildschirm von T-AI-MURO. Das Gespräch geht allein durch Antippen von Auswahlmöglichkeiten voran *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 1-10】Nicht beantwortbare Fragen sammeln sich im Verwaltungsbildschirm (synthetische Daten) *(Die Bildschirmanzeige ist auf Japanisch.)*

### 1-9 Und dann, von der KI der Gäste aus

Mit dem Bau von T-AI-MURO hat die Reservierungsseite von Tamuro die Fähigkeit gewonnen, „Fragen zum Lokal im Gespräch zu beantworten, Preise und freie Zeiten zu zeigen und Menschen bis zur Reservierung zu führen“.

Als Nächstes dachte ich daran, dasselbe auch von der eigenen KI der Gäste aus möglich zu machen.

T-AI-MURO kann nur mit Menschen sprechen, die auf die Reservierungsseite von Tamuro kommen. Aber viele Menschen fragen zuerst die KI, die sie üblicherweise nutzen. Kennt diese KI Tamuro nicht, taucht Tamuro nicht einmal als Vorschlag auf. Statt darauf zu warten, dass Gäste auf die Seite von Tamuro kommen, öffne ich in der KI der Gäste ein Fenster zu Tamuro. Das ist der MCP-Server.

Ehrlich gesagt zögerte ich anfangs, ihn zu bauen. Noch buchen nicht viele Menschen Restaurants über ihre eigene KI. Weil ich keinen direkten Anstieg der Reservierungen erwarten konnte, stufte ich die Priorität einmal herab und legte ihn auf Eis.

Ich entschied mich trotzdem für den Bau, weil ich dachte, dass es nur eine Frage der Zeit ist, bis sich der Zugangsweg ändert. Wie ich eingangs geschrieben habe, wurde es im August 2026 möglich, über einen großen Reservierungsdienst aus ChatGPT heraus zu reservieren. Früher oder später wird es normal sein, sich ein Restaurant von einer KI suchen zu lassen. Wenn es so weit ist, fallen kleine Lokale, die bei den großen Diensten nicht gelistet sind, aus dem Blickfeld der KI. Also: das Fenster öffnen, bevor sich der Zugangsweg ändert.

Was ich für die erste Version festlegte, war sehr eng gefasst. Sie musste nur dasselbe können wie das Gesprächsfenster auf der Reservierungsseite (T-AI-MURO). Sie kann nur die Informationen des Lokals, freie Zeiten und Preise auslesen und die URL einer Reservierungsseite mit bereits eingetragenen Angaben übergeben. Die Reservierung bestätigen die Gäste selbst auf der Seite von Tamuro. Die KI der Gäste bestätigt keine Reservierung eigenmächtig. Den letzten Klick macht ein Mensch.

Kehren wir zur Eröffnungsszene zurück.

An einem Freitagabend fragt ein Gast die eigene KI: „Gibt es in Higashi-Nakano heute Abend einen Ort, wo ich allein etwas trinken kann?“ Die KI fragt das Fenster von Tamuro ab. Das Reservierungssystem von Tamuro liefert die freien Plätze für heute Abend sowie das Angebot und den Preis, die zu Einzelgästen passen. Die KI teilt es dem Gast mit und bietet eine Reservierungsseite von Tamuro an, in der Datum, Uhrzeit und Personenzahl eingetragen sind.

Alles, worüber ich in diesem Kapitel geschrieben habe, trägt diese Abfolge von Schritten. Das Rabattsystem, das zusammen mit der Preiserhöhung gebaut wurde. Das System, das die Stammkundschaft pflegt. Die Daten, die zeigten, dass die meisten Reservierungen am selben Tag gemacht werden. Das Wissen über das Lokal, das durch je eine kurze Antwort auf 11 Fragen gewachsen ist. Der Grundsatz, den Wunsch der Gäste vor die Empfehlung des Lokals zu stellen.

Ein Lokal, das über KI gebucht wird, ist nicht über Nacht entstanden. Es steht auf der Anhäufung kleiner Systeme, die einzeln hinzugefügt, getestet, verworfen und repariert wurden.

> Probieren Sie es aus: Registrieren Sie den MCP-Server von Tamuro (https://tamuroreservation.vercel.app/api/mcp) bei Ihrer eigenen KI und fragen Sie: „Ist bei Tamuro heute Abend noch Platz?“ Wie man ihn registriert, steht im Nachwort.

### 1-10 Was ich gebaut habe und was gewirkt hat

In diesem Kapitel habe ich erzählt, wie ich viele Systeme gebaut habe. Aber „es ließ sich bauen“ und „das Geschäft hat sich verändert“ sind zwei verschiedene Dinge. Am Ende des Kapitels trenne ich die beiden.

Was sich mit Zahlen bestätigen ließ. Dass 88,1% der Reservierungen am selben Tag gemacht werden. Dass die Zahl der bestandenen Testszenarien des Gesprächsfensters allein durch das Hinzufügen von 11 Tatsachen über das Lokal von 9 auf 24 (von 36) stieg. Dass die Bestehensquote bei der Beratung zu Preisen und Angeboten nach Korrekturen von 29,4% auf 42,7% stieg. Das sind festgehaltene Tatsachen.

Was zu wirken scheint, wo ich den ursächlichen Zusammenhang aber nicht belegen kann. Dass mehr Gäste mit dem Gruppenrabatt in Gruppen kommen. Dass die Angebote „Erstes Mal“ und „Willkommen zurück“ gewählt werden. Dass das Thema der Bestätigungs-E-Mail zum Teil des Gesprächs an der Theke geworden ist. Im Lokal spüre ich es, aber ich kann nicht sagen: „Ohne dieses System wären sie nicht gekommen.“

Was gebaut wurde, bei dem ich die Wirkung aber noch nicht kenne. Wie viele zusätzliche Vorabreservierungen der Frühbucherrabatt bringen wird. Wie viele Reservierungen tatsächlich über MCP eingehen werden. Mit dem Wochenbericht habe ich gerade erst begonnen zu messen, die Zahlen kommen später.

Betrachten Sie das Staunen darüber, „dass sich mit KI so viel bauen ließ“, und das Ergebnis „wie sich das Geschäft dadurch verändert hat“ getrennt voneinander. Ohne diese Unterscheidung wird das Bauen selbst zum Ziel. Beinahe wäre mir das selbst einmal passiert (wie ich in 1-7 geschrieben habe).

Die Technik hinter diesem Reservierungssystem folgt in Kapitel 2. Wenn Sie sich nicht für Technik interessieren, springen Sie zu Kapitel 3. Dort erzähle ich, wie die kleinen Werkzeuge, die rund um dieses Reservierungssystem entstanden sind, auch an andere Lokale weitergegeben werden.

## Kapitel 2: Technik - Hinter dem Reservierungssystem

Die wichtigsten Punkte dieses Kapitels

- Die Qualität der Gespräche der KI wurde weniger von der Klugheit der KI bestimmt als davon, „welche Tatsachen über das Lokal wir übergeben“ und „ob ein Programm die Antworten der KI eigenmächtig überschreibt“
- Das Reservierungssystem, das ich nach Gefühl gebaut hatte, hatte immer noch eine Lücke, durch die persönliche Daten von Gästen von außen lesbar waren, und null automatisierte Tests. Ich ließ eine KI es prüfen, um das herauszufinden, und ließ sie es beheben
- Aus dieser Erfahrung heraus änderte ich mein Vorgehen: vor dem Bau die Anforderungen im Detail festlegen und der KI die Spezifikation selbst zur Umsetzung übergeben

(Dieses Kapitel enthält viele Fachbegriffe. Wenn Sie sich nicht für Technik interessieren, können Sie zu Kapitel 3 springen, und die Geschichte hängt trotzdem zusammen.)

