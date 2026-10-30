# review-log：1冊目（hitori-de-mise）イタリア語版

レビュー：章ごとに実行。**00・01・02 章の一部は agy -p（Gemini 3.8 Flash High）、返事が遅く（1章7分前後・全体で2時間超の見込み）30分を超えたため、残りは review-api.mjs（Gemini API、gemini-3.8-flash）に切替**。ChatGPT は使っていない。指摘は全章分を読み、窓がまとめて直した。**未対応：0**（「採らない」はすべて理由つきで判断済み）。**本1は Google Play 新規。**

## はじめに（00）— agy
| 指摘 | 判断 | 理由・反映 |
|---|---|---|
| tuo の親称が混じる（Lei に整合） | 採る | 「avere l'IA al proprio fianco」 |
| programmazione difficile が稚拙 | 採る | programmazione complessa |
| rivendita（小売の語）を飲食店に | 採る | 「locale specializzato in hamburger al curry」。全箇所を直した |
| hamburger がパン挟みと誤解される | 採る（一部） | 初出に訳注 *(hamburg steak alla giapponese …)* を足した（日本の補足） |
| su presentazione が「提示」と誤解される | 採る（初出のみ） | 「accessibile solo su presentazione di altri clienti」 |
| menu fisso … e da bere が口語的 | 採る | 「e bevande」 |
| seminterrato stretto／siamo が一人営業と矛盾 | 採る | 「piccolo」「ho sempre da fare」 |
| 「systems guy」を日本での呼び名のように書いた | 採らない | 英語版と同じ書き方（英語版・原文の「システム屋」の説明）。親へ英語版の見直しを伝える程度に留める |
| mettermi in mezzo が否定的 | 採る | fare da tramite |
| decisioni … porto da solo がぎこちない | 採る | 「che devo prendere senza nessuno con cui dividerle」 |
| mansioni が硬い | 採る | compiti operativi |
| ortografia → sintassi | 採る | 意味の取り違え |
| 非人称（si ha）が Lei のトーンと離れる | 採らない | 非人称は読者を限定しない意図。文体は style.md |
| fastidi → frustrazioni | 採る | |
| prima linea が合わない | 採らない | イタリア語でも「in prima linea」は現場の意味で通じる |
| senso → intuito | 採る | |
| 12年目と満12年のずれ | 採らない | 「今年で12年目」＝「sono dodici anni」で英語版と同じ |
| 見出し・数字・脱落・日本語の残り | 指摘なし | |

## 第1章（01）— agy
spalla con cui parlare → semplice interlocutore（全箇所）／lavoro in sala → lavoro pratico del locale／la sala di un locale → il lavoro in un locale／Pensa → Elabora（lo slogan）／ovvietà → consigli da manuale／da sola → in piena autonomia／multimodale → 「multimodalità」（見出し）／cibo → ingredienti rimasti／disegno → grafica／scomodo → faticoso／gliela の係り（写真）→ la mostra all'IA／sul posto → di persona／Noi locali … del titolare → Noi titolari、autocompiacimento → autoreferenziale／individualità → personalità：**すべて採る**。
- I due si somigliano の言い換え：採らない（意味は変わらない）。
- La prego … lo fa → 接続法に：採らない（Lei の依頼文として自然）。

## 第2章（02）— agy
perde le indicazioni → si lascia sfuggire／progettato → curato nessuna grafica／sconclusionato → prolisso e disordinato／関係節の重なり／molto discusso → fa molto parlare di sé／prendere a cuore → acceso la sua passione（人物の代名詞を避けた）／「giapponese」だけで使うと誤解 → 「la lingua di tutti i giorni（nel mio caso, il giapponese）」／queste → questi（性の不一致）／palleggio → botta e risposta／impiccia → perde tempo／pulsanti → tasti（キーボード）／drastico → enorme／studiare conoscenze → nozioni／più sicura → più rapida：**採る**。
- figura … estraneo の性の不一致：採らない（estraneo は「mondo」に係る）。
- 命令形が主語になる文：採る（直した）。
- **Mac のショートカット [Cmd]+[Shift]+[4] はクリップボードに入らない、[Ctrl] を足せ**：採らない（代表の裁定 2026-10-29 で英語版・全言語に入れた書き方。親へ「全言語で [Cmd]+[Ctrl]+[Shift]+[4] に直すか」を依頼）。

## 第3章前半（03-1）— API
siamese の文（人と動物が両方置換と読める）→ 採る／Falli tenere → 採る（Fai in modo che…）／fa una brutta figura → 採る／alfabeto → 「scritta in caratteri latini」採る。

## 第3章後半（03-2）— API
applicazione LINE → 「richiesta degli adesivi di LINE」／mi dà fastidio → 「c'è qualcosa che non mi convince」／見出し3-7 の命令形 → 不定詞／avidità → 「Ho voluto strafare」／affidare → delegare tutta l'analisi：**採る**。

## 第4章（04）— API
perla → Gem（見出し）／in sala → lavoro pratico／述語のない文を直した／del campo → sul campo、scorte effettive／LINE と enoteca → rivenditore di alcolici に（LINE の説明は前に出ている）：**採る**。
- コラム3だけ Lei が硬い → tu に統一：採らない（全体は Lei。style.md）。
- LINE を WhatsApp に置換せよ：採らない（原文の事実。補足は第2章に入っている）。

## 第5章（05）— API
Percorso del Consiglio → Percorso Consigliato／apparire alla moda → fare l'elegante／incoraggiamento → pura grinta／verificare le risposte → i risultati／a tratto di linea → a linee essenziali／gemere → mugugnare：**すべて採る**。

## 第6章（06）— API
senza falta（スペイン語混入）→ assolutamente／6-1 の見出し／struccato → spoglio／コラム4の tu → Lei：**採る**。
- 「角ボトル」を Suntory Kaku と明記せよ：採らない（原文にない固有名詞を足さない）。

## おわりに（07）— API
Le → le（AI を指す代名詞）／esperto speciale → vero esperto／in seguito → i prossimi strumenti／fu scritto → 「All'epoca in cui ho scritto」／rivendita → locale：**採る**。
- prima linea：採らない（上と同じ）。
- 「uscite」の比喩が伝わらない：採らない（全言語で「3つの出口」を同じ語で統一している）。
- taccuino → agenda：採らない（シリーズの名づけ。用語集で固定）。
- Ho visto il libro → Ho letto il libro：採る（合言葉。両書そろえた）。
