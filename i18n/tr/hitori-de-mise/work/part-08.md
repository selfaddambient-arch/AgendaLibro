#### 3. Aşama: Bir Alternatif ve Rota Değişikliği

Gemini ardından şunu önerdi:

"Google Fotoğraflar'ı kullanamayız ama açık kaynaklı kütüphanelerle (OpenCV ya da face_recognition gibi) yerel bir ortamda kendi yüz tanıma sisteminizi kurmak mümkün. Deneyelim mi?"

Hemen "Evet" diye cevap verdim.

Buradan itibaren geliştirme planı tamamen değişti. Chrome'un özelliklerini kullanmak yerine, Python adlı bir programlama diliyle sıfırdan bir yüz tanıma sistemi kuracaktım.

#### 4. Aşama: Siyah Ekranla Boğuşmak ve Elektronik Tabloya Bağlanmak

Yapmam gereken şey değişmedi. Gemini'ye "gerekli kütüphaneler nasıl kurulur" diye sordum ve cevabı siyah ekrana (komut istemine) yapıştırdım.

Bir hata belirdiğinde kırmızı yazıyı olduğu gibi Gemini'ye geri fırlattım.

Birkaç saat sonra sistem nihayet tamamlandı.

1.  Web kamera yüzümü yakalıyor.

2.  Bilgisayardaki bir klasörde bulunan "yüz fotoğrafı verileriyle" eşleştiriyor.

3.  Bir eşleşme bulduğunda Google Elektronik Tablo'daki müşteri listesine bakıyor.

4.  Ekranda "Bay Bonta: kare şişede kalan miktar ○○ g." görüntüleniyor.

![Çalışan yüz tanıma sistemi. İşletmecinin yüzünü tanıyor ve bilgileri gösteriyor. Yakalanan görüntü Gemini kullanılarak mozaikle kapatıldı](images/fig-27.png)

Dış kaynak maliyeti: ¥0 (yaklaşık $0,00). Kendi kodlama işim: sıfır.

Higashi-Nakano'nun bir köşesinde eşi benzeri olmayan bir "yüz tanımalı CRM sisteminin" doğduğu andı.

#### 5. Aşama: Ve Sonra "Koruma Sorumluluğunu" Fark Etmek

Sistem tamamlanmıştı. Ama sevinçle birlikte tüylerimin ürperdiğini hissettim.

"Bir dakika. Şu anda bu bilgisayar müşterilerin yüz verilerini (biyometrik bilgi) tutuyor, değil mi...?"

O güne kadar "Çalıştığı sürece sorun yok" diye düşünmüştüm. Ama iş gerçek kullanıma geçince değişir.

Peki bu bilgisayara virüs bulaşırsa? Müşterilerin yüz verileri ve tercih bilgileri (kişisel bilgiler) birlikte sızabilir.

İnternete bağlı olmayan tek başına bir bilgisayar güvenli olurdu, ama rezervasyonları ve sosyal medyayı yönettiğim sürece internet bağlantısı şart.

"Kullanışlı bir araç kurabilmek" ile "onu güvenle yönetebilmek" ayrı konular.

Daha önce beni ikna etmeye gelen bir sigorta acentesinin söz ettiği "siber risk sigortasının" önemini ilk kez gerçekten hissettiğim yer burası oldu.

"Bizim gibi küçük bir dükkâna siber saldırı gelmez" diye gülmüştüm, ama artık yapay zekâ gelişmiş sistemler kurmamıza izin verdiğine göre, biz bireysel işletmeciler de düzgün birer "veri yöneticisi" olma sorumluluğunu üstleniyoruz.

Yapay zekâyla büyülü araçlara kavuşabilirsiniz.

Ama bu büyüyü kullanmak için gereken "asayı (okuryazarlığı)" ve "kalkanı (güvenlik önlemlerini)" taşımanın da bundan sonra bir işletmecinin işinin parçası olduğunu öğrendim.

### 6-6. Özgürlüğün Getirdiği "Sorumluluk" ve "Sigorta"

#### Önemli: Gizlilik ve Kişisel Bilgiler

Bu "yüz tanıma sistemi", teknik olarak nelerin mümkün olduğunu sınamak için kurduğum deneysel bir prototiptir. Gerçek bir dükkânda kullanacak olsanız müşterilerinizin yüz verileri "kişisel bilgi (biyometrik veri)" sayılır ve kanunla (Kişisel Bilgilerin Korunması Hakkında Kanun) sıkı biçimde korunmak zorundadır.

Benzer bir şeyi benimsemeyi düşünüyorsanız lütfen şu iki noktaya kesinlikle uyun.

Müşterileri bilgilendirin ve onay alın: Girişe "Yapay zekâ yüz tanıma kullanıyoruz" yazan bir tabela asmak ve müşteriler üye olurken onay almak gibi bir süreç gerekir. Gizli çekim kesinlikle kabul edilemez.

Verileri koruyun: Verileri internetle bağlantısı kesilmiş bir ortamda yönetmek gibi, sızıntı riskini sıfıra indiren önlemler gerekir.

Bir şeyi kurabilmek, onu yapmaya izinli olmakla aynı şey değildir. Teknik becerisi olan bir işletmeciyseniz lütfen bu teknolojiyi kullanmanın sorumluluğunun da beraberinde geldiğini unutmayın.

Şimdiye kadar el yapımı bir sistemin ne kadar harika olabileceğinden söz ettim. Ama bir işletme sahibi olarak size sert bir gerçeği de anlatmalıyım.

Şu: "Kendi yaptığınız her şey kendi sorumluluğunuzdadır."

Aylık abonelikli bir hizmette (SaaS) sunucu çökerse şirket özür diler ve yeniden çalıştırır.

Ama vibe coding ile kurulmuş bir sistemin "müşteri desteği" yoktur.

Uygulamanız öğle yemeği yoğunluğunda aniden çalışmayı bırakırsa yardıma gelecek kimse yoktur.

Google bir teknik özelliği değiştirdiğinde, dün gayet iyi çalışan kodun bugün hata vermesi gündelik bir olaydır.

Bu yüzden iki hazırlık yapıyorum.

Biri, bir "analog yedek."

"Yüz tanıma durursa kâğıt müşteri defterine bak." "Kasa uygulaması çökerse hesap makinesi ve elle yazılmış fişleri kullan."

Dijital araçlar yalnızca "kullanışlı araçlardır." Onlar durduğunda dükkânınızın da duracağı kadar onlara bağımlı olmamalısınız.

Diğeri, daha önce söz ettiğim "sigorta."

Siber sorumluluk sigortası yalnızca bilgi sızıntısı riskini değil, kendi hatanız sistemi durdurduğunda iş kaybının tazminini de karşılar. BT ile donanan bireysel bir işletmeci için bu, sorumlu bir yetişkin olmanın parçasıdır.

"Bazen işler duracak. Bazen hata yapacağım."

Bunu kabul edip riski üstlenin ve ona karşı önlem alın.

Ancak bu kararlılığa sahip olduğumuzda kimseye bağımlı olmayan "özgür bir sistemi" gerçekten kullanabiliriz.

### 6-7. Uzmana İhtiyacınız Yok. Azim Gerekiyor

Bu iki sistemin geliştirilmesi için dışarıya tek bir yen bile dış kaynak ücreti ödemedim.

Tek kullandığım, ayda birkaç bin yenlik bir yapay zekâ aboneliği ve "Bu kaygıdan (nakit akışı kaygısından) kesinlikle kurtulmalıyım" ve "Müşterilerimi mutlu etmek istiyorum" diye düşünen bir işletmecinin azmiydi.

"Programlama bilmediğim için yapamam" meselesi değil.

Yapmak istediğiniz bir şey varsa (Ne), yapay zekâ onu nasıl yapacağınızı (Nasıl) öğretir.

Anlamadığınız sözcükler çıksa bile (Node.js, PowerShell, Firestore...) korkacak bir şey yok.

Onları tercüme edip bize yol gösterecek, var olan en güçlü ortağımız "Gemini" yanımızda.

#### Not Kutusu 4: Excel ile Veri Tabanı (Firestore) Arasındaki Fark Nedir?

~ "Sizin okuyacağınız bir not" mu, yoksa "sistemin okuyacağı bir defter" mi? ~

Nakit akışı uygulamasının geliştirilmesinde Firebase (Firestore) karşınıza çıktı. Neden Excel değil diye merak etmiş olabilirsiniz.

Elektronik tablo (Excel), "insanların bakıp yazı yazdığı bir defterdir." Çok esnektir, ama bir sistem için "neyin nerede olduğu" konusunda belirsizdir.

Veri tabanı (Firestore) ise "sistem için yapılmış, düzenli bir dolaptır." "Tarih 1. gözeye, tutar 2. gözeye girer" diye sabitlendiği için bir program onu anında işleyebilir. Birkaç kişi aynı anda eriştiğinde de bozulmaz.

"Bir uygulama yapıyorsanız Excel'i değil, veri tabanını kullanın." Bunu bilmek bile yapay zekâya verdiğiniz talimatların seviyesini yükseltir.

## Son Söz: Yalnızca Dükkânınıza Ait Bir "Gelecek Tarifi"

~ Yapay zekâ zor bir teknoloji değil. "Sohbet" için yeni bir ortaktır ~

Bu kitabı sonuna kadar okuduğunuz için teşekkür ederim.

Bu kitaptan yalnızca tek bir şeyi deneyecekseniz şunu deneyin: "O can sıkıcı LINE mesajını doğrudan yapay zekâya yapıştırıp ondan 'bunu bir şemaya çevirmesini' isteyin."

Ben özel bir yapay zekâ uzmanı değilim. Bir restoranın hengâmesinde, her gün "yapay zekâyla iş yerinin diliyle konuşma" pratiğini \
sadece tekrarladım.

Bu yüzden bu kitaptan bir "doğru cevaplar derlemesi" değil, yalnızca bir "düşünme biçimi" alıp götürmeniz bence yeterli.

İlk sayfayı açtığınızda "yapay zekâ kullanmak" sözcükleri zihninizde nasıl bir görüntü canlandırıyordu?

"Zor görünüyor." "Programlama bilgisi gerekiyor, değil mi?" "Bizimki gibi küçük bir dükkânla alakası yok."

Belki böyle bir şey düşünmüştünüz.

Ama şimdi "deneme yanılma" kaydımı buraya kadar okuduğunuza göre, belki zihninizdeki o algı biraz değişmiştir.

Yaptığım şey, ileri BT teknolojisini sonuna kadar kullanmak değildi.

"Bunu elle yapamam" diye söylendim. "Bunu kullanmak zor" diye yakındım. Ve "Daha çok şöyle çalışsın istiyorum" diyerek kapris yaptım.

Bugünlerde mühendisler dünyasında "vibe coding" terimi bir akım.

Yapay zekâyla konuşarak sezgisel biçimde bir sistem kurma yöntemi bu.

Nasıl bir shogi (Japon satrancı) oyuncusu bir sonraki hamleleri okumak için yapay zekâyla konuşuyorsa, biz de yapay zekâyla konuşup "dükkânlarımızın geleceğini" kurabiliriz.

Mutfak çalışanlarınıza "Biraz daha tuz ekle" demek gibi.

Pazarda balıkçıya "Bugün iyi balık var mı?" diye sormak gibi.

Yapay zekâya "Bu işi kolaylaştır" diye seslenmek. Her şey orada başlıyor.

Bir zamanlar bir şirketin sistem biriminde "saha" ile "geliştiriciler" arasında koordinasyon yapardım.

Şimdi aynı şeyi "kendi dükkânım" ile "yapay zekâ" arasında yapıyorum.

Ve buna yürekten inanıyorum:

"Sahanın dertlerini bilen bir işletmeci, en güçlü yapay zekâ komutanı olabilir."

Siz de bugün başlayın.

Önce telefonunuzu çıkarın ve Gemini'yle konuşun.

"Merhaba, bugünkü hazırlığa nereden başlamalıyım?"

"Bu menü kalemini nasıl daha iyi satabilirim?"

"Şu evrak işi çok zahmetli. Bir şey yapabilir misin?"

Bir hata belirirse endişelenmeyin. "Sohbetin" başladığının işaretidir.

Sadece ekran görüntüsünü alın ve "bir şey ters görünüyor" diye geri gönderin.

O sohbetler biriktikçe, sonunda hayal bile edemeyeceğiniz "zaman" ve "nefes alacak alan" ile "yalnızca dükkânınıza ait bir gelecek" sizi bekliyor.

Şimdi, sizin dükkânınız için de güvenilir bir "müdür yardımcısı" işe alalım.

Çünkü geleceğin tarifi, sizinle yapay zekâ arasındaki sohbetten doğacak.

### Bu Kitabın Sunduğu Üç Kapı

Bu kitap PDF olarak, note'ta ve Google Play'de ücretsiz okunabilir. (Yalnızca Kindle'da mağazanın kuralları gereği asgari bir fiyat var.) Karşılığında, kitabı bitirdikten sonra gidebileceğiniz üç yer hazırladım. Bunlardan yalnızca birini kullanırsanız bile bu kitabı yazmaya değmiş olur.

1. Kendi dükkânınızda deneyin. Agenda serisine ücretsiz bir defterle başlayabilirsiniz. https://bontallc.com/agenda?via=b1-tr-{{FMT}}
2. Yaptıklarımı takip edin. Sıradaki araçlarımı ve barın gündelik hayatını note ve X'te yazıyorum. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Tokyo'ya yolunuz düşerse Tamuro'yu ziyaret edin. Higashi-Nakano İstasyonu'nun doğu çıkışından yürüyerek bir dakika. Rezervasyonsuz girebilirsiniz. Bu kitap ilk yazıldığında Tamuro yalnızca referansla müşteri kabul ediyordu. Bugün herkes rezervasyon yapmadan içeri girebilir. Rezervasyon sitesi https://tamuroreservation.vercel.app/?src=b1-tr-{{FMT}}

Bu kitap sayesinde gelenlere: rezervasyon yaparken lütfen "BOOK" kupon kodunu girin. İlk ziyaretinizde size bir içki ikram edeceğiz. Rezervasyonsuz geldiyseniz, ilk siparişinizi verirken "Kitaptan geldim" demeniz yeter. Aynı içkiyi ikram edeceğiz. Kitap sayesinde kaç kişinin geldiğini sayabilmem için kurduğum küçük bir düzenek bu.

### Yazar Hakkında

Raku Bonta

Tokyo'nun Higashi-Nakano semtinde tezgâhta 11 tabure ve tatami odasında 8 oturma yeri olan bir restoranı tek başına işleten bir işletmeci.

Gündüz baharat kokan bir hamburger köri dükkânı. Gece her gün değişen set yemek sunan, yalnızca referansla müşteri kabul eden bir yemek barı.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry](images/fig-28.png)

▼ Yalnızca referansla müşteri kabul eden bar "Tamuro"

https://www.instagram.com/tamuro.higashinakano/

![Yalnızca referansla müşteri kabul eden bar "Tamuro"](images/fig-29.png)

Dükkân, iki haftada bir şarap etkinlikleri, ayda bir yemek atölyesi ve çok servisli akşam yemekleriyle yemek üzerinden topluluk kurmaya da emek veriyor.

Yazar, 12 yıl önce kendi dükkânını açmadan önce bir şirkette "sistem planlaması" ve "çözüm mimarisi" alanında çalıştı.

Unvanlar zor görünüyor ama gerçek iş, "sahanın 'şunu yapmak istiyoruz' isteklerini BT firmalarına doğru biçimde aktarıp yaptıran bir koordinatörlük"tü. İleri programlama yapan bir mühendis olmayan yazar, insanlarla teknolojiyi birbirine bağlayan bir "tercüman" olarak bir geçmişe sahip.

Bugün yazar bu deneyimden yararlanarak Google Gemini gibi üretken yapay zekâları kendi dükkânını işletmek için kullanıyor ve "uzmanlık bilgisi sıfır olsa bile işe yarayan iş dönüşümünü" uygulayıp paylaşıyor.
