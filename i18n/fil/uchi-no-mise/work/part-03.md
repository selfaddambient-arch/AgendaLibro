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

