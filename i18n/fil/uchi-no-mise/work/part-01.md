# Gawa para sa Aming Bar

Ang kuwento ng may-ari ng 19-upuang bar na gumawa ng lahat, mula reservation hanggang mga tool, gamit ang AI

Raku Bonta

Ang Agenda series: https://bontallc.com/agenda?via=b2-fil-{{FMT}}

Instagram ng Tamuro: https://www.instagram.com/tamuro.higashinakano/

Reservation site ng Tamuro: https://tamuroreservation.vercel.app/?src=b2-fil-{{FMT}}

## Panimula

Ito ay simpleng tala kung paano pinapatakbo ng may-ari ng isang bar sa Higashi-Nakano na may 19 na upuan *(isang residential na lugar sa kanlurang Tokyo, sa kanluran lang ng Shinjuku)*, Tokyo, ang kanyang shop sa tulong ng AI.

Ang pangalan ng bar ay "Tamuro." Ang ibig sabihin ng pangalan ay lugar kung saan nagtitipon ang mga tao. Nagbukas ito noong Nobyembre 2018, isang maliit na lugar na may 11 upuan sa counter at 8 upuan sa tatami platform. Sa araw, sa parehong espasyo, isang staff ang nagpapatakbo ng restaurant ng hamburger curry na tinatawag na "Quatre Épices."

Sa nauna kong libro, *Ang AI Assistant Manager*, isinulat ko ang tungkol sa generative AI mismo. Sa nakalipas na mga isang taon mula noon, nagbago ang AI: mula sa tool na sumasagot ng mga tanong, naging tool na gumagawa ng trabaho para sa inyo. Bigyan lang ng instruksiyon, at isusulat nito ang program, susubukan, aayusin ang sarili nitong mga pagkakamali, at tatapusin ang gawain. Tinatawag nating agentic AI ang ganitong uri ng AI.

Gamit ang agentic AI, ako mismo ang gumawa ng reservation system ng Tamuro. Gumawa ako ng discount system na kasabay ng pagtaas ng presyo. Gumawa ako ng system para sa pag-aalaga ng mga suki. Gumawa ako ng AI na sumasagot sa mga tanong ng mga customer. At sa huli, umabot ako sa puntong puwedeng magtanong ang isang customer tungkol sa Tamuro mula sa sarili nilang AI, at makapag-reserve pa.

Bukod dito, inangkop ko ang mga kapaki-pakinabang na tool na ginawa ko para sa sarili kong shop upang magamit din ng ibang shop, at sinimulan kong ialok ang mga ito sa halagang ilang daang yen kada buwan. Iyan ang Agenda series.

Inilalarawan ng librong ito kung ano ang ginawa ko sa prosesong iyon, kung saan ako pumalpak, at kung ano ang kinailangan kong pag-aralang muli. Hindi lang ito mga kuwento ng tagumpay. Patuloy akong gumawa ng mga bagay na gumagana nang dala lang ng bugso ng sigla, kaya nagsipatong-patong ang mga kontradiksyon sa sistema. Nalaman ko na lang pagkatapos na nababasa pala mula sa labas ang personal na impormasyon ng mga customer. Nagsulat ang AI ng mga impormasyong hindi naman kailanman sinabi ng shop. Isinama ko ang mga kabiguang ito ayon sa nangyari.

### Paano Basahin ang Librong Ito

May limang kabanata ang librong ito.

| Kabanata | Nilalaman | Para kanino |
| --- | --- | --- |
| Kabanata 1 | Isang Shop na Ma-book ng AI (ang bahaging pangnegosyo ng reservation system) | Lahat |
| Kabanata 2 | Sa Likod ng Reservation System (teknikal) | Mga gumagawa at sinumang mausisa sa teknolohiya |
| Kabanata 3 | Pamamahagi ng mga Tool ng Aming Shop sa Ibang Shop (ang bahaging pangnegosyo ng Agenda series) | Lahat |
| Kabanata 4 | Isang System para sa Patuloy na Pagbuo ng mga Produkto nang Mag-isa (teknikal) | Mga gumagawa at sinumang mausisa sa teknolohiya |
| Kabanata 5 | Ang Kinabukasan ng mga Maliliit na Shop | Lahat |

Teknikal ang Kabanata 2 at 4, at mas maraming espesyalisadong termino ang gamit. Bawat isa ay nagsisimula sa tatlong linyang buod ng mga pangunahing punto, kaya kung hindi kayo interesado sa teknolohiya, basahin lang ang mga iyon at dumiretso sa susunod na kabanata. Basahin ang Kabanata 1, 3 at 5 nang sunud-sunod, at tuluy-tuloy at buo pa rin ninyong masusundan ang takbo ng kuwento.

Hangga't maaari, naglagay ako ng simpleng paliwanag sa tabi ng bawat teknikal na termino. Kahit hindi pa kayo nakapagsulat ng program, sana'y magkaroon kayo ng malinaw na ideya kung ano ang ibig sabihin ng pagpapatakbo ng shop gamit ang AI.

### Tungkol sa May-akda

Mga 16 na taon akong nagtrabaho sa IT, kadalasan sa pagpaplano ng system at bilang tagapag-ugnay ng mga taong nasa mismong lugar ng trabaho at ng mga development vendor, bago ako pumasok sa negosyo ng pagkain at inumin. Kaya hindi ito kuwento ng taong hindi pa nakapagsulat ng kahit isang linya ng code na nakabuo ng lahat nang mag-isa gamit ang AI. Gusto kong maging tapat tungkol diyan.

Gayunpaman, ngayon ay nagagawa at napapatakbo ko nang mag-isa, habang nagtatrabaho sa floor, ang isang bagay na dating nangangailangan ng buong team at puhunan. Ilang taon lang ang nakalipas, hindi iyon maiisip. Gusto kong ilarawan nang kasing-konkreto hangga't kaya ko ang realidad ng pagbabagong iyon.

### Paano Ginawa ang Librong Ito

Ginawa ko rin ang librong ito sa tulong ng AI. Mula sa mga tala na iniingatan ko sa araw-araw kong development work, ang AI ang sumulat ng mga draft, at ako ang nagbasa, nagrebisa at nagpasya. Ipinakuha ko rin sa AI ang mga screenshot na ginamit bilang larawan.

Binasa ko ang lahat, pero ang tekstong isinulat ng AI ay maaaring may kahalong hindi totoo. Gaya ng sinasabi ko sa mismong teksto, sinasabi ng AI na "tapos na," at trabaho ng tao ang pagsuri nito. Maaaring may mga pagkakamali sa librong ito na hindi ko napansin.

Gayundin, nagbabago sa loob ng ilang buwan ang mga detalye ng mga AI tool at serbisyo. Ang mga hakbang, presyo at katayuan ng suporta ng bawat kumpanya na inilarawan sa librong ito ay batay sa kalagayan noong Oktubre 2026. Kapag sinubukan ninyo ito mismo, pakisuri ang opisyal na impormasyon sa panahong iyon.

Kung may makita kayong pagkakamali, matutuwa akong ipaalam ninyo sa akin sa note o X. Itatama ko ang mga ito habang natutuklasan ko.

### Ang Tatlong Susunod na Hakbang ng Librong Ito

Libre itong mabasa bilang PDF, sa note, at sa Google Play. (Sa Kindle lang, may itinakdang pinakamababang presyo ayon sa patakaran ng store.) Bilang kapalit, naghanda ako ng tatlong lugar na maaari ninyong puntahan pagkatapos ninyong magbasa. Kung kahit isa sa mga ito ay may maitulong sa inyo, sulit ang pagsulat ng librong ito.

1. Subukan ito sa sarili ninyong shop. Maaari ninyong simulan ang Agenda series sa libreng planner app. https://bontallc.com/agenda?via=b2-fil-{{FMT}}
2. Sundan ang mga ginagawa ko. Isinusulat ko sa note at X ang tungkol sa mga susunod kong tool at sa pang-araw-araw na buhay sa shop. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Kung mapadpad kayo sa Tokyo, bisitahin ang Tamuro. Isang minuto mula sa east exit ng Higashi-Nakano Station. Puwede kayong pumasok nang walang reservation. Reservation site https://tamuroreservation.vercel.app/?src=b2-fil-{{FMT}}

## Kabanata 1: Isang Shop na Ma-book ng AI

### 1-1 "May Bakante Ba Ngayong Gabi?" Ang Panahon ng Pagtanong sa AI

Sa isang Biyernes ng gabi, may taong kakatapos lang magtrabaho na kumakausap sa kanyang smartphone.

"May lugar ba sa Higashi-Nakano kung saan puwede akong uminom mag-isa ngayong gabi? Yung hindi masyadong maingay."

Hindi kaibigan ang sumasagot. Ito ang AI na ginagamit niya araw-araw. Naglilista ang AI ng mga posibleng shop, inilalarawan ang kapaligiran ng bawat isa, at sinasabi ang mga bakanteng oras at ang mga presyo ngayong gabi. Kung may mapusuan siya, diretso na siyang makakapunta sa reservation screen.

Hindi ito kuwento tungkol sa hinaharap.

Noong August 10, 2026, nagdagdag ang OpenAI ng feature para sa restaurant reservation sa ChatGPT. Ayon sa opisyal na release notes, kumokonekta ito sa mga reservation service na OpenTable, Resy at Yelp, at lumalabas mismo sa loob ng mga sagot ng ChatGPT ang mga available na oras ng reservation. Maaari ring magtanong para paliitin ang mga pagpipilian, at kapag napili na ang oras na bagay sa inyo, maaari na kayong magpatuloy sa pag-book. Saklaw nito ang OpenTable sa buong mundo, ang Resy sa US, at ang Yelp sa US at Canada.

Sa madaling salita, ang pintuang ginagamit ng mga tao para maghanap ng makakainan ay nagsisimulang lumipat mula sa mga search engine at restaurant review site tungo sa "kanilang sariling AI."

Pero may kondisyon. Ang mga shop na nakarehistro lang sa malalaking reservation service ang puwedeng i-book sa pamamagitan ng ChatGPT. Ang mga maliliit na shop na wala sa mga iyon ay hindi nakikita ng AI.

Kaya ano ang gagawin ng isang bar sa Higashi-Nakano na may 19 na upuan na hindi gumagamit ng malalaking reservation service?

Ibang daan ang pinili ng Tamuro. Nang hindi dumadaan sa malalaking serbisyo, direktang ikinonekta nito sa AI ang sarili nitong reservation system.

Kapag tinanong ng isang customer ang sarili niyang ChatGPT o Claude, "May bakante ba ang Tamuro ngayong gabi?", direktang tinatanong ng AI ang reservation system ng Tamuro, tinitingnan ang mga bakanteng oras at ang mga presyo, at sumasagot. Kapag naayos na ang mga kondisyon, itinuturo nito ang customer sa reservation page ng Tamuro kung saan nakalagay na agad ang bilang ng tao at ang petsa at oras. Ang customer mismo ang pipindot ng huling confirm button.

Tinatawag na MCP server ang "punto ng koneksyon sa pagitan ng AI at ng system ng isang shop." Ang MCP ay nangangahulugang Model Context Protocol, isang karaniwang hanay ng mga kasunduan na nagbibigay-daan sa AI na gumamit ng mga panlabas na tool at data. Ipapaliwanag ko ang mga detalye sa Kabanata 2.

Ang totoo, inililipat din ng malalaking reservation service ang customer sa sarili nilang screen sa dulo. Para sa mga reservation na nangangailangan ng credit card, natatapos ang proseso sa screen ng OpenTable, at sa panig ng bawat serbisyo hinahawakan ang mga pagbabago o pagkansela pagkatapos mag-book. Ang AI ang pasukan, at ang screen ng reservation service ang pinagkukumpirmahan. Ganito rin ang istruktura ng ginagawa ng Tamuro. Ang tanging pagkakaiba ay walang malaking kumpanya sa gitna.

At ang gumawa ng system na ito ay hindi isang panlabas na development company. Ako iyon, ang may-ari. Nagbigay ako ng mga instruksiyon sa AI, pinasulat ko sa AI ang mga program, at pinatakbo ko sa AI ang mga test.

Siyempre, hindi ako dito nagsimula. Nagsimula ito sa isang napakasimpleng reservation form. Sumunod ang pagtaas ng presyo, tapos ang mga ideya para sa discount, tapos ang system para sa pag-aalaga ng mga suki, tapos ang mga pagkabigo at ang muling pagbuo.

Ilalarawan ko muna sa limang linya kung anong klaseng lugar ang Tamuro. Isang minutong lakad mula sa east exit ng Higashi-Nakano Station. 19 na upuan, 11 sa counter at 8 sa tatami room. Halos kalahati ng mga customer ay dumarating nang mag-isa, at madaling makipag-usap sa katabi sa counter. Ang pagkain ay kombinasyon ng apat na appetizer at isang main, at ang pinakasikat na putahe ay ang matamis at maraming bawang na tonteki (pork steak). Karamihan sa mga wine ay mula sa Spain at Italy, at may humigit-kumulang 20 uri ng Japanese craft gin. Puwede kayong pumasok nang walang reservation.

Bago magpatuloy, sasabihin ko muna ang isang bagay na nilalayon ko. Ayaw kong tumanggap lang ng mga reservation. Gusto kong magawa ng kahit maliit na shop, sa sarili nitong kamay, ang buong daloy ng pagiging kilala, pagkakaroon ng mga bumibisita, at pagpapabalik sa kanila. Ang mga discount, email at chat window na lumilitaw sa kabanatang ito ay pawang mga bahaging naglilingkod sa iisang layuning iyon.

Sa kabanatang ito, ibabalik ko ang oras at susundan kung paano lumago ang reservation system ng Tamuro.

【Larawan 1-1】Ang screen pagkatapos kumonekta mula sa ChatGPT sa MCP server ng Tamuro (October 10, 2026). Binabasa nito ang impormasyon ng shop at sinasabing kaya nitong asikasuhin ang mga bakanteng oras, mga course, mga presyo, at paggabay sa reservation page *(Nasa wikang Hapon ang screen.)*

### 1-2 Ang Panimulang Punto: Pagtanggap Lang ng mga Reservation

[Ang reservation site ng Tamuro](https://tamuroreservation.vercel.app/?src=b2-fil-{{FMT}}) ay napakasimple noong una. Pumili ng petsa, oras at bilang ng tao, ilagay ang pangalan at contact details, at ipadala. May notification na darating sa shop. Iyon lang.

Binuo ko ang unang pundasyon gamit ang AI development tool ng Google (Antigravity). Sinabi ko sa AI ang bawat feature na naisip ko, at kapag gumana, lumipat ako sa susunod. Ito ang tinatawag na vibe coding (sinasabi sa AI ang kahit anong pumasok sa isip at ipinagagawa ito nang batay sa pakiramdam).

Para sa akin noon, sunud-sunod ang mga sorpresa. Ilarawan sa salita ang layout ng isang screen, at nabubuo ito sa loob ng ilang minuto. Sabihing gusto ninyo ng calendar, at may lilitaw na calendar. Sa mga pagitan ng pagpapatakbo ng shop, nabuo ang isang reservation site.

Ang Tamuro ay lugar na puwedeng pasukan nang walang reservation. Sa katunayan, karamihan sa mga reservation ay ginagawa sa mismong araw, at maraming customer ang basta na lang pumapasok. Gayunpaman, gumawa ako ng reservation system dahil gusto ko ng paraan para makaugnayan ang mga customer bago sila bumisita. Kapag nag-reserve ang isang tao, nananatili ang pangalan at contact details niya. Kapag nananatili ang contact details, maaari ko siyang anyayahang bumalik.

Ang reservation system ay hindi lang front desk. Nagiging pasukan ito sa relasyon sa customer. Ang ideyang ito ang kalaunan ay nagbunga ng discount system at ng system para sa pag-aalaga ng mga suki.

Pero dahil binuo lang ito nang batay sa pakiramdam (vibe), malaki ang kinailangan kong bayaran pagkatapos. Isusulat ko iyon sa Kabanata 2.

### 1-3 Sabay na Pagbuo ng Pagtaas ng Presyo at mga Discount

Para sa isang restaurant o bar, ang pagtaas ng presyo ay desisyong hindi maiiwasan. Patuloy na tumataas ang presyo ng mga sangkap, utilities at paggawa. Nagtaas din ng presyo ang Tamuro. Itinaas ko ang bawat course nang humigit-kumulang ¥400–¥500 (humigit-kumulang $2.7–$3.3).

Malaki ang pagtaas, kaya halata na kung ilalabas ko ito nang ganoon lang, magsisialisan ang mga suki. Kaya kasabay ng pagtaas ng presyo, nagpasya akong magbuo ng discount system sa loob ng reservation system. Hindi lang ito basta nagpapamura. Ginagantimpalaan nito ng discount ang mga customer na kumikilos sa paraang mabuti para sa shop.

Una ang group discount. Habang dumarami ang tao sa grupo, bumababa ang presyo kada tao. Halos kalahati ng mga customer ng Tamuro ay dumarating nang mag-isa, pero kung dumating sila nang grupo, malaki ang pagtaas ng benta ng shop. Kahit ibawas ang discount, lamang pa rin ang shop. Para sa mga customer naman, dahilan ito para anyayahan ang mga kaibigan. Sa katunayan, dumami ang mga customer na dumarating nang grupo gamit ang party-size discount ng reservation site.

Ikalawa ang early-bird discount. Kung magre-reserve kayo nang hindi bababa sa isang linggo bago ang takdang araw, may 2% off kayo; kung dalawang linggo o higit pa bago ang takdang araw, 4% off. Karamihan sa mga reservation sa Tamuro ay ginagawa sa mismong araw, kaya hindi ko mahulaan ang darating. Ang early-bird discount ay mekanismo para masiguro ang mga benta sa hinaharap. Sa mga maulang araw at malamig na araw, kung may mga reservation na, makakapaghanda nang panatag ang shop.

Ikatlo, gumawa rin ako ng mekanismo ng group buying. Kung may itinakdang bilang ng taong magtipon sa itinakdang petsa at oras, mag-aalok ng set-meal course sa may-discount na presyo. Dapat itong maging mekanismong may diwa ng Tamuro, kung saan nagtitipon sa parehong oras ang mga hindi magkakakilala.

Pero hindi talaga ginamit ang planong group buying. Walang resulta, zero. Noong August 2026, itinigil ko ang planong ito at nagpasya akong huwag na itong gamitin muli.

Nakakapanghinayang itapon ang isang bagay na ginawa ninyo. Pero kung gagawa kayo gamit ang AI, maliit ang gastos at oras ng paggawa. Gumawa nang maliit, subukan, at kung hindi gumana, itapon. Naniniwala akong ang bilis na ito ang pinakamalaking bentahe ng pagpapatakbo ng shop gamit ang AI.

May isa pang taktika sa pagpepresyo. Sa mga plan, sadya akong naglalagay ng mahal na premium plan. Okay lang kahit halos walang pumili ng premium plan. Dahil may mahal na plan sa tabi nito, mukhang abot-kaya ang standard. Ginagampanan nito ang tinatawag na anchor (isang sanggunian para sa paghahambing).

【Larawan 1-7】Habang dumarami ang tao, bumababa ang presyo kada tao (paghahambing ng 1, 4 at 6 na guest)

### 1-4 Isang System para sa Pag-aalaga ng mga Suki

Kapag nananatili na sa reservation system ang mga pangalan at contact details, ang susunod na gusto ninyong gawin ay alagaan ang relasyon sa mga customer. Tinatawag na CRM (customer relationship management) ang system na namamahala ng impormasyon ng customer at nagpapalalim ng relasyon. Unti-unti, nagdagdag ako ng mga CRM feature sa reservation system ng Tamuro.

Kapag nagparehistro bilang member ang mga customer, makikita nila ang kasaysayan ng kanilang mga reservation sa My Page. Kung ilalagay nila ang kanilang kaarawan, darating ang birthday perk. Ang mga member na matagal nang hindi bumibisita ay makakatanggap ng mensaheng tumatawag sa kanila pabalik. May stamp card din. Sa tatlong pagbisita, may isang libreng inumin; sa lima, may steak at iba pang perk, at pagkatapos ng lima ay magsisimula muli ang bilang. May feature din para sa pag-imbita ng mga kaibigan.

Espesyal na pag-iingat ang ibinigay ko sa pagdisenyo ng mekanismo para sa pag-anyaya ng ikalawang pagbisita. Sa mga restaurant at bar, sinasabing ang pagbabalik ng unang beses na customer sa ikalawang pagkakataon ang nagpapasya kung magiging suki siya. Sa Tamuro, nagpapadala ako ng dalawang follow-up email, pitong araw at 21 araw pagkatapos ng unang pagbisita. Walang coupon ang una; ang ikalawa lang ang mayroon. Sa halip na akitin sila ng discount mula pa sa simula, tinutulungan ko muna silang makaalala. Kung hindi pa rin sila dumarating, saka ko sila bibigyan ng munting tulak.

Pinag-ingatan ko rin na hindi magpatung-patong ang mga email. Pinakamarami nang isang mensahe kada araw ang natatanggap ng mga customer. Kapag nagsasapawan, ganito ang pagkakasunod-sunod ng prayoridad: kaarawan, imbitasyon sa ikalawang pagbisita, pagtawag pabalik sa mga member na matagal nang di bumibisita, iba pang abiso. Ang mga member na may susunod nang reservation ay hindi tumatanggap ng mga email na nag-aanyayang bumisita.

Naka-off bilang default ang pagsang-ayon sa pagtanggap ng email. Madaragdagan ang bilang ng tatanggap kung iiwan itong naka-on, pero ang disenyong pumapayag ang mga tao nang hindi nila alam ay maaaring maging problema sa ilalim ng batas sa proteksyon ng consumer. Tiwala ang pagsikapang makuha, hindi bilang. Iyon ang naging pasya ko.

May isa pang munting detalye sa mga email. May isang "Paksa Ngayong Araw" na kasama sa reservation confirmation email. Isang bagay tungkol sa panahon, wine o pagkain. Awtomatikong sumusulat ang AI ng maikling paksa araw-araw.

Ang layunin ay bigyan ang customer ng pampasimula ng kuwentuhan bago siya bumisita. Ang Tamuro ay shop na maraming usapan sa pagitan ng mga customer. Ang paksang nabasa sa email ay nagiging unang sasabihin niya sa katabi sa counter. Kaya hindi ko hinayaang magtapos sa "Natanggap na ang reservation ninyo" ang confirmation email, at pinahatid ko rito nang maaga ang kaunting kapaligiran ng shop.

Minsan ko nang pinalitan ang AI na sumusulat ng mga paksa. Pinalitan ko ito ng isang gumagawa ng mga paksang mas natural at mas malapit sa tono ng shop. Gayunman, hindi ito mekanismo para dumami ang customer. Mekanismo ito para pagandahin nang kaunti ang karanasan ng mga dumarating. Isusulat ko muli ang pagkakaibang iyon sa ikalawang kalahati ng kabanatang ito.

Sa mga mekanismong ito, ang unti-unting nakitaan ng resulta ay ang mga plan na "Nice to Meet You" at "Welcome Back." Ito ay mga plan na madaling salihan at makatuwiran ang presyo, na unang beses pa lang na customer at mga customer na higit isang taon nang hindi bumibisita lang ang puwedeng pumili. Binibigyan nila ng dahilan para dumating ang parehong mga bagong customer at ang mga unti-unting lumalayo.

Sa kabilang banda, may problema rin. Maraming customer ang nagbu-book bilang guest nang hindi nagpaparehistro bilang member. Kung hihingin ko ang pagpaparehistro bilang member sa bawat reservation, maaaring sumuko na lang sila sa pag-book. Kaya pagkatapos ng isang reservation, nagpapakita ako ng prompt na "Gusto ba ninyong iugnay ang reservation na ito sa isang member account?", at gumawa ako ng paraan para maging member pagkatapos. Hindi ito nagdadagdag ng hadlang sa pag-book, at pinag-uugnay nito ang relasyon sa kalaunan.

【Larawan 1-8】Mga plan na ang unang beses pa lang na customer at mga hindi pa bumibisita nang higit isang taon lang ang puwedeng pumili *(Nasa wikang Hapon ang screen.)*

【Larawan 1-9】Ang stamp card sa My Page (synthetic data) *(Nasa wikang Hapon ang screen.)*

【Larawan 1-5】Reservation confirmation email. May kasamang isang "Paksa Ngayong Araw" (synthetic data) *(Nasa wikang Hapon ang screen.)*

### 1-5 Sa Pamamagitan ng mga Numero: Humigit-kumulang 88% ng mga Reservation ay Para sa Mismong Araw

Habang patuloy akong nagdaragdag ng mga mekanismo, may napansin ako. Hindi ko masabi kung alin sa mga ito ang gumagana.

Kaya binilang ko ang data ng mga reservation. Sa 244 na reservation sa nakaraang 90 araw, 215 ang same-day reservation. Iyon ay 88.1%. Ang average ay 2.71 reservation kada araw.

Ang Tamuro ay hindi lugar na nire-reserve ng mga tao, kundi lugar na pinupuntahan nila nang biglaan. Naging malinaw lang ito nang suriin ko ang mga numero.

Dalawang bagay ang nakita mula sa mga numerong ito.

Ang isa ay kung paano buuin ang reservation form. Kung karamihan ng reservation ay para sa mismong araw, mas maginhawa kung napili na ang pinakamalapit na bukas na slot ngayong araw sa pagbukas ng reservation screen. Sa kabilang banda, may ilang taong gustong mag-book ng mas huling petsa na nakakapagpadala nang walang ingat bilang ngayong araw. Kaya pinatingkad ko ang ngayong araw sa calendar, at sa confirmation screen ipinapakita ko nang malaki ang petsa at oras na may "Ngayon." Pinanatili ko ang kaginhawahan ng pagpili ng mismong araw, at ginawa kong madaling mapansin ang mga pagkakamali.

Ang isa pa ay ang kahulugan ng early-bird discount. Ang dami ng same-day reservation ay nangangahulugang hindi natin mahulaan ang mga benta sa hinaharap. Sapat na ang masamang panahon para bumaba ang dami ng taong dumarating. Para madagdagan kahit kaunti ang mga advance reservation, kailangang mas maraming gumamit ng early-bird discount. Ang kamalayang ito ang kalaunan ay nagbunga ng kuwento ng pagbuo ng AI na nagpo-post para sa may-ari.

Para tumingin sa mga numero, kailangan ninyo ng system na pambilang. Walang anumang access analytics ang reservation site. Hindi ko masabi kung ilan ang dumating sa reservation page, ilan ang tumigil sa gitna, at ilan ang nakatapos. Kaya nagdagdag ako ng system na nagbibilang ng tatlong yugto: dumating sa page, nagpasya sa mga detalye, natapos ang reservation. Hindi nito itinatala kung sino ang dumating, ang yugto at ang oras lang.

Kalaunan, gumawa rin ako ng system na nag-e-email ng lingguhang ulat na nagbubuod ng mga numero ng reservation. Ilalarawan ko kung paano ito nabuo sa 1-7.

【Larawan 1-3a】Mas litaw ang ngayong araw sa calendar *(Nasa wikang Hapon ang screen.)*

【Larawan 1-3b】Sa confirmation screen, lumilitaw nang malaki ang petsa at oras bilang "Ngayon" *(Nasa wikang Hapon ang screen.)*

