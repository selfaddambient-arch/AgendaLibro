# Costruito per il nostro bar

Come il titolare di un bar da 19 posti ha costruito con l'IA tutto, dalle prenotazioni agli strumenti

Raku Bonta

La serie Agenda: https://bontallc.com/agenda?via=b2-it-{{FMT}}

Instagram di Tamuro: https://www.instagram.com/tamuro.higashinakano/

Sito di prenotazione di Tamuro: https://tamuroreservation.vercel.app/?src=b2-it-{{FMT}}

## Introduzione

Questo libro è la semplice testimonianza di come il titolare di un bar da 19 posti a Higashi-Nakano *(un quartiere residenziale nella zona occidentale di Tokyo, subito a ovest di Shinjuku)*, a Tokyo, gestisce il locale con l'aiuto dell'IA.

Il bar si chiama «Tamuro». Il nome indica un luogo dove le persone si riuniscono. Ha aperto a novembre 2018, un piccolo spazio con 11 posti al bancone e 8 posti nella sala con tatami. Di giorno, nello stesso spazio, un collaboratore gestisce un ristorante di hamburger al curry (hamburg steak alla giapponese) chiamato «Quatre Épices».

Nel mio libro precedente, *Il vice responsabile IA*, ho scritto dell'IA generativa in sé. Nell'anno circa trascorso da allora, l'IA è passata dall'essere uno strumento che risponde alle domande a uno strumento che porta a termine il lavoro al posto nostro. Le si dà un'istruzione, e scrive il programma, lo collauda, corregge i propri errori e finisce il lavoro. A questo tipo di IA diamo il nome di IA agentica.

Usando l'IA agentica, ho costruito di persona il sistema di prenotazione di Tamuro. Ho costruito un sistema di sconti da affiancare a un aumento dei prezzi. Ho costruito un sistema per coltivare i clienti abituali. Ho costruito un'IA che risponde alle domande dei clienti. E alla fine ho raggiunto il punto in cui un cliente può fare una domanda a Tamuro dalla propria IA e proseguire con una prenotazione.

Ho anche preso gli strumenti pratici che avevo creato per il mio locale, li ho modellati perché potessero servire anche ad altri locali e ho iniziato a offrirli a qualche centinaio di yen al mese. È la serie Agenda.

Questo libro descrive che cosa ho costruito lungo il percorso, in che cosa ho fallito e che cosa ho dovuto imparare di nuovo. Non ci sono solo storie di successo. Continuavo a costruire cose che funzionavano, andando a istinto, e le contraddizioni si accumulavano. Ho scoperto più tardi che i dati personali dei clienti potevano essere letti dall'esterno. L'IA scriveva fatti che il locale non aveva mai dichiarato. Ho incluso questi fallimenti così come sono avvenuti.

### Come leggere questo libro

Questo libro ha cinque capitoli.

| Capitolo | Contenuto | Indicato per |
| --- | --- | --- |
| Capitolo 1 | Un locale prenotato dall'IA (il lato aziendale del sistema di prenotazione) | Tutti |
| Capitolo 2 | Dietro il sistema di prenotazione (tecnico) | Chi costruisce e chi è curioso di tecnologia |
| Capitolo 3 | Distribuire gli strumenti del nostro locale ad altri locali (il lato aziendale della serie Agenda) | Tutti |
| Capitolo 4 | Un sistema per costruire prodotti da soli (tecnico) | Chi costruisce e chi è curioso di tecnologia |
| Capitolo 5 | Il futuro dei piccoli locali | Tutti |

I capitoli 2 e 4 sono tecnici e usano più termini specialistici. Ognuno si apre con un riassunto di tre righe dei punti essenziali, quindi, se la tecnologia non Le interessa, legga solo quelli e passi al capitolo successivo. Leggendo i capitoli 1, 3 e 5 in ordine, il filo del racconto non si perde comunque.

Dove ho potuto, ho aggiunto accanto a ogni termine tecnico una spiegazione in parole semplici. Anche se non ha mai scritto un programma, spero che si faccia un'idea di che cosa significhi gestire un locale con l'IA.

### Chi scrive

Ho lavorato nell'informatica per circa 16 anni, per lo più nella pianificazione dei sistemi e come coordinatore tra le persone sul campo e i fornitori di sviluppo, e poi ho iniziato a lavorare nel settore della ristorazione e delle bevande. Quindi questa non è la storia di una persona che, senza aver mai scritto una riga di codice, ha costruito tutto con la sola IA. Ci tengo a dirlo con onestà.

Eppure ora posso costruire e far funzionare, senza altro aiuto e mentre lavoro in sala, qualcosa di una scala che un tempo richiedeva un team e dei fondi. Qualche anno fa sarebbe stato impensabile. Voglio descrivere nel modo più concreto possibile la realtà di questo cambiamento.

### Come è stato fatto questo libro

Anche questo libro l'ho fatto con l'IA. Partendo dalle registrazioni che tengo durante il lavoro di sviluppo quotidiano, l'IA ha scritto le bozze, e io ho letto, rivisto e preso le decisioni. Ho fatto fare all'IA anche gli screenshot usati come illustrazioni.

Ho letto tutto, ma nei testi scritti dall'IA possono insinuarsi inesattezze. Come dico nel testo principale, l'IA dice «fatto», e controllare spetta a una persona. In questo libro possono esserci errori che mi sono sfuggiti.

Inoltre, le specifiche degli strumenti e dei servizi di IA cambiano nel giro di pochi mesi. I passaggi, i prezzi e lo stato del supporto di ciascuna azienda descritti in questo libro sono aggiornati a ottobre 2026. Quando proverà di persona, controlli le informazioni ufficiali di quel momento.

Se nota un errore, mi farebbe piacere che me lo comunicasse su note o su X. Correggerò man mano che ne verrò a conoscenza.

### Le tre uscite di questo libro

Questo libro si può leggere gratuitamente in PDF, su note e su Google Play. (Solo su Kindle, le regole dello store richiedono un prezzo minimo.) In cambio, ho preparato tre posti in cui andare dopo aver finito di leggere. Se anche uno solo Le è utile, scrivere questo libro sarà valsa la pena.

1. Provare nel proprio locale. Con la serie Agenda si può iniziare con il taccuino gratuito. https://bontallc.com/agenda?via=b2-it-{{FMT}}
2. Seguire quello che faccio. Scrivo su note e su X dei prossimi strumenti che costruisco e della vita quotidiana nel locale. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Se capita di passare per Tokyo, venire a Tamuro. A un minuto dall'uscita est della stazione di Higashi-Nakano. Si può entrare senza prenotazione. Sito di prenotazione https://tamuroreservation.vercel.app/?src=b2-it-{{FMT}}

## Capitolo 1: Un locale prenotato dall'IA

### 1-1 «C'è qualche posto aperto stasera?» Lo si chiede all'IA

Un venerdì sera, chi ha appena finito di lavorare parla con il proprio smartphone.

«A Higashi-Nakano c'è un posto dove posso fermarmi a bere stasera, anche senza compagnia? Un posto non troppo rumoroso».

A rispondere non è un amico. È l'IA che quella persona usa ogni giorno. L'IA elenca i locali candidati, descrive l'atmosfera di ciascuno e comunica gli orari liberi e i prezzi di stasera. Se qualcosa attira l'attenzione, si può andare direttamente alla schermata di prenotazione.

Questa non è una storia del futuro.

Il 10 agosto 2026, OpenAI ha aggiunto a ChatGPT una funzione di prenotazione nei ristoranti. Secondo le note di rilascio ufficiali, si collega ai servizi di prenotazione OpenTable, Resy e Yelp, e gli orari disponibili compaiono direttamente nelle risposte di ChatGPT. Si possono anche fare domande per restringere le opzioni e, una volta scelto un orario adatto, passare subito a prenotare. Copre OpenTable in tutto il mondo, Resy negli Stati Uniti e Yelp negli Stati Uniti e in Canada.

In altre parole, l'ingresso che le persone usano per trovare un posto dove mangiare comincia a spostarsi dai motori di ricerca e dai siti di recensioni dei ristoranti alla «mia IA».

Ma c'è una condizione. Gli unici locali che si possono prenotare tramite ChatGPT sono quelli registrati presso i grandi servizi di prenotazione. I piccoli locali che non vi figurano sono invisibili all'IA.

E allora che cosa deve fare un bar da 19 posti a Higashi-Nakano che non usa i grandi servizi di prenotazione?

Tamuro ha scelto un'altra strada. Senza passare per i grandi servizi, ha collegato direttamente il proprio sistema di prenotazione all'IA.

Quando un cliente chiede al proprio ChatGPT o Claude: «C'è posto da Tamuro stasera?», l'IA interroga direttamente il sistema di prenotazione di Tamuro, controlla gli orari liberi e i prezzi e risponde. Una volta stabilite le condizioni, indirizza il cliente alla pagina di prenotazione di Tamuro con il numero di persone, la data e l'ora già compilati. Il pulsante finale di conferma lo preme il cliente stesso.

Questo «punto di collegamento tra l'IA e il sistema di un locale» si chiama server MCP. MCP sta per Model Context Protocol, un insieme comune di accordi che permette all'IA di usare strumenti e dati esterni. Ne spiego i dettagli nel capitolo 2.

In realtà anche i grandi servizi di prenotazione, alla fine, passano i clienti alle proprie schermate. Per le prenotazioni che richiedono una carta di credito, la procedura si conclude sulla schermata di OpenTable, e le modifiche o le cancellazioni dopo la prenotazione vengono gestite da ciascun servizio. L'IA è l'ingresso, e la schermata del servizio di prenotazione è il luogo in cui si conferma. Ciò che fa Tamuro ha la stessa struttura. L'unica differenza è che in mezzo non c'è nessuna grande azienda.

E a costruire questo sistema non è stata una società di sviluppo esterna. L'ho costruito io, il titolare. Ho dato istruzioni all'IA, le ho fatto scrivere i programmi e le ho fatto eseguire i test.

Naturalmente, all'inizio non ero a questo punto. Tutto è cominciato con un modulo di prenotazione semplicissimo. Poi è venuto un aumento dei prezzi, poi le idee per gli sconti, poi un sistema per coltivare i clienti abituali, poi i fallimenti e la ricostruzione.

Descrivo prima, in cinque righe, che tipo di posto è Tamuro. A un minuto a piedi dall'uscita est della stazione di Higashi-Nakano. 19 posti, 11 al bancone e 8 nella sala con tatami. Circa metà dei clienti arriva senza compagnia, e il bancone rende facile iniziare a chiacchierare con chi è seduto accanto. Il cibo è una combinazione di quattro antipasti e un piatto principale, e il piatto più popolare è una tonteki (bistecca di maiale) dolce, all'aglio. I vini sono soprattutto spagnoli e italiani, e ci sono circa 20 tipi di gin artigianale giapponese. Si può entrare senza prenotazione.

Aggiungo anche un obiettivo che mi ero prefissato. Non volevo semplicemente prendere prenotazioni. Volevo che anche un piccolo locale potesse costruire con le proprie mani l'intero flusso del farsi conoscere, far venire le persone e farle tornare. Gli sconti, le email e la finestra di chat che compaiono in questo capitolo sono tutti elementi al servizio di quell'unico scopo.

In questo capitolo riavvolgo il tempo e ripercorro come è cresciuto il sistema di prenotazione di Tamuro.

【Figura 1-1】La schermata dopo il collegamento da ChatGPT al server MCP di Tamuro (10 ottobre 2026). Legge le informazioni del locale e risponde che sa gestire orari liberi, menu, prezzi e l'indirizzamento alla pagina di prenotazione *(La schermata è in giapponese.)*

### 1-2 Il punto di partenza: soltanto prendere prenotazioni

[Il sito di prenotazione di Tamuro](https://tamuroreservation.vercel.app/?src=b2-it-{{FMT}}) all'inizio era molto semplice. Si sceglie una data, un orario e il numero di persone, si inseriscono nome e recapiti e si invia. Al locale arriva una notifica. Tutto qui.

La prima base l'ho costruita con lo strumento di sviluppo IA di Google (Antigravity). Dicevo all'IA ogni funzione che mi veniva in mente e, quando una cosa funzionava, passavo alla successiva. È quello che si chiama vibe coding (dire all'IA tutto ciò che viene in mente e farle costruire a sensazione).

Per me, allora, era una sorpresa dopo l'altra. Si descrive a parole l'impaginazione di una schermata e prende forma in pochi minuti. Si dice che si vuole un calendario e compare un calendario. Nei ritagli di tempo tra un impegno e l'altro nella gestione del locale, è nato un sito di prenotazione.

Tamuro è un posto in cui si può entrare senza prenotazione. Anzi, la maggior parte delle prenotazioni viene fatta lo stesso giorno, e molti clienti entrano direttamente senza prenotazione. Eppure ho costruito un sistema di prenotazione perché volevo un modo di entrare in contatto con i clienti prima della loro visita. Quando qualcuno prenota, restano il nome e i recapiti. Una volta che restano i recapiti, posso invitarlo a tornare.

Un sistema di prenotazione non è solo un banco di accoglienza. Diventa l'ingresso a una relazione con il cliente. Questa idea ha portato più tardi al sistema di sconti e al sistema per coltivare i clienti abituali.

Ma per una base costruita a istinto, ho finito per pagare un prezzo alto più avanti. Ne scriverò nel capitolo 2.

### 1-3 Costruire insieme un aumento dei prezzi e gli sconti

Per un ristorante o un bar, un aumento dei prezzi è una decisione inevitabile. Ingredienti, utenze e manodopera continuano a rincarare. Anche Tamuro ha alzato i prezzi. Ho aumentato ciascun menu di circa ¥400–¥500 (circa $2,7–$3,3).

L'aumento era consistente, quindi era ovvio che, se l'avessi presentato così com'era, i clienti abituali si sarebbero allontanati. Così, contemporaneamente all'aumento dei prezzi, ho deciso di integrare un sistema di sconti nel sistema di prenotazione. Non si limita a far costare meno. Premia con sconti i clienti che si comportano in modi vantaggiosi per il locale.

Il primo è lo sconto di gruppo. Più persone ci sono nel gruppo, più basso è il prezzo a persona. Circa metà dei clienti di Tamuro arriva senza compagnia, ma se vengono in gruppo le vendite del locale crescono moltissimo. Anche sottraendo lo sconto, il locale ci guadagna. Anche per i clienti è un motivo per invitare gli amici. Di fatto, il numero dei clienti che vengono in gruppo usando lo sconto per numero di persone del sito di prenotazione è cresciuto.

Il secondo è lo sconto per chi prenota in anticipo. Prenotando fino a una settimana prima si ha il 2% di sconto; fino a due settimane prima, il 4%. La maggior parte delle prenotazioni di Tamuro viene fatta lo stesso giorno, quindi non riesco a prevedere cosa arriverà. Lo sconto anticipato è un meccanismo per assicurarsi le vendite future. Nei giorni di pioggia e nei giorni freddi, se le prenotazioni sono già arrivate, il locale può organizzare con serenità la preparazione.

In terzo luogo, ho costruito anche un meccanismo di acquisto di gruppo. Se in una certa data e a una certa ora si fosse riunito un certo numero di persone, sarebbe stato offerto a prezzo scontato un menu a più portate. Doveva essere un meccanismo nello spirito di Tamuro, dove sconosciuti si riuniscono nello stesso momento.

Ma il piano di acquisto di gruppo non è stato usato per niente. Risultati zero. Ad agosto 2026 ho interrotto questo piano e ho deciso di non usarlo più.

Buttare via qualcosa che si è fatto sembra uno spreco. Ma se si costruisce con l'IA, il costo e il tempo per costruire sono piccoli. Si costruisce in piccolo, si prova e, se non funziona, si butta via. Credo che questa velocità sia il più grande vantaggio di gestire un locale con l'IA.

C'è ancora un trucco nella definizione dei prezzi. Tra i piani, ne metto di proposito uno premium costoso. Va bene se quasi nessuno sceglie il piano premium. Con un piano caro accanto, quello standard sembra conveniente. Svolge il ruolo di quello che si chiama ancoraggio (un punto di riferimento per il confronto).

【Figura 1-7】Più persone ci sono, più basso è il prezzo a persona (confronto tra 1, 4 e 6 ospiti)

### 1-4 Un sistema per coltivare i clienti abituali

Quando nel sistema di prenotazione restano nomi e recapiti, la cosa successiva che si desidera fare è coltivare il rapporto con i clienti. Un sistema che gestisce le informazioni dei clienti e approfondisce le relazioni si chiama CRM (gestione delle relazioni con i clienti). A poco a poco ho aggiunto funzioni CRM al sistema di prenotazione di Tamuro.

Quando i clienti si registrano come iscritti, possono vedere lo storico delle prenotazioni in una pagina personale. Se registrano la data di nascita, arriva un omaggio di compleanno. Gli iscritti che non vengono da un po' ricevono un messaggio che li richiama. C'è anche una tessera a timbri. Tre visite fanno guadagnare un drink, cinque una bistecca e altri vantaggi, e dopo aver raggiunto cinque il conteggio ricomincia. C'è anche una funzione per presentare amici.

Ho progettato con particolare cura il meccanismo per invitare a una seconda visita. Nei ristoranti e nei bar si dice che il fatto che un cliente alla prima visita torni una seconda volta decida se diventerà un abituale. A Tamuro invio due email di invito, a sette giorni e a 21 giorni dalla prima visita. La prima non ha coupon; ce l'ha solo la seconda. Invece di attirare con uno sconto fin dall'inizio, prima aiuto a ricordare. Se ancora non vengono, do una spintarella.

Ho fatto attenzione anche a che le email non si accumulassero. I clienti ricevono al massimo un messaggio al giorno. Quando coincidono, la priorità segue questo ordine: compleanno, invito alla seconda visita, richiamo degli iscritti che non vengono da tempo, altri avvisi. Gli iscritti che hanno già la prossima prenotazione non ricevono email di invito a venire.

Il consenso a ricevere email è disattivato per impostazione predefinita. Lasciarlo attivo aumenterebbe il numero dei destinatari, ma una progettazione in cui le persone acconsentono senza saperlo potrebbe porre un problema ai sensi della legge sulla tutela dei consumatori. Meritare fiducia più che numeri. Questo è stato il mio giudizio.

C'è un altro piccolo tocco nelle email. Nell'email di conferma della prenotazione entra un «Argomento di oggi». Qualcosa sulla stagione, sul vino o sul cibo. L'IA scrive automaticamente ogni giorno un breve argomento.

L'obiettivo è consegnare al cliente un seme di conversazione prima della visita. Tamuro è un locale dove si conversa molto tra clienti. Un argomento letto nell'email diventa la prima cosa che dicono alla persona seduta accanto al bancone. Così non ho lasciato che l'email di conferma finisse con «La sua prenotazione è stata ricevuta», e ho fatto in modo che anticipasse un po' dell'atmosfera del locale.

Ho sostituito una volta l'IA che scrive gli argomenti. Ne ho adottata una che produce argomenti più naturali e più vicini al tono del locale. Tuttavia, questo non è un meccanismo per aumentare i clienti. È un meccanismo per rendere un po' migliore l'esperienza di chi viene. Scriverò ancora di questa distinzione nella seconda metà di questo capitolo.

Tra questi meccanismi, quelli di cui i risultati hanno cominciato a vedersi sono i piani «Piacere di conoscerci» e «Bentornato». Sono piani accessibili e a prezzo contenuto che possono scegliere solo i clienti alla prima visita e quelli che non vengono da più di un anno. Danno un motivo per venire sia ai nuovi clienti sia a quelli che si stanno allontanando.

D'altra parte c'è stato anche un problema. Molti clienti prenotano come ospiti senza registrarsi come iscritti. Se richiedessi la iscrizione a ogni prenotazione, potrebbero rinunciare del tutto a prenotare. Così, dopo che una prenotazione è conclusa, mostro un invito, «Vuole collegare questa prenotazione a un account di iscrizione?», e ho costruito un modo per iscriversi in un secondo momento. Non alza alcun ostacolo alla prenotazione e così la relazione si lega solo in un secondo momento.

【Figura 1-8】Piani che possono scegliere solo i clienti alla prima visita e chi non viene da più di un anno *(La schermata è in giapponese.)*

【Figura 1-9】La tessera a timbri nella pagina personale (dati sintetici) *(La schermata è in giapponese.)*

【Figura 1-5】Email di conferma della prenotazione. Contiene un «Argomento di oggi» (dati sintetici) *(La schermata è in giapponese.)*

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

## Capitolo 3: Distribuire gli strumenti del mio locale ad altri locali

### 3-1 La piccola insegna verde sulla pagina di prenotazione

Aprendo la pagina di prenotazione di Tamuro si vede, vicino alla parte alta, una piccola insegna verde. Finché il locale è aperto c'è scritto «OPEN» e, quando chiude, «CLOSED». Quando il titolare preme il pulsante di prolungamento, l'orario di chiusura si sposta in avanti di 30 minuti e sull'insegna compare un tocco di vermiglio.

I ristoranti indipendenti hanno un tratto in comune. Aprono quasi esattamente in orario, ma la chiusura spesso slitta. Se la conversazione con i clienti è animata, le luci del locale restano accese oltre l'ultima ordinazione delle 22:30.

Ma dal lato del cliente, questo non si vede. L'indicazione «Aperto» di Google Maps è giudicata solo dagli orari registrati, quindi non riflette né i prolungamenti, né le chiusure anticipate, né le chiusure temporanee. Nessuno va a piedi fino a un locale oltre l'orario di chiusura pensando «Forse è ancora aperto». E anche telefonare per chiedere mette a disagio.

Questa insegna è uno strumento che risponde a quel «È ancora aperto?». Si chiama «AgendaLuce (Taccuino della Luce)». Luce significa «luce».

Il Taccuino della Luce è costruito per funzionare quasi senza attenzioni da parte del titolare. Si registrano una volta gli orari di apertura e chiusura di ogni giorno della settimana e l'insegna si accende e si spegne automaticamente. Il titolare la tocca solo per prolungare, chiudere in anticipo o prendersi un giorno di riposo. Per prolungare si preme un pulsante sullo smartphone. Anche il personale può usarla da un collegamento dedicato che funziona senza accesso.

I clienti non hanno bisogno di accesso né di registrazione. Aprendo la pagina pubblica si vede lo stato attuale della luce. Se la si aggiunge alla schermata iniziale dello smartphone, funziona come un'app. Il piccolo componente dell'insegna si può anche incorporare in altri siti web. Quello che compare sulla pagina di prenotazione di Tamuro è quel componente.

Il Taccuino della Luce è gratuito. Se ci si limita a incorporare il componente dell'insegna nel proprio sito web, la configurazione richiede circa 10 minuti.

Ed ecco la parte importante. Questo Taccuino della Luce non è solo per Tamuro. Può usarlo qualsiasi locale.

Ho lasciato di proposito fuori il nome del locale dal design dell'insegna. Se vi mettessi un nome, diventerebbe l'insegna di Tamuro. Si può anche scegliere la lingua di visualizzazione. Ho reso il componente piccolo in modo che si possa incorporare nel sito di qualsiasi locale.

Uno strumento nato dal problema di Tamuro, «la chiusura slitta», fatto fin dall'inizio in una forma che chiunque può usare. Questo è il Taccuino della Luce. E l'insieme di strumenti come questo è la «serie Agenda».

【Figura 3-1a】L'insegna del Taccuino della Luce sopra la pagina di prenotazione (aperto) *(La schermata è in giapponese.)*

【Figura 3-1b】Durante un prolungamento compare un tocco di vermiglio *(La schermata è in giapponese.)*

【Figura 3-6a】La schermata del titolare. Per prolungare si preme il pulsante una volta *(La schermata è in giapponese.)*

【Figura 3-6b】Subito dopo aver premuto il prolungamento. L'orario di chiusura si sposta in avanti di 30 minuti *(La schermata è in giapponese.)*

【Figura 3-6c】La pagina pubblica che vedono i clienti (durante un prolungamento) *(La schermata è in giapponese.)*

### 3-2 È cominciato dal taccuino di pelle nera

La serie Agenda non era pianificata come una serie. È cominciata con un unico sistema, che non è nemmeno ancora stato pubblicato.

Quello che mi ero proposto di costruire per primo era un meccanismo che riconosce i volti dei clienti e accoglie gli abituali. Una telecamera all'ingresso del locale distingue i visitatori dal volto e avvisa il titolare: «Quella è la persona che aveva preso la tonteki l'ultima volta, quella che non vedevamo da tre mesi». Intendevo far aiutare da una macchina il lavoro che il titolare di un piccolo locale fa a mente: ricordare volti, nomi e preferenze.

Ma poco dopo aver iniziato a costruire, ho capito che era un sistema a cui veniva affidato qualcosa di molto pesante. Volti. Attributi. Cronologia delle visite. Il carattere di un cliente. Sono tutte informazioni che, una volta trapelate, non si possono riprendere indietro.

Quello che mi è venuto in mente allora è stato «Il taccuino di pelle nera» di Seicho Matsumoto. Un archivio che non si mostra a nessuno, eppure certamente esistente. Un registro che, una volta aperto, mette in moto la vita e la morte delle persone. Non è proprio ciò che sto cercando di costruire?

In italiano, «agenda» indica il taccuino degli appuntamenti e «nera» significa «nero». Messi insieme: AgendaNera. Il taccuino di pelle nera. È così che il nome è stato deciso per primo.

AgendaNera è ancora in costruzione. È quello che sto costruendo con più cura nella serie.

E questa scelta del nome è stata il punto di svolta. Se esiste un taccuino nero, possono esistere taccuini di altri colori. Avrei ricostruito i meccanismi che usavo ogni giorno nel mio locale in forme che qualsiasi locale può usare e li avrei pubblicati un taccuino alla volta. Questa è la [serie Agenda](https://bontallc.com/agenda?via=b2-it-{{FMT}}).

### 3-3 Aggiungere taccuini, uno alla volta

La serie Agenda è un insieme di piccole app web, ciascuna delle quali risponde a un problema della ristorazione con uno strumento. Ognuna ha un nome italiano e un soprannome (in giapponese termina con «taccuino»). Ogni nome ha la sua origine.

| Nome | Soprannome | Origine del nome | Che cosa fa |
| --- | --- | --- | --- |
| AgendaTimbro | Timbrature | Timbro significa «timbro». È la timbratura stessa | Registra l'entrata e l'uscita del personale |
| AgendaOro | Redditività | Oro significa «oro». Il taccuino del denaro | Stima la redditività dell'apertura di un locale o di un nuovo piatto del menu (gratuito) |
| AgendaBis | Guida al Secondo Locale | Bis significa «bis». Il «Bis!» gridato dal pubblico a un concerto | Guida i clienti a un secondo locale vicino (gratuito) |
| AgendaQA | Guida al Supporto | Qua significa «qui». Quando si è in difficoltà, qui | Il servizio di assistenza condiviso della serie (gratuito) |
| AgendaLuce | Taccuino della Luce | Luce significa «luce» | Mostra se il locale è aperto (gratuito) |
| AgendaRicetta | Taccuino dei Costi | Ricetta significa «ricetta» | Calcola il costo di una ricetta e l'incidenza del costo (gratuito) |
| AgendaNera | Taccuino dei Clienti Abituali | Nera significa «nera». Il taccuino di pelle nera | Accoglie gli abituali con il riconoscimento facciale (in costruzione) |
| AgendaTurno | Taccuino dei Turni | Turno in italiano è il turno di servizio | Raccoglie le richieste di turno del personale e distribuisce il piano che l'IA del titolare mette insieme (in arrivo) |

Quale taccuino si adatta a quale tipo di locale? Timbrature è per i locali con due o più collaboratori che gestiscono le presenze su carta o su LINE *(l'app di messaggistica più diffusa in Giappone)*. Redditività è per chi sta per aprire un locale e per chi vuole rivedere i propri numeri perché sono cambiati l'affitto o i costi. La Guida al Secondo Locale è per i locali incentrati sul pasto che vogliono mandare presto i clienti al locale successivo. Il Taccuino della Luce è per i locali indipendenti la cui chiusura slitta più tardi o più presto del previsto. Il Taccuino dei Costi è per i locali in cui le ricette sono in testa ma non si è mai calcolata l'incidenza dei costi.

#### Timbrature non calcola gli stipendi

Timbrature trasforma così com'è il tablet del locale o gli smartphone del personale in una macchina per timbrare. Basta toccare il proprio nome. Il foglio presenze viene totalizzato automaticamente e si può esportare in CSV (un formato che si apre nei programmi di fogli di calcolo). Il giorno di attività comincia alle 5 del mattino, quindi, anche con orari notturni, la data non cambia.

Ma questo Timbrature di proposito non calcola gli stipendi.

Paghe orarie, indennità e date di chiusura differiscono troppo da un locale all'altro. Notte con il 25% in più, festivi come categoria a parte, trasporti a importo giornaliero. Comunque lo costruissi, non si adatterebbe al locale di qualcuno.

Così, invece di calcolare, ho preparato «un modello di istruzioni da consegnare a un'IA». Il titolare incolla il CSV delle presenze scaricato e questo modello, così come sono, in qualunque IA usi normalmente, sia ChatGPT, Claude o Gemini. Poi l'IA calcola le maggiorazioni notturne, la paga dei festivi e i trasporti e li elenca. Le regole di ciascun locale, come «chiudiamo i conti a fine mese, la notte ha il 25% in più e le domeniche sono una categoria a parte», si possono aggiungere al modello e verranno rispecchiate così come sono. Il CSV include colonne per il giorno della settimana e il nome del festivo, così che l'IA possa calcolare correttamente.

Non possiedo io il meccanismo di calcolo; ogni locale tiene le proprie regole nelle proprie mani. Credo che sia il modo più difficile da rompere.

#### Guidare verso un secondo locale e lasciare il proprio nella memoria

La Guida al Secondo Locale è uno strumento per creare una «pagina guida al secondo locale» da dare ai clienti. A chi ha finito di mangiare, indica un bar vicino o un posto per un ultimo boccone, insieme a quanti minuti ci vogliono a piedi.

Sembra uno strumento per mandare i clienti altrove, ma c'è un piccolo trucco. Guidare qualcuno verso una seconda tappa sottintende che la prima tappa è stata il proprio locale. Pur sembrando di mandare via i clienti, in realtà si incide nella loro memoria che «la prima tappa è stata questo locale». È progettato così.

#### Tre principi di progetto: automatico, forza presa in prestito, funzione singola

Tutti i taccuini della serie Agenda condividono tre principi.

Il primo è «automatico». Deve funzionare senza che il titolare lo tocchi ogni giorno. Con il Taccuino della Luce, una volta registrato l'orario, la luce si accende e si spegne da sola. Chi gestisce un ristorante non ha tempo di toccare uno schermo durante il servizio. Uno strumento che non funziona se non lo si tocca finirà prima o poi per non essere più usato.

Il secondo è «forza presa in prestito». Non costruire tutto da sé; lasciare le cose agli strumenti e all'IA che il titolare già usa. Il calcolo degli stipendi di Timbrature ne è il caso esemplare. Il taccuino dei turni è lo stesso: si occupa soltanto di raccogliere le preferenze del personale e lascia il lavoro di costruire i turni all'IA del titolare. Non porta con sé né un meccanismo complicato proprio, né il costo di chiamare un'IA. Ecco perché il prezzo si può tenere basso.

Il terzo è «funzione singola». Un taccuino fa una sola cosa, e la fa in modo affidabile. Un sistema multifunzione è troppo pesante per un locale indipendente. Se si continuano ad aggiungere funzioni, diventa più difficile da usare e le contraddizioni dal lato di chi costruisce si moltiplicano. È quello che ho imparato in prima persona con il sistema di prenotazione nel capitolo 2. Così aggiungo i taccuini uno alla volta, ciascuno impegnato a fare «solo questa cosa, fatta bene».

#### Perché il sistema di prenotazione non è nella serie

A questo punto mi aspetto una domanda ovvia. La cosa in cui Tamuro ha messo più lavoro è il sistema di prenotazione. Perché non metterlo nella serie Agenda?

In realtà una volta avevo intenzione di farlo. Il piano era di mettere il sistema di prenotazione in una forma utilizzabile da altri ristoranti e pubblicarlo come un taccuino della serie. Ma ad agosto 2026 ho annullato quel piano.

Il motivo è proprio quello di cui ho scritto nel capitolo 1. Il sistema di prenotazione di Tamuro è pieno del modo di fare impresa di Tamuro. Che i clienti singoli sono la metà. Che quasi il 90% delle prenotazioni viene fatto nel giorno stesso. Che voglio vendere il tempo prima dell'apertura. Che voglio che si venga in gruppo. Che voglio far crescere gli abituali. Ho costruito le combinazioni di sconti, l'ordine delle email e il modo in cui la chat raccomanda le cose per adattarli tutti a questo.

Se lo diluissi in qualcosa che chiunque possa usare, diventerebbe un normale sistema di prenotazione che va bene per tutti i locali così così. Allora la forza di Tamuro svanirebbe. Il sistema di prenotazione e il CRM sono il modo in cui il locale si vende. Invece di adattare il locale a un sistema generico, adattare il sistema del locale al locale. Il nostro locale, con le nostre specifiche. Così ho deciso di tenere il sistema di prenotazione di Tamuro solo di Tamuro.

Quindi non c'è nulla da distribuire oltre al locale? Niente affatto. Attorno al sistema di prenotazione ci sono molti piccoli problemi comuni a ogni locale. Tenere il cuore del locale sulle proprie specifiche. Costruire gli strumenti che risolvono i problemi circostanti in una forma che tutti possano usare fin dall'inizio e distribuirli. La pagina di prenotazione di Tamuro è un esempio con entrambe le cose allineate su un'unica schermata. Sopra un sistema di prenotazione solo per Tamuro c'è l'insegna del Taccuino della Luce, che chiunque può usare.

【Figura 3-2】La pagina di presentazione della serie Agenda *(La schermata è in giapponese.)*

【Figura 3-3a】Presentazione di Timbrature *(La schermata è in giapponese.)*

【Figura 3-3b】Presentazione di Redditività *(La schermata è in giapponese.)*

【Figura 3-3c】Presentazione della Guida al Secondo Locale *(La schermata è in giapponese.)*

【Figura 3-4】La schermata di timbratura di Timbrature. Basta toccare il proprio nome (dati sintetici) *(La schermata è in giapponese.)*

### 3-4 Costruire fin dall'inizio per tutti

Faccio uno strumento per il mio locale e poi lo distribuisco anche ad altri locali. A dirlo sembra semplice, ma per farlo deve cambiare il modo di decidere le cose prima di iniziare a costruire.

Se costruissi solo per Tamuro, il modo più rapido sarebbe scrivere direttamente nel programma gli orari di Tamuro e il nome di Tamuro. Ma allora nessun altro locale potrebbe usarlo. Se si cerca di renderlo generico più tardi, si finisce per cercare ogni punto scritto in modo fisso e correggerli uno a uno.

Così gli strumenti della serie Agenda sono specificati fin dall'inizio sul presupposto che tutti possano usarli. Parto da un problema di Tamuro, ma nella fase dei requisiti separo due domande: «Questo vale solo per Tamuro o vale per ogni locale?» Non mettere il nome del locale sull'insegna. Lasciare scegliere la lingua. Renderlo inseribile in qualsiasi sito web. Ho fissato decisioni come queste mentre scrivevo il documento dei requisiti del Taccuino della Luce.

È un altro uso della definizione dei requisiti che ho imparato di nuovo nel capitolo 2. Se si decidono prima queste cose, si può usare lo strumento a Tamuro e distribuirlo ad altri locali così com'è.

I problemi del mio locale sono anche i problemi di altri locali. Non sono l'unico titolare che vuole dire ai clienti che l'orario di chiusura sta slittando. Il titolare di un locale indipendente costruisce uno strumento a partire dal proprio problema, poi lo distribuisce ad altri locali. È l'idea alla base della serie Agenda.

### 3-5 La democratizzazione della tecnologia

La serie Agenda ha ormai più di 10 prodotti. Li costruisco e li gestisco senza altro aiuto, stando dietro il bancone.

Qualche anno fa sarebbe stato impensabile. Per costruire un prodotto servivano qualcuno che lo pianificasse, qualcuno che progettasse le schermate, qualcuno che scrivesse il codice, qualcuno che lo collaudasse e qualcuno che lo gestisse. Senza un team e dei fondi non si poteva mettere un prodotto al mondo.

Non è più così. Il titolare dice i requisiti all'IA, l'IA scrive il codice, l'IA lo collauda e un'altra IA lo sottopone ad audit. Quello che fa il titolare è decidere che cosa costruire, giudicare se i risultati dell'IA si adattano allo scopo del locale e fare solo le operazioni che solo le persone possono fare.

Questo tipo di cambiamento si chiama in genere «democratizzazione della tecnologia». Il potere di costruire non è più proprietà di poche persone o aziende.

Ma qui voglio parlare con onestà. Come ho scritto nell'Introduzione, ho lavorato nell'informatica per circa 16 anni, per lo più nella pianificazione dei sistemi e come coordinatore tra le persone sul campo e i fornitori di sviluppo. Conoscevo per esperienza la definizione dei requisiti, il modo di pensare i database e come far girare i test. Perciò non dico che chi non ha mai scritto una riga di codice possa fare lo stesso dall'oggi al domani.

Eppure, è cambiato moltissimo. Ora posso costruire, in autonomia e negli interstizi tra il mio lavoro principale, cose di una scala che un tempo richiedeva un team. E per chi non ha esperienza, l'ingresso si è certamente abbassato. L'IA insegna, se si chiede qualcosa che non si capisce. Dà forma a ciò che le si dice a parole. Ciò che manca non è la tecnica, ma la capacità di decidere che cosa costruire e le parole per dirlo all'IA. Sono capacità che chi gestisce un locale usa comunque ogni giorno.

### 3-6 Il dibattito sulla «morte del SaaS»

Il software che si usa via internet pagando un canone mensile, come la serie Agenda, si chiama SaaS (Software as a Service). Software di contabilità, gestione di presenze e orari, gestione delle prenotazioni. Oggi i ristoranti usano molti strumenti SaaS.

L'IA metterà fine al SaaS? Nel 2026 quel dibattito è divampato in grande.

Uno dei fattori scatenanti è stata una dichiarazione dell'amministratore delegato di Microsoft, Satya Nadella. In un podcast di dicembre 2024, Nadella ha detto che le applicazioni SaaS sarebbero crollate nell'era degli agenti IA. Il ragionamento: quando gli agenti IA assumeranno la parte decisionale del lavoro aziendale, il software costruito perché le persone lo usino tramite schermate non servirà più.

Poi, a febbraio 2026, Anthropic ha annunciato Claude Cowork (uno strumento di IA che esegue compiti aziendali in autonomia), e le azioni delle società di software americane sono state vendute massicciamente. A Wall Street il crollo è stato chiamato «SaaSpocalypse». Ciò che gli investitori temevano era che, se gli agenti IA fanno il lavoro, il modello SaaS di guadagnare un canone per persona (prezzi per postazione) sarebbe crollato.

Ci sono anche controargomenti. L'amministratore delegato di Nvidia, Jensen Huang, ha detto che gli agenti IA non sostituiranno il software ma lo useranno per conto delle persone, e ha definito la vendita massiccia una reazione eccessiva. Non pochi altri vedono anzi il SaaS che assorbe l'IA diventare più forte.

Il SaaS morirà davvero? Ecco cosa penso.

Ciò che muore è lo strato intermedio del SaaS: quello che fa pagare un canone mensile alto per postazione e presuppone che le persone lo usino tramite schermate. Se è l'IA a fare il lavoro al posto delle persone, non servono postazioni per ciascuna persona. Se nessuno usa una schermata, non serve una schermata elaborata.

Ciò che resta sono gli strumenti economici che fanno una cosa in modo affidabile. E gli strumenti che sono facili da usare per l'IA.

Sono esattamente i tre principi della serie Agenda. Funziona automaticamente, è lasciata all'IA del titolare (affidarsi ad altri) e fa una cosa sola (funzione singola). AgendaTurno lascia il lavoro di costruire il piano dei turni all'IA del titolare, che è proprio la forma «l'IA usa il software» descritta da Huang. Il sistema di prenotazione di Tamuro apre una finestra tramite MCP alle IA dei clienti, ed è la stessa idea.

Naturalmente può sembrare che qui ci sia una contraddizione. Parlo della morte del SaaS, eppure la serie Agenda è essa stessa SaaS. Ma la serie Agenda è un insieme di strumenti che un titolare ha costruito per il proprio locale e poi reso pubblici a basso prezzo. Non è un modello che fa pagare un canone mensile alto per postazione, e non presuppone che le persone stiano incollate a una schermata ogni giorno. È costruita fin dall'inizio sul presupposto che sia l'IA a usarla.

#### La «morte del SaaS» per i ristoranti

Questo dibattito può sembrare una storia di investitori e di industria informatica. Ma per i ristoranti la stessa cosa sta per accadere in una forma molto più familiare.

Molti locali indipendenti pagano un canone mensile a siti gastronomici e siti di prenotazione e, in aggiunta, pagano una commissione di segnalazione per ogni prenotazione. In cambio del portare clienti, il sito detiene il legame con il cliente, e non è raro che il locale non abbia nemmeno i recapiti del cliente. Se i prezzi salgono, il locale non ha scelta che seguire, e se cambia il sistema delle classifiche, cambia il flusso dei clienti.

Come ho scritto nel capitolo 1, nel 2026 è iniziata l'epoca in cui i clienti fanno cercare i locali alla propria IA. Se l'ingresso si sposta sull'IA, l'intero assetto di pagare a un sito canoni mensili e commissioni per essere messi in alto nei suoi elenchi comincia a vacillare. Se un locale apre da sé una finestra all'IA, i clienti possono raggiungerlo senza passare per i grandi siti. I registri delle prenotazioni e la relazione con il cliente restano nelle mani del locale.

Se metto «la morte del SaaS» nelle parole di un locale indipendente, è «la fine dell'epoca in cui bastava pagare per comparire». Tamuro ha aperto la propria finestra tramite MCP e tiene le prenotazioni e il CRM sulle proprie specifiche, come preparazione a questo.

Se il SaaS morirà, nessuno lo sa ancora. Ma la forma degli strumenti che resteranno nell'epoca dell'IA comincia a delinearsi. Questo è ciò che penso.

### 3-7 Monetizzazione: piccoli, tanti, economici

Costruisco la serie Agenda con l'obiettivo di farla reggere come attività. L'obiettivo è renderla un secondo pilastro di reddito, separato dal ristorante.

Ho fissato prezzi molto contenuti. I canoni mensili partono da qualche centinaio di yen. Timbrature, per esempio, costa ¥500 (circa $3,3) al mese. Mescolo anche strumenti gratuiti, come Redditività, il Taccuino della Luce e il Taccuino dei Costi. Gli strumenti gratuiti fanno da ingresso con cui si conosce la serie Agenda. Il Taccuino della Luce non usa né un'API di mappe né l'IA generativa, quindi costa quasi nulla da far funzionare. Per questo posso regalarlo.

C'è un solo account. Con un account condiviso chiamato AgendaID si possono usare tutti gli strumenti della serie. Non serve registrarsi di nuovo per ogni strumento. Gli strumenti a pagamento hanno un periodo gratuito di tre mesi e si possono iniziare senza registrare una carta. Il periodo gratuito è disponibile una sola volta per ciascuna combinazione di locale e prodotto. Se si presenta un altro locale, si ottiene un bonus.

Il motivo per cui posso tenere bassi i prezzi sta nel modo in cui costruisco. Costruisco in autonomia, faccio fare la costruzione all'IA e riutilizzo una base condivisa. Il costo del database è tenuto a circa $35 al mese per l'intera serie. Se il costo per costruire e il costo per gestire sono entrambi piccoli, un'attività regge anche con piccole vendite.

Lo dico con franchezza. Mentre scrivo questo libro, alcuni locali hanno provato gli strumenti, ma non ci sono quasi registrazioni a pagamento. Il sistema per costruire c'è, ma il sistema per farsi conoscere è ancora da fare. Anche questo libro è pensato come un volume a quello scopo, per farsi conoscere.

#### Costruire qualcosa e far continuare a usarlo sono cose diverse

C'è un'altra cosa che voglio dire con franchezza. Riuscire a costruire uno strumento e avere qualcuno che continua a usarlo sono faccende distinte.

Costruire è diventato più veloce grazie all'IA. Ma far sì che le persone continuino a usarlo richiede tutt'altro lavoro. Rispondere alle domande su come si usa (la Guida al Supporto esiste per questo). Inviare un avviso prima che finisca il periodo gratuito. Spiegare il motivo quando si alza un prezzo. Cancellare correttamente i dati quando qualcuno chiede di disdire. E soprattutto, farlo funzionare senza che il titolare lo tocchi.

Dei tre principi della serie Agenda, «automatico» è il principio per questo «far continuare a usare». Uno strumento che non funziona se il titolare non lo tocca ogni giorno verrà prima o poi disdetto. Non è finito quando è costruito. Diventa un'attività solo quando continua a essere usato. Aggiungere, uno a uno, locali che continuano a usarlo: è il mio compito dopo la pubblicazione di questo libro.

#### Se si vuole cominciare nel proprio locale

Per chi ha letto questo libro e vuole provare nel proprio locale, ci sono tre passi.

1. Aprire https://bontallc.com/agenda?via=b2-it-{{FMT}} e accedere con un account Google (verrà creato AgendaID. Non serve registrare una carta)
2. Per prima cosa, aggiungere un taccuino gratuito. Consiglio il Taccuino della Luce. Basta incollare il componente dell'insegna nel proprio sito web e funziona in 10 minuti. Se non si è ancora aperto, provare Redditività
3. Se sembra adatto, provare Timbrature gratis per tre mesi. Man mano che la scadenza si avvicina arriva un avviso, quindi non verrà addebitato nulla anche se lo si lascia stare

Per qualsiasi domanda, ci si rivolge alla Guida al Supporto (AgendaQA). L'IA risponde subito alle domande operative, e le domande su specifiche e bug le leggo di persona.

Le vendite di un ristorante dipendono dal tempo e dalla stagione. Il numero di posti e gli orari di apertura hanno entrambi dei limiti. Le vendite di strumenti, invece, non hanno limite di posti. Gestire un locale mentre si distribuiscono strumenti nati dai problemi del proprio locale, e lasciare che questo diventi lentamente un reddito: credo che possa diventare un altro modo di guadagnare per un locale indipendente.

#### Restare una piccola azienda, andare nel mondo

C'è un'altra cosa che ho deciso fin dall'inizio per la serie Agenda. Non l'avrei costruita solo in giapponese.

Timbrature, Redditività e la Guida al Supporto si possono usare tutti in 20 lingue. I testi delle schermate e le domande frequenti, tutto. Uno strumento costruito per un bar da 19 posti a Tokyo funziona allo stesso modo in inglese, in coreano, in vietnamita.

I motivi sono due. Il primo è che i problemi dei ristoranti non cambiano al cambiare del paese. Si vogliono registrare gli orari di arrivo e di uscita del personale. Si vuole conoscere la redditività prima di aprire. Si vuole dire ai clienti che l'orario di chiusura è stato prolungato. Sono tutti problemi che i locali indipendenti di tutto il mondo condividono. L'altro è che il numero di locali indipendenti in Giappone continua a calare. Se servissi solo il mercato di lingua giapponese, le vendite degli strumenti avrebbero un tetto.

In passato, perché una piccola azienda vendesse prodotti all'estero servivano agenti locali, società di traduzione ed entità giuridiche. Ora l'IA aiuta con traduzione e revisione. Sistemi di pagamento condivisi funzionano in tutto il mondo. Per la consegna basta un server e non ci sono scorte né magazzini in ogni paese. Uno strumento fatto da un titolare può stare sugli scaffali del mondo in 20 lingue il giorno dopo averlo fatto. In passato potevano farlo solo le grandi aziende.

Una piccolissima azienda che fa affari con più paesi fin dall'inizio: aziende così si chiamano talvolta micro-multinazionali (minuscole società multinazionali). Bonta LLC punta proprio a questo, con un locale a Higashi-Nakano e un titolare.

Naturalmente, tradurre in 20 lingue non significa che i titolari all'estero comincino a usarlo subito. Alcune traduzioni attendono ancora la revisione di madrelingua per suonare naturali. Ciononostante, eliminando fin dall'inizio la barriera linguistica, il tetto a quanto lontano possano arrivare gli strumenti scompare, proprio come il tetto sui posti.

Di come sto costruendo quella base parlerò nel capitolo 4.

【Figura 3-5】Il cambio di lingua nella Guida al Supporto. Sono elencate 20 lingue *(La schermata è in giapponese.)*

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

## Capitolo 5: Il futuro di un piccolo bar

### 5-1 Da Zatta Gohan a Tamuro

Ho iniziato a lavorare nel settore della ristorazione a 39 anni.

L'occasione è stata un bar di quartiere chiamato Zatta. Una volta al mese, a volte ogni due settimane, mi lasciavano servire dei pasti lì. Per molto tempo avevo imparato a cucinare da autodidatta, ma ora avevo un posto in cui le persone mangiavano la mia cucina ed erano felici. Quella è stata la mia esperienza di partenza.

Nel 2014 ho aperto un ristorante chiamato Zatta Gohan ad Arai-Yakushi. Era un piccolo locale che serviva pasti a menu fisso. L'ho gestito per sette anni.

Ad Arai-Yakushi, però, sentivo un limite nel numero di clienti. Poi ho trovato un immobile a Higashi-Nakano. Dall'uscita est della stazione si cammina meno di un minuto. Anche nei giorni di pioggia ci si arriva senza bagnarsi molto.

A novembre 2018 vi ho aperto Tamuro. «Tamuro» indica un luogo in cui le persone si riuniscono. Ha 11 posti al bancone e 8 posti su tatami, 19 in tutto. Per tre anni ho gestito due locali in parallelo, Arai-Yakushi e Higashi-Nakano. Durante il periodo del COVID mantenerli entrambi è diventato difficile, quindi ho chiuso il locale di Arai-Yakushi e mi è rimasto solo Tamuro.

#### Il curation bar

Tamuro si definisce un «curation bar», un bar basato su un'attenta selezione.

Curation, la cura nella selezione, significa avere un occhio selettivo. Prima ancora di essere un cuoco, voglio essere un curatore. Il cibo, le bevande, l'atmosfera del bar: faccio tutto scegliendo con occhio selettivo. Questo è Tamuro.

Viaggio spesso per mangiare, sia all'estero sia in Giappone. Vietnam, Cambogia, Italia, Shanghai, Pechino, Messico. Mangiare girando è un piacere e, allo stesso tempo, è un modo per trovare che cosa servire a Tamuro. Ricreo ingredienti costosi con ingredienti a portata di mano. Per esempio, se si fa seccare il tuorlo d'uovo e lo si grattugia, si ottiene un sapore vicino alla bottarga. Considero questo tipo di sostituzione (localizzazione) il mio ruolo.

Durante il periodo del COVID ho studiato di nuovo la cucina. Ho seguito un corso di cucina francese di otto lezioni in tutto e ho frequentato anche un corso di cucina giapponese. Come gestire l'umami e come controllare la cottura. Ciò che ho imparato lì è la base della mia cucina di oggi.

Il menu di Tamuro è costruito con quattro antipasti e un piatto principale. Gli do una gamma di ingredienti perché i clienti che vivono da soli possano assumere molte verdure. Lo compongo in modo che i metodi di cottura (fritto, in agrodolce all'aceto, stufato, alla griglia) e i sapori (dolce, piccante, acido) non si sovrappongano. Il piatto più popolare è la tonteki, la bistecca di maiale. Ha una salsa leggermente dolce a base di salsa di soia di Kyushu, con tanto aglio.

#### Un luogo dove le persone si riuniscono

Circa metà dei clienti di Tamuro arriva senza compagnia. Hanno per lo più dai 30 ai 50 anni e molti sono vicini di Higashi-Nakano, ma vengono persone anche da zone come Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo ed Eifukucho.

La caratteristica distintiva del bar è quanto i clienti parlino tra loro. Ho costruito il bancone in modo che sia facile parlare con la persona accanto, e io o il personale decidiamo i posti a sedere valutando chi andrà d'accordo. I clienti che erano venuti senza compagnia a volte tornano insieme in seguito. Come dice il nome, è diventato un luogo dove le persone si riuniscono. Pubblico su [Instagram](https://www.instagram.com/tamuro.higashinakano/) come sono le giornate del bar.

Nella cena a percorso che si tiene circa una volta al mese servo da sette a otto piatti nell'arco di due o tre ore, insieme ad abbinamenti di vino. Ogni mese il tema cambia: italiano, francese, giapponese. I corsi di cucina sono laboratori di tre ore e, dopo aver cucinato, tutti brindano, mangiano e vanno a casa. C'è l'aperitivo, con vino e piccoli piatti nel tardo pomeriggio, prima dell'apertura. C'è un barbecue circa due volte l'anno. C'è una festa di fine anno una volta l'anno. E c'è la festa degli yukata di cui ho scritto nel capitolo 1.

Il sistema di prenotazione di cui ho scritto nel capitolo 1, la finestra di chat e MCP sono tutti strumenti per portare le persone in questo bar. L'IA è un mezzo per riunire le persone, non l'obiettivo.

### 5-2 L'hamburger al curry di Quatre Épices

Tamuro è un bar serale. Di giorno lo spazio è vuoto.

Sfruttando quel tempo, a gennaio 2024 ho avviato Quatre Épices. È un locale specializzato in hamburger al curry che opera solo a pranzo nello stesso posto, e la gestisce il personale.

Quatre Épices in francese significa «quattro spezie». Fedeli al nome, invece di sovrapporre tante spezie, le scegliamo e le riduciamo per rendere chiaro il profilo del sapore. Il curry non usa farina; si finisce con la naturale densità delle verdure e della carne stesse. Soddisfazione a fine pasto e nessuna pesantezza allo stomaco. E armonia con l'hamburger. L'ho progettato su queste tre premesse.

Siamo attenti a come viene cotto l'hamburger. Impostiamo l'impasto in modo che venga croccante fuori e soffice dentro e cuociamo in modo adatto a quell'impasto. Il controllo della cottura che ho imparato la sera a Tamuro serve anche al piatto di giorno.

Prezzi, giorni di attività e orari possono cambiare, quindi si prega di consultare l'Instagram di Tamuro (https://www.instagram.com/tamuro.higashinakano/) per le informazioni più recenti.

Quatre Épices gestisce anche una mensa per bambini nello stesso posto. È un'attività che usa le strutture e gli acquisti del bar esistente per servire pasti ai bambini del quartiere. Attraverso quel legame abbiamo costruito anche un rapporto con il centro civico locale. A volte serviamo curry e panini a eventi sportivi locali, eventi del centro civico e feste con il ballo del Bon.

Per essere onesti, sfruttare le ore del giorno non è andato tutto bene. Ho creato giorni dedicati al bere di giorno e ho affittato lo spazio ad altri, ma i clienti non sono venuti come speravo. Il fascino del bar arriva in modo diverso quando c'è il titolare la sera e quando c'è solo il personale diurno. Far crescere il locale diurno con un fascino diverso da quello del locale serale è ancora un compito incompiuto.

### 5-3 Bonta LLC: due pilastri

La piccola azienda che gestisce Tamuro e Quatre Épices è Bonta LLC. Ne ricopro il ruolo di socio amministratore.

L'azienda ha due pilastri. Uno è la ristorazione: Tamuro e Quatre Épices. L'altro è l'informatica: lo sviluppo della serie Agenda e la consulenza.

La ristorazione e gli strumenti si differenziano nel modo di guadagnare. Sostenere l'azienda con due pilastri di natura diversa è la forma che ho in mente.

E i due pilastri si forniscono a vicenda i materiali. Un guaio al bar diventa il seme di uno strumento. Ciò che imparo costruendo strumenti ritorna nella gestione del bar. Il Taccuino della Luce è nato dalle chiusure che slittavano, e i registri dei prolungamenti del Taccuino della Luce diventano la base per le stime dei profitti e per i turni. Le «domande a cui non abbiamo saputo rispondere» che si accumulano nella finestra di chat migliorano le informazioni del bar. Questo ciclo è il motivo per cui riesco a gestire in autonomia sia il bar sia lo sviluppo.

Non penso di ingrandire l'azienda. Piccoli, tanti ed economici. Questa è la forma di questa azienda.

### 5-4 Scrivere come Raku Bonta

Quando scrivo e pubblico, uso lo pseudonimo «Raku Bonta». Ho scritto questo libro con quel nome.

Il mio libro precedente, *Il vice responsabile IA*, era un libro sull'IA generativa. È arrivato al primo posto nella categoria della gestione del tempo di Amazon ed è stato letto da molte persone. Questo libro ne è il seguito.

Oltre ai libri scrivo anche su note. Scrivo degli sforzi del bar con l'IA, di ciò che ho scoperto in un viaggio di formazione, dell'avanzamento della pubblicazione dei miei libri e della serie Agenda. Il seguito che non ho potuto inserire in questo libro si può seguire su note (https://note.com/bontallc).

Per me scrivere è anche un modo di mettere in parole e verificare sia il bar sia lo sviluppo. Come ho scritto nel capitolo 1, la prima conoscenza della finestra di chat «T-AI-MURO» è stata costruita con parole che avevo lasciato su X. Ciò che avevo scritto è diventato materiale per l'IA. D'ora in poi, anche ciò che scrivo tornerà sia al bar sia all'IA.

C'è un'altra cosa che ho deciso sullo scrivere. Non annuncio cose non finite con un «in arrivo». Finisco, preparo una pagina di presentazione e solo allora le pubblico. Credo che rispettare quell'ordine sia ciò che fa guadagnare fiducia a una piccola azienda.

### 5-5 Il futuro del locale indipendente

Infine raccolgo ciò che ho scritto in questo libro in un unico quadro.

【Figura 5-1】Il quadro d'insieme di ciò che questo libro ha descritto. Un piccolo bar apre la propria finestra (la prima storia) e trasforma i propri guai in strumenti da dare ad altri bar (la seconda storia) *(La schermata è in giapponese.)*

I clienti arriveranno a far cercare un bar e a far fare la prenotazione alla propria IA. Ad agosto 2026 è diventato possibile prenotare i ristoranti da ChatGPT tramite un grande servizio di prenotazione. L'ingresso si sta spostando dai motori di ricerca e dai siti di recensioni gastronomiche all'IA di ciascuna persona.

A quel punto, un bar non presente nel grande servizio di prenotazione è invisibile all'IA. Ma anche senza essere nel grande servizio, c'è una strada perché un bar si colleghi direttamente all'IA. Tamuro ha scelto quella strada aprendo una finestra chiamata MCP. Un piccolo bar che apre da sé la propria finestra. È la prima storia di questo libro.

I titolari di bar potranno trasformare i propri guai in strumenti e darli ad altri bar. Il Taccuino della Luce è nato dal guaio di Tamuro, voler dire alle persone che la chiusura sarebbe slittata, e si può usare in qualsiasi bar. Il potere di costruire sta diventando qualcosa che non è più solo di certe persone o aziende. Il titolare di un piccolo bar passa dal lato di chi usa gli strumenti al lato di chi li costruisce e li distribuisce. È la seconda storia di questo libro.

Ciò che le due hanno in comune è che più il bar è piccolo, più può avere un'identità netta.

Le grandi catene generalizzano i propri sistemi perché ogni punto vendita offra la stessa qualità. Tamuro è il contrario. I clienti singoli sono la metà, quasi il 90% delle prenotazioni viene fatto nel giorno stesso e i clienti parlano tra loro. Per adattarmi a questo carattere di Tamuro, ho costruito nel dettaglio il sistema di prenotazione, gli sconti e la finestra di chat. Poiché non generalizza, ha un'identità netta. Per questo diventa un motivo per cui i clienti lo scelgono.

E più il bar ha un'identità netta, più semi di strumenti trova. Più ci si confronta con il carattere del bar, più i guai diventano specifici. I guai specifici diventano strumenti specifici. Gli strumenti specifici aiutano altri bar che hanno lo stesso guaio.

L'IA ha reso possibile a un solo titolare fare entrambe le cose. Dare al bar un'identità netta e distribuire strumenti. Un tempo si doveva sceglierne una. Ora si possono fare entrambe.

Naturalmente è ancora un lavoro in corso. Il tasso di superamento della finestra di chat viene ancora alzato. Il manuale riceve aggiunte a ogni insuccesso. Come far crescere il locale diurno resta una sfida. Le persone che prenotano tramite l'IA non sono ancora molte.

Ciononostante, credo che il futuro del piccolo bar sia luminoso. Essere piccoli non è una debolezza. Poiché siamo piccoli, possiamo sperimentare in fretta, abbandonare in fretta e correggere in fretta. Poiché siamo piccoli, possiamo avere un'identità netta. E i guai di un bar con un'identità netta diventano strumenti e passano ad altri piccoli bar.

Ho scritto questo libro da un bar da 19 posti a Higashi-Nakano.

## Postfazione

Grazie di aver letto fin qui.

Quanto ho scritto in questo libro è una testimonianza aggiornata a ottobre 2026. Gli strumenti di IA cambiano forma nel giro di pochi mesi. Alcuni dei meccanismi che ho descritto potrebbero già avere assunto un'altra forma al momento della pubblicazione. Ciononostante l'ho messo per iscritto, credendo che la testimonianza di che cosa un piccolo bar ha costruito con l'IA e come, dove ha fallito e che cosa ha imparato, debba restare utile per un po'.

La serie Agenda: https://bontallc.com/agenda?via=b2-it-{{FMT}}

Seguire le mie attività: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Se capita di passare per Higashi-Nakano, passi da Tamuro. Si può prenotare dal sito di prenotazione, dalla finestra di chat «T-AI-MURO» del sito e, naturalmente, dalla propria IA.

Sito di prenotazione di Tamuro: https://tamuroreservation.vercel.app/?src=b2-it-{{FMT}}

Instagram di Tamuro: https://www.instagram.com/tamuro.higashinakano/

Per chi vuole provare a prenotare dall'IA. L'indirizzo di collegamento del server MCP di Tamuro è il seguente URL.

https://tamuroreservation.vercel.app/api/mcp

Nelle impostazioni della propria IA (come Claude o ChatGPT), apra la schermata per aggiungere strumenti esterni (connettori, server MCP) e registri questo URL. Il modo di registrarlo varia a seconda dell'IA e nel tempo, quindi la via più sicura è cercare «MCP» o «connettore» nella guida di ciascuna IA. A seconda del piano che si ha, potrebbe non essere possibile collegare un server MCP di propria scelta. Una volta registrato, chieda alla Sua IA: «C'è posto da Tamuro stasera?» Controllerà le fasce libere e i prezzi e La guiderà alla pagina di prenotazione. Il pulsante di conferma lo preme Lei.

Per chi viene dopo aver letto il libro. Quando prenota, inserisca il codice coupon «BOOK». Alla prima consumazione offriremo un drink della casa. Se si presenta senza prenotazione, basta dire «Ho letto il libro» al primo ordine. Offriremo lo stesso drink. È un piccolo accorgimento che mi permette di contare quante persone sono venute grazie al libro.

Si può entrare senza prenotazione. Anche chi viene senza compagnia non si sente fuori posto. Può anche capitare di finire a chiacchierare allegramente con la persona accanto.

La aspetto in un luogo dove le persone si riuniscono.

Raku Bonta

### Riferimenti

- OpenAI Help Center, «ChatGPT — Release Notes», 10 agosto 2026, «Restaurant reservations in ChatGPT» https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, «Alpaca MCP Server» (un esempio di server MCP negli Stati Uniti che permette all'IA di effettuare ordini di azioni e altri titoli) https://docs.alpaca.markets/docs/alpaca-mcp-server
- Il dibattito sulla «morte del SaaS»: le dichiarazioni di Satya Nadella nel podcast BG2 (dicembre 2024), il forte calo dei titoli software di febbraio 2026 e come è stato chiamato, e la replica di Jensen Huang sono tratti dai seguenti rapporti e commenti. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
