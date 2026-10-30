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

