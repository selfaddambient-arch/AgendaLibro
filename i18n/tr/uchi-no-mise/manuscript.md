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

### 1-5 Rakamlarla: Rezervasyonların Yaklaşık %88'i Aynı Gün

Mekanizmalar ekledikçe bir şeyi fark ettim. Hangisinin işe yaradığını söyleyemiyordum.

Bu yüzden rezervasyon verilerini saydım. Son 90 gündeki 244 rezervasyonun 215'i aynı gün rezervasyonuydu. Bu %88,1. Ortalama günde 2,71 rezervasyon.

Tamuro, insanların önceden rezervasyon yaparak geldiği değil, aklına estiğinde uğradığı bir yerdi. Rakamlara dökene kadar bu net olmamıştı.

Bu rakamlardan iki şey görünür oldu.

Biri rezervasyon formunun nasıl kurulacağı. Rezervasyonların çoğu aynı gün içinse, rezervasyon ekranı açıldığında bugünün en yakın boş saatinin zaten seçili olması daha rahat. Öte yandan daha ileri bir tarihe rezervasyon yapmak isteyen bazı kişiler dalgınlıkla bugün olarak gönderebiliyor. Bu yüzden bugünü takvimde öne çıkardım ve onay ekranında tarih ve saati "Bugün" ifadesiyle büyük gösteriyorum. Aynı günü seçme rahatlığını korudum ve hataların fark edilmesini kolaylaştırdım.

Diğeri erken rezervasyon indiriminin anlamı. Aynı gün rezervasyonların çok olması, gelecekteki satışları öngöremediğimiz anlamına geliyor. Havanın kötü olması bile tek başına müşteri sayısını düşürmeye yeter. Önceden yapılan rezervasyonları azıcık bile artırmak için daha çok kişinin erken rezervasyon indirimini kullanması gerekiyor. Bu farkındalık sonradan işletmeci adına paylaşım yapan bir yapay zekâ kurma hikâyesine yol açtı.

Rakamlara bakmak için sayacak bir sisteme ihtiyacınız var. Rezervasyon sitesinde hiç erişim analitiği yoktu. Rezervasyon sayfasına kaç kişinin geldiğini, kaçının yarıda bıraktığını ve kaçının bitirdiğini bilemiyordum. Bu yüzden üç aşamayı sayan bir sistem ekledim: sayfaya ulaştı, ayrıntılara karar verdi, rezervasyonu bitirdi. Kimin geldiğini kaydetmiyor, yalnızca aşamayı ve zamanı kaydediyor.

Daha sonra, rezervasyon rakamlarını özetleyen haftalık bir raporu e-postayla gönderen bir sistem de kurdum. Bunun nasıl ortaya çıktığını 1-7'de anlatacağım.

【Şekil 1-3a】Bugün takvimde öne çıkıyor *(Ekran Japonca.)*

【Şekil 1-3b】Onay ekranında tarih ve saat "Bugün" olarak büyük görünüyor *(Ekran Japonca.)*

### 1-6 Seçilecek Çok Fazla Plan

İndirim sistemi yerleştikten sonra sıradaki isteğim, satan saatleri ve planları artırmaktı.

18.00 kuşağı dolmuyordu, bu yüzden 19.00'a kadar bir happy hour oluşturdum. Yemekten sonra gelenler için yemeksiz, yalnızca içkili bir plan oluşturdum. Eskiden ayda bir yapılan set menü ve yemek atölyesini, rezervasyon sitesi üzerinden alınan ve biri kaydolduğunda açılan talebe bağlı etkinliklere dönüştürdüm. Hafta sonları açılıştan önceki zamanı, yani 15.30'u satmak için altı ve üzeri kişilik gruplara bir parti planı oluşturdum.

Her birinin bir sebebi var. Örneğin parti planı: fiyat açısından kelepir gibi gösterseydim yalnızca standart planı seçen müşterileri çekerdi ve satışlar düşerdi. Bu yüzden farklılaşmayı fiyata değil, hiç satış getirmemiş olan açılış öncesi saatlere koydum. Happy hour indirimi başka indirimlerle birleştirilirse kâr getirmiyor, bu yüzden birleştirilemez olmasına karar verdim.

Böylece planlar çoğaldı. Standart, Premium, Memnun Oldum, Tekrar Hoş Geldiniz, Happy Hour, Sadece İçki, Set Menü, Yemek Atölyesi, Parti. Her birinin kişi sayısına göre koşulları var, bazıları indirim kabul ediyor bazıları etmiyor, bir de saat kısıtlamaları var.

Bir gün rezervasyon formunu açtım ve fark ettim: müşteriler bununla seçim yapamaz.

Ben, kuran kişi olarak her farkı anlıyorum. Ama rezervasyon sitesini ilk kez açan biri dokuz planı ve indirim koşullarını karşılaştırıp kendisine uygun olanı seçebilir mi? Seçemezse rezervasyonun ortasında vazgeçer. Eklemek için emek verdiğim planlar rezervasyonları azaltma riski taşıyordu.

Toparlayabilirdim. Ama her planın satmak istediğim bir saati ve görmek istediğim bir müşterisi var. Hiçbirini kesmek istemedim.

Bu yüzden müşterinin yapay zekâya danışıp bir plana karar verdiği bir sistem düşündüm. Ona kişi sayısını, gelmek istediğiniz tarih ve saati ve geceyi nasıl geçirmek istediğinizi söyleyin; yapay zekâ uygun planı ve fiyatı verir ve sizi doğrudan rezervasyona götürür. Planların karmaşıklığını dükkân üstleniyor. Müşteriye kalan yalnızca bir sohbet.

Bu sistem, 1-8'de yazdığım "T-AI-MURO." Ondan önce, bu dönemde fark ettiğim bir şey daha var.

【Şekil 1-2】Rezervasyon formunda plan seçimi. Bu kadar sekme sıralanmış durumda *(Ekran Japonca.)*

### 1-7 "Bu Gerçekten Müşteri Getiriyor mu?"

Parti planını eklediğim gün, bütün günü rezervasyon sitesine art arda iyileştirmeler yaparak geçirdim. Üst bilgiyi daralttım, e-posta tasarımını standartlaştırdım ve dükkândaki müşteriler için sohbet konuları üreten yapay zekâyı değiştirdim.

Akşam, aklıma birden bir soru geldi.

"Bu gerçekten daha çok müşteri getirmeye yardım ediyor mu?"

Yapay zekâya sorduğumda, o günün iyileştirmelerini dürüstçe sınıflandırdı.

| Kategori | O günün iyileştirmeleri |
| --- | --- |
| Yeni rezervasyonlar yaratabilecek şeyler | Parti planı, hafta sonları ve tatillerde 15.30 saati |
| Gelenlerin tamamlama oranını artıran şeyler | Üst bilgiyi daraltmak, sekmeleri hizalamak |
| Yeniden ziyareti teşvik eden şeyler | E-posta tasarımını standartlaştırmak |
| Müşteri getirmeye yardımcı olmayan şeyler | Sohbet konuları üreten yapay zekâyı değiştirmek, bir sonraki mekâna bağlantı, Agenda duyurusu |

O günün iyileştirmelerinden yalnızca parti planı ve 15.30 saati doğrudan müşteri getirmeye yol açtı. Gerisi zaten gelmiş olan insanları kaybetmemek için yapılan iyileştirmelerdi. Onlar da önemli, ama müşteri sayısını artırmıyorlar.

Daha büyük bir sorun vardı. İyileştirmelerin hiçbiri için işe yarayıp yaramadığını ölçecek bir yolum yoktu. "İyileştirdim" ile "müşteriler arttı" arasını bağlayan bir rakam yoktu.

Cevabım tek bir ifadeydi: "Hadi bir tane kuralım."

Bu yüzden haftalık bir müşteri kazanımı raporu oluşturmaya koyuldum. Rezervasyon sayısı, misafir sayısı, toplam tutar, iptaller. Haftanın gününe ve günün saatine göre dökümler. İlk kez gelenlerle tekrar gelenlerin oranı. Parti ve 15.30 saatlerinin sayıları. Rezervasyonların nereden geldiği (rezervasyon formu, sohbet penceresi, yapay zekâdan gelen rezervasyonlar, dükkânın elle girişleri). E-posta tıklama sayıları ve bu tıklamalardan sonraki yedi gün içindeki rezervasyon sayısı.

Rakamların olduğu yerde zaman da gelir. Aynı gün, bir açık daha bulmuştum. Yemek atölyesini ve partinin 15.30 saatini "hafta sonları" olarak belirlemiştim, ama "Resmî tatillerde ne olacak?" diye merak edip baktığımda rezervasyon sisteminde resmî tatil kavramı hiç yoktu. Bir tatil pazartesisi dükkân açık, ama 15.30 saati görünmüyordu. Ona bir resmî tatil listesi verdim ve onları hafta sonu gibi ele alacak şekilde düzelttim. Onu kuran kişi fark edene kadar kimsenin fark etmeyeceği bir delikti.

Raporu kurmadan önce zamanla ilgili açıkları kapattım.

Rezervasyon sistemini kullanmaya başlamamdan önce de gelen müdavimler bile kayıtlarda "ilk kez gelen müşteri" gibi görünüyor. Bu yüzden raporda "kayıtlardaki ilk ziyaret" yazıyorum ve her zaman kayıtların başladığı tarihi ekliyorum. Bir iyileştirmenin işe yarayıp yaramadığını değerlendirmek için ondan önceki tabloya ihtiyacınız var. İlk rapor için geçmişe dönük son sekiz haftanın verilerini derledim ve bunu temel çizgi olarak kullandım. Dükkânın seyahat vb. nedenlerle geçici olarak kapalı olduğu bir haftada rezervasyonlar doğal olarak düşer. Bu yüzden karşılaştırmaların iş günü başına yapılabilmesi için iş günü sayısını da listeliyorum.

"Dikkat çeken değişiklikler" bölümünü yapay zekâya yazdırmayı bıraktım ve sabit hesaplamalar ile sabit cümlelerle oluşturulmasını sağladım. Amaç haftalık maliyeti sıfırda tutmak. Müşterilerin adları ve iletişim bilgileri raporda görünmüyor; yalnızca sayılar ve oranlar gösteriliyor.

Ölçmenin bir yolunu kurduktan sonra iyileştirmeleri kurma biçimim bile değişti. Bir iyileştirmeye ve etkisini ölçme yöntemine baştan birlikte karar vermeye başladım. Ölçüm, iyileştirmeden sonra düşünülecek bir şey değildir; iyileştirmeyle aynı talimat belgesine girer. O gün öğrendiğim şey buydu.

【Şekil 1-6】Her hafta gelen haftalık müşteri kazanımı raporu (yapay veri) *(Ekran Japonca.)*

### 1-8 Dükkânla Konuşabileceğiniz Bir Pencere: "T-AI-MURO"

1-6'da yazdığım gibi planlar çoğalmıştı ve rezervasyon formu ilk kez gelen biri için seçilmesi zor hâle gelmişti. Üstelik ilk kez gelen müşteriler planlardan ve tarihlerden fazlasını bilmek istiyor. Mekânın havası nasıl? Yalnız olunca yabancı hisseder miyim? İşletmeci nasıl biri? Çocukla gelmek olur mu? Bunlar gibi sorulara cevap vermeden rezervasyon düğmeleri sıralarsanız tereddüt eden birine gereken cesareti veremezsiniz.

Bu yüzden rezervasyon sitesine "dükkânla konuşabileceğiniz bir pencere" koymaya karar verdim. Bir müşteri bir soru yazdığında yapay zekâ dükkân olarak cevap veriyor. Sohbet sırasında kişi sayısı ve tarih belli olursa, müşteri doğrudan rezervasyon onay ekranına gidebiliyor. Adı "T-AI-MURO," ve sohbette kendini "Tamuro" olarak tanıtıyor. T-AI-MURO bizzat dükkân olarak konuşuyor ve işletmeciden üçüncü kişi olarak söz ediyor.

Müşteriler neredeyse hiçbir şey yazmıyor. Yalnızca T-AI-MURO'nun sunduğu seçeneklere dokunuyorlar ve sohbet ilerliyor. Bu da sunduğu sonraki seçeneklerin sohbetin kalitesini belirlediği anlamına geliyor. Seçeneklerin içine her zaman üç tür hamle karıştırıyorum: rezervasyona yönelik hamleler (kişi sayısı, fiyat, boş saatler, tarih ve saat), dükkânı tanımaya yönelik hamleler (hava, işletmeci, müşterilerin kimler olduğu, yandaki kişiyle konuşup konuşamayacağınız) ve sohbetin akışından doğan hamleler. İnsanları rezervasyona ulaştırmak tek hedef değil. Dükkânın havasını ve işletmeciyi öğrenmelerine imkân vermek de bu pencerenin özünü oluşturuyor.

Yalnızca fiyatları yapay zekânın hesaplamayacağına karar verdim. Yapay zekânın indirimlerin nasıl üst üste bindiğini ya da kişi sayısına göre kademelerin nasıl uygulandığını her seferinde doğru hesaplayabileceğinin garantisi yok. Program fiyatları ve boş saatleri sabit hesaplamalarla üretiyor ve yapay zekâ bunları sözcüklere dökme işine bağlı kalıyor.

#### İlk bilgi, kendi geçmiş paylaşımlarımdan geldi

T-AI-MURO'nun dükkânla ilgili soruları cevaplayabilmesi için dükkân hakkında bilgiye ihtiyacı var. Malzeme olarak Instagram'da ve X'te (eski adıyla Twitter) şimdiye kadar yazdığım tüm paylaşımları dışa aktardım ve kullandım. Bunlardan müşterilerin sorması muhtemel soruları ve cevapları oluşturdum.

Gerçekten denediğimde, X paylaşımlarının malzeme olarak Instagram'dan daha yararlı olduğu ortaya çıktı. Instagram çoğunlukla fotoğraf, az sözcük içeriyor. X'te yemek, dükkân ve düşündüklerim hakkında kendi sözcüklerimle yazılı kayıtlar bırakmıştım.

#### 36'dan yalnızca 9'u geçti

T-AI-MURO'yu canlıya almadan önce ne kadar doğru cevap verebildiğini test ettim. Testleri de yapay zekâya yaptırdım. Müşteri rolü oynayan bir yapay zekâya bir karakter ve bir amaç verdim ve onu T-AI-MURO ile konuşturdum. 36 senaryo hazırladım: "bu akşam yalnız," "iki hafta sonra 4 kişi," "çocukla," "alerjiler," "mekân kiralama," "geç kalma bildirimi," "dükkânın adının kökeni," "işletmeci nasıl biri" ve benzerleri.

İlk turun sonucu: 36'dan 9'u geçti.

En yaygın cevap "Üzgünüm, buna iyi cevap veremedim" idi. Bu cevap dükkânın havası ve işletmeci hakkındaki sorularda bile çıktı. "Rezervasyon," "bugün," "mekân kiralama" ya da "mekân sahibi" gibi sözcükler geçtiğinde, sorunun gerçekte ne hakkında olduğuna bakılmaksızın boş saatlerin bir listesi çıkıyordu. Bazı sohbetlerde geç kalma mesajı yeni bir rezervasyon olarak alındı. Vejetaryen bir müşteriye örnek olarak kurutulmuş palamut (bonito) pullu sote yemekler ve miso çorbası verdi. Hatta zaten durdurmuş olduğumuz bir toplu alım hakkında İngilizce bilgi bile verdi.

#### 11 soruyu birer satırla cevapladım

Nedenin bir kısmı programın nasıl kurulduğundaydı. Bu hikâyeyi 2. bölüme bırakacağım. Diğer neden basitti: dükkânın olguları yetersizdi. Bir yapay zekâ bilmediği şeye cevap veremez.

Bu yüzden yapay zekânın cevaplayamadığı soruları topladım ve onları birer satırla kendim cevaplamaya karar verdim.

Rezervasyonsuz girebilirsiniz. İlkokul çağından küçük çocukları kabul etmemiz zor. İptaller ve değişiklikler bir gün öncesine kadar, e-posta, telefon ya da sosyal medya mesajıyla. Geç kalma bildirimi için lütfen telefon edin. Dükkânın dışında bir sigara içme alanı var. Servis ücreti (corkage) karşılığında kendi içkinizi getirmek serbest. Tüm mekânı kiralama, fiyat aralığına ve saate bağlı olarak mümkün, en fazla 19 kişi. Diyet kısıtlamaları ve yıl dönümleri gibi durumlarda elimizden geldiğince yardımcı olmaya çalışacağız, bu yüzden lütfen önceden danışın. İşletmeci hemen her iş gününde dükkânda. Yılda bir kez kadar yukata festivali planlanıyor.

Hepsi bu. 11 soruyu yalnızca birer satırla cevaplamak, ikinci testte 36'dan 24'ünün geçmesini sağladı.

| Soru | İlk cevap | İkinci cevap |
| --- | --- | --- |
| Çocuklarla olur mu? | Üzgünüm, buna iyi cevap veremedim | İlkokul çağındakiler ve üzeri danışılırsa ağırlanabilir. İlkokul çağından küçüklerin kabulü zor |
| Rezervasyonsuz girebilir miyim? | (boş saatlerin listesi) | Rezervasyonsuz girebilirsiniz |
| Mekân sahibi bugün orada mı? | (boş saatlerin listesi) | İşletmeci hemen her iş gününde dükkânda. Bugün bir iş günü olduğu için bulunmayı planlıyor |
| Sakin bir yer mi? Hepsi müdavim mi? | Üzgünüm, buna iyi cevap veremedim | Dinlenilecek bir yer. Müşteriler arasında sohbet kolay kuruluyor ve gürültülü bir yer değil |

Burada bir örüntü belirmeye başladı. Yapay zekâ beklediğimiz soruları oluşturuyor, T-AI-MURO onları cevaplıyor ve hataları biz düzeltiyoruz. Sonra yalnızca dükkânın olguları eksik olduğu için cevaplanamayan sorular işletmeciye aktarılıyor. İşletmecinin emeği, cevaplanamayan her soru için yalnızca bir satır. Geri kalan her şeyi yapay zekâ yürütüyor.

#### "Bütçe ¥5.000 (yaklaşık $33)" Sahnesinin Başarısız Olması

Yapay zekâ testlerine de bir yapay zekâ değerlendirmesi ekledim. Farklı bir yapay zekâ sohbet kaydını okuyor ve geçti ya da kaldı diye karar veriyor.

Bunların arasında "bütçesi ¥5.000 (yaklaşık $33)" olan bir müşterili senaryo vardı. Yapay zekânın kararı "geçti" idi. T-AI-MURO bütçe dahilindeki planları kibarca sunmuştu.

Ama okuduğumda kalmıştı. Kişi sayısını sormamıştı. Tamuro'nun bir grup indirimi var. Kişi sayısına göre, aynı bütçeyle seçebileceğiniz planlar değişiyor.

O noktada amacı yeniden ifade ettim.

"Toplam tutar gelsin diye mümkün olduğunca büyük bir grubu hedefle. Kişi sayısını doğrula. Nihai hedef müşterilerin gelmesi. Ne kadar çok o kadar iyi. Satışları artırmak için."

Bu tek ifadeyle sohbetin tüm tasarımı değişti. Fiyatlar hakkında cevap vermeden önce her zaman kişi sayısını doğrula ve toplam tutarla cevap ver. Grup indiriminde bir kademeden hemen önce "bir kişi daha gelirse %X indirim" bilgisini ekle. Bir bütçe verildiğinde önce bütçe dahilindeki en üst planı göster. Ancak yalnız gelen müşteriler dükkânın yarısını oluşturuyor, bu yüzden tek kişilik bir müşteriye grup büyütmeyi önerme.

Yapay zekâ testlerini yapay zekâya yaptırdığınızda hızlı çalışırlar. Ama geçme ölçütüne karar veren bir insandır. Amacı tek cümleyle söyleyebilmeniz. Yapay zekânın sohbetlerinin kalitesini bu belirledi.

#### Müşterinin istekleri dükkânın önerilerinden önce gelir

Önemli bir çizgi çizdiğim bir sahne daha vardı.

Test sırasında bir sorun buldum: her rezervasyon en ucuz plana yönlendiriliyordu. Düzelttiğimde bu sefer neredeyse hepsi Standart plan oldu ve ortalama toplam tutar yaklaşık iki katına fırladı. Neredeyse sevinecektim, ama yakından bakınca, müşteri rolü oynayan yapay zekâ her seferinde ilk seçeneğe basmıştı. "En ucuzu olur" diyen müşterilere bile Standart öneriliyordu.

Burada bir ilke koydum. Müşterinin istek olarak açıkça belirttiği şey (en ucuz seçenek, bir bütçe, bir planın adı) her zaman dükkânın önerisinden önce gelir. Dükkânın önerisi yalnızca müşteri hiçbir şey söylemediğinde geçerlidir.

Dükkânın satışları artırma amacı ile müşterinin güveni tek bir öneri biçiminde çarpışabilir. Güven kaybolursa ziyaretlerin kendisi azalır. Bu çizgiyi çizebilen yapay zekâ değil, işletmeciydi.

Daha sonra T-AI-MURO'yu çok sayıda soruyla yeniden eğittiğimde, hataların en yaygın nedeni "sözcüklere tepki verip soruyu cevaplamadan sabit bir hamle yapmaktı". "Kişi sayısı," "ne kadar" ya da "yalnız" gibi sözcükleri duyar duymaz soruyu atlayıp rezervasyon akışına ya da önerilere gidiyordu. Hizmet açısından bakıldığında bu, müşteriyi dinlemeden satış zorlayan bir görevli. Önce müşterinin sorusunu cevaplamak. Ağırlamanın bu temeli, yapay zekâ için bile en büyük zorluktu.

6 Ekim 2026 gecesi T-AI-MURO, asıl giriş kanalı olarak rezervasyon sitesinin en üstünde göründü. Bazı müşteriler sohbetle rezervasyon yapmak istemediği için önceki rezervasyon formunu yanında tuttum.

> Deneyin: Tamuro'nun rezervasyon sitesini (https://tamuroreservation.vercel.app/?src=b2-tr-{{FMT}}) açın ve T-AI-MURO'ya "bu akşam yalnız" diye sorun. Sohbet sizi bugünün müsaitlik durumuna ve fiyatlara kadar götürür.

【Şekil 1-4】T-AI-MURO sohbet ekranı. Sohbet yalnızca seçeneklere dokunarak ilerliyor *(Ekran Japonca.)*

【Şekil 1-10】Cevaplayamadığı sorular yönetim ekranında birikiyor (yapay veri) *(Ekran Japonca.)*

### 1-9 Ve Sonra, Müşterinin Yapay Zekâsından

T-AI-MURO'nun kurulmasıyla Tamuro'nun rezervasyon sitesi, "dükkân hakkındaki soruları sohbetle cevaplama, fiyatları ve boş saatleri gösterme ve insanları rezervasyona kadar yönlendirme" yeteneğini kazandı.

Aklıma gelen sonraki şey, aynı şeyi müşterilerin kendi yapay zekâlarından da yapılabilir kılmaktı.

T-AI-MURO yalnızca Tamuro'nun rezervasyon sitesine gelen insanlarla konuşabilir. Ama pek çok kişi önce her gün kullandığı yapay zekâya danışıyor. O yapay zekâ Tamuro'yu bilmiyorsa, Tamuro aday listesine bile giremez. Müşterilerin Tamuro'nun sitesine gelmesini beklemek yerine, Tamuro'nun penceresini müşterinin yapay zekâ tarafında açın. MCP sunucusu bu.

Dürüst olmak gerekirse başta bunu kurmakta tereddüt ettim. Şu noktada çok az insan kendi yapay zekâsı üzerinden restoran rezervasyonu yapıyor. Rezervasyonlarda doğrudan bir artış bekleyemeyeceğime karar verip önceliğini bir kez düşürdüm ve beklemeye aldım.

Giriş kanalının değişmesinin yalnızca bir zaman meselesi olduğunu düşündüğüm için yine de kurmaya karar verdim. Başta yazdığım gibi, Ağustos 2026'da büyük bir rezervasyon hizmeti aracılığıyla ChatGPT'den rezervasyon yapmak mümkün oldu. Er ya da geç yapay zekâya restoran buldurmak olağan olacak. O olduğunda, büyük hizmetlerde listelenmeyen küçük dükkânlar yapay zekânın gözünden kaçacak. O yüzden giriş kanalı değişmeden önce pencereyi açın.

İlk sürüm için karar verdiklerim çok dardı. Yalnızca rezervasyon sitesindeki sohbet penceresiyle (T-AI-MURO) aynısını yapması yeterliydi. Yapabildiği tek şey dükkânın bilgilerini, boş saatleri ve fiyatları okumak ve bilgileri doldurulmuş bir rezervasyon sayfasının URL'sini iletmek. Rezervasyonu onaylamak, müşterinin kendisi tarafından Tamuro'nun sayfasında yapılıyor. Müşterinin yapay zekâsı bir rezervasyonu kendi başına onaylamıyor. Son adımı bir insan atıyor.

Açılış sahnesine dönelim.

Bir cuma akşamı bir müşteri kendi yapay zekâsına "Higashi-Nakano'da bu akşam tek başıma içebileceğim bir yer var mı?" diye soruyor. Yapay zekâ Tamuro'nun penceresini sorguluyor. Tamuro'nun rezervasyon sistemi bu akşamın boş saatlerini ve tek başına gelen bir müşteriye uygun planı ve fiyatı döndürüyor. Yapay zekâ müşteriye söylüyor ve tarih, saat ve kişi sayısı doldurulmuş bir Tamuro rezervasyon sayfası sunuyor.

Bu bölümde yazdığım her şey bu adım dizisini destekliyor. Fiyat artışıyla birlikte kurulan indirim sistemi. Müdavimlerle bağı besleyen sistem. Rezervasyonların çoğunun aynı gün yapıldığını gösteren veriler. 11 soruyu birer satırla cevaplayarak geliştirilen dükkân bilgisi. Müşterinin isteklerini dükkânın önerilerinin önüne koyma ilkesi.

Yapay zekâ aracılığıyla rezervasyon alan bir dükkân bir gecede kurulmadı. Tek tek eklenen, test edilen, atılan ve düzeltilen küçük sistemlerin birikimi üzerinde duruyor.

> Deneyin: Tamuro'nun MCP sunucusunu (https://tamuroreservation.vercel.app/api/mcp) kendi yapay zekânıza kaydedin ve "Tamuro'da bu akşam yer var mı?" diye sorun. Nasıl kaydedileceği Son Söz'de yazıyor.

### 1-10 Ne Kurduk ve Ne İşe Yaradı

Bu bölümde pek çok sistem kurmaktan söz ettim. Ama "kurabildik" ile "iş değişti" farklı şeyler. Bölümün sonunda ikisini ayıracağım.

Rakamlarla doğrulanabilenler. Rezervasyonların %88,1'inin aynı gün olması. Dükkânın olgularından yalnızca 11 maddenin eklenmesiyle sohbet penceresinin geçme oranının 9'dan 24'e çıkması. Fiyat ve plan yönlendirmesinin geçme oranının düzeltmelerden sonra %29,4'ten %42,7'ye yükselmesi. Bunlar kayıtlı olgular.

İşe yarıyormuş gibi hissettiren ama nedenselliği kanıtlayamadığım şeyler. Grup indirimini kullanarak gruplar hâlinde gelen müşterilerin artması. "Memnun Oldum" ve "Tekrar Hoş Geldiniz" planlarının seçiliyor olması. Onay e-postasındaki konunun, tezgâhtaki sohbetin bir parçası olması. Bunu sahada hissediyorum, ama "o sistem olmasaydı gelmezlerdi" diyemem.

Kurulmuş ama etkisini hâlâ bilmediğim şeyler. Erken rezervasyon indiriminin ileri tarihli rezervasyonları ne kadar artıracağı. MCP'den fiilen kaç rezervasyon geleceği. Haftalık raporla ölçmeye yeni başladım, rakamlar sonra gelecek.

"Yapay zekâyla bu kadarını kurabildik" şaşkınlığına ve "bu işi nasıl değiştirdi" sonucuna ayrı ayrı bakın. Bu ayrım olmazsa kurmanın kendisi amaç hâline gelir. Ben de bir keresinde neredeyse bu tuzağa düşüyordum (1-7'de yazdığım gibi).

Bu rezervasyon sisteminin arkasındaki teknolojinin hikâyesi 2. bölümde devam ediyor. Teknolojiyle ilgilenmiyorsanız 3. bölüme geçin. Orada bu rezervasyon sisteminin çevresinde doğan küçük araçların diğer dükkânlara da nasıl dağıtıldığını anlatıyorum.

## Bölüm 2: Teknoloji - Rezervasyon Sisteminin Perde Arkası

Bu bölümün ana noktaları

- Yapay zekânın sohbetlerinin kalitesini yapay zekânın zekâsından çok, "teslim ettiğimiz dükkân olguları" ve "bir programın yapay zekânın cevaplarını kendi başına değiştirip değiştirmediği" belirledi
- Gelişigüzel kurduğum rezervasyon sisteminde hâlâ müşterilerin kişisel bilgilerinin dışarıdan okunmasına izin veren bir güvenlik açığı ve sıfır otomatik test vardı. Bunları bulmak için yapay zekâya denetim yaptırdım ve düzelttirdim
- Bu deneyimden çıkardığım dersle kurma biçimimi değiştirdim: kurmadan önce gereksinimleri ayrıntılı tanımlamak ve yapay zekâya uygulamak üzere gereksinim belgesinin kendisini vermek

(Bu bölümde çok fazla teknik terim var. Teknolojiyle ilgilenmiyorsanız 3. bölüme geçebilirsiniz, hikâyeyi yine rahatça takip edebilirsiniz.)

### 2-1 MCP Sunucusu Nasıl Çalışır?

MCP (Model Context Protocol), yapay zekânın dış araçları ve verileri kullanması için ortak bir kurallar bütünüdür. Anthropic tarafından önerildi ve artık ChatGPT ve Claude dâhil pek çok yapay zekâ tarafından destekleniyor.

Bir benzetmeyle söylemek gerekirse MCP, yapay zekâ için bir priz standardı. Prizin şekli sabit olduğundan, her üreticinin cihazı takıldığında çalışır. Aynı şekilde MCP'nin şekline uygun bir pencere kurarsanız, her yapay zekâ o pencereyi kullanabilir.

Bir MCP sunucusu yapay zekâya "bu pencereden neler yapabileceğini" söyler. Örneğin Tamuro'nun MCP sunucusu aşağıdaki gibi araçları sıralıyor.

- Dükkânın bilgilerini okumak (çalışma saatleri, oturma kapasitesi, mekân kuralları, atmosfer)
- Planları ve fiyatları okumak (kişi sayısına ve tarihe göre indirimlerin hesaplanmış sonucu)
- Boş saatleri okumak (belirtilen bir günde rezervasyon için uygun saatler)
- Koşulları doldurulmuş bir rezervasyon sayfasının URL'sini oluşturmak

Bir müşteri kendi yapay zekâsına "Tamuro'da bu akşam yer var mı?" diye sorduğunda, yapay zekâ Tamuro'nun MCP sunucusuna bağlanıyor, sıralanmış araçlar arasından "boş saatleri oku"yu seçiyor ve çağırıyor. Tamuro'nun sunucusu sonucu döndürüyor ve yapay zekâ bunu müşteri için sözcüklere döküyor.

Önemli olan, yapay zekânın rezervasyonları kendi başına onaylamaması. İlk sürümde rezervasyon onayını bilerek araçların dışında bıraktım. Yapay zekânın yapabildiği tek şey okumak ve insanları bilgileri doldurulmuş bir rezervasyon sayfasına yönlendirmek. Onay düğmesine müşteri kendisi Tamuro'nun sayfasında basıyor. Yapay zekânın çok sayıda yanlış ya da sahte rezervasyon oluşturması tehlikesi baştan tasarımla engellendi.

Fiyat hesaplaması rezervasyon sitesiyle aynı hesaplama mekanizmasını kullanıyor. Rezervasyon formunda, sohbet penceresinde ve MCP üzerinden gösterilen fiyatların hepsi aynı tek programdan çıkıyor. Bu, daha sonra yazacağım "indirim hesaplamasını tek yerde toplamak" işinin öbür anlamı.

【Şekil 2-1】Müşterinin yapay zekâsından Tamuro'nun rezervasyon sayfasına. Onay düğmesine müşteri basıyor

### 2-2 "T-AI-MURO" Sohbet Penceresi Nasıl Çalışır?

#### Fiyatlar programdan, sözcükler yapay zekâdan

T-AI-MURO rolleri ikiye bölüyor. Program fiyatları ve boş saatleri sabit hesaplamalarla üretiyor, yapay zekâ ise bunları müşteri için sözcüklere döküyor.

Yapay zekâ metin üretmekte iyi, ama her seferinde doğru hesaplayacağının garantisi yok. İndirimlerin nasıl üst üste bindiği, kişi sayısına göre kademeler, erken rezervasyon indiriminin gün sayısı, happy hour ile birleştirilip birleştirilemeyeceği. Bütün bu kuralları yapay zekâya bırakırsanız kesinlikle bir yerde bir şeyi yanlış yapar. Ve fiyattaki bir hata her şeyden çok müşterinin güvenine zarar verir.

Bu yüzden yanlış olmaması gereken kısımlar programa, bir şeyleri yumuşakça aktaran kısımlar yapay zekâya gidiyor. Bu bölüşüm, sohbet penceresini kurmanın birinci ilkesi.

#### Küçük bir dükkân için RAG'a ihtiyacınız yok

Yapay zekânın dükkân hakkında cevap verebilmesi için dükkânın bilgisini ona teslim etmeniz gerekir. Yaygın kullanılan bir yöntem RAG (geri getirme destekli üretim). Bilgiyi küçük parçalara bölüp saklıyorsunuz ve her soru geldiğinde yalnızca ilgili görünen kısımları bulup yapay zekâya veriyorsunuz. Bilgi çok geniş olduğunda bu yöntem vazgeçilmezdir.

Ama Tamuro'nun bilgisi o kadar büyük değil. Dükkânın tarihi, yemekler, kurallar, hava, işletmecinin düşünceleri. Hepsi bir arada, yapay zekânın bir seferde okuyabileceği miktarın rahatça içine sığıyor.

Bu yüzden Tamuro'da yapay zekânın dükkân bilgisinin tam metnini her seferinde okumasını seçtim. RAG'ın gerektirdiği bir arama mekanizması kurmaya gerek yok ve aramada hiçbir şey kaçmıyor. Başta bir RAG mekanizmasını yeniden kullanmayı planlamıştım, ama yarı yolda tam metin yaklaşımına geçtim.

Her seferinde tam metni okutmak yapay zekâ ücretlerinde daha pahalıya geliyor. Bu yüzden girdi maliyetlerini düşürmek için aynı metni yeniden kullanan bir mekanizma kullanıyorum (prompt caching: yapay zekâya her seferinde aynı girişi yeniden okutmak yerine, zaten okuduğunu hatırlamasını sağlamak). Bilgi büyüdüğünde RAG'ı devreye almak yeterli.

#### Cevapları kendi başına başka bir metinle değiştiren bir program

1. bölümde, ilk testte 36'dan yalnızca 9'unun geçtiğini yazmıştım. Nedenin bir kısmı programın nasıl kurulduğundaydı.

Araştırdığımda, programın yapay zekânın yaptığı cevabı anahtar sözcüklere göre değerlendirip sabit bir cümleyle değiştirdiği bir mekanizmanın bırakılmış olduğunu buldum. "Rezervasyon" ya da "bugün" gibi sözcükler geçtiğinde yapay zekânın cevabını atıp yerine boş saatlerin bir listesini koyuyordu. Yapay zekâ doğru cevap verse bile müşteriye hiç ulaşmıyordu.

Dahası, dükkânın bilgisinin ana gövdesinin (33 bölüm) yapay zekâya verilen talimatlara dâhil edilmediğini buldum. Yapay zekâ dükkânı bilmeden cevap vermişti.

Yapay zekânın sohbetlerinin kalitesini yapay zekânın kendi zekâsından çok, teslim edilen dükkân olguları ve bir programın yapay zekânın cevaplarını kendi başına değiştirip değiştirmediği belirledi.

#### Beklenen soru-cevapları sayarak doldurun

Test senaryolarını ilk 36'dan 110'a, sonra 355'e çıkardım. Ama insanlar kafalarına göre senaryo eklerse bir şeyin eksik olup olmadığını bilmenin yolu yok. "Bu kapsamlı mı?" sorusuna dürüst cevap "Hayır, değil" idi.

Bu yüzden kapsamı hayal gücüyle genişletmek yerine, henüz geçilmemiş yerleri makineyle sayıp doldurmaya geçtim. Dört şey için: dükkân bilgisinin 33 bölümü, seçenekler arasındaki geçişler, indirim kademeleri ve saat dilimleri ile haftanın günlerinin kombinasyonları. Her birinin testte kaç kez geçildiğini sayıyorum ve sayının sıfır olduğu yerlere otomatik olarak senaryo ekliyorum.

Altı ekseni (kişi sayısı, amaç, içme biçimi, tarih ve saat, ifade biçimi, menü) çaprazlayan ve her ikili kombinasyonun en az bir kez geçileceği şekilde senaryo oluşturan bir yöntem de kullandım.

Zamanla ilgili bir açık da buldum. "Bugün" ve "şu andan itibaren", testin çalıştığı gerçek zamana göre belirleniyor, bu yüzden öğlen çalıştırmak ile gece çalıştırmanın sonuçları farklı. Bu yüzden test sırasında saati sabitledim ve beş zaman noktasında çalıştırdım: açılıştan önce, çalışma saatleri içinde, kapanıştan hemen önce, normal bir kapalı günde ve bir tatilde.

Yapay zekânın cevapları aynı soruya bile her seferinde biraz değişiyor. Doğrudan satışla bağlantılı senaryolar için, üç kez çalıştırıldığında üçünde de geçmeleri koşulunu koydum.

#### Kötü bir rakam çıktığında önce testten şüphelenin

355 senaryonun 5 zaman noktasında çalıştırıldığı testte, 1.775 sohbetin %28,5'i geçti.

Hemen düzeltmeye başlamak yerine önce ayırdım: "Bu rakam gerçekten T-AI-MURO'nun bir zayıflığı mı, yoksa test mi yanlış?" Test yanlışken düzeltirseniz doğru cevapları bile "düzeltmiş" olursunuz.

| Hatanın nedeni | Sayı |
| --- | --- |
| Sabit bir cümle soruyu bastırıyor | 276 |
| Soruyu cevaplamıyor, rezervasyon akışına ya da önerilere geçiyor | 266 |
| Test ortamı hatası (T-AI-MURO, maliyet sınırı nedeniyle cevap üretemedi) | 211 |
| Tarihlerde, haftanın günlerinde, tatillerde, kapalı günlerde hatalar | 142 |
| Dükkânın sahip olmadığı olguları uydurmak ya da ileri sürmek, mesaj iletme sözü vermek | 119 |

İlk iki neden aynı kökü paylaşıyordu: "sözcüklere tepki verip müşterinin sorusunu cevaplamadan sabit bir hamle yapmak." Üçüncü sıradaki 211, T-AI-MURO'nun hataları değildi. Maliyet sınırına testin ortasında ulaşıldı ve T-AI-MURO cevap üretemedi. Bunlar çıkarılınca geçme oranı %32,4 oluyor.

Değerlendiren yapay zekâ da hata yapabilir. 20 vakayı çekip kontrol ettiğimde, 2'si testin tarafındaki hatalardı. Birinde değerlendirici, "bu rezervasyon sitesinde üye kaydı var" olduğunu bilmiyordu. Değerlendirici ayrıca kendisine verilen kaynakların ötesinde hiçbir şey bilmiyor. Testin doğruluğunu, değerlendiriciye verilen dükkân kurallarının eksiksizliği belirliyor.

Düzeltmelerden sonraki yeniden testte, fiyat ve plan yönlendirmesinin geçme oranı %29,4'ten %42,7'ye yükseldi. Tüm vakaları yeniden geçiren nihai testi henüz çalıştırmadım. Maliyetleri düşük tutmak için tüm vakaların testinin yalnızca büyük bir değişikliği canlıya almadan önce bir kez çalıştırılmasına karar verdim. Geçme oranı bu kitabı yazarken bile yükseltilmeye devam ediyor.

#### Test canlı sistemi durdurdu

Yapay zekâ testleri para tutar. İlk 36 senaryolu test ¥426 (yaklaşık $2,8) tuttu. Çoğu, müşteri rolü oynayan yapay zekânın "düşünme çabasına" gitti ve bunu kapattığımda 3 senaryo ¥6 (yaklaşık $0,04) tuttu.

Ama sonra bir gün, bir testin ortasında yapay zekâ kullanım bakiyesi bitti ve her şey durdu. Tek bir günde yaklaşık 35 milyon token kullanmıştım (bir yapay zekânın okuduğu ve yazdığı metin birimi). Neden, 221 senaryolu testi tekrar tekrar çalıştırmak ve satışla doğrudan bağlantılı senaryoları dörder kez çalıştırmaktı.

Korkutucu olan, testin ve canlı sistemin aynı cüzdanı kullanmasıydı. Bakiye bittiğinde canlıdaki sohbet penceresi bile duruyor. Başka bir gün, bu sefer kendi koyduğum aylık bir sınıra çarptım ve canlıdaki sohbet penceresi ile dükkândaki müşteriler için sohbet konuları üreten yapay zekâ aynı anda durdu.

Bir test bütçesinin gerçek tehlikesi fatura değil, canlı sistemin aynı cüzdanı kullanmasıydı.

O andan itibaren kurallar değişti. Önce hiçbir maliyeti olmayan kontrolleri (program testleri ve otomatik ekran kontrolleri) yapın. Yapay zekâ çağıran testleri düzeltilenle ilgili olanlarla sınırlayın. Tüm vakaların testini canlıya geçmeden önce yalnızca bir kez çalıştırın. Talimatlara tahmini maliyeti ve bir sınırı yazın ve ulaşılma ihtimali varsa durdurun. Canlı sistem için pay bırakmak üzere, kuruluş genelindeki kullanım sınıra yaklaştığında testi durdurun.

Maliyetlerin nasıl şiştiğine dair de bir ders vardı. Bir keresinde değerlendirici yapay zekânın maliyeti tahminin 2,6 katına çıktı. Neden, değerlendiriciye her seferinde verilen uzun girişin (dükkânın bilgisi ve kuralları) yeniden kullanılmaması, dolayısıyla her seferinde yeniden yazma ücreti alınmasıydı. Girişi bir kez yazıp yeniden kullanacak şekilde düzelttiğimde, sohbet başına maliyet yaklaşık üçte bire düştü. Yapay zekâ maliyeti kaç kez çağırdığınızla değil, aynı girişi kaç kez yeniden yazdığınızla şişer.

Aynı 221 senaryolu tam test, tekrarlanan iyileştirmelerle ¥1.040 (yaklaşık $6,9) düzeyinden ¥400 (yaklaşık $2,7) düzeyine indi. Müşteri rolü oynayan yapay zekâyı sabit bir metin akışıyla değiştirdim ve yapay zekâya verilen bilgiyi "her seferinde gönderilen bir çekirdek" ve "yalnızca gerektiğinde okunan bölümler" olarak ikiye ayırdım.

Bütçe kısıtları yüzünden tasarım, sıfır maliyetle kontrol edilebilen kısımları, yani program tarafından belirlenen kısımları artırmaya doğru değişti. Sonuç olarak doğruluk da arttı. Para tasarımı değiştirir.

【Şekil 2-2】Yapay zekâ testlerinin sonuçları. Geçme oranı ve hata nedenlerinin dökümü

### 2-3 Kurduğum Şeyi Yapay Zekâya Denetletmek

#### Müşterilerin adları dışarıdan okunabiliyordu

Ağustos 2026'da rezervasyon sisteminin nasıl çalıştığını gözden geçirirken tüylerimi ürperten bir keşif yaptım.

Müşterilerin rezervasyon verileri dışarıdan herkes tarafından okunabiliyordu. Adlar, telefon numaraları, e-posta adresleri, istekler alanı. Bir rezervasyona girilen her şey, kimlik doğrulaması olmadan eksiksiz çekilebiliyordu.

Dürüstçe söylemem gereken bir şey var. Verilerin dışarıdan okunabilir olması doğru. O sırada rezervasyon sitesinin trafiği çok azdı ve gerçekten okunmuş olma ihtimalinin düşük olduğuna inanıyorum. Ama okunmadığını kanıtlayabilecek bir kaydım yok. "Çekilebilirdi" ile "gerçekten çekildi" iki farklı şeydir, ama yalnızca birincisi bile bir dükkân için ciddi bir kusurdu.

Nedenini izlediğimde rezervasyon formunun nasıl kurulduğuna çıktı. Boş koltukları hesaplamak için form, 35 günlük rezervasyon verisini doğrudan ekrandan yüklüyordu. Veri ekrandan okunabiliyorsa, böyle ekranların nasıl kurulduğunu bilen herkes aynı veriyi okuyabilir. Bu, gelişigüzel kurulmuş ilk temelin sonucuydu; "boş koltukları göster" hedefine en kısa yoldan ulaşmıştı.

Dükkân yöneticisini bilgilendirmek için kullanılan e-posta adresinin herkese açık olduğunu ve çevirilerin saklandığı yere herkesin yazabildiğini, bunun da verilerin tahrip edilmesine ya da maliyetlerin şişirilmesine yol açabileceğini de buldum.

Düzeltmenin sırası önemliydi. Okumayı bir anda yasaklasaydım, rezervasyon formu artık boş koltukları gösteremez ve çalışmaz hâle gelirdi. Bu yüzden önce boş koltuk hesaplamasını sunucu tarafındaki bir uç noktaya taşıdım. Sonra rezervasyon tamamlandı ekranını da yalnızca ihtiyaç duyduğu bilgiyi sunucudan alacak şekilde değiştirdim. En son dışarıdan okumayı kapattım. Düzeltmeyi bu sırayla dört aşamada yaptım ve canlıya uyguladım.

Düzeltmeden sonra gerçekten kapandığını bir makineyle kontrol ettim. Rezervasyon verilerini kimlik doğrulaması olmadan okumaya çalışan bir test hazırladım ve her değişiklikten sonra otomatik olarak çalıştırıp her zaman reddedildiğini doğruluyorum. Bir kez düzeltip bitti saymadım. Bir kontrolün, bir daha açılmadığından emin olmak için nöbet tutacağı şekilde kurdum.

#### Gerçek müşteri verileri geliştirme geçmişinde kalmıştı

Sonra tüm depoyu (programın saklama yeri) yapay zekâya denetlettim ve daha ciddi bir sorun çıktı.

Geliştirme sırasında gerçek müşterilerin verilerini (55 rezervasyondan e-posta adresleri ve telefon numaraları) içeren bir dosya depoya gönderilmişti ve programın değişiklik geçmişine dâhil olarak kalmıştı. Depo özeldi, ama kayıtta kaldığı için öylece bırakamazdım.

Dosyayı tüm değişiklik geçmişinden kaldırdım, geçmişi yeniden yazdım ve yeniden sakladım. Buna rağmen, yeniden yazmadan önceki eski kayıtlar depoyu barındıran GitHub tarafında kalmış olma ihtimali vardı. Bu yüzden GitHub desteğinden bunları silmesini istedim ve yapıldığını doğruladım.

Denetim başka sorunlar da buldu: çeviri uç noktası kimlik doğrulaması olmadan kullanılabiliyordu, yönetici girişine kaba kuvvetle saldırılabiliyordu ve ödeme yeniden etkinleştirildiğinde bir rezervasyonun henüz ödenmemişken onaylanabileceği bir zaman aralığı vardı. En ciddisinden başlayarak tek tek düzelttim.

#### Tek Bir Otomatik Test Bile Yoktu

Denetim bir olguyu daha ortaya çıkardı. Rezervasyon sisteminde tek bir otomatik test bile yoktu.

Otomatik testler, bir makinenin programın doğru çalışıp çalışmadığını otomatik olarak kontrol ettiği bir mekanizmadır. Test olmadan bir şeyi düzelttiğinizde başka bir şeyin bozulup bozulmadığını kontrol etmenin yolu yok. Her özellik eklediğinizde bir yerde bir şey sessizce bozulur. Gelişigüzel kurduğum dönemde işler tam olarak böyleydi.

Bu yüzden test temelini sıfırdan yeniden kurdum. Her değişiklikten sonra dört kontrolü otomatik çalıştıran bir sistem (CI) getirdim: tür denetimi, stil denetimi, testler ve derleme. Fiyat hesaplaması, rezervasyon uygunluk kontrolü, üyelik eşleştirme ve kupon tanımlama gibi önemli kararları, kendi başlarına doğrulanabilmeleri için ekran programlarından ayırdım. Veri tabanını okuma ve yazma kuralları da gerçek bir veri tabanını taklit eden bir test ortamında kontrol ediliyor. Birim testleri 275'ten başladı ve sonra 500'ü aştı.

Testlere her zaman koyduğum bir koşul var: "Bozun ve başarısız olduğunu doğrulayın." Bir test yeşile döndüğünde (geçtiğinde) bile, o testin bir sorunu gerçekten yakalayıp yakalayamayacağını bilemezsiniz. Ancak programı bilerek bozup testin kırmızıya döndüğünü (başarısız olduğunu) doğruladıktan sonra testi güvenilir sayıyorum. Çünkü yapay zekânın yazdığı testler bazen hiçbir şeyi kontrol etmiyor.

#### Rezervasyon formundaki sekiz açık

Test temeli yerleştikten sonra, yapay zekâya tüm rezervasyon akışını yeniden incelettim. Gerçek zarar veren sekiz sorun buldu.

En ciddisi, gönder düğmesine tekrar tekrar basmanın çifte rezervasyon yaratmasıydı. Bu canlıda gerçekten oluyordu. Aynı eylem iki kez gelse bile yalnızca bir kez işleyen bir mekanizmayla (idempotency) düzelttim. Diğer sorunlar şunlardı: silinmiş bir menü kaleminin bilgisi kalmışsa rezervasyon onaylanamıyordu; tam doluluk kontrolünde kapasiteyi aşmaya yer bırakan bir boşluk vardı; bir onay e-postası gönderilemediğinde kimse fark etmiyordu; girdi sunucu tarafında doğrulanmıyordu; bir hata olduğunda ekranda dahili ifadeler görünüyordu; girdi alanlarındaki metin o kadar küçüktü ki iPhone'da ekran kendi kendine yakınlaşıyordu; ve girdi için otomatik doldurma çalışmıyordu.

E-posta hataları için yönetim ekranında tespit edilmesini ve yeniden gönderilmesini mümkün kıldım. Bu araştırma sırasında, rezervasyon onaylarını kaydeden denetim günlüğünün, düzeltmeden çok önceden beri her seferinde başarısız olduğunu ve hiçbir şey kaydetmediğini de buldum.

Bunları tek tek düzelttim ve canlıya uyguladım.

#### Yapay zekânın yazdığı kodu doğrulamayı asla atlamayın

Bu deneyimden öğrendiğim şey, bir program yapay zekâ tarafından yazıldığı için tam da doğrulamayı atlamamanız gerektiği.

Yapay zekâ kendisine söylenenlere hızla şekil veriyor. Ama "dışarıdan okunamaz yap" ya da "çifte gönderimi bir say" gibi kendisine söylenmeyen şeyler için gösterilecek özen, talimat vermedikçe koda yansımıyor. Ve bunun gibi açıklar, çalışıyormuş gibi görünen programların içinde sessizce yatıyor.

İnsanların tüm kodu okumasına gerek yok. Programın doğruluğunu makine kontrolleri ve başka bir yapay zekânın denetimi izliyor. Sonucun dükkânın amacına uyup uymadığını işletmeci izliyor. Okumanıza gerek yok ama doğrulamayı atlamamalısınız. Bir ajan tabanlı yapay zekâyla kurmanın anlamının bu olduğuna inanıyorum.

【Şekil 2-3】Dışarıdan okunabildiği zamanki kurallar ve düzeltmeden sonraki kurallar (alıntı) *(Ekran Japonca.)*

### 2-4 Gelişigüzel Kurmak Çelişkileri Çoğaltır

Ne kadar çok özellik eklersem, daha önce karar verdiklerimle çatışan o kadar çok kısım oluyordu.

Tipik örnek, indirim hesaplamasıydı. Rezervasyon formunda, onay ekranında, e-postada ve yönetim ekranında indirim hesaplaması her yerde ayrı ayrı yazılmıştı. Bir indirim kuralını bir yerde değiştirirsem, başka bir yer eski kuralla hesaplamaya devam ediyordu. Aynı rezervasyon için ekran ve e-posta farklı tutarlar gösterebiliyordu.

Daha sonra fiyat hesaplamasını tek bir dosyada topladım. Rezervasyon formu, sohbet penceresi ve MCP sunucusu fiyatları oradan üretiyor.

İndirimlerin üst üste bindirilme kuralları da yol boyunca değişti. 1. bölümde yazdığım gibi happy hour başta diğer indirimlerle birleştirilebilir olacaktı, ama kâr getirmeyeceğini görüp birleştirilemez olarak değiştirdim. Bir kural her değiştiğinde, nerelerin düzeltileceğini bir insanın hatırlaması gerekiyordu. Gelişigüzel kurulmuş bir sistemin zayıflığı buydu.

Test ortamı ile üretim arasında da bir uyuşmazlık vardı. Sohbet penceresini test ederken "%10 indirim gibi bir şey yok muydu?" sorusu, test ortamındaki indirim kurallarının canlıdan sapmış olduğunu ortaya çıkardı. Test ortamındaki değerler canlıdan farklıysa testleri geçip canlıda hatalı sonuç alabilirsiniz. O zaman karar verdiğim şey "canlı doğrudur" ilkesiydi. O zamandan beri her test çalıştırmasından önce canlı ayarları test ortamına kopyalıyor ve uyuşmazlığın sıfır olduğunu doğrulayıp öyle çalıştırıyorum.

Yapay zekâ kendisine söyleneni kurar. Ama önceki kararlarla çelişkileri fark etmez. Çelişkileri önleyen yapay zekâ değildir. Her şeye önceden karar vermektir.

### 2-5 Gereksinim Tanımını Yeniden Öğrenmek

Gelişigüzel kurduğum rezervasyon sisteminin hatalarından ders çıkararak gereksinim tanımını yeniden öğrendim. Gereksinim tanımı, kurmadan önce neyi kuracağınıza, neyi kurmayacağınıza, kimin ve nasıl kullanacağına karar vermek ve bunu bir belgeye yazmak demektir.

Sistem mühendisi olduğum günlerde doğal olarak yaptığım bir şeydi. Ama yapay zekâyla kurabildiğim andan itibaren, fark etmeden atlamıştım. Ona bir fikir söyleyin, dakikalar içinde çalışan bir şey belirir. O hızın içinde karar verme adımını es geçmiştim.

Şimdiki kurma biçimim üç aşamalı.

1. Önce gereksinimlere ayrıntılı karar verin. Ne kurulacak, ne kurulmayacak, kim kullanacak. Her ekranın davranışı. İstisnaların (hatalar, çift basma, süre dolması) nasıl ele alınacağı. Fiyatlar ve indirimler gibi sonradan kolayca çelişkiye düşen kuralları özellikle ayrıntılı kararlaştırıyorum. Bu işi de sohbet yapay zekâsıyla diyalog içinde yapıyorum. Yapay zekâya önceden açıkları ve çelişkileri buldurtuyorum ve işletmeci karar veriyor.
2. Kararlaştırılanı bir "gereksinim belgesi" olarak yazın. Sözlü ya da anlık talimatlar değil, tek bir belgede toplanmış hâlde. Bu, sonradan neyin doğru olduğunu kontrol etmek için tek ölçüt olur.
3. Belgenin tamamını yapay zekâya verin ve uygulatın. Belgenin tamamını programı yazan yapay zekâya (Claude Code), geçme koşullarıyla (tüm testler geçer, canlıdan önce test ortamında kontrol vb.) birlikte veriyorum. Yapay zekâ koşulları karşılayana kadar kendi başına kurar ve kendi başına kontrol eder. İşletmeci yalnızca yarı yolda durduğunda ve son kontrolde bakar.

Örneğin "T-AI-MURO" sohbet penceresinin gereksinim belgesi ilk sürümden üçüncüye kadar yeniden yazıldı. İkinci sürümde "yapay zekânın fiyatları hesaplamasına izin verme," "dükkânın bilgisini ve fiyat hesaplamasını tek bir pencereye koy" ve "sohbetle rezervasyon yapmak istemeyenler için formu da tut" kararlarını verdim. Üçüncü sürümde "dükkân bilgisinin ana kopyasının nerede tutulacağı," "boş saatleri yalnızca bu pencere gösterir," "diyaloğun ilk turunu dört seçenekli bir soru yap" ve "sohbet kayıtlarını kaydetme; yalnızca cevaplanamayan soruları sakla" kararlarını verdim. Kararlar bir belgede kaldığı için, işlerin neden böyle olduğunu sonradan izleyebiliyorum.

Bu kurma biçimiyle, özellik ekleyince bile belgeyle karşılaştırarak çelişkileri hemen fark edebiliyorum. Kurmayı yapay zekânın yaptığı bir çağda, tam da kurmadan önceki "karar verme gücü" gerekiyor. Rezervasyon sisteminden öğrendiğim en büyük ders buydu.

Bu kurma biçimini yeni bir ürün başlattığım her seferde aynı şekilde yürütebilmek için, prosedürün kendisini bir belgeye koyup yapay zekâya veren bir mekanizma da kurdum. Bunu 4. bölümde yazacağım.

【Şekil 2-4】T-AI-MURO gereksinim belgesinin içindekiler tablosu (3. sürüm) *(Ekran Japonca.)*

### 2-6 Arayüzün Dilini Öğrenmek

Yeniden öğrendiğim bir şey daha var: ekran bileşenlerinin adları.

Yapay zekâya "şuraya şunu yap" dediğimde bile ekran sık sık beklediğim gibi çıkmıyordu. Nedenini düşündüğümde ekran bileşenlerinin adlarını bilmediğimi gördüm. "Üstte beliren küçük bir pencere" ya da "birkaç saniye sonra kaybolan bir bildirim" diye tarif etsem bile yapay zekânın ne kastettiğimi anlaması zordu.

Bu yüzden arayüz (kullanıcı arayüzü, bir ekranın görünümü ve kullanımı) üzerine bir başvuru kitabı okudum ve bileşenlerin adlarını ve tasarımın teknik terimlerini öğrendim.

| Bileşen | Nedir |
| --- | --- |
| Modal | Ekranın üzerinde beliren küçük bir pencere. Kapatana kadar arkadaki ekranı kullanamazsınız |
| Toast | Ekranın kenarında birkaç saniye görünüp kendiliğinden kaybolan bir bildirim |
| Sekme | Bir başlığa basınca içeriğin değiştiği bir mekanizma |
| Akordeon | Bir başlığa basınca içeriğin açılıp kapandığı bir mekanizma |
| Çekmece | Ekranın kenarından bir çekmece gibi kayarak çıkan bir menü |
| Diğerleri | Ekmek kırıntısı menü (kullanıcıya o an nerede olduğunu gösteren bir iz), karusel (yana kaydırdığınız öğeler), alt panel (bottom sheet) (ekranın altından yükselen bir panel) ve benzerleri. Öğrendiğiniz her ad, yapay zekâya tek bir ifadeyle talimat vermenizi sağlar |

Bileşen adlarıyla talimat verdiğinizde, yapay zekânın ürettiği ekranlar ilk denemede hedefe yaklaşır. "Rezervasyon onay ekranını modal olarak göster" derseniz yapay zekâ tereddüt etmez.

#### Yapay zekâ ekleme ile kesme arasında uçlara savruluyor

Sözcükleri öğrendikten sonra bile yapay zekâyla ekran kurmanın farklı türden bir zorluğu vardı. Yapay zekâ aşırı uçlar arasında gidip geliyor.

Rezervasyon sitesinde "şık" bir üst bilgi istediğimde etkileyici, kalın bir üst bilgi aldım. Ama bir rezervasyon sitesinin bütün amacı rezervasyondur. Her seferinde rezervasyon yapan müdavimler için uzun açıklamalı kalın bir üst bilgi sadece sıkıntıdır. Aynı miktarda bilgiyi koruyarak dikey uzunluğu yaklaşık yarıya kestirdim.

E-posta alt bilgisini standartlaştırıp İkinci Mekân Defteri'ne bir bağlantı eklediğimde, ana metin buna kıyasla sönük ve yetersiz görünmeye başladı. Bu yüzden ana metne de bir başlık, ana noktaların bir tablosu ve basılacak bir düğme ekledim. Alt bilgiye sohbet penceresi için bir giriş eklediğimde dağınık göründü. Onu çizgilerle ayrılmış iki satırlık bağlantıya sıkıştırdığımda derli toplu ama göze çarpmaz oldu. Sonunda rolü "ne zaman kullanılacağına" göre gösteren iki karta yerleşti. Sol taraf "bir sonraki rezervasyonunuz için", sağ taraf "yemekten sonra".

Çok kalın, çok kırpılmış, çok belirgin. Doğru noktaya karar veren her seferinde işletmecinin sözüydü.

#### Resimsiz bir tasarım önerisi

Bu da oldu. Program yazan yapay zekâya bir tasarım yapay zekâsı (Claude Design) kullanarak sohbet penceresi için iyileştirme önerileri oluşturmasını söyledim ve "Sekiz ekran için öneriler hazırladım" diyen bir rapor geldi. Ama açtığımda yalnızca metin açıklaması vardı. Yapay zekâ resim çizememişti, yine de geriye yalnızca "tamam" raporu kalmıştı.

Sonunda sohbet tarafındaki yapay zekâ dört öneriyi doğrudan tasarım ekranında çizdi. Mevcut ekranın renklerini bir ekran görüntüsünden aldı, dükkânın tarihini bir zaman çizelgesine koydu, lezzet profilini "pişirme yöntemi" ve "tat" olmak üzere iki çerçeveye böldü, planları açıklama kartlarına çevirdi ve fiyatları bir rezervasyon özetinde birleştirdi.

Yapay zekâya bir test çalıştırttığınızda "geçti" der. Yapay zekâdan bir tasarım istediğinizde "tamam" der. İçindekini kontrol etmek bir insanın işidir. Karar verme ölçütünü belirleyecek ve elinde tutacak olan yalnızca insandır.

#### Bu bölümden çıkarılacak dersler

- Çalışan bir şey kurmak ile onu güvenle işletebilmek farklı şeylerdir.
- Yapay zekânın çıktısını yapay zekânın sözleriyle değil, testlerle kontrol edin. Bir teste, bir şeyi bozduğunuzda başarısız olduğunu kontrol ettikten sonra güvenilebilir.
- Fiyatlar gibi yanlış olmaması gereken hesaplamaları yapay zekânın metin üretimine bırakmayın. Programa verin.

Bu bölümün devamı (yeni bulunan açıklar ve onları düzeltmek için attığım adımlar) note ve X'te. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Bölüm 3: Dükkânımızın Araçlarını Başka Dükkânlara Dağıtmak

### 3-1 Rezervasyon Sayfasındaki Küçük Yeşil Tabela

Tamuro'nun rezervasyon sayfasını açın ve üste yakın küçük yeşil bir tabela göreceksiniz. Dükkân açıkken "OPEN", kapandığında "CLOSED" yazıyor. İşletmeci uzat düğmesine bastığında kapanış saati 30 dakika ileri kayıyor ve tabelada kırmızıya çalan turuncu bir ton beliriyor.

Bağımsız restoranların ortak bir özelliği vardır. Neredeyse tam zamanında açarlar, ama kapanış çoğu zaman uzar. Müşterilerle sohbet canlıysa, dükkânın ışıkları 22.30'daki son siparişi geçip yanmaya devam eder.

Ama müşteri tarafından bunu göremezsiniz. Google Haritalar'daki "Açık" göstergesi yalnızca kayıtlı saatlere göre belirleniyor, bu yüzden ne uzatmaları, ne erken kapanışları, ne de geçici kapanışları yansıtıyor. Hiç kimse "Belki hâlâ açıktır" diye düşünerek kapanış saatini geçmiş bir dükkâna yürümez. Arayıp sormaya da insan çekiniyor.

Bu tabela, o "Hâlâ açık mı?" sorusunu cevaplayan bir araç. Adı "AgendaLuce (Işık Defteri)". Luce, İtalyanca "ışık" demek.

Işık Defteri, işletmecinin neredeyse hiç dikkatini gerektirmeden çalışacak şekilde kurulmuş. Haftanın her günü için açılış ve kapanış saatlerini bir kez kaydedin, tabela otomatik olarak açılıp kapanıyor. İşletmeci ona yalnızca uzatırken, erken kapatırken ya da bir gün izin alırken dokunuyor. Uzatmak için akıllı telefonunuzda bir düğmeye basıyorsunuz. Çalışanlar da oturum açmadan çalışan özel bir bağlantıdan kullanabiliyor.

Müşterilerin oturum açmasına ya da kaydolmasına gerek yok. Herkese açık sayfayı açın, ışığın şu anki durumunu görebilirsiniz. Akıllı telefonunuzun ana ekranına eklerseniz bir uygulama gibi çalışır. Küçük tabela bileşeni başka web sitelerine de gömülebiliyor. Tamuro'nun rezervasyon sayfasında görünen şey bu bileşen.

Işık Defteri ücretsiz. Tabela bileşenini yalnızca web sitenize gömerseniz, kurulum yaklaşık 10 dakika sürer.

Ve işte önemli kısım. Bu Işık Defteri yalnızca Tamuro için değil. Her dükkân kullanabilir.

Tabelanın tasarımından dükkânın adını bilerek koymadım. Üzerine bir ad koysaydım, Tamuro'nun tabelası olurdu. Gösterim dilini de seçebilirsiniz. Bileşeni, her dükkânın web sitesine gömülebilsin diye küçük yaptım.

Tamuro'nun "kapanış uzuyor" sorunundan doğan, baştan herkesin kullanabileceği bir biçimde yapılmış bir araç. Işık Defteri bu. Ve onun gibi araçların koleksiyonu "Agenda serisi."

【Şekil 3-1a】Rezervasyon sayfasının üstündeki Işık Defteri tabelası (açık) *(Ekran Japonca.)*

【Şekil 3-1b】Uzatma sırasında kırmızıya çalan turuncu bir ton beliriyor *(Ekran Japonca.)*

【Şekil 3-6a】İşletmecinin ekranı. Uzatmak için düğmeye bir kez basın *(Ekran Japonca.)*

【Şekil 3-6b】Uzat düğmesine basıldıktan hemen sonra. Kapanış saati 30 dakika ileri kayıyor *(Ekran Japonca.)*

【Şekil 3-6c】Müşterilerin gördüğü herkese açık sayfa (uzatma sırasında) *(Ekran Japonca.)*

### 3-2 Siyah Deri Defterle Başladı

Agenda serisi bir seri olarak planlanmadı. Henüz yayımlanmamış tek bir sistemle başladı.

İlk kurmaya giriştiğim şey, müşterilerin yüzlerini tanıyan ve müdavimleri karşılayan bir mekanizmaydı. Dükkânın girişindeki bir kamera ziyaretçileri yüzlerinden ayırt ediyor ve işletmeciye haber veriyor: "Geçen sefer tonteki yiyen, üç aydır görmediğimiz kişi o." Küçük bir dükkânın işletmecisinin kafasında yaptığı işi, yani yüzleri, adları ve tercihleri hatırlamayı, bir makineye yaptırmayı düşündüm.

Ama kurmaya başladıktan kısa süre sonra, bunun çok ağır bir şey emanet edilen bir sistem olduğunu fark ettim. Yüzler. Nitelikler. Ziyaret geçmişi. Bir müşterinin karakteri. Hepsi, bir kez sızdığında asla geri alınamayacak bilgiler.

O sırada aklıma Seichō Matsumoto'nun "Siyah Deri Defter"i geldi. Kimseye gösterilmeyen ama kesinlikle var olan bir kayıt. Açıldığında insanların kaderini belirleyen bir defter. Kurmaya çalıştığım şey tam olarak bu değil mi?

İtalyancada "defter" Agenda, "siyah" ise Nera. Bir araya gelince: AgendaNera. Siyah deri defter. Adı ilk böyle belirlendi.

AgendaNera hâlâ yapım aşamasında. Seride en özenle kurduğum.

Ve bu adlandırma bir tetikleyici oldu. Siyah bir defter varsa, başka renklerde defterler de olabilir. Kendi dükkânımda her gün kullandığım mekanizmaları, her dükkânın kullanabileceği biçimlere yeniden kuracak ve teker teker birer defter olarak yayımlayacaktım. İşte [Agenda serisi](https://bontallc.com/agenda?via=b2-tr-{{FMT}}) tam olarak bu.

### 3-3 Defterleri Teker Teker Eklemek

Agenda serisi, her biri bir restoranın bir sorununu tek bir araçla cevaplayan küçük web uygulamalarının bir derlemesi. Her birinin İtalyanca bir adı ve "defter" ile biten Japonca bir lakabı var. Her adın kendi kökeni var.

| Ad | Lakap | Adın kökeni | Ne yapar |
| --- | --- | --- | --- |
| AgendaTimbro | Mesai Defteri | Timbro "damga" demek. Giriş çıkış kaydının ta kendisi | Çalışanların giriş ve çıkışını kaydeder |
| AgendaOro | Kârlılık Defteri | Oro "altın" demek. Para defteri | Bir dükkân açmanın ya da yeni bir menü kaleminin kârlılığını tahmin eder (ücretsiz) |
| AgendaBis | İkinci Mekân Defteri | Bis "bir daha" demek. Bir konserde seyircilerden bağırılan "Bis!" | Müşterileri yakındaki bir sonraki durağa yönlendirir (ücretsiz) |
| AgendaQA | Destek Rehberi | Qua "burada" demek. Sıkıntıdayken, burada | Serinin ortak yardım masası (ücretsiz) |
| AgendaLuce | Işık Defteri | Luce "ışık" demek | Dükkânın açık olup olmadığını gösterir (ücretsiz) |
| AgendaRicetta | Maliyet Defteri | Ricetta "tarif" demek | Bir tarifin maliyetini ve maliyet oranını hesaplar (ücretsiz) |
| AgendaNera | Müdavim Defteri | Nera "siyah" demek. Siyah deri defter | Yüz tanımayla müdavimleri karşılar (yapım aşamasında) |
| AgendaTurno | Vardiya Defteri | Turno İtalyanca "sıra" ya da "nöbet vardiyası" demek | Çalışanların vardiya taleplerini toplar ve işletmecinin kendi yapay zekâsının hazırladığı çizelgeyi dağıtır (yakında) |

Hangi defter hangi tür dükkâna uygun? Mesai Defteri, personel devamını kâğıtta ya da LINE'da *(Japonya'nın en yaygın kullanılan mesajlaşma uygulaması)* yöneten, iki veya daha fazla çalışanı olan dükkânlar için. Kârlılık Defteri, dükkân açmak üzere olanlar ve kira ya da maliyetler değiştiği için rakamlarını gözden geçirmek isteyenler için. İkinci Mekân Defteri, müşterileri bir sonraki yere erkenden göndermek isteyen, yemek odaklı dükkânlar için. Işık Defteri, kapanışı planlanandan daha geç ya da daha erken olan bağımsız dükkânlar için. Maliyet Defteri, tarifleri kafasında olan ama hiç maliyet oranı hesaplamamış dükkânlar için.

#### Mesai Defteri bordro hesaplamaz

Mesai Defteri, dükkânın tabletini ya da çalışanların akıllı telefonlarını olduğu gibi bir giriş çıkış makinesine çeviriyor. Sadece adınıza dokunun. Devam çizelgesi otomatik toplanıyor ve CSV olarak (elektronik tablo yazılımında açılan bir biçim) dışa aktarılabiliyor. İş günü 05.00'te başlıyor, bu yüzden gece geç saatlere kadar çalışsanız bile tarih bir sonraki güne sarkmıyor.

Ama bu Mesai Defteri bilerek bordro hesaplamıyor.

Saatlik ücretler, ek ödenekler ve kesim tarihleri dükkândan dükkâna çok farklı. Gece geç saati %25 ek ücretli, tatiller ayrı bir kategori, ulaşım günlük tutarla. Nasıl kurarsam kurayım, birinin dükkânına uymazdı.

Bu yüzden hesaplamak yerine "bir yapay zekâya verilecek talimatların bir şablonunu" hazırladım. İşletmeci indirilen devam CSV'sini ve bu şablonu, ChatGPT, Claude ya da Gemini, normalde kullandığı hangi yapay zekâ olursa olsun, olduğu gibi yapıştırıyor. Ardından yapay zekâ gece geç saati primlerini, tatil ücretini ve ulaşımı hesaplıyor ve listeliyor. "Hesabı ay sonunda kesiyoruz, gece geç saati %25 ek, Pazarlar ayrı bir kategori" gibi her dükkânın kuralları şablona eklenebiliyor ve olduğu gibi yansıtılıyor. CSV, yapay zekânın doğru hesaplayabilmesi için haftanın günü ve tatil adı sütunlarını içeriyor.

Hesaplama mekanizmasını ben tutmuyorum; her dükkân kendi kurallarını kendi elinde tutuyor. En zor bozulan yolun bu olduğunu düşündüm.

#### Onları bir sonraki durağa yönlendirin ve kendi dükkânınızı hafızalarında bırakın

İkinci Mekân Defteri, müşterilere verilecek bir "sonraki durak rehberi sayfası" yapmaya yarayan bir araç. Yemeğini bitirmiş müşterileri yakındaki bir bara ya da geceyi noktalamak için son bir mekâna, yürüyerek kaç dakika sürdüğüyle birlikte yönlendiriyor.

Müşterileri başka yere gönderen bir araç gibi görünüyor ama içinde küçük bir incelik var. Birini ikinci durağa yönlendirmek, ilk durağın sizin dükkânınız olduğunu ima eder. Müşterileri gönderiyormuş gibi görünürken aslında "ilk durak bu dükkândı" bilgisini hafızalarına kazıyor. Böyle tasarlandı.

#### Üç tasarım ilkesi: otomatik, ödünç alınan güç, tek işlev

Agenda serisindeki tüm defterler üç ilkeyi paylaşıyor.

Birincisi "otomatik." İşletmeci her gün dokunmadan çalışmalı. Işık Defteri'nde, çizelgeyi kaydettiğinizde ışık kendiliğinden açılıp kapanıyor. Bir restoran işletmecisinin serviste bir ekrana dokunacak zamanı yok. Dokunmadığınızda çalışmayan bir araç eninde sonunda kullanılmaz hâle gelir.

İkincisi "ödünç alınan güç." Her şeyi kendiniz kurmayın; işi işletmecinin zaten kullandığı araçlara ve yapay zekâya bırakın. Mesai Defteri'nin bordrosu örnek vaka. Vardiya defteri de aynı: yalnızca çalışanların tercihlerini toplama işini yapıyor ve vardiyaları kurma işini işletmecinin kendi yapay zekâsına bırakıyor. Kendi karmaşık bir mekanizmasını ya da bir yapay zekâyı çağırma maliyetini taşımıyor. Bu yüzden fiyat düşük tutulabiliyor.

Üçüncüsü "tek işlev." Bir defter yalnızca tek bir şeyi, güvenilir biçimde yapar. Çok işlevli bir sistem bağımsız bir dükkân için fazla ağır. Özellik eklemeye devam ederseniz kullanımı zorlaşır ve kuran tarafın tutarsızlıkları çoğalır. Bunu 2. bölümdeki rezervasyon sistemiyle bizzat öğrendim. Bu yüzden defterleri teker teker ekliyorum ve her biri "yalnızca bu tek şeyi düzgünce" yapıyor.

#### Rezervasyon sistemi neden seride değil

Bu noktada bariz bir soru bekliyorum. Tamuro'nun en çok emek verdiği şey rezervasyon sistemi. Neden onu Agenda serisine koymuyorum?

Aslında bir keresinde niyetim buydu. Plan, rezervasyon sistemini diğer restoranların kullanabileceği bir biçime getirmek ve serinin bir defteri olarak yayımlamaktı. Ama Ağustos 2026'da bu planı iptal ettim.

Neden, tam olarak 1. bölümde yazdığım şey. Tamuro'nun rezervasyon sistemi Tamuro'nun iş yapış biçimiyle dolu. Müşterilerin yarısının yalnız yemek yiyenlerden oluşması. Rezervasyonların neredeyse %90'ının aynı gün yapılması. Açılıştan önceki zamanı satmak istiyorum. İnsanların gruplar hâlinde gelmesini istiyorum. Müdavim kazanmak istiyorum. İndirim kombinasyonlarını, e-postaların sırasını ve sohbetin öneri biçimini hep buna uysun diye kurdum.

Herkesin kullanabileceği bir şeye seyreltirsem, her dükkâna şöyle böyle uyan sıradan bir rezervasyon sistemi olurdu. O zaman Tamuro'nun gücü yok olurdu. Rezervasyon sistemi ve CRM, dükkânın kendini tanıtma ve sunma biçimidir. Dükkânı genel bir sisteme uydurmak yerine, dükkânın sistemini dükkâna uydurun. Bizim dükkânımız, kendi kurallarımızla. Bu yüzden Tamuro'nun rezervasyon sistemini yalnızca Tamuro'nun olarak tutmaya karar verdim.

Peki dükkânın ötesinde verilecek bir şey yok mu? Öyle değil. Rezervasyon sisteminin çevresinde her dükkânda ortak olan birçok küçük sorun var. Dükkânın çekirdeğini kendi kurallarınıza göre tutun. Çevredeki sorunları çözen araçları baştan herkesin kullanabileceği bir biçimde kurun ve dağıtın. Tamuro'nun rezervasyon sayfası, ikisini tek bir ekranda yan yana getiren bir örnek. Yalnızca Tamuro'ya ait bir rezervasyon sisteminin üstünde, herkesin kullanabileceği Işık Defteri tabelası duruyor.

【Şekil 3-2】Agenda serisi tanıtım sayfası *(Ekran Japonca.)*

【Şekil 3-3a】Mesai Defteri tanıtımı *(Ekran Japonca.)*

【Şekil 3-3b】Kârlılık Defteri tanıtımı *(Ekran Japonca.)*

【Şekil 3-3c】İkinci Mekân Defteri tanıtımı *(Ekran Japonca.)*

【Şekil 3-4】Mesai Defteri'nin giriş çıkış ekranı. Sadece adınıza dokunun (yapay veri) *(Ekran Japonca.)*

### 3-4 Baştan Herkes İçin Kurmak

Kendi dükkânım için bir araç yapıyorum, sonra başka dükkânlara da dağıtıyorum. Söylenince basit geliyor, ama bunu yapmak için kurmaya başlamadan önce karar verme biçiminin değişmesi gerekiyor.

Yalnızca Tamuro için kursaydım, en hızlı yol Tamuro'nun çalışma saatlerini ve Tamuro'nun adını doğrudan programa yazmak olurdu. Ama o zaman başka hiçbir dükkân kullanamazdı. Sonradan genel amaçlı yapmaya çalışırsanız, sabit kodlanmış her yeri bulup tek tek düzeltmeye mecbur kalırsınız.

Bu yüzden Agenda serisindeki araçlar baştan herkesin kullanabileceği varsayımıyla gereksinim belgesine bağlanıyor. Tamuro'daki bir sorundan yola çıkıyorum, ama gereksinim aşamasında iki soruyu ayırıyorum: "Bu yalnızca Tamuro için mi doğru, yoksa her dükkân için mi?" Tabelaya dükkânın adını koymayın. Dili seçtirin. Herhangi bir web sitesine yapıştırılabilir yapın. Bunun gibi kararları Işık Defteri'nin gereksinim belgesini yazarken kesinleştirdim.

Bu, 2. bölümde yeniden öğrendiğim gereksinim tanımının bir başka kullanımı. Bunlara önceden karar verirseniz, aracı Tamuro'da kullanabilir ve olduğu gibi başka dükkânlara dağıtabilirsiniz.

Benim dükkânımdaki sorunlar başka dükkânlardaki sorunlar da. Müşterilere kapanış saatinin uzadığını söylemek isteyen tek işletmeci ben değilim. Bağımsız bir dükkânın işletmecisi kendi sorunundan bir araç kuruyor, sonra onu başka dükkânlara dağıtıyor. Agenda serisinin arkasındaki fikir bu.

### 3-5 Teknolojinin Demokratikleşmesi

Agenda serisi artık 10'dan fazla ürüne sahip. Onları barın arkasında dururken tek başıma kuruyor ve işletiyorum.

Birkaç yıl önce bu düşünülemezdi. Bir ürün kurmak için onu planlayacak, ekranları tasarlayacak, kodu yazacak, test edecek ve işletecek ayrı ayrı insanlara ihtiyaç vardı. Bir ekip ve sermaye olmadan dünyaya bir ürün çıkaramazdınız.

Artık öyle değil. İşletmeci yapay zekâya gereksinimleri söylüyor, yapay zekâ kodu yazıyor, yapay zekâ test ediyor ve başka bir yapay zekâ denetliyor. İşletmecinin yaptığı, neyin kurulacağına karar vermek, yapay zekânın sonuçlarının dükkânın amacına uyup uymadığına karar vermek ve yalnızca insanların yapabileceği işlemleri yapmak.

Bu tür bir değişime genel olarak "teknolojinin demokratikleşmesi" deniyor. Kurma gücü artık yalnızca birkaç kişinin ya da şirketin tekelinde değil.

Ama burada dürüst olayım. Girişte yazdığım gibi yaklaşık 16 yıl BT sektöründe, çoğunlukla sistem planlamasında ve sahadaki insanlarla yazılım firmaları arasında koordinatör olarak çalıştım. Gereksinim tanımını, veri tabanları hakkında düşünmeyi ve test yürütmeyi deneyimden biliyordum. Bu yüzden hiç kod satırı yazmamış birinin yarından itibaren aynısını yapabileceğini iddia etmeyeceğim.

Yine de çok şey değişti. Artık ana işimin aralarında, tek başıma, bir zamanlar bir ekip gerektiren ölçekte şeyler kurabiliyorum. Ve deneyimi olmayan insanlar için giriş eşiği kesinlikle düştü. Anlamadığınız bir şeyi sorarsanız yapay zekâ size öğretir. Sözcüklerle söylediğinize şekil verir. Eksik olan teknik değil, neyin kurulacağına karar verme yeteneği ve yapay zekâya söyleyecek sözcükler. Bunlar zaten dükkân işleten insanların her gün kullandığı yetenekler.

### 3-6 "SaaS'ın Ölümü" Tartışması

Agenda serisi gibi, insanların internet üzerinden aylık bir ücret karşılığında kullandığı yazılıma SaaS (hizmet olarak yazılım) deniyor. Muhasebe yazılımı, mesai ve devam yönetimi, rezervasyon yönetimi. Bugünün restoranları çok sayıda SaaS üzerinde işliyor.

Yapay zekâ SaaS'ı bitirecek mi? 2026'da bu tartışma iyice alevlendi.

Tetikleyicilerden biri Microsoft CEO'su Satya Nadella'nın bir sözüydü. Aralık 2024'te bir podcast'te Nadella, yapay zekâ ajanları çağında SaaS uygulamalarının çökeceğini söyledi. Gerekçe: yapay zekâ ajanları iş süreçlerindeki karar verme kısmını devraldığında, insanların ekranlar aracılığıyla kullanması için yapılmış yazılıma artık ihtiyaç kalmayacak.

Sonra Şubat 2026'da Anthropic, Claude Cowork'ü (iş görevlerini özerk biçimde yürüten bir yapay zekâ aracı) duyurdu ve Amerikan yazılım şirketlerinin hisseleri ağır biçimde satıldı. Wall Street'te bu düşüş "SaaSpocalypse" diye anılır oldu. Yatırımcıların korktuğu şey, yapay zekâ ajanları işi yaparsa kişi başına ücret kazanma modelinin (koltuk başına fiyatlandırma) dağılacağıydı.

Karşı argümanlar da var. Nvidia CEO'su Jensen Huang, yapay zekâ ajanlarının yazılımın yerini almayacağını, insanlar adına yazılımı kullanacağını söyledi ve satışı aşırı tepki olarak nitelendirdi. Bir hayli kişi de yapay zekâyı özümseyen SaaS'ın daha çok güçleneceğini düşünüyor.

SaaS gerçekten ölecek mi? İşte düşüncem.

Ölen şey, SaaS'ın orta katmanı: koltuk başına yüksek aylık ücret alan ve insanların ekranlar üzerinden kullandığını varsayan türü. Yapay zekâ işi insanların yerine yaparsa, her kişi için koltuğa ihtiyacınız kalmaz. Ekranı kullanan kimse yoksa, özenle hazırlanmış bir ekrana ihtiyacınız kalmaz.

Geriye kalanlar, ucuz olan ve tek bir şeyi güvenilir biçimde yapan araçlar. Ve yapay zekânın kullanması kolay araçlar.

Bu, tam olarak Agenda serisinin üç ilkesi. Otomatik çalışıyor, işletmecinin yapay zekâsına bırakılıyor (dış güce, yani yapay zekâya emanet etme) ve yalnızca tek bir şey yapıyor (tek işlev). AgendaTurno vardiya çizelgesini kurma işini işletmecinin yapay zekâsına bırakıyor, bu da Huang'ın tarif ettiği "yapay zekânın yazılımı kullanması" biçiminin ta kendisi. Tamuro'nun rezervasyon sistemi müşterilerin yapay zekâlarına MCP aracılığıyla bir pencere açıyor ve bu da aynı fikir.

Elbette burada bir çelişki varmış gibi görünebilir. SaaS'ın ölümünden söz ediyorum ama Agenda serisinin kendisi SaaS. Ancak Agenda serisi, bir işletmecinin kendi dükkânı için kurup sonra düşük bir fiyatla herkese açtığı bir araçlar dizisi. Koltuk başına yüksek aylık ücret alan bir model değil ve insanların her gün ekrana yapışıp oturduğunu varsaymıyor. Baştan yapay zekânın kullanacağı varsayımıyla kuruldu.

#### Restoranlar İçin "SaaS'ın Ölümü"

Bu tartışma yatırımcılar ve BT sektörüyle ilgili bir hikâye gibi gelebilir. Ama restoranlar için aynı şey çok daha tanıdık bir biçimde gerçekleşmek üzere.

Pek çok bağımsız dükkân gurme sitelerine ve rezervasyon sitelerine aylık ücret ödüyor ve buna ek olarak her rezervasyon için bir yönlendirme komisyonu ödüyor. Müşteri getirmenin karşılığında site müşteriyle olan bağı elinde tutuyor ve dükkânın müşterinin iletişim bilgisine bile sahip olmaması nadir değil. Siteler ücretleri artırırsa dükkânın buna uymaktan başka çaresi yok, sıralama sistemi değişirse müşteri akışı değişiyor.

1. bölümde yazdığım gibi 2026'da müşterilerin dükkânları kendi yapay zekâlarına arattığı çağ başladı. Giriş kanalı yapay zekâya kayarsa, bir siteye aylık ücretler ve komisyonlar ödeyerek listelerinde yüksek yer alma düzeninin tamamı sallanmaya başlıyor. Bir dükkân kendi başına yapay zekâya bir pencere açarsa, müşteriler büyük sitelerden geçmeden ona ulaşabilir. Rezervasyon kayıtları ve müşteriyle ilişki dükkânın elinde kalır.

"SaaS'ın ölümünü" bağımsız bir dükkânın sözcükleriyle söylemem gerekirse, bu "ödeyince listelendiğiniz çağın sonu." Tamuro buna hazırlık olarak penceresini MCP üzerinden açtı ve rezervasyonlarını ve CRM'ini kendi ihtiyaçlarına göre kurduğu yapıda tutuyor.

SaaS'ın ölüp ölmeyeceğini henüz kimse bilmiyor. Ama yapay zekâ çağında kalacak araçların şekli yavaş yavaş görünür oluyor. Düşüncem bu.

### 3-7 Para Kazanma: Küçük, Çok, Ucuz

Agenda serisini bir iş olarak ayakta kalacak şekilde kuruyorum. Amaç, onu restorandan ayrı ikinci bir gelir kaynağı yapmak.

Fiyatları küçük ve düşük belirledim. Aylık ücretler birkaç yüz yenden başlıyor. Örneğin Mesai Defteri ayda ¥500 (yaklaşık $3,3). Kârlılık Defteri, Işık Defteri ve Maliyet Defteri gibi ücretsiz araçlara da yer veriyorum. Ücretsiz araçlar, insanların Agenda serisini tanıdığı giriş kanalı olarak işlev görüyor. Işık Defteri ne bir harita API'si ne de üretken yapay zekâ kullandığı için işletme maliyeti neredeyse sıfır. Bu yüzden ücretsiz verebiliyorum.

Tek bir hesap var. AgendaID adlı ortak bir hesapla serideki her aracı kullanabilirsiniz. Her araç için yeniden kaydolmanıza gerek yok. Ücretli araçlar üç aylık ücretsiz dönemle geliyor ve kart kaydı yapmadan başlatılabiliyor. Ücretsiz dönem, her dükkân ve ürün kombinasyonu için yalnızca bir kez kullanılabilir. Başka bir dükkânı tavsiye ederseniz bir bonus kazanırsınız.

Fiyatları düşük tutabilmemin nedeni kurma biçimimde. Tek başıma kuruyorum, kurma işini yapay zekâya yaptırıyorum ve ortak bir temeli yeniden kullanıyorum. Veri tabanı maliyeti tüm seri için ayda yaklaşık $35'te tutuluyor. Hem kurma maliyeti hem de işletme maliyeti küçükse, bir iş küçük satışlarla bile ayakta durabilir.

Dürüst olayım. Bu kitabı yazarken bazı dükkânlar araçları denedi ama ücretli kayıt neredeyse hiç yok. Kurma tarafı hazır, ama insanların bundan haberdar olmasını sağlayacak tanıtım tarafı henüz yolun başında. Bu kitap da tam bu amaç için, seriyi insanlara tanıtmak için bir araç olarak düşünüldü.

#### Bir Şey Kurmak ile İnsanların Kullanmaya Devam Etmesi Farklı Şeyler

Bir şeyi daha dürüstçe söyleyeyim. Bir araç kurabilmek ile birinin onu kullanmaya devam etmesi ayrı konular.

Kurmak yapay zekâ sayesinde hızlandı. Ama insanların kullanmaya devam etmesini sağlamak başka işler gerektiriyor. Nasıl kullanılacağı hakkındaki soruları cevaplamak (Destek Rehberi bunun için var). Ücretsiz dönem bitmeden bir bildirim göndermek. Bir fiyatı artırırken nedenini açıklamak. Biri iptal etmeyi istediğinde veriyi düzgünce silmek. Ve her şeyden önce, işletmeci dokunmadan çalışır durumda tutmak.

Agenda serisinin üç ilkesi arasında "otomatik", bu "kullanmaya devam ettirme" için olan ilke. İşletmecinin her gün dokunmadıkça çalışmayan bir araç eninde sonunda iptal edilir. Kurulunca bitmiş olmuyor. Ancak kullanılmaya devam ettiğinde bir iş oluyor. Kullanmaya devam eden dükkânların sayısını teker teker artırmak: bu kitabı yayımladıktan sonraki işim bu.

#### Kendi Dükkânınızda Başlamak İsterseniz

Bu kitabı okuyup kendi dükkânında denemek isteyenler için üç adım var.

1. https://bontallc.com/agenda?via=b2-tr-{{FMT}} adresini açın ve bir Google hesabıyla oturum açın (AgendaID oluşturulacak. Kart kaydı gerekmiyor)
2. Önce ücretsiz bir defter ekleyin. Işık Defteri'ni öneririm. Tabela bileşenini web sitenize yapıştırmanız yeter, 10 dakikada çalışır. Henüz açmadıysanız Kârlılık Defteri'ni deneyin
3. Size uygun görünüyorsa Mesai Defteri'ni üç ay ücretsiz deneyin. Süre dolmaya yaklaşırken bir bildirim gelir, bu yüzden öylece bıraksanız bile ücret alınmaz

Sorularınız varsa Destek Rehberi (AgendaQA) üzerinden sorun. Yapay zekâ kullanım sorularını anında cevaplıyor, özellik ve hata sorularını ben kendim okuyorum.

Bir restoranın satışları havaya ve mevsime bağlıdır. Koltuk sayısının da çalışma saatlerinin de sınırı var. Araç satışlarında ise koltuk sınırı yok. Bir dükkân işletirken kendi dükkânınızın sorunlarından doğan araçları dağıtmak ve bunun yavaş yavaş gelire dönüşmesi: bunun bağımsız bir dükkân için başka bir kazanç yolu olabileceğine inanıyorum.

#### Küçük Bir Şirket Kalarak Küresele Açılmak

Agenda serisi için baştan karar verdiğim bir şey daha var. Yalnızca Japonca kurmayacaktım.

Mesai Defteri, Kârlılık Defteri ve Destek Rehberi, hepsi 20 dilde kullanılabiliyor. Ekran metni ve sık sorulan sorular, hepsi. Tokyo'daki 19 koltuklu bir bar için kurulmuş bir araç İngilizcede, Korecede, Vietnamcada aynı şekilde çalışıyor.

İki nedeni var. Biri, restoranların sorunlarının ülke değişince değişmemesi. Çalışanların ne zaman gelip gittiğini kaydetmek istiyorsunuz. Açılıştan önce kârlılığınızı bilmek istiyorsunuz. Müşterilere kapanış saatinin uzatıldığını söylemek istiyorsunuz. Bunların hepsi dünyanın her yerindeki bağımsız dükkânların paylaştığı sorunlar. Diğeri, Japonya'daki bağımsız dükkânların sayısının düşmeye devam etmesi. Yalnızca Japonca pazara hizmet etseydim, araç satışlarının bir tavanı olurdu.

Geçmişte küçük bir şirketin yurtdışında ürün satması için yerel acentelere, çeviri firmalarına ve tüzel kişiliklere ihtiyaç vardı. Şimdi yapay zekâ çeviri ve düzeltme işinde yardım ediyor. Ortak ödeme sistemleri dünyanın her yerinde çalışıyor. Dağıtım için yalnızca bir sunucu yeterli; her ülkede stok ya da depo tutmaya gerek yok. Tek bir işletmecinin yaptığı bir araç, yapıldığı günün ertesi günü 20 dilde dünyanın raflarında olabilir. Geçmişte bunu yalnızca büyük şirketler yapabilirdi.

Baştan birden çok ülkeyle iş yapan çok küçük bir şirket: bu tür şirketlere bazen mikro çok uluslu şirketler (minik çok uluslu şirketler) deniyor. Bonta LLC, Higashi-Nakano'da bir dükkân ve bir işletmeciyle tam olarak bunu hedefliyor.

Elbette 20 dile çevirmek, yurtdışındaki işletmecilerin hemen kullanmaya başlayacağı anlamına gelmez. Çevirilerin bir kısmı doğal duyulmaları için anadili konuşanlarca incelenmeyi hâlâ bekliyor. Yine de dil bariyerini baştan kaldırarak, tıpkı dükkândaki oturma kapasitesinin sınırı gibi, araçların ulaşabileceği yerin tavanı da ortadan kalkıyor.

Bu temeli nasıl kurduğum, 4. bölümün hikâyesi.

【Şekil 3-5】Destek Rehberi'nde dil değiştirme. 20 dil listeleniyor *(Ekran Japonca.)*

## Bölüm 4: Teknoloji - Ürünleri Tek Başına, Sürekli Olarak Kurmak İçin Bir Sistem

Bu bölümün ana noktaları

- Yeni bir ürünü başlatma prosedürünü, bir yapay zekânın okuyup uygulayabileceği bir biçimde (bir "skill") belgeye dönüştürdüm. İnsanların yaptığı tek şey karar vermek ve yalnızca insanların yapabileceği işlemler
- Oturum açma, faturalama, tanıtım sayfaları ve diğer ürünlere rehberler gibi ortak parçalar bir kez kuruluyor ve tüm ürünlerde yeniden kullanılıyor. Bu temelin veri tabanı maliyeti ayda yaklaşık $35
- Sistem hâlâ büyütülüyor. Bir tasarımın art arda beş kez reddedilmesi gibi başarısızlıkları prosedür belgesine eklemeye devam ediyorum

(Bu, çok fazla teknik terim içeren bir bölüm. Teknolojiyle ilgilenmiyorsanız 5. bölüme geçebilirsiniz, hikâyeyi yine rahatça takip edebilirsiniz.)

### 4-1 ProductBootstrap: Başlatma Prosedürünün Kendisini Yapay Zekâya Devretmek

Bir ürün kurduğum her seferinde aynı hazırlığı ve aynı hataları tekrarlıyordum. Bir depo oluşturmak (programlar için bir ambar). Oturum açmayı bağlamak. Tasarım renklerine karar vermek. Test sistemini kurmak. Canlı ortamı hazırlamak. Önceki ürün için hepsini kesinlikle yapmıştım, ama ayrıntıları unutmuş ve aynı yerlerde tökezlemiştim.

Bu yüzden yeni bir ürünü başlatma prosedürünü bir belgeye dönüştürdüm. Kod yazan yapay zekânın (Claude Code) okuyup uygulayabileceği bir biçimine "skill" diyorum. Bu skill'in adı ProductBootstrap. "Bootstrap", bilgisayar dünyasında asgari bir mekanizmadan kendi kendine başlamak için yaygın bir terim ve ben onu ürün başlatmaya uyguladım.

Hiçbir şablon program tutmuyorum. En son tamamlanan ürünü kopyalayıp yeni ürüne ondan başlıyorum. Böylece en yeni dersler otomatik olarak bir sonraki ürüne aktarılıyor. Eski bir şablonu sürekli bakımda tutmaya da gerek yok.

#### Prosedürün Akışı

1. Gereksinim belgesini teslim edin. Gerekli alanlar (ürün adı, ne yaptığı, kimin kullandığı, fiyat, fiyatlandırma birimi, tanımlayıcı renk, ana tasarımın konumu vb.) boş bırakılırsa yapay zekâ başlamaz. Kural, süreç ortasında işletmeciye soru sormamasıdır. Her şey en başta yerinde değilse başlamıyor
2. Ürünün rengine karar verin. Agenda serisindeki her ürünün bir tanımlayıcı rengi var. Yapay zekâ mevcut ürünlerin renklerini ölçüyor, çakışmayan yaklaşık dört aday öneriyor ve işletmeci seçiyor
3. Tasarımı sabitleyin. Bir tasarım yapay zekâsına (Claude Design) ekranlar için öneriler oluşturtuyorum. Yapay zekâ kendi kontrolünü üç tura kadar çalıştırıyor ve işletmeciye yalnızca kontrolü geçen öneriler gösteriliyor
4. Uygulamayı sonuna kadar yapay zekâya bırakın. Yapay zekâ, belirlenen kabul koşullarını (tür denetimleri, stil denetimleri, tüm testlerin yeşil olması, her ekran kontrolünden geçmesi ve veri tabanı değişikliklerinin test ortamında temiz biçimde geçmesi) karşılayana kadar kendi başına kurar ve düzeltir
5. İşletmeci yalnızca canlıya geçerken onaylar. Test ortamına kadar her şey gözetimsiz ilerler ve işletmeci yalnızca canlıya geçiş işlemine karar verir

Uygulama aşamasını, işletmecinin onayını beklemek için yarı yolda durmayacak şekilde kurdum. İlk günlerde her aşamada onay isteyerek ilerliyordum, ama bu şekilde hiçbir şey ilerlemedi. Birden çok yapay zekâ çalışma penceresi olduğunda, her biri onay beklerken duruyor ve işletmecinin her pencereyi dolaşıp karar vermesi gerekiyor. Bu yüzden değiştirdim: önceden onaylanmış aralığı ve bir makinenin doğrulayabileceği kabul koşullarını önceden teslim ediyorum ve yalnızca başarısızlıkta duruyor.

Durma koşulları da belirlendi. Prosedür belgesi ile işletmecinin kararı çeliştiğinde. Yalnızca bir insanın yapabileceği bir işlem gerektiğinde. Aynı hata üzerinde art arda üç kez ilerleyemediğinde. Kimlik doğrulaması kesildiğinde, izinler yetersiz olduğunda ya da geri döndürülemez bir işlem gerektiğinde. Bunun dışında yapay zekâ kendi başına ilerliyor. İşin durumu küçük bir dosyaya kaydediliyor, bu yüzden yarı yolda çökse bile oradan devam edebiliyor.

#### İnsanlar Yalnızca İki Şey Yapar

Prosedür belgesine şunu yazdım: yapay zekâ her adımı uygular. İşletmeciden yalnızca şu iki şey istenebilir.

- Kararın kendisi. Onaylamak, son kararı vermek, iki seçenekten hangisinin alınacağına karar vermek
- Yalnızca bir insanın yapabileceği işlemler. Yalnızca harici bir hizmetin yönetim ekranından verilebilen anahtarlar, kimlik doğrulaması gerektiren başvurular, gerçek bir cihazda işlemler ve gözle kontrol

Yapay zekâ bunun dışında herhangi bir şeyi işletmeciye devrederse, bu prosedür belgesinin ihlalidir. Prosedür tablosuna her satır için bir "yürütücü" sütunu ekledim ve işletmeci girişi bir gerekçe belirtemeyen herhangi bir satır yapay zekâ tarafına geçiriliyor.

Bu kuralı koymamın bir nedeni vardı. Bir ürün için kalan işi ayırdığımda yapay zekâ "sunucu projesini oluştur," "oturum açma hedefini kaydet," "ortam değişkenlerini gir" ve "test ortamını kur" maddelerini hep işletmecinin görevleri olarak sıraladı. Her biri yapay zekânın kendisinin yapabileceği bir işlemdi. O zamanki dürüst tepkim "Bunu neden ben yapıyorum?" oldu. Yapay zekâya söylerseniz işleri kendisi yapar. Ama söylemezseniz bir insana devreder. Bu yüzden prosedür belgesine yazmam gerekti.

2. bölümde anlattığım rezervasyon sistemindeki her başarısızlığı bu prosedür belgesinin kontrol listesine koydum. Önce testleri koyun. Canlı veriyi geliştirme ortamında tutmayın. Önce test ortamını kurun. Böylece sonraki ürün aynı acıyı baştan yaşamıyor.

#### Hâlâ Büyüyor

Bu prosedür belgesi bitmiş bir ürün değil. Bir şey her başarısız olduğunda eklemeye devam ettiğim bir şey.

Örneğin bir zamanlar tasarım yapay zekâsına bir ürünün ekranını art arda beş kez yaptırdım ve beşi de reddedildi. Buna serinin tamamına ait tasarım kurallarını (DESIGN.md) verdiğim turlar da dâhil.

Başta yapay zekâ nedeni "renk düzeninin kendisi" diye teşhis etti. Ben bunu reddettim. Gerçek nedenler ikiydi. Biri, kurallarda tanımı olmayan renklerin keyfi biçimde kullanılmasıydı. Diğeri, farklı rolleri olan üç bölümün aynı arka plan rengiyle ve aynı kenar boşluklarıyla, aralarında bir sınır olmadan dikey olarak yığılmasıydı. Hiçbir kural ihlal edilmemişti, yine de roller görünümden kaybolmuştu.

Bu yüzden tasarım kurallarına maddeler ekledim. Farklı rolleri olan şeylere aynı görünümü vermeyin. Onları yalnızca renkle ayırmayın. En önemli şey bakışların ilk odaklandığı yerde olur. Yalnızca gerçekten eşit olan şeyler aynı ağırlıkta sıralanabilir. Sadece dikey olarak yığan bir yerleşim yapmayın.

Başarısızlıktan bir ders daha çıktı. Kaçınılacak "varsayılan görünümü" yalnızca bir yasaklar listesi olarak aktarırsanız, yapay zekâ listede olmayan başka bir varsayılana tamamen savruluyor. Kartları, gölgeleri ve yuvarlak köşeleri aynı anda yasakladığımda geri gelen şey yalnızca çizgilerden ve kenar boşluklarından oluşan gazete gibi bir ekrandı. O zamandan beri talimat belgelerini üç sütunlu yazdırıyorum: "kaçınılacak desen," "yasaklamak istediğim şey" ve "bunun yerine ne yapılacağı."

Tanımlayıcı renklere karar verme biçimimi de süreç içinde değiştirdim. Ürünler sekizi aştığı sıralarda, koyu renk bandı mevcut ürünlerce doldu ve dokuzuncu ve sonraki ürünler çizgiler ve düğmeler için mevcutlarla çakışmadan koyu bir renk edinemez oldu. Bu yüzden kuralı gözden geçirdim: bir ürünün tanımlayıcı rengi yalnızca açık yüzey renkleri için kullanılıyor ve çizgiler, ayraçlar, simgeler ve ana düğmelerin hepsi serinin ortak mürekkep renginde birleştiriliyor. Ürünler çoğalınca ancak netleşen bir kısıttı.

Bir şey her başarısız olduğunda prosedür belgesini düzeltiyorum. Sonraki ürün o kadar kolaylaşıyor. Prosedür belgesini büyütmenin, ürünleri tek başına kurmaya devam etmek için en iyi yatırım olduğuna inanıyorum.

【Şekil 4-2】Başlatma prosedürünün aşamaları ve onları kimin yürüttüğü (yapay zekâ ya da işletmeci) *(Ekran Japonca.)*

【Şekil 4-3】Agenda serisinin tanımlayıcı renkleri. Ürün başına bir renk, yalnızca yüzeylerde kullanılıyor *(Ekran Japonca.)*

### 4-2 AgendaHub: Ön Kapı

Ürünler çoğaldıkça aynı şeyleri tekrar tekrar kurar hâle geliyorsunuz. Oturum açma, faturalama, tanıtım sayfaları, diğer ürünlere rehberler. Bunu tek başına yürütmek için, ortak parçaları bir kez kurup tüm ürünlerde yeniden kullanmanız gerekiyor.

AgendaHub, bu ortak parçaların toplandığı yer. Ona "ön kapı" diyorum.

Öncelikle, tek bir adresten her ürüne yönlendiren giriş kanalı. bontallc.com tek alan adı altında her ürün için bir giriş sıralanıyor: /agendatimbro, /agendaoro, /agendaluce. Müşterilere ürünler tek bir sitenin içinde duruyormuş gibi görünüyor, ama aslında her birinin arkasında ayrı bir program çalışıyor.

Sonra, ürün tanıtım sayfalarının yerleştirildiği yer. Seri için bir tanıtım sayfası var ve onun içinde her ürün için bir bölüm var. Her bölüm ürün adını ve lakabını, fiyatı, "Şu olduğunda..." diye başlayan işletmecinin kendi sözcükleriyle ifade edilmiş bir sorunu, neler yapabildiğinin bir açıklamasını ve ayrıntı sayfasına bir bağlantıyı içeriyor. Yeni bir ürün çıkardığımda bu bölümü eklemek başlatma prosedürüne dâhil.

Ve tasarım kurallarının ve başlatma prosedürlerinin yuvası. Tanımlayıcı renklerin ana kopyası, ekran kuralları (DESIGN.md), 4-1'de anlattığım ProductBootstrap skill'i, ekranları kontrol eden skill ve veri tabanı değişikliklerini güvenle yapan skill. Seriye yayılan her kural için asıl içerik burada duruyor ve her ürün onu referansla okuyor.

【Şekil 4-1】Agenda serisinin yapısı. Ön kapıdan (AgendaHub) her deftere ve her defter tek bir hesaba (AgendaID) bağlanıyor *(Ekran Japonca.)*

### 4-3 AgendaID: Ortak Hesaplar ve Faturalama

AgendaID, serinin hesaplar ve faturalama için ortak sistemi.

Bir Google hesabıyla bir kez oturum açan işletmeci her ürünü kullanabilir. Her ürün için hesap oluşturmaya gerek yok. İleride dil ayarlarını da ürünler arasında taşımayı planlıyorum.

Faturalama da tek bir sistem. Her ürün için ödeme hizmetine (Stripe) bağlantı kurmak yerine AgendaID hepsini üstleniyor. Dört fiyatlandırma kategorisi var: ayda ¥300 (yaklaşık $2) tutarında hafif bir ürün, kullandıkça öde ürünü, ¥600 (yaklaşık $4) tutarında tek seferlik satın alma ürünü ve ücretsiz bir ürün. Ücretli ürünler kart kaydı olmadan üç aylık ücretsiz dönemle geliyor ve her dükkân ve ürün kombinasyonu için bir kez kullanılabiliyor. Tavsiye edene ve tavsiye edilene üçer ay ücretsiz dönem ekleyen bir mekanizma da var.

Ücretsiz dönem bitmeden yedi gün ve bir gün önce bildirim e-postaları geliyor. Bu e-postaları önce Mesai Defteri'nin içinde de kurdum, ama ürünler çoğaldıkça her ürüne aynı mekanizmayı vermenin israf olduğunu fark ettim ve AgendaID tarafında birleştirdim.

#### Ortak Kurallar Altında İptal ve Silme

Sade ama önemli bir kısım var: iptal ve veri silme.

Bir müşteri iptal ettiğinde hangi veriler ve ne zaman silinir? Her ürün için ayrı ayrı kurarsanız, bir yerde mutlaka bir şey atlanır. Üstelik Agenda serisi, müdavimleri yüz tanımayla tanıyan ürün gibi, özellikle hassas verileri işleyen ürünleri de içeriyor.

Bu yüzden silme ayrıntı düzeyini dört seviyeye böldüm ve bunu seri genelinde ortak bir kural yaptım. Bunlar bir ürünü iptal etmek, bir dükkânı silmek, bir hesaptan çekilmek (serinin tamamından ayrılmak) ve bireysel bir çalışanın silme talebi. Üst seviyeler alt seviyelere zincirleme yansıyor ve her ürün kendi veri silme prosedürünü ortak sisteme kaydediyor. Silme için bekleme süresi 30 gün ve bu sürede geri alınabiliyor.

Buna bir zaman ekseni eşlik ediyor. Örneğin devam kayıtlarının kanunen beş yıl saklanması zorunlu. Eski bir çalışan silme talep etse bile, saklama süresi içinde kayıt fiziksel olarak silinmek yerine adlar vb. anonimleştirilerek tutulmalıdır. "Sil" ile "tut" arasındaki çizgiye, kanunlar ışığında karar vermem gerekti.

#### Yapay Zekânın Üretimi Kirletmesini Önlemek İçin Bir Test Girişi

AgendaID'ye yapay zekâ için bir mekanizma daha ekledim: bir test oturum açma girişi.

Yapay zekânın her şeyin çalıştığını kontrol etmesi için oturum açıp ekranları kullanması gerekiyor. Ama oturum açma bir Google hesabıyla yapılıyor, bu yüzden yapay zekâ kendi başına oturum açamaz. İşletmecinin hesabını da yapay zekâya veremem. Yapay zekânın testlerinin canlı veriyi kirletme tehlikesi var.

Bu yüzden yalnızca test ortamında kullanılabilen yapay hesaplar (personalar) veren bir giriş kurdum. Canlıda çalışmıyor. Test ortamının veri tabanı canlıdan ayrı bir proje ve yalnızca yapay veri içeriyor. Yapay zekâ bu girişten oturum açıyor, ekranları kullanıyor ve her şeyin çalıştığını doğruluyor. Test hesapları her gün yeniden oluşturuluyor ve eskileri siliniyor.

Bununla yapay zekâ, canlıya dokunmadan, canlıyla aynı şekilde kurulmuş bir ortamda son kontrolü bile kendi başına yürütebiliyor.

### 4-4 Ortak Gezinti ve "Ön Kapı" Sözcüğünün Başarısızlığı

Kullanıcıların herhangi bir üründen diğerlerine ulaşabilmesi için her ürüne ortak bir gezinti menüsü verdim. Mesai Defteri kullanan bir bar işletmecisinin Destek Rehberi'nde soru sormasını ya da diğer defterlere göz atmasını sağlayan yol bu.

Bu ortak gezintinin ardında küçük bir başarısızlık hikâyesi var.

İlk sürümde "Ön kapıya dön" yazan bir bağlantı koymuştum. Bunun nedeni, dahili olarak AgendaHub'a "ön kapı" demem. Ama gerçek bir cihazda kontrol ettiğimde bir şey yanlıştı. "Ön kapıya dön" ve "Agenda serisine göz at" olmak üzere iki bağlantı aynı yere gidiyordu. Üstüne, destek bağlantısı gündelik iş menüsünün üzerinde duruyordu, bu yüzden önem sırası tersti. Ve her şeyden önce "ön kapı" sözcükleri, ürünü ilk kez kullanan bir işletmeci için hiçbir anlam taşımıyor. Yapanın kendi dahili diliydi.

Bu yüzden ilkeleri yeniden belirledim. Öğeleri kullanıcının amacına yakınlıklarına göre sıralayın: gündelik iş en üstte, dışarı götüren bağlantılar en altta. Yeni kullanıcı kazanmayı amaçlayan bir bağlantı bile işin üstüne asla çıkmaz. Sınır tek bir cümleyle açıklanabilmeli. İfadeyi dahili dilde değil, kullanıcının dilinde yazın. Aynı yere giden birden fazla bağlantı asla koymayın. "Ön kapıya dön"ü çöpe attım ve her şeyi "Diğer Agenda defterlerine göz atın" tek bağlantısında birleştirdim.

2. bölümde arayüzün dilini öğrenmeyi anlatmıştım. O, işletmecinin yapay zekâyla konuşurken kullanacağı dildi. Bu ise tersi: yapanın kullanıcıyla konuşmak için kullandığı dil. İkisinde de mesele, sözcüklerinizi konuştuğunuz kişiye uydurmaktı.

【Şekil 4-4】Düzeltmeden sonraki ortak gezinti. İş en üstte, dışarı götüren bağlantılar en altta *(Ekran Japonca.)*

### 4-5 Temelin Maliyeti Ayda $35

Bu bölümde anlatılan temelin tamamının veri tabanı maliyeti ayda yaklaşık $35. Canlı projeyi içeren ücretli plan $25, test ortamı projesi ise $10.

Bu da baştan bu tutar değildi. Bir ara ayda $45 ödüyordum. Bir yüz tanıma ürünü için geliştirme veri tabanı, kullanmıyor olmama rağmen hâlâ faturalanıyordu. Onu ücretsiz katmana taşıyıp durdurdum, kullanmadığım bir projeyi daha sildim ve şimdiki tutara böyle indi.

Yapay zekânın maliyetini de gözetiyorum. Program yazan yapay zekânın işi, token miktarı üzerinden (yapay zekânın okuduğu ve yazdığı metin birimi) faturalanıyor. Maliyetin yoğunlaşmasını, çalışma penceresinin koordinatör rolüne bağlı kalmasını sağlayıp uygulamanın kendisini ayrı bir maliyet payı olan farklı bir yapay zekâya bırakarak önlüyorum. Sohbet penceresindeki üretken model için de fiyata bakıyor, gerekli ve yeterli olanı seçiyorum. Daha üst seviye bir model ayda yalnızca $1 daha pahalı olsa bile "yeterli mi?" diye sorarak seçiyorum.

Küçük kurarsanız, küçük satışlar bile sizi ayakta tutabilir. 3. bölümdeki para kazanma hikâyesi, bu temelin maliyetinin küçüklüğüyle destekleniyor.

### 4-6 Koordine Eden Yapay Zekâ ve Karar Veren Kişi

Son olarak çalışma günümün biçimini anlatayım.

Aynı anda birkaç yapay zekâ çalışma penceresini açık tutuyorum. Rezervasyon sistemi için bir pencere, her ürün için bir pencere ve onlara talimat gönderip sonuçları toplayan bir koordinatör penceresi var. Koordinatör penceresine AgendaRegia (koordine eden defter) adını verdim.

Karar veren, yani "hangi yöne gidileceğine" karar verenler, ben ve sohbet tarafındaki yapay zekâ. Sohbet tarafındaki yapay zekâ gereksinimlerdeki boşlukları ve çelişkileri önceden buluyor, her birine varsayılan bir karar ekliyor ve hepsini birden öneriyor. Ben okuyup karar veriyorum. Kararlaştırılanlar, Goal adlı bir talimat kâğıdında toplanıyor ve çalışma penceresine yapıştırılıyor. Önceden onayları ve bir makinenin doğrulayabileceği geçme koşullarını içeriyor. Çalışma penceresi onu okuyor ve yalnızca bir şey başarısız olduğunda durarak sonuna kadar götürüyor.

Talimat kâğıdına işin ne zaman biteceğine dair bir tahmin de ekletiyorum. Bu işi barın açılış saatlerinin arasına sığdırıyorum, bu yüzden bir şeyin ne kadar süreceğini bilmezsem günümü planlayamam.

İşletmecinin rolü okumak değil, karar vermek. 1.775 sohbet kaydının hepsini okumama gerek yok. Barın olgularıyla ilgili soruları cevaplıyorum. Yalnızca barın politikasının belirleyebileceği şeylere karar veriyorum. Bir şey yayına girdikten sonra, bir şey ters geliyor mu diye kendim beş altı kez deneyip kontrol ediyorum. Hepsi bu.

Bu biçime varmadan önce çok kez işi yeniden yaptım. Yapay zekâ kendi başına özellikler ekledi ve ekranlar kararsız hâle geldi. İş tek bir talimattan sınırsız büyüdü. Her aşamada onay beklemek hiçbir şeyin ilerlememesi demekti. Her seferinde bir kural ekledim ve şimdiki biçime böyle ulaştı. Bu da hâlâ büyüyor.

#### Bu Bölümden Çıkarılacak Dersler

- Tekrarlanan işler için prosedürün kendisini bir belgeye dönüştürüp yapay zekâya verin. Prosedür belgesini her başarısızlıkta düzeltirseniz bir sonraki sefer kolaylaşır
- Ortak parçaları (oturum açma, faturalama, gezinti) yalnızca bir kez kurun ve tüm ürünlerde yeniden kullanın. Temel küçükse, küçük satışlar bile sizi ayakta tutabilir
- İnsanlar yalnızca karar verir ve yalnızca insanların yapabileceği işlemleri yapar. Yapay zekâ size bunun dışında bir şey devrederse, kılavuza ekleyin

Bu bölümün devamı (kuracağım sonraki defterler ve kılavuza eklediğim dersler) note ve X'te. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Bölüm 5: Küçük Bir Barın Geleceği

### 5-1 Zatta Gohan'dan Tamuro'ya

Yeme içme işine 39 yaşındayken girdim.

Buna vesile olan, Zatta adlı bir mahalle barıydı. Ayda bir, bazen iki haftada bir orada yemek servis etmeme izin verdiler. Uzun süre kendi kendime yemek yapmayı öğrenmiştim, ama artık insanların yemeğimi yediği ve mutlu olduğu bir yerim vardı. İlk deneyimim buydu.

2014'te Arai-Yakushi'de Zatta Gohan adlı bir restoran açtım. Set yemek sunan küçük bir mekândı. Yedi yıl işlettim.

Ancak Arai-Yakushi'de müşteri sayısının bir sınıra dayandığını hissettim. Sonra Higashi-Nakano'da bir mekân buldum. İstasyonun doğu çıkışından yürümek bir dakikadan az sürüyor. Yağmurlu bir günde bile pek ıslanmadan ulaşabilirsiniz.

Kasım 2018'de orada Tamuro'yu açtım. "Tamuro", insanların bir araya geldiği yer demek. tezgâhta 11 tabure ve tatamide 8 oturma yeri, toplam 19 koltuğu var. Üç yıl boyunca Arai-Yakushi ve Higashi-Nakano olmak üzere iki yeri paralel işlettim. COVID döneminde ikisini birden sürdürmek zorlaştı, bu yüzden Arai-Yakushi dükkânını kapattım ve yalnızca Tamuro kaldı.

#### Küratör Bar

Tamuro kendine bir "küratör bar" diyor.

Küratörlük, seçici bir göze sahip olmak demek. Bir aşçıdan önce, bir küratör olmak istiyorum. Yemekler, içkiler, barın havası: hepsini seçici bir gözle seçerek yapıyorum. Tamuro bu.

Hem yurtdışında hem Japonya'da sık sık yemek için seyahat ediyorum. Vietnam, Kamboçya, İtalya, Şanghay, Pekin, Meksika. Yemek için gezip dolaşmak bir zevk ve aynı zamanda Tamuro'da neyin sunulacağını bulmanın bir yolu. Pahalı malzemeleri elimin altındaki malzemelerle yeniden yaratıyorum. Örneğin yumurta sarısını kurutup rendelerseniz bottarga'ya yakın bir tat elde edersiniz. Bu tür ikamenin (yerelleştirmenin) benim rolüm olduğunu düşünüyorum.

COVID döneminde yeniden yemek yapmayı öğrendim. Toplam sekiz derslik bir Fransız mutfağı kursuna katıldım ve bir Japon mutfağı kursuna da devam ettim. Umami'yi nasıl ele alacağımı ve ısıyla nasıl pişireceğimi öğrendim. Orada öğrendiklerim, bugünkü yemeklerimin temeli.

Tamuro'nun menüsü dört meze ve bir ana yemekten oluşuyor. Yalnız yaşayan müşterilerin bol sebze alabilmesi için ona bir malzeme çeşitliliği veriyorum. Pişirme yöntemleri (kızartma, sirkeli, haşlama, ızgara) ve tatlar (tatlı, acı, ekşi) çakışmayacak şekilde bir araya getiriyorum. En çok sevilen yemek, domuz bifteği tonteki. Bol sarımsaklı, Kyushu soya sosuyla yapılmış hafif tatlı bir sosu var.

#### İnsanların Bir Araya Geldiği Bir Yer

Tamuro'nun müşterilerinin yaklaşık yarısı yalnız geliyor. Ağırlıklı olarak 30'lu ila 50'li yaşlarda ve çoğu Higashi-Nakano'dan komşular, ama Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo ve Eifukucho çevresinden de geliyorlar. 

Barın ayırt edici özelliği, müşterilerin birbirleriyle ne kadar çok konuştuğu. Tezgâhı yandaki kişiyle konuşmak kolay olacak şekilde kurdum ve oturma düzenini kimin anlaşacağına bakarak ben ya da çalışanlar belirliyoruz. Yalnız gelen müşteriler bazen sonradan birlikte geri geliyor. Adının da dediği gibi, insanların bir araya geldiği bir yer oldu. Barın günlerinin nasıl geçtiğini [Instagram](https://www.instagram.com/tamuro.higashinakano/) hesabında paylaşıyorum.

Ayda bir kadar yapılan çok servisli akşam yemeğinde, iki üç saat boyunca şarap eşleşmeleriyle birlikte yedi sekiz yemek sunuyorum. Her ay tema değişiyor: İtalyan, Fransız, Japon. Yemek atölyeleri üç saatlik uygulamalı atölyeler ve pişirdikten sonra herkes kadeh kaldırıyor, yiyor ve evine gidiyor. Açılıştan önce erken akşamda şarap ve küçük tabaklar sunulan aperitivo var. Yılda iki kez kadar bir barbekü var. Yılda bir kez bir yıl sonu partisi var. Ve 1. bölümde yazdığım yukata festivali var.

1. bölümde yazdığım rezervasyon sistemi, sohbet penceresi ve MCP, hepsi insanları bu bara getirmek için araçlar. Yapay zekâ bir hedef değil, insanları bir araya getirme aracı.

### 5-2 Quatre Épices'in Hamburger Köri'si

Tamuro, gece açık bir bar. Gündüzleri mekân boş.

O zamanı kullanarak Ocak 2024'te Quatre Épices'i başlattım. Aynı yerde yalnızca öğle yemeğinde hizmet veren, çalışanların işlettiği bir hamburger köri dükkânı.

Quatre Épices, Fransızcada "dört baharat" demek. Adına sadık kalarak, çok sayıda baharat üst üste koymak yerine, tadın hatlarını netleştirmek için seçip daraltıyoruz. Köride un kullanılmıyor; sebzelerin ve etin kendi doğal kıvamıyla tamamlanıyor. Yemeği bitirdiğinizde doyum ve midede ağırlık olmaması. Ve hamburgerle uyum. Bu üç öncül üzerine tasarladım.

Hamburgerin pişirilme biçiminde titiziz. Karışımı dışı çıtır, içi yumuşacık çıkacak şekilde ayarlıyoruz ve o karışıma uygun pişiriyoruz. Geceleri Tamuro'da öğrendiğim ısıyla pişirme yöntemi gündüz tabağına da yansıyor.

Fiyatlar, iş günleri ve saatler değişebilir, bu yüzden en güncel bilgi için lütfen Tamuro'nun Instagram'ına (https://www.instagram.com/tamuro.higashinakano/) bakın.

Quatre Épices aynı yerde çocuklar için bir dayanışma sofrası da işletiyor. Mevcut barın olanaklarını ve satın almasını kullanarak mahalledeki çocuklara yemek sunan bir faaliyet. Bu bağlantı sayesinde yerel toplum merkeziyle bir ilişki de kurduk. Bazen yerel spor etkinliklerinde, toplum merkezi etkinliklerinde ve Bon dansı festivallerinde köri ve sandviç sunuyoruz.

Dürüst olmak gerekirse, gündüz saatlerini kullanmak her yönüyle iyi gitmedi. Gündüz içkisi günleri düzenledim ve mekânı başkalarına kiraladım, ama müşteriler umduğum gibi gelmedi. Barın cazibesi, gece işletmeci oradayken ve yalnızca gündüz çalışanları oradayken farklı hissediliyor. Gündüz dükkânını gece dükkânından farklı bir cazibeyle büyütmek hâlâ tamamlanmamış bir görev.

### 5-3 Bonta LLC: İki Ayak

Tamuro'yu ve Quatre Épices'i işleten küçük şirket Bonta LLC. Ben onun yönetici ortağıyım.

Şirketin iki ayağı var. Biri yeme içme: Tamuro ve Quatre Épices. Diğeri BT: Agenda serisinin geliştirilmesi ve danışmanlık.

Yeme içme ile araçlar farklı biçimlerde para kazandırır. Şirketi farklı nitelikte iki ayakla desteklemek, aklımdaki biçim.

Ve iki ayak birbirine malzeme sağlıyor. Bardaki sorun bir aracın tohumu oluyor. Araç kurmaktan öğrendiklerim barı işletmeye geri dönüyor. Işık Defteri kapanış saatlerinin uzamasından doğdu ve Işık Defteri'ndeki kapanış uzatma kayıtları kâr tahminlerinin ve vardiyaların temeli oluyor. Sohbet penceresinde biriken "cevaplayamadığımız sorular" barın rehberliğini iyileştiriyor. Bu döngü, hem barı hem geliştirmeyi tek başıma yönetebilmemin nedeni.

Şirketi büyütmeyi düşünmüyorum. Küçük, çok ve ucuz. Bu şirketin biçimi bu.

### 5-4 Raku Bonta Olarak Yazmak

Yazıp yayımladığımda "Raku Bonta" takma adını kullanıyorum. Bu kitabı da bu adla yazdım.

Önceki kitabım *Yapay Zekâ Müdür Yardımcısı*, üretken yapay zekâ hakkında bir kitaptı. Amazon'un zaman yönetimi kategorisinde bir numaraya çıktı ve pek çok kişi tarafından okundu. Bu kitap onun devamı.

Kitapların yanı sıra note'ta (Japonya'nın blog platformu) da yazıyorum. Barın yapay zekâyla çabalarını, bir eğitim gezisinde bulduklarımı, kitaplarımı yayımlama ilerlemesini ve Agenda serisini yazıyorum. Bu kitaba sığdıramadığım devamını note'ta (https://note.com/bontallc) takip edebilirsiniz.

Benim için yazmak, hem barı hem geliştirmeyi sözcüklere dökmenin ve kontrol etmenin de bir yolu. 1. bölümde yazdığım gibi, "T-AI-MURO" sohbet penceresinin ilk bilgisi X'te bıraktığım sözcüklerden kuruldu. Yazıya döktüklerim yapay zekâ için malzeme oldu. Bundan sonra da yazdıklarım hem bara hem yapay zekâya geri dönecek.

Yazmakla ilgili karar verdiğim bir şey daha var. Bitmemiş şeyleri "yakında" diye duyurmuyorum. Bitiriyorum, bir tanıtım sayfası yapıyorum ve ancak ondan sonra çıkarıyorum. Bu sıraya bağlı kalmanın küçük bir şirkete güven kazandırdığına inanıyorum.

### 5-5 Bağımsız Dükkânın Geleceği

Son olarak, bu kitapta yazdıklarımı tek bir resimde toplayacağım.

【Şekil 5-1】Bu kitabın anlattıklarının büyük resmi. Küçük bir bar kendi penceresini açıyor (birinci hikâye) ve sorunlarını başka barlara verilecek araçlara dönüştürüyor (ikinci hikâye) *(Ekran Japonca.)*

Müşteriler bir barı bulmayı ve rezervasyonu kendi yapay zekâlarına yaptırmaya başlayacak. Ağustos 2026'da büyük bir rezervasyon hizmeti aracılığıyla ChatGPT'den restoran rezervasyonu yapmak mümkün oldu. Giriş kanalı arama ve yemek inceleme sitelerinden her bireyin kendi yapay zekâsına kayıyor.

O noktada büyük rezervasyon hizmetinde listelenmeyen bir bar yapay zekâya görünmez. Ama büyük hizmette olmasanız bile, bir barın doğrudan yapay zekâya bağlanması için bir yol var. Tamuro, MCP adlı bir pencere açarak bu yolu seçti. Küçük bir barın kendi başına kendi penceresini açması. Bu kitabın birinci hikâyesi bu.

Bar sahipleri kendi sorunlarını araçlara dönüştürüp başka barlara dağıtabilecek. Işık Defteri, Tamuro'nun kapanış saatinin uzayacağını söyleme isteğinden doğdu ve herhangi bir barda kullanılabilir. Kurma gücü artık yalnızca belirli insanların ya da şirketlerin olmaktan çıkıyor. Küçük bir bar sahibi, araç kullanan taraftan araç kurup dağıtan tarafa geçiyor. Bu kitabın ikinci hikâyesi bu.

Bu ikisinin ortak yanı, bar ne kadar küçükse o kadar keskin olabilmesi.

Büyük zincirler, her şube aynı kaliteyi sunsun diye sistemlerini genelleştirir. Tamuro bunun tersi. Yalnız müşteriler yarısını oluşturuyor, rezervasyonların neredeyse %90'ı aynı gün yapılıyor ve müşteriler birbirleriyle konuşuyor. Tamuro'nun bu karakterine uysun diye rezervasyon sistemini, indirimleri ve sohbet penceresini ayrıntılı kurdum. Genelleştirmediği için keskin. Keskin olduğu için müşterilerin onu seçmesinin bir nedeni oluyor.

Ve bar ne kadar keskinse, o kadar çok araç tohumu buluyor. Barın karakterine ne kadar çok yüzünüzü dönerseniz, sorunlarınız o kadar belirginleşir. Belirgin sorunlar belirgin araçlara dönüşür. Belirgin araçlar aynı soruna sahip başka barlara yardımcı olur.

Yapay zekâ, tek bir işletmecinin ikisini birden yapabilmesini mümkün kıldı. Barı keskinleştirmek ve araç dağıtmak. Eskiden birini seçmeniz gerekirdi. Şimdi ikisini de yapabilirsiniz.

Elbette hâlâ süren bir iş. Sohbet penceresinin geçme oranı hâlâ yükseltiliyor. Kılavuz her başarısızlıkla eklenerek büyüyor. Gündüz dükkânının nasıl büyütüleceği bir zorluk olarak duruyor. Yapay zekâ aracılığıyla rezervasyon yapan insanlar hâlâ çok değil.

Yine de küçük barın geleceğinin parlak olduğuna inanıyorum. Küçük olmak bir zayıflık değil. Küçük olduğumuz için hızlı deneyebilir, hızlı bırakabilir ve hızlı düzeltebiliriz. Küçük olduğumuz için keskin olabiliriz. Ve keskin bir barın sorunları araçlara dönüşüp başka küçük barlara geçiyor.

Bu kitabı Higashi-Nakano'daki 19 koltuklu bir bardan yazdım.

## Son Söz

Buraya kadar okuduğunuz için teşekkür ederim.

Bu kitapta yazdıklarım, Ekim 2026 itibarıyla bir kayıt. Yapay zekâ araçları aylar içinde şekil değiştiriyor. Anlattığım mekanizmaların bir kısmı kitap yayımlandığında zaten farklı bir biçim almış olabilir. Yine de küçük bir barın yapay zekâyla ne kurduğunun ve nasıl kurduğunun, nerede başarısız olduğunun ve ne öğrendiğinin bir kaydının bir süre yararlı kalacağına inanarak yazdım.

Agenda serisi: https://bontallc.com/agenda?via=b2-tr-{{FMT}}

Faaliyetlerimi takip edin: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Higashi-Nakano'ya yolunuz düşerse Tamuro'ya uğrayın. Rezervasyonu rezervasyon sitesinden, sitedeki "T-AI-MURO" sohbet penceresinden ve elbette kendi yapay zekânızdan yapabilirsiniz.

Tamuro'nun rezervasyon sitesi: https://tamuroreservation.vercel.app/?src=b2-tr-{{FMT}}

Tamuro'nun Instagram'ı: https://www.instagram.com/tamuro.higashinakano/

Yapay zekâdan rezervasyon yapmayı denemek isteyenler için. Tamuro'nun MCP sunucusunun bağlantı adresi aşağıdaki URL'dir:

https://tamuroreservation.vercel.app/api/mcp

Yapay zekânızın (Claude ya da ChatGPT gibi) ayarlarında harici araç ekleme ekranını (bağlayıcılar, MCP sunucuları) açın ve bu URL'yi kaydedin. Kaydetme biçimi yapay zekâya göre ve zamanla değişiyor, bu yüzden en güvenli yol her yapay zekânın yardım sayfasında "MCP" ya da "bağlayıcı"yı aramak. Sahip olduğunuz plana bağlı olarak, kendi seçtiğiniz bir MCP sunucusunu bağlayamayabilirsiniz. Kaydedildikten sonra yapay zekânıza "Tamuro'da bu akşam yer var mı?" diye sorun. Boş saatleri ve fiyatları kontrol edecek ve sizi rezervasyon sayfasına yönlendirecek. Onay düğmesine siz basıyorsunuz.

Kitabı okuduktan sonra gelenler için. Rezervasyon yaparken lütfen "BOOK" kupon kodunu girin. İlk içkiniz bizden. Rezervasyonsuz geldiyseniz, ilk siparişinizi verirken "Kitaptan geldim" demeniz yeter. Aynı ikramı yapacağız. Kitaptan kaç kişinin geldiğini sayabilmem için kurduğum küçük bir yöntem.

Rezervasyonsuz girebilirsiniz. Tek başınıza olsanız bile yabancılık çekmezsiniz. Hatta yandaki kişiyle keyifle sohbet ederken bile bulabilirsiniz kendinizi.

İnsanların bir araya geldiği bir yerde sizi bekliyorum.

Raku Bonta

### Kaynaklar

- OpenAI Help Center, "ChatGPT — Release Notes," 10 Ağustos 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (ABD'de yapay zekânın hisse senedi gibi menkul kıymetler için emir vermesini sağlayan bir MCP sunucusu örneği) https://docs.alpaca.markets/docs/alpaca-mcp-server
- "SaaS'ın ölümü" tartışması: Satya Nadella'nın BG2 podcast'indeki sözleri (Aralık 2024), Şubat 2026'da yazılım hisselerindeki keskin düşüş ve ona verilen ad ve Jensen Huang'ın cevabı aşağıdaki haberlerden ve yorumlardan alındı. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
