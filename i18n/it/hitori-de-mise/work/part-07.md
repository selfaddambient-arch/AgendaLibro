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
