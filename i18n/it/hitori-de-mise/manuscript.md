## Introduzione

Questo libro è una testimonianza aggiornata a gennaio 2026. Da allora alcune cose sono cambiate: il modo in cui gestisco il locale, i nomi e le specifiche degli strumenti di IA. Il seguito, *Costruito per il nostro bar*, riprende da lì il racconto.

### Perché chi veniva dal mondo dei sistemi parla con l'IA in un locale seminterrato

Grazie di aver preso in mano questo libro.

*Il locale lo gestisco da solo, e l'IA è arrivata al mio fianco.*

Davanti a questo titolo, alcuni di voi penseranno: «Sono proprio io». Altri si chiederanno: «Cosa vuol dire avere l'IA al proprio fianco?»

Questo non è un libro tecnico sulla programmazione complessa. È un libro per persone come Lei, titolari di locali che stanno ogni giorno in cucina, fanno la preparazione e sono sempre occupati con i clienti.

Mi presento brevemente.

Oggi gestisco un piccolo locale nel seminterrato di un palazzo a Higashi-Nakano *(un quartiere residenziale nella zona occidentale di Tokyo, subito a ovest di Shinjuku)*, a Tokyo.

Ha due volti. Di giorno è un locale specializzato in hamburger al curry *(hamburg steak alla giapponese servita con il curry)*, profumato di spezie. Di sera è un bar-ristorante con un menu fisso del giorno e bevande.

▼ Hamburger al curry Quatre Epice (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Hamburger al curry Quatre Epice (Instagram)](images/fig-01.png)

▼ Il bar «Tamuro» (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Il bar «Tamuro» (Instagram)](images/fig-02.png)

È uno spazio accogliente, con soli 11 posti al bancone e 8 su una piattaforma rialzata con tatami.

Ma non ci limitiamo a servire da mangiare.

Ogni due settimane organizziamo una serata dedicata al vino e, una volta al mese, un corso di cucina o una giornata con un menu speciale. Anche in un seminterrato piccolo, ho sempre da fare e sono in movimento ogni giorno.

Quest'anno sono dodici anni che gestisco il locale.

Prima lavoravo come dipendente in un'azienda. Mi occupavo di «pianificazione dei sistemi» e di «architettura delle soluzioni».

Quando lo dico, a volte la gente risponde: «Quindi era una persona che sviluppava sistemi importanti». In realtà non è così.

Quello che facevo non era scrivere codice complicato. Ascoltavo ciò che volevano le persone in prima linea, lo riferivo con precisione ai fornitori informatici (le società di sviluppo) e lo facevo realizzare. Facevo il «coordinatore». In Giappone questa figura si chiama «systems guy», l'addetto ai sistemi.

Chi lavorava in prima linea desiderava: «Vorrei che il mio lavoro fosse più facile». Gli ingegneri dicevano: «Servono requisiti definiti in modo logico».

Il mio compito era fare da tramite, interpretare il linguaggio di ciascuno e portare tutti all'obiettivo.

Per questo capisco i disagi e le preoccupazioni di chi, come Lei, i sistemi li usa, e capisco anche un poco che cosa pensa chi sta dalla parte informatica.

Dodici anni fa ho lasciato l'azienda e ho aperto il mio locale. Da allora ho le sue stesse preoccupazioni.

La preparazione che non finisce mai, la mancanza di personale, l'ansia di attirare clienti, le decisioni di gestione che devo prendere senza nessuno con cui dividerle...

Certo, quando c'è molto da fare a volte mi danno una mano collaboratori part-time e a contratto su cui posso contare.

Ma sono, in fondo, partner per i «compiti operativi».

Non c'è nessuno con cui confrontarmi sulle «decisioni di gestione» più pesanti, come «Come affronto il flusso di cassa del mese prossimo?» o «Devo scommettere su questo nuovo piatto?»

Mi preoccupo, decido e mi assumo ogni responsabilità. In questo senso ho sempre «gestito il locale da solo». E a sedersi accanto a me, come interlocutore per quel «me titolare» così solo, è stata l'IA.

In questa situazione è arrivata l'IA generativa, e in particolare un partner chiamato «Google Gemini».

Il «coordinamento» che un tempo facevo tra «la prima linea» e i «fornitori informatici», ora lo faccio io stesso tra «i problemi del locale» e l'«IA». E ho capito una cosa.

Non serve memorizzare la sintassi di linguaggi di programmazione complessi (come Python).\
Quello lo sa l'IA. Ma il disegno di «che cosa si vuole fare, e in quale ordine» lo può tracciare solo una persona.\
Quello che ho accumulato nel mondo dei sistemi era proprio questa «capacità di tradurre ciò che vuole la prima linea in passaggi logici».\
In questo libro condividerò, senza tenermi nulla, non solo come si usa l'IA, ma anche questo «istinto logico per far lavorare l'IA (pensiero sistemico)».\
Una volta che lo si ha, si passa da «zero conoscenze» al «miglior committente possibile».

※ Qui voglio dire con franchezza una cosa.

Vengo dal mondo dei sistemi. Ma negli usi dell'IA presentati in questo libro, in realtà quasi mai le conoscenze del mio vecchio lavoro mi sono servite direttamente.

Quello che è servito non era «la capacità di scrivere programmi».\
Era soltanto «l'abitudine di trasformare in parole ordinate le vaghe frustrazioni della prima linea».

E questa abitudine non è un talento speciale.\
È «un intuito che ha già qualunque titolare che gestisce un locale ogni giorno».

In questo libro separerò di proposito ciò che solo io potevo fare\
da ciò che Lei può copiare tale e quale, a partire da oggi.

## Capitolo 1: Concetti - Gli agenti IA, il nuovo tipo di dipendente

~ Assuma l'IA come «partner di lavoro», non come «semplice interlocutore» ~

### 1-1. I limiti del titolare che fa tutto da solo e i fraintendimenti sull'IA

Gestire un locale indipendente come il nostro è una corsa continua contro il tempo. Preparazione, cucina, servizio in sala, cassa, pulizie... tutto deve essere gestito da una sola persona, o da un piccolo gruppo.\
Anche se assumiamo personale, noi titolari indipendenti di fatto portiamo avanti un'«attività da una persona sola».

Il motivo è che non abbiamo «direttori di negozio» o «formatori» come le grandi catene.

Si cucina mentre si danno istruzioni al personale di sala, si insegna ai nuovi assunti e si gestiscono i turni.

Tutto questo «lavoro mentale» si concentra su una sola persona: Lei, il titolare.

Le mani possono aumentare, ma la testa resta una. Ed è proprio per questo che serve l'IA a sostenere quella «testa».

«Se solo avessi un altro buon collaboratore...»

Lo pensa certamente molte volte al giorno.

Quando dico «Usiamo l'IA», molti titolari rispondono così:

«Intendi ChatGPT? L'ho provato, ma scrive soltanto testi, no? Non serve per il lavoro pratico del locale».

In realtà qui c'è un grosso equivoco.

La maggior parte delle IA con cui abbiamo avuto a che fare finora erano dei «chatbot (semplici interlocutori)». Ma ciò a cui mira oggi l'IA più recente, a partire da Google Gemini, è la forma dell'«agente IA (partner di lavoro)».

I due si somigliano, ma sono cose diverse. Confrontiamoli con un lavoro concreto.

### 1-2. Da «dizionario» a «membro dello staff»

Supponiamo, per esempio, che Lei voglia fare un poster per un evento del locale.

Con l'IA di ieri (un chatbot):

Se chiede «Dimmi come si fa un poster», l'IA spiega i passaggi come un dizionario o un manuale: «Lo slogan deve essere breve», «Scegli i colori così».

Ma chi lavora davvero con le mani per realizzare il poster è Lei. Le sue conoscenze sono cresciute, ma il tempo di lavoro non si è ridotto.

Con l'IA di domani (un agente IA):

Basta dire: «Fai un poster».

A quel punto l'IA ragiona da sola per raggiungere l'obiettivo. Elabora lo slogan, genera l'immagine di sfondo e propone perfino l'impaginazione.

Come un ottimo collaboratore, usa gli strumenti, pianifica ed esegue il lavoro in piena autonomia.

Quello che vogliamo non è un consulente che dà consigli da manuale, ma un partner che suda accanto a noi.

※ In questo libro chiamerò con affetto questo partner affidabile (l'IA generativa come Google Gemini) il «vice responsabile (IA)».

※ In questo libro uso come esempio «Google Gemini», che uso soprattutto, ma la maggior parte delle idee presentate qui si può riprodurre quasi allo stesso modo con altre IA generative come ChatGPT e Claude.

Ciò che conta non è il nome dello strumento, ma «l'atteggiamento di trattare l'IA non come una spalla con cui parlare, ma come un partner a cui si può affidare il lavoro».

### 1-3. La «multimodalità» salverà i locali

C'è un'altra parola chiave fondamentale per gestire un locale. È «multimodale».

È un termine un po' tecnico, ma il significato è semplice.

Vuol dire «essere in grado di comprendere più tipi di informazioni insieme: non solo testo (leggere e scrivere), ma anche immagini (vedere e disegnare) e audio (ascoltare e parlare)».

L'IA tradizionale capiva solo le «parole». Ma il lavoro in un locale non va avanti solo con le «parole».

- L'aspetto degli ingredienti rimasti in frigorifero

- La scrittura a mano sulle comande

- Le voci dei clienti e l'atmosfera del locale

- La grafica dell'etichetta di una bottiglia di vino

Tutte queste sono «informazioni non verbali» che è faticoso mettere in parole.

Il vice responsabile (IA) le riconosce proprio come farebbe una persona.

Se con lo smartphone fotografa l'interno del frigorifero e la mostra all'IA, questa riconosce: «Ah, ha verdura e carne in avanzo» e da lì può proporre un menu.

In altre parole, l'IA di oggi è «un ottimo vice responsabile che vede, sente e parla».

※ Ma c'è una cosa che non voglio venga fraintesa.\
L'IA è più brava a dire cose che suonano plausibili che a dire cose corrette. Per il riconoscimento delle immagini, i numeri, le date e i nomi propri,\
La prego di usarla partendo dal presupposto che l'ultimo controllo lo fa sempre una persona.

Il motivo per cui in questo libro l'IA funziona bene è\
che io «non affido tutto all'IA e controllo sempre di persona».

### 1-4. Sostenga la sua «intuizione» con i dati

Le grandi catene hanno enormi quantità di dati dalle casse POS e team di marketing.

Noi titolari indipendenti, invece, abbiamo l'«intuito» e l'«esperienza». È l'arma più forte, ma a volte può diventare autoreferenziale o lasciare nell'incertezza.

Aggiungiamo dunque un «vice responsabile».

Faccia confrontare all'IA la sua intuizione, «penso che questo piatto piacerà ai clienti», con i «dati di vendita passati» e le «informazioni sulle tendenze».

Così si conservano il «calore» e la «personalità» che solo un locale indipendente può avere, e si gestisce comunque un'attività solida, fondata sui dati.

## Capitolo 2: Le basi - Il «vibe coding» a partire da zero conoscenze

~ I programmi non si «scrivono». Si «fanno costruire all'IA parlandole» ~

### 2-1. Nessuno legge un «lungo messaggio su LINE». La magia di un «diagramma» che richiede 30 secondi

Dire «costruisci un sistema con l'IA» può ancora sembrare un ostacolo un po' alto.

Cominciamo quindi da un «modo di usare l'IA» più familiare, che può usare subito, già da oggi.

È una rivoluzione nel «dare istruzioni al personale».

Molti titolari come me usano LINE *(l'app di messaggistica più diffusa in Giappone)* per contattare il personale.\
Di solito gestisco il locale con poche persone e, durante il servizio più intenso, non c'è tempo per dare istruzioni con calma.

Così gli avvisi finiscono inevitabilmente per dipendere dai messaggi su LINE dopo la chiusura.

Ma è estremamente difficile trasmettere solo a parole, a chi ha meno esperienza o a chi dà una mano ogni tanto, l'immagine di «lo voglio fatto così» che esiste solo nella mia testa.

Ed è da qui che nasce il «lungo messaggio su LINE».

Più si cerca di spiegare con cura, più il testo si allunga e, di conseguenza...

«Ah, scusa, non ho letto fin lì».

«Era tutto testo e non capivo quale parte fosse importante».

Errori come questi non capitano anche nel Suo locale?

Sono capitati anche a me.

Un giorno, per un'app che stavo sviluppando, ho provato a chiedere a un collaboratore di fare delle «foto degli ingredienti».

Le condizioni erano un po' complicate, così le istruzioni che ho scritto sullo smartphone sono diventate un lungo messaggio come questo.

![Il lungo messaggio su LINE che ho davvero inviato al personale, refusi compresi](images/fig-03.jpg)

Anche vedendolo, il personale di cucina, sempre di corsa, lo scorre in fretta pensando «Insomma, devo solo fare le foto, giusto?» e si lascia sfuggire le indicazioni su «angolazione» e «orientamento del contenitore».

Ma io non ho tempo di aprire PowerPoint, allineare le forme e preparare un foglio di istruzioni.

Così ho dato in pasto questo testo, così com'era, all'IA (uno strumento di IA come Manus o Gemini) e ho chiesto:

«Riassumi il contenuto di questo testo in una slide, come un "foglio di istruzioni di lavoro" che il personale possa capire a colpo d'occhio».

### 2-2. L'IA è un «ottimo traduttore»

Dopo qualche secondo di attesa, quello che l'IA ha prodotto era una «slide con un diagramma» sorprendentemente facile da capire.

![La slide «Istruzioni di lavoro per la raccolta dati e le fotografie» generata automaticamente dall'IA](images/fig-04.jpg)

Non ho curato nessuna grafica. Ho solo detto: «Ecco il testo, riassumilo».

Dal mio testo prolisso e disordinato l'IA ha capito all'istante «che cosa è importante» e «come va classificato», e lo ha «tradotto» in un'impaginazione che le persone afferrano d'istinto.

### 2-3. Liberi dallo «stress di non farsi capire»

Ho incollato questa immagine su LINE e l'ho inviata.

L'effetto è stato immediato.

Il collaboratore non ha fatto domande e al primo tentativo mi ha rimandato foto perfette, in «orientamento verticale» e con «3 angolazioni».

Fino ad allora mi irritavo con il personale pensando «Perché non leggono?» e mi preoccupavo: «Forse sono io che spiego male».

Ma la colpa non era né del personale né mia. Era della «comunicazione fatta solo di testo».

Questa esperienza ha cambiato il mio modo di vedere l'IA.

L'IA non è soltanto uno strumento per «creare da zero» nuovi testi e nuove immagini.

È «uno strumento che "converte" le nostre parole che faticano ad arrivare in una forma che raggiunge l'altra persona».

### 2-4. Il «vibe coding», un nuovo tipo di dialogo

Quando ci si è abituati a parlare con l'IA, viene finalmente il momento di «costruire strumenti».

Magari pensa: «Programmare non fa per me», ma non si preoccupi.

In questo momento, tra gli ingegneri, un termine chiamato «vibe coding» fa molto parlare di sé.

È un metodo in cui, invece di scrivere codice difficile a mano, si costruisce un sistema parlando con l'IA come se si cercasse un'intesa sulle «vibrazioni» (sensazione e atmosfera).

Sota Fujii, Meijin di shogi (detentore del titolo), ha citato il «vibe coding» come la novità che più ha acceso la sua passione nel 2025, quest'anno. Anche una figura del mondo dello shogi, che sembra del tutto estraneo alla costruzione di sistemi, a quanto si dice descrive all'IA in giapponese ciò che desidera e si costruisce strumenti pratici.

Parlando con l'IA, anche noi possiamo costruire sistemi senza conoscenze specialistiche.

Si usa soltanto la lingua di tutti i giorni (nel mio caso, il «giapponese»). Quando si dice «Vorrei che funzionasse così» oppure «Questa parte è scomoda da usare», il vice responsabile (IA) scrive il codice dietro le quinte.

In altre parole, non serve diventare un «programmatore».

Basta diventare il «direttore dei lavori» che dà istruzioni a un «ottimo ingegnere (IA)».

### 2-5. Le «lamentele» del Suo locale sono i prompt più efficaci

Le istruzioni all'IA (i prompt) non hanno bisogno di parole ricercate.

Il prompt più efficace che ho scoperto sono gli «inconvenienti» e le «frustrazioni» del Suo locale, cioè, in altre parole, le Sue lamentele.

- «Che fatica fare questo calcolo ogni giorno».

- «Non voglio ridimensionare le immagini a mano».

Per l'IA questi sono «requisiti di sviluppo» perfettamente validi.

Un sentimento come «non lo sopporto» fa emergere una soluzione concreta più facilmente di un obiettivo come «vorrei fare questo».

### 2-6. Un errore non è un «fallimento». È l'«inizio di un dialogo».

Quando comincerà a creare qualcosa con l'IA, incontrerà sicuramente un «errore».

Ma nel vibe coding un errore non è un fallimento.

È «il segnale che è iniziato un botta e risposta con l'IA».

Anche tra persone è raro che l'intenzione arrivi alla perfezione al primo colpo.

Quando l'IA segnala un errore, lo liquidi con leggerezza con un «Ah, il messaggio non è passato» e risponda: «No, quello che voglio è questo».

Continui lo scambio senza arrendersi. Se riesce a fare solo questo, anche con zero conoscenze potrà sicuramente costruire «un sistema che è soltanto Suo».

### 2-7. Aumentare drasticamente l'efficienza con i «pulsanti fisici»: usare una tastiera secondaria

Nel vibe coding la cosa più importante è «curare l'inserimento».

Più la conversazione con l'IA diventa veloce, meno il pensiero si ferma e più rapidamente procede lo sviluppo. Al contrario, se si perde tempo con l'inserimento, anche una grande idea può svanire.

Prima Le ho detto: «Quando compare un errore, la mossa giusta è fare uno screenshot e incollarlo».

Ma premere [Windows] + [Maiusc] + [S] (Mac: [Cmd] + [Maiusc] + [4]) decine di volte al giorno, selezionare un'area con il mouse, tornare alla schermata di Gemini e premere [Ctrl] + [V] (Mac: [Cmd] + [V])...

Francamente, stanca le dita, non è vero?

Così ho introdotto una «tastiera secondaria a 6 tasti».

È una piccola tastiera di produzione cinese, che costa da qualche centinaio a circa mille yen, e che compare cercando «tastiera programmabile» su Amazon o siti simili.

![Una foto della tastiera secondaria a 6 tasti che uso](images/fig-05.jpg)

A questi sei tasti ho assegnato le seguenti scorciatoie.

1.  Avvio dello screenshot

2.  Seleziona tutto (Ctrl + A; Mac: Cmd + A)

3.  Copia (Ctrl + C; Mac: Cmd + C)

4.  Incolla (Ctrl + V; Mac: Cmd + V)

5.  Invio (per inviare)

6.  (Di riserva)

Tutto qui. Ma l'effetto è enorme.

Compare un errore.

↓

Con la mano sinistra premo il «Tasto 1 (screenshot)».

↓

Seleziono l'area, poi sulla schermata di Gemini premo il «Tasto 4 (incolla)».

↓

Premo il «Tasto 5 (invio)».

Tutto questo richiede appena 2 secondi.

Non serve ricordare le scorciatoie da tastiera né muovere le dita in modo complicato.

Si possono lanciare informazioni all'IA come se si usasse il controller di un videogioco.

Come vedrà nei capitoli successivi, quando si corregge il codice sorgente che l'IA produce, seleziona tutto (Ctrl + A), copia (Ctrl + C) e incolla (Ctrl + V) permettono di rieseguirlo subito, ed è comodo.

Prima di studiare nozioni avanzate di programmazione, provi a procurarsi questo piccolo accessorio.

Eliminare fisicamente la «fatica dell'inserimento». È la scorciatoia più rapida per rendere più veloci le conversazioni con il Suo partner IA.

## Capitolo 3: Pratica 1 - Automatizzare il lavoro creativo e attirare clienti

~ «Incollare uno screenshot e affidare tutto» si è rivelato il metodo di sviluppo più forte ~

### 3-1. Tentativi ed errori per cancellare l'«aspetto da IA» (adesivi per LINE)

Presa confidenza con il dialogo a testo (vibe coding), ho deciso di affrontare finalmente la «generazione di immagini».

Per esercitarmi ho scelto di creare degli «adesivi per LINE», che possono anche aiutare a costruire una schiera di appassionati del locale.

Ma le «immagini lisce, da grafica al computer» tipiche delle immagini generate dall'IA non si adattano all'atmosfera del mio locale.

Quello che puntavo a ottenere era «un design piatto, retrò, in stile anni Ottanta, con un tocco disegnato a mano, che mantenga la consistenza del pastello a cera e del pennello».

Da qui è cominciato un lungo «dialogo» tra me e il vice responsabile (IA).

All'inizio ho cominciato con personaggi di «due ragazzi e uno Shiba Inu».

«Dammi 25 modelli di conversazione quotidiana».

«Rendi lo spessore delle linee irregolare, come pennellate».

Uno per uno, come se dessi indicazioni di correzione a un illustratore in carne e ossa, gli ho insegnato con pazienza il gusto che preferisco.

![Illustrazioni generate per gli adesivi di LINE](images/fig-06.png)

### 3-2. La richiesta audace: «Cambia solo il cane in un gatto»

Quando le cose avevano preso una certa forma, ho deciso un cambio di rotta importante: «In realtà vorrei che fossero due ragazze e un gatto».

Un illustratore normale farebbe una smorfia e direbbe: «Cosa, ricominciare da capo?». Ma il vice responsabile (IA) non si è lamentato nemmeno una volta.

«Cambia i personaggi in due ragazze, una con i capelli lunghi e una con i capelli corti. Vestiti gialli e verdi, nello stesso stile disegnato a mano di prima».

«Cambia il cane in un gatto, passa alle parole da gatto che hai generato prima e crea pose adatte».

«Fai un gatto siamese, non un soriano rosso».

In più ho fatto una richiesta che metteva alla prova i limiti dell'IA.

«Mantieni esattamente la composizione di "ragazzi e Shiba Inu" che hai fatto prima, e riscrivi solo la parte del cane come un gatto siamese».

Con mia sorpresa, l'IA ha capito questa istruzione complicata. Le posizioni e le pose dei ragazzi sono rimaste le stesse, mentre l'animale è stato sostituito con ordine da un «gatto siamese».

![Il foglio di illustrazioni finito per gli adesivi di LINE](images/fig-07.png)

Tuttavia, per usarle come adesivi su LINE bisogna dividere le illustrazioni, creare le miniature, comprimere tutto in un file ZIP e caricarlo.

Anche questo si può fare dialogando con Gemini, ma lo spiegherò di nuovo più avanti, nel paragrafo 3-6. Il primo ostacolo: la semplice suddivisione e la «trappola della qualità dell'immagine».

### 3-3. Caso 2: Il «banner di Natale» realizzato in 22 scambi di dialogo

Dopo gli adesivi di LINE, c'è un altro lavoro importante che ho fatto mano nella mano con l'IA. È il banner di annuncio per la «cena di Natale», l'evento più importante dell'anno per il locale.

Ho usato un'IA chiamata «Nano Banana» (il modello di generazione di immagini integrato in Gemini di Google).

#### Fase 1: Regolare impaginazione e testo

All'inizio ho cominciato disponendo gli elementi necessari (Babbo Natale, renne, informazioni testuali) su una tela larga.

Guardando le immagini uscite, ho dato le istruzioni.

«Sembra un po' vuoto. Aggiungi illustrazioni di un albero di Natale e dello champagne».

«Il menu è un elenco puntato ed è difficile da leggere. Riassumilo come "sei portate in tutto" e ingrandisci il titolo rendendolo più appariscente».

![L'immagine generata nella fase iniziale. Sembra ancora un po' vuota](images/fig-08.png)

#### Fase 2: Regolare la «vivacità»

Fissata l'impaginazione, è venuta l'atmosfera. Mancava il «clima di festa».

Ho indicato: «Rendilo più vivace! Spargi tanti piccoli Babbo Natale e renne, palloncini e coriandoli».

Questa volta la schermata è diventata fin troppo affollata.

«Scusa, erano troppi elementi. Riduci una volta i personaggi e rendilo pulito».

Poter ripetere questa messa a punto di «aggiunte e sottrazioni» è il punto di forza dell'IA.

#### Fase 3: L'idea inattesa di «rifare tutto»

A metà lavoro mi è venuto un dubbio. «Non sembrerebbe più appetitoso mostrare immagini dei piatti, invece di mettere i personaggi al centro?»

Così ho indicato con decisione: «In alternativa, crea un design che abbia come elemento principale le illustrazioni dei piatti veri e propri».

![Proposta di illustrazione con i piatti in primo piano (alcuni testi sono illeggibili)](images/fig-09.png)

L'IA ha subito pensato a idee di illustrazioni di cibo appetitose, ma dopo averle confrontate ho deciso di tenere comunque il design originale con i personaggi. Anche un «torniamo a com'era» come questo si può chiedere all'IA senza esitazioni.

#### Fase 4: L'ultima linea di difesa è l'occhio «umano»

Stabilito il design finale, ho lasciato all'IA anche le varianti di formato, per i post di Instagram (verticale) e per le Storie (ancora più alto).

E proprio quando stava per essere finito, ho notato un errore grave.

«Aspetta, il giorno della settimana accanto alla data è sbagliato!»

L'IA è brava a disegnare immagini, ma non capisce i giorni della settimana di un calendario. Se l'avessi pubblicato così com'era, sarebbe stato un disastro.

Ho indicato in fretta: «Correggi la data in "24/12 (mer) e 25 (gio)"!» e ho concluso la versione finale.

![Il banner finale dopo la correzione](images/fig-10.png)

In totale 22 giri di correzioni e dialogo.

L'IA non è una bacchetta magica, ma se si dialoga con pazienza non esiste un partner di design più affidabile.

### 3-4. Caso 3: Un avviso di apertura per il nuovo anno che evolve con la situazione

L'entusiasmo del Natale si è appena spento che arriva il prossimo evento: l'attività di fine e inizio anno.

Per un ristorante o un bar, in questo periodo dell'anno far girare la voce è una corsa contro il tempo. «Fino a quando siete aperti a fine anno?» «Quando riaprite nel nuovo anno?» I clienti cercano sempre informazioni.

Ma le informazioni cambiano di minuto in minuto.

«Finito il servizio di fine anno, voglio riscrivere il tutto in modo che mostri solo l'avviso per il nuovo anno».

«L'ho pubblicato su X (orizzontale), ma voglio farlo girare anche su Instagram (verticale)».

Se l'avessi chiesto a un grafico esterno, già le spese per le modifiche sarebbero state un incubo e, soprattutto, non sarebbe stato pronto in tempo.

Così ancora una volta ho fatto squadra con un'IA di generazione di immagini (Nano Banana) e ho iniziato a lavorare sui banner che mi accompagnassero lungo il periodo di fine e inizio anno.

#### Passo 1: Lo stile è «disegno a pastello degli anni Ottanta»

Per prima cosa ho costruito l'aspetto e il tono generale.

Quello che si addice al mio bar non è la grafica patinata al computer.

«Uno stile caldo, come un disegno a pastello a cera fatto a mano negli anni Ottanta, con pennellate visibili. Lascia lo sfondo bianco semplice».

Con questa istruzione come nucleo, e pensando a un annuncio su X (già Twitter), ho iniziato a lavorare su una tela orizzontale.

#### Passo 2: Il serpente che se ne va e il cavallo che arriva. Un brindisi per passare il testimone

All'inizio avevo pensato di disegnare un solo animale dello zodiaco, ma si trattava pur sempre del passaggio d'anno.

Mi è venuta un'idea: «Voglio che compaiano sia l'animale dell'anno che finisce (il segno zodiacale di quest'anno) sia quello dell'anno che arriva (il prossimo)».

Così ho dato all'IA questa istruzione:

«Metti un gruppo di serpenti (l'anno del Serpente) sul lato sinistro dello schermo e un gruppo di cavalli (l'anno del Cavallo) sul lato destro. Fai in modo che ciascuno tenga un boccale di birra e brindi allegramente, come se si passassero il testimone a fine anno».

L'immagine generata dall'IA era esattamente quella che avevo immaginato.

Serpenti simpatici a sinistra, cavalli dall'aria affidabile a destra, che bevono insieme oltre il confine tra le specie.

Dalla «fine dell'anno (Serpente)» al «nuovo anno (Cavallo)».

In una sola immagine, il passare del tempo e l'atmosfera di festa erano condensati in modo splendido.

![Un'immagine generata con un serpente a sinistra e un cavallo a destra che brindano, a rappresentare l'anno vecchio che cede il posto al nuovo](images/fig-11.png)

#### Passo 3: «Regia» e «prova costumi» per gli animali

Definita la composizione, il lavoro successivo era la messa in scena più fine. Anche qui l'IA ha sopportato le mie pretese puntigliose.

Nelle prime immagini gli animali stavano semplicemente in fila, oppure reggevano i boccali in modo innaturale.

«Falli sembrare più felici! Come clienti abituali che si divertono insieme».

«Voglio anche un tocco stagionale. Mettigli sciarpe e papillon, dagli un aspetto invernale».

Con quella sola osservazione, gli animali sullo schermo si sono avvolti in sciarpe rosse e verdi dall'aria calda e si sono trasformati all'istante nei protagonisti di una «festa d'inverno».

«Sì, adesso ha quel calore di quando si beve di giorno nelle giornate fredde».

Guardando bene, alcuni movimenti delle mani e il modo di tenere i boccali sono ancora innaturali. Ma essere pignoli significa impiegare più tempo. Bilanciando il tempo con quanto bene arriva il messaggio, mi accontento di un risultato abbastanza buono.

#### Passo 4: Con il passare del tempo, le informazioni cambiano

Da qui in poi l'IA mostra davvero il suo valore.

Il banner originale mostrava insieme gli orari di dicembre e di gennaio come «Programma di apertura di fine e inizio anno».

Ma passato il 31 dicembre, le informazioni di fine anno non servono più.

Ho aperto il progetto su cui stavo lavorando e ho chiesto una modifica importante al testo.

1.  Cambiare il titolo: da «Orari di fine e inizio anno» a «Si riapre l'anno con l'aperitivo di giorno».

2.  Sistemare le informazioni: eliminare il programma di dicembre ormai passato e restringere il tutto al solo «programma del nuovo anno (2/1–4/1)».

3.  Correggere i personaggi dello zodiaco: trasformare in cavalli i serpenti dell'anno che finisce.

4.  Aggiungere un richiamo: aggiungere un'offerta allettante, «highball e pollo fritto a volontà», come nuova attrattiva per i clienti.

![Passo 4: Con il passare del tempo, le informazioni cambiano](images/fig-12.png)

Senza ricreare l'immagine da zero, ho potuto rinnovare le informazioni come se riscrivessi le parole su una lavagna. È questo il punto di forza del design con l'IA.

#### Passo 5: Da X a Instagram. Un formato che cambia a piacere

E ora, il tocco finale.

«L'ho annunciato su X. Adesso lo voglio pubblicare nelle Storie di Instagram».

Ma le Storie usano il formato «verticale», che riempie tutto lo schermo dello smartphone. Se si inserisce un'immagine orizzontale così com'è, restano fasce vuote sopra e sotto, e l'effetto è brutto.

Con una normale illustrazione, un cambiamento del genere significherebbe ridisegnarla.

Ma io ho solo detto all'IA:

«Mantieni questo design, ma riorganizzalo in un'impaginazione verticale per le Storie di Instagram».

L'IA ha riorganizzato in verticale gli animali che erano sparsi in orizzontale, ha regolato l'equilibrio del testo e ha generato all'istante un design su misura per gli smartphone.

![L'immagine verticale finita per le Storie di Instagram](images/fig-13.png)

### 3-5. Caso 4: La creazione del logo del bar - Un dialogo che trasforma il «significato» in «forma»

Oltre alle «immagini» come banner e adesivi, con l'IA ho affrontato anche una sfida più astratta: progettare un nuovo logo.

Deve essere inserito nei banner e simili, così che si riconosca Tamuro a colpo d'occhio.

Il soggetto è Tamuro, il bar che gestisco la sera. Questo nome porta con sé un forte desiderio: «essere un luogo dove ogni genere di persone si riunisce liberamente e con gioia (tamuro-suru, ritrovarsi a stare insieme) nel quartiere di Higashi-Nakano».

Come condensare questa «storia» invisibile in un piccolo marchio? È cominciato un paziente dialogo con l'IA.

#### Passo 1: Scegliere il lettering e la direzione del design

All'inizio ho lanciato all'IA idee come «un aspetto sobrio con il kanji 屯» e «qualcosa di vivace in katakana», e ho fatto preparare qualche bozza.

Ma nessuna mi convinceva. Data la natura del bar, volevo qualcosa di più moderno, con un'impronta neutra che accogliesse la diversità.

Così ho cambiato strada.

«Partiamo dalla scritta in caratteri latini, molto versatile, "TAMURO". Lo stile deve essere un "design piatto" senza decorazioni complicate. E il colore deve risultare forte anche in tinta unica».

L'IA ha subito proposto un "TAMURO" semplice, in un carattere sans-serif deciso.

![Il logo in carattere sans-serif](images/fig-14.png)

#### Passo 2: Dare un «significato» alla forma

Qui comincia la vera prova. Le lettere semplici non significano nulla. E avere solo la «M» al centro non comunica molto.

«Voglio esprimere l'origine del nome, "persone che si riuniscono". Potresti raccogliere il tutto in un "cerchio" amichevole, dando a ogni lettera dell'alfabeto una forma che sembri una persona che si muove con gioia?»

È una richiesta molto astratta. Ma l'immaginazione del mio vice responsabile (l'IA) ha superato le mie aspettative.

Quello che l'IA ha ideato era un design in cui gli scheletri delle lettere «T», «A», «M» e le altre si trasformavano in sagome di persone che ballano con braccia e gambe allargate.

![Un logo che trasforma l'alfabeto in persone](images/fig-15.png)

#### Passo 3: Il tiro alla fune tra design e leggibilità

«Interessante! Ma così non si legge "TAMURO"...»

Se si dà troppo peso al design, non si riconosce più come scritta e, se si dà peso alla scritta, perde il suo fascino. Ho incontrato proprio questo dilemma.

Da qui in poi si è trattato di ripetute messe a punto.

«La lettera "A" sembra una persona, ed è un bene, ma enfatizza un po' di più la sua struttura di "A". Metti bene la barra trasversale».

«L'equilibrio generale va bene, ma le persone sono troppo vicine e sembrano strette. Lascia un po' più di spazio allegro».

«Combina le persone che ballano di prima con le lettere TAMURO e fanne un cerchio!»

![Il marchio circolare «TAMURO», completato dopo tentativi ed errori](images/fig-16.png)

Pur essendo fatto di vivaci sagome di persone, basta uno sguardo alla parte inferiore per leggere chiaramente «TAMURO».

Scambiandoci idee con l'IA più e più volte, ho ottenuto un logo che mi soddisfa, che fonde leggibilità, qualità del design e, soprattutto, il «desiderio» che ho riposto nel bar.

Ora è usato come icona degli account X (già Twitter) e Instagram del bar.

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

## Capitolo 5: Applicazioni - Analisi aziendale e miglioramento dei profitti

~ Portare alla luce la «miniera d'oro invisibile». Una riunione di gestione con il proprio consulente IA ~

### 5-1. La notte in cui mi spremo le meningi sulla calcolatrice, alla fine di ogni mese

Per chi di noi ha un piccolo ristorante indipendente, nessun momento pesa come la chiusura mensile dei conti.

Nel silenzio della notte, mentre si sommano i dati della cassa e li si digita in Excel, si sente soltanto il proprio sospiro.

«L'obiettivo di vendite di questo mese era ○○0.000 yen. ...L'ho mancato».

«Il numero dei clienti non è male. Nel fine settimana eravamo pieni. Ma, chissà perché, la spesa per cliente non cresce».

Perché non riesco a raggiungere l'obiettivo? Il cibo dovrebbe essere buono. Mi impegno sul servizio.

«Forse i prezzi sono troppo alti?»

«No, se scendo ancora non faccio profitto. E anche il costo degli ingredienti sta salendo».

Le domande senza risposta girano e rigirano nella mia testa e alla fine chiudo con un discorso di pura grinta: «Il mese prossimo ci metterò più grinta e spingerò di più i consigliati». Questa era la mia cattiva abitudine, e quella di molti titolari.

Ma ora ho un consigliere senza emozioni.

Ho presentato a Gemini i dati di vendita di quel mese e i dati del menu del locale.

### 5-2. Un esperimento: far leggere all'IA «immagini» e «numeri» nello stesso momento

Questa volta ho dato a Gemini tre informazioni.

Ho buttato dentro, tutte insieme, il «design (emisfero destro)» e i «numeri (emisfero sinistro)» che avevo sempre gestito separatamente.

1.  «L'obiettivo di vendite di questo mese»

- Il mio desiderio sincero. Il numero che devo assolutamente raggiungere.

2.  «Tutti i dati dei recenti scontrini di vendita (CSV/Excel)»

- Il risultato nella realtà. I fatti freddi di chi ha ordinato che cosa, e a quale prezzo.

3.  «Un file PDF del menu attuale»

- Il mondo che vedono i clienti. Informazioni visive come la posizione delle foto, la dimensione e il colore del testo.

E poi ho chiesto questo.

Non era un ordine di lavoro come il precedente «crea un'immagine». Era una domanda, di quelle che pone un titolare.

> «Confronta i dati di vendita attuali (realtà) con l'impaginazione del menu (aspetto).
>
> Indica il collo di bottiglia: che cosa ci manca per raggiungere l'obiettivo di ○○0.000 yen?»

### 5-3. Il «presupposto del titolare» che l'IA ha smascherato

Pochi secondi dopo è arrivata la risposta di Gemini, e ha colpito proprio il mio punto cieco.

Mi aspettavo consigli generici come «Sviluppiamo un nuovo piatto per il menu» oppure «Facciamo promozione sui social».

Ma quello che l'IA ha indicato era un fatto che avevo cercato di nascondere senza rendermene conto.

La risposta di Gemini:

> «Incrociando i dati con il menu, ho trovato una grande occasione mancata.
>
> La formula di bevute a volontà, che ha un margine di profitto alto e può aumentare con sicurezza la spesa per cliente, è attualmente indicata sul menu (Prima) solo con del testo, discretamente, in fondo a sinistra.
>
> Nel frattempo, il posto migliore del menu, in cima, è occupato dal "Set a ¥2.200 (circa $15)" a basso prezzo. In questo modo i clienti scivolano verso la formula più economica e non si accorgono nemmeno dell'opzione a volontà dal prezzo più alto».

Guardando lo schermo, non ho potuto fare a meno di mugugnare. Aveva perfettamente ragione.

Una formula a volontà ce l'abbiamo. Ma da qualche parte nella mia mente pensavo questo:

«Non siamo una catena di izakaya *(un pub giapponese informale che serve cibo e bevande)*. Vendere le bevute a volontà a caratteri grandi fa sembrare a buon mercato».

«Voglio che la gente assapori il gusto del vino, quindi dovrebbe ordinarla solo chi ne è a conoscenza».

Quel mio «presupposto» si vedeva nell'impaginazione del menu, nel testo in fondo.

![Il menu Prima. L'indicazione delle bevute a volontà è in basso a sinistra e non risalta. È anche difficile capire che il cibo è a parte](images/fig-21.png)

L'IA non se n'è lasciata sfuggire nulla.

«Titolare, vuoi raggiungere il tuo obiettivo, giusto? Allora dovresti mettere in cima, con orgoglio, il percorso che vuoi vendere di più, quello con le bevute a volontà».

### 5-4. Niente immagini a disposizione? Allora facciamo disegnare anche quelle all'IA

Ho deciso. «Se fare l'elegante serve solo a far calare le vendite, tanto vale provare a ogni costo».

Ma a quel punto è sorto un problema.

«Anche se lo metto grande in cima, il solo testo è debole...»

E se prendo da un sito di foto gratuite una foto di persone che brindano con la birra, subito sembra un ristorante di catena. Non si adatta all'atmosfera del mio locale.

Non ho talento per il disegno e assumere un illustratore costa denaro e tempo.

Ho iniziato a preoccuparmi, «Che cosa faccio...?», ma poi mi è tornato in mente subito.

«Giusto, ho un vice responsabile (l'IA) che sa disegnare».

Avevo trovato su un sito di materiali qualcosa di vicino all'immagine che volevo. Diceva che le modifiche erano consentite.

Ho digitato nella casella di chat questo:

> «Disegna un'illustrazione da mettere in cima al menu. Usa come base l'immagine allegata.
>
> Voglio la sensazione di persone che brindano felici, ma senza sembrare a buon mercato.
>
> Per favore, fallo in uno stile semplice, a linee essenziali».

Pochi secondi dopo sono comparse sullo schermo quattro proposte di illustrazione.

Tra queste ho scelto l'illustrazione «Cheers!», semplice e calda, che meglio si accordava con l'atmosfera del locale.

![L'illustrazione «Cheers!» generata dall'IA in soli 10 secondi](images/fig-22.png)

Ci sono voluti solo 10 secondi.

Non solo l'analisi: anche il «materiale» necessario al miglioramento si può procurare sul momento.

È questa la vera forza di integrare l'IA generativa nella gestione.

### 5-5. Cambiare soltanto l'impaginazione ha aumentato di circa il 40% la spesa per cliente

Così ho ridisegnato il menu.

#### Prima: il menu com'era

- Posto migliore (in cima): prodotti a basso prezzo come il «Set a ¥2.200 (circa $15)» e il «Set Menu a ¥3.300 (circa $22)».

- Bevute a volontà: indicate solo con del testo, nell'angolo in basso a sinistra, come «Bevute a volontà da ¥3.000 (circa $20)». Erano completamente sepolte.

#### Dopo: il menu rivisto

- Posto migliore (in cima): formule di prezzo alto da ¥4.500–¥5.700 (circa $30–$38), presentate come «Il nostro consiglio! Percorso Piacere Pieno (con bevute a volontà)».

- Design: con l'aggiunta dell'illustrazione «Cheers!» generata dall'IA, guida con forza lo sguardo, visivamente, verso «Guarda prima qui».

- Cambio di impaginazione: i set economici che prima erano le star sono stati spostati più in basso.

![Il menu Dopo. Il percorso con le bevute a volontà è collocato in cima](images/fig-23.png)

In realtà il cibo, i prezzi e la qualità delle bevande sono quasi invariati. Ho cambiato solo «come è mostrato» e «dove».

E il risultato?

Dal giorno dopo, il comportamento d'ordine dei clienti è cambiato in modo drastico.

Le prime parole dei clienti che aprivano il menu non erano più «Intanto una birra», ma «Allora prendiamo questo "Percorso Consigliato (¥4.900 (circa $33))" con l'illustrazione».

I clienti che prima chiudevano con «il Set (¥2.200 (circa $15)) più due drink» (una spesa di circa ¥3.500 (circa $23) a testa) ora sceglievano fin dall'inizio il percorso da ¥4.900 (circa $33).

Solo con questo, la spesa per cliente è salita di ¥1.400 (circa $9,3).

Inoltre, i clienti avevano anche il vantaggio di «poter bere senza pensare al conto», quindi la soddisfazione è aumentata anziché calare.

### 5-6. Verificare i risultati con il PDF delle vendite di dicembre (PDCA)

Era passato un mese da quando avevo messo in pratica l'iniziativa.

Non fermarsi qui è l'essenza dell'uso dell'IA.

Molti titolari giudicano i risultati a sensazione e si fermano lì: «Eravamo pieni, quindi avrà funzionato» oppure «Le vendite sono salite, quindi va bene».

Ma ho interpellato di nuovo Gemini.

Questa volta ho caricato il «PDF dei dati di vendita di dicembre», in cui c'erano i risultati, e ho chiesto questo:

> «I risultati dell'iniziativa del mese scorso (il cambio del menu) sono arrivati.
>
> Guarda questi dati di vendita di dicembre e verifica i risultati (valuta): gli ordini del "Percorso Consigliato" sono aumentati come previsto e come hanno influito sulla spesa per cliente?»

Gemini ha analizzato i dati all'istante e mi ha rimandato un rapporto.

![La schermata del rapporto di analisi delle vendite di Gemini: ho preparato un riassunto per la pubblicazione, quindi il contenuto in parte differisce dal testo qui sotto](images/fig-24.png)

L'analisi di Gemini:

> «Sono risultati eccellenti. Guardando l'andamento dei dati, gli ordini del "Percorso Piacere Pieno" sono saliti a circa 1,8 volte rispetto al mese precedente.
>
> Di conseguenza, la spesa complessiva per cliente è salita in media di ○○ yen.
>
> Il fattore principale è che collocare più in alto la formula a volontà ha aumentato il valore degli ordini, soprattutto per i gruppi».

Sentendo quelle parole, per la prima volta ho provato una vera tranquillità.

Non «in qualche modo abbiamo guadagnato», ma la sicurezza di «ho mirato e ho fatto i numeri».

Questo diventa la spinta per l'iniziativa successiva.

1.  Plan (pianificare): guardare i dati di vendita e il menu e individuare il problema (la formula a volontà è nascosta).

2.  Do (fare): far disegnare un'illustrazione all'IA e cambiare l'impaginazione del menu.

3.  Check (verificare): farle leggere il PDF delle vendite di dicembre e verificare i risultati.

4.  Act (agire): pensare, come passo successivo, a rivedere l'impaginazione del menu dei piatti.

Il «ciclo PDCA» che le grandi aziende portano avanti con costi enormi può essere portato avanti da un singolo titolare come me, con il solo smartphone, se ha l'IA come partner.

## Capitolo 6: Sfide - Sviluppare un sistema fatto apposta per il mio locale

~ «Se non esiste, lo costruisco». Un progetto di sviluppo di sistema senza esperti ~

※Per chiarezza, non serve fare tutto quello che c'è in questo libro.

・Inviare un'immagine e far scrivere un testo all'IA\
・Trasformare un lungo messaggio di LINE in un diagramma

Questi due bastano per cominciare. Già così il lavoro diventerà senz'altro più facile.\
Basta anche leggere questo libro come un racconto e pensare: «Allora con l'IA si può fare perfino questo».

### 6-1. Le app già pronte non arrivano proprio dove serve a me

Finora ho parlato dell'uso dell'IA sopra piattaforme esistenti, come la generazione di immagini e l'analisi del menu.

Ma continuando a gestire un'attività emergono preoccupazioni che le «app già pronte» semplicemente non riescono a risolvere.

In particolare, per un modello di attività irregolare come il nostro, «curry di giorno, bar di sera», anche il flusso del denaro in entrata e in uscita è complicato.

«Voglio confrontare il saldo del mio conto PayPay Bank con i pagamenti in arrivo e sapere la cifra a cui arriverò a fine mese».

«Le date di pagamento sono divise tra il 10 e il 25. Voglio simularle».

I software di contabilità in circolazione sono molto capaci, ma nessuno individuava «la preoccupazione che ho in testa adesso».

Così ho deciso.

«Se non esiste, lo costruisco io. Ho Gemini, il miglior ingegnere».

### 6-2. Fasi 1–3: dagli appunti scarabocchiati al «cloud»

Lo sviluppo è cominciato mostrando a Gemini i miei appunti su Google Keep.

![La nota di Keep che è stata il punto di partenza dello sviluppo](images/fig-25.png)

#### Fase 1: Costruire la logica

«Voglio automatizzare i calcoli di questa nota».

In risposta alla mia richiesta, Gemini ha messo insieme rapidamente la logica di calcolo.

- Quando cambio l'importo di una voce, calcola subito il saldo finale.

- Se i fondi stanno per scarseggiare, mostra un «avviso» in rosso.

- Simula le scadenze dei pagamenti divise tra «il 10» e «il 25 / fine mese».

- I dati vengono salvati nel browser (cache).

Già questo era abbastanza comodo, ma ho voluto di più. «Voglio che i dati restino anche quando chiudo il browser. Voglio poterli controllare anche sullo smartphone».

#### Fase 2: Adottare uno strumento sconosciuto, «Firebase»

Pensavo di collegarmi a un foglio di calcolo, ma il suggerimento di Gemini è stato inatteso.

«Se pensi alle prestazioni in tempo reale e all'efficienza, usiamo "Firebase" di Google. Il livello gratuito basta per farlo funzionare».

«Firebase...?» Non avevo mai sentito il nome. Ma con l'istinto dei miei tempi da coordinatore di sistemi ho deciso: «Se l'IA lo raccomanda con tanta convinzione, proviamo».

Il risultato è stato che, usando un database chiamato Firestore, i dati hanno cominciato a essere archiviati al sicuro nel cloud.

#### Fase 3: Login con Google e un sistema di approvazione

Si tratta di denaro, quindi non va bene che possa vederlo chiunque.

All'inizio avevo pensato a qualcosa come una «frase d'accesso», ma Gemini ha suggerito: «Se vuoi una sicurezza maggiore, usiamo il login con Google».

Poi, quando ho detto: «Voglio che possa vederlo solo il personale che approvo io», ha costruito perfino «un sistema in cui un amministratore può approvare e rimuovere i membri direttamente a schermo».

### 6-3. Fasi 4–5: affrontare lo schermo nero (il terminale)

Da qui è arrivato il più grande ostacolo del vibe coding: pubblicare l'app su internet (il deploy).

#### Avvertenza: da qui in poi è il corso da «cintura nera»

Le prossime pagine sono la parte «pratica» più difficile di questo libro. Si userà uno «schermo nero (terminale)» come quelli degli hacker nei film.

Parlo con franchezza. Qui riceverà sicuramente degli errori. Anch'io ne ho avuti. Incontrerà muri come un «errore di autorizzazioni di PowerShell» che sembra una formula magica. Ma non abbia paura. Quello che si fa qui è lo stesso: basta «fare uno screenshot della schermata di errore e lanciarlo all'IA».

La verità che ho imparato ai tempi in cui lavoravo nei sistemi è questa: «Anche i professionisti ricevono errori. L'unica differenza è se, quando compare un errore, si molla oppure si cerca (si chiede) aiuto». Se Le sembra troppo difficile, salti questa sezione e porti via soltanto la possibilità: «Con l'IA si può fare perfino questo».

Gemini ha detto:

«Prepariamo l'ambiente di sviluppo sul tuo PC Windows. Installa "Node.js" e digita i comandi seguenti in "VS Code"».

Ho aperto lo schermo nero (terminale) come indicato e subito è comparso un errore.

«Impossibile eseguire a causa delle restrizioni di sicurezza di PowerShell».

Un titolare comune qui si perderebbe d'animo.

Ma io ho copiato e incollato la schermata di errore e l'ho lanciata all'IA.

L'IA ha risposto subito: «Togli la restrizione con un comando chiamato "Set-ExecutionPolicy"».

Senza capire che cosa significasse, ho digitato il comando, poi npm run build, firebase deploy...

Ogni volta che digitavo quei caratteri da formula magica, il testo scorreva sullo schermo e il processo andava avanti.

E alla fine la mia app è comparsa sul web.

#### Fase 5: Trasformarla in un'app per smartphone (PWA)

L'app pubblicata era all'inizio in uno stato «spoglio», con il design rovinato, ma anche questo si è risolto aggiungendo un'impostazione chiamata «Tailwind CSS».

Poi, quando ho chiesto «Voglio mettere un'icona sulla schermata iniziale del telefono e usarla come un'app», mi ha insegnato le impostazioni per renderla una «PWA (Progressive Web App)».

E così, dentro il mio telefono è nata un'app dedicata, fatta da me (senza scrivere una sola riga di codice).

![La schermata dell'app finita per la gestione del flusso di cassa](images/fig-26.png)

### 6-4. Fase 6: Il problema dopo 30 giorni e la correzione

Circa un mese dopo aver iniziato a usarla, è sorto un problema.

«Fino a ieri funzionava, e all'improvviso non riesco ad accedere!»

Nel panico, ho consultato Gemini, e la causa era in un punto inatteso.

«Le impostazioni del database (Firestore) erano ancora in "modalità di prova (limitata a 30 giorni)". È scaduta».

Per risparmiare la fatica di configurare tutto all'inizio dello sviluppo, l'IA aveva impostato di proposito una regola con una data di scadenza.

«Riscriviamo le regole di sicurezza in modo che "qualunque utente connesso possa continuare a usarla"».

Quando, seguendo le indicazioni dell'IA, ho riscritto qualche riga del file delle impostazioni, l'app è tornata a funzionare senza problemi.

Anche questo inconveniente è stato per me una buona esperienza.

Ho imparato che «un sistema è una cosa viva e richiede manutenzione».

E ho acquisito la rassicurante certezza che «anche se succede un guaio, c'è sempre una risposta se lo chiedo all'IA».

### 6-5. Caso di studio 2: Il «progetto di riconoscimento facciale» nato da un video dimostrativo su X (già Twitter)

Ecco un altro sviluppo di sistema che ho affrontato, e il più grande.

È «un sistema che riconosce i clienti che entrano tramite una telecamera e mi dice discretamente il loro nome, i loro dati e le loro preferenze».

Tutto è cominciato dal social media X, che stavo scorrendo distrattamente.

Nel mio feed è comparso un video dimostrativo pubblicato da un ingegnere: usava l'IA integrata in Google Chrome (Built-in AI) per spiegare in tempo reale ciò che vedeva una webcam.

È scattato l'istinto dei miei tempi nei sistemi.

«Questo è "multimodale". E se è integrato nel browser, non potrebbe funzionare interamente sul mio PC, senza pagare il cloud?»

Se avesse funzionato, forse avrei potuto costruire un sistema di accoglienza fatto apposta per il mio locale, senza installare un costoso sistema.

Ho copiato l'URL e l'ho lanciato a Gemini.

«Voglio fare la stessa cosa di questo. Dimmi come si implementa».

#### Fase 1: Funzionava, ma non riuscivo a capire «chi»

Ho cambiato le impostazioni di Chrome (i flag) come indicato da Gemini e ho incollato il codice, e lo stesso sistema della demo ha funzionato senza problemi.

Quando comparivo davanti alla telecamera, lo schermo mostrava questo:

«Un uomo con gli occhiali è seduto davanti a un PC».

Usa un'IA integrata nel browser chiamata GeminiNano. Il suo vantaggio è che funziona interamente dentro il browser senza collegarsi al cloud, ma riconosce solo cose generiche come «occhiali» e «uomo». Non arriva a stabilire chi sia la persona.

È una tecnologia straordinaria. Ma da titolare di un ristorante, la delusione è stata immediata.

«Così non va».

Quello che voglio sapere non è una caratteristica generica come «un uomo con gli occhiali», ma l'identificazione della singola persona: «È A o è B?»

#### Fase 2: Il muro dell'integrazione con Google Foto e la risposta dell'IA

Così ho proposto a Gemini un'idea ingenua.

«Collega questo sistema al mio Google Foto. Ha i dati dei raggruppamenti di volti dei miei amici e dei clienti abituali, quindi se fai il confronto con quelli puoi ottenere i nomi, giusto?»

La risposta di Gemini è stata fredda, ma corretta.

«Mi dispiace, ma non è possibile. I dati di riconoscimento facciale di Google Foto sono informazioni sulla privacy molto sensibili e, per motivi di sicurezza, non è consentito che siano usati da programmi esterni».

Giusto. La strada sembrava finire qui.

Ma da qui è emersa la vera essenza del «vibe coding (sviluppo tramite dialogo)». L'IA non si è limitata a rifiutare.

#### Fase 3: Un'alternativa e una svolta

Gemini ha continuato con questo suggerimento:

«Non possiamo usare Google Foto, ma è possibile costruire un sistema di riconoscimento facciale tutto tuo in un ambiente locale usando librerie open source (come OpenCV o face_recognition). Proviamo?»

Ho risposto subito «Sì».

Da qui il piano di sviluppo è cambiato completamente. Invece di usare le funzioni di Chrome, avrei costruito un sistema di riconoscimento facciale da zero usando un linguaggio di programmazione chiamato Python.

#### Fase 4: La lotta con lo schermo nero e il collegamento a un foglio di calcolo

Quello che dovevo fare non cambiava. Ho chiesto a Gemini «come installare le librerie necessarie» e ho incollato la risposta nello schermo nero (il prompt dei comandi).

Quando compariva un errore, rimandavo a Gemini il testo rosso così com'era.

Qualche ora dopo il sistema era finalmente completo.

1.  La webcam cattura il mio volto.

2.  Lo confronta con i «dati delle foto dei volti» in una cartella del PC.

3.  Quando trova una corrispondenza, consulta l'elenco clienti in un foglio di Google.

4.  Lo schermo mostra «Bonta: bottiglia quadrata rimasta ○○ g».

![Il sistema di riconoscimento facciale in funzione. Riconosce il volto del titolare e mostra le informazioni. L'immagine catturata è stata pixelata usando Gemini](images/fig-27.png)

Costo dell'esternalizzazione: ¥0 (circa $0,00). Il mio lavoro di programmazione: zero.

È stato il momento in cui, in un angolo di Higashi-Nakano, è nato un «sistema CRM di riconoscimento facciale» unico nel suo genere.

#### Fase 5: E poi mi rendo conto della «responsabilità di proteggere»

Il sistema era completo. Ma insieme alla gioia ho sentito un brivido lungo la schiena.

«Aspetta un attimo. In questo momento questo computer contiene i dati dei volti dei clienti (informazioni biometriche), vero...?»

Fino ad allora avevo pensato: «Basta che funzioni». Ma quando entra in funzione reale, la musica cambia.

Che cosa succede se questo computer viene infettato da un virus? I dati dei volti dei clienti e le informazioni sulle loro preferenze (dati personali) potrebbero trapelare insieme.

Un PC isolato, non collegato a internet, sarebbe sicuro, ma finché gestisco prenotazioni e social media, il collegamento a internet è indispensabile.

«Riuscire a costruire uno strumento utile» e «riuscire a gestirlo in sicurezza» sono due faccende distinte.

È stato qui che ho capito davvero, per la prima volta, l'importanza della «assicurazione contro i rischi informatici» di cui mi aveva parlato un agente assicurativo venuto a farmi una proposta.

Avevo riso: «Un piccolo locale come il nostro non subisce attacchi informatici», ma ora che l'IA ci permette di costruire sistemi avanzati, anche noi titolari singoli assumiamo la responsabilità di essere dei veri «gestori di dati».

Con l'IA si possono ottenere strumenti magici.

Ma ho imparato che portare con sé il «bastone (la competenza)» e lo «scudo (le misure di sicurezza)» per usare quella magia fa d'ora in poi parte del mestiere di titolare.

### 6-6. La «responsabilità» e l'«assicurazione» che accompagnano la libertà

#### Importante: privacy e dati personali

Questo «sistema di riconoscimento facciale» è un prototipo sperimentale che ho costruito per verificare che cosa sia tecnicamente possibile. Se lo si usasse in un locale vero, i dati dei volti dei clienti conterebbero come «dati personali (dati biometrici)» e dovrebbero essere rigorosamente protetti dalla legge (la legge giapponese sulla protezione dei dati personali).

Se sta pensando di adottare qualcosa del genere, tenga assolutamente presenti questi due punti.

Informare i clienti e ottenere il loro consenso: serve una procedura, per esempio un cartello all'ingresso con scritto «Utilizziamo il riconoscimento facciale con IA» e l'acquisizione del consenso quando i clienti si iscrivono come soci. Le riprese di nascosto non sono assolutamente ammesse.

Proteggere i dati: servono misure che riducano a zero il rischio di fuga di dati, come gestirli in un ambiente isolato da internet.

Poter costruire qualcosa non significa essere autorizzati a farlo. Se è un titolare con competenze tecniche, ricordi che la responsabilità di usare quella tecnologia viene insieme ad essa.

Finora ho parlato di quanto sia meraviglioso un sistema fatto in casa. Ma da titolare d'attività devo parlarLe anche di una dura realtà.

È questa: «Tutto ciò che costruisce da sé è responsabilità Sua».

Con un servizio in abbonamento mensile (SaaS), se il server si ferma, l'azienda si scusa e lo fa ripartire.

Ma un sistema costruito con il vibe coding non ha un «servizio clienti».

Se la Sua app smette all'improvviso di funzionare nell'ora di punta del pranzo, nessuno verrà ad aiutarLa.

Quando Google cambia una specifica, che un codice che funzionava benissimo ieri dia errori oggi è un fatto quotidiano.

Per questo faccio due preparativi.

Uno è il «backup analogico».

«Se il riconoscimento facciale si ferma, si guarda il registro cartaceo dei clienti». «Se l'app della cassa va in tilt, si usano la calcolatrice e gli scontrini scritti a mano».

Gli strumenti digitali sono soltanto «strumenti comodi». Non bisogna dipenderne al punto che, quando si fermano, si ferma anche il locale.

L'altro è l'«assicurazione» di cui ho parlato prima.

L'assicurazione di responsabilità civile informatica copre non solo il rischio di una fuga di informazioni, ma anche il risarcimento per l'attività persa quando un proprio errore blocca il sistema. Per un singolo titolare che si arma di informatica, fa parte dell'essere un adulto responsabile.

«A volte le cose si fermeranno. A volte sbaglierò».

Lo dia per scontato, accetti il rischio e prenda delle misure contro di esso.

Solo con questa determinazione possiamo davvero usare un «sistema libero» che non risponde a nessuno.

### 6-7. Non serve un esperto. Serve la perseveranza

Per lo sviluppo di questi due sistemi non ho pagato nemmeno uno yen di spese di esternalizzazione.

Ho usato soltanto un abbonamento a un'IA da qualche migliaio di yen al mese e la perseveranza di chi pensava: «Devo assolutamente liberarmi di questa preoccupazione (sul flusso di cassa)» e «Voglio rendere felici i miei clienti».

Non è questione di «non posso, perché non so programmare».

Se c'è qualcosa che si vuole costruire (il Cosa), l'IA insegna come costruirlo (il Come).

Anche quando compaiono parole che non si capiscono (Node.js, PowerShell, Firestore...), non c'è nulla da temere.

Abbiamo il miglior partner che esista, «Gemini», che le traduce e ci guida.

#### Rubrica 4: Che differenza c'è tra Excel e un database (Firestore)?

~ È un «appunto che legge Lei» o un «registro che legge il sistema»? ~

Nello sviluppo dell'app per il flusso di cassa è comparso Firebase (Firestore). Forse si è chiesto: perché non Excel?

Un foglio di calcolo (Excel) è un «quaderno che le persone guardano e in cui scrivono». È molto flessibile, ma per un sistema è vago su «che cosa sta dove».

Un database (Firestore), invece, è un «armadietto ordinato fatto per il sistema». Poiché è stabilito che «la data va nello scomparto 1 e l'importo nello scomparto 2», un programma può gestirlo all'istante. E non si rompe nemmeno quando più persone vi accedono nello stesso momento.

«Se si costruisce un'app, si usa un database, non Excel». Il solo saperlo alzerà il livello delle Sue istruzioni all'IA.

## Postfazione: Una «ricetta del futuro» che solo il Suo locale possiede

~ L'IA non è una tecnologia difficile. È un nuovo partner per la «conversazione» ~

Grazie di aver letto questo libro fino in fondo.

Se di questo libro prova una cosa sola, provi questa: «Incolli quel fastidioso messaggio di LINE direttamente nell'IA e le chieda di "trasformarlo in un diagramma"».

Non sono un vero esperto di IA. Ho semplicemente ripetuto ogni giorno la pratica di «parlare con l'IA con le parole del posto di lavoro»,\
sul campo di battaglia di un ristorante.

Per questo penso che basti portare a casa da questo libro non una «raccolta di risposte giuste», ma soltanto un «modo di pensare».

Quando ha aperto la prima pagina, che immagine aveva delle parole «usare l'IA»?

«Sembra difficile». «Servono conoscenze di programmazione, vero?» «Non c'entra niente con un piccolo locale come il mio».

Può darsi che abbia pensato qualcosa del genere.

Ma ora che ha letto fin qui questa testimonianza dei miei «tentativi ed errori», forse quell'immagine è cambiata un po'.

Quello che ho fatto non è stato sfruttare al massimo una tecnologia informatica avanzata.

Ho brontolato: «A mano non ce la faccio». Ho protestato: «È scomodo da usare». E ho preteso, con egoismo: «Voglio che funzioni più così».

In questi giorni, nel mondo degli ingegneri, il termine «vibe coding» è una tendenza.

È un metodo per costruire un sistema a sensazione, mentre si parla con l'IA.

Come un giocatore di shogi parla con l'IA per leggere le mosse successive, anche noi possiamo parlare con l'IA e costruire il «futuro dei nostri locali».

Come quando si dice al personale di cucina: «Metti ancora un po' di sale».

Come quando si chiede al pescivendolo del mercato: «Ha del buon pesce oggi?»

Rivolgersi all'IA e dirle: «Rendi più facile questo lavoro». Da qui comincia tutto.

Un tempo lavoravo nel reparto sistemi di un'azienda, facendo da coordinatore tra la «prima linea» e gli «sviluppatori».

Ora faccio la stessa cosa tra il «mio locale» e l'«IA».

E di questo ho la certezza:

«Un titolare che conosce i problemi della prima linea può diventare il più forte comandante dell'IA».

Cominci oggi anche Lei.

Per prima cosa, prenda lo smartphone e parli con Gemini.

«Ehi, da dove comincio oggi con la preparazione?»

«Come posso far vendere meglio questo piatto del menu?»

«Queste scartoffie sono una seccatura. Puoi fare qualcosa?»

Non si preoccupi se compare un errore. È il segno che la «conversazione» è cominciata.

Basta fare uno screenshot e rimandarlo con un «c'è qualcosa che non va».

Alla fine di quell'accumulo di conversazioni attende il «tempo» e il «respiro» che non avrebbe mai immaginato, e «un futuro che appartiene solo al Suo locale».

Adesso assumiamo un «vice responsabile» affidabile anche per il Suo locale.

Perché la ricetta del futuro nascerà dalla conversazione tra Lei e l'IA.

### Le tre uscite di questo libro

Questo libro si può leggere gratuitamente in PDF, su note e su Google Play. (Solo su Kindle, le regole dello store richiedono un prezzo minimo.) In cambio, ho preparato tre posti in cui andare dopo aver finito di leggere. Se ne usa anche solo uno, scrivere questo libro sarà valsa la pena.

1. Provare nel proprio locale. La serie Agenda si può iniziare con un taccuino gratuito. https://bontallc.com/agenda?via=b1-it-{{FMT}}
2. Seguire quello che faccio. Scrivo su note e su X dei prossimi strumenti che costruisco e della vita quotidiana al bar. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Se capita di passare per Tokyo, venire a Tamuro. A un minuto dall'uscita est della stazione di Higashi-Nakano. Si può entrare senza prenotazione. Sito di prenotazione https://tamuroreservation.vercel.app/?src=b1-it-{{FMT}}

A chi viene grazie a questo libro: quando prenota, inserisca per favore il codice coupon «BOOK». Alla prima visita offriremo un drink. Se si presenta senza prenotazione, basta dire «Ho letto il libro» al primo ordine. Offriremo lo stesso drink. È un piccolo accorgimento per poter contare quante persone sono venute grazie al libro.

### Chi scrive

Raku Bonta

Un titolare che gestisce da solo un locale con 11 posti al bancone e 8 posti nella sala con tatami a Higashi-Nakano, Tokyo.

Di giorno è un locale specializzato in hamburger al curry, profumato di spezie. Di sera è un bar-ristorante con un menu fisso che cambia ogni giorno.

▼ Hamburger al curry Quatre Epice

https://www.instagram.com/quatre.epice.hamburg.curry/

![Hamburger al curry Quatre Epice](images/fig-28.png)

▼ Il bar «Tamuro»

https://www.instagram.com/tamuro.higashinakano/

![Il bar «Tamuro»](images/fig-29.png)

Il locale si impegna anche a costruire comunità attraverso il cibo, con serate dedicate al vino ogni due settimane, un corso di cucina al mese e cene a più portate.

Prima di aprire in proprio il locale 12 anni fa, Raku Bonta lavorava in un'azienda nella «pianificazione dei sistemi» e nell'«architettura delle soluzioni».

I titoli suonano difficili, ma il lavoro vero era quello di «coordinatore che trasmette con precisione ai fornitori informatici i desideri della prima linea, "vogliamo fare questo", e li fa realizzare». Non un ingegnere che fa programmazione avanzata, ma un percorso da «traduttore» che collega persone e tecnologia.

Oggi, attingendo a quell'esperienza, usa l'IA generativa come Google Gemini per gestire il proprio locale, praticando e condividendo una «riforma dell'attività che funziona anche con zero conoscenze specialistiche».
