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
