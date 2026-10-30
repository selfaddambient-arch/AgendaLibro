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
