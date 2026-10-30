## Capitolo 4: Pratica, parte 2 - Rendere più efficiente il lavoro quotidiano (con l'IA multimodale)

~Chiudere la «noiosa immissione di dati» con un solo smartphone~

### 4-1. Il problema dell'aggiornamento della carta dei vini

Per chi gestisce un bar o un ristorante, aggiornare il menu è un compito poco appariscente ma pesante.

Quello che mi dava più problemi era preparare la «carta dei vini».

Ogni volta che arriva un vino nuovo serve questo lavoro.

1.  Guardare l'etichetta della bottiglia (corsivo in lingua straniera, difficile da leggere).

2.  Digitare sul PC senza errori il nome del marchio e l'annata (l'anno).

3.  Cercare online le caratteristiche e il sapore del vino.

4.  Scrivere una «presentazione» che faccia venire voglia di leggerla.

5.  Pensare ai piatti che si abbinano bene al vino (abbinamenti).

Fare tutto questo con il dizionario in mano, nei ritagli tra un servizio e l'altro, è quasi impossibile. Lo rimandavo con un «lo faccio dopo» e la lista dei consigliati spesso finiva per non essere mai aggiornata.

### 4-2. Basta una foto. Lo shock della «Gem della carta dei vini»

Così ho deciso di provare la «funzione multimodale (riconoscimento delle immagini)» di Gemini.

Il metodo è così semplice da lasciare quasi delusi.

1.  Fotografare la bottiglia di vino con lo smartphone.

2.  Inviare quella foto a Gemini.

3.  Aggiungere una riga: «Fanne una lista».

Tutto qui.

![Una foto dell'etichetta di una vera bottiglia di vino scattata con lo smartphone](images/fig-19.jpg)

A quel punto Gemini legge all'istante le informazioni dell'etichetta dalla foto.

Non si limita a trascrivere il nome del marchio, come «Cave d'Occi Winery, Tsukimi de Ippai 2024», ma cerca anche in un enorme database online le sue caratteristiche e genera automaticamente una descrizione accattivante.

Quello che mi ha sorpreso ancora di più è che ha prodotto anche, in aggiunta, dei «suggerimenti di abbinamento».

Suggerimenti come «L'aroma ricco di questo vino si sposa bene con ○○» sono comparsi sullo schermo in pochi secondi.

Le ore che passavo a lottare con il dizionario si erano ridotte a un solo clic sull'otturatore dello smartphone.

### 4-3. Creare il proprio «Gem»

Per rendere tutto questo molto più efficiente, ho poi usato una funzione chiamata «Gems».

È una «funzione di IA personalizzata, tutta propria», in cui si può far memorizzare in anticipo all'IA un certo ruolo e certe regole.

Spiegare tutto da capo ogni volta, «Sei un sommelier. Guarda questa foto e...», è una seccatura.

Così ho registrato in anticipo su Gemini le seguenti «istruzioni (prompt)». Questo è l'interno della testa dell'«IA sommelier dedicata» del mio bar.

#### Le istruzioni che ho effettivamente registrato

> Leggi l'immagine e crea una carta dei vini nel formato seguente.
>
> Per i prezzi, non usare i prezzi di mercato. Calcolali ipotizzando il prezzo della bottiglia in un ristorante tipico (circa 2,5-3 volte il costo).
>
> Non usare il formato tabella. Crealo in modo che stia su uno o due fogli di carta A4.
>
> Il formato è solo un riferimento; crea la lista usando soltanto ciò che è stato inserito.
>
> Il formato è il seguente.
>
> Regno Unito 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8.500 (circa $57)
>
>  Oro pallido con piacevoli bollicine. Note di melone e miele tra gli aromi di agrumi... (il resto è omesso)

In realtà, la metà inferiore di questo prompt, cioè la parte del «formato (esempio)», non l'ho inventata da zero.

Prima, quando cercavo informazioni sul vino online, pensavo «Oh, la descrizione di questo locale è facile da capire» oppure «Il modo di scrivere di questo sito fa venire l'acquolina», e semplicemente avevo copiato e incollato quei brani in un blocco note, più e più volte.

Ho lanciato a Gemini quel «memo patchwork» così com'era.

«Questi sono brani che ho copiato e raccolto tempo fa. Imita questo stile e scrivi anche sul vino della nuova foto».

Questo è tutto quello che gli ho detto.

Eppure questa istruzione contiene tre accorgimenti che alleggeriscono il lavoro pratico del locale.

① «La logica del calcolo dei prezzi»

È il più grande risparmio di tempo. Poiché chiedo «il prezzo che applicherebbe un ristorante» invece del «prezzo di mercato», l'IA ricostruisce a ritroso partendo dai tipici prezzi d'acquisto e mi dà una cifra come «¥8.500 (circa $57)» che può andare direttamente sul menu. (Naturalmente la decisione finale spetta al titolare, ma avere un riferimento rende tutto più facile.)

② «Non in formato tabella, ma su carta A4»

Se l'output arriva in formato tabella come Excel, l'impaginazione si sfalda quando lo si incolla nel menu. Facendolo scrivere fin dall'inizio in un «formato menu A4», punto a un output che si possa stampare e usare così com'è.

③ Usare come «esempio» il testo copiato e incollato dal web

Invece di chiedere in modo vago «Scrivi una bella descrizione», gli mostro un esempio concreto (il mio memo copiato e incollato): «bandiera 🇬🇧 + nome del vino + prezzo + descrizione sensoriale».

Quando a un'IA si mostra un esempio, capisce «Ah, questo è il tono e il modo in cui devo scrivere» e la precisione dell'output fa un balzo. In termini tecnici si chiama «few-shot prompting», ma in sostanza è come «insegnare lasciando guardare le proprie spalle mentre si lavora».

E quelle «spalle» possono benissimo essere fatte di testo trovato, l'equivalente scritto di una foto trovata sul web.

![Il testo finito della carta dei vini prodotto da Gemini](images/fig-20.png)

### 4-4. Non serve nemmeno un'immagine. La rivoluzione del copia e incolla da LINE

La cosa bella di questa «Gem della carta dei vini» è che l'input non è limitato alle foto.

In effetti, in un bar gli ordini al rivenditore di alcolici si fanno spesso su LINE, non è vero?

Quando l'ordine è fatto, dal rivenditore arriva un messaggio come questo.

> «Grazie come sempre. Abbiamo ricevuto il Suo ordine come segue.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 bottiglie
>
> ・Ridgeview Bloomsbury 6 bottiglie
>
> ・○○ (vino nuovo) 2 bottiglie
>
> Consegneremo domani».

Un giorno mi è venuto in mente all'improvviso: «Non potrei usare questo testo così com'è?»

Per prova, ho copiato col dito questo messaggio di LINE e l'ho lanciato direttamente in Gemini.

Il risultato era perfetto.

Gemini ha riconosciuto solo i «nomi dei prodotti» nel messaggio di LINE, ha cercato le informazioni online e ha fatto una lista nel solito formato (bandiera + prezzo + descrizione).

In altre parole, non devo nemmeno aspettare che arrivino le bottiglie per fotografarle.

Nel momento stesso in cui faccio l'ordine, solo copiando e incollando dentro lo smartphone, la lista del menu è finita prima ancora che arrivino i prodotti.

Non serve aprire un PC, non serve avviare la fotocamera.

In un angolo della cucina, o in treno, il lavoro si fa con le sole operazioni sullo smartphone.

Non è questa la «vera efficienza» che dovrebbe ottenere un titolare che fa tutto da solo?

### 4-5. Il suggerimento dell'IA × il giudizio sul campo (la realtà)

Eppure non mando giù i suggerimenti dell'IA senza discuterli. Quello che conta qui è il nostro «giudizio umano sul campo».

Una volta, l'IA ha fatto questo suggerimento da abbinare a un vino:

IA: «Per questo vino rosso, l'anatra arrosto con salsa all'arancia è un abbinamento perfetto».

Un suggerimento splendido, ma purtroppo quel giorno nel frigorifero del locale non c'era anatra.

Non penso: «L'IA dice così, quindi devo comprare l'anatra». Ragiono in questo modo:

Io (sul campo): «Anatra non ne abbiamo, ma oggi è arrivato del buon pollo ruspante. Ha un grasso paragonabile a quello dell'anatra, quindi rosolerò questo pollo fino a rendere croccante la pelle e lo completerò con una salsa all'arancia, proprio come dice l'IA».

«La conoscenza dell'IA (anatra e arancia stanno bene insieme)» × «le scorte effettive (abbiamo del pollo)» = «un nuovo piatto del menu, deciso e realistico».

Questa combinazione è il vero piacere di sviluppare i menu con l'IA.

L'IA dà la risposta da manuale, ma non sa che cosa c'è oggi nel frigorifero. Colmare quella distanza è il compito del titolare.

### 4-6. L'ultimo miglio: l'IA non sa «assaggiare»

C'è un'altra cosa che non va mai lasciata all'IA.

È l'assaggio che si fa prima che qualunque cosa esca verso un cliente.

Le descrizioni e gli abbinamenti scritti dall'IA si basano su «dati generali del mondo».

Ma il vino è una cosa viva. Anche la stessa etichetta cambia di sapore con l'annata e con il modo in cui è stata conservata.

Una volta, l'IA ha scritto per un vino bianco questa descrizione: «Un vino fresco, leggero, secco. Perfetto con un carpaccio di pesce».

Ma quando ho aperto davvero la bottiglia e l'ho assaggiato, era più invecchiato di quanto mi aspettassi, con note ricche, di miele.

«Se lo servo come un "vino leggero e secco", il cliente resterà deluso... Starebbe meglio con il pollo in salsa alla panna che con il carpaccio».

Ho corretto subito il testo che aveva prodotto Gemini.

- Prima (IA): «Fresco e leggero. Adatto agli antipasti»

- Dopo (persona): «Ricco, di corpo pieno per l'invecchiamento. Abbastanza forte da reggere un secondo piatto»

L'IA fa il 90% della bozza e la persona assaggia e aggiunge «l'ultimo 10% (l'anima)».

Questo controllo è la responsabilità di chi gestisce un locale, ed è qualcosa che l'IA non potrà mai imitare.

Non «perché l'ha detto l'IA», ma «perché l'ho bevuto ed era buono».

Per servire con questa sicurezza, ancora oggi assaggio il vino appena aperto, con in una mano la lista fatta dall'IA.

#### Rubrica 3: Consigli per fotografare in modo che l'IA veda «correttamente»

~ Come mostrare un'etichetta a un sommelier ~

Quando si invia una foto a Gemini, alcuni piccoli accorgimenti possono migliorare molto il riconoscimento di ciò che vede.

1.  Evitare i riflessi: le etichette delle bottiglie riflettono facilmente la luce, quindi cambi un po' l'angolazione oppure crei un'ombra con il corpo mentre scatta.

2.  Scattare più foto e inviarle insieme: per cose come il contenuto di un frigorifero, invii insieme una ripresa ampia e dei primi piani, e l'IA riconoscerà anche gli elementi nei punti ciechi.

3.  Indicare con il dito: aiuta anche indicare con il dito il punto che vuole far guardare all'IA mentre scatta la foto. Nel prompt scriva qualcosa come «Sto indicando con il dito». È come indicare un piatto sul menu in un ristorante all'estero.
