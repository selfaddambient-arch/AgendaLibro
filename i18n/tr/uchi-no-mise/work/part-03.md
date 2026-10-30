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
