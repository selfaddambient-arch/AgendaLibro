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

