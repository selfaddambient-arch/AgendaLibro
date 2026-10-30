## Bölüm 4: Uygulama Bölüm 2 - Günlük İşleri Daha Verimli Hâle Getirmek (Çok Kipli Yapay Zekâ Kullanarak)

~"Sıkıcı veri girişini" tek bir akıllı telefonla bitirin~

### 4-1. Şarap Listesini Güncellemenin Derdi

Bir bar ya da restoran sahibi için menü kitapçığını güncellemek gösterişsiz ama ağır bir yüktür.

Beni en çok zorlayan şey "şarap listesi" hazırlamaktı.

Her yeni şarap geldiğinde şu işler gerekir.

1.  Şişenin etiketine bakmak (yabancı dilde, okunması zor el yazısı gibi yazılar).

2.  Marka adını ve yıl bilgisini (üretim yılını) bilgisayara hatasız yazmak.

3.  Şarabın özelliklerini ve tadını internetten araştırmak.

4.  Müşterilerin okumak isteyeceği bir "tanıtım" yazmak.

5.  Şaraba yakışan yemekleri (eşleşmeleri) düşünmek.

Bunların hepsini, yoğun servisin aralarında elde bir sözlükle yapmak neredeyse imkânsız. "Sonra yaparım" diye ertelerdim ve önerilen liste çoğu zaman hiç güncellenmeden kalırdı.

### 4-2. Sadece Fotoğraf Çekin. "Şarap Listesi Gem"inin Şaşırtıcı Gücü

Bu yüzden Gemini'nin "çok kipli özelliğini (görüntü tanıma)" denemeye karar verdim.

Yöntem o kadar basit ki insan neredeyse şaşırıyor.

1.  Akıllı telefonunuzla şarap şişesinin fotoğrafını çekin.

2.  Bu fotoğrafı Gemini'ye gönderin.

3.  Bir satır ekleyin: "Liste yap."

Hepsi bu.

![Akıllı telefonla çekilmiş gerçek bir şarap şişesi etiketi fotoğrafı](images/fig-19.jpg)

Gemini hemen fotoğraftaki etiket bilgilerini okuyor.

"Cave d'Occi Winery, Tsukimi de Ippai 2024" gibi marka adını yalnızca yazıya dökmekle kalmıyor, aynı zamanda devasa bir çevrimiçi veri tabanında özelliklerini arıyor ve çekici bir açıklamayı otomatik olarak üretiyor.

Beni daha da şaşırtan şey, "eşleşme önerilerini" de bir arada vermesiydi.

"Bu şarabın zengin aroması ○○ ile uyum sağlar" gibi öneriler birkaç saniye içinde ekranda belirdi.

Sözlükle boğuşarak harcadığım saatler, telefonun deklanşörüne tek bir tıklamaya inmişti.

### 4-3. Kendi "Gem"inizi Yapmak

Bunu çarpıcı biçimde daha verimli kılmak için "Gem" adlı bir özelliği kullandım.

Yapay zekâya belirli bir rolü ve kuralları önceden ezberletebileceğiniz, "kendinize ait özel bir yapay zekâ özelliği" bu.

Her seferinde baştan "Sen bir sommelier'sin. Bu fotoğrafa bak ve..." diye anlatmak zahmetli.

Bu yüzden Gemini'ye aşağıdaki "talimatları (istemi)" önceden kaydettim. Bu, barımın "özel sommelier yapay zekâsının" kafasının içi.

#### Gerçekten Kayıtlı Olan Talimatlarım

> Görüntüyü oku ve aşağıdaki biçimde bir şarap listesi oluştur.
>
> Fiyatlar için piyasa fiyatlarını kullanma. Tipik bir restoranda şişe fiyatı olacağını varsayarak hesapla (maliyetin yaklaşık 2,5 ila 3 katı).
>
> Tablo biçimi kullanma. A4 kâğıdın bir ya da iki sayfasına sığacak şekilde oluştur.
>
> Biçim yalnızca bir referanstır; listeyi yalnızca girilenleri kullanarak oluştur.
>
> Biçim aşağıdadır.
>
> Birleşik Krallık 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8.500 (yaklaşık $57)
>
>  Hoş köpükleriyle soluk altın rengi. Narenciye aromaları arasında kavun ve bal tonları... (devamı çıkarıldı)

Aslında bu istemin alt yarısı, yani "biçim (örnek)" kısmı.

Onu sıfırdan ben bulmadım.

Daha önce internette şarap bilgisi ararken "Ah, bu dükkânın açıklaması anlaşılır" ya da "Bu sitenin yazış biçimi şarabı lezzetli gösteriyor" diye düşünür ve bu tür pasajları defalarca bir not defterine kopyalayıp yapıştırırdım.

O "yama işi notu" olduğu gibi Gemini'ye fırlattım.

"Bunlar bir süre önce kopyalayıp topladığım pasajlar. Bu havayı taklit et ve yeni fotoğraftaki şarabı da böyle yaz."

Ona söylediğim tek şey buydu.

Buna rağmen bu talimat, sahadaki yükü azaltan üç püf noktası içeriyor.

① "Fiyat hesaplama mantığı"

Bu, en büyük zaman kazandıran şey. "Piyasa fiyatı" yerine "bir restoranın isteyeceği fiyatı" vermesini istediğim için yapay zekâ tipik alış fiyatlarından geriye doğru hesaplıyor ve doğrudan menüye girebilecek "¥8.500 (yaklaşık $57)" gibi bir rakam veriyor. (Elbette son karar işletmecinindir, ama bir ölçü olması işleri kolaylaştırıyor.)

② "Tablo biçimi değil, A4 kâğıda sığacak"

Çıktı Excel gibi bir tablo biçiminde gelirse menü kitapçığına yapıştırdığınızda düzen bozulur. Baştan "A4 menü biçiminde" yazdırarak, basılıp olduğu gibi kullanılabilecek bir çıktıyı hedefliyorum.

③ Kopyala-yapıştırla alınan web metnini "örnek" olarak kullanmak

"Güzel bir açıklama yaz" diye belirsizce istemek yerine, somut bir örnek gösteriyorum (kopyalayıp yapıştırdığım notum): "🇬🇧 bayrağı + şarap adı + fiyat + duyusal bir açıklama."

Bir yapay zekâya örnek gösterildiğinde "Ah, demek yazmam gereken ton ve tarz bu" diye anlıyor ve çıktının doğruluğu fırlıyor. Teknik terimle buna "few-shot prompting" deniyor, ama özünde "yaparak gösterip örnekle öğretmekle" aynı şey.

Ve o "örnek", internetten bulunmuş bir fotoğrafın yazılı karşılığı olan bulunmuş metinden de gayet iyi oluşturulabilir.

![Gemini'nin çıktısı olan bitmiş şarap listesi metni](images/fig-20.png)

### 4-4. Görüntü Bile Olması Gerekmez. LINE'dan Kopyala-Yapıştır Devrimi

Bu "Şarap Listesi Gem"inin güzel yanı, girdinin fotoğraflarla sınırlı olmaması.

Aslında barda içki satıcısına siparişleri sık sık LINE üzerinden veriyorsunuz, değil mi?

Sipariş tamamlandığında içki satıcısından şöyle bir mesaj gelir.

> "Her zamanki gibi teşekkür ederiz. Siparişinizi aşağıdaki şekilde aldık.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 şişe
>
> ・Ridgeview Bloomsbury 6 şişe
>
> ・○○ (yeni şarap) 2 şişe
>
> Yarın teslim edeceğiz."

Bir gün aniden aklıma geldi: "Bu metni olduğu gibi kullanamaz mıyım?"

Deneme olarak bu LINE mesajını parmağımla kopyaladım ve doğrudan Gemini'ye attım.

Sonuç kusursuzdu.

Gemini, LINE mesajındaki yalnızca "ürün adlarını" tanıdı, internette bilgi aradı ve alışılmış biçimde (bayrak + fiyat + açıklama) bir liste yaptı.

Yani şişelerin gelmesini bekleyip fotoğraf çekmeme bile gerek yok.

Siparişi verdiğim anda, sadece telefonumun içinde kopyala-yapıştır yaparak, ürünler daha gelmeden menü listesi bitiyor.

Bilgisayar açmaya gerek yok, kamera başlatmaya gerek yok.

Mutfağın bir köşesinde ya da trende, iş yalnızca telefon işlemleriyle bitiyor.

Tek başına çalışan bir işletmecinin elde etmesi gereken "gerçek verimlilik" bu değil mi?

### 4-5. Yapay Zekânın Önerisi × Sahanın Yargısı (Gerçeklik)

Yine de yapay zekânın önerilerini körü körüne kabul etmiyorum. Burada önemli olan, "sahadaki insan yargımız".

Bir seferinde yapay zekâ bir şaraba eşlik edecek şu öneriyi yaptı:

Yapay zekâ: "Bu kırmızı şarap için portakal soslu kızarmış ördek mükemmel bir eşleşme."

Harika bir öneri, ama maalesef o gün dükkânın buzdolabında ördek yoktu.

"Yapay zekâ öyle diyor, o halde ördek almalıyım" diye düşünmem. Ben şöyle düşünüyorum:

Ben (sahada): "Ördeğimiz yok ama bugün iyi serbest gezen tavuk geldi. Ördekle kıyaslanabilir yağı var, bu yüzden bu tavuğu derisi çıtır olana kadar kızartıp, tıpkı yapay zekânın dediği gibi portakal aromalı bir sosla bitireceğim."

"Yapay zekânın bilgisi (ördek ve portakal uyumlu)" × "sahadaki stok (elimizde tavuk var)" = "tereddütsüz ve gerçekçi yeni bir menü kalemi."

Bu birleşim, yapay zekâyla menü geliştirmenin gerçek zevkidir.

Yapay zekâ size ders kitabı cevabını verir ama bugün buzdolabında ne olduğunu bilmez. Bu boşluğu doldurmak, işletmeci olarak sizin işiniz.

### 4-6. Son Kilometre: Yapay Zekâ Şarabı "Tadamaz"

Yapay zekâya asla bırakmamanız gereken bir şey daha var.

Müşteriye herhangi bir şey çıkmadan önce yaptığınız tadımdır.

Yapay zekânın yazdığı açıklamalar ve eşleşmeler "dünyanın genel verilerine" dayanır.

Ama şarap canlı bir şeydir. Aynı etiket bile üretim yılına ve nasıl saklandığına göre tat değiştirir.

Bir keresinde yapay zekâ bir beyaz şarap için şu açıklamayı yazdı: "Ferah, hafif, sek bir şarap. Deniz ürünlü carpaccio ile mükemmel."

Ama şişeyi gerçekten açıp tattığımda, beklediğimden daha olgundu ve zengin, bal gibi tonları vardı.

"Bunu 'hafif, sek bir şarap' diye sunarsam müşteri hayal kırıklığına uğrar... Carpaccio'dan çok kremalı soslu tavukla daha iyi gider."

Gemini'nin ürettiği metni hemen düzelttim.

- Önce (Yapay zekâ): "Ferah ve hafif. Başlangıçlar için iyi"

- Sonra (insan): "Olgunlaşmadan gelen zengin, dolgun gövde. Ana yemeğin karşısında durabilecek güçte"

Yapay zekâ taslağın %90'ını yapar, insan tadar ve "son %10'u (ruhu)" ekler.

Bu kontrol bir restoran işletmecisinin sorumluluğudur ve yapay zekânın asla taklit edemeyeceği bir şeydir.

"Yapay zekâ öyle dediği için" değil, "içtim ve lezzetliydi" diye.

Müşteriye bu güvenle sunmak için, bir elimde yapay zekânın yaptığı listeyle, yeni açılmış şarabı bugün de bizzat tadıyorum.

#### Not Kutusu 3: Yapay Zekânın Bir Şeyi "Doğru" Görmesi İçin Fotoğraf Çekme İpuçları

~ Bir sommelier'ye etiket gösterir gibi ~

Gemini'ye fotoğraf gönderirken, birkaç küçük püf noktası, yapay zekânın gördüğünü ne kadar iyi tanıdığını çarpıcı biçimde artırabilir.

1.  Yansımadan kaçının: Şişe etiketleri ışığı kolay yansıtır; bu yüzden açıyı biraz değiştirin ya da çekerken vücudunuzla gölge düşürün.

2.  Birkaç çekim yapıp birlikte gönderin: Buzdolabının içi gibi şeyler için geniş bir çekimle yakın çekimleri birlikte gönderirseniz yapay zekâ kör noktalardaki kalemleri bile tanır.

3.  Parmağınızla işaret edin: Fotoğrafı çekerken yapay zekânın bakmasını istediğiniz yeri işaret etmek de işe yarar. İstemin içine "Parmağımla işaret ediyorum" gibi bir şey koyun. Yurtdışında bir restoranda menüyü işaret etmekle aynı şey.
