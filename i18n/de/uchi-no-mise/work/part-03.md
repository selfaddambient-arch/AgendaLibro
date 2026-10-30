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

