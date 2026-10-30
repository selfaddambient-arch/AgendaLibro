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
