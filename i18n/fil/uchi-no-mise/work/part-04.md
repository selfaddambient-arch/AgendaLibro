### 2-6 Pag-aaral ng Wika ng UI

May isa pa akong muling natutunan: ang mga pangalan ng mga bahagi ng screen.

Kahit sinabi ko sa AI na "gawin ito rito," madalas na hindi lumalabas ang screen na inaasahan ko. Nang pag-isipan ko ang dahilan, napagtanto kong hindi ko alam ang mga pangalan ng mga bahagi ng screen. Kahit ilarawan ko ang "maliit na window na lumalabas sa ibabaw" o ang "abisong nawawala pagkalipas ng ilang segundo," mahirap para sa AI na maintindihan kung ano ang ibig kong sabihin.

Kaya nagbasa ako ng reference book tungkol sa UI (user interface, ang hitsura at paraan ng paggamit ng isang screen) at natutunan ko ang mga pangalan ng mga bahagi at ang mga teknikal na termino ng disenyo.

| Bahagi | Ano ito |
| --- | --- |
| Modal | Maliit na window na lumalabas sa ibabaw ng screen. Hindi magagamit ang screen sa likod nito hangga't hindi ito isinasara |
| Toast | Abisong lumalabas sa gilid ng screen nang ilang segundo at kusang nawawala |
| Tab | Mekanismong nagpapalit ng nilalaman kapag pinindot ang isang heading |
| Accordion | Mekanismong nagbubukas at nagsasara ng nilalaman kapag pinindot ang isang heading |
| Drawer | Menu na dumudulas palabas mula sa gilid ng screen na parang drawer |
| Iba pa | Breadcrumbs (landas na nagpapakita kung nasaan ka ngayon), carousel (mga aytem na ini-scroll nang pahalang), bottom sheet (panel na umaangat mula sa ibaba ng screen), at iba pa. Sa bawat pangalang matututuhan ninyo, maibibigay ninyo ang utos sa AI sa isang parirala lang |

Kapag pangalan ang ginamit ninyo sa pakikipag-usap, halos tama na agad sa isang subok ang mga screen na ginagawa ng AI. Kung sasabihin ninyong, "Ipakita ang screen ng kumpirmasyon ng reservation bilang modal," hindi na magdadalawang-isip ang AI.

#### Sobra-sobra ang galaw ng AI, sa pagdaragdag man o sa pagbabawas

Kahit natutunan ko na ang mga salita, iba pang uri ng hirap ang naranasan ko sa paggawa ng mga screen kasama ang AI. Malayo ang indayog ng AI.

Nang humingi ako ng "magarang" header para sa reservation site, makapal at kapansin-pansing header ang lumabas. Pero reservation ang buong layunin ng isang reservation site. Para sa mga suking nagre-reserve sa bawat pagpunta, abala lang ang makapal na header na may mahahabang paliwanag. Ipinabawas ko ang taas nito nang halos kalahati, habang pareho pa rin ang dami ng impormasyon.

Nang gawin kong pare-pareho ang footer ng email at nilagyan ko ito ng link papunta sa Gabay sa Susunod na Tambayan, biglang mukhang payak at walang dating ang katawan ng email kung ikukumpara. Kaya nilagyan ko rin ng heading ang katawan, pati ng talahanayan ng mga pangunahing punto at ng isang buton na pipindutin. Nang dagdagan ko ng pasukan papunta sa chat window ang footer, nagmukha itong magulo. Nang isiksik ko ito sa dalawang linya ng mga link na pinaghihiwalay ng guhit, maayos nga ito pero hindi kapansin-pansin. Sa huli, dalawang card ang pinili, na nagpapakita ng gamit ayon sa "kung kailan ito gagamitin." Ang nasa kaliwa ay "para sa susunod ninyong reservation," at ang nasa kanan ay "pagkatapos ninyong kumain."

Masyadong makapal, masyadong pinutol, masyadong litaw. Sa bawat pagkakataon, ang salita ng may-ari ang nagpasya kung ano ang tamang balanse.

#### Panukala sa disenyo na walang larawan

Nangyari rin ito. Ipinagawa ko sa AI na sumusulat ng programa ang mga panukalang pagpapabuti para sa chat window gamit ang isang design AI (Claude Design), at bumalik ang ulat na nagsasabing, "Gumawa ako ng mga panukala para sa walong screen." Pero nang buksan ko, puro paglalarawan sa teksto lang ang laman. Hindi nakaguhit ng mga larawan ang AI, pero ang ulat na "tapos na" lang ang naiwan.

Sa huli, ang AI sa panig ng chat mismo ang direktang gumuhit ng apat na panukala sa design screen. Kinuha nito ang mga kulay ng kasalukuyang screen mula sa isang screenshot, inilagay sa timeline ang kasaysayan ng shop, hinati sa dalawang kategorya ang lasa, ang "paraan ng pagluluto" at ang "lasa," ginawang mga card ng paliwanag ang mga plano, at pinag-isa sa isang buod ng reservation ang mga presyo.

Kapag pinatakbo ninyo ng test ang AI, sasabihin nitong "pumasa." Kapag humingi kayo ng disenyo sa AI, sasabihin nitong "tapos na." Trabaho ng tao ang tingnan kung ano ang laman. Ang pamantayan sa paghusga ay bagay na tao lang ang kayang patuloy na panatilihin.

#### Ano ang maiuuwi ninyo mula sa kabanatang ito

- Magkaiba ang paggawa ng bagay na gumagana at ang kakayahang patakbuhin ito nang ligtas.
- Huwag ang salita ng AI ang gawing batayan sa pagsusuri ng output nito, kundi ang mga test. Mapagkakatiwalaan lang ang isang test kapag natiyak ninyong pumapalpak ito kapag sinadya ninyong sirain ang sistema.
- Huwag ipaubaya sa pagbuo ng teksto ng AI ang mga kalkulasyong hindi puwedeng magkamali, gaya ng presyo. Ibigay ito sa program.

Ang karugtong ng kabanatang ito (ang mga bagong natuklasang butas at ang mga hakbang na ginawa ko para ayusin ang mga ito) ay nasa note at X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Kabanata 3: Pamamahagi ng mga Tool ng Aking Shop sa Iba pang Shop

### 3-1 Ang Maliit na Berdeng Karatula sa Reservation Page

Buksan ninyo ang reservation page ng Tamuro at makikita ninyo ang maliit na berdeng karatula malapit sa itaas. Habang bukas ang shop, nakasulat dito ang "OPEN," at kapag nagsara na, "CLOSED." Kapag pinindot ng may-ari ang buton ng extend, na-e-extend nang 30 minuto ang oras ng pagsasara at may dampi ng vermilion na lilitaw sa karatula.

May isang katangiang pareho ang mga independent na restawran. Halos eksaktong oras silang nagbubukas, pero madalas na nahuhuli ang pagsasara. Kung masigla ang kuwentuhan kasama ang mga customer, nananatiling bukas ang mga ilaw ng shop hanggang lampas sa last order na 10:30 p.m.

Pero hindi ito nakikita ng customer. Ang "Open" na ipinapakita sa Google Maps ay ibinabatay lang sa mga nakarehistrong oras, kaya hindi nito nasasalamin ang extension, ang maagang pagsasara, o ang pansamantalang pagsasara. Walang pumupunta sa isang shop na lampas na sa oras ng pagsasara habang iniisip na, "Baka bukas pa." Nakakailang din ang tumawag para magtanong.

Ang karatulang ito ay tool na sumasagot sa tanong na "Bukas pa ba?" Tinatawag itong "AgendaLuce (Talaan ng Ilaw)." Ang Luce ay nangangahulugang "ilaw" sa Italyano.

Ginawa ang Talaan ng Ilaw para tumakbo nang halos hindi na kailangang pansinin ng may-ari. Irehistro nang minsan ang oras ng pagbubukas at pagsasara sa bawat araw ng linggo, at kusang sisindi at mamamatay ang ilaw ng karatula. Hinahawakan lang ito ng may-ari kapag mag-e-extend, magsasara nang maaga, o magpapahinga sa isang araw. Para mag-extend, isang buton lang sa smartphone ang pipindutin. Puwede rin itong patakbuhin ng staff mula sa nakalaang link na gumagana nang hindi kailangang mag-log in.

Hindi kailangan ng mga customer na mag-log in o magparehistro. Buksan lang ang pampublikong page at makikita na ang kasalukuyang lagay ng ilaw. Kung idadagdag ito sa home screen ng smartphone, gumagana ito na parang app. Maaari ring i-embed sa ibang website ang maliit na component ng karatula. Iyon ang lumalabas sa reservation page ng Tamuro.

Libre ang Talaan ng Ilaw. Kung ie-embed lang ninyo ang component ng karatula sa inyong website, mga 10 minuto lang ang setup.

At heto ang mahalaga. Ang Talaan ng Ilaw na ito ay hindi lang para sa Tamuro. Magagamit ito ng kahit anong shop.

Sinadya kong iwanang walang pangalan ng shop ang disenyo ng karatula. Kung lalagyan ko ng pangalan, magiging karatula na ito ng Tamuro. Mapipili rin ang wika ng display. Pinaliit ko ang component para ma-embed ito sa website ng kahit anong shop.

Isang tool na isinilang mula sa problema ng Tamuro na "nahuhuli ang pagsasara," at ginawa mula sa simula sa anyong magagamit ng sinuman. Iyan ang Talaan ng Ilaw. At ang koleksyon ng mga tool na tulad nito ang tinatawag na "Agenda series."

【Larawan 3-1a】Ang karatula ng Talaan ng Ilaw sa itaas ng reservation page (bukas) *(Nasa wikang Hapon ang screen.)*

【Larawan 3-1b】May dampi ng vermilion kapag may extension *(Nasa wikang Hapon ang screen.)*

【Larawan 3-6a】Ang screen ng may-ari. Para mag-extend, pindutin nang isang beses ang buton *(Nasa wikang Hapon ang screen.)*

【Larawan 3-6b】Kaagad pagkatapos pindutin ang extend. Na-extend nang 30 minuto ang oras ng pagsasara *(Nasa wikang Hapon ang screen.)*

【Larawan 3-6c】Ang pampublikong page na nakikita ng mga customer (habang may extension) *(Nasa wikang Hapon ang screen.)*

### 3-2 Nagsimula sa Itim na Leather Notebook

Hindi pinlano ang Agenda series bilang isang series. Nagsimula ito sa iisang sistema, na hindi pa nga nailalabas.

Ang una kong binalak buuin ay isang mekanismong nakakakilala sa mukha ng mga customer at sumasalubong sa mga suki. Ang camera sa pasukan ng shop ay nakikilala ang mga bisita sa pamamagitan ng mukha at ipinapaalam sa may-ari: "Iyan ang taong kumain ng tonteki noong nakaraan, ang hindi pa natin nakikita sa loob ng tatlong buwan." Balak kong ipatulong sa makina ang trabaho ng may-ari ng maliit na shop na ginagawa niya sa kanyang isip: ang pag-alala sa mga mukha, pangalan, at kagustuhan.

Pero ilang sandali pagkasimula ko ng paggawa, napagtanto kong ito ay sistemang pinagkatiwalaan ng napakabigat na bagay. Mga mukha. Mga katangian. Kasaysayan ng pagbisita. Ang pagkatao ng customer. Lahat ng ito ay impormasyong hindi na mababawi kapag nag-leak.

Ang pumasok noon sa isip ko ay ang "Itim na Leather Notebook" ni Seicho Matsumoto. Isang talaang hindi ipinakikita kaninuman, pero tiyak na umiiral. Isang ledger na kapag nabuksan, nagdidikta sa buhay at kamatayan ng mga tao. Hindi ba iyon mismo ang sinusubukan kong buuin?

Sa Italyano, ang "notebook" ay Agenda, at ang "itim" ay Nera. Pagsamahin: AgendaNera. Ang itim na leather notebook. Ganoon unang napagpasyahan ang pangalan.

Binubuo pa rin ang AgendaNera. Ito ang pinakamaingat kong binubuo sa series.

At ang pagpapangalang ito ang naging simula. Kung may itim na notebook, puwedeng may mga notebook na may ibang kulay. Muli kong bubuuin ang mga mekanismong ginagamit ko araw-araw sa sarili kong shop sa mga anyong magagamit ng kahit anong shop, at ilalabas ko ang mga ito nang isa-isa bilang notebook. Iyan ang [Agenda series](https://bontallc.com/agenda?via=b2-fil-{{FMT}}).

### 3-3 Pagdaragdag ng mga Notebook, Isa-isa

Ang Agenda series ay koleksyon ng maliliit na web app, na bawat isa ay sumasagot sa isang problema ng restawran gamit ang isang tool. Bawat isa ay may pangalang Italyano at palayaw sa wikang Hapon na nagtatapos sa "-techo" (notebook). Bawat pangalan ay may sariling pinagmulan.

| Pangalan | Palayaw | Pinagmulan ng pangalan | Ano ang ginagawa nito |
| --- | --- | --- | --- |
| AgendaTimbro | Talaan ng Oras | Ang Timbro ay nangangahulugang "selyo." Ito mismo ang clock-in | Nagtatala ng clock-in at clock-out ng staff |
| AgendaOro | Talaan ng Kita | Ang Oro ay nangangahulugang "ginto." Ang notebook ng pera | Tinatantiya ang kakayahang kumita sa pagbubukas ng shop o ng bagong item sa menu (libre) |
| AgendaBis | Gabay sa Susunod na Tambayan | Ang Bis ay nangangahulugang "encore." Ang "Bis!" na isinisigaw ng mga manonood sa isang konsiyerto | Gumagabay sa mga customer papunta sa kalapit na susunod na tambayan (libre) |
| AgendaQA | Gabay sa Suporta | Ang Qua ay nangangahulugang "dito." Kapag may problema, dito | Ang shared na help desk ng series (libre) |
| AgendaLuce | Talaan ng Ilaw | Ang Luce ay nangangahulugang "ilaw" | Ipinapakita kung bukas ang shop (libre) |
| AgendaRicetta | Talaan ng Gastos sa Resipe | Ang Ricetta ay nangangahulugang "resipe" | Kinukuwenta ang gastos ng isang resipe at ang cost ratio nito (libre) |
| AgendaNera | Talaan ng mga Suki | Ang Nera ay nangangahulugang "itim." Ang itim na leather notebook | Sumasalubong sa mga suki gamit ang face recognition (binubuo pa) |
| AgendaTurno | Talaan ng Duty | Ang Turno ay Italyano para sa "turn" o "duty shift" | Kinokolekta ang mga hiling ng staff para sa shift at ibinibigay ang schedule na binuo ng sariling AI ng may-ari (malapit na) |

Aling notebook ang bagay sa anong uri ng shop? Ang Talaan ng Oras ay para sa mga shop na may dalawa o higit pang staff na namamahala ng attendance sa papel o sa LINE *(ang pinakamalawakang ginagamit na messaging app sa Japan)*. Ang Talaan ng Kita ay para sa mga magbubukas pa lang ng shop, at para sa mga gustong repasuhin ang kanilang mga numero dahil nagbago ang upa o mga gastos. Ang Gabay sa Susunod na Tambayan ay para sa mga shop na nakasentro sa pagkain at gustong maagang ihatid ang mga customer sa susunod na lugar. Ang Talaan ng Ilaw ay para sa mga independent na shop na mas huli o mas maaga ang pagsasara kaysa sa plano. Ang Talaan ng Gastos sa Resipe ay para sa mga shop na nasa isip lang ang mga resipe pero hindi pa nakukuwenta ang cost ratio.

#### Hindi nagkukuwenta ng sahod ang Talaan ng Oras

Ginagawang clock-in machine ng Talaan ng Oras ang tablet ng shop o ang mga smartphone ng staff, nang walang binabago. Pindutin lang ang pangalan ninyo. Awtomatikong nate-tally ang attendance sheet at maaari itong i-export bilang CSV (format na mabubuksan sa spreadsheet software). Alas-5 ng umaga nagsisimula ang business day, kaya kahit abutin ng madaling-araw ang operasyon, hindi nagpapalit ang petsa.

Pero sinadya kong huwag ipakuwenta ng Talaan ng Oras ang sahod.

Masyadong magkakaiba ang bayad kada oras, mga allowance, at petsa ng cutoff sa bawat shop. Dagdag na 25% sa gabi, hiwalay na kategorya ang mga holiday, araw-araw na halaga ang pamasahe. Kahit paano ko ito buuin, hindi ito magiging angkop sa bawat shop.

Kaya sa halip na magkuwenta, naghanda ako ng "template ng mga tagubiling ibibigay sa isang AI." Ipapaste ng may-ari ang dina-download na attendance CSV at ang template na ito, nang buo, sa anumang AI na karaniwan niyang ginagamit, ChatGPT man, Claude, o Gemini. Pagkatapos, kukuwentahin ng AI ang dagdag sa gabi, bayad sa holiday, at pamasahe, at ililista ang mga ito. Maaaring idagdag sa template ang mga patakaran ng bawat shop, gaya ng "isinasara namin ang libro sa katapusan ng buwan, may dagdag na 25% sa gabi, at hiwalay na kategorya ang Linggo," at awtomatiko itong masasalamin sa kalkulasyon. May mga column ang CSV para sa araw ng linggo at sa pangalan ng holiday para tama ang makuwenta ng AI.

Hindi ako ang may hawak ng mekanismo ng pagkukuwenta; hawak ng bawat shop sa sarili nitong kamay ang sarili nitong mga patakaran. Naisip kong iyon ang pinakamahirap masira.

#### Gabayan sila sa susunod na tambayan, at ipaiwan ang sarili ninyong shop sa kanilang alaala

Ang Gabay sa Susunod na Tambayan ay tool para gumawa ng "page ng gabay sa susunod na tambayan" na ibibigay sa mga customer. Sa mga customer na tapos nang kumain, ginagabayan sila nito papunta sa kalapit na bar o lugar para sa huling kagat, kasama ang ilang minuto ang lakad papunta roon.

Mukha itong tool para ipadala ang mga customer sa ibang lugar, pero may maliit na lihim ito. Ang paggabay sa isang tao sa ikalawang hintuan ay nagpapahiwatig na ang unang hintuan ay ang shop ninyo. Habang tila ipinapasa ang mga customer sa ibang shop, ang totoo ay inuukit nito sa kanilang alaala na "ang unang hintuan ay ang shop na ito." Ganoon ito idinisenyo.

#### Tatlong prinsipyo sa disenyo: awtomatiko, hiram na lakas, iisang tungkulin

May tatlong pare-parehong prinsipyong sinusunod ang lahat ng notebook sa Agenda series.

Ang una ay "awtomatiko." Dapat itong tumakbo nang hindi kailangang hawakan araw-araw ng may-ari. Sa Talaan ng Ilaw, kapag naiparehistro na ang schedule, kusang bubukas at papatay ang ilaw. Walang oras ang may-ari ng restawran na humawak ng screen habang may serbisyo. Ang tool na hindi gumagana kung hindi hinahawakan ay hindi rin magtatagal at titigil na ring gamitin.

Ang ikalawa ay "hiram na lakas." Huwag buuin ang lahat nang mag-isa; ipaubaya sa mga tool at AI na ginagamit na ng may-ari. Ang pagkukuwenta ng sahod sa Talaan ng Oras ang huwarang halimbawa. Ganoon din ang shift notebook: ang hawak lang nito ay ang pagkolekta ng mga kagustuhan ng staff, at ipinauubaya nito sa sariling AI ng may-ari ang pagbuo ng mga shift. Wala itong dalang masalimuot na sariling mekanismo, ni gastos sa pagtawag sa isang AI. Kaya nananatiling mababa ang presyo.

Ang ikatlo ay "iisang tungkulin." Isang bagay lang ang ginagawa ng isang notebook, at ginagawa ito nang maaasahan. Masyadong mabigat para sa isang independent na shop ang sistemang maraming tungkulin. Kapag patuloy kang nagdaragdag ng feature, lalong mahirap itong gamitin, at dumarami ang mga kontradiksyon sa panig ng gumagawa. Iyan ang natutunan ko mismo sa reservation system sa Kabanata 2. Kaya nagdaragdag ako ng mga notebook nang isa-isa, na bawat isa ay gumagawa ng "isang bagay na ito lang nang maayos."

#### Bakit wala sa series ang reservation system

Sa puntong ito, inaasahan kong may malinaw na tanong. Ang pinakamalaking pinaglaanan ng trabaho ng Tamuro ay ang reservation system. Bakit hindi ito inilagay sa Agenda series?

Sa totoo lang, minsan ko itong binalak. Ang plano ay gawing anyong magagamit ng ibang restawran ang reservation system at ilabas ito bilang isa pang notebook ng series. Pero noong Agosto 2026, kinansela ko ang planong iyon.

Ang dahilan ay eksaktong isinulat ko sa Kabanata 1. Punung-puno ng paraan ng pagnenegosyo ng Tamuro ang reservation system nito. Na kalahati ng mga customer ay mga kumakain nang mag-isa. Na halos 90% ng mga reservation ay ginagawa sa mismong araw. Na gusto kong ibenta ang oras bago magbukas. Na gusto kong dumating ang mga tao nang grupo-grupo. Na gusto kong magparami ng mga suki. Ginawa ko ang mga kombinasyon ng diskwento, ang pagkakasunod-sunod ng mga email, at ang paraan ng pagrekomenda ng chat para umangkop sa lahat ng ito.

Kung palalabnawin ko ito para maging pangkalahatan at magamit ng kahit sino, magiging karaniwang reservation system lang ito na puwede na sa bawat shop. Mawawala noon ang lakas ng Tamuro. Ang reservation system at ang CRM ay ang paraan ng shop sa pagbebenta ng sarili nito. Sa halip na iangkop ang shop sa isang pangkalahatang sistema, iangkop ang sistema sa shop. Sarili naming shop, sa sarili naming mga espesipikasyon. Kaya nagpasya akong panatilihing sa Tamuro lang ang reservation system ng Tamuro.

Kaya wala na bang maibibigay lampas sa shop? Mayroon pa. Sa paligid ng reservation system, maraming maliliit na problemang karaniwan sa bawat shop. Panatilihin ang ubod ng shop sa sarili ninyong mga espesipikasyon. Buuin ang mga tool na lumulutas sa mga nakapaligid na problema sa anyong magagamit ng lahat mula sa simula, at ibigay ang mga ito. Ang reservation page ng Tamuro ay isang sampol na pinagsasama ang dalawa sa iisang screen. Sa ibabaw ng reservation system na para lang sa Tamuro ay nakalagay ang karatula ng Talaan ng Ilaw na magagamit ng sinuman.

【Larawan 3-2】Ang pahina ng pagpapakilala sa Agenda series *(Nasa wikang Hapon ang screen.)*

【Larawan 3-3a】Pagpapakilala sa Talaan ng Oras *(Nasa wikang Hapon ang screen.)*

【Larawan 3-3b】Pagpapakilala sa Talaan ng Kita *(Nasa wikang Hapon ang screen.)*

【Larawan 3-3c】Pagpapakilala sa Gabay sa Susunod na Tambayan *(Nasa wikang Hapon ang screen.)*

【Larawan 3-4】Ang clock-in screen ng Talaan ng Oras. Pindutin lang ang pangalan ninyo (synthetic na data) *(Nasa wikang Hapon ang screen.)*

### 3-4 Gumawa para sa Lahat Mula sa Simula

Gumagawa ako ng tool para sa sarili kong shop, tapos ipinamamahagi ko rin sa ibang shop. Madaling sabihin, pero para magawa ito, kailangang magbago ang paraan ng pagpapasya bago magsimulang bumuo.

Kung para lang sa Tamuro ang binubuo ko, ang pinakamabilis na paraan ay isulat nang direkta sa program ang oras ng operasyon at pangalan ng Tamuro. Pero hindi na ito magagamit ng ibang shop. Kung susubukan ninyo itong gawing pangkalahatan sa huli, hahanapin mo ang bawat hard-coded na bahagi at aayusin isa-isa.

Kaya ang mga tool sa Agenda series ay itinakda mula sa simula sa pagpapalagay na magagamit ng lahat. Nagsisimula ako sa isang problema sa Tamuro, pero sa yugto ng mga requirement, pinaghihiwalay ko ang dalawang tanong: "Totoo lang ba ito sa Tamuro, o totoo sa bawat shop?" Huwag ilagay ang pangalan ng shop sa karatula. Hayaang mapili ang wika. Gawing mai-paste sa kahit anong website. Ganitong mga desisyon ang inayos ko habang isinusulat ang requirements document ng Talaan ng Ilaw.

Isa pa itong gamit ng requirements definition na muli kong natutunan sa Kabanata 2. Kapag napagpasyahan ninyo muna ang mga ito, magagamit ninyo ang tool sa Tamuro at maipamamahagi ito sa ibang shop nang walang binabago.

Ang mga problema sa shop ko ay mga problema rin sa ibang shop. Hindi lang ako ang may-ari na gustong ipaalam sa mga customer na nahuhuli ang oras ng pagsasara. Ang may-ari ng isang independent na shop ay bumubuo ng tool mula sa sarili nitong problema, saka ipinamamahagi sa ibang shop. Iyan ang ideya sa likod ng Agenda series.

### 3-5 Ang Demokratisasyon ng Teknolohiya

Mahigit 10 na ang produkto ng Agenda series ngayon. Ako lang ang bumubuo at nagpapatakbo sa mga ito, habang nakatayo sa likod ng bar.

Ilang taon na ang nakararaan, hindi ito maiisip. Para makabuo ng isang produkto, kailangan ninyo ng magpaplano, ng magdidisenyo ng mga screen, ng magsusulat ng code, ng magte-test, at ng magpapatakbo. Kung walang team at pondo, hindi kayo makapaglalabas ng produkto sa mundo.

Iba na ang kalagayan ngayon. Sinasabi ng may-ari sa AI ang mga requirement, isinusulat ng AI ang code, tine-test ito ng AI, at ino-audit ito ng isa pang AI. Ang ginagawa ng may-ari ay magpasya kung ano ang bubuuin, timbangin kung angkop ba sa layunin ng shop ang mga resulta ng AI, at gawin lang ang mga operasyong tao lang ang kayang gumawa.

Ang ganitong pagbabago ay karaniwang tinatawag na "demokratisasyon ng teknolohiya." Hindi na pag-aari ng iilang tao o kumpanya ang kakayahang bumuo.

Pero maging tapat tayo rito. Gaya ng isinulat ko sa Panimula, nagtrabaho ako sa IT nang humigit-kumulang 16 na taon, kadalasan sa pagpaplano ng sistema at bilang tagapag-ugnay sa pagitan ng mga tao sa field at ng mga development vendor. Alam ko ang requirements definition, ang mga konsepto ng database, at ang pagpapatakbo ng mga test, na lahat ay mula sa karanasan. Kaya hindi ko sasabihing magagawa ito ng taong hindi pa nakasulat ng kahit isang linya ng code simula bukas.

Gayunman, malaki na ang nagbago. Nakakabuo na ako ngayon, nang mag-isa at sa mga pagitan ng pangunahing trabaho, ng mga bagay na dati ay nangangailangan ng buong team. At para sa mga walang karanasan, tiyak na mas mababa na ang hadlang sa pagpasok. Magtuturo ang AI kung magtatanong kayo tungkol sa hindi ninyo naiintindihan. Bibigyan nito ng hugis ang sinasabi ninyo sa mga salita. Ang kulang ay hindi teknik, kundi ang kakayahang magpasya kung ano ang bubuuin at ang mga salitang sasabihin sa AI. Mga kakayahan itong araw-araw namang ginagamit ng mga nagpapatakbo ng shop.

