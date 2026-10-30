### 1-5 In cifre: circa l'88% delle prenotazioni è per lo stesso giorno

Mentre continuavo ad aggiungere meccanismi, ho notato una cosa. Non riuscivo a capire quali funzionassero.

Così ho contato i dati delle prenotazioni. Delle 244 prenotazioni degli ultimi 90 giorni, 215 erano per lo stesso giorno. Cioè l'88,1%. La media è di 2,71 prenotazioni al giorno.

Tamuro non era un posto per cui si prenota, ma un posto in cui si viene d'impulso. È emerso con chiarezza solo quando l'ho messo in numeri.

Da questi numeri sono diventate visibili due cose.

La prima è come costruire il modulo di prenotazione. Se la maggior parte delle prenotazioni è per lo stesso giorno, è più comodo che all'apertura della schermata di prenotazione sia già selezionata la fascia libera più vicina di oggi. D'altra parte, alcune persone che vogliono prenotare per una data successiva la invieranno distrattamente come oggi. Così ho fatto risaltare oggi sul calendario e, nella schermata di conferma, mostro la data e l'ora in grande con «Oggi». Ho mantenuto la comodità di scegliere lo stesso giorno e ho reso facile accorgersi degli errori.

L'altra è il significato dello sconto per chi prenota in anticipo. Tante prenotazioni dello stesso giorno significano che non possiamo prevedere le vendite future. Basta il maltempo per far calare l'affluenza. Per aumentare anche solo un po' le prenotazioni anticipate, più persone devono usare lo sconto anticipato. Questa consapevolezza ha portato più tardi alla storia della costruzione di un'IA che pubblica al posto del titolare.

Per guardare i numeri serve un sistema per contare. Il sito di prenotazione non aveva alcuna analisi degli accessi. Non sapevo quante persone arrivassero alla pagina di prenotazione, quante abbandonassero a metà e quante finissero. Così ho aggiunto un sistema che conta tre fasi: arrivo alla pagina, decisione dei dettagli, prenotazione conclusa. Non registra chi è venuto, solo la fase e l'ora.

Ancora più tardi ho costruito anche un sistema che invia via email un rapporto settimanale che riassume i numeri delle prenotazioni. Descriverò come è nato nel paragrafo 1-7.

【Figura 1-3a】Oggi risalta sul calendario *(La schermata è in giapponese.)*

【Figura 1-3b】Nella schermata di conferma, la data e l'ora compaiono in grande con «Oggi» *(La schermata è in giapponese.)*

### 1-6 Troppi piani tra cui scegliere

Una volta messo in funzione il sistema di sconti, volevo poi aumentare le fasce orarie e i piani che si vendono.

La fascia delle 18 non si riempiva, così ho creato un happy hour fino alle 19. Per chi viene dopo aver mangiato, ho creato un piano di solo bere, senza pasto. Il percorso a menu fisso e il corso di cucina, che un tempo si tenevano ogni mese, li ho trasformati in eventi su richiesta che si aprono quando qualcuno si iscrive, raccolti tramite il sito di prenotazione. Per vendere il tempo prima dell'apertura nei fine settimana, dalle 15:30, ho creato un piano festa per gruppi di sei o più persone.

Ognuno ha una ragione. Il piano festa, per esempio: se l'avessi fatto sembrare un affare sul prezzo, avrebbe attirato soltanto i clienti che sceglievano il piano standard, e le vendite sarebbero calate. Così ho collocato la differenziazione non sul prezzo ma sulle ore prima dell'apertura, che non avevano mai portato alcuna vendita. Lo sconto dell'happy hour non dà profitto se combinato con altri sconti, quindi ho deciso che non è cumulabile.

E così i piani si sono moltiplicati. Standard, Premium, Piacere di conoscerci, Bentornato, Happy Hour, Solo bere, Percorso a menu fisso, Corso di cucina, Festa. Ognuno ha condizioni sul numero di persone, alcuni accettano sconti e altri no, e ci sono limiti di orario.

Un giorno ho aperto il modulo di prenotazione e ho capito: i clienti con questo non riescono a scegliere.

Io, che l'ho costruito, capisco tutte le differenze. Ma chi apre il sito di prenotazione per la prima volta riesce a confrontare nove piani e le loro condizioni di sconto e a scegliere quello che fa per sé? Se non ci riesce, rinuncia a metà della prenotazione. I piani che avevo faticato ad aggiungere potevano finire per ridurre le prenotazioni.

Avrei potuto mettere ordine. Ma ogni piano ha una fascia oraria che voglio vendere e un cliente che voglio vedere. Non volevo eliminarne nessuno.

Così ho pensato a un sistema in cui il cliente si consulta con l'IA e decide un piano. Si indicano il numero di persone, la data e l'ora in cui si vorrebbe venire e come si vuole godere la serata, e l'IA fornisce il piano e il prezzo adatti e porta direttamente alla prenotazione. Il locale si fa carico della complessità dei piani. Al cliente resta soltanto una conversazione.

Questo sistema è il «T-AI-MURO» di cui scrivo in 1-8. Prima, c'è ancora una cosa di cui mi sono accorto in questo periodo.

【Figura 1-2】La scelta del piano nel modulo di prenotazione. Ci sono tutte queste schede in fila *(La schermata è in giapponese.)*

### 1-7 «Ma questo porta davvero clienti?»

Il giorno in cui ho aggiunto il piano festa, ho passato l'intera giornata a fare un miglioramento dopo l'altro al sito di prenotazione. Ho sistemato l'intestazione, ho uniformato il design delle email e ho sostituito l'IA che crea gli argomenti di conversazione per i clienti nel locale.

La sera mi è venuta all'improvviso una domanda.

«Ma questo aiuta davvero a portare più clienti?»

Quando l'ho chiesto all'IA, ha classificato con onestà i miglioramenti di quel giorno.

| Categoria | I miglioramenti di quel giorno |
| --- | --- |
| Cose che possono creare nuove prenotazioni | Piano festa, la fascia delle 15:30 nei fine settimana e nei festivi |
| Cose che alzano il tasso di completamento per chi è arrivato | Sistemazione dell'intestazione, allineamento delle schede |
| Cose che incoraggiano le visite di ritorno | Uniformare il design delle email |
| Cose che non aiutano a portare clienti | Cambio dell'IA che crea gli argomenti di conversazione, il collegamento alla tappa successiva, l'avviso di Agenda |

Di tutti i miglioramenti di quel giorno, solo il piano festa e la fascia delle 15:30 portavano direttamente clienti. Il resto erano miglioramenti per non perdere le persone già arrivate. Contano anche quelli, ma non aumentano i clienti.

C'era un problema più grande. Per nessuno dei miglioramenti avevo un modo di misurare se avesse funzionato. Non c'era un numero che collegasse «ho migliorato» e «i clienti sono aumentati».

La mia risposta è stata una frase: «Costruiamone uno».

Così ho iniziato a creare un rapporto settimanale di acquisizione clienti. Il numero di prenotazioni, il numero di ospiti, l'importo totale, le cancellazioni. Ripartizioni per giorno della settimana e per fascia oraria. Il rapporto tra clienti alla prima visita e clienti di ritorno. I conteggi delle fasce di festa e delle 15:30. Da dove arrivano le prenotazioni (il modulo di prenotazione, la finestra di chat, le prenotazioni dall'IA, gli inserimenti manuali del locale). I conteggi dei clic sulle email e il numero di prenotazioni entro sette giorni da quei clic.

Ai numeri si legano sempre questioni di tempo. Lo stesso giorno avevo trovato un altro buco. Avevo impostato il corso di cucina e la fascia delle 15:30 della festa come «fine settimana», ma quando mi sono chiesto «Che cosa succede nei giorni festivi?» e ho verificato, il sistema di prenotazione non aveva alcun concetto di giorni festivi. In un lunedì festivo il locale è aperto, eppure la fascia delle 15:30 non compariva. Gli ho dato un elenco dei giorni festivi e l'ho corretto perché li trattasse come i fine settimana. Era un buco di cui nessuno si sarebbe accorto prima di chi l'ha costruito.

Prima di costruire il rapporto, ho tappato per prima cosa i buchi legati al tempo.

Anche i clienti abituali che venivano da prima che iniziassi a usare il sistema di prenotazione appaiono come «clienti alla prima visita» nei registri. Così nel rapporto scrivo «prima visita registrata» e allego sempre la data in cui sono iniziati i registri. Per giudicare se un miglioramento ha funzionato serve il quadro precedente. Per il primo rapporto ho fatto i conteggi retrospettivi delle ultime otto settimane e li ho usati come riferimento. In una settimana in cui il locale ha chiuso temporaneamente, per un viaggio o altri motivi, le prenotazioni calano naturalmente. Così elenco anche il numero dei giorni di attività, in modo da poter fare i confronti per giorno di attività.

Per la sezione «Cambiamenti rilevanti», invece di farla scrivere all'IA, ho deciso di compilarla con calcoli e frasi prefissati. Serve a mantenere a zero il costo settimanale. Nomi e recapiti dei clienti non compaiono nel rapporto; si mostrano solo conteggi e percentuali.

Una volta costruito un modo di misurare, è cambiato il modo stesso in cui costruisco i miglioramenti. Ho cominciato a decidere fin dall'inizio, insieme, un miglioramento e il metodo per misurarne l'effetto. La misurazione non è una cosa a cui pensare dopo un miglioramento; va nello stesso documento di istruzioni del miglioramento. È quello che ho imparato quel giorno.

【Figura 1-6】Il rapporto settimanale di acquisizione clienti che arriva ogni settimana (dati sintetici) *(La schermata è in giapponese.)*

### 1-8 Una finestra che parla con il locale: «T-AI-MURO»

Come ho scritto in 1-6, i piani si erano moltiplicati e il modulo di prenotazione era diventato difficile da scegliere per chi viene per la prima volta. E i clienti alla prima visita vogliono sapere più dei piani e delle date. Che atmosfera ha il posto? Mi sentirò fuori posto se vengo senza compagnia? Che tipo di persona è il titolare? Si possono portare bambini? Se si allineano pulsanti di prenotazione senza rispondere a domande come queste, non si può dare la spinta necessaria a chi esita.

Così ho deciso di mettere sul sito di prenotazione una «finestra che parla con il locale». Quando un cliente scrive una domanda, l'IA risponde a nome del locale. Se durante la conversazione si stabiliscono il numero di persone e la data, il cliente può andare direttamente alla schermata di conferma della prenotazione. Si chiama «T-AI-MURO» e nella conversazione si presenta come «Tamuro». T-AI-MURO parla come il locale stesso e si riferisce al titolare in terza persona.

I clienti non scrivono quasi nulla. Toccano soltanto le scelte che T-AI-MURO propone, e la conversazione va avanti. Questo significa che le scelte che propone subito dopo decidono la qualità della conversazione. Nelle scelte mescolo sempre tre tipi di mosse: mosse verso una prenotazione (numero di persone, prezzo, fasce libere, data e ora), mosse verso la conoscenza del locale (atmosfera, il titolare, chi sono i clienti, se si può parlare con la persona accanto) e mosse che nascono dal flusso della conversazione. Portare le persone alla prenotazione non è l'unico obiettivo. Far conoscere l'atmosfera del locale e il titolare è anch'esso il cuore di questa finestra.

Solo i prezzi, ho deciso, non li avrebbe calcolati l'IA. Non c'è garanzia che l'IA sappia calcolare correttamente, ogni singola volta, come si sommano gli sconti o come si applicano i gradini per numero di persone. Il programma produce prezzi e fasce libere con calcoli fissi, e l'IA si attiene al compito di metterli in parole.

#### La prima conoscenza è venuta dai miei vecchi post

Perché T-AI-MURO possa rispondere alle domande sul locale, ha bisogno di conoscere il locale. Come materiale ho esportato e usato tutti i post che avevo scritto fino ad allora su Instagram e X (già Twitter). Da quelli ho costruito le domande che i clienti probabilmente avrebbero fatto e le risposte.

Quando l'ho provato davvero, i post di X si sono rivelati più utili di Instagram come materiale. Instagram è per lo più fatto di foto, con poche parole. Su X avevo lasciato testimonianze scritte, con parole mie, sul cibo, sul locale e su ciò che pensavo.

#### Solo 9 su 36 hanno superato la prova

Prima di mettere in produzione T-AI-MURO, ho verificato con quanta correttezza sapesse rispondere. Anche i test li ho fatti eseguire all'IA. Ho dato a un'IA che faceva la parte del cliente un personaggio e uno scopo, e l'ho fatta conversare con T-AI-MURO. Ho preparato 36 scenari: «una persona stasera», «4 persone tra due settimane», «con un bambino», «allergie», «prenotazione privata», «avviso di ritardo», «l'origine del nome del locale», «che tipo di persona è il titolare» e così via.

Il risultato del primo giro: 9 superati su 36.

La risposta più frequente era «Mi dispiace, non ho saputo rispondere bene». Questa risposta compariva perfino per domande sull'atmosfera del locale e sul titolare. Ogni volta che comparivano parole come «prenotazione», «oggi», «prenotazione privata» o «gestore», saltava fuori un elenco di fasce libere indipendentemente da ciò che la domanda chiedeva davvero. In alcune conversazioni, un messaggio sul ritardo veniva scambiato per una nuova prenotazione. A un cliente vegetariano, dava come esempi piatti saltati con scaglie di bonito e zuppa di miso. Dava perfino in inglese informazioni su un acquisto di gruppo che avevamo già interrotto.

#### Ho risposto a 11 domande con una riga ciascuna

Parte della causa stava nel modo in cui era costruito il programma. Quella storia la rimando al capitolo 2. L'altra causa era semplice: i fatti del locale erano insufficienti. Un'IA non può rispondere a ciò che non sa.

Così ho raccolto le domande a cui l'IA non sapeva rispondere e ho deciso di rispondere di persona, una riga ciascuna.

Si può entrare senza prenotazione. I bambini sotto l'età della scuola elementare sono difficili da accogliere. Cancellazioni e modifiche entro il giorno prima, via email, telefono o messaggio sui social. Per l'avviso di ritardo, si prega di telefonare. C'è una zona fumatori fuori dal locale. Portare le proprie bevande è consentito con un diritto di tappo. La prenotazione privata è possibile a seconda della fascia di prezzo e dell'orario, per un massimo di 19 persone. Per le restrizioni alimentari e gli anniversari ci adeguiamo per quanto possibile, quindi si prega di consultarci prima. Il titolare è nel locale quasi tutti i giorni di attività. Una festa degli yukata è prevista circa una volta all'anno.

Tutto qui. Rispondendo soltanto a 11 domande con una riga ciascuna, nel secondo test 24 su 36 sono stati superati.

| Domanda | Prima risposta | Seconda risposta |
| --- | --- | --- |
| Va bene con i bambini? | Mi dispiace, non ho saputo rispondere bene | Dall'età della scuola elementare in su si può accogliere, consultandoci. Sotto l'età della scuola elementare è difficile |
| Si può entrare senza prenotazione? | (elenco di fasce libere) | Si può entrare senza prenotazione |
| Il gestore c'è oggi? | (elenco di fasce libere) | Il titolare è nel locale quasi tutti i giorni di attività. Oggi è un giorno di attività, quindi è prevista la sua presenza |
| È un posto tranquillo? Tutti habitué? | Mi dispiace, non ho saputo rispondere bene | È un posto in cui rilassarsi. La conversazione tra i clienti viene facile e non è un posto chiassoso |

Qui ha cominciato a delinearsi uno schema. L'IA crea le domande che ci aspettiamo, T-AI-MURO risponde e noi correggiamo gli errori. Poi al titolare passano soltanto le domande a cui non si può rispondere perché mancano i fatti del locale. Il lavoro del titolare è solo una riga per ogni domanda senza risposta. Tutto il resto lo fa girare l'IA.

#### La scena in cui il «budget di ¥5.000 (circa $33)» è fallito

Anche ai test dell'IA avevo aggiunto un giudizio dell'IA. Un'altra IA legge il registro della conversazione e decide se è superato o no.

Tra questi c'era uno scenario con un cliente il cui «budget è di ¥5.000 (circa $33)». Il giudizio dell'IA era: superato. T-AI-MURO aveva presentato con cortesia piani entro il budget.

Ma quando l'ho letto, era un fallimento. Non aveva chiesto il numero di persone. Tamuro ha uno sconto di gruppo. A seconda del numero di persone, i piani che si possono scegliere con lo stesso budget cambiano.

A quel punto ho riformulato lo scopo.

«Punta a gruppi il più numerosi possibile, così da incassare un importo totale più alto. Conferma il numero di persone. L'obiettivo finale è far venire i clienti. Più sono, meglio è. Per aumentare le vendite».

Con quella sola affermazione, l'intera progettazione della conversazione è cambiata. Confermare sempre il numero di persone prima di rispondere sui prezzi e rispondere con l'importo totale. Poco prima di un gradino dello sconto di gruppo, aggiungere «con una persona in più si ottiene il tot% di sconto». Quando viene dato un budget, mostrare per primo il piano migliore entro il budget. Tuttavia i clienti che vengono senza compagnia sono la metà del locale, quindi, per un cliente singolo, non suggerire di aumentare il gruppo.

Quando si fanno eseguire i test all'IA, girano in fretta. Ma è una persona a decidere il criterio per cui si supera. Riuscire o meno a dichiarare lo scopo in una sola frase: era questo a decidere la qualità delle conversazioni dell'IA.

#### I desideri del cliente hanno la precedenza sulle raccomandazioni del locale

C'è stata un'altra scena in cui ho tracciato un confine importante.

Durante i test ho trovato un problema: ogni prenotazione veniva dirottata sul piano più economico. Quando l'ho corretto, stavolta quasi tutte sono diventate del piano Standard, e l'importo totale medio è schizzato a circa il doppio. Stavo quasi per rallegrarmi, ma guardando bene, l'IA che faceva la parte del cliente premeva semplicemente ogni volta la prima scelta. Anche ai clienti che dicevano «va bene il più economico» veniva raccomandato lo Standard.

Qui ho fissato un principio. Ciò che il cliente dichiara chiaramente come desiderio (l'opzione più economica, un budget, il nome di un piano) ha sempre la precedenza sulla raccomandazione del locale. La raccomandazione del locale vale solo quando il cliente non ha detto nulla.

L'obiettivo del locale di aumentare le vendite e la fiducia del cliente possono scontrarsi su un solo modo di raccomandare. Se si perde la fiducia, le visite stesse calano. A poter tracciare questo confine era il titolare, non l'IA.

Più tardi, quando ho riaddestrato T-AI-MURO con un gran numero di domande, la causa più comune degli errori era «reagire alle parole e fare una mossa fissa prima di rispondere alla domanda». Appena sentiva parole come «numero di persone», «quanto costa» o «da solo», saltava la domanda e passava al flusso di prenotazione o alle raccomandazioni. In termini di servizio, è un commesso che spinge la vendita senza ascoltare il cliente. Rispondere prima alla domanda del cliente. Questo principio base dell'accoglienza è stato la sfida più grande perfino per l'IA.

La sera del 6 ottobre 2026, T-AI-MURO è apparso in cima al sito di prenotazione come vero ingresso. Poiché alcuni clienti non vogliono prenotare conversando, ho tenuto accanto il precedente modulo di prenotazione.

> Provare: aprire il sito di prenotazione di Tamuro (https://tamuroreservation.vercel.app/?src=b2-it-{{FMT}}) e chiedere a T-AI-MURO «stasera, una persona». La conversazione porta fino alla disponibilità e ai prezzi di oggi.

【Figura 1-4】La schermata di conversazione di T-AI-MURO. La conversazione procede semplicemente toccando le scelte *(La schermata è in giapponese.)*

【Figura 1-10】Le domande senza risposta si accumulano nella schermata di amministrazione (dati sintetici) *(La schermata è in giapponese.)*

### 1-9 E poi, dall'IA del cliente

Con la costruzione di T-AI-MURO, il sito di prenotazione di Tamuro ha acquisito la capacità di «rispondere in conversazione alle domande sul locale, mostrare prezzi e fasce libere e guidare le persone fino alla prenotazione».

Quello a cui ho pensato dopo è stato rendere possibile la stessa cosa dall'IA dei clienti stessi.

T-AI-MURO può parlare solo con le persone che arrivano al sito di prenotazione di Tamuro. Ma molte persone si consultano prima con l'IA che usano ogni giorno. Se quell'IA non conosce Tamuro, Tamuro non entra nemmeno nell'elenco dei candidati. Invece di aspettare che i clienti arrivino al sito di Tamuro, aprire la finestra di Tamuro dal lato dell'IA del cliente. Questo è il server MCP.

Per essere onesti, all'inizio ho esitato a costruirlo. Al momento non sono ancora molte le persone che prenotano un ristorante dalla propria IA. Giudicando di non poter contare su un aumento diretto delle prenotazioni, una volta ne ho abbassato la priorità e l'ho messo da parte.

Ho deciso di costruirlo comunque perché pensavo che il cambiamento dell'ingresso fosse solo questione di tempo. Come ho scritto all'inizio, ad agosto 2026 è diventato possibile fare prenotazioni da ChatGPT tramite un grande servizio di prenotazione. Prima o poi, far trovare un ristorante all'IA diventerà la norma. Quando accadrà, i piccoli locali che non figurano nei grandi servizi usciranno dalla vista dell'IA. Quindi, aprire la finestra prima che l'ingresso cambi.

Quello che ho deciso per la prima versione era molto limitato. Doveva solo fare le stesse cose della finestra di conversazione sul sito di prenotazione (T-AI-MURO). Tutto ciò che sa fare è leggere le informazioni del locale, le fasce libere e i prezzi, e consegnare l'URL di una pagina di prenotazione con le condizioni già compilate. A confermare la prenotazione è il cliente stesso, sulla pagina di Tamuro. L'IA del cliente non conferma da sola una prenotazione. La spinta finale la dà una persona.

Torniamo alla scena iniziale.

Un venerdì sera, un cliente chiede alla propria IA: «A Higashi-Nakano c'è un posto dove posso fermarmi a bere stasera, anche senza compagnia?» L'IA interroga la finestra di Tamuro. Il sistema di prenotazione di Tamuro restituisce le fasce libere di stasera, più il piano e il prezzo adatti a un cliente singolo. L'IA lo comunica al cliente e propone una pagina di prenotazione di Tamuro con data, ora e numero di persone già compilati.

Tutto ciò di cui ho scritto in questo capitolo sostiene questa serie di passaggi. Il sistema di sconti costruito insieme all'aumento dei prezzi. Il sistema che coltiva i clienti abituali. I dati che mostravano che la maggior parte delle prenotazioni viene fatta nel giorno stesso. La conoscenza del locale cresciuta rispondendo a 11 domande con una riga ciascuna. Il principio di mettere i desideri del cliente davanti alle raccomandazioni del locale.

Un locale che viene prenotato tramite l'IA non è stato costruito in una notte. Poggia sull'accumulo di piccoli sistemi aggiunti uno alla volta, collaudati, scartati e corretti.

> Provare: registrare il server MCP di Tamuro (https://tamuroreservation.vercel.app/api/mcp) nella propria IA e chiedere: «C'è posto da Tamuro stasera?» Come registrarlo è scritto nella Postfazione.

### 1-10 Che cosa abbiamo costruito e che cosa ha funzionato

In questo capitolo ho parlato della costruzione di tanti sistemi. Ma «siamo riusciti a costruirlo» e «l'attività è cambiata» sono cose diverse. Alla fine del capitolo separerò le due.

Ciò che si è potuto confermare con i numeri. Che l'88,1% delle prenotazioni è per lo stesso giorno. Che il tasso di superamento della finestra di conversazione è salito da 9 a 24 solo aggiungendo 11 informazioni concrete sul locale. Che il tasso di superamento per le indicazioni su prezzi e piani è salito dal 29,4% al 42,7% dopo le correzioni. Sono fatti registrati.

Ciò che sembra funzionare, ma di cui non posso dimostrare il nesso causale. Che più clienti vengono in gruppo usando lo sconto di gruppo. Che il piano per chi viene la prima volta o torna dopo tempo viene scelto. Che l'argomento dell'email di conferma è diventato parte della conversazione al bancone. Lo sento in sala, ma non posso dire «non sarebbero venuti senza quel sistema».

Ciò che è stato costruito, ma di cui ancora non conosco l'effetto. Quante prenotazioni anticipate in più porterà lo sconto per chi prenota presto. Quante prenotazioni arriveranno davvero da MCP. Ho appena iniziato a misurare con il rapporto settimanale e i numeri verranno più avanti.

Vanno tenuti distinti lo stupore di «poter costruire così tanto con l'IA» e il risultato di «come ha cambiato l'attività». Senza questa distinzione, costruire diventa l'obiettivo in sé. Una volta ho rischiato di cadervi anch'io (come ho scritto in 1-7).

La storia di ciò che sta dietro questo sistema di prenotazione, la tecnologia, continua nel capitolo 2. Se la tecnologia non Le interessa, passi al capitolo 3. Lì racconto come i piccoli strumenti nati attorno a questo sistema di prenotazione vengono distribuiti anche ad altri locali.
