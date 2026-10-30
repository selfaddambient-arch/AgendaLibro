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

