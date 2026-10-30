# Barımıza Göre Yapıldı

19 Koltuklu Bir Barın Sahibi, Rezervasyondan Araçlara Kadar Her Şeyi Yapay Zekâyla Nasıl Kurdu

Raku Bonta

Agenda serisi: https://bontallc.com/agenda?via=b2-tr-{{FMT}}

Tamuro'nun Instagram'ı: https://www.instagram.com/tamuro.higashinakano/

Tamuro'nun rezervasyon sitesi: https://tamuroreservation.vercel.app/?src=b2-tr-{{FMT}}

## Giriş

Bu kitap, Tokyo'nun Higashi-Nakano semtinde *(Shinjuku'nun hemen batısında, Tokyo'nun batı yakasındaki bir yerleşim semti)* 19 koltuklu bir barın sahibinin dükkânı yapay zekânın yardımıyla nasıl işlettiğinin sade bir kaydıdır.

Barın adı "Tamuro." Ad, insanların bir araya geldiği yer anlamına geliyor. Kasım 2018'de, tezgâhta 11 tabure ve tatami odasında 8 oturma yeriyle küçük bir mekân olarak açıldı. Gündüzleri aynı mekânda bir çalışan "Quatre Épices" adlı bir hamburger köri restoranı işletiyor.

Önceki kitabım *Yapay Zekâ Müdür Yardımcısı*'nda üretken yapay zekânın kendisini anlattım. Aradan geçen bir yıl kadar sürede yapay zekâ, soruları yanıtlayan bir araçtan sizin yerinize iş yapan bir araca dönüştü. Ona talimat veriyorsunuz; programı yazıyor, test ediyor, hatalarını düzeltiyor ve işi bitiriyor. Bu tür yapay zekâya ajan tabanlı yapay zekâ diyoruz.

Ajan tabanlı yapay zekâyı kullanarak Tamuro'nun rezervasyon sistemini kendim kurdum. Fiyat artışını dengeleyen bir indirim sistemi kurdum. Müdavim kazandırmaya yönelik bir sistem kurdum. Müşterilerin sorularını yanıtlayan bir yapay zekâ kurdum. Sonunda bir müşterinin kendi yapay zekâsından Tamuro'ya soru sorup ardından rezervasyon yapabileceği noktaya geldim.

Ayrıca kendi dükkânım için yaptığım kullanışlı araçları, başka dükkânların da kullanabileceği biçime getirip ayda birkaç yüz yenden başlayan fiyatlarla sunmaya başladım. İşte Agenda serisi tam olarak bu.

Bu kitap, yol boyunca neler kurduğumu, nerede başarısız olduğumu ve neleri yeniden öğrenmem gerektiğini anlatıyor. Yalnızca başarı hikâyeleri değil. Çalışıyor diye anlık bir hevesle bir şeyler kurmaya devam ettim ve çelişkiler birikti. Sonradan müşterilerin kişisel bilgilerinin dışarıdan okunabildiğini fark ettim. Yapay zekâ, dükkânın hiç belirtmediği bilgileri yazdı. Bu başarısızlıkları olduğu gibi kitaba aldım.

### Bu Kitap Nasıl Okunur?

Bu kitap beş bölümden oluşuyor.

| Bölüm | İçerik | Kimler için en uygun |
| --- | --- | --- |
| Bölüm 1 | Yapay Zekâ Üzerinden Rezervasyon Alan Bir Dükkân (rezervasyon sisteminin iş yönü) | Herkes |
| Bölüm 2 | Rezervasyon Sisteminin Perde Arkası (teknik) | Sistem kuranlar ve teknolojiyi merak edenler |
| Bölüm 3 | Dükkânımızın Araçlarını Başka Dükkânlara Dağıtmak (Agenda serisinin iş yönü) | Herkes |
| Bölüm 4 | Ürünleri Tek Başına Kurmak İçin Bir Sistem (teknik) | Sistem kuranlar ve teknolojiyi merak edenler |
| Bölüm 5 | Küçük Dükkânların Geleceği | Herkes |

2. ve 4. bölümler teknik olup daha çok uzmanlık terimi kullanıyor. Her birinin başında ana noktalar üç satırlık bir özetle veriliyor; teknoloji ilginizi çekmiyorsa yalnızca onları okuyup sonraki bölüme geçin. 1., 3. ve 5. bölümleri sırayla okursanız hikâye yine tek bir çizgi olarak bir bütün oluşturur.

Mümkün olduğunca her teknik terimin yanına sade bir açıklama ekledim. Hiç program yazmamış olsanız bile, bir dükkânı yapay zekâyla işletmenin ne anlama geldiğine dair bir fikir edinmenizi umuyorum.

### Yazar Hakkında

Yaklaşık 16 yıl BT sektöründe, çoğunlukla sistem planlaması alanında ve sahadaki insanlarla yazılım firmaları arasında koordinatör olarak çalıştım, sonra yeme içme işine girdim. Yani bu, hiç kod satırı yazmamış birinin her şeyi tek başına yapay zekâyla kurduğu bir hikâye değil. Bu konuda dürüst olmak istiyorum.

Yine de artık bizzat dükkânda çalışırken kendi başıma, bir zamanlar bir ekip ve sermaye gerektiren ölçekte bir şeyi kurup işletebiliyorum. Birkaç yıl önce bu düşünülemezdi. Bu değişimin gerçekliğini mümkün olduğunca somut biçimde anlatmak istiyorum.

### Bu Kitap Nasıl Yapıldı?

Bu kitabı da yapay zekâyla yaptım. Günlük geliştirme çalışmalarım sırasında tuttuğum kayıtlardan yola çıkarak taslakları yapay zekâ yazdı; ben okudum, düzelttim ve kararları verdim. Resim olarak kullanılan ekran görüntülerini de yapay zekâya aldırdım.

Hepsini okudum, ama yapay zekânın yazdığı metne doğru olmayan şeyler karışmış olabilir. Ana metinde de söylediğim gibi, yapay zekâ "yaptım" der ve bunu kontrol etmek insanın işidir. Gözümden kaçmış hatalar bu kitapta olabilir.

Ayrıca yapay zekâ araçlarının ve hizmetlerinin özellikleri birkaç ay içinde değişiyor. Bu kitapta anlatılan adımlar, fiyatlar ve her şirketin destek durumu Ekim 2026 itibarıyladır. Kendiniz denerken lütfen o günkü resmî bilgileri kontrol edin.

Bir hata görürseniz note'ta veya X'te bana bildirirseniz sevinirim. Fark edildikçe düzelteceğim.

### Bu Kitabın Sunduğu Üç Kapı

Bu kitap PDF olarak, note'ta ve Google Play'de ücretsiz okunabilir. (Yalnızca Kindle'da mağazanın kuralları gereği asgari bir fiyat var.) Karşılığında, kitabı bitirdikten sonra gidebileceğiniz üç yer hazırladım. Bunlardan biri bile işinize yararsa bu kitabı yazmaya değmiş olur.

1. Kendi dükkânınızda deneyin. Agenda serisine ücretsiz defterle başlayabilirsiniz. https://bontallc.com/agenda?via=b2-tr-{{FMT}}
2. Yaptıklarımı takip edin. Yapacağım sonraki araçları ve dükkânın gündelik hayatını note ve X'te yazıyorum. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Tokyo'ya yolunuz düşerse Tamuro'yu ziyaret edin. Higashi-Nakano İstasyonu'nun doğu çıkışından yürüyerek bir dakika. Rezervasyonsuz girebilirsiniz. Rezervasyon sitesi https://tamuroreservation.vercel.app/?src=b2-tr-{{FMT}}

## Bölüm 1: Yapay Zekâ Üzerinden Rezervasyon Alan Bir Dükkân

### 1-1 "Bu Akşam Açık Bir Yer Var mı?" Yapay Zekâya Soruyorsunuz

Bir cuma akşamı, işi yeni bitirmiş biri akıllı telefonuyla konuşuyor.

"Higashi-Nakano'da bu akşam tek başıma içebileceğim bir yer var mı? Çok gürültülü olmasın."

Cevap veren bir arkadaş değil. O kişinin günlük hayatta kullandığı yapay zekâ. Yapay zekâ aday dükkânları sıralıyor, her birinin havasını anlatıyor, bu akşamki müsait saatleri ve fiyatları söylüyor. Biri dikkatini çekerse doğrudan rezervasyon ekranına geçebiliyor.

Bu, gelecekle ilgili bir hikâye değil.

10 Ağustos 2026'da OpenAI, ChatGPT'ye bir restoran rezervasyonu özelliği ekledi. Resmî sürüm notlarına göre OpenTable, Resy ve Yelp rezervasyon hizmetleriyle bağlantı kuruyor ve uygun rezervasyon saatleri doğrudan ChatGPT'nin cevaplarında görünüyor. Seçenekleri daraltmak için sorulara da cevap verebiliyor ve size uygun bir saati seçtiğinizde doğrudan rezervasyona geçebiliyorsunuz. Dünya genelinde OpenTable'ı, ABD'de Resy'yi, ABD ve Kanada'da Yelp'i kapsıyor.

Başka bir deyişle, insanların yemek yeri bulmak için kullandığı giriş kanalı arama motorlarından ve restoran inceleme sitelerinden "kendi yapay zekâsına" kaymaya başlıyor.

Ama bir koşul var. ChatGPT üzerinden yalnızca büyük rezervasyon hizmetlerine kayıtlı dükkânlara rezervasyon yapabilirsiniz. Orada listelenmeyen küçük dükkânlar yapay zekâya görünmezdir.

Peki büyük rezervasyon hizmetlerini kullanmayan Higashi-Nakano'daki 19 koltuklu bir bar ne yapmalı?

Tamuro farklı bir yol seçti. Büyük hizmetleri araya sokmadan kendi rezervasyon sistemini doğrudan yapay zekâya bağladı.

Bir müşteri kendi ChatGPT'sine ya da Claude'una "Tamuro'da bu akşam yer var mı?" diye sorduğunda, yapay zekâ doğrudan Tamuro'nun rezervasyon sistemini sorguluyor, müsait saatleri ve fiyatları kontrol ediyor ve cevap veriyor. Koşullar netleşince müşteriyi, kişi sayısı ile tarih ve saat önceden doldurulmuş hâlde Tamuro'nun rezervasyon sayfasına yönlendiriyor. Son onay düğmesine müşteri kendisi basıyor.

"Yapay zekâ ile bir dükkânın sistemi arasındaki bu bağlantı noktasına" MCP sunucusu deniyor. MCP, yapay zekânın dış araçları ve verileri kullanmasını sağlayan ortak bir anlaşmalar bütünü olan Model Context Protocol'ün kısaltması. Ayrıntıları 2. bölümde anlatıyorum.

Büyük rezervasyon hizmetleri de aslında sonunda müşteriyi kendi ekranlarına devreder. Kredi kartı gerektiren rezervasyonlarda işlem OpenTable'ın ekranında tamamlanır; rezervasyondan sonraki değişiklikler ya da iptaller her hizmetin kendi tarafında yürütülür. Yapay zekâ giriş kanalıdır, rezervasyon hizmetinin ekranı ise onaylandığı yerdir. Tamuro'nun yaptığı da aynı yapıya sahip. Tek fark, araya büyük bir şirketin girmemesi.

Bu sistemi kuran da dışarıdan bir geliştirme şirketi değildi. İşletme sahibi olan bendim. Yapay zekâya talimat verdim, programları yapay zekâya yazdırdım ve testleri yapay zekâya yaptırdım.

Elbette buraya en başta varmadım. Çok basit bir rezervasyon formuyla başladı. Sonra bir fiyat artışı geldi, sonra indirim fikirleri, sonra müdavimleri yetiştirme sistemi, sonra başarısızlıklar ve yeniden kurma.

Önce Tamuro'nun nasıl bir yer olduğunu beş satırda anlatayım. Higashi-Nakano İstasyonu'nun doğu çıkışından yürüyerek bir dakika. 19 koltuk; 11'i tezgâhta, 8'i tatami odasında. Müşterilerin yaklaşık yarısı yalnız geliyor ve tezgâh, yandaki kişiyle sohbete başlamayı kolaylaştırıyor. Yemekler dört meze ve bir ana yemeğin birleşiminden oluşuyor; en çok sevilen yemek tatlı, sarımsaklı bir tonteki (domuz bifteği). Şaraplar ağırlıklı olarak İspanya ve İtalya'dan, ayrıca yaklaşık 20 çeşit Japon butik cini var. Rezervasyonsuz girebilirsiniz.

Hedeflediğim bir şeyi de söyleyeyim. Yalnızca rezervasyon almak istemedim. Küçük bir dükkânın bile tanınma, ziyaret ettirme ve yeniden geri getirme akışının tamamını kendi eliyle kurabilmesini istedim. Bu bölümde geçen indirimler, e-postalar ve sohbet penceresi, hep bu tek amaca hizmet eden parçalar.

Bu bölümde zamanı geri saracağım ve Tamuro'nun rezervasyon sisteminin nasıl büyüdüğünün izini süreceğim.

【Şekil 1-1】ChatGPT'den Tamuro'nun MCP sunucusuna bağlandıktan sonraki ekran (10 Ekim 2026). Dükkânın bilgilerini okuyor ve müsait saatleri, menüleri, fiyatları ve rezervasyon sayfasına yönlendirmeyi yapabileceğini söylüyor *(Ekran Japonca.)*

### 1-2 Başlangıç Noktası: Sadece Rezervasyon Almak

[Tamuro'nun rezervasyon sitesi](https://tamuroreservation.vercel.app/?src=b2-tr-{{FMT}}) başta çok basitti. Bir tarih, saat ve kişi sayısı seçiyorsunuz, bir ad ve iletişim bilgileri giriyor ve gönderiyorsunuz. Dükkâna bir bildirim ulaşıyor. Hepsi bu.

İlk temeli Google'ın yapay zekâ geliştirme aracıyla (Antigravity) kurdum. Aklıma gelen her özelliği yapay zekâya anlattım ve bir şey çalıştığında sonrakine geçtim. Buna vibe coding deniyor (aklınıza gelen her şeyi yapay zekâya söyleyip hisle yaptırmak).

O zamanki benim için art arda gelen sürprizlerdi. Bir ekranın düzenini sözcüklerle anlatın, dakikalar içinde şekillenir. Bir takvim istediğinizi söyleyin, bir takvim belirir. Dükkânı işletirken arada kalan boşluklarda bir rezervasyon sitesi ortaya çıktı.

Tamuro, rezervasyonsuz girebileceğiniz bir yer. Aslında rezervasyonların çoğu aynı gün yapılıyor ve pek çok müşteri doğrudan içeri giriyor. Yine de müşterilerle ziyaretlerinden önce bağ kurabileceğim bir yol istediğim için bir rezervasyon sistemi kurdum. Biri rezervasyon yaptığında adı ve iletişim bilgileri kalır. İletişim bilgileri kalınca onları yeniden gelmeye davet edebilirim.

Bir rezervasyon sistemi yalnızca rezervasyon kabul eden basit bir araç değildir. Müşteriyle ilişkinin giriş kanalı olur. Bu fikir daha sonra indirim sistemine ve müdavimleri yetiştirme sistemine yol açtı.

Ama içgüdüyle kurulmuş bir temel için sonradan büyük bir bedel ödedim. Bunu 2. bölümde yazacağım.

### 1-3 Fiyat Artışını ve İndirimleri Aynı Anda Kurmak

Bir restoran ya da bar için fiyat artışı kaçınılmaz bir karardır. Malzeme, enerji ve işçilik sürekli pahalanıyor. Tamuro da fiyatları artırdı. Her menüyü yaklaşık ¥400–¥500 (yaklaşık $2,7–$3,3) artırdım.

Artış büyüktü, bu yüzden olduğu gibi duyursam müdavimlerin uzaklaşacağı açıktı. Bu yüzden fiyat artışıyla aynı anda rezervasyon sistemine bir indirim sistemi yerleştirmeye karar verdim. Bu yalnızca işleri ucuzlatmıyor. Dükkâna yararlı biçimde davranan müşterileri indirimle ödüllendiriyor.

Birincisi grup indirimi. Gruptaki kişi sayısı arttıkça kişi başı fiyat düşüyor. Tamuro'nun müşterilerinin yaklaşık yarısı yalnız geliyor, ama gruplar hâlinde gelirlerse dükkânın satışları çok büyüyor. İndirim düşüldükten sonra bile dükkân kazançlı çıkıyor. Müşteriler için de arkadaşlarını davet etmek için bir sebep. Nitekim rezervasyon sitesinin kişi sayısı indirimini kullanarak gruplar hâlinde gelen müşterilerin sayısı arttı.

İkincisi erken rezervasyon indirimi. Bir hafta öncesine kadar rezervasyon yaparsanız %2, iki hafta öncesine kadar yaparsanız %4 indirim alıyorsunuz. Tamuro rezervasyonlarının çoğu aynı gün yapıldığı için gelecek günleri öngöremiyorum. Erken rezervasyon indirimi gelecekteki satışları sabitlemenin bir mekanizması. Yağmurlu ve soğuk günlerde rezervasyonlar zaten gelmişse dükkân (ve mutfak) hazırlığını gönül rahatlığıyla yapabilir.

Üçüncüsü, toplu alım mekanizması da kurdum. Belirli bir tarih ve saatte belirli sayıda kişi toplanırsa, indirimli fiyatla bir set menü sunulacaktı. Birbirini tanımayan insanların aynı anda bir araya geldiği Tamuro ruhuna uygun bir mekanizma olması gerekiyordu.

Ama toplu alım planı hiç kullanılmadı. Sıfır sonuç. Ağustos 2026'da bu planı durdurdum ve bir daha kullanmamaya karar verdim.

Yaptığınız bir şeyi atmak israf gibi geliyor. Ama yapay zekâyla kuruyorsanız kurmanın maliyeti ve zamanı küçüktür. Küçük kurun, deneyin, işe yaramazsa atın. Bu hızın, bir dükkânı yapay zekâyla işletmenin en büyük avantajı olduğuna inanıyorum.

Fiyatlandırmada ince bir taktik daha var. Planların arasına bilerek pahalı bir premium plan koyuyorum. Premium planı neredeyse kimse seçmese de sorun değil. Yanında pahalı bir plan olunca standart olan uygun görünüyor. Çıpa (karşılaştırma için bir referans noktası) denen şeyin rolünü oynuyor.

【Şekil 1-7】Kişi sayısı arttıkça kişi başı fiyat düşüyor (1, 4 ve 6 kişilik karşılaştırma)

### 1-4 Müdavimlerle Bağı Besleyen Bir Sistem

Rezervasyon sisteminde adlar ve iletişim bilgileri kalınca, bir sonraki yapmak istediğiniz şey müşterilerle ilişkiyi beslemek. Müşteri bilgilerini yöneten ve ilişkileri derinleştiren sisteme CRM (müşteri ilişkileri yönetimi) deniyor. Tamuro'nun rezervasyon sistemine adım adım CRM özellikleri ekledim.

Müşteriler üye olarak kaydolduklarında Hesabım sayfasında rezervasyon geçmişlerini görebiliyor. Bir doğum günü kaydederlerse bir doğum günü ayrıcalığı geliyor. Bir süredir gelmeyen üyeler onları geri çağıran bir mesaj alıyor. Bir de sadakat kartı var. Üç ziyaret bir içki, beş ziyaret ise biftek gibi ayrıcalıklar kazandırıyor, beşe ulaştıktan sonra sayım yeniden başlıyor. Arkadaşları tavsiye etme özelliği de var.

İkinci ziyarete davet mekanizmasını özellikle özenle tasarladım. Restoranlarda ve barlarda, ilk kez gelen bir müşterinin ikinci kez gelip gelmemesinin onun müdavim olup olmayacağını belirlediği söylenir. Tamuro'da ilk ziyaretten 7 gün ve 21 gün sonra iki davet e-postası gönderiyorum. İlkinde kupon yok; yalnızca ikincisinde var. Baştan indirimle cezbetmek yerine önce hatırlamalarına yardım ediyorum. Yine de gelmezlerse küçük bir teşvik sunuyorum.

E-postaların birikmemesine de dikkat ettim. Müşteriler günde en fazla bir mesaj alıyor. Çakıştıklarında öncelik şu sırayla veriliyor: doğum günü, ikinci ziyaret daveti, ilişkisi kopan üyeleri geri çağırma, diğer duyurular. Bir sonraki rezervasyonu zaten olan üyelere ziyarete davet eden e-postalar gönderilmiyor.

E-posta alma onayı varsayılan olarak kapalı. Açık bırakmak alıcı sayısını artırırdı, ama insanların farkında olmadan onay verdiği bir tasarım tüketicinin korunması hukuku açısından sorun olabilir. Rakamlardan çok güveni kazanmak. Benim kararım buydu.

E-postalarda küçük bir dokunuş daha var. Rezervasyon onay e-postasına bir "Bugünün Konusu" giriyor. Mevsimle, şarapla ya da yemekle ilgili bir şey. Yapay zekâ her gün kısa bir konuyu otomatik olarak yazıyor.

Amaç, müşteriye ziyaretinden önce bir sohbet konusu vermek. Tamuro, müşteriler arasında çok sohbet olan bir dükkân. E-postada okunan bir konu, tezgâhta yandaki kişiye söylenecek ilk şey oluyor. Bu yüzden onay e-postasının "Rezervasyonunuz alındı" ile bitmesine izin vermedim; bunun yerine dükkânın havasından biraz önceden iletmesini sağladım.

Konuları yazan yapay zekâyı bir kez değiştirdim. Daha doğal ve dükkânın tonuna daha yakın konular üreten birine geçtim. Ancak bu, müşteri sayısını artırma mekanizması değil. Gelenlerin deneyimini biraz daha iyi hâle getirme mekanizması. Bu ayrıma bu bölümün ikinci yarısında tekrar değineceğim.

Bu mekanizmalar arasında etkisini yavaş yavaş göstermeye başlayanlar "Memnun Oldum" ve "Tekrar Hoş Geldiniz" planları oldu. Bunlar yalnızca ilk kez gelen müşterilerin ve bir yıldan uzun süredir gelmeyen müşterilerin seçebildiği, denemesi kolay, makul fiyatlı planlar. Hem yeni müşterilere hem de uzaklaşmakta olan müşterilere gelmek için bir sebep veriyor.

Öte yandan bir sorun da vardı. Birçok müşteri üye olarak kaydolmadan misafir olarak rezervasyon yapıyor. Her rezervasyonda üyelik kaydı isteseydim rezervasyon yapmaktan tamamen vazgeçebilirlerdi. Bu yüzden rezervasyon bittikten sonra "Bu rezervasyonu bir üye hesabına bağlamak ister misiniz?" diye bir istem gösterip sonradan üye olmanın bir yolunu kurdum. Bu, rezervasyonun önüne engel koymadan ilişkiyi sonradan kurmanın bir yolu.

【Şekil 1-8】Yalnızca ilk kez gelenlerin ve bir yıldan uzun süredir gelmeyenlerin seçebildiği planlar *(Ekran Japonca.)*

【Şekil 1-9】Hesabım sayfasındaki sadakat kartı (yapay veri) *(Ekran Japonca.)*

【Şekil 1-5】Rezervasyon onay e-postası. Bir "Bugünün Konusu" içeriyor (yapay veri) *(Ekran Japonca.)*
