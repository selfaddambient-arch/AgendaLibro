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
