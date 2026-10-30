## Bab 2: Teknologi - Di Sebalik Sistem Tempahan

Perkara utama bab ini

- Mutu perbualan AI lebih banyak ditentukan oleh "fakta kedai yang kita serahkan" dan "sama ada atur cara menimpa balasan AI dengan sendirinya" berbanding kepandaian AI
- Sistem tempahan yang saya bina secara spontan masih mempunyai lubang yang membolehkan maklumat peribadi pelanggan dibaca dari luar, dan langsung tiada ujian automatik. Saya meminta AI mengauditnya untuk menemui perkara ini, dan meminta AI membetulkannya
- Berdasarkan pengajaran daripada itu, saya mengubah cara saya membina: takrifkan keperluan dengan terperinci sebelum membina, dan serahkan spesifikasi itu sendiri kepada AI untuk dilaksanakan

(Bab ini mempunyai banyak istilah teknikal. Jika anda tidak berminat dengan teknologi, anda boleh melangkau ke Bab 3 dan kisahnya tetap bersambung.)

### 2-1 Cara Pelayan MCP Berfungsi

MCP (Model Context Protocol) ialah satu set konvensyen bersama untuk AI menggunakan alat dan data luar. Dicadangkan oleh Anthropic, ia kini disokong oleh banyak AI, termasuk ChatGPT dan Claude.

Sebagai analogi, MCP ialah piawaian soket kuasa untuk AI. Kerana bentuk soket ditetapkan, perkakas daripada pengeluar mana pun berfungsi apabila dicucuk. Dengan cara yang sama, jika anda membina tetingkap yang sepadan dengan bentuk MCP, mana-mana AI boleh menggunakan tetingkap itu.

Pelayan MCP memberitahu AI "apa yang boleh anda lakukan melalui tetingkap ini." Pelayan MCP Tamuro, contohnya, menyusun alat seperti berikut.

- Membaca maklumat kedai (waktu perniagaan, bilangan tempat duduk, peraturan kedai, suasana)
- Membaca pelan dan harga (hasil pengiraan diskaun mengikut bilangan orang dan tarikh)
- Membaca slot kosong (waktu yang tersedia untuk ditempah pada hari yang ditentukan)
- Mencipta URL halaman tempahan dengan butiran yang sudah diisi

Apabila pelanggan bertanya kepada AI mereka sendiri, "Tamuro ada tempat kosong malam ini?", AI menyambung ke pelayan MCP Tamuro, memilih "baca slot kosong" daripada alat yang tersusun, dan memanggilnya. Pelayan Tamuro mengembalikan hasilnya, dan AI menyatakannya dalam kata-kata kepada pelanggan.

Yang penting ialah AI tidak mengesahkan tempahan sendiri. Dalam versi pertama, saya dengan sengaja tidak memasukkan pengesahan tempahan dalam alat. Yang boleh dilakukan AI hanyalah membaca, dan mengarahkan orang ke halaman tempahan dengan butiran yang sudah diisi. Butang sahkan ditekan oleh pelanggan sendiri pada halaman Tamuro. Bahaya AI mencipta tempahan salah atau tempahan olok-olok dalam jumlah besar dielakkan melalui reka bentuk sejak awal.

Pengiraan harga menggunakan mekanisme pengiraan yang sama seperti laman tempahan. Harga yang ditunjukkan pada borang tempahan, dalam tetingkap perbualan, dan melalui MCP semuanya keluar daripada satu atur cara yang sama. Ini makna lain bagi tugas yang akan saya tulis kemudian, "menyatukan pengiraan diskaun di satu tempat."

【Rajah 2-1】Daripada AI pelanggan ke halaman tempahan Tamuro. Pelanggan menekan butang sahkan

### 2-2 Cara Tetingkap Perbualan "T-AI-MURO" Berfungsi

#### Harga daripada atur cara, kata-kata daripada AI

T-AI-MURO membahagikan peranan kepada dua. Atur cara menghasilkan harga dan slot kosong dengan pengiraan tetap, dan AI menyatakannya dalam kata-kata kepada pelanggan.

AI pandai menghasilkan teks, tetapi tiada jaminan ia mengira dengan betul setiap kali. Bagaimana diskaun bertindan, peringkat mengikut bilangan orang, bilangan hari untuk diskaun menempah awal, sama ada ia boleh digabungkan dengan happy hour. Jika anda menyerahkan semua peraturan ini kepada AI, ia pasti tersilap di suatu tempat. Dan kesilapan harga paling merosakkan kepercayaan pelanggan.

Maka, bahagian yang tidak boleh salah diserahkan kepada atur cara, dan bahagian yang menyampaikan dengan lembut diserahkan kepada AI. Pembahagian ini ialah prinsip pertama dalam membina tetingkap perbualan.

#### Untuk kedai kecil, anda tidak memerlukan RAG

Untuk meminta AI menjawab tentang kedai, anda perlu menyerahkan pengetahuan kedai kepada AI. Kaedah yang lazim digunakan ialah RAG (retrieval-augmented generation, penjanaan dipertingkat dapatan semula). Anda memotong pengetahuan kepada kepingan kecil dan menyimpannya, dan setiap kali soalan masuk, anda mencari hanya bahagian yang kelihatan berkaitan dan menyerahkannya kepada AI. Apabila pengetahuan itu sangat luas, kaedah ini amat diperlukan.

Tetapi pengetahuan Tamuro tidak sebesar itu. Sejarah kedai, makanan, peraturan, suasana, pemikiran pemilik. Kesemuanya, muat dengan mudah dalam apa yang boleh dibaca AI pada satu masa.

Maka di Tamuro saya memilih untuk meminta AI membaca keseluruhan teks pengetahuan kedai setiap kali. Tidak perlu membina mekanisme carian seperti yang diperlukan RAG, dan tiada yang terlepas dalam carian. Pada mulanya saya merancang untuk menggunakan semula mekanisme RAG, tetapi di pertengahan saya beralih kepada pendekatan teks penuh.

Membacanya keseluruhan setiap kali memerlukan lebih banyak kos AI. Maka saya menggunakan mekanisme yang menggunakan semula teks yang sama untuk merendahkan kos input (prompt caching: daripada meminta AI membaca semula pendahuluan yang sama setiap kali, ia mengingati apa yang telah dibacanya). Cukuplah untuk memperkenalkan RAG apabila pengetahuan menjadi besar.

#### Atur cara yang menimpa balasan dengan sendirinya

Dalam Bab 1, saya menulis bahawa hanya 9 daripada 36 lulus dalam ujian pertama. Sebahagian puncanya terletak pada cara atur cara dibina.

Apabila saya menyiasat, saya mendapati mekanisme lama yang masih tertinggal di mana atur cara menilai balasan yang dibuat AI mengikut kata kunci dan menggantikannya dengan ayat tetap. Apabila perkataan seperti "tempahan" atau "hari ini" muncul, ia membuang balasan AI dan menggantikannya dengan senarai slot kosong. Walaupun AI menjawab dengan betul, ia tidak pernah sampai kepada pelanggan.

Tambahan pula, saya mendapati bahawa bahagian utama pengetahuan kedai (33 bahagian) tidak dimasukkan dalam arahan kepada AI. AI telah menjawab tanpa mengetahui tentang kedai.

Mutu perbualan AI lebih banyak ditentukan oleh fakta kedai yang diserahkan dan sama ada atur cara menimpa balasan AI dengan sendirinya, berbanding kepandaian AI sendiri.

#### Lengkapkan Soal Jawab yang Dijangka dengan Mengira

Saya menambah senario ujian daripada 36 yang pertama kepada 110, kemudian kepada 355. Tetapi jika orang menambah senario mengikut sesuka hati, tiada cara untuk mengetahui sama ada ada yang tercicir. Bagi soalan "Adakah ini menyeluruh?", jawapan jujurnya ialah "Belum menyeluruh."

Maka daripada meluaskan liputan dengan imaginasi, saya menjadikannya soal mengira dengan mesin tempat-tempat yang belum dilalui, dan mengisinya. Untuk empat perkara: 33 bahagian pengetahuan kedai, peralihan antara pilihan, peringkat diskaun, dan gabungan slot waktu dengan hari dalam seminggu. Saya mengira berapa kali setiap satu dilalui dalam ujian, dan menambah senario secara automatik di mana kiraannya sifar.

Saya juga menggunakan kaedah menyilangkan enam paksi (bilangan orang, tujuan, cara minum, tarikh dan masa, pertuturan, menu) dan mencipta senario supaya setiap pasangan dua gabungan dilalui sekurang-kurangnya sekali.

Saya juga menemui lubang berkaitan masa. "Hari ini" dan "mulai sekarang" ditentukan oleh waktu sebenar ujian dijalankan, jadi hasil menjalankannya pada tengah hari dan pada waktu malam berbeza. Maka saya menetapkan jam semasa pengujian dan menjalankannya pada lima titik masa: sebelum buka, semasa waktu perniagaan, sejurus sebelum tutup, pada hari cuti biasa, dan pada hari cuti umum.

Jawapan AI berbeza sedikit setiap kali, walaupun untuk soalan yang sama. Bagi senario yang terus berkait dengan jualan, saya menetapkan syarat bahawa ia mesti lulus ketiga-tiga kali apabila dijalankan tiga kali.

#### Apabila Angka Rendah, Semak Ujian Dahulu

Dalam ujian yang menjalankan 355 senario pada 5 titik masa, daripada 1,775 perbualan, 28.5% lulus.

Daripada terus mula membetulkan, saya terlebih dahulu mengasingkan: "Adakah angka ini benar-benar kelemahan T-AI-MURO, atau ujiannya yang salah?" Jika anda membetulkan semasa ujian salah, anda akhirnya "membetulkan" malah jawapan yang betul.

| Punca ralat | Bilangan |
| --- | --- |
| Ayat tetap merampas soalan | 276 |
| Tidak menjawab soalan, beralih ke aliran tempahan atau saranan | 266 |
| Kegagalan persekitaran ujian (T-AI-MURO tidak dapat menghasilkan balasan kerana had kos) | 211 |
| Ralat pada tarikh, hari dalam seminggu, cuti umum, hari cuti | 142 |
| Mereka-reka atau menegaskan fakta yang tiada pada kedai, menjanjikan untuk menyampaikan mesej | 119 |

Dua teratas berkongsi akar yang sama: "bertindak balas kepada perkataan dan membuat langkah tetap sebelum menjawab soalan pelanggan." 211 di tempat ketiga bukan ralat T-AI-MURO. Had kos dicapai di pertengahan ujian, dan T-AI-MURO sekadar tidak dapat menghasilkan balasan. Dengan mengecualikan ini, kadar lulus menjadi 32.4%.

AI penilai juga boleh membuat kesilapan. Apabila saya mengeluarkan 20 kes dan menyemaknya, 2 ialah ralat di pihak ujian. Dalam salah satunya, penilai tidak tahu bahawa "laman tempahan ini mempunyai pendaftaran ahli." Penilai juga tidak mengetahui apa-apa di luar bahan yang diberikan kepadanya. Ketepatan ujian ditentukan oleh kelengkapan peraturan kedai yang diserahkan kepada penilai.

Dalam ujian semula selepas pembetulan, kadar lulus bagi panduan harga dan pelan naik daripada 29.4% kepada 42.7%. Saya belum lagi menjalankan ujian akhir yang melalukan setiap kes sekali lagi. Untuk mengekalkan kos rendah, saya memutuskan bahawa ujian semua kes dijalankan hanya sekali, sebelum memasukkan perubahan besar ke pengeluaran. Kadar lulus masih terus dinaikkan walaupun ketika saya menulis buku ini.

#### Ujian menghentikan pengeluaran

Ujian AI memerlukan wang. Ujian 36 senario yang pertama menelan kira-kira ¥426 (kira-kira $2.8). Kebanyakannya dihabiskan untuk "usaha berfikir" AI yang memainkan pelanggan, dan apabila saya mematikannya, 3 senario menelan kira-kira ¥6 (kira-kira $0.04).

Tetapi kemudian suatu hari, di pertengahan ujian, baki penggunaan AI habis dan semuanya berhenti. Dalam satu hari saya telah menggunakan kira-kira 35 juta token (unit teks yang dibaca dan ditulis AI). Puncanya ialah menjalankan ujian 221 senario berulang kali, dan menjalankan senario yang terus berkait dengan jualan sebanyak empat kali setiap satu.

Yang menakutkan ialah ujian dan pengeluaran berkongsi baki penggunaan yang sama. Apabila baki habis, malah tetingkap perbualan pengeluaran pun berhenti. Pada hari lain, kali ini saya mencapai had bulanan yang saya tetapkan sendiri, dan tetingkap perbualan pengeluaran serta AI yang mencipta topik perbualan untuk pelanggan di kedai berhenti serentak.

Bahaya sebenar bajet pengujian bukan bilnya, tetapi hakikat bahawa pengeluaran berkongsi baki penggunaan yang sama.

Dari situ peraturan berubah. Lakukan semakan yang tidak berkos (ujian atur cara dan semakan skrin automatik) dahulu. Hadkan ujian yang memanggil AI kepada yang berkaitan dengan apa yang dibetulkan. Jalankan ujian semua kes hanya sekali, sebelum ke pengeluaran. Tulis anggaran kos dan had dalam arahan, dan berhenti jika ia kelihatan akan tercapai. Untuk mengekalkan dana bagi pengeluaran, hentikan ujian apabila penggunaan seluruh organisasi menghampiri had.

Terdapat juga pengajaran tentang bagaimana kos membengkak. Pernah sekali, kos AI penilai mencecah 2.6 kali ganda anggaran. Puncanya ialah pendahuluan panjang yang diserahkan kepada penilai setiap kali (pengetahuan dan peraturan kedai) tidak digunakan semula, jadi caj pemprosesan semula dikenakan setiap kali. Apabila saya membetulkannya supaya menulis pendahuluan sekali dan menggunakannya semula, kos setiap perbualan turun kepada kira-kira satu pertiga. Kos AI membengkak bukan dengan berapa kali anda memanggilnya, tetapi dengan berapa kali anda menulis semula pendahuluan yang sama.

Ujian penuh 221 senario yang sama turun daripada kira-kira ¥1,040 (kira-kira $6.9) kepada kira-kira ¥400 (kira-kira $2.7) melalui penambahbaikan berulang. Saya menggantikan AI yang memainkan pelanggan dengan skrip tetap, dan membahagikan maklumat yang diserahkan kepada AI kepada "teras yang dihantar setiap kali" dan "bahagian yang dibaca hanya apabila diperlukan."

Kerana kekangan bajet, reka bentuk berubah ke arah menambah bahagian yang boleh disemak dengan kos sifar, iaitu bahagian yang diputuskan oleh atur cara. Akibatnya, ketepatan turut meningkat. Wang mengubah reka bentuk.

【Rajah 2-2】Keputusan ujian AI. Kadar lulus dan pecahan punca ralat

### 2-3 Meminta AI Mengaudit Apa yang Saya Bina

#### Nama pelanggan boleh dibaca dari luar

Pada Ogos 2026, semasa saya menyemak cara sistem tempahan berfungsi, saya membuat satu penemuan yang menyebabkan seram sejuk menjalar.

Data tempahan pelanggan boleh dibaca oleh sesiapa sahaja dari luar. Nama, nombor telefon, alamat e-mel, ruangan permintaan. Segala yang dimasukkan ke dalam tempahan boleh ditarik sepenuhnya, tanpa pengesahan.

Ada sesuatu yang patut saya katakan dengan jujur. Memang benar data itu boleh dibaca dari luar. Pada masa itu, laman tempahan mempunyai trafik yang sangat sedikit, dan saya percaya tidak mungkin ada sesiapa yang benar-benar membacanya. Tetapi saya tidak mempunyai rekod yang boleh membuktikan ia tidak dibaca. "Ia boleh diambil" dan "ia benar-benar diambil" ialah dua perkara yang berbeza, tetapi yang pertama sahaja sudah merupakan kegagalan serius bagi sebuah kedai.

Apabila saya menjejaki puncanya, ia berpunca daripada cara borang tempahan dibina. Untuk mengira tempat duduk kosong, borang memuatkan data tempahan 35 hari terus dari skrin. Jika data itu boleh dibaca terus daripada skrin, maka sesiapa yang tahu cara skrin seperti itu dibina boleh membaca data yang sama. Ia akibat asas pertama yang dibina secara spontan, yang mencapai matlamat "tunjukkan tempat duduk kosong" melalui laluan terpendek.

Saya juga mendapati bahawa alamat e-mel untuk memaklumkan pentadbir kedai terbuka kepada umum, dan bahawa sesiapa sahaja boleh menulis ke tempat penyimpanan terjemahan, yang bermakna data boleh dirosakkan atau kos boleh melambung.

Urutan pembetulan itu penting. Jika saya melarang pembacaan sekali gus, borang tempahan tidak lagi dapat menunjukkan tempat duduk kosong dan akan berhenti berfungsi. Maka mula-mula saya memindahkan pengiraan tempat duduk kosong ke titik akhir di sebelah pelayan. Seterusnya saya mengubah skrin tempahan selesai supaya ia juga hanya mendapat maklumat yang diperlukan daripada pelayan. Akhir sekali, saya menutup pembacaan dari luar. Saya membuat pembetulan dalam empat peringkat mengikut urutan ini dan menerapkannya ke pengeluaran.

Selepas pembetulan, saya menggunakan mesin untuk menyemak bahawa ia benar-benar tertutup. Saya menyediakan ujian yang cuba membaca data tempahan tanpa pengesahan, dan saya menjalankannya secara automatik selepas setiap perubahan untuk memastikan ia sentiasa ditolak. Saya tidak membetulkannya sekali lalu menganggapnya selesai. Saya menyediakannya supaya satu semakan terus berjaga untuk memastikan ia tidak terbuka lagi.

#### Data pelanggan sebenar tertinggal dalam sejarah pembangunan

Kemudian saya meminta AI mengaudit keseluruhan repositori (tempat penyimpanan atur cara), dan satu masalah yang lebih serius timbul.

Semasa pembangunan, sebuah fail yang mengandungi data pelanggan sebenar (alamat e-mel dan nombor telefon daripada 55 tempahan) telah dihantar ke repositori, masih termasuk dalam sejarah perubahan atur cara. Repositori itu persendirian, tetapi memandangkan ia kekal dalam rekod, saya tidak boleh membiarkannya.

Saya membuang fail itu daripada keseluruhan sejarah perubahan, menulis semula sejarah, dan menyimpannya semula. Walaupun begitu, rekod lama sebelum penulisan semula mungkin masih kekal di pihak GitHub, yang menyimpan repositori. Maka saya meminta sokongan GitHub memadamkannya, dan mengesahkan ia telah dilakukan.

Audit itu juga menemui masalah lain: titik akhir terjemahan boleh digunakan tanpa pengesahan, log masuk pentadbir boleh diserang secara brute force, dan terdapat satu tempoh masa di mana, jika pembayaran dihidupkan semula, tempahan boleh disahkan sementara masih belum dibayar. Saya membetulkannya satu demi satu, bermula dengan yang paling serius.

#### Tiada Walau Satu Pun Ujian Automatik

Audit itu mendedahkan satu lagi fakta. Sistem tempahan tidak mempunyai walau satu ujian automatik pun.

Ujian automatik ialah mekanisme di mana mesin menyemak secara automatik sama ada atur cara berfungsi dengan betul. Tanpa ujian, apabila anda membetulkan sesuatu, anda tiada cara untuk menyemak sama ada ada yang lain telah rosak. Setiap kali anda menambah ciri, di suatu tempat sesuatu rosak tanpa disedari. Itulah keadaan sebenar sepanjang tempoh saya membina secara spontan.

Maka saya membina semula asas pengujian dari sifar. Saya memperkenalkan sistem (CI) yang secara automatik menjalankan empat semakan selepas setiap perubahan: semakan jenis, semakan gaya, ujian, dan binaan. Keputusan penting seperti pengiraan harga, penilaian tempahan, memautkan ahli, dan mengeluarkan kupon diasingkan daripada atur cara skrin supaya ia boleh disahkan sendiri. Peraturan membaca dan menulis pangkalan data juga disemak dalam persekitaran ujian yang meniru pangkalan data sebenar. Ujian unit bermula pada 275 dan kemudian bertambah melebihi 500.

Ada satu syarat yang sentiasa saya kenakan pada ujian: "rosakkannya, dan sahkan ia gagal." Walaupun ujian bertukar hijau (lulus), anda tidak tahu sama ada ujian itu benar-benar dapat menangkap masalah. Hanya selepas saya dengan sengaja merosakkan atur cara dan mengesahkan bahawa ujian bertukar merah (gagal) barulah saya mempercayai ujian itu. Itu kerana ujian yang ditulis AI kadangkala tidak menyemak apa-apa langsung.

#### Lapan lubang dalam borang tempahan

Selepas asas pengujian disediakan, saya meminta AI memeriksa semula keseluruhan aliran tempahan. Ia menemui lapan masalah yang menyebabkan kemudaratan sebenar.

Yang paling serius ialah menekan butang hantar berulang kali mencipta tempahan berganda. Ini sebenarnya berlaku di pengeluaran. Saya membetulkannya dengan mekanisme yang memproses tindakan yang sama sekali sahaja walaupun ia tiba dua kali (idempotensi). Masalah lain ialah ini: tempahan tidak dapat disahkan jika maklumat tentang item menu yang dipadam masih kekal; terdapat jurang dalam semakan kapasiti penuh yang meninggalkan ruang untuk melebihi kapasiti; tiada siapa perasan apabila e-mel pengesahan gagal dihantar; input tidak disahkan di sebelah pelayan; mesej dalaman muncul di skrin apabila ralat berlaku; teks dalam ruangan input begitu kecil sehingga skrin membesar sendiri pada iPhone; dan isian automatik untuk input tidak berfungsi.

Bagi kegagalan e-mel, saya menjadikannya boleh dikesan pada skrin pentadbir dan boleh dihantar semula. Semasa penyiasatan itu, saya juga mendapati bahawa log audit yang merekod pengesahan tempahan telah gagal setiap kali, sejak jauh sebelum pembetulan, dan tidak merekod apa-apa.

Saya membetulkannya satu demi satu dan menerapkannya ke pengeluaran.

#### Jangan sekali-kali melangkau pengesahan kod yang ditulis AI

Apa yang saya pelajari daripada pengalaman ini ialah bahawa justeru kerana atur cara ditulis oleh AI, anda tidak boleh melangkau pengesahan.

AI dengan pantas memberi bentuk kepada apa yang diberitahu kepadanya. Tetapi pertimbangan terhadap perkara yang tidak diberitahu, seperti "jadikan ia tidak boleh dibaca dari luar" atau "anggap penghantaran berganda sebagai satu," tidak masuk melainkan anda mengarahkannya. Dan lubang seperti ini terletak dengan senyap di dalam atur cara yang kelihatan berfungsi.

Orang tidak perlu membaca semua kod. Ketepatan atur cara diawasi oleh semakan mesin dan oleh audit daripada AI lain. Sama ada hasilnya sesuai dengan tujuan kedai diawasi oleh pemilik. Anda tidak perlu membacanya, tetapi anda tidak boleh melangkau pengesahan. Itulah yang saya percaya maksud membina dengan AI jenis ejen.

【Rajah 2-3】Peraturan apabila ia boleh dibaca dari luar, dan peraturan selepas pembetulan (petikan) *(Skrin dalam bahasa Jepun.)*

### 2-4 Membina Secara Spontan Melipatgandakan Percanggahan

Semakin banyak ciri yang saya tambah, semakin banyak bahagian yang berlanggar dengan apa yang telah saya putuskan lebih awal.

Kes tipikalnya ialah pengiraan diskaun. Dalam borang tempahan, skrin pengesahan, e-mel, dan skrin pentadbir, pengiraan diskaun ditulis secara berasingan di setiap tempat. Jika saya menukar peraturan diskaun di satu tempat, tempat lain terus mengira dengan peraturan lama. Bagi tempahan yang sama, skrin dan e-mel boleh menunjukkan jumlah yang berbeza.

Kemudian, saya menghimpunkan pengiraan harga ke dalam satu fail. Borang tempahan, tetingkap sembang, dan pelayan MCP semuanya menghasilkan harga dari situ.

Peraturan untuk menindan diskaun juga berubah di tengah jalan. Seperti yang saya tulis dalam Bab 1, happy hour pada asalnya akan boleh digabungkan dengan diskaun lain, tetapi saya mendapati ia tidak akan menguntungkan dan mengubahnya kepada tidak boleh digabungkan. Setiap kali peraturan berubah, seseorang perlu mengingati di mana hendak membetulkan. Itulah kelemahan sistem yang dibina secara spontan.

Terdapat juga ketakpadanan antara persekitaran ujian dengan pengeluaran. Semasa menguji tetingkap sembang, soalan, "Bukankah ada sesuatu seperti diskaun 10%?", mendedahkan bahawa peraturan diskaun dalam persekitaran ujian telah menyimpang daripada pengeluaran. Jika nilai dalam persekitaran ujian berbeza daripada pengeluaran, anda boleh lulus ujian dan masih salah di pengeluaran. Apa yang saya putuskan ketika itu ialah prinsip bahawa "pengeluaran adalah betul." Sejak itu, sebelum setiap ujian dijalankan, saya menyalin tetapan pengeluaran ke persekitaran ujian dan mengesahkan ketakpadanan sifar sebelum menjalankannya.

AI membina apa yang diberitahu kepadanya. Tetapi ia tidak perasan percanggahan dengan keputusan terdahulu. Apa yang mencegah percanggahan bukanlah AI, tetapi memutuskan perkara terlebih dahulu.

### 2-5 Mempelajari Semula Definisi Keperluan

Selepas merenung sistem tempahan yang saya bina secara spontan, saya mempelajari semula definisi keperluan. Definisi keperluan bermaksud memutuskan, sebelum anda membina, apa yang akan anda bina, apa yang tidak akan anda bina, dan siapa yang akan menggunakannya dan bagaimana, serta menuliskannya dalam dokumen.

Ia sesuatu yang saya lakukan sebagai lumrah pada zaman saya sebagai jurutera sistem. Tetapi sebaik sahaja saya boleh membina dengan AI, saya telah melangkaunya tanpa sedar. Beritahu satu idea dan sesuatu yang berfungsi muncul dalam beberapa minit. Dalam kelajuan itu, saya telah mengetepikan usaha memutuskan.

Cara saya membina kini mempunyai tiga peringkat.

1. Pertama, putuskan keperluan dengan terperinci. Apa yang hendak dibina, apa yang tidak, siapa yang akan menggunakannya. Kelakuan setiap skrin. Cara menangani pengecualian (ralat, klik berganda, tamat tempoh). Peraturan yang mudah akhirnya bercanggah kemudian, seperti harga dan diskaun, saya putuskan dengan lebih terperinci. Saya melakukan kerja ini juga dalam dialog dengan AI sembang. Saya meminta AI mencari lubang dan percanggahan lebih awal, dan pemilik yang memutuskan.
2. Tuliskan apa yang diputuskan sebagai "dokumen keperluan." Bukan arahan lisan atau spontan, tetapi dihimpunkan dalam satu dokumen. Ini menjadi satu-satunya piawaian untuk menyemak kemudian apa yang betul.
3. Serahkan keseluruhan dokumen kepada AI dan minta ia melaksanakannya. Saya memberikan keseluruhan dokumen kepada AI yang menulis atur cara (Claude Code), bersama syarat untuk lulus (semua ujian lulus, semak dalam persekitaran ujian sebelum pengeluaran, dan seterusnya). AI membina sendiri sehingga ia memenuhi syarat, dan menyemak sendiri. Pemilik hanya melihat apabila ia berhenti di tengah jalan dan pada semakan akhir.

Contohnya, dokumen keperluan untuk tetingkap sembang "T-AI-MURO" ditulis semula daripada versi pertama hingga ketiga. Dalam versi kedua saya memutuskan "jangan biarkan AI mengira harga," "letakkan pengetahuan kedai dan pengiraan harga dalam satu tetingkap," dan "kekalkan borang juga, untuk orang yang tidak mahu menempah melalui sembang." Dalam versi ketiga saya memutuskan "di mana hendak menyimpan salinan induk pengetahuan kedai," "hanya tetingkap ini menunjukkan slot kosong," "jadikan pertukaran pertama soalan empat pilihan," dan "jangan simpan log perbualan; simpan hanya soalan yang tidak dapat dijawab." Kerana keputusan kekal dalam dokumen, saya boleh menjejaki kemudian mengapa sesuatu itu begitu.

Dengan cara membina ini, walaupun saya menambah ciri, saya boleh menyedari percanggahan serta-merta dengan menyemak berbanding dokumen. Justeru pada zaman AI yang melakukan pembinaan, "keupayaan untuk memutuskan" sebelum membina diperlukan. Itulah pengajaran terbesar yang saya pelajari daripada sistem tempahan.

Saya juga membina mekanisme yang memasukkan prosedur itu sendiri ke dalam dokumen dan menyerahkannya kepada AI, supaya cara membina ini dapat dijalankan dengan cara yang sama setiap kali saya melancarkan produk baharu. Saya akan menulis tentang itu dalam Bab 4.

【Rajah 2-4】Jadual kandungan dokumen keperluan T-AI-MURO (versi 3) *(Skrin dalam bahasa Jepun.)*

### 2-6 Mempelajari Istilah UI

Ada satu lagi perkara yang saya pelajari semula: nama komponen skrin.

Walaupun saya memberitahu AI "buat ini di sini," skrin sering tidak keluar seperti yang saya jangka. Apabila saya memikirkan puncanya, saya mendapati saya tidak tahu nama komponen skrin. Walaupun saya menerangkan "tetingkap kecil yang muncul di atas" atau "notis yang hilang dalam beberapa saat," AI sukar mengetahui maksud saya.

Maka saya membaca buku rujukan tentang UI (antara muka pengguna, rupa dan operasi sesuatu skrin) dan mempelajari nama komponen serta istilah teknikal reka bentuk.

| Komponen | Apakah itu |
| --- | --- |
| Modal | Tetingkap kecil yang muncul di atas skrin. Anda tidak boleh mengendalikan skrin di belakangnya sehingga anda menutupnya |
| Toast | Pemberitahuan yang muncul di tepi skrin selama beberapa saat dan hilang sendiri |
| Tab | Mekanisme di mana menekan sesuatu tajuk menukar kandungan |
| Akordion | Mekanisme di mana menekan sesuatu tajuk membuka dan menutup kandungan |
| Laci | Menu yang meluncur keluar dari sisi skrin seperti laci |
| Lain-lain | Breadcrumb (jejak yang menunjukkan di mana anda sekarang), karusel (item yang anda tatal ke sisi), bottom sheet (panel yang naik dari bawah skrin), dan seterusnya. Setiap nama yang anda pelajari membolehkan anda mengarahkan AI dalam satu frasa |

Apabila anda berkomunikasi dengan nama, skrin yang dihasilkan AI menghampiri sasaran dalam satu percubaan. Jika anda berkata, "Tunjukkan skrin pengesahan tempahan sebagai modal," AI tidak teragak-agak.

#### AI berayun ke ekstrem antara menambah dan memotong

Walaupun selepas saya mempelajari perkataannya, membina skrin dengan AI mempunyai kesukaran jenis lain. AI berayun dengan luas.

Apabila saya meminta pengepala yang "bergaya" untuk laman tempahan, saya mendapat pengepala tebal yang mengagumkan. Tetapi seluruh tujuan laman tempahan ialah tempahan. Bagi pelanggan tetap yang menempah setiap kali, pengepala tebal dengan penerangan panjang hanyalah gangguan. Saya memintanya mengurangkan ketinggiannya kira-kira separuh, dengan mengekalkan jumlah maklumat yang sama.

Apabila saya menyeragamkan pengaki e-mel dan menambah pautan ke Buku Destinasi Seterusnya, teks badan kini kelihatan hambar dan buruk berbanding. Maka saya menambah tajuk, jadual perkara utama, dan satu butang untuk ditekan pada badan juga. Apabila saya menambah pintu masuk ke tetingkap sembang dalam pengaki, ia kelihatan bersepah. Apabila saya memampatkannya ke dalam dua baris pautan yang dipisahkan garis, ia kemas tetapi tidak menonjol. Akhirnya ia ditetapkan pada dua kad yang menunjukkan peranan mengikut "bila hendak menggunakannya." Yang kiri ialah "untuk tempahan seterusnya anda," yang kanan ialah "selepas makan anda."

Terlalu tebal, terlalu dipotong, terlalu menonjol. Yang menentukan titik yang tepat ialah kata-kata pemilik setiap kali.

#### Cadangan reka bentuk tanpa gambar

Ini juga berlaku. Saya meminta AI yang menulis atur cara mencipta cadangan penambahbaikan untuk tetingkap sembang menggunakan AI reka bentuk (Claude Design), dan satu laporan kembali berkata, "Saya telah membuat cadangan untuk lapan skrin." Tetapi apabila saya membukanya, hanya ada penerangan teks. AI tidak dapat melukis gambar, namun hanya laporan "siap" yang tinggal.

Akhirnya, AI di pihak sembang melukis empat cadangan terus dalam skrin reka bentuk. Ia mengambil warna skrin semasa daripada tangkapan skrin, meletakkan sejarah kedai dalam garis masa, membahagikan rasa hidangan kepada dua bahagian, "kaedah memasak" dan "rasa," menjadikan pelan kad penerangan, dan menyeragamkan harga ke dalam ringkasan tempahan.

Apabila anda meminta AI menjalankan ujian, ia berkata "lulus." Apabila anda meminta AI membuat reka bentuk, ia berkata "siap." Menyemak apa yang ada di dalamnya ialah tugas manusia. Piawaian untuk menilai ialah sesuatu yang hanya manusia boleh terus pegang.

#### Apa yang boleh anda bawa pulang daripada bab ini

- Membina sesuatu yang berfungsi dan dapat menjalankannya dengan selamat ialah dua perkara yang berbeza.
- Semak output AI bukan dengan kata-kata AI tetapi dengan ujian. Ujian hanya boleh dipercayai setelah anda menyemak bahawa ia gagal apabila anda merosakkan sesuatu.
- Pengiraan yang tidak boleh salah, seperti harga, tidak patut diserahkan kepada penjanaan teks AI. Serahkan kepada atur cara.

Sambungan bab ini (lubang yang baru ditemui dan langkah yang saya ambil untuk membetulkannya) ada di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
