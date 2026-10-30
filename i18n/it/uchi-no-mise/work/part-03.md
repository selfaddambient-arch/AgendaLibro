## Capitolo 2: Tecnologia - Dietro il sistema di prenotazione

Punti chiave di questo capitolo

- La qualità delle conversazioni dell'IA è stata decisa meno dall'intelligenza dell'IA che dai «fatti del locale che le consegniamo» e dal fatto che «un programma sovrascriva da solo le risposte dell'IA»
- Il sistema di prenotazione che avevo costruito a sensazione aveva ancora un buco che lasciava leggere dall'esterno i dati personali dei clienti, e zero test automatici. Ho fatto fare un audit all'IA per trovarli e le ho fatto correggere
- Da quella riflessione ho cambiato il modo di costruire: definire i requisiti nel dettaglio prima di costruire e consegnare all'IA la specifica stessa da implementare

(Questo capitolo contiene molti termini tecnici. Se la tecnologia non Le interessa, può passare al capitolo 3 e il filo del discorso non si perde.)

### 2-1 Come funziona il server MCP

MCP (Model Context Protocol) è un insieme comune di convenzioni con cui l'IA usa strumenti e dati esterni. Proposto da Anthropic, è oggi supportato da molte IA, tra cui ChatGPT e Claude.

Con un'analogia, MCP è uno standard per le prese di corrente, per l'IA. Poiché la forma della presa è fissata, gli apparecchi di qualsiasi produttore funzionano se inseriti. Allo stesso modo, se si costruisce una finestra che corrisponde alla forma di MCP, qualunque IA può usare quella finestra.

Un server MCP dice all'IA «che cosa si può fare attraverso questa finestra». Il server MCP di Tamuro, per esempio, mette in fila strumenti come questi.

- Leggere le informazioni del locale (orari di apertura, numero di posti, regole della casa, atmosfera)
- Leggere piani e prezzi (il risultato del calcolo degli sconti per numero di persone e data)
- Leggere le fasce libere (gli orari prenotabili in un giorno indicato)
- Creare l'URL di una pagina di prenotazione con le condizioni già compilate

Quando un cliente chiede alla propria IA: «C'è posto da Tamuro stasera?», l'IA si collega al server MCP di Tamuro, sceglie «leggere le fasce libere» tra gli strumenti in elenco e lo chiama. Il server di Tamuro restituisce il risultato, e l'IA lo mette in parole per il cliente.

Ciò che conta è che l'IA non conferma le prenotazioni da sola. Nella prima versione ho lasciato di proposito la conferma della prenotazione fuori dagli strumenti. Tutto ciò che l'IA può fare è leggere e indirizzare le persone a una pagina di prenotazione con le condizioni già compilate. Il pulsante di conferma lo preme il cliente stesso sulla pagina di Tamuro. Il pericolo che l'IA crei un gran numero di prenotazioni sbagliate o per scherzo è evitato fin dall'inizio per progetto.

Il calcolo dei prezzi usa lo stesso meccanismo di calcolo del sito di prenotazione. I prezzi mostrati nel modulo di prenotazione, nella finestra di conversazione e tramite MCP escono tutti dallo stesso, unico programma. È l'altro significato del compito di cui scriverò più avanti, «concentrare in un solo posto il calcolo degli sconti».

【Figura 2-1】Dall'IA del cliente alla pagina di prenotazione di Tamuro. Il cliente preme il pulsante di conferma

### 2-2 Come funziona la finestra di conversazione «T-AI-MURO»

#### I prezzi dal programma, le parole dall'IA

T-AI-MURO divide i ruoli in due. Il programma produce prezzi e fasce libere con calcoli fissi, e l'IA li mette in parole per il cliente.

L'IA è brava a produrre testo, ma non c'è garanzia che calcoli correttamente ogni volta. Come si sommano gli sconti, i gradini per numero di persone, il numero di giorni dello sconto per prenotazione anticipata, se è cumulabile con l'happy hour. Se si lasciano tutte queste regole all'IA, di sicuro sbaglierà da qualche parte. E un errore sul prezzo danneggia la fiducia del cliente più di ogni altra cosa.

Quindi, le parti che non devono sbagliare vanno al programma, e le parti che trasmettono le cose con dolcezza vanno all'IA. Questa divisione è il primo principio nella costruzione della finestra di conversazione.

#### Per un piccolo locale non serve il RAG

Per far rispondere l'IA sul locale, bisogna consegnarle la conoscenza del locale. Un metodo di uso comune è il RAG (generazione aumentata dal recupero). Si taglia la conoscenza in piccoli pezzi e la si archivia e, a ogni domanda in arrivo, si trovano solo le parti che sembrano pertinenti e si consegnano all'IA. Quando la conoscenza è vasta, questo metodo è indispensabile.

Ma la conoscenza di Tamuro non è così grande. La storia del locale, il cibo, le regole, l'atmosfera, il pensiero del titolare. Tutto insieme, sta comodamente entro ciò che l'IA può leggere in una sola volta.

Così a Tamuro ho scelto di far leggere all'IA ogni volta l'intero testo della conoscenza del locale. Non serve costruire il meccanismo di ricerca richiesto dal RAG e nella ricerca non si perde nulla. All'inizio avevo previsto di riutilizzare un meccanismo RAG, ma a metà strada ho adottato l'approccio del testo integrale.

Farlo leggere per intero ogni volta costa di più in spese per l'IA. Così uso un meccanismo che riutilizza lo stesso testo per abbassare i costi di input (prompt caching: invece di far rileggere all'IA ogni volta lo stesso preambolo, le fa ricordare quello che ha già letto). Basta introdurre il RAG quando la conoscenza diventa grande.

#### Un programma che sovrascrive da solo le risposte

Nel capitolo 1 ho scritto che nel primo test solo 9 su 36 sono stati superati. Parte della causa stava nel modo in cui era costruito il programma.

Indagando, ho trovato rimasto in funzione un meccanismo in cui il programma giudicava a parole chiave la risposta data dall'IA e la sostituiva con una frase fissa. Quando comparivano parole come «prenotazione» o «oggi», buttava via la risposta dell'IA e la sostituiva con un elenco di fasce libere. Anche quando l'IA rispondeva correttamente, la risposta non arrivava mai al cliente.

Inoltre ho scoperto che il corpo principale della conoscenza del locale (33 sezioni) non era incluso nelle istruzioni all'IA. L'IA rispondeva senza conoscere il locale.

La qualità delle conversazioni dell'IA è stata decisa meno dall'intelligenza dell'IA stessa che dai fatti del locale consegnati e dal fatto che un programma sovrascrivesse da solo le risposte dell'IA.

#### Riempire le domande e risposte attese contando

Ho portato gli scenari di test dai 36 iniziali a 110 e poi a 355. Ma se si aggiungono scenari a casaccio, non c'è modo di sapere se manca qualcosa. Alla domanda «È completo?», la risposta onesta era «No, non lo è».

Così, invece di allargare la copertura a immaginazione, ho fatto in modo che fosse una questione di contare in automatico i punti ancora non attraversati e di riempirli. Per quattro cose: le 33 sezioni della conoscenza del locale, le transizioni tra le scelte, i gradini degli sconti e le combinazioni di fasce orarie e giorni della settimana. Conto quante volte ciascuna è stata attraversata nei test e aggiungo automaticamente scenari dove il conteggio è zero.

Ho usato anche un metodo che incrocia sei assi (numero di persone, scopo, modo di bere, data e ora, formulazione, menu) e crea scenari in modo che ogni coppia di variabili venga attraversata almeno una volta.

Ho trovato anche un buco legato al tempo. «Oggi» e «da adesso» sono determinati dall'ora reale in cui gira il test, quindi i risultati di un'esecuzione a mezzogiorno e di una di sera differiscono. Così ho fissato l'orologio durante i test e li ho fatti girare in cinque momenti: prima dell'apertura, durante l'orario di attività, poco prima della chiusura, in un normale giorno di riposo e in un giorno festivo.

Le risposte dell'IA variano leggermente ogni volta, anche alla stessa domanda. Per gli scenari legati direttamente alle vendite, ho posto la condizione che superino il test tre volte su tre.

#### Quando esce un numero brutto, sospettare prima del test

Nel test che ha fatto girare 355 scenari in 5 momenti, su 1.775 conversazioni ne è stato superato il 28,5%.

Invece di mettermi subito a correggere, ho prima distinto: «Questo numero è davvero una debolezza di T-AI-MURO o è sbagliato il test?» Se si corregge mentre il test è sbagliato, si finisce per «correggere» anche le risposte giuste.

| Causa dell'errore | Numero |
| --- | --- |
| Una frase fissa dirotta la domanda | 276 |
| Non risponde alla domanda, passa al flusso di prenotazione o alle raccomandazioni | 266 |
| Guasto dell'ambiente di test (T-AI-MURO non ha potuto produrre una risposta a causa del tetto di spesa) | 211 |
| Errori in date, giorni della settimana, festivi, giorni di riposo | 142 |
| Inventare fatti inesistenti sul locale o affermarli con sicurezza, promettere di inoltrare messaggi | 119 |

I primi due avevano la stessa radice: «reagire alle parole e fare una mossa fissa prima di rispondere alla domanda del cliente». I 211 al terzo posto non erano errori di T-AI-MURO. A metà del test si è raggiunto il tetto di spesa, e T-AI-MURO semplicemente non ha potuto produrre risposte. Escludendoli, il tasso di superamento diventa del 32,4%.

Anche l'IA che giudica può sbagliare. Quando ho estratto 20 casi e li ho controllati, 2 erano errori dalla parte del test. In uno di essi, il giudice non sapeva che «questo sito di prenotazione ha la registrazione dei soci». Il giudice non sa nulla oltre ai materiali che gli sono stati dati. La precisione del test è decisa dalla completezza delle regole del locale consegnate al giudice.

Nel nuovo test dopo le correzioni, il tasso di superamento per le indicazioni su prezzi e piani è salito dal 29,4% al 42,7%. Non ho ancora fatto girare il test finale che fa passare di nuovo tutti i casi. Per contenere i costi, ho deciso che il test di tutti i casi si fa una sola volta, prima di mettere in produzione una modifica importante. Sto continuando ad alzare il tasso di superamento anche mentre scrivo questo libro.

#### Il test ha fermato la produzione

I test con l'IA costano denaro. Il primo test da 36 scenari è costato circa ¥426 (circa $2,8). La maggior parte è andata nello «sforzo di pensiero» dell'IA che faceva la parte del cliente e, quando l'ho spento, 3 scenari sono costati circa ¥6 (circa $0,04).

Ma poi un giorno, a metà di un test, il saldo d'uso dell'IA è finito e tutto si è fermato. In un solo giorno avevo usato circa 35 milioni di token (l'unità di testo che un'IA legge e scrive). La causa era aver fatto girare più e più volte il test da 221 scenari e aver fatto girare quattro volte ciascuno gli scenari legati direttamente alle vendite.

Ciò che faceva paura era che il test e la produzione usassero lo stesso portafoglio. Quando il saldo finisce, si ferma perfino la finestra di conversazione in produzione. In un altro giorno ho raggiunto un tetto mensile che mi ero imposto, e la finestra di conversazione in produzione e l'IA che crea gli argomenti di conversazione per i clienti nel locale si sono fermate contemporaneamente.

Il vero pericolo di un budget di test non era il conto, ma che la produzione usasse lo stesso portafoglio.

Da lì le regole sono cambiate. Fare prima i controlli che non costano nulla (test dei programmi e controlli automatici delle schermate). Limitare i test che chiamano l'IA a quelli legati a ciò che è stato corretto. Far girare il test di tutti i casi una sola volta, prima della produzione. Scrivere nelle istruzioni il costo stimato e un tetto, e fermarsi se sembra probabile raggiungerlo. Per tenere fondi per la produzione, fermare i test quando l'uso a livello di organizzazione si avvicina al tetto.

C'è stata anche una lezione su come i costi si gonfiano. Una volta, il costo dell'IA che giudica è arrivato a 2,6 volte la stima. La causa era che il lungo preambolo consegnato ogni volta al giudice (la conoscenza e le regole del locale) non veniva riutilizzato, quindi a ogni volta veniva addebitato un costo di riscrittura. Quando l'ho corretto in modo da scrivere il preambolo una sola volta e riutilizzarlo, il costo per conversazione è sceso a circa un terzo. Il costo dell'IA non si gonfia con il numero di chiamate, ma con il numero di volte in cui si riscrive lo stesso preambolo.

Lo stesso test completo da 221 scenari è sceso da circa ¥1.040 (circa $6,9) a circa ¥400 (circa $2,7) con ripetuti miglioramenti. Ho sostituito l'IA che faceva la parte del cliente con un copione fisso e ho diviso le informazioni consegnate all'IA in un «nucleo inviato ogni volta» e «sezioni lette solo quando servono».

A causa dei vincoli di budget, la progettazione è cambiata verso l'aumento delle parti che si possono controllare a costo zero, cioè quelle decise dal programma. Di conseguenza è aumentata anche la precisione. Il denaro cambia il progetto.

【Figura 2-2】Risultati dei test con l'IA. Il tasso di superamento e la ripartizione delle cause degli errori

### 2-3 Far fare all'IA un audit di ciò che ho costruito

#### I nomi dei clienti si potevano leggere dall'esterno

Ad agosto 2026, mentre rivedevo il funzionamento del sistema di prenotazione, ho fatto una scoperta che mi ha fatto correre un brivido lungo la schiena.

I dati di prenotazione dei clienti potevano essere letti da chiunque dall'esterno. Nomi, numeri di telefono, indirizzi email, il campo delle richieste. Tutto ciò che era stato inserito in una prenotazione poteva essere estratto per intero, senza alcuna autenticazione.

Devo dire una cosa con onestà. È vero che i dati potevano essere letti dall'esterno. Allora il sito di prenotazione aveva pochissimo traffico, e credo sia improbabile che qualcuno li abbia letti davvero. Ma non ho alcuna registrazione che possa dimostrare che non siano stati letti. «Poteva essere recuperato» e «è stato recuperato davvero» sono due cose diverse, ma già la prima era da sola un grave fallimento per un locale.

Risalendo alla causa, tutto dipendeva da come era costruito il modulo di prenotazione. Per calcolare i posti liberi, il modulo caricava direttamente dalla schermata 35 giorni di dati di prenotazione. Se la schermata può leggerli, allora chiunque sappia come sono costruite schermate di quel tipo può leggere gli stessi dati. Era il risultato di una prima base costruita a sensazione, che aveva raggiunto l'obiettivo «mostrare i posti liberi» per la via più breve.

Ho trovato anche che l'indirizzo email per avvisare l'amministratore del locale era pubblico e che chiunque poteva scrivere nel luogo in cui erano archiviate le traduzioni, il che significava che i dati potevano essere vandalizzati o i costi gonfiati.

L'ordine della correzione contava. Se avessi vietato tutte le letture in un colpo solo, il modulo di prenotazione non avrebbe più potuto mostrare i posti liberi e avrebbe smesso di funzionare. Così per prima cosa ho spostato il calcolo dei posti liberi su un punto di accesso lato server. Poi ho cambiato la schermata di prenotazione completata in modo che ricevesse dal server solo le informazioni necessarie. Infine ho chiuso la lettura dall'esterno. Ho fatto la correzione in quattro fasi in questo ordine e l'ho applicata alla produzione.

Dopo la correzione, ho usato una macchina per verificare che fosse davvero chiuso. Ho preparato un test che prova a leggere i dati delle prenotazioni senza autenticazione e lo faccio girare automaticamente dopo ogni modifica per confermare che sia sempre rifiutato. Non ho corretto una volta e basta. Ho fatto in modo che un controllo vigili perché non si riapra mai più.

#### Dati reali dei clienti rimasti nella cronologia di sviluppo

Poi ho fatto fare all'IA un audit dell'intero repository (il luogo di archiviazione del programma) ed è emerso un problema più grave.

Durante lo sviluppo, un file contenente dati di clienti reali (indirizzi email e numeri di telefono di 55 prenotazioni) era stato inviato al repository, rimanendo incluso nella cronologia delle modifiche del programma. Il repository era privato, ma poiché restava nella registrazione, non potevo lasciar correre.

Ho rimosso il file dall'intera cronologia delle modifiche, ho riscritto la cronologia e l'ho archiviata di nuovo. Ciononostante, i vecchi record precedenti alla riscrittura potevano ancora restare dal lato di GitHub, che ospita il repository. Così ho chiesto al supporto di GitHub di eliminarli e ho confermato che è stato fatto.

L'audit ha trovato anche altri problemi: il punto di accesso delle traduzioni poteva essere usato senza autenticazione, l'accesso dell'amministratore poteva essere attaccato a forza bruta e c'era una finestra di tempo in cui, se il pagamento fosse stato riattivato, una prenotazione poteva essere confermata ancora non pagata. Li ho corretti uno a uno, cominciando dal più grave.

#### I test automatici erano zero

L'audit ha rivelato un altro fatto. Il sistema di prenotazione non aveva nemmeno un test automatico.

I test automatici sono un meccanismo in cui una macchina verifica automaticamente se il programma funziona correttamente. Senza test, quando si corregge qualcosa non c'è modo di verificare se si è rotto altro. Ogni volta che si aggiunge una funzione, da qualche parte si rompe silenziosamente qualcosa. Era esattamente lo stato delle cose nel periodo in cui costruivo a sensazione.

Così ho ricostruito da zero le basi dei test. Ho introdotto un sistema (CI) che esegue automaticamente quattro controlli dopo ogni modifica: controllo dei tipi, controllo dello stile, test e build. Decisioni importanti come il calcolo dei prezzi, il giudizio sulle prenotazioni, il collegamento dei soci e l'emissione dei coupon sono state separate dai programmi delle schermate in modo da poter essere verificate da sole. Anche le regole di lettura e scrittura del database sono controllate in un ambiente di test che imita un vero database. I test unitari sono partiti da 275 e in seguito sono saliti oltre 500.

C'è una condizione che impongo sempre ai test: «romperlo e confermare che fallisca». Anche quando un test diventa verde (supera), non si sa se quel test possa davvero cogliere un problema. Mi fido del test solo dopo aver rotto di proposito il programma e aver confermato che il test diventa rosso (fallisce). Perché i test scritti dall'IA a volte non verificano proprio nulla.

#### Otto buchi nel modulo di prenotazione

Dopo aver messo in piedi le basi dei test, ho fatto esaminare di nuovo all'IA l'intero flusso di prenotazione. Ha trovato otto problemi che facevano danni reali.

Il più grave era che premendo ripetutamente il pulsante di invio si creava una doppia prenotazione. Succedeva davvero in produzione. L'ho corretto con un meccanismo che elabora la stessa azione una sola volta anche se arriva due volte (idempotenza). Gli altri problemi erano questi: una prenotazione non si poteva confermare se restavano informazioni su una voce di menu eliminata; c'era una lacuna nel controllo del tutto esaurito che lasciava margine per superare la capienza; nessuno si accorgeva quando l'invio di un'email di conferma falliva; l'input non veniva convalidato lato server; quando si verificava un errore comparivano a schermo messaggi tecnici interni; il testo nei campi di input era così piccolo che su iPhone la schermata si ingrandiva da sola; e il riempimento automatico dei campi non funzionava.

Per gli errori delle email, ho reso possibile rilevarli nella schermata di amministrazione e reinviare. Durante quell'indagine ho scoperto anche che il registro di audit che registra le conferme delle prenotazioni falliva ogni volta, da ben prima della correzione, e non aveva registrato nulla.

Li ho corretti uno a uno e li ho applicati alla produzione.

#### Non saltare mai la verifica del codice scritto dall'IA

Ciò che ho imparato da questa esperienza è che proprio perché un programma è scritto dall'IA, non si deve saltare la verifica.

L'IA dà rapidamente forma a ciò che le viene detto. Ma l'attenzione a ciò che non le viene detto, come «rendilo illeggibile dall'esterno» o «tratta un doppio invio come uno solo», non entra se non lo si indica. E buchi come questi stanno silenziosamente dentro programmi che sembrano funzionare.

Le persone non hanno bisogno di leggere tutto il codice. La correttezza del programma è tenuta d'occhio dai controlli delle macchine e dall'audit di un'altra IA. Se il risultato si adatta allo scopo del locale lo tiene d'occhio il titolare. Non serve leggerlo, ma non si deve saltare la verifica. È questo, credo, che significa costruire con un'IA di tipo agente.

【Figura 2-3】Le regole quando si poteva leggere dall'esterno e le regole dopo la correzione (estratto) *(La schermata è in giapponese.)*

### 2-4 Costruire a sensazione moltiplica le contraddizioni

Più funzioni aggiungevo, più c'erano parti in conflitto con ciò che avevo deciso prima.

Il caso tipico era il calcolo degli sconti. Nel modulo di prenotazione, nella schermata di conferma, nell'email e nella schermata di amministrazione, il calcolo degli sconti era scritto separatamente in ciascun posto. Se cambiavo una regola di sconto in un posto, un altro continuava a calcolare con la vecchia regola. Per la stessa prenotazione, la schermata e l'email potevano mostrare importi diversi.

Più tardi ho riunito il calcolo dei prezzi in un unico file. Il modulo di prenotazione, la finestra di chat e il server MCP producono i prezzi da lì.

Anche le regole di cumulo degli sconti sono cambiate strada facendo. Come ho scritto nel capitolo 1, l'happy hour doveva inizialmente essere cumulabile con altri sconti, ma ho visto che non avrebbe dato profitto e l'ho cambiato in non cumulabile. Ogni volta che una regola cambiava, una persona doveva ricordare dove correggere. Era la debolezza di un sistema costruito a sensazione.

C'era anche un disallineamento tra l'ambiente di test e la produzione. Mentre collaudavo la finestra di chat, una domanda, «Non c'era qualcosa come il 10% di sconto?», ha rivelato che le regole di sconto nell'ambiente di test si erano allontanate da quelle di produzione. Se i valori nell'ambiente di test differiscono dalla produzione, si possono superare i test e sbagliare comunque in produzione. Quello che ho deciso allora è il principio «la produzione fa fede». Da allora, prima di ogni esecuzione dei test, copio le impostazioni di produzione nell'ambiente di test e confermo che il disallineamento sia zero prima di avviarli.

L'IA costruisce ciò che le viene detto. Ma non nota le contraddizioni con decisioni precedenti. Ciò che previene le contraddizioni non è l'IA. È decidere le cose in anticipo.

### 2-5 Imparare di nuovo la definizione dei requisiti

Dopo aver riflettuto sul sistema di prenotazione che avevo costruito a sensazione, ho imparato di nuovo la definizione dei requisiti. Definire i requisiti significa decidere, prima di costruire, che cosa si costruirà, che cosa non si costruirà e chi lo userà e come, e metterlo per iscritto in un documento.

Era una cosa che facevo come ovvia ai tempi in cui lavoravo nei sistemi. Ma una volta potuto costruire con l'IA, l'avevo saltata senza accorgermene. Le si dice un'idea e in pochi minuti compare qualcosa che funziona. In quella velocità avevo tagliato la fatica del decidere.

Il mio modo di costruire oggi ha tre fasi.

1. Per prima cosa, decidere nel dettaglio i requisiti. Che cosa costruire, che cosa non costruire, chi lo userà. Il comportamento di ogni schermata. Come trattare le eccezioni (errori, doppie pressioni, scadenze). Le regole che si finisce facilmente per contraddire più tardi, come prezzi e sconti, le decido con particolare dettaglio. Faccio anche questo lavoro in dialogo con l'IA di chat. Faccio trovare all'IA in anticipo buchi e contraddizioni, e decide il titolare.
2. Scrivere ciò che è stato deciso come «documento dei requisiti». Non istruzioni a voce o improvvisate, ma raccolte in un unico documento. Diventa l'unico criterio per verificare in seguito che cosa è corretto.
3. Consegnare tutto il documento all'IA e farlo implementare. Do l'intero documento all'IA che scrive il programma (Claude Code), insieme alle condizioni per considerarlo superato (tutti i test superati, verifica nell'ambiente di test prima della produzione e così via). L'IA costruisce da sola finché non rispetta le condizioni e controlla da sola. Il titolare guarda solo quando si ferma a metà e al controllo finale.

Per esempio, il documento dei requisiti della finestra di chat «T-AI-MURO» è stato riscritto dalla prima versione alla terza. Nella seconda versione ho deciso «non far calcolare i prezzi all'IA», «mettere in un'unica finestra la conoscenza del locale e il calcolo dei prezzi» e «tenere anche il modulo, per chi non vuole prenotare in chat». Nella terza versione ho deciso «dove tenere l'originale della conoscenza del locale», «solo questa finestra mostra le fasce libere», «fare del primo scambio una domanda a quattro scelte» e «non salvare i registri delle conversazioni; conservare solo le domande a cui non si è potuto rispondere». Poiché le decisioni restano in un documento, posso ricostruire in seguito perché le cose stanno così.

Con questo modo di costruire, anche quando aggiungo funzioni posso accorgermi subito delle contraddizioni confrontando con il documento. Proprio in un'epoca in cui è l'IA a costruire, serve il «potere di decidere» prima di costruire. È stata la lezione più grande che ho imparato dal sistema di prenotazione.

Ho costruito anche un meccanismo che mette la procedura stessa in un documento e la consegna all'IA, così che questo modo di costruire possa essere ripetuto allo stesso modo ogni volta che avvio un nuovo prodotto. Ne scriverò nel capitolo 4.

【Figura 2-4】Indice del documento dei requisiti di T-AI-MURO (versione 3) *(La schermata è in giapponese.)*

### 2-6 Imparare il linguaggio dell'interfaccia

C'è un'altra cosa che ho imparato di nuovo: i nomi dei componenti delle schermate.

Anche quando dicevo all'IA «fai questo qui», la schermata spesso non veniva come mi aspettavo. Pensando alla causa, ho scoperto che non conoscevo i nomi dei componenti delle schermate. Anche descrivendo «una piccola finestra che compare sopra» o «un avviso che sparisce in pochi secondi», era difficile per l'IA capire che cosa intendessi.

Così ho letto un libro di riferimento sull'interfaccia utente (UI, l'aspetto e il funzionamento di una schermata) e ho imparato i nomi dei componenti e i termini tecnici del design.

| Componente | Che cos'è |
| --- | --- |
| Modale | Una piccola finestra che compare sopra la schermata. Non si può usare la schermata dietro finché non la si chiude |
| Toast | Una notifica che compare al bordo della schermata per qualche secondo e sparisce da sola |
| Scheda | Un meccanismo in cui premendo un titolo cambia il contenuto |
| Accordion (a fisarmonica) | Un meccanismo in cui premendo un titolo il contenuto si apre e si chiude |
| Cassetto | Un menu che scivola fuori dal lato della schermata come un cassetto |
| Altri | Breadcrumb (una traccia che mostra dove ci si trova ora), caroselli (elementi che scorrono di lato), bottom sheet (un pannello che sale dal fondo della schermata) e così via. Ogni nome che si impara permette di istruire l'IA con una sola espressione |

Quando si comunica per nomi, le schermate prodotte dall'IA si avvicinano al primo colpo. Se si dice «Mostra la schermata di conferma della prenotazione come modale», l'IA non esita.

#### L'IA oscilla agli estremi tra aggiungere e togliere

Anche dopo aver imparato le parole, costruire schermate con l'IA aveva un altro tipo di difficoltà. L'IA oscilla ampiamente.

Quando ho chiesto un'intestazione «elegante» per il sito di prenotazione, ne è venuta una imponente e spessa. Ma tutto lo scopo di un sito di prenotazione sono le prenotazioni. Per i clienti abituali che prenotano ogni volta, un'intestazione spessa con lunghe spiegazioni è solo un fastidio. Gliel'ho fatta ridurre di circa metà in lunghezza verticale, mantenendo la stessa quantità di informazioni.

Quando ho uniformato il piè di pagina delle email e ho aggiunto un collegamento alla Guida al Secondo Locale, il testo del corpo è sembrato a confronto spoglio e misero. Così ho aggiunto anche al corpo un titolo, una tabella dei punti chiave e un pulsante da premere. Quando ho aggiunto nel piè di pagina un ingresso alla finestra di chat, sembrava disordinato. Quando l'ho compresso in due righe di collegamenti separati da linee, era ordinato ma poco appariscente. Alla fine si è assestato su due schede che mostrano il ruolo con «quando usarlo». A sinistra «per la prossima prenotazione», a destra «dopo il pasto».

Troppo spesso, troppo sfoltito, troppo vistoso. A decidere il punto giusto, ogni volta, era la parola del titolare.

#### Una proposta di design senza immagini

È successo anche questo. Ho chiesto all'IA che scrive i programmi di creare proposte di miglioramento per la finestra di chat usando un'IA di design (Claude Design), ed è tornato un rapporto che diceva: «Ho fatto proposte per otto schermate». Ma quando l'ho aperto, c'era solo una descrizione testuale. L'IA non era riuscita a disegnare immagini, eppure era rimasto solo il rapporto «fatto».

Alla fine l'IA dal lato della chat ha disegnato quattro proposte direttamente nella schermata di design. Ha ripreso da uno screenshot i colori della schermata attuale, ha messo la storia del locale in una linea del tempo, ha suddiviso i sapori in due riquadri, «metodo di cottura» e «gusto», ha trasformato i piani in schede esplicative e ha unificato i prezzi in un riepilogo della prenotazione.

Quando si fa eseguire un test all'IA, dice «superato». Quando si chiede un design all'IA, dice «fatto». Controllare che cosa c'è dentro è compito di una persona. Il criterio per giudicare è qualcosa che solo le persone possono continuare a mantenere.

#### Che cosa si può portare via da questo capitolo

- Costruire qualcosa che funziona e saperlo gestire in sicurezza sono cose diverse.
- Controllare l'output dell'IA non dalle parole dell'IA ma dai test. Di un test ci si può fidare solo dopo aver verificato che fallisca quando si rompono le cose.
- I calcoli che non devono sbagliare, come i prezzi, non vanno lasciati alla generazione di testo dell'IA. Vanno dati al programma.

Il seguito di questo capitolo (i buchi trovati di recente e i passaggi che ho compiuto per correggerli) è su note e su X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
