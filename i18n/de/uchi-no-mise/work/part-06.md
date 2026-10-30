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
