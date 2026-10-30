## Bölüm 6: Zorluklar - Yalnızca Kendi Dükkânım İçin Bir Sistem Geliştirmek

~ "Yoksa kendin yap." Uzmansız bir sistem geliştirme projesi ~

※Bilginiz olsun, bu kitaptaki her şeyi yapmanıza gerek yok.

・Bir görsel gönderin ve yapay zekâya metin yazdırın\
・Uzun bir LINE mesajını şemaya çevirin

Başlamak için bu ikisi yeter. Bu bile işlerinizi kesinlikle kolaylaştırır.\
Bunu bir hikâye olarak okuyup "Yapay zekâyla demek bu kadarı bile yapılabiliyormuş" diye düşünmeniz de yeterli.

### 6-1. Hazır Uygulamalar Tam İhtiyacım Olan Yere Ulaşamıyor

Şimdiye kadar görsel üretimi ve menü analizi gibi mevcut platformların üzerinde yapay zekâ kullanmaktan söz ettim.

Ama bir işi sürdürdükçe, "hazır uygulamaların" çözemediği kaygılar ortaya çıkıyor.

Özellikle bizimki gibi "gündüz köri, gece bar" şeklinde düzensiz bir iş modelinde para giriş çıkışı da karmaşık.

"PayPay Bank bakiyemi yaklaşan ödemelerle eşleştirip ay sonunda ulaşacağım tutarı bilmek istiyorum."

"Ödeme tarihleri 10'u ve 25'i arasında bölünmüş durumda. Bunu simüle etmek istiyorum."

Piyasadaki muhasebe yazılımları son derece yetenekli, ama hiçbiri "şu anda aklımdaki kaygıyı" tam olarak hedef almıyordu.

Bu yüzden karar verdim.

"Yoksa kendim yaparım. Yanımda en güçlü mühendis Gemini var."

### 6-2. 1-3. Aşamalar: Karalanmış Notlardan "Bulut"a

Geliştirme, notlarımı Google Keep'te Gemini'ye göstermemle başladı.

![Geliştirmenin başlangıç noktası olan Keep notu](images/fig-25.png)

#### 1. Aşama: Mantığı Kurmak

"Bu nottaki hesaplamaları otomatikleştirmek istiyorum."

İsteğime karşılık Gemini hesaplama mantığını çabucak bir araya getirdi.

- Bir kalemin tutarını değiştirdiğimde son bakiyeyi anında hesaplıyor.

- Para yetmemek üzereyse kırmızıyla bir "uyarı" gösteriyor.

- Ödeme zamanlamasını "10'u" ve "25'i / ay sonu" olarak bölerek simüle ediyor.

- Veriler tarayıcıda (önbellekte) saklanıyor.

Bu bile yeterince kullanışlıydı ama iştahım kabardı. "Tarayıcıyı kapatsam bile verilerin kalmasını istiyorum. Telefonumdan da kontrol etmek istiyorum."

#### 2. Aşama: Tanımadığım Bir Araç Olan "Firebase"i Benimsemek

Bir elektronik tabloya bağlamayı düşünüyordum ama Gemini'nin önerisi beklenmedikti.

"Gerçek zamanlılığı ve verimliliği düşünürseniz Google'ın 'Firebase'ini kullanalım. Ücretsiz katman çalıştırmaya yeter."

"Firebase...?" Kelimeyi hiç duymamıştım. Ama sistem koordinatörlüğü günlerimden kalma içgüdümle "Yapay zekâ bu kadar kuvvetle öneriyorsa onunla gidelim" diye karar verdim.

Sonuç olarak Firestore adlı bir veri tabanı kullanılarak veriler bulutta güvenle saklanır hâle geldi.

#### 3. Aşama: Google Girişi ve Bir Onay Sistemi

Konu para, herkesin görmesi kötü olur.

Başta "parola cümlesi" gibi bir şey düşündüm ama Gemini "Daha güçlü güvenlik istiyorsanız Google girişini kullanalım" önerisinde bulundu.

Sonra "Yalnızca onayladığım çalışanların görebilmesini istiyorum" dediğimde, hatta "bir yöneticinin ekranda üyeleri onaylayıp çıkarabildiği bir sistem" bile kurdu.

### 6-3. 4-5. Aşamalar: Siyah Ekranla (Terminal) Yüzleşmek

Buradan sonrası vibe coding'in en büyük sınavıydı: uygulamayı internette yayımlamak (dağıtmak).

#### Uyarı: Buradan Sonrası "Siyah Kuşak" Kursu

Sonraki birkaç sayfa, bu kitabın en zor "uygulamalı" kısmı. Filmlerdeki hackerların kullandığı gibi bir "siyah ekranı (terminali)" kullanacaksınız.

Dürüst olacağım. Burada kesinlikle hata alacaksınız. Ben de aldım. Büyü gibi okunan "PowerShell izin hatası" gibi duvarlarla karşılaşacaksınız. Ama korkmayın. Burada yaptığınız şey yine aynı: sadece "hata ekranının görüntüsünü alıp yapay zekâya fırlatmak."

Sistem sektöründeki günlerimde öğrendiğim gerçek şu: "Profesyoneller bile hata alır. Tek fark, hata belirdiğinde pes mi ettiğiniz, yoksa yardım mı aradığınız (sorduğunuz)." Çok zor görünüyorsa bu bölümü atlayın ve yalnızca şu olasılığı aklınızda tutun: "Yapay zekâyla bu kadarı bile yapılabiliyor."

Gemini şöyle dedi:

"Windows bilgisayarınıza geliştirme ortamını kuracağız. 'Node.js'i kurun ve 'VS Code'da aşağıdaki komutları yazın."

Söylenildiği gibi siyah ekranı (terminali) açtım ve hemen bir hata aldım.

"PowerShell güvenlik kısıtlamaları nedeniyle çalıştırılamıyor."

Sıradan bir işletmeci burada cesaretini yitirirdi.

Ama ben hata ekranını kopyalayıp yapıştırdım ve yapay zekâya fırlattım.

Yapay zekâ anında cevap verdi: "Kısıtlamayı 'Set-ExecutionPolicy' adlı bir komutla kaldırın."

Ne anlama geldiğini anlamadan komutu yazdım, sonra npm run build, firebase deploy...

O büyü gibi karakterleri her yazışımda ekranda yazılar akıyor ve işlem ilerliyordu.

Ve sonunda uygulamam internette belirdi.

#### 5. Aşama: Akıllı Telefon Uygulamasına Dönüştürmek (PWA)

Yayımlanan uygulama başta tasarımı bozuk, "çıplak" bir durumdaydı ama bu da "Tailwind CSS" adlı bir ayar eklenerek çözüldü.

Sonra "Telefonumun ana ekranına bir simge koyup uygulama gibi kullanmak istiyorum" dediğimde, bana onu bir "PWA'ya (Progresif Web Uygulaması)" dönüştürecek ayarları öğretti.

Böylece yaptığım (tek satır kod yazmadan) özel bir uygulama telefonumun içinde doğdu.

![Tamamlanan nakit akışı yönetim uygulamasının ekranı](images/fig-26.png)

### 6-4. 6. Aşama: 30 Gün Sonraki Sorun ve Çözümü

Kullanmaya başlamamdan yaklaşık bir ay sonra bir sorun çıktı.

"Düne kadar sorunsuz çalışıyordu, birden erişemez oldum!"

Telaşlandım ve Gemini'ye danıştım; neden beklenmedik bir yerdeydi.

"Veri tabanı (Firestore) ayarları hâlâ 'test modundaydı (30 günle sınırlı)'. Süresi doldu."

Yapay zekâ, geliştirmenin başında yapılandırma zahmetinden kurtarmak için bilerek son kullanma tarihli bir kural koymuştu.

"Güvenlik kurallarını 'oturum açmış herhangi bir kullanıcı kullanmaya devam edebilsin' şeklinde yeniden yazalım."

Yapay zekânın talimatıyla ayar dosyasının birkaç satırını yeniden yazdığımda uygulama sorunsuzca geri geldi.

Bu sorun da benim için iyi bir deneyim oldu.

"Bir sistemin canlı bir şey olduğunu ve bakım gerektirdiğini" öğrendim.

Ve "bir sorun çıksa bile yapay zekâya sorarsam her zaman bir cevap vardır" güvencesini edindim.

### 6-5. Örnek 2: X'te (Eski Adıyla Twitter) Bir Demo Videosuyla Başlayan "Yüz Tanıma Projesi"

İşte üstlendiğim bir sistem geliştirme daha, ve en büyüğü.

Bu, "kameradan içeri giren müşterileri tanıyan ve bana sessizce adlarını, verilerini ve tercihlerini söyleyen bir sistem."

Öylesine gezindiğim sosyal medya sitesi X'te başladı.

Akışıma bir mühendisin paylaştığı bir demo videosu düştü: Google Chrome'a yerleşik yapay zekâyı (Built-in AI) kullanarak bir web kameranın gördüklerini gerçek zamanlı olarak açıklıyordu.

Eski bir sistemci olarak içgüdülerim devreye girdi.

"Bu 'çok kipli'. Ve tarayıcıya yerleşikse, buluta para ödemeden tamamen kendi bilgisayarımda çalışamaz mı?"

Bu işe yararsa, pahalı bir sistem kurmadan yalnızca dükkânıma özel bir ağırlama sistemi kurabilirdim.

URL'yi kopyalayıp Gemini'ye fırlattım.

"Bununla aynı şeyi yapmak istiyorum. Nasıl uygulanacağını söyle."

#### 1. Aşama: Çalıştı Ama "Kim" Olduğunu Söyleyemiyordu

Gemini'nin talimatıyla Chrome ayarlarını (bayrakları) değiştirdim ve kodu yapıştırdım; demodakiyle aynı sistem sorunsuz çalıştı.

Kamerada göründüğümde ekranda şu belirdi:

"Gözlüklü bir adam bir bilgisayarın karşısında oturuyor."

Tarayıcıya yerleşik GeminiNano adlı bir yapay zekâ kullanıyor. Avantajı buluta bağlanmadan tamamen tarayıcının içinde çalışması, ama yalnızca "gözlük" ve "adam" gibi genel şeyleri tanıyabiliyor. Kişinin kim olduğunu belirlemeye kadar gidemiyor.

Müthiş bir teknoloji. Ama bir restoran sahibi olarak hemen hayal kırıklığına uğradım.

"Bu olmaz."

Bilmek istediğim şey "gözlüklü bir adam" gibi genel bir özellik değil, bireyin kimliği: "Bu Bay A mı, Bay B mi?"

#### 2. Aşama: Google Fotoğraflar Entegrasyonunun Duvarı ve Yapay Zekânın Cevabı

Bu yüzden Gemini'ye saf bir fikir sundum.

"Bu sistemi Google Fotoğraflar'ıma bağla. Orada arkadaşlarımın ve müdavimlerimin yüz gruplama verileri var, onlarla eşleştirirsen adları alabilirsin, değil mi?"

Gemini'nin cevabı soğuk ama doğruydu.

"Üzgünüm ama bu mümkün değil. Google Fotoğraflar'daki yüz tanıma verileri son derece hassas gizlilik bilgileridir ve güvenlik nedeniyle dış programlar tarafından kullanılmasına izin verilmez."

Haklı. Yol burada bitmiş gibiydi.

Ama buradan "vibe coding'in (diyalogla geliştirmenin)" gerçek özü başladı. Yapay zekâ yalnızca reddetmedi.
