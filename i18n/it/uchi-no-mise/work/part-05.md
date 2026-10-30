## Capitolo 4: Tecnologia - Un sistema per costruire prodotti da soli, in continuità

Punti chiave di questo capitolo

- Ho trasformato la procedura per lanciare un nuovo prodotto in un documento, in una forma (una skill) che un'IA può leggere ed eseguire. Alle persone spettano soltanto i giudizi e le operazioni che solo le persone possono fare
- Le parti condivise, come accesso, fatturazione, pagine di presentazione e guide ad altri prodotti, si costruiscono una volta e si riutilizzano in tutti i prodotti. Il costo del database di quella base è di circa $35 al mese
- Il sistema è ancora in crescita. Continuo ad aggiungere al documento della procedura gli insuccessi, come un design respinto cinque volte di seguito

(Questo è un capitolo con molti termini tecnici. Se la tecnologia non Le interessa, può passare al capitolo 5 e il filo del discorso non si perde.)

### 4-1 ProductBootstrap: consegnare all'IA la stessa procedura di lancio

Ogni volta che costruivo un prodotto, ripetevo gli stessi preparativi e gli stessi errori. Creare un repository (un deposito per i programmi). Collegare l'accesso. Decidere i colori del design. Impostare il sistema di test. Preparare l'ambiente di produzione. Di sicuro avevo fatto tutto per il prodotto precedente, ma avevo dimenticato i dettagli e inciampavo negli stessi punti.

Così ho trasformato in un documento la procedura per lanciare un nuovo prodotto. Una forma di essa che l'IA che scrive codice (Claude Code) può leggere ed eseguire è ciò che chiamo una «skill». Il nome di questa skill è ProductBootstrap. «Bootstrap» è un termine comune nel mondo dei computer per avviarsi da soli a partire da un meccanismo minimo, e l'ho applicato al lancio dei prodotti.

Non tengo alcun programma modello. Copio il prodotto completato più di recente e avvio da quello il nuovo prodotto. In questo modo le lezioni più recenti passano automaticamente al prodotto successivo. E non serve nemmeno continuare a mantenere un vecchio modello.

#### Il flusso della procedura

1. Consegnare il documento dei requisiti. Se i campi richiesti (nome del prodotto, che cosa fa, chi lo usa, prezzo, unità di prezzo, colore identificativo, posizione del design originale e così via) sono lasciati in bianco, l'IA non parte. La regola è che non pone domande al titolare in corso d'opera. Se non c'è tutto fin dall'inizio, non comincia
2. Decidere il colore del prodotto. Ogni prodotto della serie Agenda ha un colore identificativo. L'IA misura i colori dei prodotti esistenti, propone circa quattro candidati che non si sovrappongano e il titolare sceglie
3. Fissare il design. Faccio creare a un'IA di design (Claude Design) proposte per le schermate. L'IA esegue la propria verifica fino a tre giri, e al titolare vengono mostrate solo le proposte che superano la verifica
4. Lasciare l'implementazione all'IA fino alla fine. L'IA costruisce e corregge da sola finché non rispetta le condizioni di accettazione stabilite (controlli dei tipi, controlli dello stile, tutti i test verdi, superamento di ogni controllo delle schermate e modifiche al database che passano senza intoppi nell'ambiente di test)
5. Il titolare approva soltanto quando si va in produzione. Tutto fino all'ambiente di test procede senza sorveglianza e il titolare giudica solo l'operazione in produzione

Ho costruito la fase di implementazione in modo che non si fermi a metà ad aspettare l'approvazione del titolare. All'inizio procedevo chiedendo l'approvazione a ogni fase, ma così niente andava avanti. Quando ci sono più finestre di lavoro dell'IA, ciascuna si ferma in attesa di approvazione, e il titolare deve fare il giro di tutte le finestre a dare giudizi. Così ho cambiato: consegno in anticipo l'ambito già approvato e le condizioni di accettazione che una macchina può giudicare, e si ferma solo in caso di fallimento.

Sono fissate anche le condizioni di arresto. Quando il documento della procedura e il giudizio del titolare sono in conflitto. Quando diventa necessaria un'operazione che solo una persona può fare. Quando non riesce ad avanzare per tre volte di seguito sullo stesso errore. Quando l'autenticazione decade, i permessi sono insufficienti o serve un'operazione irreversibile. Altrimenti l'IA procede da sola. Lo stato del lavoro è registrato in un piccolo file, così anche se si interrompe a metà può riprendere da lì.

#### Le persone fanno solo due cose

Nel documento della procedura ho scritto questo: l'IA esegue ogni passaggio. Al titolare si possono chiedere soltanto le due cose seguenti.

- Il giudizio in sé. Approvare, decidere, scegliere quale delle due opzioni prendere
- Le operazioni che solo una persona può fare. Chiavi che si possono emettere solo dalla schermata di amministrazione di un servizio esterno, richieste che comportano la verifica dell'identità, operazioni su un dispositivo reale e giudizio visivo

Se l'IA consegna qualunque altra cosa al titolare, è una violazione del documento della procedura. Nella tabella della procedura ho aggiunto a ogni riga una colonna «esecutore» e ogni riga in cui la voce del titolare non può indicare un motivo viene spostata dalla parte dell'IA.

Avevo un motivo per fare questa regola. Quando ho riordinato il lavoro rimanente per un prodotto, l'IA ha messo in fila «creare il progetto del server», «registrare la destinazione dell'accesso», «inserire le variabili d'ambiente» e «costruire l'ambiente di test», tutte come compiti del titolare. Erano tutte operazioni che l'IA poteva eseguire da sé. «Perché devo farlo io?» è stata la mia reazione sincera di allora. L'IA le fa da sé se le si chiede. Ma se non le si chiede, le passa a una persona. Per questo ho dovuto scriverlo nel documento della procedura.

Ho messo nella lista di controllo di questo documento della procedura tutti gli insuccessi del sistema di prenotazione che ho descritto nel capitolo 2. Mettere prima i test. Non tenere dati di produzione nell'ambiente di sviluppo. Costruire prima l'ambiente di test. Il prodotto successivo evita fin dall'inizio gli stessi dolori.

#### Ancora in crescita

Questo documento della procedura non è un prodotto finito. È qualcosa a cui continuo ad aggiungere ogni volta che qualcosa fallisce.

Per esempio, c'è stata una volta in cui ho fatto creare all'IA di design la schermata di un prodotto cinque volte di seguito, e tutte e cinque sono state respinte. Questo include i giri in cui le ho consegnato le regole di design di tutta la serie (DESIGN.md).

All'inizio l'IA ha diagnosticato come causa «la combinazione di colori in sé». L'ho negato. Le cause reali erano due. Una era che venivano usati liberamente colori senza definizione nelle regole. L'altra era che tre sezioni con ruoli diversi erano impilate in verticale con lo stesso colore di sfondo e gli stessi margini, senza un confine tra loro. Nessuna regola era stata violata, eppure i ruoli erano scomparsi dall'aspetto.

Così ho aggiunto clausole alle regole di design. Non dare lo stesso aspetto a cose con ruoli diversi. Non separarle solo con il colore. La cosa più importante viene per prima nella linea dello sguardo. Solo cose davvero uguali possono essere allineate con lo stesso peso. Non fare un'impaginazione che si limita a impilare le cose in verticale.

C'è stata un'altra lezione dall'insuccesso. Se si trasmette l'«aspetto predefinito da evitare» solo come elenco di divieti, l'IA oscilla completamente verso un altro aspetto predefinito che non è nell'elenco. Quando ho vietato in un colpo solo schede, ombre e angoli arrotondati, è tornata una schermata da giornale, fatta solo di linee e margini. Da allora faccio scrivere i materiali della richiesta in tre colonne: «lo schema da evitare», «ciò che volevo vietare» e «che cosa fare invece».

Ho cambiato anche, a metà strada, il modo di decidere i colori identificativi. Quando i prodotti hanno superato gli otto, la gamma dei colori scuri era riempita dai prodotti esistenti, e il nono prodotto e i successivi non potevano più ottenere un colore scuro per linee e pulsanti senza scontrarsi con quelli esistenti. Così ho rivisto la regola: il colore identificativo di un prodotto si usa solo per i colori chiari delle superfici, mentre linee, filetti, icone e pulsanti principali sono tutti unificati nel colore d'inchiostro condiviso della serie. Era un vincolo che è emerso con chiarezza solo quando i prodotti si sono moltiplicati.

Ogni volta che qualcosa fallisce, correggo il documento della procedura. Il prodotto successivo diventa più facile di altrettanto. Credo che far crescere il documento della procedura sia il miglior investimento per continuare a costruire prodotti da soli.

【Figura 4-2】Le fasi della procedura di lancio e chi le esegue (l'IA o il titolare) *(La schermata è in giapponese.)*

【Figura 4-3】I colori identificativi della serie Agenda. Un colore per prodotto, usato solo sulle superfici *(La schermata è in giapponese.)*

### 4-2 AgendaHub: l'ingresso

Man mano che i prodotti si moltiplicano, si finisce per costruire le stesse cose più e più volte. Accesso, fatturazione, pagine di presentazione, guide ad altri prodotti. Per gestire tutto questo senza aiuti, bisogna costruire le parti condivise una volta e riutilizzarle in tutti i prodotti.

AgendaHub è il luogo in cui queste parti condivise sono raccolte. Lo chiamo l'«ingresso».

Prima di tutto, è la porta che da un unico indirizzo instrada verso ogni prodotto. Sotto un unico dominio, bontallc.com, sono allineati gli ingressi di ciascun prodotto: /agendatimbro, /agendaoro, /agendaluce. Ai clienti sembra che i prodotti stiano dentro un unico sito, ma in realtà dietro ciascuno gira un programma separato.

Poi, è il luogo in cui sono collocate le pagine di presentazione dei prodotti. C'è una pagina di presentazione della serie e al suo interno una sezione per ciascun prodotto. Ogni sezione contiene il nome del prodotto e il suo soprannome, il prezzo, un problema espresso con le parole del titolare che comincia con «Quando...», una descrizione di ciò che sa fare e un collegamento alla pagina di dettaglio. Quando rilascio un nuovo prodotto, l'aggiunta di questa sezione è compresa nella procedura di lancio.

Ed è la casa delle regole di design e delle procedure di lancio. L'originale dei colori identificativi, le regole delle schermate (DESIGN.md), la skill ProductBootstrap che ho descritto in 4-1, la skill che controlla le schermate e la skill che compie in sicurezza le modifiche al database. Per ogni regola che attraversa la serie, il contenuto reale sta qui e ogni prodotto lo legge per riferimento.

【Figura 4-1】La struttura della serie Agenda. Dall'ingresso (AgendaHub) a ciascun taccuino, e ogni taccuino si collega a un unico account (AgendaID) *(La schermata è in giapponese.)*

### 4-3 AgendaID: account e fatturazione condivisi

AgendaID è il sistema condiviso della serie per gli account e la fatturazione.

Un titolare che accede una volta con un account Google può usare ogni prodotto. Non serve creare un account per ciascun prodotto. Ho in programma anche di riportare, prima o poi, le impostazioni della lingua da un prodotto all'altro.

Anche la fatturazione è un unico sistema. Invece di costruire per ogni prodotto il collegamento al servizio di pagamento (Stripe), se ne fa carico tutto AgendaID. Ci sono quattro categorie di prezzo: un prodotto leggero a ¥300 (circa $2) al mese, un prodotto a consumo, un prodotto con acquisto una tantum a ¥600 (circa $4) e un prodotto gratuito. I prodotti a pagamento hanno un periodo gratuito di tre mesi senza registrazione della carta, utilizzabile una volta per ciascuna combinazione di locale e prodotto. C'è anche un meccanismo che aggiunge tre mesi di periodo gratuito a chi presenta e a chi è presentato.

Prima che finisca il periodo gratuito arrivano email di avviso sette giorni e un giorno prima. Queste email le avevo costruite dapprima dentro Timbrature, ma man mano che i prodotti si moltiplicavano ho capito che era uno spreco dare a ogni prodotto lo stesso meccanismo, quindi le ho consolidate dal lato di AgendaID.

#### Disdetta e cancellazione anche sotto regole condivise

C'è una parte poco appariscente ma importante: la disdetta e la cancellazione dei dati.

Quando un cliente disdice, quali dati vengono cancellati e quando? Se lo si costruisce separatamente per ogni prodotto, di sicuro da qualche parte si perde qualcosa. Per di più, la serie Agenda include prodotti che trattano dati particolarmente sensibili, come quello che identifica i clienti abituali con il riconoscimento facciale.

Così ho diviso la granularità della cancellazione in quattro livelli e ne ho fatto una regola condivisa nella serie. Sono: disdire un prodotto, eliminare un locale, chiudere un account (uscire da tutta la serie) e una richiesta di cancellazione da parte di un singolo collaboratore. I livelli superiori si propagano a quelli inferiori e ogni prodotto registra presso il sistema condiviso la propria procedura di cancellazione dei dati. Il periodo di tolleranza per la cancellazione è di 30 giorni e in quel tempo si può annullare.

A questo si accompagna un asse temporale. I registri delle presenze, per esempio, per legge devono essere conservati per cinque anni. Anche se un ex collaboratore chiede la cancellazione, entro il periodo di conservazione il registro va tenuto, con i nomi e simili resi anonimi, anziché cancellato fisicamente. Dovevo decidere il confine tra «cancellare» e «conservare» verificandolo con la legge.

#### Un accesso di prova per evitare che l'IA contamini la produzione

Ho aggiunto ad AgendaID un altro meccanismo, per l'IA: un ingresso di accesso di prova.

Perché l'IA verifichi che le cose funzionano, l'IA deve accedere e usare le schermate. Ma l'accesso si fa con un account Google, quindi l'IA non può accedere da sola. E non posso nemmeno consegnare all'IA l'account del titolare. C'è il pericolo che i test dell'IA contaminino i dati di produzione.

Così ho costruito un ingresso che emette account sintetici (persone fittizie) utilizzabili solo nell'ambiente di test. In produzione non funziona. Il database dell'ambiente di test è un progetto separato dalla produzione e contiene solo dati sintetici. L'IA accede da questo ingresso, usa le schermate e conferma che le cose funzionano. Gli account di prova vengono ricostruiti ogni giorno e quelli vecchi vengono cancellati.

In questo modo l'IA può eseguire da sola anche il controllo finale, in un ambiente costruito esattamente come la produzione, senza toccare la produzione.

### 4-4 La navigazione comune e il fallimento della parola «ingresso»

Perché gli utenti possano passare da qualsiasi prodotto agli altri, ho dato a ogni prodotto un menu di navigazione condiviso. È il percorso che permette al titolare di un bar che usa Timbrature di fare una domanda nella Guida al Supporto o di andare a vedere gli altri taccuini.

Dietro questa navigazione condivisa c'è una piccola storia di fallimento.

Nella prima versione avevo collocato un collegamento che diceva «Torna all'ingresso». Era perché, internamente, chiamavo AgendaHub l'«ingresso». Ma quando ho controllato su un dispositivo reale, qualcosa non andava. Due collegamenti, «Torna all'ingresso» e «Vedi la serie Agenda», portavano nello stesso posto. In più, il collegamento al supporto stava sopra il menu del lavoro quotidiano, quindi l'ordine di importanza era rovesciato. E soprattutto, la parola «ingresso» non significa nulla per un titolare che usa il prodotto per la prima volta. Era il linguaggio interno di chi lo ha fatto.

Così ho rimesso a punto i principi. Ordinare le voci in base alla vicinanza allo scopo dell'utente: il lavoro quotidiano in cima, i collegamenti che portano all'esterno in fondo. Anche un collegamento pensato per conquistare nuovi utenti non va mai sopra il lavoro. Il confine deve poter essere spiegato con una sola riga. Scrivere le formulazioni nel linguaggio dell'utente, non in quello interno. Non mettere mai più di un collegamento che porta nello stesso posto. Ho scartato «Torna all'ingresso» e ho unito tutto in un unico collegamento, «Vedi gli altri taccuini Agenda».

Nel capitolo 2 ho scritto dell'imparare il linguaggio dell'interfaccia. Quello era il linguaggio che il titolare usa per parlare con l'IA. Questo è il contrario: il linguaggio che chi costruisce usa per parlare con l'utente. In entrambi i casi si trattava di adattare le proprie parole alla persona a cui si parla.

【Figura 4-4】La navigazione condivisa dopo la correzione. Il lavoro è in cima e i collegamenti che portano all'esterno sono in fondo *(La schermata è in giapponese.)*

### 4-5 La base costa $35 al mese

Il costo del database dell'intera base descritta in questo capitolo è di circa $35 al mese. Il piano a pagamento che include il progetto di produzione costa $25 e il progetto per l'ambiente di test $10.

Anche questa non era la cifra dall'inizio. A un certo punto pagavo $45 al mese. Il database di sviluppo di un prodotto di riconoscimento facciale veniva ancora fatturato anche se non lo usavo. L'ho spostato sul livello gratuito e l'ho fermato, ho eliminato un altro progetto che non usavo e così si è arrivati alla cifra attuale.

Tengo d'occhio anche il costo dell'IA. Il lavoro dell'IA che scrive programmi viene fatturato in base alla quantità di token (l'unità di testo che l'IA legge e scrive). Evito di concentrare i costi facendo in modo che la finestra di lavoro si attenga al ruolo di coordinatore e lasciando l'implementazione vera e propria a un'altra IA con un proprio budget separato. Anche per il modello generativo della finestra di chat guardo il prezzo e scelgo ciò che è necessario e sufficiente. Anche se un modello di livello superiore costasse solo $1 in più al mese, scelgo chiedendomi «basta?».

Se si costruisce in piccolo, anche poche vendite possono bastare a sostenere l'attività. Il discorso sulla monetizzazione del capitolo 3 si regge proprio sulla ridotta spesa di questa base.

### 4-6 L'IA di coordinamento e la persona che decide

Infine, descrivo la forma della mia giornata di lavoro.

Tengo aperte più finestre di lavoro dell'IA contemporaneamente. C'è una finestra per il sistema di prenotazione, una finestra per ciascun prodotto e una finestra di coordinamento che invia loro le istruzioni e raccoglie i risultati. Ho chiamato la finestra di coordinamento AgendaRegia (il taccuino di regia).

A prendere le decisioni, cioè a stabilire da che parte andare, siamo io e l'IA dal lato della chat. L'IA dal lato della chat trova in anticipo lacune e contraddizioni nelle specifiche, allega a ciascuna una decisione predefinita e le propone tutte insieme. Io le leggo e decido. Ciò che è deciso viene raccolto in un foglio di istruzioni chiamato Goal e incollato nella finestra di lavoro. Comprende approvazioni anticipate e condizioni di superamento che una macchina può giudicare. La finestra di lavoro lo legge e prosegue fino in fondo, fermandosi solo quando qualcosa fallisce.

Faccio includere nel foglio di istruzioni anche una stima di quando il lavoro sarà finito. Incastro questo lavoro tra gli orari di apertura del bar, quindi se non so quanto tempo richiederà qualcosa, non posso pianificare la giornata.

Il ruolo del titolare non è leggere, ma decidere. Non ho bisogno di leggere tutti i 1.775 registri di conversazione. Rispondo alle domande sui fatti del bar. Decido sulle cose che solo la politica del bar può decidere. Dopo che qualcosa va online, lo tocco di persona cinque o sei volte per controllare se qualcosa stona. Tutto qui.

Prima di arrivare a questa forma ho rifatto il lavoro molte volte. L'IA aggiungeva funzioni da sola e le schermate diventavano instabili. Il lavoro cresceva senza limite a partire da una sola istruzione. Aspettare l'approvazione a ogni fase significava che niente andava avanti. Ogni volta aggiungevo una regola, ed è così che si è arrivati alla forma attuale. Anche questa è ancora in crescita.

#### Che cosa si può portare via da questo capitolo

- Per il lavoro ripetuto, trasformare la procedura stessa in un documento e consegnarla all'IA. Se si corregge il manuale ogni volta che fallisce, la volta successiva diventa più facile
- Costruire una sola volta le parti comuni (accesso, fatturazione, navigazione) e riutilizzarle in tutti i prodotti. Se la base è piccola, anche poche vendite possono bastare
- Alle persone spettano soltanto il giudizio e le operazioni che solo le persone possono fare. Se l'IA consegna qualunque altra cosa, aggiungerla al manuale

Il seguito di questo capitolo (i prossimi taccuini che costruisco e le lezioni che ho aggiunto al manuale) è su note e su X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
