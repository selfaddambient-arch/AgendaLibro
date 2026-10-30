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
