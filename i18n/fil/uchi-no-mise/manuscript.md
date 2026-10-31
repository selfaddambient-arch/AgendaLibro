# Gawa para sa Aming Bar

Ang kuwento ng may-ari ng 19-upuang bar na gumawa ng lahat, mula reservation hanggang mga tool, gamit ang AI

Raku Bonta

Ang Agenda series: https://bontallc.com/agenda?via=b2-tl-{{FMT}}

Instagram ng Tamuro: https://www.instagram.com/tamuro.higashinakano/

Reservation site ng Tamuro: https://tamuroreservation.vercel.app/?src=b2-tl-{{FMT}}

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

1. Subukan ito sa sarili ninyong shop. Maaari ninyong simulan ang Agenda series sa libreng planner app. https://bontallc.com/agenda?via=b2-tl-{{FMT}}
2. Sundan ang mga ginagawa ko. Isinusulat ko sa note at X ang tungkol sa mga susunod kong tool at sa pang-araw-araw na buhay sa shop. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Kung mapadpad kayo sa Tokyo, bisitahin ang Tamuro. Isang minuto mula sa east exit ng Higashi-Nakano Station. Puwede kayong pumasok nang walang reservation. Reservation site https://tamuroreservation.vercel.app/?src=b2-tl-{{FMT}}

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

[Ang reservation site ng Tamuro](https://tamuroreservation.vercel.app/?src=b2-tl-{{FMT}}) ay napakasimple noong una. Pumili ng petsa, oras at bilang ng tao, ilagay ang pangalan at contact details, at ipadala. May notification na darating sa shop. Iyon lang.

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

### 1-6 Napakaraming Plan na Mapagpipilian

Nang maitatag na ang discount system, ang gusto ko namang gawin ay dagdagan ang mga oras at plan na nabebenta.

Hindi napupuno ang oras ng 6 p.m., kaya gumawa ako ng happy hour hanggang 7 p.m. Para sa mga dumarating pagkatapos kumain, gumawa ako ng drink-only plan na walang pagkain. Ang course meal at cooking class, na dating buwan-buwang ginaganap, ginawa kong on-demand na event na bubukas kapag may nag-sign up, na tinatanggap sa pamamagitan ng reservation site. Para maibenta ang oras bago magbukas tuwing weekend, mula 3:30 p.m., gumawa ako ng party plan para sa mga grupong anim na tao pataas.

May dahilan ang bawat isa. Halimbawa ang party plan: kung ginawa kong mukhang bargain ito sa presyo, ang maaakit lang nito ay ang mga customer na pumipili na ng standard plan, at bababa ang benta. Kaya inilagay ko ang pagkakaiba hindi sa presyo kundi sa mga oras bago magbukas, na kailanman ay hindi nagdala ng anumang benta. Walang kinikita ang happy hour discount kung pagsasamahin sa iba pang discount, kaya nagpasya akong hindi ito puwedeng isama.

At sa gayon dumami ang mga plan. Standard, Premium, Nice to Meet You, Welcome Back, Happy Hour, Drink Only, Course Meal, Cooking Class, Party. Bawat isa ay may mga kondisyon sa bilang ng tao, ang ilan ay tumatanggap ng discount at ang ilan ay hindi, at may mga limitasyon sa oras.

Isang araw, binuksan ko ang reservation form at napagtanto ko: hindi makakapili ang mga customer dito.

Ako, ang gumawa, ay nauunawaan ang bawat pagkakaiba. Pero ang taong unang beses pa lang magbubukas ng reservation site, kaya ba niyang paghambingin ang siyam na plan at ang mga kondisyon ng discount ng mga ito at piliin ang bagay sa kanya? Kung hindi, susuko siya sa gitna ng pag-book. Ang mga plan na pinagsikapan kong idagdag ay maaaring magpababa pa ng mga reservation.

Puwede sana akong mag-ayos at magbawas. Pero bawat plan ay may oras na gusto kong maibenta at customer na gusto kong dumating. Ayaw kong tanggalin ang alinman.

Kaya naisip ko ang isang system kung saan kumokonsulta ang customer sa AI para magpasya ng plan. Sabihin lang ang bilang ng tao, ang petsa at oras na gusto ninyong dumating, at kung paano ninyo gustong i-enjoy ang gabi, at ibibigay ng AI ang angkop na plan at presyo at dadalhin kayo diretso sa pag-book. Ang shop ang pumapasan ng pagiging masalimuot ng mga plan. Ang natitira para sa customer ay usapan na lang.

Ang system na ito ang "T-AI-MURO" na isinusulat ko sa 1-8. Bago iyon, may isa pa akong napansin sa panahong ito.

【Larawan 1-2】Pagpili ng plan sa reservation form. Ganito karaming tab ang nakahanay *(Nasa wikang Hapon ang screen.)*

### 1-7 "Nakakapagdala Ba Talaga Ito ng mga Customer?"

Sa araw na idinagdag ko ang party plan, buong araw akong gumawa ng sunud-sunod na pagpapahusay sa reservation site. Pinaliit ko ang espasyo ng header, itinugma ko ang disenyo ng email, at pinalitan ko ang AI na gumagawa ng mga paksa ng usapan para sa mga customer sa loob ng shop.

Pagsapit ng gabi, bigla akong tinamaan ng isang tanong.

"Nakakatulong ba talaga ito para magdala ng mas maraming customer?"

Nang tanungin ko ang AI, tapat nitong inuri ang mga pagpapahusay ng araw na iyon.

| Kategorya | Mga pagpapahusay ng araw na iyon |
| --- | --- |
| Mga bagay na maaaring lumikha ng bagong reservation | Party plan, ang 3:30 p.m. na slot tuwing weekend at holiday |
| Mga bagay na nagpapataas ng completion rate ng mga bumibisita sa site | Pagbawas ng espasyo sa header, pag-aayos ng mga tab |
| Mga bagay na naghihikayat ng pagbabalik | Pag-iisa ng disenyo ng email |
| Mga bagay na hindi nakakatulong magdala ng mga customer | Pagpapalit ng AI na gumagawa ng mga paksa ng usapan, ang link papunta sa susunod na hintuan, ang abiso tungkol sa Agenda |

Sa mga pagpapahusay ng araw na iyon, ang party plan at ang 3:30 p.m. na slot lang ang direktang nagdala ng mga customer. Ang iba ay mga pagpapahusay para hindi mawala ang mga taong dumating na. Mahalaga rin ang mga iyon, pero hindi nila dinaragdagan ang mga customer.

May mas malaking problema. Para sa alinman sa mga pagpapahusay, wala akong paraan para sukatin kung gumana ba. Walang numerong nag-uugnay sa "pinahusay ko" at "dumami ang mga customer."

Isang parirala ang sagot ko: "Gumawa tayo ng isa."

Kaya sinimulan kong gumawa ng lingguhang ulat sa pagkuha ng customer. Ang bilang ng mga reservation, bilang ng mga guest, kabuuang halaga, mga pagkansela. Mga breakdown ayon sa araw ng linggo at oras ng araw. Ang ratio ng mga unang beses na customer sa mga bumabalik. Ang bilang para sa mga party at 3:30 p.m. na slot. Kung saan nanggaling ang mga reservation (ang reservation form, ang chat window, mga reservation mula sa AI, mga manu-manong entry ng shop). Ang bilang ng click sa email, at ang bilang ng mga reservation sa loob ng pitong araw mula sa mga click na iyon.

Laging may kaakibat na oras ang mga numero. Sa parehong araw, may nahanap pa akong isa pang butas. Itinakda ko ang cooking class at ang 3:30 p.m. na slot ng party bilang "weekend," pero nang pagtakhan ko, "Ano ang mangyayari sa mga public holiday?" at siyasatin ito, wala palang konsepto ng public holiday ang reservation system. Sa isang holiday na Lunes, bukas ang shop, pero hindi lumitaw ang 3:30 p.m. na slot. Binigyan ko ito ng listahan ng mga public holiday at inayos kong ituring ang mga ito gaya ng weekend. Butas ito na walang makakapansin hangga't hindi ito napapansin ng mismong gumawa.

Bago buuin ang ulat, tinakpan ko muna ang mga butas na may kinalaman sa oras.

Kahit ang mga suki na dumarating na bago ko pa ginamit ang reservation system ay mukhang "unang beses na customer" sa mga talaan. Kaya sa ulat, isinusulat ko ang "unang pagbisita sa talaan" at palagi kong inilalagay ang petsa kung kailan nagsimula ang mga talaan. Para hatulan kung gumana ang isang pagpapahusay, kailangan ninyo ang larawan bago nito. Para sa unang ulat, nagbilang ako pabalik sa nakaraang walong linggo at ginamit iyon bilang baseline. Sa linggong pansamantalang sarado ang shop, dahil sa biyahe o iba pang dahilan, natural na bumababa ang mga reservation. Kaya inililista ko rin ang bilang ng mga araw ng operasyon, para maihambing kada araw ng operasyon.

Ang seksiyong "Mga Kapansin-pansing Pagbabago" ay itinigil kong ipasulat sa AI, at pinasunod ko sa mga nakatakdang kalkulasyon at nakatakdang pangungusap. Para ito mapanatiling zero ang lingguhang gastos. Hindi lumilitaw sa ulat ang mga pangalan at contact details ng mga customer; mga bilang at ratio lang ang ipinapakita.

Nang makabuo ako ng paraan ng pagsukat, nagbago ang mismong paraan ng paggawa ko ng mga pagpapahusay. Nagsimula akong magpasya sa isang pagpapahusay at sa paraan ng pagsukat ng epekto nito nang magkasama mula pa sa simula. Ang pagsukat ay hindi bagay na pag-iisipan pagkatapos ng pagpapahusay; kasama ito sa parehong dokumento ng instruksiyon ng pagpapahusay. Iyon ang natutuhan ko sa araw na iyon.

【Larawan 1-6】Ang lingguhang ulat sa pagkuha ng customer na dumarating bawat linggo (synthetic data) *(Nasa wikang Hapon ang screen.)*

### 1-8 Isang Bintana Kung Saan Makakausap ang Shop: "T-AI-MURO"

Gaya ng isinulat ko sa 1-6, dumami ang mga plan, at naging mahirap pumili sa reservation form para sa unang beses na bisita. At gusto ng mga unang beses na customer na malaman ang higit pa sa mga plan at petsa. Anong klaseng kapaligiran ang mayroon ang lugar? Hindi kaya ako magmukhang out of place kung mag-isa lang ako? Anong klaseng tao ang may-ari? Okay lang bang magdala ng mga bata? Kung maglalagay lang kayo ng hanay ng mga reservation button nang hindi sinasagot ang mga tanong na tulad nito, hindi ninyo maibibigay sa taong nag-aalinlangan ang tulak na kailangan niya.

Kaya nagpasya akong maglagay ng "bintana kung saan makakausap ang shop" sa reservation site. Kapag nagsulat ng tanong ang isang customer, sumasagot ang AI bilang ang shop. Kung maayos na ang bilang ng tao at ang petsa sa gitna ng usapan, makakapunta nang diretso ang customer sa reservation confirmation screen. Tinatawag itong "T-AI-MURO," at sa usapan, nagpapakilala ito bilang "Tamuro." Nagsasalita ang T-AI-MURO bilang ang mismong shop, at tinutukoy ang may-ari sa ikatlong panauhan.

Halos walang tina-type ang mga customer. Tina-tap lang nila ang mga pagpipiliang iniaalok ng T-AI-MURO, at umuusad ang usapan. Ibig sabihin, ang mga pagpipiliang iniaalok nito sa susunod ang nagpapasya sa kalidad ng usapan. Palagi akong naghahalo ng tatlong uri ng galaw sa mga pagpipilian: mga galaw tungo sa reservation (bilang ng tao, presyo, mga bukas na slot, petsa at oras), mga galaw tungo sa pagkilala sa shop (kapaligiran, ang may-ari, sino ang mga customer, kung puwede bang makipag-usap sa katabi), at mga galaw na bumubukal mula sa daloy ng usapan. Ang paghatid sa mga tao sa reservation ay hindi lang ang layunin. Ang pagpapaalam sa kanila tungkol sa kapaligiran ng shop at sa may-ari ay ubod din ng bintanang ito.

Ang mga presyo lang, nagpasya ako, ang hindi kakalkulahin ng AI. Walang garantiya na tama nitong makakalkula, sa bawat pagkakataon, kung paano nagpapatung-patong ang mga discount o kung paano nalalapat ang mga tier batay sa bilang ng tao. Ang program ang gumagawa ng mga presyo at bukas na slot gamit ang mga nakatakdang kalkulasyon, at ang AI ay nananatili sa trabahong ilagay ang mga ito sa salita.

#### Ang unang kaalaman ay nagmula sa sarili kong mga nakaraang post

Para masagot ng T-AI-MURO ang mga tanong tungkol sa shop, kailangan nito ng kaalaman tungkol sa shop. Bilang materyal, in-export ko ang lahat ng post na naisulat ko na sa Instagram at X (dating Twitter) at ginamit ko ang mga ito. Mula sa mga iyon, binuo ko ang mga tanong na malamang itanong ng mga customer, at ang mga sagot.

Nang subukan ko talaga, lumabas na mas kapaki-pakinabang na materyal ang mga post sa X kaysa sa Instagram. Halos puro larawan ang Instagram, kaunti ang salita. Sa X, nag-iwan ako ng mga nakasulat na talaan, sa sarili kong mga salita, tungkol sa pagkain, sa shop, at sa iniisip ko.

#### 9 lang sa 36 ang pumasa

Bago ilagay ang T-AI-MURO sa production, sinubukan ko kung gaano katumpak ang mga sagot nito. Pinatakbo ko rin sa AI ang mga test. Binigyan ko ng karakter at layunin ang isang AI na gumaganap na customer, at pinakausap ko ito sa T-AI-MURO. Naghanda ako ng 36 na scenario: "mag-isa ngayong gabi," "4 na tao sa loob ng dalawang linggo," "may kasamang bata," "allergy," "private booking," "abiso ng pagkahuli," "pinagmulan ng pangalan ng shop," "anong klaseng tao ang may-ari," at iba pa.

Ang resulta ng unang round: 9 ang pumasa sa 36.

Ang pinakamadalas na sagot ay "Pasensya na, hindi ko po nasagot nang maayos iyan." Lumabas pa ang sagot na ito sa mga tanong tungkol sa kapaligiran ng shop at sa may-ari. Tuwing lumilitaw ang mga salitang tulad ng "reservation," "ngayon," "private booking," o "master," lumalabas ang listahan ng mga bukas na slot anuman ang tunay na tinatanong. Sa ilang usapan, itinuring na bagong reservation ang mensahe tungkol sa pagkahuli. Sa isang vegetarian na customer, nagbigay ito ng stir-fried dishes na may bonito flakes at miso soup bilang mga halimbawa. Nagbigay pa ito ng impormasyon sa English tungkol sa group purchase na itinigil na namin.

#### Sinagot ko ang 11 tanong nang tig-iisang linya

Bahagi ng sanhi ay nasa kung paano binuo ang program. Iiwan ko ang kuwentong iyon para sa Kabanata 2. Ang isa pang sanhi ay simple: kulang ang mga katotohanan tungkol sa shop. Hindi masasagot ng AI ang hindi nito alam.

Kaya tinipon ko ang mga tanong na hindi masagot ng AI at nagpasya akong sagutin ang mga iyon mismo, tig-iisang linya.

Puwede kayong pumasok nang walang reservation. Mahirap tumanggap ng mga batang wala pa sa edad ng elementarya. Mga pagkansela at pagbabago hanggang isang araw bago, sa pamamagitan ng email, telepono, o mensahe sa social media. Para sa abiso ng pagkahuli, pakitawagan. May smoking area sa labas ng shop. Pinapayagan ang pagdadala ng sariling inumin na may corkage fee. Posible ang private booking depende sa saklaw ng presyo at oras, hanggang pinakamarami na 19 na tao. Ang mga dietary restriction at anibersaryo ay aasikasuhin namin hangga't kaya, kaya pakikonsulta sa amin nang maaga. Halos tuwing araw ng operasyon, nasa shop ang may-ari. May yukata festival na pinaplano mga isang beses kada taon.

Iyon lang. Sa pagsagot lang ng 11 tanong nang tig-iisang linya, 24 sa 36 ang pumasa sa ikalawang test.

| Tanong | Unang sagot | Ikalawang sagot |
| --- | --- | --- |
| Puwede bang magdala ng bata? | Pasensya na, hindi ko po nasagot nang maayos iyan | Puwedeng tanggapin ang edad ng elementarya pataas kung kokonsulta kayo sa amin. Mahirap ang mas bata pa sa edad ng elementarya |
| Puwede bang pumasok nang walang reservation? | (listahan ng mga bukas na slot) | Puwede kayong pumasok nang walang reservation |
| Nandiyan ba ang master ngayon? | (listahan ng mga bukas na slot) | Halos tuwing araw ng operasyon, nasa shop ang may-ari. Araw ng operasyon ngayon, kaya inaasahang nasa shop ang may-ari |
| Tahimik ba ang lugar? Puro suki ba? | Pasensya na, hindi ko po nasagot nang maayos iyan | Lugar ito para magpahinga. Madaling magkaroon ng usapan sa pagitan ng mga customer, at hindi ito maingay na lugar |

Dito nagsimulang lumitaw ang isang padron. Ang AI ang gumagawa ng mga tanong na inaasahan natin, sinasagot ito ng T-AI-MURO, at inaayos natin ang mga pagkakamali. Pagkatapos, ang mga tanong lang na hindi masagot dahil kulang ang mga katotohanan ng shop ang ipinapasa sa may-ari. Ang kailangan lang gawin ng may-ari ay isang linya lang para sa bawat tanong na hindi masagot. Ang lahat ng iba pa, AI ang nagpapatakbo.

#### Ang eksenang pumalpak ang "budget na ¥5,000 (humigit-kumulang $33)"

Nilagyan ko rin ng hatol ng AI ang mga AI test. Ang isang ibang AI ang bumabasa ng log ng usapan at nagpapasya kung pasa o bagsak.

Kabilang dito ang isang scenario na may customer na ang "budget ay ¥5,000 (humigit-kumulang $33)." Pasa ang hatol ng AI. Magalang na naglahad ang T-AI-MURO ng mga plan na pasok sa budget.

Pero nang basahin ko, bagsak iyon. Hindi nito tinanong ang bilang ng tao. May group discount ang Tamuro. Depende sa bilang ng tao, nagbabago ang mga plan na mapipili ninyo sa parehong budget.

Sa puntong iyon, inulit ko ang layunin.

"Layunin ang pinakamalaking grupong posible, para pumasok ang kabuuang halaga. Kumpirmahin ang bilang ng tao. Ang huling layunin ay mapadating ang mga customer. Habang mas marami, mas mabuti. Para tumaas ang benta."

Sa iisang pahayag na iyon, nagbago ang buong disenyo ng usapan. Palaging kumpirmahin ang bilang ng tao bago sumagot tungkol sa mga presyo, at sumagot gamit ang kabuuang halaga. Bago ang isang hakbang sa group discount, idagdag ang "isa pang tao at makakakuha kayo ng ganitong porsiyentong off." Kapag may ibinigay na budget, ipakita muna ang pinakamataas na plan sa loob ng budget. Gayunman, kalahati ng shop ang mga customer na dumarating nang mag-isa, kaya para sa customer na isa lang, huwag magmungkahing dagdagan ang bilang ng tao.

Kapag pinatakbo ninyo sa AI ang mga AI test, mabilis silang tumatakbo. Pero tao ang nagpapasya ng pamantayan para pumasa. Kung kaya ninyong sabihin ang layunin sa isang pangungusap. Iyon ang nagpasya sa kalidad ng mga usapan ng AI.

#### Nangunguna ang mga nais ng customer kaysa sa mga rekomendasyon ng shop

May isa pang eksena kung saan nagtakda ako ng mahalagang hangganan.

Habang nagte-test, nakakita ako ng problema: lahat ng reservation ay ipinapasa sa pinakamurang plan. Nang ayusin ko ito, sa pagkakataong ito halos lahat ay naging Standard plan, at halos nadoble ang karaniwang kabuuang halaga. Halos natuwa ako, pero nang suriing mabuti, ang AI na gumaganap na customer ay palaging pinipindot lang ang unang pagpipilian. Kahit ang mga customer na nagsabing "okay na ang pinakamura" ay Standard ang inirerekomenda.

Dito, nagtakda ako ng prinsipyo. Ang malinaw na sinasabi ng customer bilang nais (ang pinakamura, isang budget, ang pangalan ng isang plan) ay palaging nangunguna kaysa sa rekomendasyon ng shop. Ang rekomendasyon ng shop ay para lang kapag wala pang sinabi ang customer.

Ang layunin ng shop na magpataas ng benta at ang tiwala ng customer ay maaaring magbanggaan sa iisang paraan ng pagrerekomenda. Kapag nawala ang tiwala, bumababa mismo ang mga pagbisita. Ang may-ari, hindi ang AI, ang nakaguhit ng hangganang ito.

Kalaunan, nang muli kong sanayin ang T-AI-MURO sa napakaraming tanong, ang pinakakaraniwang sanhi ng mga pagkakamali ay ang "pagre-react sa mga salita at paggawa ng nakatakdang galaw bago sagutin ang tanong." Sa sandaling marinig nito ang mga salitang tulad ng "bilang ng tao," "magkano," o "mag-isa," nilalaktawan nito ang tanong at pumupunta sa reservation flow o sa mga rekomendasyon. Sa usapin ng serbisyo, ito ay isang clerk na nagpupumilit magbenta nang hindi nakikinig sa customer. Sagutin muna ang tanong ng customer. Ang batayang ito ng pagtanggap ng bisita ang pinakamalaking hamon kahit sa AI.

Noong gabi ng October 6, 2026, lumitaw ang T-AI-MURO sa itaas ng reservation site bilang opisyal na entry point sa production. Dahil may mga customer na ayaw mag-book sa pamamagitan ng usapan, pinanatili ko sa tabi nito ang dating reservation form.

> Subukan ito: Buksan ang reservation site ng Tamuro (https://tamuroreservation.vercel.app/?src=b2-tl-{{FMT}}) at itanong sa T-AI-MURO ang "mag-isa ngayong gabi." Dadalhin kayo ng usapan hanggang sa availability at mga presyo ngayong araw.

【Larawan 1-4】Ang conversation screen ng T-AI-MURO. Umuusad ang usapan sa pag-tap lang ng mga pagpipilian *(Nasa wikang Hapon ang screen.)*

【Larawan 1-10】Naiipon sa admin screen ang mga tanong na hindi nito nasagot (synthetic data) *(Nasa wikang Hapon ang screen.)*

### 1-9 At Pagkatapos, Mula sa AI ng Customer

Dahil binuo ang T-AI-MURO, nagkaroon ang reservation site ng Tamuro ng kakayahang "sagutin ang mga tanong tungkol sa shop sa usapan, ipakita ang mga presyo at bukas na slot, at gabayan ang mga tao hanggang sa reservation."

Ang sumunod kong naisip ay gawing posible ang parehong bagay mula sa sariling AI ng mga customer.

Makakausap lang ng T-AI-MURO ang mga taong pumupunta sa reservation site ng Tamuro. Pero maraming tao ang unang kumokonsulta sa AI na ginagamit nila araw-araw. Kung hindi kilala ng AI na iyon ang Tamuro, hindi man lang makakasama ang Tamuro sa listahan ng mga kandidato. Sa halip na hintaying pumunta ang mga customer sa site ng Tamuro, ang panatilihing nakabukas ang bintana ng Tamuro sa panig ng AI ng customer. Iyon ang MCP server.

Sa totoo lang, nag-alinlangan ako noong una sa pagbuo nito. Sa puntong ito, kakaunti ang nagbu-book ng restaurant mula sa sarili nilang AI. Dahil sa tantiya kong hindi ako makakaasa ng direktang pagtaas ng mga reservation, minsan kong ibinaba ang prayoridad nito at ipinagpaliban.

Ipinasya kong buuin pa rin ito dahil naisip kong usapin na lang ng panahon ang pagbabago sa entry point ng mga customer. Gaya ng isinulat ko sa simula, noong August 2026, naging posible nang mag-reserve mula sa ChatGPT sa pamamagitan ng isang malaking reservation service. Maaga o huli, magiging normal na ang pagpapahanap sa AI ng restaurant. Kapag nangyari iyon, mawawala sa paningin ng AI ang mga maliliit na shop na hindi nakalista sa malalaking serbisyo. Kaya buksan ang bintana bago magbago ang entry point.

Naging napakalimitado ang saklaw ng ipinasya ko para sa unang bersiyon. Kailangan lang nitong gawin ang kapareho ng conversation window sa reservation site (T-AI-MURO). Ang kaya lang nitong gawin ay basahin ang impormasyon ng shop, mga bukas na slot, at mga presyo, at ibigay ang URL ng reservation page kung saan nakalagay na ang mga kondisyon. Ang pagkumpirma ng reservation ay ginagawa mismo ng customer sa page ng Tamuro. Hindi kumukumpirma ng reservation nang mag-isa ang AI ng customer. Tao ang gumagawa ng huling pindot.

Bumalik tayo sa panimulang eksena.

Sa isang Biyernes ng gabi, tinatanong ng isang customer ang sarili niyang AI, "May lugar ba sa Higashi-Nakano kung saan puwede akong uminom mag-isa ngayong gabi?" Tinatanong ng AI ang bintana ng Tamuro. Ibinabalik ng reservation system ng Tamuro ang mga bukas na slot ngayong gabi, kasama ang plan at presyong bagay sa nag-iisang customer. Sinasabi ito ng AI sa customer, at iniaalok ang isang reservation page ng Tamuro kung saan nakalagay na ang petsa, oras, at bilang ng tao.

Sinusuportahan ng lahat ng isinulat ko sa kabanatang ito ang seryeng ito ng mga hakbang. Ang discount system na binuo kasabay ng pagtaas ng presyo. Ang system na nag-aalaga ng mga suki. Ang data na nagpakitang karamihan ng reservation ay ginagawa sa mismong araw. Ang kaalaman tungkol sa shop na lumago sa pagsagot ng 11 tanong nang tig-iisang linya. Ang prinsipyo ng pagbibigay-priyoridad sa nais ng customer kaysa sa rekomendasyon ng shop.

Ang shop na nabu-book sa pamamagitan ng AI ay hindi nabuo sa magdamag. Bunga ito ng pinagpatong-patong na maliliit na system na idinagdag nang isa-isa, sinubukan, itinapon, at inayos.

> Subukan ito: Irehistro ang MCP server ng Tamuro (https://tamuroreservation.vercel.app/api/mcp) sa sarili ninyong AI at itanong, "May bakante ba ang Tamuro ngayong gabi?" Nakasulat sa Pangwakas kung paano magrehistro.

### 1-10 Ang Aming Binuo, at Kung Ano ang Gumana

Sa kabanatang ito, napag-usapan ko ang pagbuo ng maraming system. Pero magkaiba ang "nagawa naming buuin" at ang "nagbago ang negosyo." Sa dulo ng kabanata, paghihiwalayin ko ang dalawa.

Ang mga bagay na nakumpirma na gamit ang mga numero. Na 88.1% ng mga reservation ay para sa mismong araw. Na tumaas ang pass rate ng conversation window mula 9 hanggang 24 sa pagdaragdag lang ng 11 katotohanan tungkol sa shop. Na tumaas ang pass rate ng paggabay sa presyo at plan mula 29.4% hanggang 42.7% pagkatapos ng mga pag-aayos. Mga katotohanan ang mga ito na nasa talaan.

Ang mga bagay na pakiramdam ay gumagana, pero hindi ko mapatunayan ang sanhi. Na mas maraming customer ang dumarating nang grupo gamit ang group discount. Na pinipili ang mga planong "Hajimemashite" (Unang Pagbisita) at "Okaeri" (Pagbabalik). Na naging bahagi na ng usapan sa counter ang paksa ng confirmation email. Nararamdaman ko ito sa floor, pero hindi ko masasabing "hindi sila darating kung wala ang system na iyon."

Ang mga bagay na nabuo na, pero hindi ko pa alam ang epekto. Ilan pang advance reservation ang madadala ng early-booking discount. Ilang reservation ang talagang papasok mula sa MCP. Nagsimula pa lang akong sumukat gamit ang lingguhang ulat, at darating ang mga numero sa kalaunan.

Tingnan nang hiwalay ang pagkamangha sa "ganito karami ang nagawa namin gamit ang AI" at ang resulta ng "paano nito binago ang negosyo." Kung hindi paghihiwalayin ang dalawang ito, ang pagbuo mismo ang nagiging layunin. Halos mahulog ako rito minsan (gaya ng isinulat ko sa 1-7).

Ang kuwento ng nasa likod ng reservation system na ito, ang teknolohiya, ay magpapatuloy sa Kabanata 2. Kung hindi kayo interesado sa teknolohiya, lumaktaw sa Kabanata 3. Doon ko ikukuwento kung paano ibinibigay din sa ibang shop ang mga maliliit na tool na nabuo kasabay ng reservation system na ito.

## Kabanata 2: Teknolohiya - Sa Likod ng Reservation System

Mga pangunahing punto ng kabanatang ito

- Ang kalidad ng mga usapan ng AI ay mas napagpasyahan ng "mga katotohanan tungkol sa shop na iniaabot natin" at ng "kung ino-override ba ng isang program ang mga sagot ng AI nang mag-isa" kaysa sa talino ng AI
- Ang reservation system na binuo ko nang basta-basta (vibe) ay may butas pa ring nagpapahintulot na mabasa mula sa labas ang personal na impormasyon ng mga customer, at zero ang mga automated test. Ipinasuri ko ito sa AI para mahanap ang mga ito, at ipinaayos ko rin sa AI
- Mula sa pagninilay na iyon, binago ko ang paraan ng paggawa ko: tukuyin nang detalyado ang mga requirement bago bumuo, at ibigay sa AI ang mismong specification para ipatupad

(Maraming teknikal na termino ang kabanatang ito. Kung hindi kayo interesado sa teknolohiya, puwede kayong lumaktaw sa Kabanata 3 at magkakaugnay pa rin ang kuwento.)

### 2-1 Paano Gumagana ang MCP Server

Ang MCP (Model Context Protocol) ay isang karaniwang hanay ng mga kumbensiyon para magamit ng AI ang mga panlabas na tool at data. Iminungkahi ng Anthropic, sinusuportahan na ito ngayon ng maraming AI, kabilang ang ChatGPT at Claude.

Kung ihahambing, ang MCP ay pamantayan ng saksakan ng kuryente, para sa AI. Dahil nakatakda ang hugis ng saksakan, gumagana ang appliance ng alinmang gumawa kapag isinaksak. Sa parehong paraan, kung bubuo kayo ng bintana na tugma sa hugis ng MCP, magagamit ng alinmang AI ang bintanang iyon.

Sinasabi ng isang MCP server sa AI kung "ano ang magagawa ninyo sa pamamagitan ng bintanang ito." Halimbawa, ang MCP server ng Tamuro ay may mga tool na tulad ng mga sumusunod.

- Basahin ang impormasyon ng shop (oras ng operasyon, bilang ng upuan, mga patakaran ng shop, kapaligiran)
- Basahin ang mga plan at presyo (ang resulta ng pagkalkula ng mga discount ayon sa bilang ng tao at petsa)
- Basahin ang mga bukas na slot (ang mga oras na puwedeng i-book sa isang tinukoy na araw)
- Gumawa ng URL ng reservation page kung saan nakalagay na ang mga kondisyon

Kapag tinanong ng isang customer ang sarili niyang AI, "May bakante ba ang Tamuro ngayong gabi?", kumokonekta ang AI sa MCP server ng Tamuro, pinipili ang "basahin ang mga bukas na slot" mula sa mga naka-hanay na tool, at tinatawag ito. Ibinabalik ng server ng Tamuro ang resulta, at ipinapahayag ito ng AI sa customer gamit ang natural na pangungusap.

Ang mahalaga, hindi basta-basta nagkukumpirma ng mga reservation ang AI nang walang pahintulot. Sa unang bersiyon, sadya kong iniwan sa labas ng mga tool ang pagkumpirma ng reservation. Ang kaya lang gawin ng AI ay magbasa, at gabayan ang mga tao sa isang reservation page kung saan nakalagay na ang mga kondisyon. Ang customer mismo ang pipindot ng confirm button sa page ng Tamuro. Ang panganib na makagawa ang AI ng napakaraming maling reservation o prank na reservation ay iniiwasan na ng disenyo mula pa sa simula.

Ginagamit sa pagkalkula ng presyo ang parehong mekanismo ng pagkalkula ng reservation site. Ang mga presyong ipinapakita sa reservation form, sa conversation window, at sa pamamagitan ng MCP ay pawang lumalabas sa iisang program. Ito ang isa pang kahulugan ng gawaing isusulat ko sa ibang bahagi, ang "pagsasama-sama ng pagkalkula ng discount sa iisang lugar."

【Larawan 2-1】Mula sa AI ng customer hanggang sa reservation page ng Tamuro. Ang customer ang pipindot ng confirm button

### 2-2 Paano Gumagana ang Conversation Window na "T-AI-MURO"

#### Mga presyo mula sa program, mga salita mula sa AI

Hinahati ng T-AI-MURO ang mga tungkulin sa dalawa. Ang program ang gumagawa ng mga presyo at bukas na slot gamit ang mga nakatakdang kalkulasyon, at ang AI ang naglalagay ng mga ito sa salita para sa customer.

Magaling ang AI sa paggawa ng teksto, pero walang garantiya na tama ang kalkulasyon nito sa bawat pagkakataon. Kung paano nagpapatung-patong ang mga discount, ang mga hakbang ayon sa bilang ng tao, ang bilang ng araw para sa early-booking discount, kung puwede bang isama sa happy hour. Kung ipauubaya ninyo sa AI ang lahat ng patakarang ito, tiyak na magkakamali ito sa kung saan. At ang pagkakamali sa presyo ang pinakamalaking sumisira sa tiwala ng customer.

Kaya ang mga bahaging hindi dapat magkamali ay napupunta sa program, at ang mga bahaging nagpaparating nang malumanay ay napupunta sa AI. Ang paghahating ito ang unang prinsipyo sa pagbuo ng conversation window.

#### Para sa maliit na shop, hindi ninyo kailangan ang RAG

Para masagot ng AI ang tungkol sa shop, kailangan ninyong iabot sa AI ang kaalaman ng shop. Isang karaniwang ginagamit na paraan ang RAG (retrieval-augmented generation). Hinahati-hati ninyo ang kaalaman sa maliliit na bahagi at iniimbak, at sa bawat pagdating ng tanong, hinahanap ninyo ang mga bahaging mukhang may kaugnayan at iniaabot sa AI. Kapag napakalawak ng kaalaman, kailangang-kailangan ang paraang ito.

Pero hindi ganoon kalaki ang kaalaman ng Tamuro. Ang kasaysayan ng shop, ang pagkain, ang mga patakaran, ang kapaligiran, ang pananaw ng may-ari. Kapag pinagsama-sama, madali itong magkasya sa kayang basahin ng AI nang minsanan.

Kaya sa Tamuro, pinili kong ipabasa sa AI ang buong teksto ng kaalaman ng shop sa bawat pagkakataon. Hindi na kailangang bumuo ng mekanismo ng paghahanap na hinihingi ng RAG, at walang nalalampasan sa paghahanap. Sa simula, plano kong gamitin muli ang isang mekanismo ng RAG, pero sa gitna ng proseso ay lumipat ako sa full-text na paraan.

Mas malaki ang gastos sa bayad sa AI kapag pinabasa ang buong teksto sa bawat pagkakataon. Kaya gumagamit ako ng mekanismong ginagamit muli ang parehong teksto para ibaba ang gastos sa input (prompt caching: sa halip na ipabasang muli sa AI ang parehong paunang bahagi sa bawat pagkakataon, naaalala nito ang nabasa na nito). Sapat nang gumamit ng RAG kapag lumaki na ang kaalaman.

#### Isang program na basta-basta na lang nag-o-override ng mga sagot

Sa Kabanata 1, isinulat kong 9 lang sa 36 ang pumasa sa unang test. Bahagi ng sanhi ay nasa kung paano binuo ang program.

Nang imbestigahan ko, nakita ko ang isang mekanismong naiwan kung saan hinuhusgahan ng program ang sagot na ginawa ng AI batay sa mga keyword at pinapalitan ito ng nakatakdang pangungusap. Kapag lumitaw ang mga salitang tulad ng "reservation" o "ngayon," itinatapon nito ang sagot ng AI at pinapalitan ng listahan ng mga bukas na slot. Kahit tama ang sagot ng AI, hindi ito umabot sa customer.

Higit pa rito, nalaman kong ang pangunahing bahagi ng kaalaman ng shop (33 seksiyon) ay hindi kasama sa mga instruksiyon sa AI. Sumasagot ang AI nang hindi alam ang tungkol sa shop.

Ang kalidad ng mga usapan ng AI ay mas napagpasyahan ng mga katotohanan tungkol sa shop na iniabot at ng kung ino-override ba ng isang program ang mga sagot ng AI nang mag-isa, kaysa sa sariling talino ng AI.

#### Punan ang mga inaasahang Q&A sa pamamagitan ng pagbibilang

Dinagdagan ko ang mga test scenario mula sa unang 36 hanggang 110, at pagkatapos ay hanggang 355. Pero kung nagdaragdag ang mga tao ng mga scenario batay lang sa biglaang naisip, walang paraan para malaman kung may kulang. Sa tanong na "Komprehensibo ba ito?", ang tapat na sagot ay "Hindi."

Kaya sa halip na palawakin ang saklaw sa pamamagitan ng imahinasyon, ginawa kong usapin ng pagbibilang ng makina ang mga lugar na hindi pa nadadaanan, at pagpupuno sa mga ito. Para sa apat na bagay: ang 33 seksiyon ng kaalaman ng shop, ang mga paglipat sa pagitan ng mga pagpipilian, ang mga hakbang ng mga discount, at ang mga kombinasyon ng mga time slot at araw ng linggo. Binibilang ko kung ilang beses nadaanan ang bawat isa sa pagte-test, at awtomatiko akong nagdaragdag ng mga scenario kung saan zero ang bilang.

Gumamit din ako ng paraang pagtatambal ng anim na axis (bilang ng tao, layunin, paraan ng pag-inom, petsa at oras, pagkakasabi, menu) at paggawa ng mga scenario para madaanan nang kahit isang beses ang bawat pares ng dalawang kombinasyon.

Nakakita rin ako ng blind spot kaugnay ng oras. Ang "ngayon" at "mula ngayon" ay natutukoy ng aktuwal na oras ng pagtakbo ng test, kaya iba ang resulta kapag pinatakbo nang tanghali at nang gabi. Kaya itinakda ko ang orasan sa panahon ng pagte-test at pinatakbo ito sa limang punto ng oras: bago magbukas, sa oras ng operasyon, bago magsara, sa regular na araw ng pahinga, at sa holiday.

Bahagyang nag-iiba sa bawat pagkakataon ang mga sagot ng AI, kahit sa parehong tanong. Para sa mga scenario na direktang nakatali sa benta, itinakda ko ang kondisyong dapat silang pumasa sa lahat ng tatlong beses kapag pinatakbo nang tatlong beses.

#### Kapag may lumabas na masamang numero, hinalaan muna ang test

Sa test na nagpatakbo ng 355 scenario sa 5 punto ng oras, sa 1,775 usapan, 28.5% ang pumasa.

Sa halip na agad magsimulang mag-ayos, una kong inihiwalay: "Talaga bang kahinaan ng T-AI-MURO ang numerong ito, o mali ang test?" Kung mag-aayos kayo habang mali ang test, aabot kayo sa "pag-aayos" kahit ng mga tamang sagot.

| Sanhi ng error | Bilang |
| --- | --- |
| Inaagaw ng nakatakdang pangungusap ang tanong | 276 |
| Hindi sinasagot ang tanong, lumilipat sa reservation flow o sa mga rekomendasyon | 266 |
| Pagkabigo ng test environment (hindi nakagawa ng sagot ang T-AI-MURO dahil sa cost cap) | 211 |
| Mga error sa petsa, araw ng linggo, holiday, araw ng pahinga | 142 |
| Pag-imbento o pagpapatibay ng mga katotohanang wala sa shop, pangakong ipapasa ang mga mensahe | 119 |

Iisa ang ugat ng nangungunang dalawa: "pagre-react sa mga salita at paggawa ng nakatakdang galaw bago sagutin ang tanong ng customer." Ang 211 sa ikatlong puwesto ay hindi mga error ng T-AI-MURO. Naabot ang cost cap sa gitna ng test, at hindi lang talaga nakagawa ng mga sagot ang T-AI-MURO. Kung ibubukod ang mga ito, 32.4% ang pass rate.

Maaari ring magkamali ang AI na naghuhusga. Nang pumili ako ng 20 kaso at suriin, 2 ay mga error sa panig ng test. Sa isa sa mga iyon, hindi alam ng judge na "may member registration ang reservation site na ito." Wala ring alam ang judge na lampas sa mga materyal na ibinigay dito. Ang katumpakan ng test ay napagpapasyahan ng pagkakumpleto ng mga patakaran ng shop na iniabot sa judge.

Sa retest pagkatapos ng mga pag-aayos, tumaas ang pass rate ng paggabay sa presyo at plan mula 29.4% hanggang 42.7%. Hindi ko pa napapatakbo ang huling test na nagpapadaan muli sa bawat kaso. Para mapanatiling mababa ang gastos, ipinasya kong minsan lang patatakbuhin ang all-cases test, bago ilagay sa production ang isang malaking pagbabago. Itinataas pa rin ang pass rate habang isinusulat ko ang librong ito.

#### Pinahinto ng test ang production

May gastos ang mga AI test. Ang unang test na may 36 na scenario ay nagkahalaga ng humigit-kumulang ¥426 (humigit-kumulang $2.8). Karamihan nito ay napunta sa "thinking effort" ng AI na gumaganap na customer, at nang patayin ko iyon, 3 scenario ang nagkahalaga ng humigit-kumulang ¥6 (humigit-kumulang $0.04).

Pero isang araw, sa gitna ng isang test, naubos ang balanse ng paggamit ng AI at huminto ang lahat. Sa iisang araw, nakagamit ako ng humigit-kumulang 35 milyong token (ang yunit ng tekstong binabasa at isinusulat ng AI). Ang sanhi ay ang paulit-ulit na pagpapatakbo ng test na may 221 scenario, at ang pagpapatakbo ng mga scenario na direktang nakatali sa benta nang apat na beses bawat isa.

Ang nakakatakot ay iisang wallet ang ginamit ng test at ng production. Kapag naubos ang balanse, humihinto pati ang production conversation window. Sa ibang araw, sa pagkakataong ito ay naabot ko ang buwanang cap na itinakda ko mismo, at sabay na huminto ang production conversation window at ang AI na gumagawa ng mga paksa ng usapan para sa mga customer sa loob ng shop.

Ang tunay na panganib ng budget sa pagte-test ay hindi ang bill, kundi ang katotohanang iisang wallet ang pinagsasaluhan ng test at ng production.

Mula noon ay nagbago ang mga patakaran. Gawin muna ang mga check na walang gastos (mga test ng program at awtomatikong pagsusuri ng screen). Limitahan ang mga test na tumatawag sa AI sa mga may kaugnayan sa inayos. Patakbuhin ang all-cases test nang minsan lang, bago pumunta sa production. Isulat sa mga instruksiyon ang tinatayang gastos at isang cap, at huminto kung mukhang aabot dito. Para mapanatili ang pondo para sa production, itigil ang pagte-test kapag malapit na sa cap ang paggamit ng buong organisasyon.

May aral din sa kung paano lumolobo ang mga gastos. Minsan, umabot sa 2.6 beses ng tantiya ang gastos ng judging AI. Ang sanhi ay hindi nagagamit muli ang mahabang paunang bahagi na iniaabot sa judge sa bawat pagkakataon (ang kaalaman at mga patakaran ng shop), kaya may singil sa muling pagsulat sa bawat pagkakataon. Nang ayusin ko ito para isulat nang minsan ang paunang bahagi at gamitin muli, bumaba sa humigit-kumulang isang-katlo ang gastos kada usapan. Hindi sa dami ng pagtawag sa AI lumolobo ang gastos nito, kundi sa dami ng muling pagsulat ng parehong paunang bahagi.

Ang parehong 221-scenario na full test ay bumaba mula sa humigit-kumulang ¥1,040 (humigit-kumulang $6.9) tungong humigit-kumulang ¥400 (humigit-kumulang $2.7) sa pamamagitan ng paulit-ulit na pagpapahusay. Pinalitan ko ang AI na gumaganap na customer ng nakatakdang script, at hinati ko ang impormasyong iniaabot sa AI sa isang "core na ipinapadala sa bawat pagkakataon" at mga "seksiyong binabasa lang kapag kailangan."

Dahil sa mga limitasyon ng budget, nagbago ang disenyo tungo sa pagpaparami ng mga bahaging masusuri nang walang gastos, ibig sabihin, ang mga bahaging pinagpapasyahan ng program. Bunga nito, tumaas din ang katumpakan. Binabago ng pera ang disenyo.

【Larawan 2-2】Mga resulta ng mga AI test. Ang pass rate at breakdown ng mga sanhi ng error

### 2-3 Pagpapasuri sa AI ng Aking Binuo

#### Nababasa mula sa labas ang mga pangalan ng customer

Noong August 2026, habang sinusuri ko kung paano gumagana ang reservation system, may natuklasan akong nagpatayo ng balahibo ko.

Nababasa ng sinuman mula sa labas ang data ng mga reservation ng mga customer. Mga pangalan, numero ng telepono, email address, ang field ng mga kahilingan. Lahat ng inilagay sa isang reservation ay makukuha nang buo, nang walang authentication.

May sasabihin akong dapat sabihin nang tapat. Totoong nababasa ang data mula sa labas. Noong panahong iyon, napakakaunti ng traffic ng reservation site, at naniniwala akong malabong may talagang nagbasa nito. Pero wala akong talaan na makapagpapatunay na hindi ito nabasa. Magkaiba ang "puwede itong makuha" at ang "talagang nakuha ito," pero ang una pa lang ay malubhang pagkukulang na para sa isang shop.

Nang hanapin ko ang sanhi, nauwi ito sa kung paano binuo ang reservation form. Para makalkula ang mga bukas na upuan, direktang nilo-load ng form mula sa screen ang 35 araw ng data ng reservation. Kung nababasa ito ng screen, nababasa rin ang parehong data ng sinumang nakakaalam kung paano binubuo ang mga ganoong screen. Bunga ito ng unang pundasyong binuo nang basta-basta, na nakarating sa layuning "ipakita ang mga bukas na upuan" sa pinakamaikling daan.

Nalaman ko rin na pampubliko ang email address para sa pag-abiso sa administrator ng shop, at na kahit sino ay nakakasulat sa lugar kung saan iniimbak ang mga salin, na nangangahulugang maaaring sirain ang data o palobohin ang mga gastos.

Mahalaga ang pagkakasunod-sunod ng pag-aayos. Kung bigla ko na lang ipagbabawal ang pagbabasa, hindi na maipapakita ng reservation form ang mga bukas na upuan at hihinto itong gumana. Kaya una, inilipat ko ang pagkalkula ng bukas na upuan sa isang endpoint sa panig ng server. Sumunod, binago ko ang reservation-complete screen para kunin din nito mula sa server ang impormasyong kailangan lang nito. Sa huli, isinara ko ang pagbabasa mula sa labas. Ginawa ko ang pag-aayos sa apat na yugto sa ganitong pagkakasunod-sunod at inilapat sa production.

Pagkatapos ng pag-aayos, gumamit ako ng makina para tiyaking talagang sarado na. Naghanda ako ng test na sumusubok magbasa ng data ng reservation nang walang authentication, at awtomatiko ko itong pinatatakbo pagkatapos ng bawat pagbabago para tiyaking palaging tinatanggihan. Hindi ako nag-ayos nang minsan at nagpahayag na tapos na. Inayos ko ito para may check na nagbabantay na hindi na ito muling bumukas.

#### Naiwan sa development history ang tunay na data ng mga customer

Pagkatapos, ipinasuri ko sa AI ang buong repository (ang imbakan ng program), at may lumitaw na mas malubhang problema.

Sa panahon ng development, may file na naglalaman ng tunay na data ng mga customer (mga email address at numero ng telepono mula sa 55 reservation) na naipadala sa repository, at kasama pa rin sa kasaysayan ng mga pagbabago ng program. Pribado ang repository, pero dahil nananatili ito sa talaan, hindi ko ito maaaring pabayaan.

Inalis ko ang file mula sa buong kasaysayan ng mga pagbabago, isinulat kong muli ang kasaysayan, at muling inimbak ito. Gayunpaman, maaaring nananatili pa rin ang mga lumang talaan bago ang pagsulat muli sa panig ng GitHub, na nagho-host ng repository. Kaya humiling ako sa GitHub support na burahin ang mga ito, at kinumpirma kong nagawa na.

Nakita rin ng audit ang iba pang mga problema: magagamit nang walang authentication ang translation endpoint, maaaring atakihin ng brute force ang login ng administrator, at may panahong, kung muling pinagana ang pagbabayad, makukumpirma ang isang reservation habang hindi pa bayad. Inayos ko ang mga ito isa-isa, simula sa pinakamalubha.

#### Zero ang mga automated test

May isa pang katotohanang inihayag ng audit. Walang kahit isang automated test ang reservation system.

Ang mga automated test ay mekanismo kung saan awtomatikong sinusuri ng makina kung tama ang paggana ng program. Kung walang mga test, kapag may inayos kayo, wala kayong paraan para suriin kung may ibang nasira. Sa bawat pagdaragdag ng feature, may tahimik na nasisira sa kung saan. Iyon mismo ang kalagayan noong panahong gumagawa ako sa hinuha.

Kaya muli kong binuo ang pundasyon ng pagte-test mula sa zero. Naglagay ako ng system (CI) na awtomatikong nagpapatakbo ng apat na check pagkatapos ng bawat pagbabago: type checking, style checking, mga test, at ang build. Ang mahahalagang desisyon tulad ng pagkalkula ng presyo, pag-validate ng reservation, pag-uugnay ng mga member, at pag-isyu ng mga coupon ay inihiwalay sa mga program ng screen para ma-verify ang mga ito nang hiwalay. Sinusuri rin sa test environment na ginagaya ang tunay na database ang mga patakaran sa pagbabasa at pagsusulat ng database. Nagsimula sa 275 ang mga unit test at kalaunan ay lumampas sa 500.

May isang kondisyon na palagi kong ipinapataw sa mga test: "sirain ito, at tiyaking bumabagsak." Kahit maging green (pumasa) ang isang test, hindi ninyo alam kung talagang nakakahuli ng problema ang test na iyon. Pagkatapos ko lang sadyang sirain ang program at kumpirmahing nagiging red (bumabagsak) ang test saka ko pinagkakatiwalaan ang test. Iyon ay dahil may mga test na isinulat ng AI na walang sinusuri.

#### Walong butas sa reservation form

Pagkatapos maitatag ang pundasyon ng pagte-test, ipinasuri kong muli sa AI ang buong daloy ng reservation. Nakahanap ito ng walong problemang may tunay na pinsala.

Ang pinakamalubha ay ang paulit-ulit na pagpindot sa submit button na lumilikha ng double reservation. Aktuwal itong nangyari sa production. Inayos ko ito gamit ang mekanismong pinoproseso nang minsan lang ang parehong aksiyon kahit dalawang beses itong dumating (idempotency). Ang iba pang mga problema ay ang mga ito: hindi makumpirma ang isang reservation kung may natirang impormasyon ng binurang menu item; may puwang sa full-house check na nag-iwan ng lugar para lumampas sa kapasidad; walang nakapansin nang mabigo ang pagpapadala ng confirmation email; hindi vina-validate sa panig ng server ang input; lumilitaw sa screen ang panloob na mensahe ng system kapag may error; napakaliit ng teksto sa mga input field kaya kusang nag-zoom in ang screen sa iPhone; at hindi gumagana ang autofill para sa input.

Para sa mga pagkabigo ng email, ginawa kong posibleng matukoy ang mga ito sa admin screen at ipadala muli. Sa panahon ng imbestigasyong iyon, nalaman ko ring ang audit log na nagtatala ng mga pagkumpirma ng reservation ay nabibigo sa bawat pagkakataon, mula pa bago ang pag-aayos, at wala itong naitalang anuman.

Inayos ko ang mga ito nang isa-isa at inilapat sa production.

#### Huwag kailanman laktawan ang pag-verify ng code na isinulat ng AI

Ang natutuhan ko sa karanasang ito ay na dahil mismo sa isinulat ng AI ang isang program, hindi dapat laktawan ang pag-verify.

Mabilis na binibigyang-hugis ng AI ang sinabi rito. Pero ang konsiderasyon sa mga bagay na hindi sinabi rito, tulad ng "gawing hindi mabasa mula sa labas" o "ituring na isa ang dobleng pag-submit," ay hindi pumapasok maliban kung ito ay ipag-uutos. At ang mga butas na tulad nito ay tahimik na nakatago sa loob ng mga program na mukhang gumagana.

Hindi kailangang basahin ng mga tao ang lahat ng code. Ang kawastuhan ng program ay binabantayan ng mga machine check at ng audit mula sa ibang AI. Ang pagiging angkop ng resulta sa layunin ng shop ay binabantayan ng may-ari. Hindi ninyo kailangang basahin ito, pero hindi dapat laktawan ang pag-verify. Iyon ang pinaniniwalaan kong ibig sabihin ng pagbuo gamit ang agent-type na AI.

【Larawan 2-3】Ang mga patakaran noong nababasa ito mula sa labas, at ang mga patakaran pagkatapos ng pag-aayos (excerpt) *(Nasa wikang Hapon ang screen.)*

### 2-4 Ang Paggawa nang Basta-basta ay Nagpaparami ng mga Salungatan

Habang dumarami ang idinadagdag kong feature, dumarami rin ang mga bahaging sumasalungat sa dati kong ipinasya.

Ang tipikal na kaso ay ang pagkalkula ng discount. Sa reservation form, sa confirmation screen, sa email, at sa admin screen, hiwa-hiwalay na isinulat sa bawat lugar ang pagkalkula ng discount. Kung binago ko ang isang patakaran ng discount sa isang lugar, patuloy na kumakalkula ang ibang lugar gamit ang lumang patakaran. Para sa parehong reservation, maaaring magpakita ng magkaibang halaga ang screen at ang email.

Kalaunan, tinipon ko ang pagkalkula ng presyo sa iisang file. Doon na gumagawa ng mga presyo ang reservation form, ang chat window, at ang MCP server.

Nagbago rin sa gitna ang mga patakaran sa pagpapatung-patong ng mga discount. Gaya ng isinulat ko sa Kabanata 1, ang happy hour ay una nang puwedeng isama sa iba pang discount, pero nalaman kong hindi ito kikita at ginawa kong hindi puwedeng isama. Sa bawat pagbabago ng patakaran, kailangang tandaan ng tao kung saan mag-aayos. Iyon ang kahinaan ng system na binuo sa hinuha.

Nagkaroon din ng hindi pagkakatugma sa pagitan ng test environment at ng production. Habang nagte-test ng chat window, isang tanong, "Hindi ba may 10% off na ganoon?", ang nagpakitang lumihis na ang mga patakaran ng discount sa test environment mula sa production. Kung magkaiba ang mga halaga sa test environment at sa production, makakapasa kayo sa mga test at mali pa rin sa production. Ang ipinasya ko noon ay ang prinsipyong "tama ang production." Mula noon, bago ang bawat pagpapatakbo ng test, kinokopya ko ang mga setting ng production sa test environment at kinukumpirma kong zero ang hindi pagkakatugma bago magpatakbo.

Binubuo ng AI ang sinabi rito. Pero hindi nito napapansin ang mga salungatan sa mga naunang desisyon. Ang pumipigil sa mga salungatan ay hindi ang AI. Ito ay ang pagpapasya sa mga bagay nang maaga.

### 2-5 Muling Pag-aaral ng Requirements Definition

Pagkatapos magnilay sa reservation system na binuo ko nang basta-basta (vibe), muli kong pinag-aralan ang requirements definition. Ang requirements definition ay nangangahulugang pagpapasya, bago bumuo, kung ano ang bubuuin, kung ano ang hindi bubuuin, at kung sino ang gagamit at paano, at pagsusulat nito sa isang dokumento.

Bagay itong ginagawa ko nang likas noong systems engineer pa ako. Pero nang makabuo na ako gamit ang AI, nalampasan ko ito nang hindi namamalayan. Sabihin lang ang isang ideya at may lalabas na gumaganang bagay sa loob ng ilang minuto. Sa bilis na iyon, pinutol ko ang pagsisikap ng pagpapasya.

Tatlong yugto ang paraan ko ng paggawa ngayon.

1. Una, pagpasyahan nang detalyado ang mga requirement. Ano ang bubuuin, ano ang hindi bubuuin, sino ang gagamit. Ang gawi ng bawat screen. Kung paano hahawakan ang mga exception (mga error, dobleng pindot, pag-expire). Ang mga patakarang madaling mauwi sa pagsasalungatan sa kalaunan, tulad ng mga presyo at discount, ay mas detalyado kong pinagpapasyahan. Ginagawa ko rin ang gawaing ito sa pakikipag-usap sa chat AI. Ipinahahanap ko sa AI ang mga butas at salungatan nang maaga, at ang may-ari ang nagpapasya.
2. Isulat ang napagpasyahan bilang isang "requirements document." Hindi mga salitang binigkas o mga instruksiyong biglaan, kundi tinipon sa iisang dokumento. Ito ang nagiging nag-iisang pamantayan para suriin sa kalaunan kung ano ang tama.
3. Iabot sa AI ang buong dokumento at ipaimplement. Ibinibigay ko ang buong dokumento sa AI na sumusulat ng program (Claude Code), kasama ang mga kondisyon para pumasa (pumapasa ang lahat ng test, check sa test environment bago ang production, at iba pa). Binubuo ng AI nang mag-isa hanggang matugunan ang mga kondisyon, at sinusuri rin nito nang mag-isa. Tumitingin lang ang may-ari kapag huminto ito sa gitna at sa huling check.

Halimbawa, ang requirements document para sa chat window na "T-AI-MURO" ay muling isinulat mula sa unang bersiyon hanggang sa ikatlo. Sa ikalawang bersiyon, ipinasya kong "huwag hayaang kumalkula ng mga presyo ang AI," "ilagay sa iisang chat window ang kaalaman ng shop at ang pagkalkula ng presyo," at "panatilihin din ang form, para sa mga taong ayaw mag-reserve sa chat." Sa ikatlong bersiyon, ipinasya ko "kung saan itatago ang master copy ng kaalaman ng shop," "ang chat window na ito lang ang magpapakita ng mga bukas na slot," "gawing tanong na may apat na pagpipilian ang unang palitan," at "huwag mag-save ng mga log ng usapan; mag-imbak lang ng mga tanong na hindi nasagot." Dahil nananatili ang mga desisyon sa isang dokumento, matutunton ko sa kalaunan kung bakit ganito ang mga bagay.

Sa paraang ito ng paggawa, kahit magdagdag ako ng mga feature, agad kong mapapansin ang mga salungatan sa pamamagitan ng pagsusuri laban sa dokumento. Sa panahon mismo na AI ang bumubuo, kailangan ang "kakayahang magpasya" bago bumuo. Iyon ang pinakamalaking aral na natutuhan ko mula sa reservation system.

Gumawa rin ako ng mekanismong inilalagay sa isang dokumento ang mismong pamamaraan at iniaabot sa AI, para maipatakbo nang pareho sa bawat pagkakataon ang paraang ito ng paggawa tuwing maglulunsad ako ng bagong produkto. Isusulat ko iyon sa Kabanata 4.

【Larawan 2-4】Talaan ng nilalaman ng requirements document ng T-AI-MURO (bersiyon 3) *(Nasa wikang Hapon ang screen.)*

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

At ang pagpapangalang ito ang naging simula. Kung may itim na notebook, puwedeng may mga notebook na may ibang kulay. Muli kong bubuuin ang mga mekanismong ginagamit ko araw-araw sa sarili kong shop sa mga anyong magagamit ng kahit anong shop, at ilalabas ko ang mga ito nang isa-isa bilang notebook. Iyan ang [Agenda series](https://bontallc.com/agenda?via=b2-tl-{{FMT}}).

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

### 3-6 Ang Debate Tungkol sa "Kamatayan ng SaaS"

Ang software na ginagamit ng mga tao sa internet kapalit ng buwanang bayad, gaya ng Agenda series, ay tinatawag na SaaS (Software as a Service). Accounting software, pamamahala ng oras at attendance, pamamahala ng reservation. Sa ngayon, maraming SaaS ang ginagamit sa pagpapatakbo ng mga restawran.

Tatapusin ba ng AI ang SaaS? Noong 2026, malakas na sumiklab ang debateng iyan.

Isa sa mga mitsa ang pahayag ni Satya Nadella, CEO ng Microsoft. Sa isang podcast noong Disyembre 2024, sinabi ni Nadella na guguho ang mga SaaS application sa panahon ng mga AI agent. Ang katwiran: kapag inako na ng mga AI agent ang bahagi ng gawaing pangnegosyo na nagpapasya, hindi na kakailanganin ang software na ginawa para patakbuhin ng mga tao sa pamamagitan ng mga screen.

Pagkatapos, noong Pebrero 2026, inanunsyo ng Anthropic ang Claude Cowork (isang AI tool na kusang gumagawa ng mga gawaing pangnegosyo), at malakas na ibinenta ang mga share ng mga kumpanya ng software sa Amerika. Sa Wall Street, tinawag na "SaaSpocalypse" ang pagbagsak. Ang kinatakutan ng mga investor ay kung ang mga AI agent na ang gagawa ng trabaho, guguho ang modelo ng SaaS na kumikita ng bayad kada tao (per-seat pricing).

May mga kontra-argumento rin. Sinabi ni Jensen Huang, CEO ng Nvidia, na hindi papalitan ng mga AI agent ang software kundi gagamitin nila ito sa halip na mga tao, at tinawag niyang sobrang reaksyon ang bentahan. Marami ring iba ang nakakakita na lalo pang lalakas ang SaaS na nag-iintegrate ng AI.

Mamamatay ba talaga ang SaaS? Heto ang palagay ko.

Ang mamamatay ay ang gitnang patong ng SaaS: ang uri na naniningil ng mataas na buwanang bayad kada tao at nagpapalagay na pinapatakbo ito ng mga tao sa pamamagitan ng mga screen. Kung AI na ang gagawa ng trabaho sa halip na mga tao, hindi na kailangan ng seat para sa bawat tao. Kung walang nagpapatakbo ng screen, hindi na kailangan ng masalimuot na screen.

Ang mananatili ay ang mga tool na mura at iisang bagay ang ginagawa nang maaasahan. At ang mga tool na madaling gamitin ng AI.

Ito mismo ang tatlong prinsipyo ng Agenda series. Awtomatikong tumatakbo ito, ipinauubaya ito sa sariling AI ng may-ari (hiram na lakas), at isang bagay lang ang ginagawa nito (iisang tungkulin). Ipinauubaya ng AgendaTurno sa sariling AI ng may-ari ang pagbuo ng schedule ng shift, na eksaktong anyong "AI ang gumagamit ng software" na inilalarawan ni Huang. Nagbubukas ng bintana ang reservation system ng Tamuro sa pamamagitan ng MCP para sa mga AI ng mga customer, at iisang ideya rin iyon.

Siyempre, maaaring mukhang may kontradiksyon dito. Nagsasalita ako tungkol sa kamatayan ng SaaS, pero SaaS din mismo ang Agenda series. Pero ang Agenda series ay hanay ng mga tool na binuo ng isang may-ari para sa sarili nitong shop at saka inilabas sa publiko sa mababang presyo. Hindi ito modelong naniningil ng mataas na buwanang bayad kada tao, at hindi nito ipinapalagay na nakadikit ang mga tao sa screen araw-araw. Binuo ito mula sa simula sa pagpapalagay na gagamitin ito ng AI.

#### Ang "Kamatayan ng SaaS" para sa mga Restawran

Maaaring parang kuwento tungkol sa mga investor at sa industriya ng IT ang debateng ito. Pero para sa mga restawran, mararanasan ang parehong bagay sa mas pamilyar na paraan.

Maraming independent na shop ang nagbabayad ng buwanang bayad sa mga gourmet site at reservation site, at bukod doon ay nagbabayad ng referral commission sa bawat reservation. Kapalit ng pagdadala ng mga customer, hawak ng site ang ugnayan sa customer, at hindi na bago na walang contact information ng customer ang shop. Kapag tumaas ang presyo, walang magagawa ang shop kundi sumunod, at kapag nagbago ang sistema ng ranking, nagbabago ang daloy ng mga customer.

Gaya ng isinulat ko sa Kabanata 1, noong 2026 nagsimula ang panahon kung saan may sariling AI ang mga customer na naghahanap ng mga shop. Kung lilipat sa AI ang pasukan, nagsisimulang mayanig ang buong kaayusan ng pagbabayad sa isang site ng buwanang bayad at komisyon para mailagay nang mataas sa listahan nito. Kung magbubukas ang isang shop ng sarili nitong bintana para sa AI, makararating sa kanila ang mga customer nang hindi dumadaan sa malalaking site. Nananatili sa kamay ng shop ang mga talaan ng reservation at ang ugnayan sa customer.

Kung isasalin sa wika ng isang independent na shop ang "kamatayan ng SaaS," ito ay "ang pagtatapos ng panahong nakakapasok kayo sa listahan dahil nagbayad kayo." Binuksan ng Tamuro ang bintana nito sa pamamagitan ng MCP, at pinananatili ang mga reservation at CRM nito sa sarili nitong mga espesipikasyon, bilang paghahanda para riyan.

Kung mamamatay ba ang SaaS, wala pang nakakaalam. Pero unti-unti nang lumilitaw ang hugis ng mga tool na mananatili sa panahon ng AI. Iyan ang palagay ko.

### 3-7 Monetization: Maliit, Marami, Mura

Binubuo ko ang Agenda series na may layuning mapatayo ito bilang negosyo. Ang layunin ay gawin itong ikalawang haligi ng kita, hiwalay sa restawran.

Maliit at mababa ang itinakda kong presyo. Nagsisimula sa ilang daang yen ang buwanang bayad. Ang Talaan ng Oras, halimbawa, ay ¥500 (humigit-kumulang $3.3) kada buwan. Naglalagay rin ako ng mga libreng tool, gaya ng Talaan ng Kita, Talaan ng Ilaw at Talaan ng Gastos sa Resipe. Ang mga libreng tool ang nagsisilbing pasukan para makilala ang Agenda series. Hindi gumagamit ng map API o generative AI ang Talaan ng Ilaw, kaya halos walang gastos sa pagpapatakbo nito. Kaya naibibigay ko itong libre.

Iisa ang account. Sa shared na account na tinatawag na AgendaID, magagamit ninyo ang bawat tool sa series. Hindi na kailangang magparehistro ulit sa bawat tool. May tatlong buwang libreng panahon ang mga bayad na tool at maaaring simulan nang hindi nagrerehistro ng card. Minsan lang magagamit ang libreng panahon sa bawat kombinasyon ng shop at produkto. Kung magrerekomenda kayo ng ibang shop, may bonus kayo.

Ang dahilan kung bakit mapananatili kong mababa ang presyo ay nasa paraan ko ng pagbuo. Nag-iisa akong bumubuo, pinagagawa ko sa AI ang pagbuo, at ginagamit kong muli ang shared na pundasyon. Pinananatili sa humigit-kumulang $35 kada buwan ang gastos sa database para sa buong series. Kung maliit ang gastos sa pagbuo at maliit din ang gastos sa pagpapatakbo, makatatayo ang negosyo kahit sa maliit na benta.

Magiging tapat ako. Sa panahong isinusulat ko ang librong ito, may ilang shop na sumubok ng mga tool, pero halos wala pang nagpaparehistro nang may bayad. Handa na ang sistema para sa pagbuo, pero ang sistema para makilala ay nasa unahan pa. Ang librong ito ay nilalayon ding maging isang aklat para sa layuning iyon, ang makilala.

#### Magkaiba ang Pagbuo ng Isang Bagay at ang Pagpapatuloy ng Paggamit Dito

Magiging tapat pa ako sa isa pang bagay. Magkaibang usapin ang kakayahang bumuo ng tool at ang pagkakaroon ng taong patuloy na gumagamit nito.

Bumilis ang pagbuo dahil sa AI. Pero ibang trabaho ang kailangan para patuloy itong gamitin ng mga customer. Pagsagot sa mga tanong tungkol sa paggamit (para dito ang Gabay sa Suporta). Pagpapadala ng abiso bago matapos ang libreng panahon. Pagpapaliwanag ng dahilan kapag magtataas ng presyo. Maayos na pagbura ng data kapag humiling ang isang tao na kanselahin ang serbisyo. At higit sa lahat, ang pagpapanatili nitong tumatakbo nang hindi kailangang galawin ng may-ari.

Sa tatlong prinsipyo ng Agenda series, ang "awtomatiko" ang prinsipyo para sa "pagpapatuloy ng paggamit" na ito. Ang tool na kailangan pang asikasuhin ng may-ari araw-araw para gumana ay kalaunan ding ipakakansela. Hindi pa tapos ang trabaho kapag nabuo na. Nagiging negosyo lang ito kapag patuloy itong ginagamit. Ang pagdaragdag, isa-isa, ng mga shop na patuloy na gumagamit nito: iyan ang trabaho ko pagkatapos mailathala ang librong ito.

#### Kung Gusto Ninyong Magsimula sa Sarili Ninyong Shop

Para sa mga nakabasa ng librong ito at gustong subukan sa sarili nilang shop, tatlo ang hakbang.

1. Buksan ang https://bontallc.com/agenda?via=b2-tl-{{FMT}} at mag-log in gamit ang Google account (gagawin ang AgendaID. Hindi kailangang magrehistro ng card)
2. Una, magdagdag ng isang libreng tool. Inirerekomenda ko ang Talaan ng Ilaw. I-paste lang ang component ng karatula sa inyong website, at gagana ito sa loob ng 10 minuto. Kung hindi pa kayo nagbubukas, subukan ang Talaan ng Kita
3. Kung mukhang bagay sa inyo, subukan nang libre sa loob ng tatlong buwan ang Talaan ng Oras. May darating na abiso habang papalapit ang deadline, kaya hindi kayo masisingil kahit hayaan ninyo lang ito

Kung may mga tanong kayo, magtanong sa pamamagitan ng Gabay sa Suporta (AgendaQA). Agad na sinasagot ng AI ang mga tanong tungkol sa paggamit, at ako mismo ang nagbabasa ng mga tanong tungkol sa mga espesipikasyon at bug.

Nakadepende sa panahon at sa season ang benta ng isang restawran. May hangganan ang bilang ng upuan at ang oras ng operasyon. Sa kabilang banda, walang limitasyon sa bilang ng mga upuan ang benta ng mga tool. Ang pagpapatakbo ng shop habang ipinamamahagi ang mga tool na isinilang mula sa mga problema ng sarili ninyong shop, at ang unti-unting pagiging kita nito: naniniwala akong maaari itong maging isa pang paraan ng pagkita ng isang independent na shop.

#### Manatiling Maliit na Kumpanya, Pumunta sa Buong Mundo

May isa pa akong napagpasyahan tungkol sa Agenda series mula sa simula. Hindi ko ito bubuuin sa wikang Hapon lang.

Magagamit sa 20 wika ang Talaan ng Oras, ang Talaan ng Kita at ang Gabay sa Suporta. Ang teksto ng screen at ang mga madalas itanong, lahat. Ang tool na ginawa para sa isang bar sa Tokyo na may 19 na upuan ay ganoon din ang takbo sa Ingles, sa Koreano, sa Vietnamese.

May dalawang dahilan. Ang una ay hindi nagbabago ang mga problema ng mga restawran kapag nagbago ang bansa. Gusto ninyong itala kung kailan dumarating at umaalis ang staff. Gusto ninyong malaman ang kakayahang kumita bago magbukas. Gusto ninyong ipaalam sa mga customer na pinahaba ang oras ng pagsasara. Mga problemang pareho ito ng mga independent na shop sa buong mundo. Ang ikalawa ay patuloy na bumababa ang bilang ng mga independent na shop sa Japan. Kung ang pamilihang Hapones lang ang pagsisilbihan ko, may hangganan ang benta ng mga tool.

Dati, para makapagbenta ng mga produkto sa ibang bansa ang isang maliit na kumpanya, kailangan nito ng mga lokal na ahente, kumpanya sa pagsasalin, at legal na entidad. Ngayon, tumutulong ang AI sa pagsasalin at pag-proofread. Gumagana sa buong mundo ang mga shared na sistema ng pagbabayad. Para sa paghahatid, server lang ang kailangan, at hindi kailangan ang stock o bodega sa bawat bansa. Ang tool na gawa ng isang may-ari ay maaaring nasa mga istante ng buong mundo sa 20 wika kinabukasan pagkatapos itong magawa. Noon, malalaking kumpanya lang ang nakagagawa niyan.

Isang napakaliit na kumpanyang nakikipagnegosyo sa maraming bansa mula sa simula: ang mga ganitong kumpanya ay tinatawag minsang micro-multinational (maliliit na multinasyunal na kumpanya). Ito mismo ang tinutungo ng Bonta LLC, na may isang shop sa Higashi-Nakano at isang may-ari.

Siyempre, hindi nangangahulugang magsisimula agad na gamitin ng mga may-ari sa ibang bansa ang mga ito dahil lang naisalin sa 20 wika. May ilang salin na naghihintay pa ng pagsusuri ng mga native speaker para tumunog na natural. Gayunpaman, sa pag-alis ng hadlang ng wika mula sa simula, nawawala ang hangganan kung hanggang saan makararating ang mga tool, gaya ng pagkawala ng hangganan ng mga upuan.

Ang kuwento ng Kabanata 4 ay kung paano ko binubuo ang pundasyong iyon.

【Larawan 3-5】Pagpapalit ng wika sa Gabay sa Suporta. Nakalista ang 20 wika *(Nasa wikang Hapon ang screen.)*

## Kabanata 4: Teknolohiya - Sistemang Bumubuo ng mga Produkto Nang Mag-isa at Tuluy-tuloy

Mga pangunahing punto ng kabanatang ito

- Ginawa kong dokumento ang pamamaraan sa paglulunsad ng bagong produkto, sa anyong (isang skill) na mababasa at maisasagawa ng AI. Ang ginagawa ng tao ay ang paghusga at ang mga operasyong tao lang ang kayang gumawa
- Ang mga shared na bahagi, gaya ng login, billing, mga pahina ng pagpapakilala, at mga gabay papunta sa ibang produkto, ay binubuo nang isang beses lang at ginagamit muli sa lahat ng produkto. Humigit-kumulang $35 kada buwan ang gastos sa database ng pundasyong iyon
- Patuloy pang pinalalaki ang sistema. Patuloy kong idinaragdag sa dokumento ng pamamaraan ang mga pagkabigo, gaya ng disenyong tinanggihan nang limang beses na sunod-sunod

(Kabanatang maraming teknikal na termino ito. Kung hindi kayo interesado sa teknolohiya, puwede kayong lumaktaw sa Kabanata 5 at tuloy pa rin ang kuwento.)

### 4-1 ProductBootstrap: Ipinauubaya sa AI ang Mismong Pamamaraan ng Paglulunsad

Sa bawat pagbuo ko ng produkto, inuulit ko ang parehong paghahanda at ang parehong mga pagkakamali. Gumawa ng repository (imbakan ng mga program). Ikonekta ang login. Piliin ang mga kulay ng disenyo. I-set up ang sistema ng pagte-test. Ihanda ang production environment. Tiyak na nagawa ko na ang lahat ng iyon para sa naunang produkto, pero nakalimutan ko ang mga detalye at nagkamali ako sa parehong mga bahagi.

Kaya ginawa kong dokumento ang pamamaraan sa paglulunsad ng bagong produkto. Ang anyo nitong mababasa at maisasagawa ng AI na sumusulat ng code (Claude Code) ang tinatawag kong "skill." Ang pangalan ng skill na ito ay ProductBootstrap. Ang "Bootstrap" ay karaniwang termino sa mundo ng computer para sa pagsisimula nang mag-isa mula sa kaunting mekanismo, at ginamit ko ito sa paglulunsad ng mga produkto.

Wala akong iniingatang template na program. Kinokopya ko ang pinakahuling natapos na produkto at doon ako nagsisimula sa bagong produkto. Sa ganoong paraan, kusang naipapasa sa susunod na produkto ang pinakabagong mga aral. Hindi na rin kailangang patuloy na i-maintain ang lumang template.

#### Ang Daloy ng Pamamaraan

1. Ibigay ang requirements document. Kung may naiwang blangko sa mga kinakailangang field (pangalan ng produkto, ang ginagawa nito, sino ang gagamit, presyo, yunit ng pagpepresyo, kulay na pagkakakilanlan, lokasyon ng master na disenyo, at iba pa), hindi nagsisimula ang AI. Ang patakaran ay hindi ito magtatanong sa may-ari habang nasa gitna. Kung hindi kumpleto ang lahat sa simula, hindi ito nagsisimula
2. Piliin ang kulay ng produkto. May isang kulay na pagkakakilanlan ang bawat produkto sa Agenda series. Sinusukat ng AI ang mga kulay ng mga kasalukuyang produkto, nagmumungkahi ng mga apat na kandidatong hindi nagsasapawan, at pumipili ang may-ari
3. Itakda ang disenyo. Pinapagawa ko sa isang design AI (Claude Design) ang mga panukala para sa mga screen. Hanggang tatlong round ang self-check ng AI, at ang mga panukalang pumasa lang sa pagsusuri ang ipinapakita sa may-ari
4. Ipaubaya sa AI ang pagpapatupad hanggang sa dulo. Bumubuo at nag-aayos ang AI nang mag-isa hanggang matugunan ang mga itinakdang kondisyon ng pagtanggap (mga type check, mga style check, berde ang lahat ng test, pumasa sa bawat pagsusuri ng screen, at maayos na pumapasok sa test environment ang mga pagbabago sa database)
5. Ang may-ari ay nag-aapruba lang kapag papunta na sa production. Awtomatikong tumatakbo ang lahat hanggang sa test environment, at ang operasyon sa production lang ang hinuhusgahan ng may-ari

Binuo ko ang yugto ng pagpapatupad para hindi ito tumigil sa gitna para maghintay ng pag-apruba ng may-ari. Noong una, humihingi ang AI ng pag-apruba sa bawat yugto, pero walang umuusad sa ganoong paraan. Kapag maraming work window ng AI, bawat isa ay humihinto sa paghihintay ng pag-apruba, at kailangang libutin ng may-ari ang bawat window para humusga. Kaya binago ko ito: ibinibigay ko nang maaga ang saklaw na naaprubahan na at ang mga kondisyon ng pagtanggap na kayang husgahan ng makina, at humihinto lang ito kapag pumalpak.

Itinakda rin ang mga kondisyon ng paghinto. Kapag nagkasalungatan ang dokumento ng pamamaraan at ang hatol ng may-ari. Kapag kinailangan ang operasyong tao lang ang kayang gumawa. Kapag hindi ito umusad sa parehong error nang tatlong sunod-sunod na beses. Kapag nag-expire ang authentication, kulang ang mga pahintulot, o kinailangan ang operasyong hindi na mababawi. Maliban doon, nagpapatuloy ang AI nang mag-isa. Naitatala sa isang maliit na file ang lagay ng trabaho, kaya kahit mag-crash sa gitna, maipagpapatuloy ito mula roon.

#### Dalawang Bagay Lang ang Ginagawa ng Tao

Isinulat ko ito sa dokumento ng pamamaraan: ang AI ang nagsasagawa ng bawat hakbang. Maaaring hingan ang may-ari ng dalawang bagay lang na ito.

- Ang mismong paghusga. Pag-apruba, paghatol, pagpapasya kung alin sa dalawang opsyon ang pipiliin
- Mga operasyong tao lang ang kayang gumawa. Mga susi na maibibigay lang mula sa admin screen ng isang panlabas na serbisyo, mga aplikasyong may kinalaman sa pagpapatunay ng pagkakakilanlan, mga operasyon sa tunay na device at biswal na paghusga

Kung may anumang iba pang ibibigay ang AI sa may-ari, paglabag iyon sa dokumento ng pamamaraan. Sa talahanayan ng pamamaraan, nagdagdag ako ng column na "tagapagsagawa" sa bawat hilera, at ang anumang hilera na hindi makapagsasaad ng dahilan ang entry ng may-ari ay inililipat sa panig ng AI.

May dahilan ako sa paggawa ng patakarang ito. Nang ayusin ko ang natitirang trabaho para sa isang produkto, inilista ng AI ang "gumawa ng server project," "irehistro ang destinasyon ng login," "ilagay ang mga environment variable," at "buuin ang test environment," lahat bilang gawain ng may-ari. Bawat isa sa mga ito ay operasyong kayang gawin mismo ng AI. "Bakit ako ang gumagawa nito?" ang tapat kong reaksyon noon. Gumagawa mismo ang AI kung hihingin ninyo. Pero kung hindi ninyo hihingin, ipapasa nito sa tao. Kaya kinailangan kong isulat ito sa dokumento ng pamamaraan.

Inilagay ko sa checklist ng dokumentong ito ang bawat pagkabigo ng reservation system na inilarawan ko sa Kabanata 2. Ilagay muna ang mga test. Huwag magtago ng production data sa development environment. Buuin muna ang test environment. Sa susunod na produkto, maiiwasan na ang parehong pasakit mula sa simula.

#### Patuloy na Lumalaki

Hindi tapos na produkto ang dokumentong ito ng pamamaraan. Patuloy ko itong dinadagdagan sa bawat pagkabigo.

Halimbawa, minsan ay pinagawa ko sa design AI ang screen ng isang produkto nang limang beses na sunod-sunod, at tinanggihan ang lahat ng lima. Kasama riyan ang mga round kung saan ibinigay ko rito ang mga tuntunin ng disenyo para sa buong series (DESIGN.md).

Sa simula, ang diyagnosis ng AI sa sanhi ay "ang color scheme mismo." Hindi ako sumang-ayon doon. Dalawa ang tunay na sanhi. Una, basta-basta na lang ginagamit ang mga kulay na walang depinisyon sa mga tuntunin. Ikalawa, tatlong seksyong magkakaiba ang tungkulin ay pinagpatong nang patayo na pareho ang kulay ng background at pareho ang mga margin, na walang hangganan sa pagitan. Walang tuntuning nalabag, pero nawala sa hitsura ang mga tungkulin.

Kaya nagdagdag ako ng mga alituntunin sa mga tuntunin ng disenyo. Huwag bigyan ng parehong hitsura ang mga bagay na magkaiba ang tungkulin. Huwag paghiwalayin sa kulay lang. Ang pinakamahalaga ay nasa unahan ng linya ng paningin. Ang mga bagay lang na tunay na magkapantay ang puwedeng ihanay sa parehong bigat. Huwag gumawa ng layout na patong-patong lang nang patayo.

May isa pang aral mula sa pagkabigo. Kung ang "default na hitsura na dapat iwasan" ay ipinaparating lang bilang listahan ng mga pagbabawal, buong-buong lilipat ang AI sa ibang default na wala sa listahan. Nang ipagbawal ko nang sabay-sabay ang mga card, anino at bilugang sulok, ang bumalik ay screen na parang pahayagan na puro guhit at margin lang. Mula noon, isinusulat ko ang mga materyales ng kahilingan sa tatlong column: "ang pattern na iiwasan," "ang gusto kong ipagbawal," at "ang gagawin sa halip."

Binago ko rin sa kalagitnaan ang paraan ng pagpapasya ng mga kulay na pagkakakilanlan. Nang lumampas sa walo ang mga produkto, napuno ng mga kasalukuyang produkto ang hanay ng madidilim na kulay, at ang ikasiyam at mga sumunod na produkto ay hindi na makakuha ng madilim na kulay para sa mga guhit at buton nang hindi bumabangga sa mga kasalukuyan. Kaya binago ko ang tuntunin: ang kulay na pagkakakilanlan ng isang produkto ay ginagamit lang sa mga mapusyaw na kulay ng ibabaw, at ang mga guhit, rule, icon at pangunahing buton ay pinag-isa lahat sa shared na kulay ng tinta ng series. Isa itong limitasyong lumitaw lang nang dumami ang mga produkto.

Sa bawat pagkabigo, inaayos ko ang dokumento ng pamamaraan. Gumagaan nang ganoon ang susunod na produkto. Naniniwala akong ang paglaki ng dokumento ng pamamaraan ang pinakamahusay na puhunan para patuloy na makabuo ng mga produkto nang mag-isa.

【Larawan 4-2】Ang mga yugto ng pamamaraan sa paglulunsad, at kung sino ang nagsasagawa (ang AI o ang may-ari) *(Nasa wikang Hapon ang screen.)*

【Larawan 4-3】Ang mga kulay na pagkakakilanlan ng Agenda series. Isang kulay kada produkto, ginagamit lang sa mga ibabaw *(Nasa wikang Hapon ang screen.)*

### 4-2 AgendaHub: Ang Pintuan

Habang dumarami ang mga produkto, paulit-ulit ninyong nabubuo ang parehong mga bagay. Login, billing, mga pahina ng pagpapakilala, mga gabay papunta sa ibang produkto. Para mapatakbo ito nang mag-isa, kailangang buuin nang isang beses lang ang mga shared na bahagi at gamitin muli sa lahat ng produkto.

Ang AgendaHub ang lugar kung saan nakatipon ang mga shared na bahaging iyon. Tinatawag ko itong "pintuan."

Una, ito ang pasukang nagpapadala mula sa isang address papunta sa bawat produkto. Sa ilalim ng iisang domain, ang bontallc.com, nakahanay ang pasukan para sa bawat produkto: /agendatimbro, /agendaoro, /agendaluce. Sa mga customer, parang nasa loob ng iisang site ang mga produkto, pero sa totoo ay may magkahiwalay na program na tumatakbo sa likod ng bawat isa.

Sunod, dito inilalagay ang mga pahina ng pagpapakilala ng produkto. May isang pahina ng pagpapakilala para sa series, at sa loob nito ay may seksyon para sa bawat produkto. Taglay ng bawat seksyon ang pangalan ng produkto at ang palayaw nito, ang presyo, isang problemang sinabi sa sariling salita ng may-ari na nagsisimula sa "Kapag kayo ay...," paglalarawan ng kaya nitong gawin, at link papunta sa pahina ng detalye. Kapag naglalabas ako ng bagong produkto, kasama sa pamamaraan ng paglulunsad ang pagdaragdag ng seksyong ito.

At ito ang tahanan ng mga tuntunin ng disenyo at ng mga pamamaraan ng paglulunsad. Ang master ng mga kulay na pagkakakilanlan, ang mga tuntunin ng screen (DESIGN.md), ang ProductBootstrap skill na inilarawan ko sa 4-1, ang skill na nagsusuri ng mga screen, at ang skill na ligtas na gumagawa ng mga pagbabago sa database. Para sa bawat tuntuning sumasaklaw sa buong series, dito nakatira ang aktuwal na nilalaman, at binabasa ito ng bawat produkto sa pamamagitan ng reference.

【Larawan 4-1】Ang istruktura ng Agenda series. Mula sa pintuan (AgendaHub) papunta sa bawat notebook, at bawat notebook ay nakakonekta sa iisang account (AgendaID) *(Nasa wikang Hapon ang screen.)*

### 4-3 AgendaID: Mga Shared na Account at Billing

Ang AgendaID ang shared na sistema ng series para sa mga account at billing.

Ang may-ari na isang beses nag-log in gamit ang Google account ay makagagamit ng bawat produkto. Hindi na kailangang gumawa ng account para sa bawat produkto. Balak ko ring dalhin sa lahat ng produkto ang mga setting ng wika balang araw.

Iisang sistema rin ang billing. Sa halip na buuin ang koneksyon sa payment service (Stripe) para sa bawat produkto, ang AgendaID ang umaako sa lahat. May apat na kategorya ng pagpepresyo: magaan na produktong ¥300 (humigit-kumulang $2) kada buwan, produktong bayad ayon sa paggamit, produktong minsanang pagbili na ¥600 (humigit-kumulang $4), at libreng produkto. May tatlong buwang libreng subok ang mga produktong may bayad nang hindi nagrerehistro ng card, magagamit nang isang beses sa bawat kombinasyon ng shop at produkto. May mekanismo rin na nagdaragdag ng tig-tatlong buwang libreng panahon sa nagrekomenda at sa nirekomendahan.

Bago matapos ang libreng panahon, dumarating ang mga email ng abiso pito at isang araw nang maaga. Sa simula, binuo ko rin ang mga email na ito sa loob ng Talaan ng Oras, pero nang dumami ang mga produkto, napagtanto kong aksaya ang bigyan ng parehong mekanismo ang bawat produkto, kaya pinagsama ko ito sa panig ng AgendaID.

#### Pagkansela at Pagbura sa Ilalim din ng mga Shared na Tuntunin

May bahaging payak pero mahalaga: ang pagkansela at pagbura ng data.

Kapag nagkansela ang customer, aling data ang buburahin, at kailan? Kung bubuuin ito nang hiwalay sa bawat produkto, tiyak na may makakaligtaan sa kung saan. Higit pa riyan, kasama sa Agenda series ang mga produktong humahawak ng lalo na sensitibong data, gaya ng tumutukoy sa mga suki gamit ang face recognition.

Kaya hinati ko sa apat na antas ang antas ng pagbura at ginawa itong tuntuning shared sa buong series. Ito ay ang pagkansela ng produkto, pagbura ng shop, pag-withdraw ng account (pag-alis sa buong series), at kahilingan ng pagbura mula sa indibidwal na staff. Bumababa ang epekto ng mga mas mataas na antas sa mga mas mababa, at inirerehistro ng bawat produkto sa shared na sistema ang sarili nitong pamamaraan sa pagbura ng data. 30 araw ang palugit ng pagbura, at sa panahong iyon ay maaari itong bawiin.

Pumapasok din dito ang usapin ng panahon. Ang mga talaan ng attendance, halimbawa, ay kinakailangan ng batas na itago sa loob ng limang taon. Kahit humiling ng pagbura ang dating staff, sa loob ng panahon ng pagtatago ay kailangang itago ang talaan, na ginagawang anonymous ang mga pangalan at iba pa, sa halip na pisikal na burahin. Kinailangan kong pagpasyahan ang guhit sa pagitan ng "burahin" at "itago" sa pamamagitan ng pagsusuri nito sa batas.

#### Test Login para Hindi Madumihan ng AI ang Production

Nagdagdag pa ako ng isa pang mekanismo sa AgendaID, para sa AI: isang pasukan ng test login.

Para ipasuri sa AI na gumagana ang mga bagay, kailangang mag-log in ang AI at patakbuhin ang mga screen. Pero Google account ang ginagamit sa pag-log in, kaya hindi makakapag-log in ang AI nang mag-isa. At hindi ko rin maibibigay sa AI ang account ng may-ari. May panganib na madumihan ng mga test ng AI ang production data.

Kaya gumawa ako ng pasukang nagbibigay ng mga synthetic na account (persona) na magagamit lang sa test environment. Hindi ito gumagana sa production. Hiwalay na proyekto mula sa production ang database ng test environment at synthetic na data lang ang laman. Nag-log in ang AI sa pasukang ito, pinapatakbo ang mga screen, at tinitiyak na gumagana ang mga bagay. Muling binubuo araw-araw ang mga test account, at binubura ang mga luma.

Dahil dito, kayang isagawa mismo ng AI kahit ang huling pagsusuri, sa kapaligirang binuo na eksaktong kapareho ng production, nang hindi hinahawakan ang production.

### 4-4 Ang Common Navigation, at ang Pagkabigo ng Salitang "Pintuan"

Para makapunta ang mga gumagamit mula sa kahit anong produkto papunta sa iba pa, binigyan ko ang bawat produkto ng shared na navigation menu. Ito ang landas na nagpapahintulot sa may-ari ng bar na gumagamit ng Talaan ng Oras na magtanong sa Gabay sa Suporta, o pumunta at tingnan ang iba pang notebook.

May maliit na kuwento ng pagkabigo sa likod ng shared na navigation na ito.

Sa unang bersyon, naglagay ako ng link na nagsasabing "Bumalik sa pintuan." Iyon ay dahil sa sarili kong internal na tawag, "pintuan" ang tinatawag ko sa AgendaHub. Pero nang suriin ko sa tunay na device, may mali. Iisang lugar ang pinupuntahan ng dalawang link, ang "Bumalik sa pintuan" at ang "Tingnan ang Agenda series." Bukod pa roon, nasa ibabaw ng menu ng pang-araw-araw na trabaho ang link ng suporta, kaya baliktad ang pagkakasunod-sunod ng kahalagahan. At higit sa lahat, walang kahulugan ang salitang "pintuan" para sa may-ari na unang beses pa lang gumagamit ng produkto. Sariling panloob na wika iyon ng gumawa.

Kaya itinakda kong muli ang mga prinsipyo. Ayusin ang mga aytem ayon sa lapit ng mga ito sa layunin ng gumagamit: ang pang-araw-araw na trabaho sa pinakaitaas, ang mga link na papunta sa labas sa pinakaibaba. Kahit ang link na nilalayong makahikayat ng bagong gumagamit ay hindi kailanman ilalagay sa ibabaw ng trabaho. Dapat maipaliwanag ang hangganan sa isang linya. Isulat ang pananalita sa wika ng gumagamit, hindi sa panloob na wika. Huwag maglagay ng higit sa isang link na pumupunta sa iisang lugar. Inalis ko ang "Bumalik sa pintuan" at pinagsama ang lahat sa iisang link, "Tingnan ang iba pang notebook ng Agenda."

Sa Kabanata 2, isinulat ko ang tungkol sa pag-aaral ng wika ng UI. Wikang iyon para gamitin ng may-ari sa pakikipag-usap sa AI. Kabaligtaran ito: wikang ginagamit ng gumawa sa pakikipag-usap sa gumagamit. Sa dalawang kaso, tungkol ito sa pag-aangkop ng inyong mga salita sa taong kinakausap.

【Larawan 4-4】Ang shared na navigation pagkatapos ng pag-aayos. Nasa itaas ang trabaho, at nasa pinakaibaba ang mga link na papunta sa labas *(Nasa wikang Hapon ang screen.)*

### 4-5 Nagkakahalaga ng $35 Kada Buwan ang Pundasyon

Humigit-kumulang $35 kada buwan ang gastos sa database ng buong pundasyong inilarawan sa kabanatang ito. $25 ang bayad na plano na kasama ang production project, at $10 ang proyekto para sa test environment.

Hindi rin ito ang halaga mula sa simula. May panahon na nagbabayad ako ng $45 kada buwan. Patuloy na sinisingil ang development database ng isang produktong face recognition kahit hindi ko ginagamit. Inilipat ko ito sa free tier at pinahinto, at binura ko ang isa pang proyektong hindi ko ginagamit, at ganoon ito umabot sa kasalukuyang halaga.

Binabantayan ko rin ang gastos sa AI. Sinisingil ayon sa dami ng token (ang yunit ng tekstong binabasa at isinusulat ng AI) ang trabaho ng AI na sumusulat ng mga program. Iniiwasan kong magkonsentra ang mga gastos sa pamamagitan ng pagpapanatili sa work window sa tungkulin ng tagapag-ugnay, at pag-iwan ng mismong pagpapatupad sa ibang AI na may hiwalay na alokasyon ng gastos. Para sa generative model sa chat window, tinitingnan ko rin ang presyo at pinipili ang sapat at kailangan lang. Kahit $1 lang ang dagdag kada buwan ng mas mataas na modelo, pinipili ko sa pagtatanong na "sapat ba ito?"

Kung maliit ang pagkakabuo, kayang mabuhay ng negosyo kahit sa maliit na benta. Ang kuwento ng monetization sa Kabanata 3 ay sinusuportahan ng liit ng gastos ng pundasyong ito.

### 4-6 Ang Nag-uugnay na AI, at ang Taong Nagpapasya

Panghuli, ilalarawan ko ang daloy ng aking pang-araw-araw na pagtatrabaho.

Sabay-sabay na bukas sa akin ang ilang work window ng AI. May window para sa reservation system, window para sa bawat produkto, at isang coordinator window na nagpapadala ng mga tagubilin sa mga ito at nagtitipon ng mga resulta. Pinangalanan kong AgendaRegia (ang nag-uugnay na notebook) ang coordinator window.

Ang mga nagbibigay ng hatol, ibig sabihin, nagpapasya ng "saang direksyon pupunta," ay ako at ang AI sa panig ng chat. Nahahanap nang maaga ng AI sa panig ng chat ang mga puwang at kontradiksyon sa mga espesipikasyon, nilalagyan ang bawat isa ng default na hatol, at isinusumite ang lahat nang sabay-sabay. Binabasa ko ang mga ito at nagpapasya ako. Ang napagpasyahan ay tinitipon sa isang instruction sheet na tinatawag na Goal at ipinapaste sa work window. Kasama rito ang mga paunang pag-apruba at mga kondisyon ng pagpasa na kayang husgahan ng makina. Binabasa ito ng work window at ipinagpapatuloy hanggang sa dulo, humihinto lang kapag may pumalpak.

Pinapalagyan ko rin ang instruction sheet ng pagtatantya kung kailan matatapos ang trabaho. Isinisingit ko ang trabahong ito sa pagitan ng mga oras ng operasyon ng bar, kaya kung hindi ko alam kung gaano katagal ang isang bagay, hindi ko mapaplano ang aking araw.

Ang papel ng may-ari ay hindi ang pagbabasa kundi ang pagpapasya. Hindi ko kailangang basahin ang lahat ng 1,775 conversation log. Sumasagot ako sa mga tanong tungkol sa mga katotohanan ng bar. Humahatol ako sa mga bagay na patakaran lang ng bar ang makapagpapasya. Pagkatapos mag-live ng isang bagay, lima o anim na beses ko itong sinusubukan mismo para tingnan kung may kakaiba. Iyon lang.

Bago makarating sa anyong ito, maraming beses kong inulit ang trabaho. Basta-basta na lang nagdagdag ng mga feature ang AI nang walang pahintulot at naging hindi matatag ang mga screen. Lumaki nang walang hangganan ang trabaho mula sa iisang tagubilin. Dahil naghihintay ng pag-apruba sa bawat yugto, walang umuusad. Sa bawat pagkakataon, nagdagdag ako ng isang tuntunin, at ganoon ito umabot sa kasalukuyang anyo. Patuloy ding lumalaki ito.

#### Ano ang Maiuuwi Ninyo mula sa Kabanatang Ito

- Para sa paulit-ulit na trabaho, gawing dokumento ang mismong pamamaraan at ibigay sa AI. Kung aayusin ninyo ang manwal sa bawat pagpalpak, gagaan ang susunod na pagkakataon
- Buuin nang minsan lang ang mga karaniwang bahagi (login, billing, navigation) at gamitin muli sa lahat ng produkto. Kung maliit ang pundasyon, makapagbibigay-buhay kahit ang maliliit na benta
- Ang tao ay gumagawa lang ng paghusga at ng mga operasyong tao lang ang kayang gumawa. Kung may ibang ibibigay sa inyo ang AI, idagdag ito sa manwal

Ang karugtong ng kabanatang ito (ang mga susunod na notebook na bubuuin ko, at ang mga aral na idinagdag ko sa manwal) ay nasa note at X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Kabanata 5: Ang Kinabukasan ng Isang Maliit na Bar

### 5-1 Mula sa Zatta Gohan hanggang sa Tamuro

Pumasok ako sa negosyo ng pagkain at inumin noong 39 anyos ako.

Ang naging simula ng lahat ay isang bar sa kapitbahayan na tinatawag na Zatta. Minsan sa isang buwan, kung minsan ay tuwing dalawang linggo, pinapayagan nila akong maghain ng mga pagkain doon. Matagal akong nagturo sa sarili ng pagluluto, at nagkaroon ako ng lugar kung saan kinakain ng mga tao ang luto ko at natutuwa sila. Iyon ang orihinal kong karanasan.

Noong 2014, nagbukas ako ng restawran na tinatawag na Zatta Gohan sa Arai-Yakushi. Isa itong maliit na lugar na naghahain ng mga set meal. Pitong taon ko itong pinatakbo.

Sa Arai-Yakushi, gayunman, nadama kong may hangganan ang bilang ng mga customer. Pagkatapos ay nakahanap ako ng property sa Higashi-Nakano. Wala pang isang minuto ang lakad mula sa silangang labasan ng istasyon. Kahit maulan, makararating doon nang hindi gaanong nababasa.

Noong Nobyembre 2018, binuksan ko roon ang Tamuro. Ang "Tamuro" ay nangangahulugang lugar kung saan nagtitipon ang mga tao. May 11 upuan sa counter at 8 upuan sa tatami, 19 sa kabuuan. Sa loob ng tatlong taon, pinatakbo kong sabay ang dalawang lugar, sa Arai-Yakushi at sa Higashi-Nakano. Sa panahon ng COVID, naging mahirap panatilihin ang dalawa, kaya isinara ko ang shop sa Arai-Yakushi at ang naiwan ay ang Tamuro lang.

#### Ang Curation Bar

Tinatawag ng Tamuro ang sarili nito na "curation bar."

Ang curation ay nangangahulugang pagkakaroon ng matalas na mata sa pagpili. Higit sa pagiging kusinero, nais kong maging isang curator. Ang pagkain, ang mga inumin, ang atmospera ng bar: lahat ay ginagawa ko sa pamamagitan ng pagpili gamit ang matalas na mata. Iyan ang Tamuro.

Madalas akong maglakbay para kumain, sa ibang bansa man o sa Japan. Vietnam, Cambodia, Italya, Shanghai, Beijing, Mexico. Kasiyahan ang paglibot habang kumakain, at kasabay nito ay paraan ito ng paghahanap ng ihahain sa Tamuro. Binubuo kong muli ang mga mamahaling sangkap gamit ang mga sangkap na madaling makuha. Halimbawa, kung patutuyuin at kakayurin ang pula ng itlog, magkakaroon ng lasang malapit sa bottarga. Itinuturing kong tungkulin ko ang ganitong pagpapalit (localization).

Muli akong nag-aral ng pagluluto noong panahon ng COVID. Kumuha ako ng kursong French cooking na walong sesyon ang kabuuan, at dumalo rin ako sa isang kurso sa lutuing Hapon. Ang tamang pagtimpla ng umami, at ang wastong kontrol sa apoy at init. Ang natutunan ko roon ang pundasyon ng pagluluto ko ngayon.

Binubuo ang menu ng Tamuro ng apat na pampagana at isang main. Binibigyan ko ito ng saklaw ng mga sangkap para makakuha ng maraming gulay ang mga customer na mag-isang nakatira. Binubuo ko ito para hindi magsapawan ang mga paraan ng pagluluto (prito, may suka, nilaga, inihaw) at ang mga lasa (matamis, maanghang, maasim). Ang pinakapopular na putahe ay ang tonteki, pork steak. May bahagyang matamis itong sarsa na gawa sa toyong galing Kyushu, na maraming bawang.

#### Isang Lugar na Pinagtitipunan ng mga Tao

Halos kalahati ng mga customer ng Tamuro ay mag-isang dumarating. Karamihan sila ay nasa edad 30 hanggang 50, at marami ang mga kapitbahay mula sa Higashi-Nakano, pero may dumarating din mula sa paligid ng Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo at Eifukucho. 

Ang natatanging katangian ng bar ay kung gaano nag-uusap ang mga customer sa isa't isa. Ginawa ko ang counter para madaling kausapin ang katabi, at ako o ang staff ang nagpapasya ng upuan sa pamamagitan ng paghusga kung sino ang magkakasundo. Ang mga customer na mag-isang dumating ay minsang bumabalik nang magkakasama sa kalaunan. Gaya ng sinasabi ng pangalan, naging lugar ito kung saan nagtitipon ang mga tao. Ipinopost ko sa [Instagram](https://www.instagram.com/tamuro.higashinakano/) ang pang-araw-araw na mga kaganapan sa bar.

Sa course dinner na ginaganap halos isang beses kada buwan, naghahain ako ng pito hanggang walong putahe sa loob ng dalawa hanggang tatlong oras, kasama ang mga wine pairing. Bawat buwan ay nagbabago ang tema: Italyano, Pranses, Hapones. Ang mga cooking class ay tatlong oras na workshop, at pagkatapos magluto, nagtotoast ang lahat, kumakain, at umuuwi. May aperitivo, na naghahain ng wine at maliliit na putahe sa maagang gabi bago magbukas. May barbecue nang mga dalawang beses kada taon. May year-end party nang isang beses kada taon. At may yukata festival na isinulat ko sa Kabanata 1.

Ang reservation system na isinulat ko sa Kabanata 1, ang chat window, at ang MCP ay pawang mga tool para magdala ng mga tao sa bar na ito. Ang AI ay paraan ng pagtitipon ng mga tao, hindi ang layunin.

### 5-2 Ang Hamburger Curry ng Quatre Épices

Pang-gabing bar ang Tamuro. Sa araw, walang laman ang espasyo.

Sa paggamit ng oras na iyon, sinimulan ko ang Quatre Épices noong Enero 2024. Isa itong hamburger curry shop na nagpapatakbo lang sa tanghalian sa parehong lugar, at ang staff ang nagpapatakbo.

Ang Quatre Épices ay nangangahulugang "apat na pampalasa" sa Pranses. Alinsunod sa pangalan, sa halip na magpatong-patong ng maraming pampalasa, pinipili at nililimita namin ang mga sangkap para maging malinaw ang balangkas ng lasa. Walang harina ang curry; tinatapos ito sa natural na kapal ng mga gulay at karne mismo. Kasiyahan pagkatapos kumain, at walang bigat sa tiyan. At pagkakatugma sa hamburger. Dinisenyo ko ito sa tatlong saligang iyon.

Maselan kami sa paraan ng pagluluto ng hamburger. Itinakda namin ang timpla para lumabas itong malutong sa labas at malambot sa loob, at nagluluto kami ayon sa timplang iyon. Ang natutunan kong kontrol sa init sa gabi sa Tamuro ay napapakinabangan din sa mga inihahain tuwing tanghali.

Maaaring magbago ang mga presyo, araw ng operasyon at oras, kaya pakitingnan ang Instagram ng Tamuro (https://www.instagram.com/tamuro.higashinakano/) para sa pinakabagong impormasyon.

Nagpapatakbo rin ang Quatre Épices ng "kodomo shokudo" (isang community kitchen para sa mga bata) sa parehong lugar. Isa itong gawaing gumagamit ng mga kasalukuyang pasilidad at pamimili ng bar para maghain ng pagkain sa mga bata sa kapitbahayan. Sa pamamagitan ng koneksyong iyon, nakabuo rin kami ng ugnayan sa lokal na community center. Minsan ay naghahain kami ng curry at mga sandwich sa mga lokal na kaganapang pampalakasan, mga kaganapan ng community center at mga Bon dance festival.

Sa totoo lang, hindi lahat ng paggamit sa oras ng araw ay naging maayos. Gumawa ako ng mga araw para sa pag-inom tuwing tanghali at pinaupahan ko ang espasyo sa ibang tao, pero hindi dumating ang mga customer gaya ng inaasahan ko. Magkaiba ang dating ng ganda ng bar kapag naroon ang may-ari sa gabi at kapag ang staff sa araw lang ang naroon. Ang pagpapalago ng shop sa araw sa pamamagitan ng ganda na iba sa shop sa gabi ay hindi pa tapos na gawain.

### 5-3 Bonta LLC: Dalawang Haligi

Ang maliit na kumpanyang nagpapatakbo ng Tamuro at Quatre Épices ay ang Bonta LLC. Ako ang managing member nito.

May dalawang haligi ang kumpanya. Isa ang pagkain at inumin: ang Tamuro at Quatre Épices. Ang isa pa ay ang IT: pagbuo ng Agenda series, at consulting.

Magkaiba ang paraan ng pagkita ng pagkain at inumin at ng mga tool. Ang pagsuporta sa kumpanya sa pamamagitan ng dalawang haliging magkaiba ang kalikasan ang anyong nasa isip ko.

At nagbibigay ng mga materyales sa isa't isa ang dalawang haligi. Ang problema sa bar ay nagiging binhi ng tool. Ang natututuhan ko sa pagbuo ng mga tool ay bumabalik sa pagpapatakbo ng bar. Isinilang ang Talaan ng Ilaw mula sa pagka-extend ng oras ng pagsasara, at ang mga talaan ng extended hours mula sa Talaan ng Ilaw ay nagiging batayan ng mga pagtataya ng kita at ng mga shift. Ang "mga tanong na hindi namin nasagot" na naiipon sa chat window ay nagpapabuti sa gabay ng bar. Ang siklong ito ang dahilan kung bakit mapapamahalaan kong mag-isa ang parehong bar at pagbuo.

Hindi ko iniisip na palakihin ang kumpanya. Maliit, marami, at mura. Iyan ang hugis ng kumpanyang ito.

### 5-4 Pagsusulat bilang si Raku Bonta

Kapag nagsusulat at naglalathala ako, ginagamit ko ang sagisag-panulat na "Raku Bonta." Isinulat ko rin ang librong ito sa pangalang iyon.

Ang naunang libro ko, *Ang AI Assistant Manager*, ay libro tungkol sa generative AI. Pumuwesto ito bilang numero uno sa kategorya ng time management ng Amazon at binasa ng maraming tao. Ang librong ito ang karugtong nito.

Bukod sa mga libro, nagsusulat din ako sa note. Isinusulat ko ang mga pagsisikap ng bar kasama ang AI, ang mga natuklasan ko sa isang training trip, ang pag-usad ng paglalathala ng aking mga libro, at ang Agenda series. Masusundan ninyo sa note (https://note.com/bontallc) ang karugtong na hindi ko naipasok sa librong ito.

Para sa akin, paraan din ang pagsusulat para isalita at suriin ang parehong bar at pagbuo. Gaya ng isinulat ko sa Kabanata 1, ang unang kaalaman ng chat window na "T-AI-MURO" ay binuo mula sa mga salitang iniiwan ko sa X. Ang mga isinulat ko ay naging materyal para sa AI. Mula ngayon at sa hinaharap, babalik pa rin sa parehong bar at AI ang mga isusulat ko.

May isa pa akong napagpasyahan tungkol sa pagsusulat. Hindi ko inaanunsyo ang mga hindi pa tapos na bagay na may "malapit na." Tinatapos ko ito, gumagawa ng pahina ng pagpapakilala, at saka lang inilalabas. Naniniwala akong ang pagsunod sa ayos na iyon ang nagbibigay-tiwala sa isang maliit na kumpanya.

### 5-5 Ang Kinabukasan ng Independent na Shop

Panghuli, titipunin ko sa iisang larawan ang lahat ng isinulat ko sa librong ito.

【Larawan 5-1】Ang malaking larawan ng inilarawan ng librong ito. Binubuksan ng isang maliit na bar ang sarili nitong bintana (ang unang kuwento), at ginagawang mga tool ang mga problema nito para ibigay sa ibang bar (ang ikalawang kuwento) *(Nasa wikang Hapon ang screen.)*

Darating ang panahon na ipapahanap ng mga customer sa sarili nilang AI ang mga bar at doon magpapareserba. Noong Agosto 2026, naging posible ang pag-book ng mga restawran mula sa ChatGPT sa pamamagitan ng isang pangunahing reservation service. Lumilipat ang pasukan mula sa mga search at food review site papunta sa sariling AI ng bawat tao.

Sa puntong iyon, hindi nakikita ng AI ang bar na hindi nakalista sa pangunahing reservation service. Pero kahit wala kayo sa pangunahing serbisyo, may landas para direktang makakonekta ang isang bar sa AI. Pinili ng Tamuro ang landas na iyon sa pagbubukas ng bintanang tinatawag na MCP. Isang maliit na bar na nagbubukas ng sarili nitong bintana nang mag-isa. Iyan ang unang kuwento ng librong ito.

Magagawa ng mga may-ari ng bar na gawing mga tool ang sarili nilang problema at ibigay ang mga ito sa ibang bar. Isinilang ang Talaan ng Ilaw mula sa problema ng Tamuro na gustong ipaalam na mahuhuli ang oras ng pagsasara, at magagamit ito sa kahit anong bar. Ang kakayahang bumuo ay nagiging bagay na hindi na para lang sa ilang tao o kumpanya. Ang may-ari ng isang maliit na bar ay lumilipat mula sa panig na gumagamit ng mga tool papunta sa panig na bumubuo at nagpapamahagi nito. Iyan ang ikalawang kuwento ng librong ito.

Ang pagkakapareho ng dalawang ito ay habang mas maliit ang bar, mas kaya nitong maging natatangi at magkaroon ng sariling estilo.

Pinag-iisa ng malalaking chain ang kanilang mga sistema para maghatid ng parehong kalidad ang bawat outlet. Kabaligtaran ang Tamuro. Kalahati ang mga mag-isang customer, halos 90% ng mga reservation ay ginagawa sa mismong araw, at nag-uusap ang mga customer. Para umangkop sa katangiang iyon ng Tamuro, binuo ko nang detalyado ang reservation system, ang mga diskwento at ang chat window. Dahil hindi ito pinag-isa, matalas ito. Dahil matalas ito, nagiging dahilan ito para piliin ito ng mga customer.

At habang mas matalas ang bar, mas maraming binhi ng tool ang natatagpuan nito. Habang mas hinaharap ninyo ang katangian ng bar, mas nagiging tiyak ang mga problema ninyo. Ang mga tiyak na problema ay nagiging mga tiyak na tool. Ang mga tiyak na tool ay tumutulong sa ibang bar na may parehong problema.

Pinahintulutan ng AI ang iisang may-ari na gawin ang dalawa. Ang patalasin ang bar, at ang magbigay ng mga tool. Noon, kailangan ninyong pumili ng isa. Ngayon, magagawa ninyo ang pareho.

Siyempre, patuloy pa itong ginagawa. Patuloy pang itinataas ang pass rate ng chat window. Dinaragdagan ang manwal sa bawat pagkabigo. Nananatiling hamon kung paano palaguin ang shop sa araw. Kaunti pa rin ang mga taong nagbu-book sa pamamagitan ng AI.

Gayunpaman, naniniwala akong maliwanag ang kinabukasan ng maliit na bar. Hindi kahinaan ang pagiging maliit. Dahil maliit kami, mabilis kaming makakapag-test, mabilis na makakapag-drop, at mabilis na makakapag-ayos. Dahil maliit kami, kaya naming maging natatangi at kapansin-pansin. At ang mga problema ng matalas na bar ay nagiging mga tool at ipinapasa sa ibang maliliit na bar.

Isinulat ko ang librong ito mula sa isang bar sa Higashi-Nakano na may 19 na upuan.

## Pangwakas

Salamat sa pagbabasa hanggang dito.

Ang isinulat ko sa librong ito ay tala noong Oktubre 2026. Mabilis na nagbabago ang mga AI tool sa loob ng ilang buwan. Maaaring iba na ang anyo ng ilan sa mga mekanismong inilarawan ko pagdating ng paglalathala nito. Gayunpaman, isinulat ko ito, sa paniniwalang mananatiling kapaki-pakinabang sa ngayon ang tala kung ano ang binuo ng isang maliit na bar gamit ang AI at paano, saan ito pumalpak at ano ang natutuhan.

Ang Agenda series: https://bontallc.com/agenda?via=b2-tl-{{FMT}}

Sundan ang aking mga update: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Kung mapadpad kayo sa Higashi-Nakano, dumaan kayo sa Tamuro. Puwede kayong mag-reserve sa pamamagitan ng reservation site, sa pamamagitan ng chat window na "T-AI-MURO" sa site, at siyempre sa pamamagitan ng sarili ninyong AI.

Reservation site ng Tamuro: https://tamuroreservation.vercel.app/?src=b2-tl-{{FMT}}

Instagram ng Tamuro: https://www.instagram.com/tamuro.higashinakano/

Para sa mga gustong subukang mag-book gamit ang AI. Ang address ng koneksyon para sa MCP server ng Tamuro ay ang sumusunod na URL.

https://tamuroreservation.vercel.app/api/mcp

Sa mga setting ng inyong AI (gaya ng Claude o ChatGPT), buksan ang screen para sa pagdaragdag ng mga panlabas na tool (mga connector, MCP server) at irehistro ang URL na ito. Nag-iiba ayon sa AI at sa paglipas ng panahon ang paraan ng pagrerehistro, kaya ang pinakasiguradong paraan ay hanapin ang "MCP" o "connector" sa help ng bawat AI. Depende sa planong mayroon kayo, maaaring hindi kayo makakonekta sa MCP server na pinili ninyo mismo. Kapag naiparehistro na, itanong sa inyong AI, "May bakante ba ang Tamuro ngayong gabi?" Titingnan nito ang mga bakanteng slot at presyo at gagabayan kayo papunta sa reservation page. Kayo ang pipindot ng confirmation button.

Para sa mga bibisita pagkatapos basahin ang libro. Kapag nagre-reserve kayo, ilagay ang coupon code na "BOOK." Bibigyan namin kayo ng isang libreng inumin para sa inyong unang order. Kung pupunta kayo nang walang reservation, sabihin lang ang "Nakita ko sa libro" sa una ninyong pag-order. Ganoon ding libreng inumin ang ibibigay namin. Isa itong maliit na paraan para mabilang ko kung ilang tao ang bumisita dahil sa libro.

Puwede kayong pumasok nang walang reservation. Kahit mag-isa kayo, hindi kayo maiilang. Baka nga mauwi pa kayo sa masayang pakikipagkuwentuhan sa katabi ninyo.

Naghihintay ako sa inyo sa Tamuro, ang bar kung saan nagtitipon ang mga tao.

Raku Bonta

### Mga Sanggunian

- OpenAI Help Center, "ChatGPT — Release Notes," Agosto 10, 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (halimbawa ng MCP server sa US na nagpapahintulot sa AI na maglagay ng mga order para sa mga stock at iba pang securities) https://docs.alpaca.markets/docs/alpaca-mcp-server
- Ang debate tungkol sa "kamatayan ng SaaS": ang mga pahayag ni Satya Nadella sa BG2 podcast (Disyembre 2024), ang matinding pagbagsak ng mga software stock noong Pebrero 2026 at ang itinawag dito, at ang pagtutol ni Jensen Huang ay hinango sa mga sumusunod na ulat at komentaryo. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
