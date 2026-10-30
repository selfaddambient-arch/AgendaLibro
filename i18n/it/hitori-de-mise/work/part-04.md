### 3-6. Il primo ostacolo: la semplice suddivisione e la «trappola della qualità dell'immagine»

La sfida creativa di fare il logo era finita.

Ma il lavoro non era ancora concluso.

Torniamo agli adesivi di LINE. Quello che avevo in mano era un «foglio» con 25 illustrazioni disegnate su un'unica pagina.

Per presentarle come adesivi di LINE, dovevo ritagliarle una a una, rendere trasparente lo sfondo e ridimensionarle. Era un lavoro noioso che continuavo a rimandare.

«Non è possibile ritagliarle a mano...»

Ho consultato Gemini chiedendo una soluzione. Gemini ha detto, come se nulla fosse:

«Automatizziamo il lavoro usando un linguaggio di programmazione chiamato Python».

Francamente, ho quasi mollato lì.

«Python? Ne ho sentito il nome, ma installare quel genere di software sul mio computer mi fa paura. Anche la configurazione sembra difficile. Non aspettarti troppo da chi gestisce un bar...»

Ma questo è uno dei momenti salienti del libro. Come se avesse intuito i miei pensieri, Gemini ha fatto una proposta sorprendente.

Gemini:

«Non serve configurare alcun ambiente. Usa uno strumento gratuito di Google chiamato "Google Colab". Funziona nel browser, quindi devi solo copiare e incollare il codice che ti scrivo».

«Cosa? Esiste una cosa del genere?»

Non credevo alle mie orecchie. Non avevo mai immaginato che esistesse un ambiente in cui la programmazione gira solo con un browser, senza installare nulla sul mio PC.

Non «dopo aver studiato Python», ma «facendomi insegnare dall'IA perfino l'esistenza dello strumento (Colab)».

In quel momento è crollata la mia convinzione che «programmare significhi fare un sacco di preparativi».

### 3-7. Non «leggere» la schermata di errore: «fotografarla e inviarla»

Come indicato, ho aperto Google Colab, ho incollato il codice e ho premuto il pulsante di avvio.

Ma la realtà non è così gentile. Sullo schermo è comparsa una sequenza di testo rosso vivo... un messaggio di errore.

«Errore: file immagine non trovato...»

Il me di una volta, solo a vedere questo errore, avrebbe avuto una reazione allergica e avrebbe chiuso in silenzio il browser.

Ma ora avevo un alleato: l'IA «multimodale», un'IA con gli occhi.

Non ho nemmeno provato a leggere il messaggio di errore.

Ho semplicemente fatto uno screenshot della schermata e l'ho incollato, zac, nella casella di chat di Gemini.

E ho aggiunto una sola riga: «È comparso un errore di qualche tipo».

![Incollare così com'è in Gemini la schermata di errore di Google Colab](images/fig-17.png)

Gemini ha analizzato subito l'immagine e ha mandato una risposta.

Gemini:

«Ah, il nome del file dell'immagine che viene caricata è sbagliato. Ho corretto il codice usando ".jpg". Rieseguilo con questa versione».

«...Wow, che divertente!»

Questo scambio sembrava meno programmazione e più un gioco a «trova le differenze» o un palleggio.

- Io: (incollando uno screenshot) «Si è fermato di nuovo».

- Gemini: «La dimensione dell'immagine non corrisponde. Aggiungo una funzione che la regola automaticamente».

- Io: (incollando uno screenshot) «Stavolta l'immagine è sgranata».

- Gemini: «Ho dimenticato di aggiungere il processo chiamato "LANCZOS" che preserva la qualità dell'immagine. Lo correggo».

Non capisco nemmeno una riga del codice. Quando compare un errore, faccio uno screenshot e lo lancio all'IA con un «Guarda!».

Questo «delegare tutta l'analisi dell'errore all'IA» è stato il più grande segreto per cui, con zero conoscenze, ho potuto costruire un sistema e, al tempo stesso, l'esperienza più emozionante di tutte.

### 3-8. Il muro più grande: «disallineamento del disegno a mano» e «sbordamenti»

Continuando questa «conversazione fatta di errori», il sistema diventava sempre più raffinato.

E finalmente ho affrontato la sfida più grande: la «Fase 2: ritaglio automatico di impaginazioni disegnate a mano».

Ho voluto strafare un po'.

«Facciamo un foglio 5×5, con 25 adesivi. E siccome voglio un aspetto più artigianale, voglio disporli liberamente, senza vincoli dalle linee della griglia».

Con un codice che divide semplicemente il foglio in parti uguali, la mano o la scritta di un personaggio sconfina nella cella accanto e viene tagliata in modo miserabile.

Ho provato anche un metodo che «ritaglia tutto tranne lo sfondo bianco», ma i margini uscivano irregolari e non ha funzionato.

Stavo per arrendermi. Poi, attingendo all'istinto dei miei tempi nei sistemi, ho detto a Gemini:

«Voglio che abbandoni l'idea di tagliare l'immagine con le forbici. Guarda invece in quale cella si trova il "punto centrale" di ogni disegno. Se il centro è in quella cella, anche se sborda un po', considera l'intero disegno come "appartenente a quella cella" e mettilo nel secchio di quella cella».

Questa è la soluzione che ho chiamato il «metodo del secchio a griglia».

Perché mi è venuto in mente di «mettere in un secchio in base al punto centrale» invece di «tagliare con le forbici»?

Il modo di pensare del dilettante (analogico): si immagina di «ritagliare una singola immagine con le forbici». Così si taglia proprio lungo la linea, e le mani e i piedi del personaggio vengono mozzati.

Il modo di pensare di chi viene dai sistemi (digitale): un computer non ha il senso fisico del «tagliare». Ha invece le «coordinate (posizioni)». Io l'ho visto così: «Anche se sborda un po', finché l'"ombelico (punto centrale)" dell'immagine è dentro la cella, possiamo considerare l'intera immagine come "appartenente a questa cella"».

![L'idea analogica di «tagliare lungo le linee» e l'idea digitale di «scegliere per punto»](images/fig-18.png)

Questo significa «tradurre un lavoro analogico vago in regole digitali chiare». Quando si danno istruzioni a un'IA, funziona bene pensare a una regola di questo tipo, in cui la risposta esce uguale «chiunque guardi (o calcoli)».

Gemini ha trasformato magnificamente in codice questa richiesta astratta. Il risultato era perfetto.

La scritta «Grazie!» e le code che erano sconfinate nelle celle vicine sono state tutte riconosciute con precisione e raccolte come adesivi singoli.

Ha perfino rispettato la mia richiesta egoistica: «L'ultimo (il venticinquesimo) non serve, saltalo». Finalmente avevo uno strumento in cui «basta inserire l'immagine e premere un pulsante per ottenere un set completo di immagini per la richiesta degli adesivi di LINE».

Tutto quello che ho fatto è stato comunicare il «problema sul campo (i disegni vengono tagliati)» e proporre una «soluzione logica (decidere in base al punto centrale)». Tutto il codice difficile lo ha scritto l'IA.

Questa è l'essenza stessa del «vibe coding», cioè costruire sistemi partendo da zero conoscenze.

#### Riepilogo del Capitolo 3

1.  Disegnare con l'IA non è «una volta e basta». Si può rifare quante volte si vuole in base alla situazione: cambiare i personaggi, aggiungere un tocco stagionale, cambiare mezzo espressivo.

2.  Anche un «concetto» astratto (persone che si riuniscono) può diventare una «forma» (un logo) attraverso un dialogo ripetuto.

3.  I lavori noiosi (ritagliare immagini) sono proprio quelli che Gemini × Google Colab possono automatizzare. Gli errori si risolvono con gli screenshot.

#### Rubrica 1: Un corso accelerato su «Google Colab» per il titolare di formazione umanistica

~Usi una «cucina in affitto» e lasci il Suo PC com'è~

«Google Colab», comparso nel testo principale. Fare programmazione (Python) sul proprio computer è come «preparare un autentico ramen da zero, a partire dal brodo, nella cucina di casa». I preparativi sono tanta fatica.

Google Colab, invece, è «una cucina in affitto gratuita, completamente fornita di attrezzi». Basta aprire il browser e gli strumenti migliori sono pronti. Non occorre cambiare alcuna impostazione del computer. Si può programmare con il solo browser, mantenendo pulito il proprio ambiente. Per cominciare, cerchi «Google Colab» e dia un'occhiata a questa cucina in affitto.

#### Rubrica 2: Non «leggere» la schermata di errore è la risposta giusta

~Impari a usare l'arma definitiva: lo screenshot~

Quando compare un errore, cerca con impegno di decifrare il messaggio in inglese? È tempo sprecato.

Quando in cucina qualcosa ha un sapore strano, si chiede allo chef di assaggiare. Allo stesso modo, mostri all'IA soltanto uno «screenshot (cattura dello schermo)».

- Windows: \[Win\] + \[Maiusc\] + \[S\]

- Mac: \[Cmd\] + \[Maiusc\] + \[4\]\
  Li prema, tracci un riquadro attorno all'errore e lo incolli in Gemini. Tutto qui. Non «legga l'errore»: «mostri l'errore». Basta cambiare mentalità così per triplicare la velocità di sviluppo.

Finora ho presentato diversi esempi e tutto ciò che faccio si riduce ai tre punti seguenti.

・Non pretendere la forma finita in un colpo solo (va bene presupporre un dialogo)\
・Dire «no, non è proprio così» senza esitare\
・Presupporre che il costo delle correzioni sia zero e lanciare le richieste con leggerezza

Non serve talento per il design. Serve soltanto il coraggio di mettere in parole un «c'è qualcosa che non mi convince».
