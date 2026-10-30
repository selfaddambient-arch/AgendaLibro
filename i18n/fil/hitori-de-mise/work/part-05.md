### 4-1. Ang Hirap ng Pag-update ng Wine List

Para sa may-ari ng bar o restaurant, ang pag-update ng menu book ay isang gawaing hindi kaaya-aya pero napakabigat.

Ang pinakamahirap para sa akin ay ang paggawa ng "wine list."

Tuwing may dumarating na bagong wine, kailangang gawin ang mga sumusunod.

1.  Tingnan ang label ng bote (cursive sa banyagang wika, mahirap basahin).

2.  I-type sa PC ang pangalan ng brand at ang vintage (taon) nang walang mali.

3.  Hanapin sa internet ang katangian at lasa ng wine.

4.  Sumulat ng "pagpapakilala" na hihikayat sa mga customer na basahin ito.

5.  Mag-isip ng mga putaheng bagay na bagay sa wine (pairing).

Halos imposibleng gawin ang lahat ng ito habang may hawak na diksiyonaryo, sa gitna ng abalang oras ng serbisyo. Ipinagpapaliban ko ito ng "mamaya ko na gagawin," kaya madalas na hindi na na-uupdate ang listahan ng mga inirerekomenda.

### 4-2. Kuhanan Lang ng Litrato. Ang Gulat sa "Wine List Gem"

Kaya nagpasya akong subukan ang "multimodal feature (image recognition)" ng Gemini.

Napakasimple ng paraan, kaya nakakagulat pa nga.

1.  Kuhanan ng litrato ang bote ng wine gamit ang smartphone.

2.  Ipadala ang litratong iyon sa Gemini.

3.  Magdagdag ng isang linya: "Gawin mong listahan."

Ganoon lang kasimple.

![Litrato ng label ng isang tunay na bote ng wine na kinuhanan ng smartphone](images/fig-19.jpg)

Pagkatapos, agad na binabasa ng Gemini ang impormasyon sa label mula sa litrato.

Hindi lang nito binabasa at ine-extract ang pangalan ng brand, tulad ng "Cave d'Occi Winery, Tsukimi de Ippai 2024." Naghahanap din ito sa malaking online database para sa mga katangian nito, at awtomatikong gumagawa ng kaakit-akit na paglalarawan.

Mas nakagulat pa sa akin na naglabas din ito ng "mungkahing pairing" bilang kasama.

Sa loob ng ilang segundo, lumitaw sa screen ang mga mungkahing tulad ng "Bagay ang mayamang aroma ng wine na ito sa ○○."

Ang mga oras na ginugugol ko noon sa pakikipagbuno sa diksiyonaryo ay naging isang pindot na lang ng shutter ng telepono.

### 4-3. Gumawa ng Sarili Ninyong "Gem"

Para mas pabilisin pa ang gawaing ito, ginamit ko ang isang feature na tinatawag na "Gems."

Ito ay "sarili ninyong custom na AI" na maaari ninyong ituro at itakda ang partikular na papel at mga patakaran nang maaga.

Nakakapagod ang magpaliwanag nang paulit-ulit mula sa simula tulad ng "Isa kang sommelier. Tingnan mo ang litratong ito at..."

Kaya nirehistro ko nang maaga sa Gemini ang sumusunod na "mga tagubilin (prompt)." Ito ang laman ng isip ng "sariling sommelier AI" ng bar ko.

#### Ang mga Tagubiling Aktuwal Kong Nakarehistro

> Basahin ang larawan at gumawa ng wine list sa sumusunod na format.
>
> Sa presyo, huwag gamitin ang presyo sa merkado. Kalkulahin ito batay sa presyo ng bote sa karaniwang restaurant (humigit-kumulang 2.5 hanggang 3 beses ng puhunan).
>
> Huwag gumamit ng table format. Gawin itong kasya sa isa o dalawang sheet ng A4 na papel.
>
> Sanggunian lang ang format; gawin ang listahan gamit lamang ang mga ipinasok.
>
> Ang format ay nasa ibaba.
>
> United Kingdom 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8,500 (humigit-kumulang $57)
>
>  Maputlang ginto na may kaaya-ayang bula. Bahid ng melon at pulot sa gitna ng aroma ng citrus... (ang iba ay inalis)

Ang totoo, ang ibabang kalahati ng prompt na ito, ang bahaging "format (sample)."

Hindi ko ito naisip mula sa wala.

Noong naghahanap pa ako ng impormasyon tungkol sa wine online, madalas kong maisip, "Ah, madaling intindihin ang paglalarawan ng shop na ito," o "Nakakatakam ang pagkakasulat ng site na ito," at kinokopya ko lang ang mga talatang iyon at idinidikit sa notepad, paulit-ulit.

Ibinigay ko sa Gemini ang "patchwork na memo" na iyon nang walang binago.

"Ito ang mga talatang kinopya at tinipon ko noon. Gayahin mo ang dating nito at isulat din ang tungkol sa wine sa bagong litrato."

Iyon lang ang sinabi ko.

Kahit ganoon, may tatlong paraan sa tagubiling ito na nagpapagaan ng pasanin sa shop.

① "Ang lohika ng pagkuwenta ng presyo"

Ito ang pinakamalaking nakakatipid ng oras. Dahil "presyong sisingilin ng restaurant" ang ipinapagawa ko at hindi "presyo sa merkado," kinukwenta pabalik ng AI mula sa karaniwang presyo ng bili at nagbibigay ng halagang tulad ng "¥8,500 (humigit-kumulang $57)" na puwede nang ilagay agad sa menu. (Siyempre, ang may-ari pa rin ang magpapasya sa huli, pero mas madali kapag may gabay.)

② "Hindi table format, kundi kasya sa A4 na papel"

Kung table format na tulad ng sa Excel ang lumabas, masisira ang ayos kapag idinikit ninyo sa menu book. Sa pagpapasulat dito sa "A4 menu format" mula sa simula, layon kong makakuha ng output na puwede nang i-print at gamitin nang walang pagbabago.

③ Paggamit ng text na kinopya mula sa web bilang "sample"

Sa halip na malabong hilingin na "Sumulat ka ng magandang paglalarawan," nagpapakita ako ng konkretong halimbawa (ang kinopya kong memo): "🇬🇧 bandila + pangalan ng wine + presyo + paglalarawang pumupukaw ng pandama."

Kapag may ipinakitang halimbawa sa AI, naiintindihan nito, "Ah, ito pala ang tono at istilong dapat kong sundin," at tumataas nang husto ang husay ng output. Sa teknikal na termino, tinatawag itong "few-shot prompting," pero sa esensya, kapareho ito ng "pagtuturo sa pamamagitan ng pagpapakita ng halimbawa."

At ang "likod" na iyon ay puwedeng buuin mismo ng text na nakita sa web, mga napulot na teksto sa internet, kapareho ng mga napulot na larawan.

![Ang natapos na text ng wine list na inilabas ng Gemini](images/fig-20.png)

### 4-4. Hindi Kailangang Larawan. Ang Rebolusyon ng Copy-and-Paste mula sa LINE

Ang maganda sa "Wine List Gem" na ito ay hindi lang litrato ang puwedeng ipasok.

Ang totoo, sa bar, madalas kayong mag-order sa tindahan ng alak sa pamamagitan ng LINE, hindi ba?

Pagkatapos ng order, ganitong mensahe ang dumarating mula sa tindahan ng alak.

> "Maraming salamat po palagi. Natanggap na namin ang order ninyo ayon sa sumusunod.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 bote
>
> ・Ridgeview Bloomsbury 6 na bote
>
> ・○○ (bagong wine) 2 bote
>
> Idedeliver namin bukas."

Isang araw, bigla kong naisip: "Hindi ba puwedeng gamitin ko na lang ang text na ito nang ganito?"

Bilang pagsubok, kinopya ko ang LINE message na ito gamit ang daliri at diretsong inihagis sa Gemini.

Perpekto ang resulta.

Kinilala ng Gemini ang mga "pangalan ng produkto" lang sa LINE message, naghanap ng impormasyon online, at gumawa ng listahan sa nakagawiang format (bandila + presyo + paglalarawan).

Ibig sabihin, hindi ko na kailangang hintayin ang pagdating ng mga bote para kuhanan ng litrato.

Sa mismong sandali ng pag-order, sa pamamagitan lang ng copy at paste sa loob ng telepono, tapos na ang menu list bago pa dumating ang mga produkto.

Hindi na kailangang magbukas ng PC, hindi na kailangang buksan ang camera.

Sa sulok ng kusina, o habang nasa tren, natatapos ang gawain gamit lang ang telepono.

Hindi ba ito ang "tunay na episyensiya" na dapat makuha ng isang may-ari na mag-isa lang?

### 4-5. Ang Mungkahi ng AI × ang Pasya ng Shop (Realidad)

Gayunpaman, hindi ko basta tinatanggap nang walang pagsusuri ang mga mungkahi ng AI. Ang mahalaga rito ay ang "paghuhusga ng tao sa shop."

Minsan, ito ang iminungkahi ng AI na ipares sa isang wine:

AI: "Para sa red wine na ito, perpektong pairing ang roast duck na may orange sauce."

Magandang mungkahi, pero sa kasamaang-palad, wala nang duck sa refrigerator ng shop nang araw na iyon.

Hindi ko iniisip na, "Sinabi ng AI, kaya kailangan kong bumili ng duck." Ganito ang takbo ng isip ko:

Ako (sa shop): "Wala tayong duck, pero may dumating ngayong magandang free-range na manok. Mayaman din ang taba at linamnam nito tulad ng duck, kaya iihawin ko ang manok na ito hanggang malutong ang balat at ipapares ko sa sarsang may lasang orange, tulad ng sinabi ng AI."

"Ang kaalaman ng AI (bagay ang duck at orange)" × "ang imbentaryo ng shop (may manok tayo)" = "bagong item sa menu na tiyak at makatotohanan."

Ang kombinasyong ito ang tunay na kasiyahan sa pagbuo ng menu kasama ang AI.

Ibinibigay ng AI ang sagot na nasa aklat, pero hindi nito alam kung ano ang laman ng refrigerator ngayong araw. Ang pagpuno sa puwang na iyon ay trabaho ninyo bilang may-ari.

### 4-6. Ang Huling Hakbang: Hindi Kayang Tumikim ng AI

May isa pang bagay na hindi dapat ipaubaya sa AI kailanman.

Iyon ay ang pagtikim na ginagawa ninyo bago ilabas ang anuman sa customer.

Ang mga paglalarawan at pairing na isinusulat ng AI ay batay sa "pangkalahatang datos mula sa buong mundo."

Pero buhay na bagay ang wine. Kahit iisang label, nag-iiba ang lasa depende sa vintage at sa paraan ng pag-iimbak.

Minsan, sumulat ang AI ng paglalarawan para sa isang white wine: "Sariwa, magaan, at dry na wine. Perpekto sa seafood carpaccio."

Pero nang buksan ko ang bote at tikman, mas hinog at may edad ito kaysa inasahan ko, na may mayaman at parang pulot na lasa.

"Kung ihahain ko ito bilang 'magaan at dry na wine,' madidismaya ang customer... Mas babagay ito sa manok na may cream sauce kaysa sa carpaccio."

Agad kong itinama ang text na ginawa ng Gemini.

- Bago (AI): "Sariwa at magaan. Maganda para sa appetizer"

- Pagkatapos (tao): "Mayaman at malalim ang lasa dahil sa pagka-edad nito. Sapat ang lakas para sabayan ang main course"

Ang AI ang gumagawa ng 90% ng draft, at ang tao ang tumitikim at nagdaragdag ng "huling 10% (ang kaluluwa)."

Responsibilidad ito ng may-ari ng restaurant, at isang bagay na hinding-hindi kayang gayahin ng AI.

Hindi "dahil sinabi ng AI," kundi "dahil ininom ko at masarap."

Para makapaghain nang may ganoong kumpiyansa, hanggang ngayon ay tinitikman ko pa rin ang bagong bukas na wine, hawak sa isang kamay ang listahang ginawa ng AI.

#### Kolum 3: Mga Tip sa Pagkuha ng Litrato para "Tama" ang Makita ng AI

~ Tulad ng pagpapakita ng label sa isang sommelier ~

Kapag nagpapadala kayo ng litrato sa Gemini, may ilang maliliit na paraan na makapagpapahusay nang husto sa pagkilala nito sa nakikita.

1.  Iwasan ang silaw: Madaling sumalamin ang liwanag sa mga label ng bote, kaya bahagyang baguhin ang anggulo, o gumawa ng anino gamit ang katawan ninyo habang kumukuha.

2.  Kumuha ng ilang litrato at ipadala nang sabay: Para sa mga bagay tulad ng laman ng refrigerator, magpadala ng malawak na kuha at mga close-up nang magkasama, at makikilala ng AI kahit ang mga item sa mga blind spot.

3.  Ituro gamit ang daliri: Nakakatulong din na ituro ang bahaging gusto ninyong tingnan ng AI habang kumukuha ng litrato. Maglagay ng tulad ng "Itinuturo ko ito gamit ang daliri ko" sa prompt. Katulad ito ng pagturo sa menu sa restaurant sa ibang bansa.

## Kabanata 5: Mga Aplikasyon - Pagsusuri ng Negosyo at Pagpapabuti ng Kita

~ Hukayin ang "di-nakikitang minahan ng ginto." Isang management meeting kasama ang inyong AI consultant ~

