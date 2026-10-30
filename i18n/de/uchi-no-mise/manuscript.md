# Gebaut für unsere Bar

Aufzeichnungen aus einer Bar mit 19 Plätzen: vom Reservierungssystem bis zu eigenen Werkzeugen, alles mit KI selbst gebaut

Raku Bonta

Die Agenda-Reihe: https://bontallc.com/agenda?via=b2-de-{{FMT}}

Instagram von Tamuro: https://www.instagram.com/tamuro.higashinakano/

Reservierungsseite von Tamuro: https://tamuroreservation.vercel.app/?src=b2-de-{{FMT}}

## Einleitung

Dieses Buch ist eine schlichte Aufzeichnung darüber, wie die Person, die eine Bar mit 19 Plätzen in Higashi-Nakano *(ein Wohnviertel im Westen Tokios, direkt westlich von Shinjuku)*, Tokio, führt, ihr Lokal mithilfe von KI betreibt.

Die Bar heißt „Tamuro“. Der Name bedeutet: ein Ort, an dem Menschen zusammenkommen. Sie wurde im November 2018 eröffnet, ein kleines Lokal mit 11 Thekenplätzen und 8 Plätzen im Tatami-Raum. Tagsüber führt im selben Raum jemand aus dem Team ein Restaurant für Curry mit Hacksteak (japanisch „Hambāgu“) namens „Quatre Épices“.

In meinem vorigen Buch, *Die KI-Stellvertretung*, habe ich über generative KI an sich geschrieben. Seitdem, in gut einem Jahr, hat sich KI von einem Werkzeug, das Fragen beantwortet, zu einem Werkzeug gewandelt, das Arbeit für Sie erledigt. Sie geben einen Auftrag, und die KI schreibt das Programm, testet es, behebt ihre eigenen Fehler und bringt die Arbeit zu Ende. Diese Art von KI nennt man agentische KI.

Mit agentischer KI habe ich das Reservierungssystem von Tamuro selbst gebaut. Ich habe ein Rabattsystem gebaut, das auf eine Preiserhöhung abgestimmt ist. Ich habe ein System gebaut, mit dem sich Stammkundschaft pflegen lässt. Ich habe eine KI gebaut, die Fragen von Gästen beantwortet. Und am Ende kam ich an den Punkt, dass Gäste Tamuro über ihre eigene KI etwas fragen und anschließend gleich reservieren können.

Außerdem habe ich die praktischen Werkzeuge, die ich für mein eigenes Lokal gemacht hatte, so aufbereitet, dass auch andere Lokale sie nutzen können, und biete sie für einige Hundert Yen im Monat an. Das ist die Agenda-Reihe.

Dieses Buch beschreibt, was ich auf diesem Weg gebaut habe, woran ich gescheitert bin und was ich neu lernen musste. Es sind nicht nur Erfolgsgeschichten. Ich baute immer weiter Dinge, die funktionierten, ganz nach Gefühl, und es häuften sich Widersprüche. Später stellte ich fest, dass persönliche Daten von Gästen von außen einsehbar waren. Die KI stellte Dinge als Tatsachen hin, die das Lokal nie genannt hatte. Auch diese Fehler habe ich so aufgenommen, wie sie passiert sind.

### So lesen Sie dieses Buch

Das Buch hat fünf Kapitel.

| Kapitel | Inhalt | Besonders geeignet für |
| --- | --- | --- |
| Kapitel 1 | Ein Lokal, das über KI gebucht wird (die geschäftliche Seite des Reservierungssystems) | Alle |
| Kapitel 2 | Hinter dem Reservierungssystem (technisch) | Menschen, die selbst Software bauen, und alle, die sich für Technik interessieren |
| Kapitel 3 | Die Werkzeuge unseres Lokals an andere Lokale weitergeben (die geschäftliche Seite der Agenda-Reihe) | Alle |
| Kapitel 4 | Ein System, um allein Produkte zu bauen (technisch) | Menschen, die selbst Software bauen, und alle, die sich für Technik interessieren |
| Kapitel 5 | Die Zukunft kleiner Lokale | Alle |

Die Kapitel 2 und 4 sind technisch und verwenden mehr Fachbegriffe. Beide beginnen mit einer Zusammenfassung der wichtigsten Punkte in drei Zeilen. Wenn Sie sich nicht für Technik interessieren, lesen Sie nur diese und gehen Sie zum nächsten Kapitel weiter. Lesen Sie die Kapitel 1, 3 und 5 der Reihe nach, bleibt der rote Faden der Geschichte trotzdem erhalten.

Wo immer es ging, habe ich jedem Fachbegriff direkt eine verständliche Umschreibung beigefügt. Auch wenn Sie noch nie ein Programm geschrieben haben, bekommen Sie hoffentlich ein Gefühl dafür, was es heißt, ein Lokal mit KI zu führen.

### Über mich

Ich habe etwa 16 Jahre in der IT gearbeitet, vor allem in der Systemplanung und als Bindeglied zwischen den Fachbereichen im Betrieb und den Entwicklungsdienstleistern, und bin dann in die Gastronomie gewechselt. Dies ist also nicht die Geschichte von jemandem, der nie eine Zeile Code geschrieben hatte und trotzdem alles allein mit KI gebaut hat. Das möchte ich ehrlich sagen.

Trotzdem kann ich heute allein, während ich selbst im Lokal stehe, etwas bauen und betreiben, wofür früher ein Team und Kapital nötig waren. Vor wenigen Jahren wäre das undenkbar gewesen. Ich möchte die Wirklichkeit dieses Wandels so konkret wie möglich beschreiben.

### Wie dieses Buch entstanden ist

Auch dieses Buch habe ich mit KI gemacht. Ausgehend von den Aufzeichnungen, die ich bei der täglichen Entwicklungsarbeit geführt habe, hat die KI die Entwürfe geschrieben, und ich habe gelesen, überarbeitet und entschieden. Auch die Bildschirmfotos für die Abbildungen hat die KI aufgenommen.

Ich habe alles durchgelesen, aber in von KI geschriebenen Texten können sich sachliche Fehler einschleichen. Wie ich im Haupttext sage: Die KI behauptet „Ist erledigt“, und das zu prüfen ist Aufgabe des Menschen. Es kann in diesem Buch Fehler geben, die mir entgangen sind.

Außerdem ändern sich die Spezifikationen von KI-Werkzeugen und -Diensten innerhalb weniger Monate. Die in diesem Buch beschriebenen Schritte, Preise und der Stand der Unterstützung bei den einzelnen Anbietern entsprechen dem Stand von Oktober 2026. Wenn Sie es selbst ausprobieren, prüfen Sie bitte die dann aktuellen offiziellen Angaben.

Wenn Sie einen Fehler entdecken, freue ich mich, wenn Sie mir auf note oder X Bescheid geben. Ich korrigiere Fehler nach und nach, sobald ich von ihnen erfahre.

### Drei Wege nach der Lektüre

Dieses Buch können Sie kostenlos als PDF, auf note und bei Google Play lesen. (Nur bei Kindle verlangen die Regeln des Stores einen Mindestpreis.) Im Gegenzug habe ich drei Anlaufstellen vorbereitet, die Sie nach der Lektüre nutzen können. Wenn auch nur einer davon für Sie nützlich ist, hat sich das Schreiben dieses Buchs gelohnt.

1. Probieren Sie es im eigenen Lokal aus. Die Agenda-Reihe können Sie mit dem kostenlosen Notizbuch beginnen. https://bontallc.com/agenda?via=b2-de-{{FMT}}
2. Bleiben Sie auf dem Laufenden. Auf note und X schreibe ich über die nächsten Werkzeuge, die ich baue, und über den Alltag im Lokal. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Falls Sie einmal in Tokio sind, besuchen Sie Tamuro. Eine Minute vom Ostausgang des Bahnhofs Higashi-Nakano. Sie können auch ohne Reservierung hereinkommen. Reservierungsseite https://tamuroreservation.vercel.app/?src=b2-de-{{FMT}}

## Kapitel 1: Ein Lokal, das über KI gebucht wird

### 1-1 Das Zeitalter, in dem man die KI fragt: „Ist heute Abend irgendwo noch Platz?“

An einem Freitagabend spricht jemand, der gerade Feierabend gemacht hat, mit dem eigenen Smartphone.

„Gibt es in Higashi-Nakano heute Abend einen Ort, wo ich allein etwas trinken kann? Nicht zu laut.“

Es antwortet keine Freundin und kein Freund. Es antwortet die KI, die diese Person jeden Tag benutzt. Die KI nennt infrage kommende Lokale, beschreibt die Atmosphäre jedes einzelnen und sagt, zu welchen Zeiten heute Abend noch Platz ist und was es kostet. Gefällt etwas, geht es gleich weiter zum Reservierungsbildschirm.

Das ist keine Zukunftsmusik.

Am 10. August 2026 hat OpenAI ChatGPT um eine Restaurantreservierung erweitert. Laut den offiziellen Release Notes ist sie mit den Reservierungsdiensten OpenTable, Resy und Yelp verbunden, und freie Reservierungszeiten erscheinen direkt in den Antworten von ChatGPT. Auch Rückfragen zur Eingrenzung der Auswahl sind möglich, und sobald man eine passende Zeit gewählt hat, kann man gleich buchen. Abgedeckt sind OpenTable weltweit, Resy in den USA sowie Yelp in den USA und in Kanada.

Mit anderen Worten: Der Eingang, über den Menschen einen Ort zum Essen suchen, verschiebt sich von Suchmaschinen und Restaurantportalen hin zur „eigenen KI“.

Es gibt allerdings eine Bedingung. Über ChatGPT buchen lassen sich nur Lokale, die bei den großen Reservierungsdiensten registriert sind. Kleine Lokale, die dort nicht gelistet sind, bleiben für die KI unsichtbar.

Was soll also eine Bar mit 19 Plätzen in Higashi-Nakano tun, die die großen Reservierungsdienste nicht nutzt?

Tamuro hat einen anderen Weg gewählt. Ohne Umweg über die großen Dienste hat es sein eigenes Reservierungssystem direkt mit KI verbunden.

Wenn Gäste ihre eigene ChatGPT- oder Claude-Instanz fragen „Ist bei Tamuro heute Abend noch Platz?“, fragt die KI das Reservierungssystem von Tamuro direkt ab, prüft freie Zeiten und Preise und antwortet. Sind die Bedingungen geklärt, führt sie die Gäste zur Reservierungsseite von Tamuro, auf der Personenzahl, Datum und Uhrzeit schon eingetragen sind. Den Bestätigungsknopf drücken die Gäste selbst.

Diesen „Verbindungspunkt zwischen KI und dem System eines Lokals“ nennt man MCP-Server. MCP steht für Model Context Protocol, eine gemeinsame Vereinbarung, mit der KI externe Werkzeuge und Daten nutzen kann. Die Einzelheiten erkläre ich in Kapitel 2.

Auch die großen Reservierungsdienste leiten die Gäste am Ende auf ihre eigenen Seiten weiter. Bei Reservierungen, die eine Kreditkarte erfordern, wird der Vorgang auf dem Bildschirm von OpenTable abgeschlossen, und Änderungen oder Stornierungen nach der Buchung laufen über den jeweiligen Dienst. Die KI ist der Eingang, der Bildschirm des Reservierungsdienstes der Ort der Bestätigung. Bei Tamuro ist die Struktur dieselbe. Der einzige Unterschied: Es steht kein Großkonzern dazwischen.

Und gebaut hat dieses System keine externe Entwicklungsfirma. Ich selbst habe es gebaut, die Person, die das Lokal führt. Ich habe der KI Aufträge gegeben, die KI die Programme schreiben und die KI die Tests ausführen lassen.

Natürlich war ich nicht von Anfang an so weit. Am Anfang stand ein ganz einfaches Reservierungsformular. Dann kamen eine Preiserhöhung, dann Ideen für Rabatte, dann ein System zur Pflege der Stammkundschaft, dann Fehlschläge und der Neuaufbau.

Zuerst möchte ich in fünf Zeilen beschreiben, was für ein Ort Tamuro ist. Eine Minute zu Fuß vom Ostausgang des Bahnhofs Higashi-Nakano. 19 Plätze, 11 an der Theke und 8 im Tatami-Raum. Etwa die Hälfte der Gäste kommt allein, und an der Theke kommt man leicht mit der Person nebenan ins Gespräch. Das Essen besteht aus einer Kombination aus vier Vorspeisen und einem Hauptgang, und das beliebteste Gericht ist ein süßliches Tonteki (Schweinesteak) mit viel Knoblauch. Die Weine kommen hauptsächlich aus Spanien und Italien, dazu gibt es etwa 20 Sorten japanischen Craft-Gin. Sie können auch ohne Reservierung hereinkommen.

Ein Ziel möchte ich ebenfalls nennen. Ich wollte nicht bloß Reservierungen annehmen. Ich wollte, dass auch ein kleines Lokal den gesamten Ablauf aus Bekanntwerden, Besucht-Werden und Wiederkommen aus eigener Kraft bauen kann. Die Rabatte, die E-Mails und das Chatfenster in diesem Kapitel sind allesamt Teile, die diesem einen Zweck dienen.

In diesem Kapitel spule ich die Zeit zurück und zeichne nach, wie das Reservierungssystem von Tamuro gewachsen ist.

【Abbildung 1-1】Der Bildschirm nach der Verbindung von ChatGPT mit dem MCP-Server von Tamuro (10. Oktober 2026). Er liest die Informationen des Lokals aus und antwortet, dass er freie Zeiten, Menüs, Preise und die Weiterleitung zur Reservierungsseite abdecken kann *(Die Bildschirmanzeige ist auf Japanisch.)*

### 1-2 Der Anfang: Nur Reservierungen annehmen

[Die Reservierungsseite von Tamuro](https://tamuroreservation.vercel.app/?src=b2-de-{{FMT}}) war anfangs ganz einfach. Datum, Uhrzeit und Personenzahl wählen, Namen und Kontaktdaten eingeben, absenden. Beim Lokal geht eine Benachrichtigung ein. Mehr nicht.

Das erste Fundament habe ich mit dem KI-Entwicklungswerkzeug von Google (Antigravity) gebaut. Ich habe der KI jede Funktion genannt, die mir einfiel, und wenn etwas funktionierte, ging ich zur nächsten über. Das nennt man Vibe Coding (der KI alles sagen, was einem gerade einfällt, und sie nach Gefühl bauen lassen).

Für mich war es damals eine Überraschung nach der anderen. Man beschreibt das Layout eines Bildschirms in Worten, und in wenigen Minuten nimmt es Gestalt an. Man sagt, man möchte einen Kalender, und ein Kalender erscheint. In den Lücken zwischen der Arbeit im Lokal entstand eine Reservierungsseite.

Bei Tamuro kann man auch ohne Reservierung hereinkommen. Tatsächlich werden die meisten Reservierungen am selben Tag gemacht, und viele Gäste kommen einfach vorbei. Trotzdem habe ich ein Reservierungssystem gebaut, weil ich einen Weg wollte, mit Gästen schon vor ihrem Besuch in Verbindung zu treten. Wer reserviert, hinterlässt Namen und Kontaktdaten. Und wenn die Kontaktdaten da sind, kann ich zum nächsten Besuch einladen.

Ein Reservierungssystem ist nicht bloß eine Annahmestelle für Reservierungen. Es wird zum Eingang in eine Beziehung zu den Gästen. Dieser Gedanke führte später zum Rabattsystem und zum System für die Pflege der Stammkundschaft.

Für ein Fundament, das nach Gefühl entstanden war, habe ich aber später einen hohen Preis gezahlt. Davon schreibe ich in Kapitel 2.

### 1-3 Preiserhöhung und Rabatte zugleich bauen

Für ein Restaurant oder eine Bar ist eine Preiserhöhung eine Entscheidung, an der man nicht vorbeikommt. Zutaten, Nebenkosten und Personalkosten werden immer teurer. Auch Tamuro hat die Preise erhöht. Ich habe jedes Menü um etwa ¥400–¥500 (ca. $2,7–$3,3) angehoben.

Die Erhöhung war deutlich, und es war klar: Würde ich sie einfach so verkünden, würden Stammgäste fernbleiben. Deshalb habe ich beschlossen, gleichzeitig mit der Preiserhöhung ein Rabattsystem in das Reservierungssystem einzubauen. Es macht nicht einfach alles billiger. Es belohnt mit Rabatten die Gäste, die sich so verhalten, dass es dem Lokal guttut.

Der erste ist der Gruppenrabatt. Je mehr Personen in der Gruppe, desto niedriger der Preis pro Person. Etwa die Hälfte der Gäste von Tamuro kommt allein, aber kommen sie in Gruppen, wächst der Umsatz des Lokals stark. Auch nach Abzug des Rabatts bleibt für das Lokal ein Plus. Für die Gäste ist es ein Grund, Freundinnen und Freunde mitzubringen. Tatsächlich ist die Zahl der Gäste gewachsen, die über den Personenzahl-Rabatt der Reservierungsseite in Gruppen kommen.

Der zweite ist der Frühbucherrabatt. Wer mindestens eine Woche im Voraus reserviert, erhält 2% Nachlass, bei mindestens zwei Wochen im Voraus 4%. Die meisten Reservierungen bei Tamuro kommen am selben Tag, deshalb kann ich nicht absehen, was kommt. Der Frühbucherrabatt ist ein Mechanismus, um künftigen Umsatz festzuhalten. An Regentagen und an kalten Tagen kann sich das Lokal in Ruhe vorbereiten, wenn schon Reservierungen vorliegen.

Drittens habe ich auch einen Mechanismus für Gruppenkäufe gebaut. Fanden sich zu einem bestimmten Datum und einer bestimmten Uhrzeit eine bestimmte Zahl von Menschen zusammen, wurde ein Menü zu einem Rabattpreis angeboten. Es sollte ein Mechanismus ganz im Geist von Tamuro sein, bei dem sich Fremde zur gleichen Zeit versammeln.

Aber der Plan für Gruppenkäufe wurde überhaupt nicht genutzt. Null Ergebnisse. Im August 2026 habe ich diesen Plan eingestellt und beschlossen, ihn nicht wieder zu verwenden.

Etwas wegzuwerfen, das man gemacht hat, fühlt sich verschwenderisch an. Aber wer mit KI baut, hat nur geringe Kosten und wenig Zeitaufwand beim Bauen. Klein bauen, ausprobieren, und wenn es nicht funktioniert, wegwerfen. Ich glaube, diese Geschwindigkeit ist der größte Vorteil, wenn man ein Lokal mit KI führt.

Bei der Preisgestaltung gibt es noch einen Kniff. Unter den Angeboten platziere ich bewusst ein teures Premium-Angebot. Es ist in Ordnung, wenn sich kaum jemand für das Premium-Angebot entscheidet. Mit einem teuren Angebot daneben wirkt das Standardangebot erschwinglich. Es übernimmt die Rolle eines sogenannten Ankers (eines Bezugspunkts zum Vergleichen).

【Abbildung 1-7】Je mehr Personen, desto niedriger der Preis pro Person (Vergleich von 1, 4 und 6 Gästen)

### 1-4 Ein System zur Pflege der Stammkundschaft

Sobald im Reservierungssystem Namen und Kontaktdaten vorliegen, möchte man als Nächstes die Beziehung zu den Gästen pflegen. Ein System, das Kundendaten verwaltet und Beziehungen vertieft, heißt CRM (Customer-Relationship-Management). Nach und nach habe ich dem Reservierungssystem von Tamuro CRM-Funktionen hinzugefügt.

Wer sich als Mitglied registriert, sieht den Verlauf der eigenen Reservierungen in einem persönlichen Bereich namens „Meine Seite“. Wer einen Geburtstag hinterlegt, bekommt ein Geburtstagsgeschenk. Mitglieder, die länger nicht da waren, erhalten eine Nachricht, die sie zum Wiederkommen einlädt. Es gibt auch eine Stempelkarte. Drei Besuche bringen ein Getränk, fünf ein Steak und weitere Extras, und nach fünf beginnt die Zählung von vorn. Es gibt außerdem eine Funktion, Freundinnen und Freunde zu empfehlen.

Besonders sorgfältig habe ich den Mechanismus gestaltet, der zu einem zweiten Besuch einlädt. In Restaurants und Bars heißt es, dass sich daran, ob Erstgäste ein zweites Mal kommen, entscheidet, ob sie zur Stammkundschaft werden. Bei Tamuro schicke ich zwei Erinnerungs-E-Mails, sieben und 21 Tage nach dem ersten Besuch. Die erste enthält keinen Gutschein, nur die zweite. Statt von Anfang an mit einem Rabatt zu locken, erinnere ich sie zuerst nur an uns. Kommen sie dann immer noch nicht, gebe ich einen kleinen Anstoß.

Ich habe auch darauf geachtet, dass sich die E-Mails nicht häufen. Gäste erhalten höchstens eine Nachricht pro Tag. Überschneiden sie sich, gilt diese Rangfolge: Geburtstag, Einladung zum zweiten Besuch, Einladung an länger abwesende Mitglieder, wiederzukommen, sonstige Mitteilungen. Mitglieder, die bereits die nächste Reservierung haben, erhalten keine E-Mails mit einer Einladung zum Besuch.

Die Einwilligung in den E-Mail-Empfang ist standardmäßig ausgeschaltet. Ließe ich sie eingeschaltet, würde die Zahl der Empfangenden steigen, aber ein Aufbau, bei dem Menschen einwilligen, ohne es zu wissen, könnte nach dem Verbraucherschutzrecht ein Problem sein. Vertrauen gewinnen statt Zahlen. So habe ich entschieden.

In den E-Mails gibt es noch eine kleine Besonderheit. In die Reservierungsbestätigung kommt ein „Thema des Tages“. Etwas zur Jahreszeit, zum Wein oder zum Essen. Die KI schreibt jeden Tag automatisch ein kurzes Thema.

Ziel ist, den Gästen schon vor dem Besuch einen Gesprächsanlass mitzugeben. Tamuro ist ein Lokal, in dem unter den Gästen viel geredet wird. Ein Thema, das man in der E-Mail gelesen hat, wird zum ersten Satz an die Person neben einem an der Theke. Deshalb habe ich die Bestätigungs-E-Mail nicht bei „Ihre Reservierung ist eingegangen“ enden lassen, sondern sie ein Stück der Atmosphäre des Lokals im Voraus überbringen lassen.

Die KI, die die Themen schreibt, habe ich einmal ausgetauscht. Ich habe zu einer gewechselt, die natürlichere Themen liefert, die näher am Ton des Lokals sind. Das ist allerdings kein Mechanismus, um mehr Gäste zu gewinnen. Es ist ein Mechanismus, um das Erlebnis derer, die kommen, ein wenig besser zu machen. Auf diese Unterscheidung komme ich in der zweiten Hälfte dieses Kapitels noch einmal zurück.

Unter diesen Mechanismen sind es die Angebote „Erstes Mal“ und „Willkommen zurück“, bei denen sich nach und nach Ergebnisse zeigten. Das sind leicht zugängliche, preislich moderate Angebote, die nur Erstgäste und Gäste wählen können, die seit über einem Jahr nicht mehr da waren. Sie geben sowohl neuen Gästen als auch solchen, die abzuwandern drohen, einen Grund zu kommen.

Andererseits gab es auch ein Problem. Viele Gäste buchen als Gast, ohne sich als Mitglied zu registrieren. Würde ich bei jeder Reservierung eine Mitgliedsregistrierung verlangen, würden manche womöglich ganz aufs Buchen verzichten. Deshalb zeige ich nach abgeschlossener Reservierung die Frage „Möchten Sie diese Reservierung mit einem Mitgliedskonto verknüpfen?“ und habe einen Weg gebaut, nachträglich Mitglied zu werden. So entsteht keine Hürde beim Buchen, und die Beziehung wird später geknüpft.

【Abbildung 1-8】Angebote, die nur Erstgäste und Gäste wählen können, die seit über einem Jahr nicht da waren *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 1-9】Die Stempelkarte auf „Meine Seite“ (synthetische Daten) *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 1-5】Reservierungsbestätigung per E-Mail. Ein „Thema des Tages“ ist enthalten (synthetische Daten) *(Die Bildschirmanzeige ist auf Japanisch.)*

### 1-5 In Zahlen: Etwa 88% der Reservierungen gelten für denselben Tag

Als ich immer weiter Mechanismen hinzufügte, fiel mir etwas auf. Ich konnte nicht erkennen, welche davon wirkten.

Also habe ich die Reservierungsdaten ausgezählt. Von den 244 Reservierungen der letzten 90 Tage waren 215 Reservierungen für denselben Tag. Das sind 88,1%. Der Durchschnitt liegt bei 2,71 Reservierungen pro Tag.

Tamuro war kein Ort, für den man reserviert, sondern ein Ort, zu dem man spontan kommt. Erst als ich es in Zahlen fasste, wurde das deutlich.

Aus diesen Zahlen wurden zwei Dinge sichtbar.

Das eine ist, wie das Reservierungsformular aufgebaut sein sollte. Gelten die meisten Reservierungen für denselben Tag, ist es praktischer, wenn beim Öffnen des Reservierungsbildschirms schon der nächste freie Zeitraum von heute ausgewählt ist. Andererseits schicken manche, die für ein späteres Datum buchen wollen, die Reservierung versehentlich mit dem heutigen Datum ab. Deshalb habe ich das heutige Datum im Kalender hervorgehoben, und auf dem Bestätigungsbildschirm zeige ich Datum und Uhrzeit groß mit „Heute“. Die Bequemlichkeit, den gleichen Tag zu wählen, blieb erhalten, und Irrtümer fallen leichter auf.

Das andere ist die Bedeutung des Frühbucherrabatts. Viele Reservierungen am selben Tag bedeuten, dass sich der künftige Umsatz kaum vorhersehen lässt. Schon schlechtes Wetter allein genügt, damit weniger Laufkundschaft kommt. Um Vorabreservierungen auch nur ein wenig zu steigern, müssen mehr Menschen den Frühbucherrabatt nutzen. Dieses Bewusstsein führte später zu der Geschichte, eine KI zu bauen, die stellvertretend für die Person, die das Lokal führt, postet.

Um Zahlen anzusehen, braucht man ein System zum Zählen. Die Reservierungsseite hatte überhaupt keine Zugriffsauswertung. Ich konnte nicht erkennen, wie viele Menschen auf die Reservierungsseite kamen, wie viele mittendrin abbrachen und wie viele die Reservierung abschlossen. Also habe ich ein System ergänzt, das drei Stufen zählt: auf der Seite angekommen, Angaben festgelegt, Reservierung abgeschlossen. Es erfasst nicht, wer gekommen ist, nur die Stufe und die Uhrzeit.

Später habe ich außerdem ein System gebaut, das einen Wochenbericht mit den Reservierungszahlen per E-Mail verschickt. Wie es dazu kam, beschreibe ich in 1-7.

【Abbildung 1-3a】Heute ist im Kalender hervorgehoben *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 1-3b】Auf dem Bestätigungsbildschirm erscheinen Datum und Uhrzeit groß als „Heute“ *(Die Bildschirmanzeige ist auf Japanisch.)*

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

### 2-1 So funktioniert der MCP-Server

MCP (Model Context Protocol) ist eine gemeinsame Vereinbarung, mit der KI externe Werkzeuge und Daten nutzen kann. Von Anthropic vorgeschlagen, wird es inzwischen von vielen KI-Systemen unterstützt, darunter ChatGPT und Claude.

Als Vergleich: MCP ist ein Standard für Steckdosen, für KI. Weil die Form der Steckdose festgelegt ist, funktionieren Geräte jedes Herstellers, sobald man sie einsteckt. Genauso kann jede KI ein Fenster nutzen, wenn man es passend zur Form von MCP baut.

Ein MCP-Server sagt der KI, „was sich durch dieses Fenster tun lässt“. Der MCP-Server von Tamuro zum Beispiel stellt Werkzeuge wie die folgenden bereit.

- Die Informationen des Lokals auslesen (Öffnungszeiten, Zahl der Plätze, Hausregeln, Atmosphäre)
- Angebote und Preise auslesen (das Ergebnis der Rabattberechnung nach Personenzahl und Datum)
- Freie Zeiten auslesen (die buchbaren Zeiten an einem bestimmten Tag)
- Die URL einer Reservierungsseite mit bereits eingetragenen Angaben erzeugen

Fragen Gäste ihre eigene KI: „Ist bei Tamuro heute Abend noch Platz?“, verbindet sich die KI mit dem MCP-Server von Tamuro, wählt aus den bereitgestellten Werkzeugen „freie Zeiten auslesen“ und ruft es auf. Der Server von Tamuro liefert das Ergebnis zurück, und die KI fasst es für die Gäste in Worte.

Wichtig ist, dass die KI Reservierungen nicht eigenmächtig bestätigt. In der ersten Version habe ich die Reservierungsbestätigung bewusst nicht in die Werkzeuge aufgenommen. Die KI kann nur auslesen und Menschen zu einer Reservierungsseite mit bereits eingetragenen Angaben führen. Den Bestätigungsknopf drücken die Gäste selbst auf der Seite von Tamuro. Die Gefahr, dass die KI massenhaft fehlerhafte oder Scherzreservierungen anlegt, ist von Anfang an durch den Entwurf ausgeschlossen.

Die Preisberechnung nutzt denselben Berechnungsmechanismus wie die Reservierungsseite. Die Preise im Reservierungsformular, im Gesprächsfenster und über MCP stammen alle aus ein und demselben Programm. Das ist die andere Bedeutung der Aufgabe, über die ich später schreibe, „die Rabattberechnung an einer Stelle zu bündeln“.

【Abbildung 2-1】Von der KI der Gäste zur Reservierungsseite von Tamuro. Den Bestätigungsknopf drücken die Gäste

### 2-2 So funktioniert das Gesprächsfenster „T-AI-MURO“

#### Preise vom Programm, Worte von der KI

T-AI-MURO teilt die Rollen auf. Das Programm erzeugt Preise und freie Zeiten mit festen Berechnungen, und die KI fasst sie für die Gäste in Worte.

KI ist gut darin, Text zu erzeugen, aber es gibt keine Garantie, dass sie jedes Mal richtig rechnet. Wie Rabatte zusammenwirken, die Stufen nach Personenzahl, die Zahl der Tage beim Frühbucherrabatt, ob er sich mit der Happy Hour kombinieren lässt. Überlässt man der KI alle diese Regeln, macht sie ganz sicher irgendwo einen Fehler. Und ein Fehler beim Preis schadet dem Vertrauen der Gäste am meisten.

Deshalb ist das, was nicht falsch sein darf, Sache des Programms, und das, was weich vermittelt werden soll, Sache der KI. Diese Aufteilung ist der erste Grundsatz beim Bau des Gesprächsfensters.

#### Für ein kleines Lokal braucht man kein RAG

Damit die KI Auskunft über das Lokal geben kann, muss man ihr das Wissen über das Lokal übergeben. Eine häufig genutzte Methode ist RAG (Retrieval-Augmented Generation). Man zerlegt das Wissen in kleine Stücke und legt sie ab, und bei jeder Frage sucht man nur die Teile heraus, die relevant erscheinen, und übergibt sie der KI. Ist das Wissen riesig, ist diese Methode unverzichtbar.

Aber das Wissen von Tamuro ist nicht so groß. Die Geschichte des Lokals, das Essen, die Regeln, die Atmosphäre, die Überlegungen der Lokalleitung. Alles zusammen passt problemlos in das, was die KI auf einmal lesen kann.

Deshalb habe ich bei Tamuro gewählt, die KI jedes Mal den gesamten Text des Wissens über das Lokal lesen zu lassen. Es braucht keinen Suchmechanismus, wie ihn RAG erfordert, und bei der Suche geht nichts verloren. Anfangs hatte ich geplant, einen RAG-Mechanismus wiederzuverwenden, wechselte aber mittendrin zum Ansatz mit dem vollständigen Text.

Den ganzen Text jedes Mal lesen zu lassen, kostet mehr KI-Gebühren. Deshalb nutze ich einen Mechanismus, der denselben Text wiederverwendet, um die Eingabekosten zu senken (Prompt Caching: Statt die KI jedes Mal dieselbe Einleitung neu lesen zu lassen, merkt sie sich, was sie schon gelesen hat). Es genügt, RAG erst dann einzuführen, wenn das Wissen groß wird.

#### Ein Programm, das Antworten eigenmächtig überschreibt

In Kapitel 1 habe ich geschrieben, dass im ersten Test nur 9 von 36 bestanden. Ein Teil der Ursache lag in der Bauweise des Programms.

Bei der Untersuchung fand ich einen Mechanismus, der noch übrig geblieben war: Das Programm beurteilte die Antwort der KI anhand von Schlüsselwörtern und ersetzte sie durch einen festen Satz. Tauchten Wörter wie „Reservierung“ oder „heute“ auf, warf es die Antwort der KI weg und setzte eine Liste freier Zeiten ein. Selbst wenn die KI richtig antwortete, kam das nie bei den Gästen an.

Außerdem stellte ich fest, dass der Hauptteil des Wissens über das Lokal (33 Abschnitte) in den Anweisungen an die KI gar nicht enthalten war. Die KI hatte geantwortet, ohne etwas über das Lokal zu wissen.

Die Qualität der Gespräche der KI wurde weniger von der Klugheit der KI selbst bestimmt als davon, welche Tatsachen über das Lokal übergeben wurden und ob ein Programm die Antworten der KI eigenmächtig überschrieb.

#### Die erwarteten Fragen und Antworten durch Zählen auffüllen

Die Testszenarien erhöhte ich von anfangs 36 auf 110 und dann auf 355. Fügen Menschen Szenarien aber nur nach spontanen Einfällen hinzu, lässt sich nicht erkennen, ob etwas fehlt. Auf die Frage „Ist das vollständig?“ lautete die ehrliche Antwort: „Nein, ist es nicht.“

Statt die Abdeckung also nach Vorstellungskraft zu erweitern, machte ich daraus eine Zählaufgabe für die Maschine: die noch nicht durchlaufenen Stellen zu zählen und aufzufüllen. Und zwar bei vier Dingen: den 33 Abschnitten des Wissens über das Lokal, den Übergängen zwischen Auswahlmöglichkeiten, den Stufen der Rabatte und den Kombinationen aus Zeitfenstern und Wochentagen. Ich zähle, wie oft jedes davon im Test durchlaufen wurde, und füge automatisch Szenarien hinzu, wo der Zähler null ist.

Ich nutzte auch ein Verfahren, bei dem sechs Achsen (Personenzahl, Anlass, Art der Getränkebestellung, Datum und Uhrzeit, Formulierung, Speisen) gekreuzt werden und Szenarien so entstehen, dass jede Kombination aus zwei Achsen mindestens einmal durchlaufen wird.

Auch bei der Zeitsteuerung zeigte sich eine Lücke. „Heute“ und „ab jetzt“ werden von der tatsächlichen Uhrzeit des Testlaufs bestimmt, daher unterscheiden sich Ergebnisse bei einem Lauf am Mittag und bei einem Lauf in der Nacht. Also habe ich die Uhr während des Tests festgesetzt und ihn zu fünf Zeitpunkten laufen lassen: vor der Öffnung, während der Öffnungszeit, kurz vor Schluss, an einem regulären Ruhetag und an einem Feiertag.

Die Antworten der KI schwanken selbst bei derselben Frage leicht. Für Szenarien, die direkt mit dem Umsatz zusammenhängen, setzte ich die Bedingung, dass sie bei drei Durchläufen alle drei Male bestehen müssen.

#### Kommt eine schlechte Zahl heraus, zuerst den Test verdächtigen

Im Test mit 355 Szenarien zu 5 Zeitpunkten bestanden von 1.775 Gesprächen 28,5%.

Statt gleich mit dem Korrigieren zu beginnen, trennte ich zuerst: „Ist diese Zahl wirklich eine Schwäche von T-AI-MURO, oder ist der Test falsch?“ Korrigiert man, während der Test falsch ist, „korrigiert“ man am Ende sogar die richtigen Antworten.

| Fehlerursache | Anzahl |
| --- | --- |
| Ein fester Satz kapert die Frage | 276 |
| Beantwortet die Frage nicht, geht zum Reservierungsablauf oder zu Empfehlungen über | 266 |
| Ausfall der Testumgebung (T-AI-MURO konnte wegen der Kostenobergrenze keine Antwort erzeugen) | 211 |
| Fehler bei Datum, Wochentag, Feiertagen, Ruhetagen | 142 |
| Erfindet oder behauptet Tatsachen, die auf das Lokal nicht zutreffen, verspricht Nachrichten weiterzugeben | 119 |

Die obersten zwei hatten dieselbe Wurzel: „auf Wörter zu reagieren und ein festes Schema abzuspulen, bevor die Frage der Gäste beantwortet ist“. Die 211 auf Platz drei waren keine Fehler von T-AI-MURO. Mitten im Test wurde die Kostenobergrenze erreicht, und T-AI-MURO konnte schlicht keine Antworten erzeugen. Rechnet man diese heraus, liegt die Bestehensquote bei 32,4%.

Auch die beurteilende KI kann Fehler machen. Als ich 20 Fälle herauszog und prüfte, waren 2 Fehler auf Seiten des Tests. In einem davon wusste die beurteilende KI nicht, dass „diese Reservierungsseite eine Mitgliedsregistrierung hat“. Die beurteilende KI weiß auch nichts, was über das ihr übergebene Material hinausgeht. Die Genauigkeit des Tests wird von der Vollständigkeit der Regeln des Lokals bestimmt, die man der beurteilenden KI übergibt.

Im erneuten Test nach den Korrekturen stieg die Bestehensquote bei der Beratung zu Preisen und Angeboten von 29,4% auf 42,7%. Den abschließenden Test, der alle Fälle noch einmal durchläuft, habe ich noch nicht durchgeführt. Um die Kosten niedrig zu halten, habe ich festgelegt, den Test mit allen Fällen nur einmal vor der Inbetriebnahme einer größeren Änderung laufen zu lassen. Auch jetzt, während ich dieses Buch schreibe, arbeite ich weiter daran, die Bestehensquote zu steigern.

#### Der Test legte den Betrieb lahm

KI-Tests kosten Geld. Der erste Test mit 36 Szenarien kostete etwa ¥426 (ca. $2,8). Das meiste ging für den „Denkaufwand“ der als Gast auftretenden KI drauf, und als ich ihn abschaltete, kosteten 3 Szenarien etwa ¥6 (ca. $0,04).

Doch dann war eines Tages mitten in einem Test das KI-Nutzungsguthaben aufgebraucht, und alles stand still. An einem einzigen Tag hatte ich etwa 35 Millionen Token verbraucht (die Einheit für Text, den eine KI liest und schreibt). Die Ursache war, dass ich den Test mit 221 Szenarien wieder und wieder laufen ließ und Szenarien, die direkt mit dem Umsatz zusammenhängen, jeweils viermal ausführte.

Beängstigend war, dass Test und Betrieb dieselbe Geldbörse nutzten. Ist das Guthaben aufgebraucht, steht sogar das Gesprächsfenster im Betrieb still. An einem anderen Tag erreichte ich eine monatliche Obergrenze, die ich selbst gesetzt hatte, und das Gesprächsfenster im Betrieb und die KI, die Gesprächsthemen für die Gäste im Lokal erstellt, blieben gleichzeitig stehen.

Die eigentliche Gefahr eines Testbudgets war nicht die Rechnung, sondern dass der Betrieb dieselbe Geldbörse nutzte.

Von da an änderten sich die Regeln. Zuerst die Prüfungen durchführen, die nichts kosten (Programmtests und automatische Bildschirmprüfungen). KI-Aufrufe in Tests auf das beschränken, was mit der Korrektur zusammenhängt. Den Test mit allen Fällen nur einmal vor der Inbetriebnahme laufen lassen. Die geschätzten Kosten und eine Obergrenze in die Anweisungen schreiben und anhalten, wenn sie voraussichtlich erreicht wird. Um Mittel für den Betrieb zu erhalten, die Tests stoppen, wenn die Nutzung der gesamten Organisation der Obergrenze nahekommt.

Auch dafür, wie Kosten anschwellen, gab es eine Lehre. Einmal lagen die Kosten der beurteilenden KI beim 2,6-Fachen der Schätzung. Die Ursache war, dass die lange Einleitung, die der beurteilenden KI jedes Mal übergeben wurde (das Wissen und die Regeln des Lokals), nicht wiederverwendet wurde und so jedes Mal eine Gebühr für das erneute Schreiben anfiel. Als ich es so korrigierte, dass die Einleitung einmal geschrieben und dann wiederverwendet wird, sanken die Kosten pro Gespräch auf etwa ein Drittel. KI-Kosten schwellen nicht mit der Zahl der Aufrufe an, sondern mit der Zahl, wie oft dieselbe Einleitung neu geschrieben wird.

Denselben vollständigen Test mit 221 Szenarien brachte ich durch wiederholte Verbesserungen von etwa ¥1.040 (ca. $6,9) auf etwa ¥400 (ca. $2,7). Ich ersetzte die als Gast auftretende KI durch ein festes Skript und teilte die Informationen, die an die KI gehen, in einen „Kern, der jedes Mal gesendet wird“ und „Abschnitte, die nur bei Bedarf gelesen werden“.

Wegen der Budgetgrenzen verschob sich der Entwurf dahin, die Teile zu vermehren, die sich ohne Kosten prüfen lassen, also die Teile, die das Programm entscheidet. Dadurch stieg auch die Genauigkeit. Geld verändert den Entwurf.

【Abbildung 2-2】Ergebnisse der KI-Tests. Die Bestehensquote und eine Aufschlüsselung der Fehlerursachen

### 2-3 Das Gebaute von einer KI prüfen lassen

#### Namen von Gästen waren von außen lesbar

Im August 2026, als ich überprüfte, wie das Reservierungssystem arbeitet, machte ich eine Entdeckung, die mir einen Schauer über den Rücken jagte.

Die Reservierungsdaten der Gäste konnte jeder von außen lesen. Namen, Telefonnummern, E-Mail-Adressen, das Feld mit den Wünschen. Alles, was in eine Reservierung eingegeben worden war, ließ sich vollständig abrufen, ohne Authentifizierung.

Eines muss ich ehrlich sagen. Es stimmt, dass die Daten von außen lesbar waren. Damals hatte die Reservierungsseite sehr wenig Besuch, und ich halte es für unwahrscheinlich, dass sie tatsächlich jemand gelesen hat. Aber ich habe keine Aufzeichnung, die belegen könnte, dass sie nicht gelesen wurden. „Sie waren abrufbar“ und „sie wurden tatsächlich abgerufen“ sind zwei verschiedene Dinge, doch schon Ersteres allein war für ein Lokal ein schwerer Fehler.

Als ich die Ursache zurückverfolgte, lief es auf den Aufbau des Reservierungsformulars hinaus. Um freie Plätze zu berechnen, lud das Formular die Reservierungsdaten für 35 Tage direkt im Browser. Wenn der Browser sie lesen kann, kann jeder, der weiß, wie solche Seiten aufgebaut sind, dieselben Daten lesen. Es war das Ergebnis eines nach Gefühl gebauten ersten Fundaments, das das Ziel „freie Plätze anzeigen“ auf dem kürzesten Weg erreichte.

Außerdem stellte ich fest, dass die E-Mail-Adresse zur Benachrichtigung der Administration des Lokals öffentlich war und dass jeder in den Speicherort der Übersetzungen schreiben konnte, sodass die Daten hätten manipuliert oder die Kosten in die Höhe getrieben werden können.

Die Reihenfolge der Korrektur war wichtig. Hätte ich das Lesen auf einen Schlag verboten, hätte das Reservierungsformular keine freien Plätze mehr anzeigen können und wäre ausgefallen. Also verlegte ich zuerst die Berechnung der freien Plätze auf einen Endpunkt auf der Serverseite. Als Nächstes änderte ich den Bildschirm nach abgeschlossener Reservierung so, dass auch er nur die benötigten Informationen vom Server holt. Zuletzt schloss ich das Lesen von außen. In dieser Reihenfolge nahm ich die Korrektur in vier Stufen vor und übernahm sie in den Betrieb.

Nach der Korrektur prüfte ich automatisiert, ob es wirklich geschlossen war. Ich bereitete einen Test vor, der versucht, Reservierungsdaten ohne Authentifizierung zu lesen, und lasse ihn nach jeder Änderung automatisch laufen, um zu bestätigen, dass er immer abgewiesen wird. Ich beließ es nicht bei einer einmaligen Korrektur. Ich habe es so eingerichtet, dass eine Prüfung dauerhaft darüber wacht, dass es sich nie wieder öffnet.

#### Echte Kundendaten lagen im Entwicklungsverlauf

Dann ließ ich die KI das gesamte Repository (den Speicherort des Programms) prüfen, und es kam ein noch ernsteres Problem zutage.

Während der Entwicklung war eine Datei mit echten Kundendaten (E-Mail-Adressen und Telefonnummern aus 55 Reservierungen) ins Repository gelangt und stand noch im Änderungsverlauf des Programms. Das Repository war privat, aber weil sie in der Aufzeichnung verblieben war, konnte ich es nicht dabei belassen.

Ich entfernte die Datei aus dem gesamten Änderungsverlauf, schrieb den Verlauf neu und legte ihn erneut ab. Dennoch könnten die alten Aufzeichnungen von vor dem Neuschreiben auf Seiten von GitHub, wo das Repository liegt, noch vorhanden sein. Also bat ich den Support von GitHub, sie zu löschen, und vergewisserte mich, dass es erledigt wurde.

Die Prüfung brachte auch weitere Probleme zutage: Der Endpunkt für Übersetzungen ließ sich ohne Authentifizierung nutzen, die Anmeldung der Administration konnte per Brute Force angegriffen werden, und es gab ein Zeitfenster, in dem bei wieder aktivierter Bezahlung eine Reservierung bestätigt werden konnte, solange sie noch unbezahlt war. Ich behob sie nacheinander, beginnend mit dem schwersten.

#### Es gab null automatisierte Tests

Die Prüfung offenbarte noch eine Tatsache. Das Reservierungssystem hatte nicht einen einzigen automatisierten Test.

Automatisierte Tests sind ein Mechanismus, bei dem eine Maschine selbstständig prüft, ob das Programm korrekt arbeitet. Ohne Tests hat man beim Korrigieren keine Möglichkeit zu prüfen, ob dabei etwas anderes kaputtgegangen ist. Bei jeder neuen Funktion geht irgendwo still etwas kaputt. Genau in diesem Zustand befand sich alles in der Zeit, in der ich nach Gefühl baute.

Also baute ich das Fundament für die Tests von null auf neu. Ich führte ein System (CI) ein, das nach jeder Änderung automatisch vier Prüfungen ausführt: Typprüfung, Stilprüfung, Tests und den Build. Wichtige Entscheidungen wie Preisberechnung, Reservierungsbeurteilung, Verknüpfung von Mitgliedern und Ausgabe von Gutscheinen trennte ich vom Programmcode der Oberfläche, sodass sie sich für sich allein überprüfen lassen. Auch die Regeln zum Lesen und Schreiben der Datenbank werden in einer Testumgebung geprüft, die eine echte Datenbank nachahmt. Die Unit-Tests begannen bei 275 und wuchsen später auf über 500.

Eine Bedingung stelle ich an Tests immer: „Kaputt machen und bestätigen, dass er durchfällt.“ Auch wenn ein Test grün wird (besteht), weiß man nicht, ob dieser Test ein Problem wirklich erkennen kann. Erst wenn ich das Programm absichtlich kaputt mache und bestätige, dass der Test rot wird (durchfällt), vertraue ich dem Test. Denn von KI geschriebene Tests prüfen manchmal überhaupt nichts.

#### Acht Löcher im Reservierungsformular

Nachdem das Fundament für die Tests stand, ließ ich die KI den gesamten Reservierungsablauf noch einmal untersuchen. Sie fand acht Probleme, die echten Schaden anrichten konnten.

Das schwerste war, dass wiederholtes Drücken des Absenden-Knopfs eine doppelte Reservierung erzeugte. Das geschah tatsächlich im Betrieb. Ich behob es mit einem Mechanismus, der dieselbe Aktion nur einmal verarbeitet, auch wenn sie zweimal eintrifft (Idempotenz). Die anderen Probleme waren diese: Eine Reservierung ließ sich nicht bestätigen, wenn noch Informationen zu einem gelöschten Menüpunkt vorhanden waren; es gab eine Lücke bei der Prüfung auf Vollbelegung, die Raum ließ, die Kapazität zu überschreiten; niemand bemerkte es, wenn eine Bestätigungs-E-Mail nicht versendet werden konnte; Eingaben wurden auf der Serverseite nicht geprüft; bei einem Fehler erschienen interne Formulierungen auf dem Bildschirm; die Schrift in den Eingabefeldern war so klein, dass der Bildschirm auf dem iPhone von selbst hineinzoomte; und das automatische Vervollständigen von Eingaben funktionierte nicht.

Bei E-Mail-Ausfällen machte ich es möglich, sie im Verwaltungsbildschirm zu erkennen und erneut zu senden. Bei dieser Untersuchung fand ich auch heraus, dass das Prüfprotokoll, das Reservierungsbestätigungen aufzeichnet, schon lange vor der Korrektur jedes Mal fehlgeschlagen war und nichts aufgezeichnet hatte.

Ich behob diese Punkte nacheinander und übernahm sie in den Betrieb.

#### Von KI geschriebenen Code niemals ungeprüft lassen

Was ich aus dieser Erfahrung gelernt habe: Gerade weil ein Programm von KI geschrieben wurde, darf man die Überprüfung nicht auslassen.

KI gibt dem, was man ihr sagt, schnell Gestalt. Aber die Rücksicht auf das, was man ihr nicht sagt, etwa „von außen unlesbar machen“ oder „doppeltes Absenden als eines behandeln“, kommt nicht hinein, wenn man es nicht anweist. Und Löcher wie diese liegen still in Programmen, die aussehen, als würden sie funktionieren.

Menschen müssen nicht den gesamten Code lesen. Die Korrektheit des Programms überwachen maschinelle Prüfungen und die Prüfung durch eine andere KI. Ob das Ergebnis zum Zweck des Lokals passt, überwacht die Lokalleitung. Man muss nicht lesen, aber man darf die Überprüfung nicht auslassen. Das ist meiner Überzeugung nach gemeint, wenn man mit einer agentischen KI baut.

【Abbildung 2-3】Die Regeln, als es von außen lesbar war, und die Regeln nach der Korrektur (Auszug) *(Die Bildschirmanzeige ist auf Japanisch.)*

### 2-4 Wer nach Gefühl baut, vermehrt Widersprüche

Je mehr Funktionen ich hinzufügte, desto mehr Stellen gab es, die mit dem zuvor Entschiedenen kollidierten.

Der typische Fall war die Rabattberechnung. Im Reservierungsformular, auf dem Bestätigungsbildschirm, in der E-Mail und im Verwaltungsbildschirm war die Rabattberechnung an jeder Stelle gesondert geschrieben. Änderte ich an einer Stelle eine Rabattregel, rechnete eine andere Stelle weiter mit der alten Regel. Für dieselbe Reservierung konnten Bildschirm und E-Mail unterschiedliche Beträge zeigen.

Später bündelte ich die Preisberechnung in einer einzigen Datei. Das Reservierungsformular, das Chatfenster und der MCP-Server erzeugen die Preise alle von dort aus.

Auch die Regeln zur Kombination von Rabatten änderten sich im Laufe der Zeit. Wie ich in Kapitel 1 geschrieben habe, sollte die Happy Hour ursprünglich mit anderen Rabatten kombinierbar sein, aber ich stellte fest, dass sie sich nicht rechnet, und änderte sie in nicht kombinierbar. Bei jeder Regeländerung musste sich ein Mensch merken, wo korrigiert werden muss. Das war die Schwäche eines nach Gefühl gebauten Systems.

Es gab auch eine Abweichung zwischen Testumgebung und Betrieb. Beim Testen des Chatfensters zeigte die Frage „Gab es nicht so etwas wie 10% Rabatt?“, dass die Rabattregeln der Testumgebung vom Betrieb abgewichen waren. Unterscheiden sich die Werte der Testumgebung vom Betrieb, kann man die Tests bestehen und im Betrieb trotzdem falsch liegen. Damals legte ich den Grundsatz fest: „Der Betrieb hat recht.“ Seitdem kopiere ich vor jedem Testlauf die Einstellungen aus dem Betrieb in die Testumgebung und bestätige, dass die Abweichung null ist, bevor ich die Tests starte.

KI baut, was man ihr sagt. Aber Widersprüche zu früheren Entscheidungen bemerkt sie nicht. Was Widersprüche verhindert, ist nicht die KI. Es ist, vorher zu entscheiden.

### 2-5 Anforderungsdefinition neu lernen

Nachdem ich über das nach Gefühl gebaute Reservierungssystem nachgedacht hatte, lernte ich die Anforderungsdefinition neu. Anforderungsdefinition heißt: vor dem Bau festzulegen, was man baut, was man nicht baut und wer es wie nutzen wird, und das in einem Dokument festzuhalten.

Als ich noch Systemingenieur war, war das für mich selbstverständlich. Doch sobald ich mit KI bauen konnte, hatte ich es unbemerkt ausgelassen. Man nennt eine Idee, und in wenigen Minuten erscheint etwas Funktionierendes. In diesem Tempo hatte ich die Mühe des Entscheidens weggelassen.

Meine heutige Bauweise hat drei Stufen.

1. Zuerst die Anforderungen im Detail festlegen. Was gebaut wird, was nicht gebaut wird, wer es nutzen wird. Das Verhalten jedes Bildschirms. Der Umgang mit Ausnahmen (Fehler, doppeltes Drücken, Ablauf). Regeln, die sich später leicht widersprechen, wie Preise und Rabatte, lege ich besonders genau fest. Auch diese Arbeit erledige ich im Dialog mit der Chat-KI. Ich lasse die KI vorab Lücken und Widersprüche finden, und die Lokalleitung entscheidet.
2. Das Entschiedene als „Anforderungsdokument“ aufschreiben. Nicht mündliche oder spontane Anweisungen, sondern in einem Dokument gebündelt. Das wird der einzige Maßstab, um später zu prüfen, was richtig ist.
3. Das gesamte Dokument der KI übergeben und sie umsetzen lassen. Ich gebe das gesamte Dokument der KI, die das Programm schreibt (Claude Code), zusammen mit den Bedingungen für das Bestehen (alle Tests bestehen, Prüfung in der Testumgebung vor dem Betrieb und so weiter). Die KI baut selbstständig, bis sie die Bedingungen erfüllt, und prüft selbstständig. Die Lokalleitung schaut nur hin, wenn sie mittendrin anhält, und bei der Endkontrolle.

Zum Beispiel wurde das Anforderungsdokument für das Chatfenster „T-AI-MURO“ von der ersten bis zur dritten Fassung umgeschrieben. In der zweiten Fassung legte ich fest: „die KI keine Preise berechnen lassen“, „das Wissen über das Lokal und die Preisberechnung in ein Fenster legen“ und „das Formular auch für Menschen behalten, die nicht per Chat reservieren möchten“. In der dritten Fassung legte ich fest: „wo die Hauptfassung des Wissens über das Lokal liegt“, „nur dieses Fenster zeigt freie Zeiten“, „den ersten Austausch zu einer Frage mit vier Auswahlmöglichkeiten machen“ und „keine Gesprächsprotokolle speichern, nur die Fragen ablegen, die nicht beantwortet werden konnten“. Weil die Entscheidungen in einem Dokument bleiben, kann ich später nachvollziehen, warum die Dinge so sind, wie sie sind.

Mit dieser Bauweise bemerke ich auch beim Hinzufügen von Funktionen sofort Widersprüche, indem ich mit dem Dokument abgleiche. Gerade in einer Zeit, in der KI das Bauen übernimmt, braucht es die „Fähigkeit zu entscheiden“ vor dem Bauen. Das war die größte Lehre, die ich aus dem Reservierungssystem gezogen habe.

Ich habe außerdem einen Mechanismus gebaut, der das Vorgehen selbst in ein Dokument fasst und der KI übergibt, damit sich diese Bauweise bei jedem Start eines neuen Produkts gleich ausführen lässt. Darüber schreibe ich in Kapitel 4.

【Abbildung 2-4】Inhaltsverzeichnis des Anforderungsdokuments von T-AI-MURO (Fassung 3) *(Die Bildschirmanzeige ist auf Japanisch.)*

### 2-6 Die Sprache der Benutzeroberfläche lernen

Etwas habe ich noch einmal neu gelernt: die Namen der Bildschirmelemente.

Auch wenn ich der KI sagte „Mach hier das und das“, sah der Bildschirm oft anders aus, als ich erwartet hatte. Als ich nach dem Grund suchte, stellte ich fest, dass ich die Namen der Bildschirmelemente nicht kannte. Selbst wenn ich „ein kleines Fenster, das oben drauf erscheint“ oder „einen Hinweis, der nach ein paar Sekunden verschwindet“ beschrieb, konnte die KI nur schwer erkennen, was ich meinte.

Also las ich ein Fachbuch zur UI (User Interface, also Aussehen und Bedienung eines Bildschirms) und lernte die Namen der Elemente und die Fachbegriffe des Designs.

| Element | Was es ist |
| --- | --- |
| Modal | Ein kleines Fenster, das über dem Bildschirm erscheint. Der Bildschirm dahinter lässt sich erst bedienen, wenn man es schließt |
| Toast | Ein Hinweis, der für ein paar Sekunden am Rand des Bildschirms erscheint und von selbst wieder verschwindet |
| Tab | Ein Mechanismus, bei dem ein Druck auf eine Überschrift den Inhalt umschaltet |
| Accordion | Ein Mechanismus, bei dem ein Druck auf eine Überschrift den Inhalt auf- und zuklappt |
| Drawer | Ein Menü, das wie eine Schublade seitlich aus dem Bildschirm herausgleitet |
| Weitere | Breadcrumbs (eine Spur, die zeigt, wo man gerade ist), Carousels (Einträge, durch die man seitlich scrollt), Bottom Sheets (ein Bereich, der vom unteren Bildschirmrand hochfährt) und so weiter. Mit jedem Namen, den Sie lernen, können Sie der KI in einem einzigen Satz Anweisungen geben |

Wenn man die Elemente beim Namen nennt, kommen die Bildschirme der KI schon beim ersten Versuch nah ans Ziel. Sagt man: „Zeige den Bestätigungsbildschirm der Reservierung als Modal“, zögert die KI nicht.

#### Die KI schlägt beim Hinzufügen und Kürzen in Extreme aus

Auch nachdem ich die Wörter gelernt hatte, hatte der Bau von Bildschirmen mit KI eine andere Art von Schwierigkeit. Die KI schwankt stark.

Als ich für die Reservierungsseite einen „stilvollen“ Header wünschte, bekam ich einen eindrucksvollen, wuchtigen Header. Aber bei einer Reservierungsseite geht es nur um Reservierungen. Für Stammkundschaft, die jedes Mal bucht, ist ein hoher Header mit langen Erklärungen bloß lästig. Ich ließ die Höhe um etwa die Hälfte kürzen und dabei dieselbe Menge an Informationen behalten.

Als ich die Fußzeile der E-Mails vereinheitlichte und einen Link zum Zweites-Lokal-Heft einfügte, wirkte der Haupttext daneben schlicht und dürftig. Also fügte ich auch dem Haupttext eine Überschrift, eine Tabelle mit den wichtigsten Punkten und eine Schaltfläche hinzu. Als ich in der Fußzeile einen Zugang zum Chatfenster ergänzte, wirkte alles überladen. Als ich ihn auf zwei Linkzeilen mit Trennstrichen zusammenpresste, war es aufgeräumt, aber unauffällig. Am Ende landete es bei zwei Karten, die die Rolle danach zeigen, „wann man sie nutzt“. Die linke ist „für Ihre nächste Reservierung“, die rechte „nach Ihrem Essen“.

Zu wuchtig, zu knapp, zu auffällig. Was jedes Mal das richtige Maß bestimmte, waren die Worte der Lokalleitung.

#### Ein Designvorschlag ohne Bilder

Auch das ist passiert. Ich bat die KI, die Programme schreibt, mithilfe einer Design-KI (Claude Design) Verbesserungsvorschläge für das Chatfenster zu erstellen, und es kam ein Bericht zurück: „Ich habe Vorschläge für acht Bildschirme gemacht.“ Als ich ihn öffnete, gab es aber nur Textbeschreibungen. Die KI hatte keine Bilder zeichnen können, und doch blieb nur die Meldung „fertig“ übrig.

Am Ende zeichnete die Chat-KI vier Vorschläge direkt in der Designoberfläche. Sie übernahm die Farben des aktuellen Bildschirms aus einem Screenshot, stellte die Geschichte des Lokals als Zeitleiste dar, teilte die Würzung in zwei Felder, „Garart“ und „Geschmack“, machte aus den Angeboten Erklärkarten und vereinheitlichte die Preise zu einer Reservierungsübersicht.

Lässt man die KI einen Test ausführen, sagt sie „bestanden“. Bittet man die KI um ein Design, sagt sie „fertig“. Zu prüfen, was wirklich drin ist, ist Sache des Menschen. Der Maßstab für das Urteil ist etwas, das nur Menschen dauerhaft festhalten können.

#### Was Sie aus diesem Kapitel mitnehmen können

- Etwas zu bauen, das funktioniert, und es sicher betreiben zu können, sind zwei verschiedene Dinge.
- Prüfen Sie die Ergebnisse der KI nicht anhand ihrer Worte, sondern anhand von Tests. Einem Test können Sie erst vertrauen, wenn Sie geprüft haben, dass er fehlschlägt, sobald Sie etwas kaputt machen.
- Berechnungen, die nicht falsch sein dürfen, etwa Preise, sollten Sie nicht der Textgenerierung der KI überlassen. Geben Sie sie dem Programm.

Die Fortsetzung dieses Kapitels (neu entdeckte Lücken und die Schritte, mit denen ich sie geschlossen habe) finden Sie auf note und X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Kapitel 3: Die Werkzeuge meines Lokals an andere Lokale weitergeben

### 3-1 Das kleine grüne Schild auf der Reservierungsseite

Öffnen Sie die Reservierungsseite von Tamuro, dann sehen Sie oben ein kleines grünes Schild. Solange das Lokal geöffnet ist, steht dort „OPEN“, und wenn es schließt, „CLOSED“. Drückt die Lokalleitung die Verlängerungstaste, rückt die Schließzeit um 30 Minuten nach hinten, und ein Hauch Zinnoberrot erscheint auf dem Schild.

Eigenständige Restaurants haben eines gemeinsam. Sie öffnen fast auf die Minute pünktlich, aber das Schließen zieht sich oft in die Länge. Läuft das Gespräch mit den Gästen gut, brennt das Licht auch nach der letzten Bestellung um 22:30 Uhr noch.

Von der Seite der Gäste aus lässt sich das aber nicht erkennen. Die Anzeige „Geöffnet“ auf Google Maps wird allein anhand der hinterlegten Öffnungszeiten ermittelt und berücksichtigt deshalb weder Verlängerungen noch frühere Schließungen noch vorübergehende Schließtage. Niemand geht nach der Schließzeit noch zu einem Lokal und denkt: „Vielleicht ist ja noch offen.“ Auch anzurufen und nachzufragen, fühlt sich unangenehm an.

Dieses Schild ist ein Werkzeug, das die Frage „Hat es noch auf?“ beantwortet. Es heißt „AgendaLuce (Licht-Notizbuch)“. Luce bedeutet auf Italienisch „Licht“.

Das Licht-Notizbuch ist so gebaut, dass es fast ohne Aufmerksamkeit der Lokalleitung läuft. Tragen Sie die Öffnungs- und Schließzeiten für jeden Wochentag einmal ein, und das Schild schaltet sich automatisch ein und aus. Die Lokalleitung fasst es nur an, wenn sie verlängert, früher schließt oder einen Ruhetag einlegt. Zum Verlängern drücken Sie auf dem Smartphone eine einzige Taste. Auch das Team kann es über einen eigenen Link bedienen, der ohne Anmeldung funktioniert.

Die Gäste brauchen weder Anmeldung noch Registrierung. Öffnen sie die öffentliche Seite, sehen sie den aktuellen Zustand des Lichts. Fügt man sie dem Startbildschirm des Smartphones hinzu, funktioniert sie wie eine App. Das kleine Schild-Widget lässt sich auch in andere Websites einbetten. Was auf der Reservierungsseite von Tamuro erscheint, ist genau dieses Widget.

Das Licht-Notizbuch ist kostenlos. Wenn Sie nur das Schild-Widget in Ihre Website einbetten, dauert die Einrichtung etwa 10 Minuten.

Und jetzt kommt das Wichtige. Dieses Licht-Notizbuch ist nicht nur für Tamuro da. Jedes Lokal kann es nutzen.

Den Namen des Lokals habe ich bewusst aus dem Design des Schilds herausgelassen. Stünde ein Name darauf, wäre es ein Schild für Tamuro. Auch die Anzeigesprache lässt sich wählen. Ich habe die Komponente klein gehalten, damit sie sich in die Website jedes Lokals einbetten lässt.

Ein Werkzeug, das aus Tamuros Problem „das Schließen zieht sich in die Länge“ entstand und von Anfang an so gebaut wurde, dass jede und jeder es nutzen kann. Das ist das Licht-Notizbuch. Und die Sammlung solcher Werkzeuge ist die „Agenda-Reihe“.

【Abbildung 3-1a】Das Schild des Licht-Notizbuchs oben auf der Reservierungsseite (geöffnet) *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-1b】Während einer Verlängerung erscheint ein Hauch Zinnoberrot *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-6a】Der Bildschirm der Lokalleitung. Zum Verlängern drücken Sie die Taste einmal *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-6b】Direkt nach dem Druck auf „Verlängern“. Die Schließzeit rückt um 30 Minuten nach hinten *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-6c】Die öffentliche Seite, die die Gäste sehen (während einer Verlängerung) *(Die Bildschirmanzeige ist auf Japanisch.)*

### 3-2 Es begann mit dem schwarzen Ledernotizbuch

Die Agenda-Reihe war nicht als Reihe geplant. Sie begann mit einem einzigen System, das bis heute nicht einmal veröffentlicht ist.

Was ich zuerst bauen wollte, war ein Mechanismus, der die Gesichter der Gäste erkennt und Stammkundschaft willkommen heißt. Eine Kamera am Eingang des Lokals unterscheidet die Besuchenden am Gesicht und gibt der Lokalleitung Bescheid: „Das ist die Person, die letztes Mal das Tonteki hatte, die ich seit drei Monaten nicht gesehen habe.“ Ich wollte, dass eine Maschine die Aufgabe übernimmt, die die Leitung eines kleinen Lokals im Kopf erledigt: sich Gesichter, Namen und Vorlieben zu merken.

Doch kurz nachdem ich mit dem Bau begonnen hatte, wurde mir klar, dass diesem System etwas sehr Schwerwiegendes anvertraut wird. Gesichter. Merkmale. Besuchshistorie. Der Charakter eines Gastes. All das sind Informationen, die sich nie wieder zurückholen lassen, wenn sie einmal nach außen gelangen.

Was mir damals in den Sinn kam, war Seicho Matsumotos „Das schwarze Ledernotizbuch“. Eine Aufzeichnung, die niemandem gezeigt wird und doch ganz sicher existiert. Ein Verzeichnis, das, einmal aufgeschlagen, über Leben und Tod von Menschen entscheidet. Ist das nicht genau das, was ich hier zu bauen versuche?

Auf Italienisch heißt „Notizbuch“ Agenda und „schwarz“ Nera. Zusammengesetzt: AgendaNera. Das schwarze Ledernotizbuch. So wurde zuerst der Name festgelegt.

AgendaNera ist noch im Bau. Es ist dasjenige der Reihe, das ich am sorgfältigsten baue.

Und diese Namensgebung war der Auslöser. Wenn es ein schwarzes Notizbuch gibt, kann es auch Notizbücher in anderen Farben geben. Ich würde die Mechanismen, die ich in meinem eigenen Lokal jeden Tag nutze, in Formen umbauen, die jedes Lokal nutzen kann, und sie Notizbuch für Notizbuch veröffentlichen. Das ist die [Agenda-Reihe](https://bontallc.com/agenda?via=b2-de-{{FMT}}).

### 3-3 Notizbuch für Notizbuch hinzufügen

Die Agenda-Reihe ist eine Sammlung kleiner Web-Apps, die jeweils ein Problem eines Restaurants mit einem Werkzeug lösen. Jede hat einen italienischen Namen und einen japanischen Spitznamen, der auf „Notizbuch“ endet. Jeder Name hat seine eigene Herkunft.

| Name | Spitzname | Herkunft des Namens | Was es tut |
| --- | --- | --- | --- |
| AgendaTimbro | Zeiterfassung | Timbro bedeutet „Stempel“. Es ist das Einstempeln selbst | Erfasst Kommen und Gehen des Teams |
| AgendaOro | Rentabilität | Oro bedeutet „Gold“. Das Geld-Notizbuch | Schätzt die Rentabilität für die Eröffnung eines Lokals oder die Einführung eines neuen Gerichts (kostenlos) |
| AgendaBis | Zweites-Lokal-Heft | Bis bedeutet „Zugabe“. Das „Bis!“, das im Konzert aus dem Publikum gerufen wird | Weist Gäste zu einem nahen zweiten Lokal (kostenlos) |
| AgendaQA | Hilfe-Center | Qua bedeutet „hier“. Bei Problemen: hier | Die gemeinsame Hilfestelle der Reihe (kostenlos) |
| AgendaLuce | Licht-Notizbuch | Luce bedeutet „Licht“ | Zeigt an, ob das Lokal geöffnet ist (kostenlos) |
| AgendaRicetta | Wareneinsatz-Heft | Ricetta bedeutet „Rezept“ | Berechnet die Kosten und die Wareneinsatzquote eines Rezepts (kostenlos) |
| AgendaNera | Stammgast-Heft | Nera bedeutet „schwarz“. Das schwarze Ledernotizbuch | Begrüßt Stammkundschaft per Gesichtserkennung (im Bau) |
| AgendaTurno | Dienstplan-Heft | Turno ist Italienisch für „Reihenfolge“ oder „Schicht“ | Sammelt die Schichtwünsche des Teams und verteilt den Plan, den die eigene KI der Lokalleitung erstellt (in Kürze) |

Welches Notizbuch passt zu welchem Lokal? Die Zeiterfassung ist für Lokale mit zwei oder mehr Teammitgliedern, die die Anwesenheit auf Papier oder in LINE *(Japans meistgenutzter Messenger)* verwalten. Die Rentabilität ist für alle, die kurz vor der Eröffnung eines Lokals stehen, und für alle, die ihre Zahlen überprüfen wollen, weil sich Miete oder Kosten geändert haben. Das Zweites-Lokal-Heft ist für Lokale, in deren Mittelpunkt das Essen steht und die ihre Gäste früh zum nächsten Ort weiterschicken möchten. Das Licht-Notizbuch ist für eigenständige Lokale, deren Schluss später oder früher kommt als geplant. Das Wareneinsatz-Heft ist für Lokale, in denen die Rezepte im Kopf stecken, aber noch nie ein Kostenanteil ausgerechnet wurde.

#### Die Zeiterfassung berechnet keine Löhne

Die Zeiterfassung macht das Tablet des Lokals oder die Smartphones des Teams so, wie sie sind, zum Stempelgerät. Man tippt nur auf den eigenen Namen. Das Anwesenheitsblatt wird automatisch ausgewertet und lässt sich als CSV exportieren (ein Format, das sich in Tabellenkalkulationen öffnen lässt). Der Geschäftstag beginnt um 5 Uhr morgens, sodass das Datum auch bei Öffnungszeiten bis spät in die Nacht nicht umspringt.

Aber diese Zeiterfassung berechnet bewusst keine Löhne.

Stundenlöhne, Zulagen und Stichtage unterscheiden sich von Lokal zu Lokal zu stark. Nachtzuschlag von 25%, Feiertage als eigene Kategorie, Fahrtkosten als Tagespauschale. Wie ich es auch gebaut hätte, es würde bei irgendeinem Lokal nicht passen.

Statt zu berechnen, habe ich deshalb „eine Vorlage mit Anweisungen für eine KI“ vorbereitet. Die Lokalleitung fügt die heruntergeladene Anwesenheits-CSV und diese Vorlage unverändert in die KI ein, die sie ohnehin nutzt, sei es ChatGPT, Claude oder Gemini. Dann berechnet die KI Nachtzuschläge, Feiertagszuschläge und Fahrtkosten und listet sie auf. Die Regeln jedes Lokals, etwa „bei uns ist Abrechnungsschluss zum Monatsende, nachts gibt es 25% Zuschlag, und Sonntage sind eine eigene Kategorie“, lassen sich der Vorlage hinzufügen und werden unverändert berücksichtigt. Die CSV enthält Spalten für den Wochentag und den Namen des Feiertags, damit die KI richtig rechnen kann.

Den Berechnungsmechanismus halte ich selbst nicht in der Hand; jedes Lokal behält seine Regeln in der eigenen Hand. Ich dachte mir, dass das die Variante ist, die am schwersten kaputtgeht.

#### Zu einem zweiten Lokal weisen und das eigene Lokal in Erinnerung halten

Das Zweites-Lokal-Heft ist ein Werkzeug, um eine „Seite mit dem Weg zum nächsten Lokal“ zu erstellen, die man den Gästen mitgibt. Gästen, die ihr Essen beendet haben, zeigt sie eine nahe gelegene Bar oder einen Ort für einen letzten Happen, samt Gehzeit in Minuten.

Es sieht aus wie ein Werkzeug, das Gäste woandershin schickt, aber es steckt ein kleiner Kniff darin. Wer zu einem zweiten Lokal weist, bringt damit zum Ausdruck, dass das erste Lokal das eigene war. Während es scheinbar Gäste wegschickt, prägt es ihnen in Wahrheit ein: „Das erste Lokal war dieses.“ So ist es gedacht.

#### Drei Gestaltungsprinzipien: automatisch, geliehene Stärke, eine Funktion

Alle Notizbücher der Agenda-Reihe teilen drei Prinzipien.

Das erste ist „automatisch“. Es soll laufen, ohne dass die Lokalleitung es jeden Tag anfassen muss. Beim Licht-Notizbuch schaltet sich das Licht von selbst ein und aus, sobald der Zeitplan eingetragen ist. Wer ein Restaurant führt, hat während des Betriebs keine Zeit, einen Bildschirm zu berühren. Ein Werkzeug, das nur funktioniert, wenn man es anfasst, wird irgendwann nicht mehr benutzt.

Das zweite ist „geliehene Stärke“. Man baut nicht alles selbst, sondern überlässt Dinge den Werkzeugen und der KI, die die Lokalleitung ohnehin nutzt. Die Lohnabrechnung der Zeiterfassung ist das Musterbeispiel. Beim Dienstplan-Heft ist es genauso: Es kümmert sich nur um das Einsammeln der Wünsche des Teams und überlässt das Erstellen der Schichten der eigenen KI der Lokalleitung. Es trägt weder einen eigenen komplizierten Mechanismus noch die Kosten für den Aufruf einer KI. Deshalb lässt sich der Preis niedrig halten.

Das dritte ist „eine Funktion“. Ein Notizbuch macht nur eine Sache, und die zuverlässig. Ein Multifunktionssystem ist für ein eigenständiges Lokal zu schwer. Je mehr Funktionen man hinzufügt, desto schwerer wird die Bedienung, und desto mehr Widersprüche häufen sich auf der Seite der Entwicklung. Das habe ich beim Reservierungssystem in Kapitel 2 schmerzlich gelernt. Deshalb füge ich Notizbücher einzeln hinzu, und jedes erledigt „nur diese eine Sache richtig“.

#### Warum das Reservierungssystem nicht zur Reihe gehört

An dieser Stelle erwarte ich eine naheliegende Frage. Das Reservierungssystem ist das, in das Tamuro die meiste Arbeit gesteckt hat. Warum gehört es nicht zur Agenda-Reihe?

Tatsächlich hatte ich das einmal vor. Der Plan war, das Reservierungssystem in eine Form zu bringen, die andere Restaurants nutzen können, und es als ein Notizbuch der Reihe zu veröffentlichen. Doch im August 2026 habe ich diesen Plan abgeblasen.

Der Grund ist genau das, worüber ich in Kapitel 1 geschrieben habe. Das Reservierungssystem von Tamuro ist vollgepackt mit Tamuros Art, Geschäfte zu machen. Dass Gäste, die allein kommen, die Hälfte ausmachen. Dass fast 90% der Reservierungen am selben Tag erfolgen. Dass ich die Zeit vor der Öffnung verkaufen möchte. Dass ich möchte, dass Gruppen kommen. Dass ich Stammkundschaft aufbauen möchte. Die Rabattkombinationen, die Reihenfolge der E-Mails und die Art, wie der Chat Empfehlungen ausspricht, habe ich alle darauf zugeschnitten.

Würde ich es so ausdünnen, dass es jede und jeder nutzen kann, würde daraus ein gewöhnliches Reservierungssystem, das zu jedem Lokal nur halbwegs passt. Dann ginge Tamuros Stärke verloren. Das Reservierungssystem und das CRM sind die Art, wie das Lokal verkauft. Statt das Lokal an ein allgemeines System anzupassen, sollte man das System des Lokals an das Lokal anpassen. Unser Lokal, nach unseren eigenen Vorgaben. Also habe ich entschieden, Tamuros Reservierungssystem allein für Tamuro zu behalten.

Gibt es also nichts, was über das Lokal hinaus weitergegeben wird? Doch. Rund um das Reservierungssystem gibt es viele kleine Probleme, die jedes Lokal teilt. Den Kern des Lokals behält man nach eigenen Vorgaben. Die Werkzeuge, die die Probleme drumherum lösen, baut man von Anfang an in einer Form, die alle nutzen können, und gibt sie weiter. Die Reservierungsseite von Tamuro ist ein Beispiel, das beides auf einem einzigen Bildschirm nebeneinanderstellt. Über einem Reservierungssystem allein für Tamuro sitzt das Schild des Licht-Notizbuchs, das alle nutzen können.

【Abbildung 3-2】Die Vorstellungsseite der Agenda-Reihe *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-3a】Vorstellung der Zeiterfassung *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-3b】Vorstellung der Rentabilität *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-3c】Vorstellung des Zweites-Lokal-Hefts *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 3-4】Der Stempelbildschirm der Zeiterfassung. Man tippt nur auf den eigenen Namen (synthetische Daten) *(Die Bildschirmanzeige ist auf Japanisch.)*

### 3-4 Von Anfang an allgemein nutzbar bauen

Ich baue ein Werkzeug für mein eigenes Lokal und gebe es dann auch an andere Lokale weiter. Das klingt einfach, aber damit es gelingt, muss sich die Art ändern, wie man Dinge vor dem Bauen entscheidet.

Würde ich nur für Tamuro bauen, wäre der schnellste Weg, Tamuros Öffnungszeiten und Tamuros Namen direkt in das Programm zu schreiben. Dann könnte aber kein anderes Lokal es nutzen. Wenn man es später verallgemeinern will, muss man jede fest eingetragene Stelle aufspüren und einzeln korrigieren.

Deshalb sind die Werkzeuge der Agenda-Reihe von Anfang an unter der Voraussetzung ausgelegt, dass alle sie nutzen können. Ich gehe von einem Problem bei Tamuro aus, aber bei der Anforderungsdefinition trenne ich zwei Fragen: „Gilt das nur für Tamuro, oder gilt es für jedes Lokal?“ Keinen Namen des Lokals aufs Schild setzen. Die Sprache wählbar machen. Es in jede Website einfügbar machen. Solche Entscheidungen habe ich beim Schreiben des Anforderungsdokuments für das Licht-Notizbuch getroffen.

Das ist ein weiterer Nutzen der Anforderungsdefinition, die ich in Kapitel 2 neu gelernt habe. Wenn man diese Dinge zuerst festlegt, kann man das Werkzeug bei Tamuro einsetzen und unverändert an andere Lokale weitergeben.

Die Probleme in meinem Lokal sind auch die Probleme in anderen Lokalen. Ich bin nicht die einzige Person hinter einem Tresen, die den Gästen sagen möchte, dass die Schließzeit nach hinten rückt. Wer ein eigenständiges Lokal führt, baut aus dem eigenen Problem ein Werkzeug und gibt es an andere Lokale weiter. Das ist der Gedanke hinter der Agenda-Reihe.

### 3-5 Die Demokratisierung der Technik

Die Agenda-Reihe umfasst inzwischen mehr als 10 Produkte. Ich baue und betreibe sie allein, während ich hinter der Bar stehe.

Vor ein paar Jahren wäre das undenkbar gewesen. Um ein einziges Produkt zu bauen, brauchte man jemanden für die Planung, jemanden für das Design der Bildschirme, jemanden für den Code, jemanden für die Tests und jemanden für den Betrieb. Ohne Team und Geld konnte man kein Produkt auf den Markt bringen.

Das gilt nicht mehr. Die Lokalleitung nennt der KI die Anforderungen, die KI schreibt den Code, die KI testet ihn, und eine weitere KI prüft ihn. Was die Lokalleitung tut, ist zu entscheiden, was gebaut wird, zu beurteilen, ob die Ergebnisse der KI zum Zweck des Lokals passen, und nur die Arbeiten zu erledigen, die allein Menschen leisten können.

Diese Art von Wandel nennt man allgemein die „Demokratisierung der Technik“. Die Fähigkeit, selbst Software zu bauen, ist nicht mehr das Vorrecht weniger Menschen oder Unternehmen.

Aber lassen Sie mich hier ehrlich sein. Wie ich in der Einleitung geschrieben habe, habe ich etwa 16 Jahre in der IT gearbeitet, hauptsächlich in der Systemplanung und als Vermittler zwischen den Menschen vor Ort und den Entwicklungsfirmen. Anforderungsdefinition, Denkweisen rund um Datenbanken und den Ablauf von Tests kannte ich alle aus Erfahrung. Ich behaupte also nicht, dass Menschen, die noch nie eine Zeile Code geschrieben haben, ab morgen dasselbe tun könnten.

Dennoch hat sich sehr viel verändert. Ich kann heute allein und in den Lücken meiner Hauptarbeit Dinge bauen, für die früher ein Team nötig war. Und für Menschen ohne Erfahrung ist der Einstieg ganz sicher niedriger geworden. Die KI erklärt es Ihnen, wenn Sie nach etwas fragen, das Sie nicht verstehen. Sie gibt dem Gestalt, was Sie ihr in Worten sagen. Was fehlt, ist nicht Technik, sondern die Fähigkeit zu entscheiden, was gebaut wird, und die Worte, um es der KI zu sagen. Das sind Fähigkeiten, die Menschen, die ein Lokal führen, ohnehin jeden Tag einsetzen.

### 3-6 Die Debatte um den „Tod von SaaS“

Software, die man über das Internet gegen eine monatliche Gebühr nutzt, wie die Agenda-Reihe, heißt SaaS (Software as a Service). Buchhaltungssoftware, Zeiterfassung, Reservierungsverwaltung. Restaurants arbeiten heute mit einer Menge SaaS.

Wird die KI SaaS beenden? 2026 flammte diese Debatte in großem Stil auf.

Ein Auslöser war eine Äußerung von Satya Nadella, dem CEO von Microsoft. In einem Podcast im Dezember 2024 sagte Nadella, SaaS-Anwendungen würden im Zeitalter der KI-Agenten zusammenbrechen. Die Begründung: Sobald KI-Agenten den Teil der geschäftlichen Entscheidungen übernehmen, braucht man keine Software mehr, die dafür gebaut ist, dass Menschen sie über Bildschirme bedienen.

Dann, im Februar 2026, kündigte Anthropic Claude Cowork an (ein KI-Werkzeug, das Geschäftsaufgaben eigenständig erledigt), und die Aktien amerikanischer Softwareunternehmen wurden massiv verkauft. An der Wall Street bekam der Einbruch den Namen „SaaSpocalypse“. Die Anlegenden fürchteten, dass das SaaS-Modell, pro Person eine Gebühr zu verdienen (Preisgestaltung pro Nutzerplatz), zusammenbricht, wenn KI-Agenten die Arbeit machen.

Es gibt auch Gegenargumente. Jensen Huang, der CEO von Nvidia, sagte, KI-Agenten würden Software nicht ersetzen, sondern im Auftrag von Menschen nutzen, und bezeichnete den Ausverkauf als Überreaktion. Nicht wenige andere sehen ein SaaS, das KI in sich aufnimmt, eher noch gestärkt.

Wird SaaS wirklich sterben? Das ist meine Einschätzung.

Sterben wird die mittlere Schicht von SaaS: die Art, die eine hohe monatliche Gebühr pro Nutzerplatz verlangt und davon ausgeht, dass Menschen sie über Bildschirme bedienen. Wenn die KI die Arbeit anstelle von Menschen erledigt, braucht man keine Plätze für jede einzelne Person. Wenn niemand einen Bildschirm bedient, braucht man keine aufwendige Bedienoberfläche.

Was bleibt, sind Werkzeuge, die günstig sind und eine Sache zuverlässig tun. Und Werkzeuge, die für die KI leicht zu benutzen sind.

Das sind genau die drei Prinzipien der Agenda-Reihe. Sie läuft automatisch, sie überlässt Arbeit der KI der Lokalleitung (geliehene Stärke), und sie tut nur eine Sache (eine Funktion). AgendaTurno überlässt das Erstellen des Dienstplans der KI der Lokalleitung, und das ist genau die Form „Die KI nutzt die Software“, die Huang beschreibt. Das Reservierungssystem von Tamuro öffnet über MCP ein Fenster für die KI der Gäste, und das ist derselbe Gedanke.

Natürlich mag hier ein Widerspruch zu stecken scheinen. Ich spreche vom Tod von SaaS, und doch ist die Agenda-Reihe selbst SaaS. Aber die Agenda-Reihe ist eine Sammlung von Werkzeugen, die ich für mein eigenes Lokal gebaut und dann zu einem niedrigen Preis öffentlich gemacht habe. Sie ist kein Modell, das pro Nutzerplatz eine hohe Monatsgebühr verlangt, und sie setzt nicht voraus, dass Menschen jeden Tag am Bildschirm kleben. Sie ist von Anfang an auf der Annahme gebaut, dass die KI sie nutzt.

#### Der „Tod von SaaS“ für Restaurants

Diese Debatte mag nach einer Geschichte über Anlegende und die IT-Branche klingen. Für Restaurants steht jedoch dasselbe in einer viel vertrauteren Form bevor.

Viele eigenständige Lokale zahlen monatliche Gebühren an Gourmet- und Reservierungsportale und obendrein für jede Reservierung eine Vermittlungsprovision. Im Gegenzug für die Vermittlung von Gästen hält das Portal die Verbindung zu den Gästen, und es ist nicht ungewöhnlich, dass dem Lokal nicht einmal die Kontaktdaten der Gäste vorliegen. Erhöht das Portal die Preise, bleibt dem Lokal nichts anderes übrig, als sich zu fügen, und ändert sich das Ranking-System, ändert sich der Strom der Gäste.

Wie ich in Kapitel 1 geschrieben habe, begann 2026 das Zeitalter, in dem Gäste ihre eigene KI nach Lokalen suchen lassen. Verlagert sich der Einstiegspunkt zur KI, gerät die ganze Ordnung ins Wanken, in der man einem Portal Monatsgebühren und Provisionen zahlt, um in dessen Listen weit oben zu stehen. Wenn ein Lokal von sich aus ein Fenster zur KI öffnet, können die Gäste es erreichen, ohne über die großen Portale zu gehen. Die Reservierungsdaten und die Beziehung zu den Gästen bleiben in den Händen des Lokals.

Wenn ich den „Tod von SaaS“ in die Worte eines eigenständigen Lokals fasse, ist es „das Ende der Zeit, in der man gegen Bezahlung gelistet wurde“. Tamuro hat sein Fenster über MCP geöffnet und führt Reservierungen und CRM nach eigenen Vorgaben, als Vorbereitung darauf.

Ob SaaS sterben wird, weiß noch niemand. Aber die Gestalt der Werkzeuge, die im Zeitalter der KI bleiben werden, zeichnet sich allmählich ab. Davon bin ich überzeugt.

### 3-7 Geld verdienen: im Kleinen, in großer Zahl, günstig

Ich baue die Agenda-Reihe mit dem Ziel, dass sie sich als Geschäft trägt. Das Ziel ist, sie zu einer zweiten Einkommenssäule neben dem Restaurant zu machen.

Die Preise setze ich klein und niedrig an. Die Monatsgebühren beginnen bei ein paar hundert Yen. Die Zeiterfassung zum Beispiel kostet ¥500 (ca. $3,3) im Monat. Dazu mische ich kostenlose Werkzeuge wie die Rentabilität, das Licht-Notizbuch und das Wareneinsatz-Heft. Die kostenlosen Werkzeuge sind der Eingang, über den man die Agenda-Reihe kennenlernt. Das Licht-Notizbuch nutzt weder eine Karten-API noch generative KI, sodass der Betrieb fast nichts kostet. Deshalb kann ich es kostenlos abgeben.

Es gibt ein einziges Konto. Mit einem gemeinsamen Konto namens AgendaID können Sie jedes Werkzeug der Reihe nutzen. Sie müssen sich nicht für jedes Werkzeug erneut registrieren. Kostenpflichtige Werkzeuge haben einen kostenlosen Zeitraum von drei Monaten und lassen sich ohne Hinterlegung einer Kreditkarte starten. Der kostenlose Zeitraum gilt nur einmal pro Kombination aus Lokal und Produkt. Wenn Sie ein anderes Lokal empfehlen, erhalten Sie einen Bonus.

Der Grund, warum ich die Preise niedrig halten kann, liegt in der Art, wie ich baue. Ich baue allein, ich lasse die KI bauen, und ich verwende ein gemeinsames Fundament wieder. Die Datenbankkosten halte ich für die ganze Reihe bei etwa $35 im Monat. Wenn sowohl die Entwicklungskosten als auch die Betriebskosten klein sind, kann ein Geschäft schon mit kleinen Umsätzen bestehen.

Ich sage es ehrlich. Zum Zeitpunkt, an dem ich dieses Buch schreibe, haben einige Lokale die Werkzeuge ausprobiert, aber es gibt fast keine kostenpflichtigen Registrierungen. Das System zum Bauen steht, das System, bekannt zu werden, liegt noch vor mir. Dieses Buch soll auch genau diesem Zweck dienen, nämlich bekannt zu werden.

#### Etwas zu bauen und dafür zu sorgen, dass es weiter genutzt wird, sind zwei verschiedene Dinge

Ich möchte noch etwas ehrlich sagen. Ein Werkzeug bauen zu können und dafür zu sorgen, dass jemand es weiter nutzt, sind getrennte Angelegenheiten.

Das Bauen ist dank der KI schneller geworden. Aber damit Menschen es weiter nutzen, braucht es andere Arbeit. Fragen zur Bedienung beantworten (dafür gibt es das Hilfe-Center). Vor Ende des kostenlosen Zeitraums eine Mitteilung schicken. Den Grund erklären, wenn ein Preis steigt. Die Daten ordentlich löschen, wenn jemand kündigen möchte. Und vor allem: dafür sorgen, dass es läuft, ohne dass die Lokalleitung eingreifen muss.

Von den drei Prinzipien der Agenda-Reihe ist „automatisch“ das Prinzip für dieses „Weiternutzen“. Ein Werkzeug, das nur funktioniert, wenn die Lokalleitung jeden Tag Hand anlegen muss, wird irgendwann gekündigt. Mit dem Bauen allein ist es nicht getan. Zu einem Geschäft wird es erst, wenn es weiter genutzt wird. Einzeln Lokale hinzuzugewinnen, die es weiter nutzen: Das ist meine Aufgabe nach der Veröffentlichung dieses Buchs.

#### Wenn Sie in Ihrem eigenen Lokal anfangen möchten

Wenn Sie dieses Buch gelesen haben und es in Ihrem eigenen Lokal ausprobieren möchten, gibt es drei Schritte.

1. Öffnen Sie https://bontallc.com/agenda?via=b2-de-{{FMT}} und melden Sie sich mit einem Google-Konto an (AgendaID wird erstellt. Eine Kreditkarte ist nicht nötig)
2. Fügen Sie zuerst ein kostenloses Notizbuch hinzu. Ich empfehle das Licht-Notizbuch. Sie fügen nur das Schild-Widget in Ihre Website ein, und in 10 Minuten läuft es. Wenn Sie noch nicht eröffnet haben, probieren Sie die Rentabilität
3. Wenn es zu passen scheint, probieren Sie die Zeiterfassung drei Monate kostenlos aus. Bei nahender Frist kommt eine Mitteilung, sodass Ihnen nichts berechnet wird, auch wenn Sie es einfach liegen lassen

Bei Fragen wenden Sie sich an das Hilfe-Center (AgendaQA). Die KI beantwortet Fragen zur Bedienung sofort, und Fragen zu Spezifikationen und Fehlern lese ich selbst.

Die Umsätze eines Restaurants hängen vom Wetter und von der Jahreszeit ab. Die Zahl der Plätze und die Öffnungszeiten haben beide Grenzen. Die Verkäufe von Werkzeugen haben dagegen keine Grenze bei den Plätzen. Ein Lokal zu führen und dabei Werkzeuge weiterzugeben, die aus den Problemen des eigenen Lokals entstanden sind, und daraus langsam ein Einkommen werden zu lassen: Ich glaube, das kann für ein eigenständiges Lokal ein weiterer Weg sein, Geld zu verdienen.

#### Klein bleiben und global werden

Es gibt noch etwas, das ich bei der Agenda-Reihe von Anfang an entschieden habe. Ich habe entschieden, sie nicht nur auf Japanisch zu bauen.

Die Zeiterfassung, die Rentabilität und das Hilfe-Center lassen sich alle in 20 Sprachen nutzen. Die Bildschirmtexte und die häufig gestellten Fragen, alles. Ein Werkzeug, das für eine Bar mit 19 Plätzen in Tokio gebaut wurde, funktioniert genauso auf Englisch, auf Koreanisch, auf Vietnamesisch.

Dafür gibt es zwei Gründe. Der eine ist, dass sich die Probleme von Restaurants nicht ändern, wenn sich das Land ändert. Sie möchten festhalten, wann das Team kommt und geht. Sie möchten vor der Eröffnung Ihre Rentabilität kennen. Sie möchten den Gästen sagen, dass die Schließzeit heute nach hinten rückt. Das sind alles Probleme, die eigenständige Lokale auf der ganzen Welt teilen. Der andere ist, dass die Zahl der eigenständigen Lokale in Japan weiter sinkt. Würde ich nur den japanischsprachigen Markt bedienen, hätte der Verkauf der Werkzeuge eine Obergrenze.

Früher brauchte ein kleines Unternehmen, um Produkte ins Ausland zu verkaufen, Vertretungen vor Ort, Übersetzungsbüros und eigene Gesellschaften vor Ort. Heute hilft die KI bei Übersetzung und Korrektur. Gemeinsame Zahlungssysteme funktionieren auf der ganzen Welt. Für die Auslieferung genügt ein Server, und in keinem Land braucht man Lagerbestand oder ein Lager. Ein Werkzeug, das von einer einzigen Person gemacht wurde, kann am Tag danach in 20 Sprachen in den Regalen der Welt stehen. Früher konnten das nur große Unternehmen.

Ein sehr kleines Unternehmen, das von Anfang an mit mehreren Ländern Geschäfte macht: Solche Unternehmen nennt man manchmal Micro-Multinationals (winzige multinationale Unternehmen). Bonta LLC strebt genau das an, mit einem Lokal in Higashi-Nakano und einer Person an der Spitze.

Natürlich bedeutet eine Übersetzung in 20 Sprachen nicht, dass Menschen im Ausland es sofort nutzen werden. Manche Übersetzungen warten noch darauf, von Personen mit der jeweiligen Muttersprache auf natürlichen Klang geprüft zu werden. Trotzdem verschwindet dadurch, dass die Sprachbarriere von Anfang an entfällt, die Obergrenze dafür, wie weit die Werkzeuge reichen können, so wie die Obergrenze bei den Plätzen.

Wie ich dieses Fundament aufbaue, ist das Thema von Kapitel 4.

【Abbildung 3-5】Sprachumschaltung im Hilfe-Center. 20 Sprachen sind aufgelistet *(Die Bildschirmanzeige ist auf Japanisch.)*

## Kapitel 4: Technik - Ein System, um allein fortlaufend Produkte zu bauen

Die wichtigsten Punkte dieses Kapitels

- Ich habe den Ablauf zum Start eines neuen Produkts in ein Dokument gebracht, und zwar in einer Form (einem Skill), die eine KI lesen und ausführen kann. Menschen übernehmen nur das Entscheiden und die Arbeiten, die nur Menschen leisten können
- Die gemeinsamen Teile wie Anmeldung, Abrechnung, Vorstellungsseiten und Hinweise auf andere Produkte werden einmal gebaut und in allen Produkten wiederverwendet. Die Datenbankkosten dieses Fundaments liegen bei etwa $35 im Monat
- Das System wächst noch. Ich ergänze das Ablaufdokument laufend um die Fehlschläge, etwa um ein Design, das fünfmal hintereinander abgelehnt wurde

(Dieses Kapitel enthält viele Fachbegriffe. Wenn Sie sich nicht für die Technik interessieren, können Sie zu Kapitel 5 springen, und die Geschichte hängt trotzdem zusammen.)

### 4-1 ProductBootstrap: Den Startablauf selbst der KI übergeben

Bei jedem Produkt, das ich baute, wiederholte ich dieselben Vorbereitungen und dieselben Fehler. Ein Repository anlegen (ein Lager für Programme). Die Anmeldung anbinden. Die Designfarben festlegen. Das Testsystem einrichten. Die Produktivumgebung vorbereiten. All das hatte ich für das vorige Produkt ganz sicher schon getan, aber ich hatte die Einzelheiten vergessen und stolperte an denselben Stellen.

Also brachte ich den Ablauf zum Start eines neuen Produkts in ein Dokument. Eine Form davon, die die KI, die Code schreibt (Claude Code), lesen und ausführen kann, nenne ich einen „Skill“. Der Name dieses Skills ist ProductBootstrap. „Bootstrap“ ist in der Computerwelt ein gängiger Begriff dafür, sich aus einem minimalen Mechanismus selbst hochzufahren, und ich habe ihn auf den Start von Produkten angewandt.

Ich halte kein Vorlagenprogramm vor. Ich kopiere das zuletzt fertiggestellte Produkt und starte das neue Produkt daraus. So werden die neuesten Lehren automatisch an das nächste Produkt weitergegeben. Auch eine alte Vorlage muss man dann nicht weiter pflegen.

#### Der Ablauf des Verfahrens

1. Das Anforderungsdokument übergeben. Bleiben die Pflichtfelder (Produktname, was es tut, wer es nutzt, Preis, Preiseinheit, Erkennungsfarbe, Ablageort des Master-Designs und so weiter) leer, beginnt die KI nicht. Die Regel lautet, dass sie der Lokalleitung unterwegs keine Fragen stellt. Ist nicht alles von Anfang an vorhanden, fängt sie gar nicht erst an
2. Die Farbe des Produkts festlegen. Jedes Produkt der Agenda-Reihe hat eine Erkennungsfarbe. Die KI misst die Farben der bestehenden Produkte, schlägt etwa vier Kandidaten vor, die sich nicht überschneiden, und die Lokalleitung wählt
3. Das Design festlegen. Ich lasse eine Design-KI (Claude Design) Vorschläge für die Bildschirme erstellen. Die KI prüft sich selbst in bis zu drei Runden, und nur Vorschläge, die die Prüfung bestehen, werden der Lokalleitung gezeigt
4. Die Umsetzung bis zum Ende der KI überlassen. Die KI baut und korrigiert eigenständig, bis die festgelegten Abnahmebedingungen erfüllt sind (Typprüfungen, Stilprüfungen, alle Tests grün, jede Bildschirmprüfung bestanden und Änderungen an der Datenbank, die in der Testumgebung sauber durchlaufen)
5. Die Lokalleitung genehmigt nur beim Gang in die Produktion. Alles bis zur Testumgebung läuft ohne Aufsicht, und die Lokalleitung entscheidet nur über den Vorgang in der Produktion

Ich habe die Umsetzungsphase so gebaut, dass sie mittendrin nicht anhält, um auf die Genehmigung der Lokalleitung zu warten. In der Anfangszeit lief es so, dass bei jeder Phase um Genehmigung gebeten wurde, aber so kam nichts voran. Wenn es mehrere Arbeitsfenster der KI gibt, bleibt jedes stehen und wartet auf Genehmigung, und die Lokalleitung muss zu jedem Fenster gehen und Urteile fällen. Also habe ich es geändert: Ich übergebe vorab den bereits genehmigten Rahmen und die Abnahmebedingungen, die eine Maschine beurteilen kann, und es hält nur bei einem Fehlschlag an.

Auch die Haltebedingungen sind festgelegt. Wenn das Ablaufdokument und die Entscheidung der Lokalleitung im Widerspruch stehen. Wenn eine Arbeit nötig wird, die nur Menschen leisten können. Wenn es bei demselben Fehler dreimal hintereinander nicht vorankommt. Wenn die Authentifizierung abläuft, Berechtigungen fehlen oder ein unumkehrbarer Vorgang nötig ist. Ansonsten arbeitet die KI eigenständig weiter. Der Stand der Arbeit wird in einer kleinen Datei festgehalten, sodass die Arbeit auch nach einem Absturz mittendrin von dort wieder aufgenommen werden kann.

#### Menschen tun nur zwei Dinge

Ich habe im Ablaufdokument festgehalten: Die KI führt jeden Schritt aus. Die Lokalleitung darf nur um die folgenden zwei Dinge gebeten werden.

- Das Urteil selbst. Genehmigen, entscheiden, wählen, welche von zwei Möglichkeiten gilt
- Arbeiten, die nur Menschen leisten können. Schlüssel, die sich nur über die Verwaltungsoberfläche eines externen Dienstes ausstellen lassen, Anträge mit Identitätsprüfung, Vorgänge am echten Gerät und die Beurteilung mit dem Auge

Wenn die KI irgendetwas anderes an die Lokalleitung weiterreicht, ist das ein Verstoß gegen das Ablaufdokument. In der Ablauftabelle habe ich jeder Zeile eine Spalte „Ausführende Stelle“ hinzugefügt, und jede Zeile, bei der der Eintrag für die Lokalleitung keinen Grund nennen kann, wird auf die Seite der KI umgestellt.

Für diese Regel hatte ich einen Grund. Als ich für ein Produkt die verbleibende Arbeit sortierte, reihte die KI „das Serverprojekt anlegen“, „das Ziel der Anmeldung eintragen“, „die Umgebungsvariablen eingeben“ und „die Testumgebung aufbauen“ alle als Aufgaben der Lokalleitung auf. Jede davon war ein Vorgang, den die KI selbst ausführen konnte. „Warum soll ich das machen?“ war damals meine ehrliche Reaktion. Die KI erledigt Dinge selbst, wenn man sie darum bittet. Bittet man nicht, reicht sie sie an einen Menschen weiter. Deshalb musste ich es ins Ablaufdokument schreiben.

Alle Fehlschläge des Reservierungssystems, die ich in Kapitel 2 beschrieben habe, habe ich in die Checkliste dieses Ablaufdokuments aufgenommen. Zuerst die Tests einbauen. Keine Produktivdaten in der Entwicklungsumgebung halten. Zuerst die Testumgebung bauen. Das nächste Produkt vermeidet denselben Schmerz von Anfang an.

#### Es wächst weiter

Dieses Ablaufdokument ist kein fertiges Produkt. Ich ergänze es jedes Mal, wenn etwas schiefgeht.

Zum Beispiel ließ ich die Design-KI einmal den Bildschirm eines Produkts fünfmal hintereinander erstellen, und alle fünf wurden abgelehnt. Das schließt die Runden ein, in denen ich ihr die Designregeln der ganzen Reihe (DESIGN.md) übergeben hatte.

Zuerst diagnostizierte die KI als Ursache „das Farbschema selbst“. Dem widersprach ich. Die tatsächlichen Ursachen waren zwei. Die eine: Farben, die in den Regeln nicht definiert waren, wurden frei verwendet. Die andere: Drei Abschnitte mit unterschiedlichen Rollen waren mit derselben Hintergrundfarbe und denselben Abständen senkrecht gestapelt, ohne Grenze dazwischen. Keine Regel war verletzt worden, und doch waren die Rollen aus dem Aussehen verschwunden.

Also fügte ich den Designregeln Klauseln hinzu. Dinge mit unterschiedlichen Rollen nicht gleich aussehen lassen. Sie nicht allein durch Farbe trennen. Das Wichtigste kommt zuerst in der Blicklinie. Nur wirklich gleichrangige Dinge dürfen mit gleichem Gewicht nebeneinanderstehen. Kein Layout bauen, das nur Dinge übereinanderstapelt.

Eine weitere Lehre aus dem Scheitern gab es noch. Wenn man den „zu vermeidenden Standardlook“ nur als Liste von Verboten vermittelt, schlägt die KI ganz zu einem anderen Standard aus, der nicht auf der Liste steht. Als ich Karten, Schatten und runde Ecken auf einmal verbot, kam ein zeitungsartiger Bildschirm zurück, der nur aus Linien und Abständen bestand. Seitdem lasse ich die Anfrageunterlagen in drei Spalten schreiben: „das zu vermeidende Muster“, „was ich verbieten wollte“ und „was stattdessen zu tun ist“.

Auch die Art, die Erkennungsfarben festzulegen, habe ich mittendrin geändert. Etwa als die Zahl der Produkte acht überstieg, war der Bereich der dunklen Farben von bestehenden Produkten belegt, und das neunte und alle weiteren Produkte konnten keine dunkle Farbe für Linien und Schaltflächen mehr bekommen, ohne mit den bestehenden zu kollidieren. Also habe ich die Regel überarbeitet: Die Erkennungsfarbe eines Produkts wird nur für helle Flächenfarben verwendet, und Linien, Trennstriche, Symbole und Hauptschaltflächen werden alle auf das gemeinsame Tusche-Schwarz der Reihe vereinheitlicht. Das war eine Einschränkung, die erst klar wurde, als die Produkte sich vermehrten.

Jedes Mal, wenn etwas schiefgeht, korrigiere ich das Ablaufdokument. Das nächste Produkt wird um genau so viel leichter. Ich glaube, das Ablaufdokument wachsen zu lassen ist die beste Investition, um allein weiter Produkte zu bauen.

【Abbildung 4-2】Die Phasen des Startablaufs und wer sie ausführt (die KI oder die Lokalleitung) *(Die Bildschirmanzeige ist auf Japanisch.)*

【Abbildung 4-3】Die Erkennungsfarben der Agenda-Reihe. Eine Farbe pro Produkt, nur auf Flächen verwendet *(Die Bildschirmanzeige ist auf Japanisch.)*

### 4-2 AgendaHub: Die Eingangstür

Wenn die Produkte mehr werden, baut man immer wieder dieselben Dinge. Anmeldung, Abrechnung, Vorstellungsseiten, Hinweise auf andere Produkte. Um das allein zu betreiben, muss man die gemeinsamen Teile einmal bauen und in allen Produkten wiederverwenden.

AgendaHub ist der Ort, an dem diese gemeinsamen Teile gesammelt sind. Ich nenne ihn die „Eingangstür“.

Zuerst ist er der Eingang, der von einer Adresse zu allen Produkten leitet. Unter einer einzigen Domain, bontallc.com, stehen die Eingänge der einzelnen Produkte nebeneinander: /agendatimbro, /agendaoro, /agendaluce. Für Nutzende sieht es so aus, als lägen die Produkte auf einer einzigen Website, aber tatsächlich läuft dahinter jeweils ein eigenes Programm.

Als Nächstes ist er der Ort, an dem die Vorstellungsseiten der Produkte liegen. Es gibt eine Vorstellungsseite für die Reihe, und darin einen Abschnitt für jedes Produkt. Jeder Abschnitt enthält den Produktnamen und seinen Spitznamen, den Preis, ein Problem in den eigenen Worten der Lokalleitung, beginnend mit „Wenn Sie …“, eine Beschreibung dessen, was es kann, und einen Link zur Detailseite. Wenn ich ein neues Produkt veröffentliche, gehört das Hinzufügen dieses Abschnitts zum Startablauf.

Und er ist die Heimat der Designregeln und der Startabläufe. Das Master der Erkennungsfarben, die Bildschirmregeln (DESIGN.md), der Skill ProductBootstrap, den ich in 4-1 beschrieben habe, der Skill, der Bildschirme prüft, und der Skill, der Änderungen an der Datenbank sicher durchführt. Bei allen Regeln, die die ganze Reihe betreffen, liegt der eigentliche Inhalt hier, und jedes Produkt liest ihn per Verweis.

【Abbildung 4-1】Der Aufbau der Agenda-Reihe. Von der Eingangstür (AgendaHub) zu jedem Notizbuch, und jedes Notizbuch ist mit einem einzigen Konto (AgendaID) verbunden *(Die Bildschirmanzeige ist auf Japanisch.)*

### 4-3 AgendaID: Gemeinsame Konten und Abrechnung

AgendaID ist das gemeinsame System der Reihe für Konten und Abrechnung.

Wer sich einmal mit einem Google-Konto anmeldet, kann jedes Produkt nutzen. Man muss nicht für jedes Produkt ein Konto anlegen. Ich plane außerdem, die Spracheinstellung später über Produkte hinweg zu übernehmen.

Auch die Abrechnung ist ein einziges System. Statt für jedes Produkt die Anbindung an den Zahlungsdienst (Stripe) zu bauen, übernimmt AgendaID alles. Es gibt vier Preiskategorien: ein leichtes Produkt für ¥300 (ca. $2) im Monat, ein Produkt nach Verbrauch, ein Produkt zum einmaligen Kauf für ¥600 (ca. $4) und ein kostenloses Produkt. Kostenpflichtige Produkte haben einen kostenlosen Zeitraum von drei Monaten ohne Hinterlegung einer Kreditkarte, der einmal pro Kombination aus Lokal und Produkt nutzbar ist. Außerdem gibt es einen Mechanismus, der der werbenden und der geworbenen Seite jeweils drei Monate kostenlosen Zeitraum hinzufügt.

Vor Ende des kostenlosen Zeitraums kommen Benachrichtigungs-E-Mails sieben Tage und einen Tag vorher. Diese E-Mails hatte ich zuerst auch innerhalb der Zeiterfassung gebaut, aber als die Produkte mehr wurden, merkte ich, dass es Verschwendung ist, jedem Produkt denselben Mechanismus zu geben, und habe sie auf der Seite von AgendaID zusammengeführt.

#### Kündigung und Löschung ebenfalls nach gemeinsamen Regeln

Es gibt einen unscheinbaren, aber wichtigen Teil: Kündigung und Datenlöschung.

Wenn jemand kündigt, welche Daten werden dann wann gelöscht? Baut man das für jedes Produkt einzeln, wird irgendwo ganz sicher etwas übersehen. Hinzu kommt, dass die Agenda-Reihe Produkte enthält, die besonders sensible Daten verarbeiten, etwa das Produkt, das Stammkundschaft per Gesichtserkennung identifiziert.

Also habe ich die Granularität der Löschung in vier Stufen aufgeteilt und zu einer Regel gemacht, die für die ganze Reihe gilt. Das sind die Kündigung eines Produkts, die Löschung eines Lokals, der Austritt aus einem Konto (das Verlassen der ganzen Reihe) und der Löschantrag einer einzelnen Person aus dem Team. Die oberen Stufen greifen kaskadierend auf die unteren durch, und jedes Produkt meldet sein eigenes Löschverfahren beim gemeinsamen System an. Die Karenzzeit für die Löschung beträgt 30 Tage, und in dieser Zeit lässt sie sich rückgängig machen.

Dazu kommt eine Zeitachse. Anwesenheitsaufzeichnungen zum Beispiel müssen gesetzlich fünf Jahre aufbewahrt werden. Selbst wenn ein ehemaliges Teammitglied die Löschung verlangt, muss die Aufzeichnung innerhalb der Aufbewahrungsfrist erhalten bleiben, mit anonymisierten Namen und dergleichen, statt physisch gelöscht zu werden. Die Grenze zwischen „löschen“ und „aufbewahren“ musste ich anhand des Gesetzes prüfen und festlegen.

#### Ein Test-Login, damit die KI die Produktion nicht verunreinigt

Für die KI habe ich AgendaID noch einen Mechanismus hinzugefügt: einen Zugang für Test-Logins.

Damit die KI prüfen kann, ob etwas funktioniert, muss sie sich anmelden und die Bildschirme bedienen. Die Anmeldung läuft aber über ein Google-Konto, sodass sich die KI nicht allein anmelden kann. Und das Konto der Lokalleitung kann ich der KI auch nicht übergeben. Es besteht die Gefahr, dass die Tests der KI Produktivdaten verunreinigen.

Also habe ich einen Zugang gebaut, über den synthetische Konten (Personas) ausgegeben werden, die nur in der Testumgebung nutzbar sind. In der Produktion funktioniert er nicht. Die Datenbank der Testumgebung ist ein eigenes Projekt, getrennt von der Produktion, und enthält nur synthetische Daten. Die KI meldet sich über diesen Zugang an, bedient die Bildschirme und prüft, ob alles funktioniert. Die Testkonten werden jeden Tag neu aufgebaut, und alte werden gelöscht.

Damit kann die KI sogar die Abschlussprüfung eigenständig durchführen, in einer Umgebung, die genau wie die Produktion aufgebaut ist, ohne die Produktion zu berühren.

### 4-4 Die gemeinsame Navigation und das Scheitern des Wortes „Eingangstür“

Damit Nutzende von jedem Produkt zu den anderen gelangen, habe ich jedem Produkt ein gemeinsames Navigationsmenü gegeben. Es ist der Weg, über den jemand, der die Zeiterfassung in einer Bar nutzt, im Hilfe-Center eine Frage stellen oder sich die anderen Notizbücher ansehen kann.

Hinter dieser gemeinsamen Navigation steckt eine kleine Geschichte des Scheiterns.

In der ersten Version hatte ich einen Link mit dem Text „Zurück zur Eingangstür“ gesetzt. Das lag daran, dass ich AgendaHub intern die „Eingangstür“ nannte. Als ich es aber auf einem echten Gerät prüfte, stimmte etwas nicht. Zwei Links, „Zurück zur Eingangstür“ und „Agenda-Reihe ansehen“, führten an dieselbe Stelle. Dazu stand der Link zur Hilfe über dem Menü für die tägliche Arbeit, die Reihenfolge der Wichtigkeit war also verkehrt. Und vor allem sagt das Wort „Eingangstür“ jemandem, der das Produkt zum ersten Mal nutzt, gar nichts. Es war die interne Sprache der Person, die es gebaut hat.

Also habe ich die Grundsätze neu gesetzt. Die Einträge nach ihrer Nähe zum Zweck der Nutzenden ordnen: die tägliche Arbeit ganz oben, Links, die nach außen führen, ganz unten. Selbst ein Link, der neue Nutzende gewinnen soll, steht nie über der Arbeit. Die Grenze muss sich mit einer einzigen Linie erklären lassen. Die Formulierungen in der Sprache der Nutzenden schreiben, nicht in interner Sprache. Nie mehr als einen Link setzen, der an dieselbe Stelle führt. Ich habe „Zurück zur Eingangstür“ gestrichen und alles zu einem einzigen Link zusammengeführt: „Weitere Agenda-Notizbücher ansehen“.

In Kapitel 2 habe ich darüber geschrieben, die Sprache der UI zu lernen. Das war die Sprache, die die Lokalleitung im Gespräch mit der KI benutzt. Hier ist es das Gegenteil: die Sprache, mit der ich zu den Nutzenden spreche. In beiden Fällen ging es darum, die eigenen Worte auf das Gegenüber abzustimmen.

【Abbildung 4-4】Die gemeinsame Navigation nach der Korrektur. Die Arbeit steht oben, und die Links nach außen ganz unten *(Die Bildschirmanzeige ist auf Japanisch.)*

### 4-5 Das Fundament kostet $35 im Monat

Die Datenbankkosten des gesamten in diesem Kapitel beschriebenen Fundaments liegen bei etwa $35 im Monat. Der kostenpflichtige Tarif, der das Produktivprojekt enthält, kostet $25, und das Projekt für die Testumgebung $10.

Auch das war nicht von Anfang an der Betrag. Zeitweise zahlte ich $45 im Monat. Die Entwicklungsdatenbank für ein Produkt mit Gesichtserkennung wurde noch abgerechnet, obwohl ich sie gar nicht nutzte. Ich habe sie auf den kostenlosen Tarif umgestellt und angehalten, ein weiteres Projekt, das ich nicht nutzte, gelöscht, und so kam es auf den heutigen Betrag.

Auch die Kosten der KI behalte ich im Blick. Die Arbeit der KI, die Programme schreibt, wird nach der Menge der Tokens abgerechnet (die Einheit für Text, den die KI liest und schreibt). Ich vermeide es, dass sich die Kosten an einer Stelle ballen, indem das Arbeitsfenster bei der Rolle der Koordination bleibt und die Umsetzung selbst einer anderen KI mit einem getrennten Kostenrahmen überlassen wird. Auch beim generativen Modell im Chatfenster schaue ich auf den Preis und wähle das, was nötig und ausreichend ist. Selbst wenn ein Modell der höheren Stufe nur $1 im Monat mehr kostet, wähle ich mit der Frage „Reicht es?“.

Wenn man klein baut, reichen auch kleine Umsätze aus. Die Geschichte vom Geldverdienen in Kapitel 3 wird davon getragen, wie klein die Kosten dieses Fundaments sind.

### 4-6 Die koordinierende KI und die Person, die entscheidet

Zum Schluss möchte ich beschreiben, wie mein Arbeitstag aussieht.

Ich habe mehrere Arbeitsfenster der KI gleichzeitig geöffnet. Es gibt ein Fenster für das Reservierungssystem, ein Fenster für jedes Produkt und ein Koordinationsfenster, das ihnen Anweisungen schickt und die Ergebnisse einsammelt. Das Koordinationsfenster habe ich AgendaRegia genannt (das koordinierende Notizbuch).

Diejenigen, die entscheiden, also festlegen, „in welche Richtung es geht“, sind ich und die Chat-KI. Die Chat-KI findet vorab Lücken und Widersprüche in den Spezifikationen, versieht jede mit einer Standardentscheidung und schlägt alles auf einmal vor. Ich lese und entscheide. Was entschieden ist, wird in einem Anweisungsblatt namens Goal gesammelt und in das Arbeitsfenster eingefügt. Es enthält vorab erteilte Genehmigungen und Bestehensbedingungen, die eine Maschine beurteilen kann. Das Arbeitsfenster liest es und macht bis zum Ende weiter, und es hält nur an, wenn etwas fehlschlägt.

Ich lasse das Anweisungsblatt auch eine Schätzung enthalten, wann die Arbeit fertig sein wird. Ich schiebe diese Arbeit zwischen die Öffnungszeiten der Bar, und wenn ich nicht weiß, wie lange etwas dauert, kann ich meinen Tag nicht planen.

Die Rolle der Lokalleitung ist nicht das Lesen, sondern das Entscheiden. Ich muss nicht alle 1.775 Gesprächsprotokolle lesen. Ich beantworte Fragen zu Tatsachen der Bar. Ich entscheide über Dinge, die nur die Linie der Bar entscheiden kann. Nachdem etwas live gegangen ist, probiere ich es fünf- oder sechsmal selbst aus und prüfe, ob sich etwas falsch anfühlt. Das ist alles.

Bevor ich bei dieser Form ankam, habe ich Arbeit viele Male neu gemacht. Die KI fügte von sich aus Funktionen hinzu, und die Bildschirme wurden instabil. Die Arbeit wuchs aus einer einzigen Anweisung grenzenlos. Wenn bei jeder Phase auf eine Genehmigung gewartet wurde, kam nichts voran. Jedes Mal habe ich eine Regel ergänzt, und so kam es zur heutigen Form. Auch das wächst noch.

#### Was Sie aus diesem Kapitel mitnehmen können

- Bringen Sie bei wiederkehrender Arbeit den Ablauf selbst in ein Dokument und übergeben Sie ihn der KI. Wenn Sie das Ablaufdokument jedes Mal korrigieren, wenn etwas schiefgeht, wird es beim nächsten Mal leichter
- Bauen Sie die gemeinsamen Teile (Anmeldung, Abrechnung, Navigation) nur einmal und verwenden Sie sie in allen Produkten wieder. Ist das Fundament klein, reichen auch kleine Umsätze aus
- Menschen übernehmen nur das Entscheiden und die Arbeiten, die nur Menschen leisten können. Reicht die KI Ihnen irgendetwas anderes weiter, ergänzen Sie es im Ablaufdokument

Die Fortsetzung dieses Kapitels (die nächsten Notizbücher, die ich baue, und die Lehren, die ich dem Ablaufdokument hinzugefügt habe) finden Sie auf note und X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Kapitel 5: Die Zukunft einer kleinen Bar

### 5-1 Von Zatta Gohan zu Tamuro

In die Gastronomie bin ich mit 39 Jahren eingestiegen.

Der Auslöser war eine Bar in der Nachbarschaft namens Zatta. Einmal im Monat, manchmal alle zwei Wochen, durfte ich dort mein Essen servieren. Ich hatte mir das Kochen lange selbst beigebracht, doch nun hatte ich einen Ort, an dem Menschen mein Essen aßen und sich freuten. Das war meine prägende Erfahrung.

2014 eröffnete ich in Arai-Yakushi ein Restaurant namens Zatta Gohan. Es war ein kleines Lokal, das Menüs mit Reis und Beilagen servierte. Ich führte es sieben Jahre lang.

In Arai-Yakushi spürte ich allerdings eine Grenze bei der Zahl der Gäste. Dann fand ich eine Immobilie in Higashi-Nakano. Vom Ostausgang des Bahnhofs ist es weniger als eine Minute zu Fuß. Selbst an einem Regentag kommt man hin, fast ohne nass zu werden.

Im November 2018 eröffnete ich dort Tamuro. „Tamuro“ bedeutet einen Ort, an dem Menschen zusammenkommen. Es hat 11 Thekenplätze und 8 Tatami-Plätze, zusammen 19. Drei Jahre lang führte ich zwei Lokale parallel, Arai-Yakushi und Higashi-Nakano. In der Zeit von COVID wurde es schwierig, beide zu halten, also schloss ich das Lokal in Arai-Yakushi, und übrig blieb nur Tamuro.

#### Die Curation Bar

Tamuro nennt sich selbst eine „Curation Bar“.

Kuratieren bedeutet, ein geschultes Auge zu haben. Bevor ich Koch bin, möchte ich Kurator sein. Das Essen, die Getränke, die Atmosphäre der Bar: Alles entsteht, indem ich mit geschultem Auge auswähle. Das ist Tamuro.

Ich reise oft zum Essen, im Ausland wie in Japan. Vietnam, Kambodscha, Italien, Shanghai, Peking, Mexiko. Sich durch die Orte zu essen ist ein Vergnügen und zugleich eine Art, zu finden, was es bei Tamuro geben soll. Teure Zutaten bilde ich mit erschwinglichen, alltäglichen Zutaten nach. Wenn man zum Beispiel Eigelb trocknet und hobelt, erhält man einen Geschmack, der Bottarga nahekommt. Diese Art von Ersatz (Lokalisierung) sehe ich als meine Rolle.

In der Zeit von COVID habe ich das Kochen noch einmal gelernt. Ich besuchte einen französischen Kochkurs mit insgesamt acht Terminen, und auch einen Kurs für japanische Küche. Der Umgang mit Umami und die Kunst, beim Garen die richtige Hitze zu führen. Was ich dort gelernt habe, ist das Fundament meiner heutigen Küche.

Die Karte von Tamuro besteht aus vier Vorspeisen und einem Hauptgericht. Ich gebe ihr eine Bandbreite an Zutaten, damit Gäste, die allein leben, reichlich Gemüse bekommen. Ich stelle sie so zusammen, dass sich Garmethoden (frittiert, eingelegt in Essig, geschmort, gegrillt) und Geschmacksrichtungen (süß, scharf, sauer) nicht überschneiden. Das beliebteste Gericht ist Tonteki, ein Schweinesteak. Es hat eine leicht süße Sauce mit Sojasauce aus Kyushu und reichlich Knoblauch.

#### Ein Ort, an dem Menschen zusammenkommen

Etwa die Hälfte der Gäste von Tamuro kommt allein. Sie sind hauptsächlich zwischen 30 und 50, und viele wohnen in der Nachbarschaft von Higashi-Nakano, aber es kommen auch Menschen aus der Gegend von Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo und Eifukucho. 

Das Besondere der Bar ist, wie viel die Gäste miteinander reden. Ich habe die Theke so gebaut, dass man leicht mit der Person nebenan ins Gespräch kommt, und ich oder das Team entscheiden die Sitzordnung danach, wer sich gut verstehen wird. Gäste, die allein gekommen sind, kommen manchmal später zusammen wieder. Wie der Name sagt, ist es ein Ort geworden, an dem Menschen zusammenkommen. Wie der Alltag der Bar aussieht, zeige ich auf [Instagram](https://www.instagram.com/tamuro.higashinakano/).

Beim Menü-Abend, der etwa einmal im Monat stattfindet, serviere ich über zwei bis drei Stunden sieben bis acht Gerichte, zusammen mit passenden Weinen. Jeden Monat wechselt das Thema: italienisch, französisch, japanisch. Die Kochkurse sind dreistündige Workshops, und nach dem Kochen stoßen alle an, essen und gehen nach Hause. Es gibt den Aperitivo, bei dem am frühen Abend vor der Öffnung Wein und kleine Gerichte serviert werden. Etwa zweimal im Jahr gibt es ein Barbecue. Einmal im Jahr gibt es eine Jahresabschlussfeier. Und es gibt das Yukata-Fest, über das ich in Kapitel 1 geschrieben habe.

Das Reservierungssystem, über das ich in Kapitel 1 geschrieben habe, das Chatfenster und MCP sind alles Werkzeuge, um Menschen in diese Bar zu bringen. Die KI ist ein Mittel, Menschen zusammenzubringen, nicht das Ziel.

### 5-2 Das Hacksteak-Curry von Quatre Épices

Tamuro ist eine Bar für den Abend. Tagsüber steht der Raum leer.

Um diese Zeit zu nutzen, habe ich im Januar 2024 Quatre Épices gestartet. Es ist ein Lokal für Hacksteak-Curry (japanisch „Hambāgu“), das nur mittags am selben Ort betrieben wird, und das Team führt es.

Quatre Épices bedeutet auf Französisch „vier Gewürze“. Dem Namen getreu schichten wir nicht viele Gewürze übereinander, sondern wählen aus und beschränken uns, damit die Kontur des Geschmacks klar wird. Das Curry kommt ohne Mehl aus; es wird allein mit der natürlichen Sämigkeit von Gemüse und Fleisch gebunden. Zufriedenheit, wenn man aufgegessen hat, und kein Gefühl der Schwere im Magen. Und Harmonie mit dem Hacksteak. Auf diesen drei Voraussetzungen habe ich es entworfen.

Wir legen Wert darauf, wie das Hacksteak gegart wird. Wir stellen die Mischung so ein, dass es außen knusprig und innen locker wird, und garen passend zu dieser Mischung. Das Gespür für die richtige Hitze, das ich nachts bei Tamuro gelernt habe, kommt auch dem Mittagsgericht zugute.

Preise, Öffnungstage und Zeiten können sich ändern, bitte informieren Sie sich daher auf Tamuros Instagram (https://www.instagram.com/tamuro.higashinakano/) über den aktuellen Stand.

Quatre Épices betreibt am selben Ort auch eine Kinderkantine. Es ist eine Aktivität, die die vorhandenen Einrichtungen und den Einkauf der Bar nutzt, um Kindern aus der Nachbarschaft Mahlzeiten zu servieren. Darüber haben wir auch eine Beziehung zum örtlichen Gemeindezentrum aufgebaut. Manchmal servieren wir Curry und Sandwiches bei Sportveranstaltungen im Viertel, bei Veranstaltungen des Gemeindezentrums und bei Bon-Odori-Tanzfesten.

Ehrlich gesagt ist die Nutzung der Tageszeit nicht in allem gut gelaufen. Ich habe Tage für entspanntes Trinken am Nachmittag eingerichtet und den Raum an andere vermietet, aber die Gäste kamen nicht so, wie ich gehofft hatte. Der Reiz der Bar kommt anders an, wenn nachts die Lokalleitung da ist und wenn nur das Tagesteam da ist. Das Lokal am Tag mit einem Reiz wachsen zu lassen, der sich vom Lokal in der Nacht unterscheidet, ist noch eine unerledigte Aufgabe.

### 5-3 Bonta LLC: Zwei Säulen

Das kleine Unternehmen, das Tamuro und Quatre Épices betreibt, ist Bonta LLC. Dort bin ich als vertretungsberechtigtes Mitglied der Gesellschaft geschäftsführend tätig.

Das Unternehmen hat zwei Säulen. Die eine ist Gastronomie: Tamuro und Quatre Épices. Die andere ist IT: die Entwicklung der Agenda-Reihe und Beratung.

Gastronomie und Werkzeuge verdienen auf unterschiedliche Weise Geld. Das Unternehmen auf zwei Säulen unterschiedlicher Natur zu stellen, ist die Form, die mir vorschwebt.

Und die beiden Säulen versorgen einander mit Material. Probleme im Barbetrieb werden zum Samen eines Werkzeugs. Was ich beim Bauen von Werkzeugen lerne, fließt zurück in den Betrieb der Bar. Das Licht-Notizbuch entstand aus dem späten Schließen, und die Aufzeichnungen über verlängerte Öffnungszeiten aus dem Licht-Notizbuch werden zur Grundlage für Rentabilitätsschätzungen und Schichtpläne. Die „Fragen, die wir nicht beantworten konnten“, die sich im Chatfenster ansammeln, verbessern die Auskünfte der Bar. Dieser Kreislauf ist der Grund, warum ich Bar und Entwicklung allein bewältigen kann.

Ich denke nicht daran, das Unternehmen größer zu machen. Klein, zahlreich, günstig. Das ist die Form dieses Unternehmens.

### 5-4 Schreiben als Raku Bonta

Wenn ich schreibe und veröffentliche, verwende ich das Pseudonym „Raku Bonta“. Auch dieses Buch habe ich unter diesem Namen geschrieben.

Mein voriges Buch, *Die KI-Stellvertretung*, war ein Buch über generative KI. Es erreichte in der Kategorie Zeitmanagement bei Amazon Platz eins und wurde von vielen Menschen gelesen. Dieses Buch ist seine Fortsetzung.

Neben Büchern schreibe ich auch auf note. Ich schreibe über die Bemühungen der Bar mit KI, über das, was ich auf einer Lernreise entdeckt habe, über den Fortschritt bei der Veröffentlichung meiner Bücher und über die Agenda-Reihe. Die Fortsetzung, die ich in diesem Buch nicht unterbringen konnte, können Sie auf note verfolgen (https://note.com/bontallc).

Für mich ist das Schreiben auch eine Möglichkeit, Bar und Entwicklung in Worte zu fassen und zu überprüfen. Wie ich in Kapitel 1 geschrieben habe, wurde das erste Wissen des Chatfensters „T-AI-MURO“ aus Worten aufgebaut, die ich auf X hinterlassen hatte. Was ich aufgeschrieben hatte, wurde zum Material für die KI. Auch künftig wird das, was ich schreibe, sowohl in die Bar als auch in die KI zurückfließen.

Über das Schreiben habe ich noch etwas entschieden. Ich kündige Unfertiges nicht mit „in Kürze“ an. Ich stelle es fertig, erstelle eine Vorstellungsseite und bringe es erst dann heraus. Ich glaube, an dieser Reihenfolge festzuhalten ist es, was ein kleines Unternehmen Vertrauen verdienen lässt.

### 5-5 Die Zukunft des eigenständigen Lokals

Zum Schluss fasse ich das, was ich in diesem Buch geschrieben habe, zu einem einzigen Bild zusammen.

【Abbildung 5-1】Das große Bild dessen, was dieses Buch beschrieben hat. Eine kleine Bar öffnet ihr eigenes Fenster (die erste Geschichte) und macht ihre Probleme zu Werkzeugen, die sie an andere Bars weitergibt (die zweite Geschichte) *(Die Bildschirmanzeige ist auf Japanisch.)*

Die Gäste werden bald ihre eigene KI eine Bar finden und die Reservierung vornehmen lassen. Im August 2026 wurde es möglich, über einen großen Reservierungsdienst Restaurants von ChatGPT aus zu buchen. Der Einstiegspunkt verlagert sich von Suchmaschinen und Restaurantportalen zur eigenen KI jedes Menschen.

An diesem Punkt ist eine Bar, die nicht beim großen Reservierungsdienst gelistet ist, für die KI unsichtbar. Aber auch wenn man nicht beim großen Dienst ist, gibt es für eine Bar einen Weg, sich direkt mit der KI zu verbinden. Tamuro hat diesen Weg gewählt, indem es ein Fenster namens MCP geöffnet hat. Eine kleine Bar, die von sich aus ihr eigenes Fenster öffnet. Das ist die erste Geschichte dieses Buchs.

Wer eine Bar führt, wird die eigenen Probleme zu Werkzeugen machen und sie an andere Bars weitergeben können. Das Licht-Notizbuch entstand aus Tamuros Problem, den Menschen sagen zu wollen, dass die Schließzeit nach hinten rückt, und es lässt sich in jeder Bar nutzen. Die Fähigkeit, selbst Software zu bauen, ist nicht mehr das Vorrecht bestimmter Menschen oder Unternehmen. Wer eine kleine Bar führt, wechselt von der Seite, die Werkzeuge nutzt, auf die Seite, die sie baut und verteilt. Das ist die zweite Geschichte dieses Buchs.

Beiden ist gemeinsam: Je kleiner die Bar, desto profilierter kann sie sein.

Große Ketten verallgemeinern ihre Systeme, damit jede Filiale dieselbe Qualität liefert. Tamuro ist das Gegenteil. Gäste, die allein kommen, machen die Hälfte aus, fast 90% der Reservierungen erfolgen am selben Tag, und die Gäste reden miteinander. Passend zu diesem Charakter von Tamuro habe ich das Reservierungssystem, die Rabatte und das Chatfenster bis ins Detail gebaut. Weil es nicht verallgemeinert, hat es ein klares Profil. Weil es ein klares Profil hat, wird es zu einem Grund für die Gäste, sich dafür zu entscheiden.

Und je profilierter die Bar, desto mehr Samen für Werkzeuge findet sie. Je mehr man sich dem Charakter der Bar zuwendet, desto konkreter werden die Probleme. Konkrete Probleme werden zu konkreten Werkzeugen. Konkrete Werkzeuge helfen anderen Bars mit demselben Problem.

Die KI hat es möglich gemacht, dass eine einzelne Person beides tut. Der Bar ein klares Profil geben und Werkzeuge weitergeben. Früher musste man sich für eines von beiden entscheiden. Jetzt kann man beides.

Natürlich ist es noch ein Werk im Entstehen. Die Erfolgsquote des Chatfensters wird noch gesteigert. Das Ablaufdokument wächst mit jedem Fehlschlag. Wie das Lokal am Tag wachsen kann, bleibt eine Aufgabe. Menschen, die über die KI buchen, sind noch nicht viele.

Trotzdem bin ich zuversichtlich, dass die Zukunft der kleinen Bar gut aussieht. Klein zu sein ist keine Schwäche. Weil wir klein sind, können wir schnell testen, schnell verwerfen und schnell korrigieren. Weil wir klein sind, können wir Ecken und Kanten zeigen. Und die Probleme einer profilierten Bar werden zu Werkzeugen und gehen an andere kleine Bars weiter.

Ich habe dieses Buch in einer Bar mit 19 Plätzen in Higashi-Nakano geschrieben.

## Nachwort

Danke, dass Sie bis hierher gelesen haben.

Was ich in diesem Buch geschrieben habe, ist eine Aufzeichnung mit dem Stand Oktober 2026. KI-Werkzeuge ändern ihre Gestalt binnen weniger Monate. Manche der Mechanismen, die ich beschrieben habe, haben bis zur Veröffentlichung vielleicht schon eine andere Form angenommen. Dennoch habe ich es aufgeschrieben, in dem Glauben, dass eine Aufzeichnung darüber, was und wie eine kleine Bar mit KI gebaut hat, wo sie gescheitert ist und was sie gelernt hat, noch eine Weile nützlich bleiben sollte.

Die Agenda-Reihe: https://bontallc.com/agenda?via=b2-de-{{FMT}}

Auf dem Laufenden bleiben: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Wenn Sie einmal in Higashi-Nakano sind, schauen Sie bei Tamuro vorbei. Sie können über die Reservierungsseite reservieren, über das Chatfenster „T-AI-MURO“ auf der Seite und natürlich über Ihre eigene KI.

Reservierungsseite von Tamuro: https://tamuroreservation.vercel.app/?src=b2-de-{{FMT}}

Instagram von Tamuro: https://www.instagram.com/tamuro.higashinakano/

Für alle, die ausprobieren möchten, per KI zu buchen: Die Verbindungsadresse des MCP-Servers von Tamuro ist die folgende URL.

https://tamuroreservation.vercel.app/api/mcp

Öffnen Sie in den Einstellungen Ihrer KI (etwa Claude oder ChatGPT) den Bildschirm zum Hinzufügen externer Werkzeuge (Connectors, MCP-Server) und tragen Sie diese URL ein. Wie die Einrichtung abläuft, unterscheidet sich je nach KI und ändert sich mit der Zeit, am sichersten ist es daher, in der Hilfe der jeweiligen KI nach „MCP“ oder „Connector“ zu suchen. Je nach Tarif können Sie womöglich keinen MCP-Server Ihrer Wahl anbinden. Nach der Einrichtung fragen Sie Ihre KI: „Ist bei Tamuro heute Abend noch Platz?“ Sie prüft die freien Plätze und die Preise und führt Sie zur Reservierungsseite. Den Bestätigungsknopf drücken Sie selbst.

Für alle, die nach der Lektüre des Buchs zu uns kommen: Geben Sie bei der Reservierung bitte den Gutscheincode „BOOK“ ein. Zur ersten Runde serviere ich Ihnen ein Getränk aufs Haus. Wenn Sie ohne Reservierung kommen, sagen Sie bei Ihrer ersten Bestellung einfach: „Ich komme wegen des Buchs.“ Dann erhalten Sie ebenfalls ein Getränk aufs Haus. Es ist ein kleiner Kniff, mit dem ich zählen kann, wie viele Menschen wegen des Buchs gekommen sind.

Sie können auch ohne Reservierung hereinkommen. Auch allein fallen Sie nicht auf. Vielleicht kommen Sie sogar mit der Person neben Ihnen ins angeregte Gespräch.

Ich freue mich auf Sie an einem Ort, an dem Menschen zusammenkommen.

Raku Bonta

### Quellen

- OpenAI Help Center, „ChatGPT — Release Notes“, 10. August 2026, „Restaurant reservations in ChatGPT“ https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, „Alpaca MCP Server“ (ein Beispiel für einen MCP-Server in den USA, über den die KI Aufträge für Aktien und andere Wertpapiere erteilen kann) https://docs.alpaca.markets/docs/alpaca-mcp-server
- Die Debatte um den „Tod von SaaS“: Satya Nadellas Äußerungen im BG2-Podcast (Dezember 2024), der starke Einbruch der Softwareaktien im Februar 2026 und wie er genannt wurde, sowie Jensen Huangs Widerspruch wurden aus den folgenden Berichten und Kommentaren entnommen. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
