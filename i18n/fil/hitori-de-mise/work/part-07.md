### 6-1. Hindi Natutugunan ng mga Ready-Made App ang Eksaktong Kailangan Ko

Sa ngayon, ang napag-usapan ko ay ang paggamit ng AI gamit ang mga umiiral na platform, tulad ng pagbuo ng larawan at pagsusuri ng menu.

Pero habang patuloy kayong nagpapatakbo ng negosyo, may mga alalahaning talagang hindi malulutas ng mga "handa-nang-app."

Lalo na sa isang hindi regular na modelo ng negosyo tulad ng amin, "curry sa araw, bar sa gabi," masalimuot din ang daloy ng pera papasok at palabas.

"Gusto kong itugma ang balanse ko sa PayPay Bank sa mga susunod na bayarin at malaman kung magkano ang matitira sa katapusan ng buwan."

"Hati ang mga petsa ng bayad sa ika-10 at ika-25. Gusto kong i-simulate iyon."

Napakahusay ng mga accounting software na nariyan, pero wala ni isang tumutok sa "alalahaning nasa isip ko ngayon."

Kaya nagpasya ako.

"Kung wala, gagawa ako. Nariyan ang Gemini, ang pinakamahusay na engineer."

### 6-2. Phase 1–3: Mula sa Mabilisang Tala Hanggang sa "Cloud"

Nagsimula ang pagbuo sa pagpapakita ko sa Gemini ng mga tala ko sa Google Keep.

![Ang Keep note na naging panimulang punto ng pagbuo](images/fig-25.png)

#### Phase 1: Pagbuo ng Lohika

"Gusto kong gawing awtomatiko ang mga kalkulasyon sa note na ito."

Bilang tugon sa hiling ko, mabilis na binuo ng Gemini ang lohika ng kalkulasyon.

- Kapag binago ko ang halaga ng isang item, agad nitong kinukuwenta ang huling balanse.

- Kapag malapit nang magkulang ang pondo, nagpapakita ito ng "babala" na pula.

- Sinisimulate nito ang tiyempo ng bayad na hati sa "ika-10" at "ika-25 / katapusan ng buwan."

- Sine-save ang datos sa browser (cache).

Sapat nang maginhawa ito, pero naghangad pa ako ng higit. "Gusto kong manatili ang datos kahit isara ko ang browser. Gusto ko rin itong ma-check sa telepono."

#### Phase 2: Paggamit ng Hindi Pamilyar na Tool, ang "Firebase"

Iniisip ko noong mag-link sa spreadsheet, pero hindi ko inasahan ang mungkahi ng Gemini.

"Kung real-time na performance at episyensiya ang iisipin, gamitin natin ang 'Firebase' ng Google. Sapat na ang free tier para patakbuhin ito."

"Firebase...?" Ngayon ko lang narinig ang salitang iyon. Pero sa instinct ng mga araw ko bilang system coordinator, nagpasya ako, "Kung ganito kalakas ang rekomendasyon ng AI, sige, sundin natin."

Bilang resulta, sa paggamit ng database na tinatawag na Firestore, ligtas nang naimbak sa cloud ang datos.

#### Phase 3: Google Login at Sistema ng Pag-apruba

Tungkol ito sa pera, kaya masama kung kahit sino ay makakakita nito.

Sa una, naisip ko ang tulad ng "password phrase," pero iminungkahi ng Gemini, "Kung gusto ninyo ng mas matibay na seguridad, gumamit tayo ng Google login."

Pagkatapos, nang sabihin kong, "Gusto kong ang mga staff lang na aaprubahan ko ang makakakita nito," bumuo pa ito ng "sistema kung saan ang isang administrator ay maaaring mag-apruba at mag-alis ng mga miyembro sa mismong screen."

### 6-3. Phase 4–5: Pagharap sa Itim na Screen (ang Terminal)

Mula rito dumating ang pinakamalaking hadlang ng vibe coding: ang pag-publish ng app sa internet (deploy).

#### Babala: Mula Rito, Kurso na Ito ng "Black Belt"

Ang susunod na ilang pahina ang pinakamahirap na "hands-on" na bahagi ng aklat na ito. Gagamit kayo ng "itim na screen (terminal)" na tulad ng ginagamit ng mga hacker sa pelikula.

Magiging tapat ako. Tiyak na magkakaroon kayo ng mga error dito. Ako rin. Makakabangga kayo ng mga pader tulad ng "PowerShell permissions error" na parang mga spell kung basahin. Pero huwag kayong matakot. Pareho lang ang gagawin ninyo rito: "kunan ng screenshot ang screen ng error at ihagis sa AI."

Ang katotohanang natutunan ko noong nasa system business ako ay ito: "Nagkakaroon ng error kahit ang mga propesyonal. Ang pagkakaiba lang ay kung susuko ba kayo kapag may lumabas, o hahanap (hihingi) ng tulong." Kung masyadong mahirap, laktawan ang bahaging ito at isaisip na lang ang posibilidad: "Ganito na pala kalayo ang magagawa sa AI."

Sabi ng Gemini:

"Ise-set up natin ang development environment sa Windows PC ninyo. Mag-install ng 'Node.js,' at i-type ang mga sumusunod na command sa 'VS Code.'"

Binuksan ko ang itim na screen (terminal) ayon sa utos, at agad na nagkaroon ng error.

"Hindi mapatakbo dahil sa mga paghihigpit sa seguridad ng PowerShell."

Mawawalan ng loob dito ang ordinaryong may-ari.

Pero kinopya ko ang screen ng error at inihagis sa AI.

Agad na sumagot ang AI: "Alisin ang paghihigpit gamit ang command na 'Set-ExecutionPolicy.'"

Nang hindi nauunawaan ang ibig sabihin nito, tinype ko ang command, tapos npm run build, firebase deploy...

Sa bawat pag-type ko ng mga titik na parang spell, tumatakbo ang text sa screen at umuusad ang proseso.

At sa wakas, lumitaw sa web ang app ko.

#### Phase 5: Gawing Smartphone App (PWA)

Ang na-publish na app ay sa simula nasa payak at walang ayos na estado na sira ang disenyo, pero nalutas din ito sa pagdaragdag ng setting na tinatawag na "Tailwind CSS."

Pagkatapos, nang hilingin kong, "Gusto kong maglagay ng icon sa home screen ng telepono ko at gamitin ito na parang app," itinuro nito ang mga setting para gawin itong "PWA (Progressive Web App)."

At sa gayon, isinilang sa loob ng telepono ko ang isang dedikadong app na ako ang gumawa (nang hindi sumusulat ng kahit isang linya ng code).

![Ang screen ng natapos na app sa pamamahala ng cash flow](images/fig-26.png)

### 6-4. Phase 6: Ang Problema Pagkalipas ng 30 Araw, at ang Solusyon

Mga isang buwan matapos kong simulang gamitin ito, may lumitaw na problema.

"Gumagana ito hanggang kahapon, at bigla na lang hindi ko ma-access!"

Nataranta akong sumangguni sa Gemini, at nasa hindi inaasahang lugar ang sanhi.

"Nasa 'test mode (limitado sa 30 araw)' pa rin ang mga setting ng database (Firestore). Nag-expire na ito."

Para makatipid sa hirap ng pag-configure sa simula ng pagbuo, sadyang nagtakda ang AI ng patakarang may petsa ng pag-expire.

"Baguhin natin ang mga security rule para 'puwedeng patuloy na gamitin ng sinumang naka-login na user.'"

Nang baguhin ko ang ilang linya ng settings file ayon sa tagubilin ng AI, muling gumana nang maayos ang app.

Isa ring magandang karanasan para sa akin ang problemang ito.

Natutunan kong "buhay na bagay ang isang sistema at kailangan ng maintenance."

At nagkaroon ako ng katiyakang "kahit magkaproblema, laging may sagot kung magtatanong ako sa AI."

### 6-5. Case Study 2: Ang "Face Recognition Project" na Nagsimula sa Isang Demo Video sa X (Dating Twitter)

Narito ang isa pang pagbuo ng sistemang sinubukan kong buuin, at ang pinakamalaki.

Ito ay "isang sistemang kumikilala sa mga customer na pumapasok sa pamamagitan ng camera, at palihim na nagsasabi sa akin ng pangalan, datos, at mga kagustuhan nila."

Nagsimula ito sa social media site na X, na basta-basta kong ini-scroll.

Isang demo video na pino-post ng isang engineer ang lumabas sa feed ko: ginagamit ang AI na nakapaloob sa Google Chrome (Built-in AI) para ipaliwanag, nang real time, kung ano ang nakikita ng webcam.

Gumana ang instinct ko bilang dating taga-system.

"Ito ay 'multimodal.' At kung nakapaloob ito sa browser, hindi ba puwedeng tumakbo ito nang buo sa sarili kong PC, nang hindi nagbabayad para sa cloud?"

Kung gagana ito, baka makabuo ako ng hospitality system para lang sa shop ko, nang hindi nag-i-install ng mamahaling sistema.

Kinopya ko ang URL at inihagis sa Gemini.

"Gusto kong gawin ang katulad nito. Sabihin mo kung paano ito i-implement."

#### Phase 1: Gumana, Pero Hindi Matukoy Kung "Sino"

Binago ko ang mga setting ng Chrome (flags) ayon sa utos ng Gemini at idinikit ang code, at tumakbo nang walang problema ang parehong sistema tulad ng sa demo.

Nang lumitaw ako sa camera, ito ang ipinakita ng screen:

"Isang lalaking may salamin ang nakaupo sa harap ng PC."

Gumagamit ito ng AI na nakapaloob sa browser na tinatawag na GeminiNano. Ang bentahe nito ay gumagana ito nang buo sa loob ng browser nang hindi kumokonekta sa cloud, pero pangkalahatang bagay lang tulad ng "salamin" at "lalaki" ang nakikilala nito. Hindi nito kayang alamin kung sino ang tao.

Kamangha-manghang teknolohiya. Pero bilang may-ari ng restaurant, agad akong nadismaya.

"Hindi puwede ito."

Ang gusto kong malaman ay hindi ang pangkalahatang katangian tulad ng "lalaking may salamin," kundi ang pagkilala sa indibidwal: "Si Mr. A ba ito o si Mr. B?"

#### Phase 2: Ang Pader ng Google Photos Integration, at ang Sagot ng AI

Kaya nagbigay ako sa Gemini ng isang mababaw na ideya.

"Ikonekta mo ang sistemang ito sa Google Photos ko. Nandoon ang face-grouping data ng mga kaibigan at suki ko, kaya kung itutugma mo roon, makukuha ang mga pangalan, hindi ba?"

Malamig pero tama ang sagot ng Gemini.

"Paumanhin, pero hindi iyon posible. Lubhang sensitibong impormasyon sa privacy ang face recognition data sa Google Photos, at para sa seguridad, hindi ito pinapayagang gamitin ng mga panlabas na program."

May katwiran. Parang dito na nagtatapos ang daan.

Pero mula rito dumating ang tunay na esensya ng "vibe coding (pagbuo sa pamamagitan ng usapan)." Hindi lang tumanggi ang AI.

#### Phase 3: Isang Alternatibo at Pagbabago ng Direksyon

Nagpatuloy ang Gemini sa pagmumungkahi nito:

"Hindi natin magagamit ang Google Photos, pero posibleng bumuo ng sarili ninyong face recognition system sa local na environment gamit ang mga open-source library (tulad ng OpenCV o face_recognition). Subukan natin?"

Agad akong sumagot ng "Oo."

Mula rito, lubusang nagbago ang plano ng pagbuo. Sa halip na gamitin ang mga feature ng Chrome, bubuo ako ng face recognition system mula sa simula gamit ang programming language na tinatawag na Python.

#### Phase 4: Pakikipagbuno sa Itim na Screen at Pagkonekta sa Spreadsheet

Hindi nagbago ang kailangan kong gawin. Itinanong ko sa Gemini "kung paano i-install ang mga kinakailangang library" at idinikit ang sagot sa itim na screen (ang command prompt).

Nang lumabas ang error, ibinalik ko sa Gemini nang walang binago ang pulang text.

Pagkalipas ng ilang oras, sa wakas ay natapos ang sistema.

1.  Kinukuha ng webcam ang mukha ko.

2.  Itinutugma ito sa "datos ng litrato ng mukha" sa isang folder sa PC.

3.  Kapag may nakitang tugma, hinahanap nito ang customer list sa isang Google Spreadsheet.

4.  Ipinapakita ng screen ang "Mr. Bonta: natitirang whisky sa Kaku bottle ○○ g."

![Tumatakbo ang face recognition system. Nakikilala nito ang mukha ng may-ari at ipinapakita ang impormasyon. Nilagyan ng mosaic ang nakuhang larawan gamit ang Gemini](images/fig-27.png)

Gastos sa outsourcing: ¥0 (humigit-kumulang $0.00). Sarili kong gawain sa pag-code: wala.

Iyon ang sandaling isinilang sa isang sulok ng Higashi-Nakano ang kaisa-isang "face recognition CRM system."

#### Phase 5: At Saka Ko Naunawaan ang "Responsibilidad na Magprotekta"

Kumpleto na ang sistema. Pero kasabay ng saya, naramdaman kong may kumalat na lamig sa likod ko.

"Sandali lang. Sa ngayon, hawak ng computer na ito ang face data (biometric na impormasyon) ng mga customer, hindi ba...?"

Hanggang noon, inisip ko, "Basta gumagana, ayos na." Pero kapag nasa aktuwal na operasyon na, ibang usapan na iyon.

Paano kung mahawaan ng virus ang computer na ito? Maaaring sabay na tumagas ang face data ng mga customer at ang impormasyon ng mga kagustuhan nila (personal na impormasyon).

Ligtas ang isang standalone na PC na hindi nakakonekta sa internet, pero hangga't hawak ko ang mga reservation at social media, mahalaga ang koneksyon sa internet.

Magkahiwalay na usapin ang "kakayahang bumuo ng kapaki-pakinabang na tool" at ang "kakayahang pamahalaan ito nang ligtas."

Dito ko unang tunay na naramdaman ang kahalagahan ng "cyber risk insurance" na sinabi ng isang insurance agent noong pumunta sila para mag-alok sa akin dati.

Tinawanan ko noon, "Hindi aatakihin ng cyber attack ang maliit na shop na tulad namin," pero ngayong nakakabuo na tayo ng mga advanced na sistema sa tulong ng AI, tayong mga indibidwal na may-ari ay may pananagutan na ring maging maayos na "tagapamahala ng datos."

Sa AI, makakakuha kayo ng mahikang mga tool.

Pero natutunan kong bahagi na rin ng trabaho ng may-ari mula ngayon ang pagdadala ng "magic wand (literacy)" at "kalasag (mga hakbang sa seguridad)" para magamit ang mahikang iyon.

