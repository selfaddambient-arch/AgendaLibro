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
3. Wenn Sie einmal in Tokio sind, besuchen Sie Tamuro. Eine Minute vom Osteingang des Bahnhofs Higashi-Nakano. Sie können ohne Reservierung hereinkommen. Reservierungsseite https://tamuroreservation.vercel.app/?src=b1-de-{{FMT}}

An alle, die wegen dieses Buchs zu uns kommen: Geben Sie bei der Reservierung bitte den Gutscheincode „BOOK“ ein. Beim ersten Besuch spendieren wir Ihnen ein Getränk. Wenn Sie ohne Reservierung gekommen sind, sagen Sie bei der ersten Bestellung einfach „Ich komme wegen des Buchs“. Wir servieren Ihnen dasselbe Getränk. Es ist ein kleiner Kniff, damit ich zählen kann, wie viele Menschen wegen des Buchs gekommen sind.

### Über den Autor

Raku Bonta

Betreibt allein ein Restaurant mit 11 Theken- und 8 Tatami-Plätzen in Higashi-Nakano, Tokio.

Tagsüber ist es ein Hamburger-Curry-Laden, in dem es nach Gewürzen duftet. Abends ist es eine Dining-Bar mit täglich wechselndem Menü.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry](images/fig-28.png)

▼ Bar „Tamuro“

https://www.instagram.com/tamuro.higashinakano/

![Bar „Tamuro“](images/fig-29.png)

Das Lokal engagiert sich auch für den Aufbau von Gemeinschaft durch Essen, mit Weinveranstaltungen alle zwei Wochen, einem monatlichen Kochkurs und mehrgängigen Dinnern.

Vor der Eröffnung des eigenen Lokals vor 12 Jahren arbeitete Raku Bonta in einem Unternehmen in der „Systemplanung“ und der „Lösungsarchitektur“.

Die Titel klingen schwierig, aber die eigentliche Arbeit war die einer „Koordination, die die Wünsche der Praxis – ‚Wir wollen das tun‘ – genau an IT-Dienstleister weitergibt und umsetzen lässt“. Kein Entwickeln mit fortgeschrittener Programmierung, sondern ein Werdegang im „Übersetzen“, das Menschen und Technik verbindet.

Heute nutzt Raku Bonta diese Erfahrung und betreibt das eigene Lokal mit generativer KI wie Google Gemini, setzt „eine Betriebsverbesserung, die auch ohne Fachwissen funktioniert“ in die Praxis um und gibt sie öffentlich weiter.
