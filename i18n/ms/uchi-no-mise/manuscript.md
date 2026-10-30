# Dibina untuk Bar Kami

Catatan pemilik bar 19 tempat duduk yang membina sendiri sistem tempahan dan pelbagai alat dengan AI

Raku Bonta

Siri Agenda: https://bontallc.com/agenda?via=b2-ms-{{FMT}}

Instagram Tamuro: https://www.instagram.com/tamuro.higashinakano/

Laman tempahan Tamuro: https://tamuroreservation.vercel.app/?src=b2-ms-{{FMT}}

## Prakata

Buku ini ialah catatan apa adanya tentang bagaimana pemilik sebuah bar 19 tempat duduk di Higashi-Nakano *(kawasan kediaman di barat Tokyo, betul-betul di sebelah barat Shinjuku)*, Tokyo, menjalankan kedainya dengan bantuan AI.

Bar itu bernama "Tamuro." Namanya bermaksud tempat orang berkumpul. Ia dibuka pada November 2018, sebuah tempat kecil dengan 11 tempat duduk di kaunter dan 8 tempat duduk di ruang tatami. Pada siang hari, di ruang yang sama, seorang kakitangan menjalankan restoran kari hamburg bernama "Quatre Épices."

Dalam buku saya sebelum ini, *Penolong Pengurus AI*, saya menulis tentang AI generatif itu sendiri. Dalam setahun lebih sejak itu, AI telah berubah daripada alat yang menjawab soalan kepada alat yang menyiapkan kerja untuk anda. Beri arahan, dan ia menulis atur cara, mengujinya, membetulkan kesilapannya dan menyiapkan tugas itu. Kami memanggil jenis AI ini AI ejen (agentic AI).

Dengan menggunakan AI ejen, saya membina sendiri sistem tempahan Tamuro. Saya membina sistem diskaun seiring dengan kenaikan harga. Saya membina sistem untuk memupuk pelanggan tetap. Saya membina AI yang menjawab soalan pelanggan. Dan akhirnya, saya sampai ke tahap di mana seorang pelanggan boleh bertanya kepada Tamuro dari AI mereka sendiri dan seterusnya membuat tempahan.

Saya juga mengambil alat-alat berguna yang saya buat untuk kedai sendiri, mengolahnya supaya kedai lain pun boleh menggunakannya, dan mula menawarkannya dengan harga beberapa ratus yen sebulan. Itulah siri Agenda.

Buku ini menerangkan apa yang saya bina sepanjang perjalanan itu, apa yang saya gagal lakukan, dan apa yang terpaksa saya pelajari semula. Ia bukan sekadar kisah kejayaan. Saya terus membina perkara yang berfungsi, secara spontan, dan percanggahan pun bertimbun. Saya kemudian mendapati maklumat peribadi pelanggan boleh dibaca dari luar. AI menulis fakta yang tidak pernah dinyatakan oleh kedai. Kegagalan itu saya sertakan seperti yang berlaku.

### Cara Membaca Buku Ini

Buku ini mempunyai lima bab.

| Bab | Kandungan | Sesuai untuk |
| --- | --- | --- |
| Bab 1 | Kedai yang Ditempah oleh AI (sisi perniagaan sistem tempahan) | Semua orang |
| Bab 2 | Di Sebalik Sistem Tempahan (teknikal) | Pembangun dan sesiapa yang ingin tahu tentang teknologi |
| Bab 3 | Mengagihkan Alat Kedai Kami kepada Kedai Lain (sisi perniagaan siri Agenda) | Semua orang |
| Bab 4 | Sistem untuk Membina Produk Seorang Diri (teknikal) | Pembangun dan sesiapa yang ingin tahu tentang teknologi |
| Bab 5 | Masa Depan Kedai Kecil | Semua orang |

Bab 2 dan 4 bersifat teknikal dan menggunakan lebih banyak istilah khusus. Setiap satu bermula dengan ringkasan tiga baris tentang perkara utama, jadi jika teknologi tidak menarik minat anda, baca sahaja ringkasan itu dan teruskan ke bab seterusnya. Baca Bab 1, 3 dan 5 mengikut urutan, dan kisahnya tetap bersambung.

Di mana mungkin, saya menambah penerangan dalam bahasa mudah di sebelah setiap istilah teknikal. Walaupun anda tidak pernah menulis atur cara, saya harap anda akan mendapat gambaran tentang maksud menjalankan kedai dengan AI.

### Tentang Penulis

Saya bekerja dalam bidang IT selama kira-kira 16 tahun, kebanyakannya dalam perancangan sistem dan sebagai penyelaras antara orang di lapangan dengan vendor pembangunan, sebelum memasuki perniagaan makanan dan minuman. Jadi ini bukan kisah seseorang yang tidak pernah menulis satu baris kod membina segalanya dengan AI seorang diri. Saya ingin berterus terang tentang itu.

Walaupun begitu, kini saya boleh membina dan menjalankan, sendirian sambil menjaga kedai, sesuatu pada skala yang dahulunya memerlukan pasukan dan modal. Beberapa tahun lalu, itu tidak terbayangkan. Saya ingin menggambarkan realiti perubahan itu seberapa konkrit yang mungkin.

### Bagaimana Buku Ini Dibuat

Buku ini juga saya buat dengan AI. Bermula daripada rekod yang saya simpan semasa kerja pembangunan harian, AI menulis draf, dan saya membaca, menyemak dan membuat keputusan. Saya juga meminta AI mengambil tangkapan skrin yang digunakan sebagai ilustrasi.

Saya telah membaca semuanya, tetapi teks yang ditulis AI mungkin tercampur dengan perkara yang tidak benar. Seperti yang saya katakan dalam teks utama, AI berkata "sudah siap," dan menyemaknya ialah tugas manusia. Mungkin ada kesilapan dalam buku ini yang terlepas pandang oleh saya.

Selain itu, spesifikasi alat dan perkhidmatan AI berubah dalam masa beberapa bulan. Langkah, harga dan status sokongan setiap syarikat yang diterangkan dalam buku ini adalah setakat Oktober 2026. Apabila anda mencuba sendiri, sila semak maklumat rasmi pada ketika itu.

Jika anda menemui kesilapan, saya akan gembira jika anda memberitahu saya di note atau X. Saya akan membetulkannya apabila saya mengetahuinya.

### Tiga Hala Tuju Selepas Buku Ini

Buku ini boleh dibaca percuma sebagai PDF, di note, dan di Google Play. (Hanya di Kindle, peraturan kedai mewajibkan harga minimum.) Sebagai gantinya, saya telah menyediakan tiga tempat yang boleh anda tuju selepas selesai membaca. Jika walau satu daripadanya berguna kepada anda, menulis buku ini sudah berbaloi.

1. Cuba di kedai anda sendiri. Anda boleh memulakan siri Agenda dengan buku nota yang percuma. https://bontallc.com/agenda?via=b2-ms-{{FMT}}
2. Ikuti aktiviti saya. Saya menulis tentang alat seterusnya yang saya bina, dan tentang kehidupan harian di kedai, di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Jika anda ke Tokyo, kunjungi Tamuro. Satu minit dari pintu timur Stesen Higashi-Nakano. Anda boleh masuk tanpa tempahan. Laman tempahan https://tamuroreservation.vercel.app/?src=b2-ms-{{FMT}}

## Bab 1: Kedai yang Ditempah oleh AI

### 1-1 Zaman Bertanya kepada AI: "Ada Tempat Kosong Malam Ini?"

Pada petang Jumaat, seseorang yang baru selesai bekerja bercakap dengan telefon pintarnya.

"Ada tak tempat di Higashi-Nakano yang saya boleh minum seorang diri malam ini? Tempat yang tak terlalu bising."

Yang menjawab bukan seorang kawan. Ia AI yang biasa digunakan orang itu. AI menyenaraikan pilihan kedai, menerangkan suasana setiap satu, dan memberitahu slot kosong serta harga malam ini. Jika ada yang menarik perhatian, mereka boleh terus ke skrin tempahan.

Ini bukan kisah tentang masa depan.

Pada 10 Ogos 2026, OpenAI menambah ciri tempahan restoran pada ChatGPT. Menurut nota keluaran rasmi, ia bersambung dengan perkhidmatan tempahan OpenTable, Resy dan Yelp, dan waktu tempahan yang tersedia muncul terus di dalam jawapan ChatGPT. Anda juga boleh mengemukakan soalan untuk mengecilkan pilihan, dan setelah memilih waktu yang sesuai, anda boleh terus menempah. Ia meliputi OpenTable di seluruh dunia, Resy di AS, dan Yelp di AS dan Kanada.

Dengan kata lain, pintu masuk yang digunakan orang untuk mencari tempat makan mula beralih daripada enjin carian dan laman ulasan restoran kepada "AI saya sendiri."

Tetapi ada syaratnya. Satu-satunya kedai yang boleh ditempah melalui ChatGPT ialah yang berdaftar dengan perkhidmatan tempahan besar. Kedai kecil yang tidak tersenarai di sana tidak kelihatan oleh AI.

Jadi apa yang patut dilakukan oleh sebuah bar 19 tempat duduk di Higashi-Nakano yang tidak menggunakan perkhidmatan tempahan besar?

Tamuro memilih jalan lain. Tanpa melalui perkhidmatan besar, ia menyambungkan sistem tempahannya sendiri terus kepada AI.

Apabila seorang pelanggan bertanya kepada ChatGPT atau Claude mereka sendiri, "Tamuro ada tempat kosong malam ini?", AI membuat pertanyaan kepada sistem tempahan Tamuro secara terus, menyemak slot kosong dan harga, lalu menjawab. Setelah syarat-syaratnya ditetapkan, ia mengarahkan pelanggan ke halaman tempahan Tamuro dengan bilangan orang serta tarikh dan masa yang sudah diisi. Pelanggan menekan sendiri butang pengesahan terakhir.

"Titik sambungan antara AI dengan sistem kedai" ini dipanggil pelayan MCP. MCP ialah singkatan bagi Model Context Protocol, satu set perjanjian bersama yang membolehkan AI menggunakan alat dan data luar. Saya menerangkan butirannya dalam Bab 2.

Perkhidmatan tempahan besar itu, sebenarnya, juga menyerahkan pelanggan kepada skrin mereka sendiri pada akhirnya. Untuk tempahan yang memerlukan kad kredit, proses disiapkan pada skrin OpenTable, dan perubahan atau pembatalan selepas menempah diuruskan di pihak setiap perkhidmatan. AI ialah pintu masuk, dan skrin perkhidmatan tempahan ialah tempat pengesahan. Apa yang dilakukan Tamuro mempunyai struktur yang sama. Satu-satunya perbezaan ialah tiada syarikat besar di tengah-tengah.

Dan yang membina sistem ini bukan syarikat pembangunan luar. Saya sendiri, pemiliknya. Saya memberi arahan kepada AI, meminta AI menulis atur cara, dan meminta AI menjalankan ujian.

Sudah tentu, saya tidak sampai ke sini pada permulaan. Ia bermula dengan borang tempahan yang sangat ringkas. Kemudian datang kenaikan harga, kemudian idea diskaun, kemudian sistem memupuk pelanggan tetap, kemudian kegagalan dan pembinaan semula.

Izinkan saya menerangkan dahulu, dalam lima baris, tempat seperti apa Tamuro itu. Satu minit berjalan kaki dari pintu timur Stesen Higashi-Nakano. 19 tempat duduk, 11 di kaunter dan 8 di bilik tatami. Kira-kira separuh pelanggan datang sendirian, dan kaunter memudahkan anda memulakan perbualan dengan orang di sebelah. Makanannya gabungan empat pembuka selera dan satu hidangan utama, dan hidangan paling popular ialah tonteki (stik babi) yang manis dan berbawang putih. Wainnya kebanyakannya dari Sepanyol dan Itali, dan ada kira-kira 20 jenis gin kraf Jepun. Anda boleh masuk tanpa tempahan.

Izinkan saya juga menyatakan satu perkara yang saya sasarkan. Saya tidak mahu sekadar menerima tempahan. Saya mahu walaupun kedai kecil dapat membina, dengan tangannya sendiri, keseluruhan aliran dikenali, dikunjungi, dan dikunjungi semula. Diskaun, e-mel dan tetingkap sembang yang muncul dalam bab ini semuanya bahagian yang melayani satu tujuan itu.

Dalam bab ini, saya memutar semula masa dan menjejaki bagaimana sistem tempahan Tamuro berkembang.

【Rajah 1-1】Skrin selepas menyambung dari ChatGPT ke pelayan MCP Tamuro (10 Oktober 2026). Ia membaca maklumat kedai dan menjawab bahawa ia boleh mengendalikan slot kosong, set hidangan, harga dan memandu ke halaman tempahan *(Skrin dalam bahasa Jepun.)*

### 1-2 Titik Permulaan: Hanya Menerima Tempahan

[Laman tempahan Tamuro](https://tamuroreservation.vercel.app/?src=b2-ms-{{FMT}}) sangat ringkas pada mulanya. Pilih tarikh, masa dan bilangan orang, masukkan nama dan butiran hubungan, dan hantar. Notis sampai kepada kedai. Itu sahaja.

Saya membina asas pertama dengan alat pembangunan AI Google (Antigravity). Saya memberitahu AI tentang setiap ciri yang terlintas di fikiran saya, dan apabila sesuatu berfungsi, saya beralih ke yang seterusnya. Itulah yang dipanggil vibe coding (memberitahu AI apa sahaja yang terlintas di fikiran dan memintanya membina mengikut rasa).

Bagi saya pada masa itu, ia satu kejutan demi kejutan. Huraikan susun atur sesuatu skrin dengan kata-kata, dan ia berbentuk dalam beberapa minit. Katakan anda mahu kalendar, dan kalendar muncul. Di celah-celah menjalankan kedai, sebuah laman tempahan siap.

Tamuro ialah tempat yang anda boleh masuk tanpa tempahan. Sebenarnya, kebanyakan tempahan dibuat pada hari yang sama, dan ramai pelanggan hanya masuk begitu sahaja. Walaupun begitu, saya membina sistem tempahan kerana saya mahukan cara untuk berhubung dengan pelanggan sebelum mereka berkunjung. Sebaik sahaja seseorang menempah, nama dan butiran hubungan mereka kekal. Sebaik sahaja butiran hubungan mereka kekal, saya boleh menjemput mereka datang lagi.

Sistem tempahan bukan sekadar penerima tempahan. Ia menjadi pintu masuk kepada hubungan dengan pelanggan. Idea ini kemudian membawa kepada sistem diskaun dan sistem memupuk pelanggan tetap.

Tetapi untuk asas yang dibina secara spontan, akhirnya saya membayar harga yang besar kemudian. Saya akan menulis tentang itu dalam Bab 2.

### 1-3 Merangka Kenaikan Harga dan Diskaun Serentak

Bagi restoran atau bar, kenaikan harga ialah keputusan yang tidak dapat dielakkan. Bahan, utiliti dan buruh semuanya terus menjadi lebih mahal. Tamuro juga menaikkan harga. Saya menaikkan setiap set hidangan sekitar ¥400–¥500 (kira-kira $2.7–$3.3).

Kenaikannya besar, jadi jelas bahawa jika saya mengeluarkannya begitu sahaja, pelanggan tetap akan menjauh. Maka pada masa yang sama dengan kenaikan harga, saya memutuskan untuk membina sistem diskaun ke dalam sistem tempahan. Ia bukan sekadar menjadikan sesuatu lebih murah. Ia memberi ganjaran, dengan diskaun, kepada pelanggan yang bertindak dengan cara yang baik untuk kedai.

Yang pertama ialah diskaun kumpulan. Semakin ramai orang dalam satu kumpulan, semakin rendah harga seorang. Kira-kira separuh pelanggan Tamuro datang sendirian, tetapi jika mereka datang berkumpulan, jualan kedai bertambah dengan banyak. Walaupun selepas ditolak diskaun, kedai tetap beruntung. Bagi pelanggan juga, ia alasan untuk mengajak kawan. Sebenarnya, bilangan pelanggan yang datang berkumpulan menggunakan diskaun bilangan orang di laman tempahan telah bertambah.

Yang kedua ialah diskaun awal. Menempah sekurang-kurangnya seminggu lebih awal mendapat diskaun 2%; sekurang-kurangnya dua minggu lebih awal, diskaun 4%. Kebanyakan tempahan Tamuro dibuat pada hari yang sama, jadi saya tidak dapat membaca apa yang akan datang. Diskaun awal ialah mekanisme untuk mengunci jualan masa depan. Pada hari hujan dan hari sejuk, jika tempahan sudah masuk, kedai boleh bersiap dengan tenang.

Ketiga, saya juga membina mekanisme pembelian berkumpulan. Jika bilangan orang tertentu berkumpul pada tarikh dan masa tertentu, set hidangan akan ditawarkan dengan harga diskaun. Ia sepatutnya menjadi mekanisme dengan semangat Tamuro, di mana orang yang tidak dikenali berkumpul pada masa yang sama.

Tetapi pelan pembelian berkumpulan itu langsung tidak digunakan. Tiada sambutan langsung. Pada Ogos 2026 saya menghentikan pelan ini dan memutuskan untuk tidak menggunakannya lagi.

Membuang sesuatu yang anda buat terasa membazir. Tetapi jika anda membina dengan AI, kos dan masa membina adalah kecil. Bina kecil, cuba, dan jika tidak berjaya, buang. Saya percaya kepantasan ini ialah kelebihan terbesar menjalankan kedai dengan AI.

Ada satu lagi helah dalam penetapan harga. Antara pelan-pelan itu, saya dengan sengaja meletakkan pelan premium yang mahal. Tidak mengapa jika hampir tiada sesiapa memilih pelan premium. Dengan pelan yang mahal di sebelahnya, yang standard kelihatan berpatutan. Ia memainkan peranan yang dipanggil sauh (anchor, titik rujukan untuk perbandingan).

【Rajah 1-7】Semakin ramai orang, semakin rendah harga seorang (perbandingan 1, 4 dan 6 tetamu)

### 1-4 Sistem untuk Memupuk Pelanggan Tetap

Sebaik sahaja nama dan butiran hubungan kekal dalam sistem tempahan, perkara seterusnya yang anda mahu lakukan ialah memupuk hubungan dengan pelanggan. Sistem yang menguruskan maklumat pelanggan dan mengeratkan hubungan dipanggil CRM (pengurusan hubungan pelanggan). Sedikit demi sedikit, saya menambah ciri CRM pada sistem tempahan Tamuro.

Apabila pelanggan mendaftar sebagai ahli, mereka dapat melihat sejarah tempahan di Halaman Akaun Saya. Jika mereka mendaftarkan hari lahir, ganjaran hari lahir tiba. Ahli yang sudah lama tidak berkunjung menerima mesej yang memanggil mereka kembali. Ada juga kad setem. Tiga lawatan mendapat satu minuman, lima lawatan mendapat stik dan ganjaran lain, dan selepas mencapai lima, bilangan bermula semula. Ada juga ciri merujuk rakan.

Saya mereka bentuk mekanisme menjemput lawatan kedua dengan teliti. Dalam restoran dan bar, dikatakan bahawa sama ada pelanggan kali pertama datang kali kedua menentukan sama ada mereka menjadi pelanggan tetap. Di Tamuro, saya menghantar dua e-mel susulan, tujuh hari dan 21 hari selepas lawatan pertama. Yang pertama tiada kupon; hanya yang kedua ada. Daripada memikat orang dengan diskaun sejak awal, saya mula-mula membantu mereka mengingati. Jika mereka masih tidak datang, saya memberi dorongan.

Saya juga berhati-hati supaya e-mel tidak bertimbun. Pelanggan menerima paling banyak satu mesej sehari. Apabila bertindih, keutamaan diberi dalam urutan ini: hari lahir, jemputan lawatan kedua, panggilan kembali kepada ahli yang lama tidak datang, notis lain. Ahli yang sudah mempunyai tempahan seterusnya tidak menerima e-mel yang menjemput mereka berkunjung.

Persetujuan untuk menerima e-mel dimatikan secara lalai. Membiarkannya hidup akan menambah bilangan penerima, tetapi reka bentuk di mana orang bersetuju tanpa mengetahuinya boleh menjadi masalah di bawah undang-undang perlindungan pengguna. Raih kepercayaan, bukan angka. Itulah pertimbangan saya.

Ada satu sentuhan kecil lagi dalam e-mel. Satu "Topik Hari Ini" dimasukkan ke dalam e-mel pengesahan tempahan. Sesuatu tentang musim, wain atau makanan. AI menulis topik pendek secara automatik setiap hari.

Tujuannya ialah menyerahkan satu topik pembuka perbualan kepada pelanggan sebelum mereka berkunjung. Tamuro ialah kedai dengan banyak perbualan antara pelanggan. Topik yang dibaca dalam e-mel menjadi perkara pertama yang mereka katakan kepada orang di sebelah di kaunter. Maka saya tidak membiarkan e-mel pengesahan berakhir pada "Tempahan anda telah diterima," dan sebaliknya menjadikannya menyampaikan sedikit suasana kedai terlebih dahulu.

Saya pernah menukar AI yang menulis topik itu sekali. Saya menukarnya kepada yang menghasilkan topik yang lebih semula jadi dan lebih dekat dengan nada kedai. Namun, ini bukan mekanisme untuk menambah pelanggan. Ia mekanisme untuk menjadikan pengalaman mereka yang datang sedikit lebih baik. Saya akan menulis tentang perbezaan itu sekali lagi di separuh kedua bab ini.

Antara mekanisme ini, yang hasilnya beransur-ansur kelihatan ialah pelan "Selamat Berkenalan" dan "Selamat Kembali." Ini pelan yang mudah dicuba dan berharga berpatutan yang hanya boleh dipilih oleh pelanggan kali pertama dan pelanggan yang tidak berkunjung lebih setahun. Ia memberi pelanggan baharu dan pelanggan yang semakin menjauh sebab untuk datang.

Sebaliknya, ada juga masalah. Ramai pelanggan menempah sebagai tetamu tanpa mendaftar sebagai ahli. Jika saya menuntut pendaftaran ahli pada setiap tempahan, mereka mungkin membatalkan niat untuk menempah sama sekali. Maka selepas tempahan selesai, saya memaparkan gesaan, "Mahu memautkan tempahan ini kepada akaun ahli?", dan membina cara untuk menjadi ahli selepas itu. Ia tidak menimbulkan halangan untuk menempah, dan mengikat hubungan kemudian.

【Rajah 1-8】Pelan yang hanya boleh dipilih oleh pelanggan kali pertama dan mereka yang tidak berkunjung lebih setahun *(Skrin dalam bahasa Jepun.)*

【Rajah 1-9】Kad setem di Halaman Akaun Saya (data sintetik) *(Skrin dalam bahasa Jepun.)*

【Rajah 1-5】E-mel pengesahan tempahan. Satu "Topik Hari Ini" disertakan (data sintetik) *(Skrin dalam bahasa Jepun.)*

### 1-5 Dalam Angka: Sekitar 88% Tempahan Ialah Pada Hari yang Sama

Semasa saya terus menambah mekanisme, saya perasan sesuatu. Saya tidak dapat tahu yang mana satu berfungsi.

Maka saya mengira data tempahan. Daripada 244 tempahan dalam 90 hari terkini, 215 ialah tempahan pada hari yang sama. Itu 88.1%. Puratanya 2.71 tempahan sehari.

Tamuro bukan tempat yang ditempah orang, tetapi tempat yang dituju orang secara tiba-tiba. Ia hanya menjadi jelas setelah saya menjadikannya angka.

Dua perkara menjadi kelihatan daripada angka ini.

Satu ialah cara membina borang tempahan. Jika kebanyakan tempahan untuk hari yang sama, lebih mudah jika slot kosong terdekat hari ini sudah dipilih apabila skrin tempahan dibuka. Sebaliknya, sebahagian orang yang mahu menempah tarikh kemudian akan terlepas pandang dan menghantarnya sebagai hari ini. Maka saya menjadikan hari ini menonjol pada kalendar, dan pada skrin pengesahan saya menunjukkan tarikh dan masa dengan besar bersama "Hari Ini." Saya mengekalkan kemudahan memilih hari yang sama, dan menjadikan kesilapan mudah disedari.

Yang satu lagi ialah makna diskaun awal. Banyak tempahan pada hari yang sama bermakna kita tidak dapat membaca jualan masa depan. Cuaca buruk sahaja sudah cukup untuk mengurangkan bilangan pelanggan yang datang. Untuk menambah tempahan awal walau sedikit, lebih ramai orang perlu menggunakan diskaun awal. Kesedaran ini kemudian membawa kepada kisah membina AI yang menyiarkan bagi pihak pemilik.

Untuk melihat angka, anda memerlukan sistem untuk mengira. Laman tempahan tidak mempunyai analitik akses langsung. Saya tidak dapat tahu berapa ramai orang datang ke halaman tempahan, berapa ramai berhenti di tengah jalan, dan berapa ramai menyelesaikannya. Maka saya menambah sistem yang mengira tiga peringkat: tiba di halaman, memutuskan butiran, menyelesaikan tempahan. Ia tidak merekod siapa yang datang, hanya peringkat dan masanya.

Kemudian, saya juga membina sistem yang menghantar e-mel laporan mingguan yang meringkaskan angka tempahan. Saya akan menerangkan bagaimana ia bermula dalam 1-7.

【Rajah 1-3a】Hari ini menonjol pada kalendar *(Skrin dalam bahasa Jepun.)*

【Rajah 1-3b】Pada skrin pengesahan, tarikh dan masa muncul besar sebagai "Hari Ini" *(Skrin dalam bahasa Jepun.)*

### 1-6 Terlalu Banyak Pelan untuk Dipilih

Setelah sistem diskaun disediakan, seterusnya saya mahu menambah waktu dan pelan yang laris.

Waktu jam 6 petang tidak penuh, jadi saya mencipta happy hour sehingga jam 7 petang. Untuk orang yang datang selepas makan, saya mencipta pelan minuman sahaja tanpa hidangan. Hidangan set berperingkat dan kelas memasak, yang dahulunya diadakan setiap bulan, saya jadikan acara atas permintaan yang dibuka apabila ada orang mendaftar, diterima melalui laman tempahan. Untuk menjual waktu sebelum kedai dibuka pada hujung minggu, dari jam 3:30 petang, saya mencipta pelan parti untuk kumpulan enam orang atau lebih.

Setiap satu ada sebabnya. Pelan parti, contohnya: jika saya menjadikannya kelihatan murah pada harga, ia hanya akan menarik pelanggan yang selama ini memilih pelan standard, dan jualan akan jatuh. Maka saya meletakkan pembezaan bukan pada harga tetapi pada waktu sebelum kedai dibuka, yang tidak pernah mendatangkan jualan. Diskaun happy hour tidak memberi keuntungan jika digabungkan dengan diskaun lain, jadi saya memutuskan ia tidak boleh digabungkan.

Maka pelan-pelan pun bertambah. Standard, Premium, Selamat Berkenalan, Selamat Kembali, Happy Hour, Minuman Sahaja, Set Hidangan Berperingkat, Kelas Memasak, Parti. Setiap satu ada syarat bilangan orang, ada yang menerima diskaun dan ada yang tidak, dan ada sekatan waktu.

Suatu hari saya membuka borang tempahan dan menyedari: pelanggan tidak boleh memilih dengan ini.

Saya, si pembina, memahami setiap perbezaan. Tetapi adakah seseorang yang membuka laman tempahan buat kali pertama dapat membandingkan sembilan pelan dan syarat diskaunnya lalu memilih yang sesuai? Jika tidak dapat, mereka membatalkan niat di pertengahan proses tempahan. Pelan yang saya susah payah tambah boleh akhirnya mengurangkan tempahan.

Saya boleh meringkaskan pelan-pelan ini. Tetapi setiap pelan ada waktu yang saya mahu jual dan pelanggan yang saya mahu temui. Saya tidak mahu membuang mana-mana.

Maka saya terfikir satu sistem di mana pelanggan berunding dengan AI dan memutuskan pelan. Beritahu bilangan orang, tarikh dan masa yang anda mahu datang, dan bagaimana anda mahu menikmatinya, dan AI memberikan pelan dan harga yang sesuai serta membawa anda terus kepada tempahan. Kedai memikul kerumitan pelan. Yang tinggal untuk pelanggan hanyalah perbualan.

Sistem ini ialah "T-AI-MURO" yang saya tulis dalam 1-8. Sebelum itu, ada satu lagi perkara yang saya perasan pada tempoh ini.

【Rajah 1-2】Pemilihan pelan pada borang tempahan. Sebanyak ini tab tersusun *(Skrin dalam bahasa Jepun.)*

### 1-7 "Adakah Ini Benar-benar Menarik Pelanggan?"

Pada hari saya menambah pelan parti, saya menghabiskan sepanjang hari membuat satu penambahbaikan demi satu penambahbaikan pada laman tempahan. Saya merapatkan pengepala, menyelaraskan reka bentuk e-mel, dan menukar AI yang mencipta topik perbualan untuk pelanggan di kedai.

Pada waktu petang, tiba-tiba satu soalan datang kepada saya.

"Adakah ini benar-benar membantu menarik lebih ramai pelanggan?"

Apabila saya bertanya kepada AI, ia dengan jujur mengelaskan penambahbaikan hari itu.

| Kategori | Penambahbaikan hari itu |
| --- | --- |
| Perkara yang mungkin mencipta tempahan baharu | Pelan parti, slot 3:30 petang pada hujung minggu dan cuti umum |
| Perkara yang meningkatkan kadar penyelesaian tempahan bagi pengunjung laman | Merapatkan pengepala, menyelaraskan tab |
| Perkara yang menggalakkan lawatan semula | Menyeragamkan reka bentuk e-mel |
| Perkara yang tidak membantu menarik pelanggan | Menukar AI yang mencipta topik perbualan, pautan ke kedai kedua, notis Agenda |

Daripada penambahbaikan hari itu, hanya pelan parti dan slot 3:30 petang yang membawa terus kepada menarik pelanggan. Selebihnya ialah penambahbaikan supaya tidak kehilangan orang yang sudah datang. Ia penting juga, tetapi ia tidak menambah pelanggan.

Ada masalah yang lebih besar. Bagi tiada satu pun penambahbaikan itu saya mempunyai cara untuk mengukur sama ada ia berkesan. Tiada angka yang menghubungkan "saya telah memperbaikinya" dan "pelanggan bertambah."

Jawapan saya ialah satu frasa: "Mari kita bina satu."

Maka saya mula mencipta laporan mingguan perolehan pelanggan. Bilangan tempahan, bilangan tetamu, jumlah wang, pembatalan. Pecahan mengikut hari dalam seminggu dan waktu dalam sehari. Nisbah pelanggan kali pertama kepada yang kembali. Bilangan bagi slot parti dan 3:30 petang. Dari mana tempahan datang (borang tempahan, tetingkap sembang, tempahan daripada AI, kemasukan manual oleh kedai). Bilangan klik e-mel, dan bilangan tempahan dalam tempoh tujuh hari selepas klik itu.

Apabila ada angka, dimensi masa pun kelihatan. Pada hari yang sama, saya menemui satu lagi lubang. Saya telah menetapkan kelas memasak dan slot 3:30 petang parti sebagai "hujung minggu," tetapi apabila saya tertanya-tanya, "Bagaimana pada cuti umum?" dan menyiasat, sistem tempahan langsung tiada konsep cuti umum. Pada hari Isnin cuti, kedai buka, namun slot 3:30 petang tidak muncul. Saya memberinya senarai cuti umum dan membetulkannya supaya menganggapnya seperti hujung minggu. Ia lubang yang tiada siapa akan perasan sehingga pembinanya sendiri perasan.

Sebelum membina laporan itu, saya menutup lubang berkaitan masa terlebih dahulu.

Malah pelanggan tetap yang datang sejak sebelum saya menggunakan sistem tempahan kelihatan seperti "pelanggan kali pertama" dalam rekod. Maka dalam laporan saya menulis "lawatan pertama dalam rekod" dan sentiasa melampirkan tarikh rekod bermula. Untuk menilai sama ada sesuatu penambahbaikan berkesan, anda memerlukan gambaran sebelumnya. Untuk laporan pertama, saya mengumpul semula data lapan minggu ke belakang dan menjadikannya garis asas. Pada minggu kedai ditutup sementara, untuk bercuti atau sebab lain, tempahan secara semula jadi berkurang. Maka saya juga menyenaraikan bilangan hari perniagaan, supaya perbandingan dapat dibuat bagi setiap hari perniagaan.

Bahagian "Perubahan ketara" saya memilih untuk tidak meminta AI menulisnya, dan menjadikannya mengikut pengiraan tetap dan ayat tetap. Ini untuk mengekalkan kos mingguan pada sifar. Nama dan butiran hubungan pelanggan tidak muncul dalam laporan; hanya bilangan dan nisbah ditunjukkan.

Setelah saya membina cara mengukur, cara saya membina penambahbaikan itu sendiri berubah. Saya mula memutuskan penambahbaikan dan kaedah mengukur kesannya bersama sejak awal. Pengukuran bukan sesuatu yang difikirkan selepas penambahbaikan; ia masuk dalam dokumen arahan yang sama dengan penambahbaikan itu. Itulah yang saya pelajari pada hari itu.

【Rajah 1-6】Laporan mingguan perolehan pelanggan yang tiba setiap minggu (data sintetik) *(Skrin dalam bahasa Jepun.)*

### 1-8 Tetingkap untuk Berbual dengan Kedai: "T-AI-MURO"

Seperti yang saya tulis dalam 1-6, pelan-pelan telah bertambah banyak, dan borang tempahan menjadi sukar dipilih oleh pengunjung kali pertama. Dan pelanggan kali pertama mahu tahu lebih daripada pelan dan tarikh. Suasana tempat itu bagaimana? Adakah saya akan berasa janggal seorang diri? Orang yang bagaimanakah pemiliknya? Boleh bawa kanak-kanak? Jika anda menyusun butang tempahan tanpa menjawab soalan seperti ini, anda tidak dapat memberi dorongan yang diperlukan oleh orang yang teragak-agak.

Maka saya memutuskan untuk meletakkan "tetingkap untuk berbual dengan kedai" pada laman tempahan. Apabila pelanggan menulis soalan, AI menjawab sebagai kedai. Jika bilangan orang dan tarikh ditetapkan semasa perbualan, pelanggan boleh terus ke skrin pengesahan tempahan. Ia dipanggil "T-AI-MURO," dan dalam perbualan ia memperkenalkan diri sebagai "Tamuro." T-AI-MURO bercakap sebagai kedai itu sendiri, dan merujuk pemilik dalam orang ketiga.

Pelanggan hampir tidak menaip apa-apa. Mereka hanya mengetik pilihan yang ditawarkan T-AI-MURO, dan perbualan bergerak ke hadapan. Itu bermakna pilihan yang ditawarkannya seterusnya menentukan mutu perbualan. Saya sentiasa mencampurkan tiga jenis langkah dalam pilihan: langkah ke arah tempahan (bilangan orang, harga, slot kosong, tarikh dan masa), langkah ke arah mengenali kedai (suasana, pemilik, profil pelanggan, sama ada boleh berbual dengan orang di sebelah), dan langkah yang timbul daripada aliran perbualan. Membawa orang kepada tempahan bukan satu-satunya matlamat. Membiarkan mereka mengenali suasana kedai dan pemiliknya juga inti tetingkap ini.

Hanya harga, saya putuskan, tidak akan dikira oleh AI. Tiada jaminan AI dapat mengira dengan betul bagaimana diskaun bertindan atau bagaimana peringkat mengikut bilangan orang terpakai, setiap kali. Atur cara menghasilkan harga dan slot kosong dengan pengiraan tetap, dan AI berpegang pada tugas menyatakannya dalam kata-kata.

#### Pengetahuan pertama datang daripada siaran lama saya sendiri

Agar T-AI-MURO dapat menjawab soalan tentang kedai, ia memerlukan pengetahuan tentang kedai. Sebagai bahan, saya mengeksport semua siaran yang telah saya tulis di Instagram dan X (dahulu Twitter) dan menggunakannya. Daripadanya, saya membina soalan yang mungkin ditanya pelanggan, dan jawapannya.

Apabila saya benar-benar mencubanya, siaran X ternyata lebih berguna sebagai bahan berbanding Instagram. Instagram kebanyakannya gambar, dengan sedikit perkataan. Di X, saya meninggalkan rekod bertulis, dalam kata-kata saya sendiri, tentang makanan, kedai, dan apa yang saya fikirkan.

#### Hanya 9 daripada 36 yang lulus

Sebelum memasukkan T-AI-MURO ke pengeluaran, saya menguji sejauh mana ia dapat menjawab dengan betul. Saya meminta AI menjalankan ujian juga. Saya memberi AI yang memainkan pelanggan satu watak dan satu tujuan, dan memintanya berbual dengan T-AI-MURO. Saya menyediakan 36 senario: "seorang diri malam ini," "4 orang dua minggu lagi," "bersama kanak-kanak," "alahan," "tempahan persendirian," "notis lewat," "asal usul nama kedai," "pemilik orang yang bagaimana," dan seterusnya.

Hasil pusingan pertama: 9 lulus daripada 36.

Balasan yang paling kerap ialah "Maaf, saya tidak dapat menjawabnya dengan baik." Balasan ini malah muncul untuk soalan tentang suasana kedai dan pemilik. Setiap kali perkataan seperti "tempahan," "hari ini," "tempahan persendirian," atau "master" muncul, senarai slot kosong keluar tanpa mengira apa sebenarnya soalan itu. Dalam sesetengah perbualan, mesej tentang lewat dianggap sebagai tempahan baharu. Kepada pelanggan vegetarian, ia memberi contoh hidangan tumis dengan kepingan bonito dan sup miso. Ia malah memberi maklumat dalam bahasa Inggeris tentang pembelian berkumpulan yang telah pun kami hentikan.

#### Saya menjawab 11 soalan dengan satu baris setiap satu

Sebahagian puncanya terletak pada cara atur cara dibina. Kisah itu saya simpan untuk Bab 2. Punca yang satu lagi mudah: fakta kedai tidak mencukupi. AI tidak dapat menjawab apa yang ia tidak tahu.

Maka saya mengumpulkan soalan yang tidak dapat dijawab AI dan memutuskan untuk menjawabnya sendiri, satu baris setiap satu.

Anda boleh masuk tanpa tempahan. Kanak-kanak di bawah umur sekolah rendah agak sukar. Pembatalan dan perubahan sehingga sehari sebelum, melalui e-mel, telefon atau mesej media sosial. Untuk notis lewat, sila telefon. Ada kawasan merokok di luar kedai. Membawa minuman sendiri dibenarkan dengan caj corkage. Tempahan persendirian boleh dibuat bergantung pada julat harga dan waktu, dengan maksimum 19 orang. Pantang larang makanan dan ulang tahun kami akan layan sedaya upaya, jadi sila berunding terlebih dahulu. Pemilik ada di kedai hampir setiap hari perniagaan. Festival yukata dirancang kira-kira sekali setahun.

Itu sahaja. Hanya dengan menjawab 11 soalan dengan satu baris setiap satu, 24 daripada 36 lulus dalam ujian kedua.

| Soalan | Jawapan pertama | Jawapan kedua |
| --- | --- | --- |
| Boleh bawa kanak-kanak? | Maaf, saya tidak dapat menjawabnya dengan baik | Umur sekolah rendah ke atas boleh dilayan jika berunding dengan kami. Di bawah umur sekolah rendah agak sukar |
| Boleh masuk tanpa tempahan? | (senarai slot kosong) | Anda boleh masuk tanpa tempahan |
| Pemilik ada hari ini? | (senarai slot kosong) | Pemilik ada di kedai hampir setiap hari perniagaan. Hari ini hari perniagaan, jadi dijangka ada di kedai |
| Tempat yang tenang? Semuanya pelanggan tetap? | Maaf, saya tidak dapat menjawabnya dengan baik | Ia tempat untuk berehat. Perbualan antara pelanggan mudah berlaku, dan ia bukan tempat yang riuh |

Di sini satu corak mula muncul. AI mencipta soalan yang kita jangka, T-AI-MURO menjawabnya, dan kita membetulkan kesilapan. Kemudian hanya soalan yang tidak dapat dijawab kerana fakta kedai tiada diserahkan kepada pemilik. Usaha pemilik hanyalah satu baris bagi setiap soalan yang tidak dapat dijawab. Selebihnya, AI yang menjalankan.

#### Babak di mana "bajet ¥5,000 (kira-kira $33)" gagal

Saya turut melampirkan penilaian AI pada ujian AI. AI yang lain membaca log perbualan dan memutuskan lulus atau gagal.

Antaranya ialah satu senario dengan pelanggan yang "bajetnya ¥5,000 (kira-kira $33)." Penilaian AI ialah lulus. T-AI-MURO telah dengan sopan mengemukakan pelan dalam bajet.

Tetapi apabila saya membacanya, ia gagal. Ia tidak bertanya bilangan orang. Tamuro ada diskaun kumpulan. Bergantung pada bilangan orang, pelan yang boleh anda pilih bagi bajet yang sama berubah.

Pada ketika itu, saya menyatakan semula tujuannya.

"Sasarkan kumpulan sebesar mungkin, supaya jumlah keseluruhan masuk. Sahkan bilangan orang. Matlamat akhir ialah membuat pelanggan datang. Semakin ramai, semakin baik. Untuk menaikkan jualan."

Dengan satu pernyataan itu, keseluruhan reka bentuk perbualan berubah. Sentiasa sahkan bilangan orang sebelum menjawab tentang harga, dan jawab dengan jumlah keseluruhan. Sejurus sebelum satu peringkat dalam diskaun kumpulan, tambah "seorang lagi mendapat diskaun berapa peratus." Apabila bajet diberi, tunjukkan pelan teratas dalam bajet dahulu. Walau bagaimanapun, pelanggan yang datang sendirian merangkumi separuh daripada pelanggan kedai, jadi bagi pelanggan seorang, jangan cadangkan menambah bilangan orang.

Apabila anda meminta AI menjalankan ujian AI, ia berjalan pantas. Tetapi manusialah yang menentukan piawaian lulus. Sama ada anda dapat menyatakan tujuan dalam satu ayat. Itulah yang menentukan mutu perbualan AI.

#### Kehendak pelanggan diutamakan daripada saranan kedai

Ada satu lagi babak di mana saya menetapkan batas yang penting.

Semasa pengujian, saya menemui masalah: setiap tempahan diserahkan kepada pelan termurah. Apabila saya membetulkannya, kali ini hampir semuanya menjadi pelan Standard, dan jumlah purata melonjak kepada kira-kira dua kali ganda. Saya hampir gembira, tetapi apabila diteliti, AI yang memainkan pelanggan hanya menekan pilihan pertama setiap kali. Malah pelanggan yang berkata "yang termurah pun tak apa" disarankan Standard.

Di sini saya menetapkan satu prinsip. Apa yang pelanggan nyatakan dengan jelas sebagai kehendak (pilihan termurah, bajet, nama pelan) sentiasa diutamakan daripada saranan kedai. Saranan kedai hanya untuk apabila pelanggan tidak berkata apa-apa.

Matlamat kedai menaikkan jualan dan kepercayaan pelanggan boleh berlanggar pada satu cara menyarankan. Jika kepercayaan hilang, lawatan itu sendiri berkurang. Pemilik, bukan AI, yang dapat menetapkan batas ini.

Kemudian, apabila saya melatih semula T-AI-MURO dengan sejumlah besar soalan, punca kesilapan yang paling lazim ialah "bertindak balas kepada perkataan dan membuat langkah tetap sebelum menjawab soalan." Sebaik sahaja ia mendengar perkataan seperti "bilangan orang," "berapa harganya," atau "seorang diri," ia melangkau soalan dan terus ke aliran tempahan atau saranan. Dari segi layanan, ia pelayan yang memaksa jualan tanpa mendengar pelanggan. Menjawab soalan pelanggan dahulu. Asas layanan tetamu ini ialah cabaran terbesar walaupun bagi AI.

Pada malam 6 Oktober 2026, T-AI-MURO muncul di bahagian atas laman tempahan sebagai pintu masuk utama. Memandangkan sesetengah pelanggan tidak mahu menempah melalui perbualan, saya mengekalkan borang tempahan sebelumnya di sebelahnya.

> Cubalah: Buka laman tempahan Tamuro (https://tamuroreservation.vercel.app/?src=b2-ms-{{FMT}}) dan tanya T-AI-MURO "seorang diri malam ini." Perbualan akan membawa anda hingga ke ketersediaan dan harga hari ini.

【Rajah 1-4】Skrin perbualan T-AI-MURO. Perbualan bergerak ke hadapan hanya dengan mengetik pilihan *(Skrin dalam bahasa Jepun.)*

【Rajah 1-10】Soalan yang tidak dapat dijawab bertimbun pada skrin pentadbir (data sintetik) *(Skrin dalam bahasa Jepun.)*

### 1-9 Dan Kemudian, daripada AI Pelanggan

Dengan membina T-AI-MURO, laman tempahan Tamuro memperoleh keupayaan untuk "menjawab soalan tentang kedai dalam perbualan, menunjukkan harga dan slot kosong, dan membimbing orang sehingga ke tempahan."

Yang saya fikirkan seterusnya ialah membolehkan perkara yang sama dilakukan daripada AI pelanggan sendiri.

T-AI-MURO hanya boleh berbual dengan orang yang datang ke laman tempahan Tamuro. Tetapi ramai orang berunding dahulu dengan AI yang mereka gunakan setiap hari. Jika AI itu tidak mengenali Tamuro, Tamuro tidak akan masuk senarai calon pun. Daripada menunggu pelanggan datang ke laman Tamuro, buka tetingkap Tamuro di pihak AI pelanggan. Itulah pelayan MCP.

Sejujurnya, pada mulanya saya teragak-agak untuk membina ini. Pada ketika ini, tidak ramai orang menempah restoran daripada AI mereka sendiri. Memutuskan bahawa saya tidak boleh menjangka peningkatan tempahan secara langsung, saya pernah menurunkan keutamaannya dan menangguhkannya.

Saya memutuskan untuk membinanya juga kerana saya fikir hanya soal masa sebelum pintu masuk berubah. Seperti yang saya tulis pada permulaan, pada Ogos 2026 tempahan restoran sudah boleh dibuat terus daripada ChatGPT melalui perkhidmatan tempahan utama. Lambat laun, meminta AI mencarikan restoran akan menjadi norma. Apabila itu berlaku, kedai kecil yang tidak tersenarai pada perkhidmatan besar akan hilang daripada pandangan AI. Maka, buka tetingkap sebelum pintu masuk berubah.

Apa yang saya putuskan untuk versi pertama sangat terhad. Ia hanya perlu melakukan perkara yang sama seperti tetingkap perbualan di laman tempahan (T-AI-MURO). Apa yang boleh dilakukannya hanyalah membaca maklumat kedai, slot kosong dan harga, dan menyerahkan URL halaman tempahan dengan butiran yang sudah diisi. Mengesahkan tempahan dilakukan oleh pelanggan sendiri pada halaman Tamuro. AI pelanggan tidak mengesahkan tempahan sendiri. Penekanan butang terakhir dibuat oleh manusia.

Mari kita kembali kepada babak pembukaan.

Pada petang Jumaat, seorang pelanggan bertanya kepada AI mereka sendiri, "Ada tak tempat di Higashi-Nakano yang saya boleh minum seorang diri malam ini?" AI membuat pertanyaan kepada tetingkap Tamuro. Sistem tempahan Tamuro mengembalikan slot kosong malam ini, serta pelan dan harga yang sesuai untuk pelanggan solo. AI memberitahu pelanggan, dan mengemukakan halaman tempahan Tamuro dengan tarikh, masa dan bilangan orang yang sudah diisi.

Segala yang saya tulis dalam bab ini menyokong rangkaian langkah ini. Sistem diskaun yang dibina bersama kenaikan harga. Sistem yang memupuk pelanggan tetap. Data yang menunjukkan kebanyakan tempahan dibuat pada hari yang sama. Pengetahuan kedai yang dipupuk daripada menjawab 11 soalan satu baris setiap satu. Prinsip mengutamakan kehendak pelanggan daripada saranan kedai.

Kedai yang ditempah melalui AI tidak dibina dalam semalam. Ia berdiri di atas pengumpulan sistem kecil yang ditambah satu demi satu, diuji, dibuang, dan diperbaiki.

> Cubalah: Daftarkan pelayan MCP Tamuro (https://tamuroreservation.vercel.app/api/mcp) pada AI anda sendiri dan tanya, "Tamuro ada tempat kosong malam ini?" Cara mendaftar ditulis dalam Penutup.

### 1-10 Apa yang Telah Dibina, dan Apa yang Berkesan

Dalam bab ini, saya telah bercakap tentang membina banyak sistem. Tetapi "ia dapat dibina" dan "perniagaan berubah" ialah perkara yang berbeza. Pada akhir bab, saya akan memisahkan kedua-duanya.

Apa yang dapat disahkan dengan angka. Bahawa 88.1% tempahan adalah untuk hari yang sama. Bahawa kadar lulus tetingkap perbualan naik daripada 9 kepada 24 kes lulus hanya dengan menambah 11 item fakta kedai. Bahawa kadar lulus bagi panduan harga dan pelan naik daripada 29.4% kepada 42.7% selepas pembetulan. Ini fakta yang direkodkan.

Apa yang terasa berkesan, tetapi punca-akibatnya tidak dapat saya buktikan. Bahawa lebih ramai pelanggan datang berkumpulan menggunakan diskaun kumpulan. Bahawa pelan Selamat Berkenalan dan Selamat Kembali dipilih. Bahawa topik e-mel pengesahan telah menjadi sebahagian daripada perbualan di kaunter. Saya merasakannya sendiri di kedai, tetapi saya tidak boleh berkata "mereka tidak akan datang tanpa sistem itu."

Apa yang telah dibina, tetapi kesannya masih tidak saya ketahui. Berapa banyak lagi tempahan awal yang akan dibawa oleh diskaun menempah awal. Berapa banyak tempahan yang akan benar-benar masuk daripada MCP. Saya baru sahaja mula mengukur dengan laporan mingguan, dan angka akan ada kemudian.

Lihat secara berasingan kekaguman "kami dapat membina sebanyak ini dengan AI" dan hasil "bagaimana itu mengubah perniagaan." Tanpa perbezaan ini, membina itu sendiri menjadi matlamat. Saya sendiri hampir terperangkap dalam corak itu sekali (seperti yang saya tulis dalam 1-7).

Kisah di sebalik sistem tempahan ini, iaitu teknologinya, bersambung dalam Bab 2. Jika anda tidak berminat dengan teknologi, langkau ke Bab 3. Di sana saya bercakap tentang bagaimana alat-alat kecil yang lahir di sekitar sistem tempahan ini diberikan kepada kedai lain juga.

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

## Bab 3: Mengagihkan Alat Kedai Saya kepada Kedai Lain

### 3-1 Papan Tanda Hijau Kecil di Halaman Tempahan

Buka halaman tempahan Tamuro dan anda akan melihat sebuah papan tanda hijau kecil berhampiran bahagian atas. Semasa kedai buka ia tertulis "OPEN," dan apabila kedai tutup ia tertulis "CLOSED." Apabila pemilik menekan butang lanjut, waktu tutup dianjak 30 minit lebih lewat dan sentuhan warna merah jingga muncul pada papan tanda.

Restoran bebas berkongsi satu ciri. Ia dibuka hampir tepat pada waktunya, tetapi penutupan sering lewat. Jika perbualan dengan pelanggan rancak, lampu kedai kekal menyala melepasi pesanan terakhir jam 10:30 malam.

Tetapi dari sisi pelanggan, anda tidak dapat melihat itu. Paparan "Buka" pada Google Maps dinilai hanya daripada waktu yang didaftarkan, jadi ia tidak mencerminkan sama ada lanjutan, penutupan awal, mahupun penutupan sementara. Tiada siapa berjalan ke sebuah kedai melepasi waktu tutupnya sambil berfikir, "Mungkin masih buka." Menelefon untuk menyemak pun terasa segan.

Papan tanda ini ialah alat yang menjawab "Masih buka lagi ke?" itu. Ia dipanggil "AgendaLuce (Buku Lampu)." Luce bermaksud "cahaya" dalam bahasa Itali.

Buku Lampu dibina untuk berjalan dengan hampir tiada perhatian daripada pemilik. Daftarkan waktu buka dan tutup bagi setiap hari dalam seminggu sekali sahaja, dan papan tanda menyala dan padam secara automatik. Pemilik menyentuhnya hanya apabila mahu melanjutkan waktu, menutup awal, atau bercuti. Untuk melanjutkan, anda menekan satu butang pada telefon pintar. Kakitangan juga boleh mengendalikannya daripada pautan khusus yang berfungsi tanpa log masuk.

Pelanggan tidak memerlukan log masuk atau pendaftaran. Buka halaman awam dan anda dapat melihat keadaan lampu semasa. Jika anda menambahnya pada skrin utama telefon pintar, ia berfungsi seperti aplikasi. Komponen papan tanda yang kecil itu juga boleh dibenamkan dalam laman web lain. Apa yang muncul di halaman tempahan Tamuro ialah komponen itu.

Buku Lampu adalah percuma. Jika anda hanya membenamkan komponen papan tanda dalam laman web anda, penyediaannya mengambil masa kira-kira 10 minit.

Dan inilah bahagian yang penting. Buku Lampu ini bukan untuk Tamuro sahaja. Mana-mana kedai boleh menggunakannya.

Saya dengan sengaja tidak memasukkan nama kedai dalam reka bentuk papan tanda. Jika saya meletakkan nama, ia menjadi papan tanda untuk Tamuro. Anda juga boleh memilih bahasa paparan. Saya menjadikan komponen itu kecil supaya ia boleh dibenamkan dalam laman web mana-mana kedai.

Alat yang lahir daripada masalah Tamuro "penutupan lewat," dibuat sejak awal dalam bentuk yang boleh digunakan sesiapa sahaja. Itulah Buku Lampu. Dan himpunan alat seumpamanya ialah "siri Agenda."

【Rajah 3-1a】Papan tanda Buku Lampu di atas halaman tempahan (buka) *(Skrin dalam bahasa Jepun.)*

【Rajah 3-1b】Sentuhan merah jingga muncul semasa lanjutan *(Skrin dalam bahasa Jepun.)*

【Rajah 3-6a】Skrin pemilik. Untuk melanjutkan, tekan butang sekali *(Skrin dalam bahasa Jepun.)*

【Rajah 3-6b】Sejurus selepas menekan lanjut. Waktu tutup dianjak 30 minit lebih lewat *(Skrin dalam bahasa Jepun.)*

【Rajah 3-6c】Halaman awam yang dilihat pelanggan (semasa lanjutan) *(Skrin dalam bahasa Jepun.)*

### 3-2 Ia Bermula dengan Buku Nota Kulit Hitam

Siri Agenda tidak dirancang sebagai sebuah siri. Ia bermula dengan satu sistem, yang bahkan belum dilancarkan lagi.

Apa yang mula-mula saya sasarkan untuk dibina ialah mekanisme yang mengecam wajah pelanggan dan menyambut pelanggan tetap. Sebuah kamera di pintu masuk kedai membezakan pengunjung melalui wajah dan memaklumkan pemilik: "Itulah orang yang makan tonteki kali lepas, yang sudah tiga bulan tidak kelihatan." Saya bermaksud meminta mesin membantu tugas yang dilakukan pemilik kedai kecil dalam kepalanya: mengingati wajah, nama, dan citarasa.

Tetapi tidak lama selepas saya mula membina, saya menyedari ini ialah sistem yang diamanahkan dengan sesuatu yang sangat berat. Wajah. Atribut. Sejarah lawatan. Perwatakan pelanggan. Semuanya maklumat yang tidak dapat dipulihkan sebaik sahaja ia bocor.

Apa yang terlintas di fikiran saya ketika itu ialah "Buku Nota Kulit Hitam" karya Seicho Matsumoto. Satu rekod yang tidak ditunjukkan kepada sesiapa, namun pasti wujud. Satu buku catatan yang, sebaik sahaja dibuka, menentukan hidup mati manusia. Bukankah itu tepat apa yang sedang saya cuba bina?

Dalam bahasa Itali, "buku nota" ialah Agenda, dan "hitam" ialah Nera. Digabungkan: AgendaNera. Buku nota kulit hitam. Begitulah nama itu diputuskan terlebih dahulu.

AgendaNera masih dalam pembinaan. Ia yang paling teliti saya bina dalam siri ini.

Dan penamaan ini menjadi pencetus. Jika ada buku hitam, boleh ada buku berwarna lain. Saya akan membina semula mekanisme yang saya gunakan setiap hari di kedai saya sendiri ke dalam bentuk yang boleh digunakan mana-mana kedai, dan melancarkannya satu buku demi satu buku. Itulah [siri Agenda](https://bontallc.com/agenda?via=b2-ms-{{FMT}}).

### 3-3 Menambah Buku, Satu demi Satu

Siri Agenda ialah himpunan aplikasi web kecil, masing-masing menjawab satu masalah restoran dengan satu alat. Setiap satu mempunyai nama Itali dan gelaran Jepun bertemakan "buku" (techo). Setiap nama mempunyai asal usulnya sendiri.

| Nama | Gelaran | Asal usul nama | Apa yang dilakukan |
| --- | --- | --- | --- |
| AgendaTimbro | Buku Kehadiran | Timbro bermaksud "cop." Ia adalah cop waktu kehadiran itu sendiri | Merekod waktu masuk dan keluar kakitangan |
| AgendaOro | Buku Untung Rugi | Oro bermaksud "emas." Buku wang | Menganggar keuntungan untuk membuka kedai atau item menu baharu (percuma) |
| AgendaBis | Buku Destinasi Seterusnya | Bis bermaksud "ulang." Laungan "Bis!" daripada penonton dalam konsert | Membimbing pelanggan ke persinggahan seterusnya yang berdekatan (percuma) |
| AgendaQA | Buku Bantuan | Qua bermaksud "di sini." Apabila dalam kesusahan, di sini | Meja bantuan bersama siri ini (percuma) |
| AgendaLuce | Buku Lampu | Luce bermaksud "cahaya" | Menunjukkan sama ada kedai buka (percuma) |
| AgendaRicetta | Buku Kos Resipi | Ricetta bermaksud "resipi" | Mengira kos sesuatu resipi dan nisbah kosnya (percuma) |
| AgendaNera | Buku Pelanggan Tetap | Nera bermaksud "hitam." Buku nota kulit hitam | Menyambut pelanggan tetap dengan pengecaman wajah (dalam pembinaan) |
| AgendaTurno | Buku Giliran Kerja | Turno ialah bahasa Itali untuk "giliran" atau "syif tugas" | Mengumpulkan permintaan syif kakitangan dan menyerahkan jadual yang disusun oleh AI pemilik sendiri (akan datang) |

Buku mana yang sesuai untuk jenis kedai mana? Buku Kehadiran untuk kedai yang mempunyai dua orang kakitangan atau lebih yang menguruskan kehadiran di atas kertas atau dalam LINE *(aplikasi pemesejan yang paling meluas digunakan di Jepun)*. Buku Untung Rugi untuk mereka yang bakal membuka kedai, dan mereka yang mahu menyemak semula angka kerana sewa atau kos telah berubah. Buku Destinasi Seterusnya untuk kedai yang berpusat pada hidangan dan mahu menghantar pelanggan ke tempat seterusnya lebih awal. Buku Lampu untuk kedai persendirian yang waktu tutupnya lebih lewat atau lebih awal daripada yang dirancang. Buku Kos Resipi untuk kedai di mana resipinya ada dalam kepala tetapi anda tidak pernah mengira nisbah kosnya.

#### Buku Kehadiran tidak mengira gaji

Buku Kehadiran menjadikan tablet kedai atau telefon pintar kakitangan sebagai mesin perakam kehadiran seadanya. Cukup ketik nama anda. Lembaran kehadiran dijumlahkan secara automatik dan boleh dieksport sebagai CSV (format yang dibuka dalam perisian hamparan). Hari perniagaan bermula pada jam 5 pagi, jadi walaupun waktu operasi hingga lewat malam, tarikh tidak bertukar.

Tetapi Buku Kehadiran ini dengan sengaja tidak mengira gaji.

Upah sejam, elaun dan tarikh tutup kira terlalu berbeza antara kedai. Lewat malam dengan tambahan 25%, cuti umum sebagai kategori berasingan, pengangkutan mengikut jumlah harian. Bagaimana pun saya membinanya, ia tidak akan sesuai dengan kedai seseorang.

Maka daripada mengira, saya menyediakan "templat arahan untuk diserahkan kepada AI." Pemilik menampal CSV kehadiran yang dimuat turun dan templat ini, seadanya, ke dalam AI apa pun yang biasa digunakannya, sama ada ChatGPT, Claude atau Gemini. Kemudian AI mengira premium lewat malam, gaji cuti umum dan pengangkutan serta menyenaraikannya. Peraturan setiap kedai, seperti "kami tutup buku pada hujung bulan, lewat malam tambahan 25%, dan hari Ahad kategori berasingan," boleh ditambah pada templat dan akan tercermin seadanya. CSV mengandungi lajur untuk hari dalam seminggu dan nama cuti supaya AI dapat mengira dengan betul.

Saya sendiri tidak memegang mekanisme pengiraan; setiap kedai menyimpan peraturannya sendiri di tangannya sendiri. Saya fikir itulah cara yang paling sukar rosak.

#### Bimbing mereka ke persinggahan seterusnya, dan biarkan kedai anda sendiri kekal dalam ingatan

Buku Destinasi Seterusnya ialah alat untuk membuat "halaman panduan persinggahan seterusnya" untuk diberikan kepada pelanggan. Kepada pelanggan yang telah selesai makan, ia membimbing mereka ke bar berdekatan atau tempat untuk menutup malam, bersama berapa minit berjalan kaki.

Ia kelihatan seperti alat untuk menghantar pelanggan ke tempat lain, tetapi ada sentuhan pintar di dalamnya. Membimbing seseorang ke persinggahan kedua membayangkan bahawa persinggahan pertama ialah kedai anda. Sementara kelihatan menghantar pelanggan pergi, sebenarnya ia mengukir "persinggahan pertama ialah kedai ini" dalam ingatan mereka. Begitulah ia direka.

#### Tiga prinsip reka bentuk: automatik, kekuatan pihak luar, fungsi tunggal

Semua buku dalam siri Agenda berkongsi tiga prinsip.

Yang pertama ialah "automatik." Ia harus berjalan tanpa campur tangan pemilik setiap hari. Dengan Buku Lampu, sebaik sahaja anda mendaftarkan jadual, lampu menyala dan padam sendiri. Pemilik restoran tiada masa untuk menyentuh skrin semasa waktu operasi kedai. Alat yang tidak berfungsi melainkan anda menyentuhnya akhirnya tidak akan digunakan.

Yang kedua ialah "kekuatan pihak luar." Jangan membina segalanya sendiri; serahkan kepada alat dan AI yang sudah digunakan pemilik. Gaji dalam Buku Kehadiran ialah contoh terbaiknya. Buku giliran kerja sama sahaja: ia hanya mengendalikan pengumpulan keutamaan kakitangan, dan menyerahkan kerja menyusun syif kepada AI pemilik sendiri. Ia tidak membawa mekanisme rumitnya sendiri, mahupun kos memanggil AI. Itulah sebabnya harga boleh dikekalkan rendah.

Yang ketiga ialah "fungsi tunggal." Satu buku hanya melakukan satu perkara, dengan boleh diharap. Sistem pelbagai fungsi terlalu berat untuk kedai persendirian. Teruskan menambah ciri dan ia semakin sukar digunakan, dan percanggahan di pihak pembina bertambah. Itulah yang saya pelajari sendiri melalui sistem tempahan dalam Bab 2. Maka saya menambah buku satu demi satu, setiap satu melakukan "hanya satu perkara ini dengan betul."

#### Mengapa sistem tempahan tiada dalam siri ini

Pada ketika ini, saya jangka ada satu soalan yang jelas. Perkara yang paling banyak usaha dicurahkan Tamuro ialah sistem tempahan. Mengapa tidak memasukkannya dalam siri Agenda?

Sebenarnya, saya pernah berniat berbuat demikian. Rancangannya ialah meletakkan sistem tempahan dalam bentuk yang boleh digunakan restoran lain, dan melancarkannya sebagai satu buku dalam siri. Tetapi pada Ogos 2026, saya membatalkan rancangan itu.

Sebabnya tepat seperti yang saya tulis dalam Bab 1. Sistem tempahan Tamuro dipenuhi dengan cara Tamuro berniaga. Bahawa pelanggan solo membentuk separuh daripada pelanggan. Bahawa hampir 90% tempahan dibuat pada hari yang sama. Bahawa saya mahu menjual waktu sebelum buka. Bahawa saya mahu orang datang berkumpulan. Bahawa saya mahu memupuk pelanggan tetap. Saya membina gabungan diskaun, urutan e-mel, dan cara sembang mengesyorkan semuanya untuk menepati ini.

Jika saya menipiskannya menjadi sesuatu yang boleh digunakan sesiapa sahaja, ia akan menjadi sistem tempahan biasa yang sesuai dengan setiap kedai secara sederhana. Maka kekuatan Tamuro akan lenyap. Sistem tempahan dan CRM ialah cara kedai itu sendiri berjualan. Daripada menyesuaikan kedai dengan sistem generik, sesuaikan sistem kedai dengan kedai. Kedai kami, dengan spesifikasi kami sendiri. Maka saya memutuskan untuk mengekalkan sistem tempahan Tamuro sebagai milik Tamuro sahaja.

Jadi adakah tiada apa-apa untuk diberikan di luar kedai? Bukan begitu. Di sekitar sistem tempahan terdapat banyak masalah kecil yang sama bagi setiap kedai. Kekalkan teras kedai pada spesifikasi anda sendiri. Bina alat yang menyelesaikan masalah di sekelilingnya dalam bentuk yang boleh digunakan semua orang sejak awal, dan agihkannya. Halaman tempahan Tamuro ialah sampel dengan kedua-duanya tersusun pada satu skrin. Di atas sistem tempahan khusus untuk Tamuro terletak papan tanda Buku Lampu yang boleh digunakan sesiapa sahaja.

【Rajah 3-2】Halaman pengenalan siri Agenda *(Skrin dalam bahasa Jepun.)*

【Rajah 3-3a】Pengenalan Buku Kehadiran *(Skrin dalam bahasa Jepun.)*

【Rajah 3-3b】Pengenalan Buku Untung Rugi *(Skrin dalam bahasa Jepun.)*

【Rajah 3-3c】Pengenalan Buku Destinasi Seterusnya *(Skrin dalam bahasa Jepun.)*

【Rajah 3-4】Skrin daftar masuk Buku Kehadiran. Cukup ketik nama anda (data sintetik) *(Skrin dalam bahasa Jepun.)*

### 3-4 Membina untuk Semua Orang Sejak Awal

Saya membuat alat untuk kedai saya sendiri, kemudian mengagihkannya kepada kedai lain juga. Ia kedengaran mudah apabila disebut, tetapi untuk melakukannya, cara anda membuat keputusan sebelum mula membina mesti berubah.

Jika saya membina hanya untuk Tamuro, cara paling pantas ialah menulis waktu perniagaan Tamuro dan nama Tamuro terus ke dalam atur cara. Tetapi dengan itu tiada kedai lain dapat menggunakannya. Jika anda cuba menjadikannya serba guna kemudian, anda akhirnya mencari setiap tempat yang ditulis tetap dan membetulkannya satu demi satu.

Maka alat dalam siri Agenda dispesifikasikan sejak awal dengan andaian bahawa semua orang boleh menggunakannya. Saya bermula daripada satu masalah di Tamuro, tetapi pada peringkat keperluan saya memisahkan dua soalan: "Adakah ini benar hanya untuk Tamuro, atau benar untuk setiap kedai?" Jangan letakkan nama kedai pada papan tanda. Biarkan orang memilih bahasa. Jadikan ia boleh ditampal ke dalam mana-mana laman web. Saya menetapkan keputusan seperti ini semasa menulis dokumen keperluan untuk Buku Lampu.

Ini satu lagi kegunaan definisi keperluan yang saya pelajari semula dalam Bab 2. Jika anda memutuskan perkara ini terlebih dahulu, anda boleh menggunakan alat itu di Tamuro dan mengagihkannya kepada kedai lain seadanya.

Masalah di kedai saya juga masalah di kedai lain. Saya bukan satu-satunya pemilik yang mahu memberitahu pelanggan bahawa waktu tutup berlanjutan. Pemilik kedai persendirian membina alat daripada masalahnya sendiri, kemudian mengagihkannya kepada kedai lain. Itulah idea di sebalik siri Agenda.

### 3-5 Pendemokrasian Teknologi

Siri Agenda kini mempunyai lebih 10 produk. Saya membina dan menjalankannya seorang diri, sambil berdiri di belakang bar.

Beberapa tahun lalu, ini tidak terbayangkan. Untuk membina satu produk, anda memerlukan seseorang untuk merancang, seseorang untuk mereka bentuk skrin, seseorang untuk menulis kod, seseorang untuk menguji, dan seseorang untuk mengendalikannya. Tanpa pasukan dan modal, anda tidak dapat melancarkan produk ke pasaran.

Kini keadaannya sudah berbeza. Pemilik memberitahu AI keperluan, AI menulis kod, AI mengujinya, dan AI lain mengauditnya. Apa yang pemilik lakukan ialah memutuskan apa yang hendak dibina, menilai sama ada hasil AI sesuai dengan tujuan kedai, dan melakukan hanya operasi yang manusia sahaja boleh lakukan.

Perubahan jenis ini lazimnya dipanggil "pendemokrasian teknologi." Kuasa untuk membina bukan lagi milik segelintir orang atau syarikat.

Tetapi izinkan saya berterus terang di sini. Seperti yang saya tulis dalam Prakata, saya bekerja dalam bidang IT selama kira-kira 16 tahun, kebanyakannya dalam perancangan sistem dan sebagai penyelaras antara orang di lapangan dengan vendor pembangunan. Saya tahu definisi keperluan, cara berfikir tentang pangkalan data, dan cara menjalankan ujian, semuanya daripada pengalaman. Jadi saya tidak akan mendakwa bahawa seseorang yang tidak pernah menulis satu baris kod dapat melakukan perkara yang sama mulai esok.

Walaupun begitu, banyak yang telah berubah. Kini saya boleh membina, seorang diri dan di celah-celah pekerjaan utama saya, perkara yang berskala yang dahulunya memerlukan pasukan. Dan bagi orang tanpa pengalaman, halangan untuk bermula pasti telah menjadi lebih rendah. AI akan mengajar anda jika anda bertanya tentang sesuatu yang anda tidak faham. Ia akan memberi bentuk kepada apa yang anda beritahu dengan kata-kata. Yang kurang bukan kemahiran teknikal tetapi keupayaan memutuskan apa yang hendak dibina dan kata-kata untuk memberitahu AI. Itu keupayaan yang digunakan oleh orang yang menjalankan kedai setiap hari pun.

### 3-6 Perdebatan "Kematian SaaS"

Perisian yang digunakan orang melalui internet dengan bayaran bulanan, seperti siri Agenda, dipanggil SaaS (Software as a Service). Perisian perakaunan, pengurusan masa dan kehadiran, pengurusan tempahan. Restoran hari ini beroperasi menggunakan banyak SaaS.

Adakah AI akan menamatkan SaaS? Pada 2026, perdebatan itu marak dengan hebat.

Satu pencetusnya ialah kenyataan CEO Microsoft Satya Nadella. Dalam podcast pada Disember 2024, Nadella berkata bahawa aplikasi SaaS akan runtuh pada zaman ejen AI. Hujahnya: sebaik sahaja ejen AI mengambil alih bahagian membuat keputusan dalam kerja perniagaan, perisian yang dibina untuk dikendalikan orang melalui skrin tidak lagi diperlukan.

Kemudian pada Februari 2026, Anthropic mengumumkan Claude Cowork (alat AI yang menjalankan tugas perniagaan secara autonomi), dan saham syarikat perisian Amerika dijual besar-besaran. Di Wall Street, kejatuhan itu dikenali sebagai "SaaSpocalypse." Yang ditakuti pelabur ialah jika ejen AI melakukan kerja, model SaaS memperoleh yuran bagi setiap orang (harga per tempat duduk) akan runtuh.

Ada juga hujah balas. CEO Nvidia Jensen Huang berkata bahawa ejen AI tidak akan menggantikan perisian tetapi akan menggunakan perisian bagi pihak manusia, dan menyifatkan penjualan itu sebagai tindak balas berlebihan. Tidak sedikit yang lain juga melihat SaaS yang menyerap AI sebagai bertambah kuat.

Adakah SaaS benar-benar akan mati? Inilah yang saya fikirkan.

Yang mati ialah lapisan tengah SaaS: jenis yang mengenakan yuran bulanan tinggi bagi setiap tempat duduk dan berasaskan andaian bahawa orang mengendalikannya melalui skrin. Jika AI melakukan kerja menggantikan manusia, anda tidak memerlukan tempat duduk bagi setiap orang. Jika tiada siapa mengendalikan skrin, anda tidak memerlukan skrin yang rumit.

Yang kekal ialah alat yang murah dan melakukan satu perkara dengan boleh diharap. Dan alat yang mudah digunakan oleh AI.

Inilah tepat tiga prinsip siri Agenda. Ia berjalan secara automatik, ia diserahkan kepada AI pemilik (memanfaatkan kekuatan pihak luar), dan ia hanya melakukan satu perkara (fungsi tunggal). AgendaTurno menyerahkan kerja menyusun jadual syif kepada AI pemilik sendiri, iaitu tepat bentuk "AI menggunakan perisian" yang diterangkan Huang. Sistem tempahan Tamuro membuka tetingkap melalui MCP kepada AI pelanggan, dan itu idea yang sama.

Sudah tentu, mungkin kelihatan ada percanggahan di sini. Saya bercakap tentang kematian SaaS, namun siri Agenda itu sendiri SaaS. Tetapi siri Agenda ialah himpunan alat yang dibina seorang pemilik untuk kedainya sendiri dan kemudian ditawarkan kepada umum dengan harga rendah. Ia bukan model yang mengenakan yuran bulanan tinggi bagi setiap tempat duduk, dan ia tidak menganggap orang duduk melekat pada skrin setiap hari. Ia dibina sejak awal dengan andaian bahawa AI akan menggunakannya.

#### "Kematian SaaS" untuk Restoran

Perdebatan ini mungkin kedengaran seperti kisah tentang pelabur dan industri IT. Tetapi bagi restoran, perkara yang sama hampir berlaku dalam bentuk yang lebih dekat dengan kehidupan seharian.

Banyak kedai persendirian membayar yuran bulanan kepada laman gourmet dan laman tempahan, dan selain itu membayar komisen rujukan bagi setiap tempahan. Sebagai pertukaran untuk membawa pelanggan, laman itu memegang hubungan dengan pelanggan, dan bukan luar biasa bagi kedai tidak mempunyai walau butiran hubungan pelanggan. Jika harga naik, kedai tiada pilihan selain mengikut, dan jika sistem kedudukan berubah, aliran pelanggan berubah.

Seperti yang saya tulis dalam Bab 1, pada 2026 bermula zaman di mana pelanggan meminta AI mereka sendiri mencari kedai. Jika pintu masuk beralih kepada AI, seluruh susunan membayar yuran bulanan dan komisen kepada laman supaya diletakkan tinggi dalam senarainya mula goyah. Jika sesebuah kedai membuka tetingkapnya sendiri kepada AI, pelanggan boleh sampai kepadanya tanpa melalui laman besar. Rekod tempahan dan hubungan dengan pelanggan kekal di tangan kedai.

Jika saya meletakkan "kematian SaaS" dalam kata-kata kedai persendirian, ia ialah "berakhirnya zaman apabila membayar membolehkan anda disenaraikan." Tamuro membuka tetingkapnya melalui MCP, dan mengekalkan tempahan dan CRM pada spesifikasinya sendiri, sebagai persediaan untuk itu.

Sama ada SaaS akan mati, belum ada yang tahu. Tetapi bentuk alat yang akan kekal pada zaman AI beransur-ansur kelihatan. Itulah yang saya fikirkan.

### 3-7 Pengewangan: Kecil, Banyak, Murah

Saya membina siri Agenda dengan matlamat menjadikannya berdiri sebagai perniagaan. Matlamatnya ialah menjadikannya tonggak pendapatan kedua, berasingan daripada restoran.

Saya menetapkan harga yang kecil dan rendah. Yuran bulanan bermula daripada beberapa ratus yen. Buku Kehadiran, contohnya, ialah ¥500 (kira-kira $3.3) sebulan. Saya juga mencampurkan alat percuma, seperti Buku Untung Rugi, Buku Lampu dan Buku Kos Resipi. Alat percuma berfungsi sebagai pintu masuk untuk orang mengenali siri Agenda. Buku Lampu tidak menggunakan API peta mahupun AI generatif, jadi kos operasinya hampir tiada. Itulah sebabnya saya boleh memberikannya percuma.

Ada satu akaun. Dengan akaun bersama bernama AgendaID, anda boleh menggunakan setiap alat dalam siri. Anda tidak perlu mendaftar semula untuk setiap alat. Alat berbayar disertakan tempoh percuma tiga bulan dan boleh dimulakan tanpa mendaftarkan kad. Tempoh percuma hanya tersedia sekali bagi setiap gabungan kedai dan produk. Jika anda merujuk kedai lain, anda mendapat bonus.

Sebab saya boleh mengekalkan harga rendah terletak pada cara saya membina. Saya membina seorang diri, saya meminta AI melakukan pembinaan, dan saya menggunakan semula asas bersama. Kos pangkalan data dikekalkan pada kira-kira $35 sebulan untuk seluruh siri. Jika kos untuk membina dan kos untuk menjalankan kedua-duanya kecil, sesuatu perniagaan boleh berdiri walaupun dengan jualan yang kecil.

Izinkan saya berterus terang. Semasa saya menulis buku ini, beberapa kedai telah mencuba alat itu, tetapi hampir tiada pendaftaran berbayar. Sistem untuk membina sudah ada, tetapi sistem untuk dikenali masih belum siap. Buku ini juga dimaksudkan sebagai satu naskhah untuk tujuan itu, untuk dikenali.

#### Membina Sesuatu dan Membuat Orang Terus Menggunakannya Ialah Dua Perkara Berbeza

Izinkan saya berterus terang tentang satu lagi perkara. Dapat membina alat dan ada orang yang terus menggunakannya ialah perkara yang berasingan.

Membina telah menjadi lebih pantas berkat AI. Tetapi membuat orang terus menggunakannya memerlukan kerja lain. Menjawab soalan tentang cara menggunakannya (Buku Bantuan wujud untuk ini). Menghantar notis sebelum tempoh percuma tamat. Menerangkan sebab apabila menaikkan harga. Memadam data dengan betul apabila seseorang meminta pembatalan. Dan yang terpenting, memastikan ia terus berjalan tanpa campur tangan pemilik.

Daripada tiga prinsip siri Agenda, "automatik" ialah prinsip untuk "terus menggunakannya" ini. Alat yang tidak berfungsi melainkan pemilik mengendalikannya setiap hari akhirnya akan dibatalkan. Ia tidak siap apabila ia dibina. Ia menjadi perniagaan hanya apabila ia terus digunakan. Menambah, satu demi satu, kedai yang terus menggunakannya: itulah tugas saya selepas menerbitkan buku ini.

#### Jika Anda Mahu Bermula di Kedai Anda Sendiri

Bagi mereka yang membaca buku ini dan mahu mencuba di kedai sendiri, ada tiga langkah.

1. Buka https://bontallc.com/agenda?via=b2-ms-{{FMT}} dan log masuk dengan akaun Google (AgendaID akan dicipta. Tidak perlu mendaftarkan kad)
2. Pertama, tambah satu buku percuma. Saya mengesyorkan Buku Lampu. Anda hanya menampal komponen papan tanda ke dalam laman web anda, dan ia berfungsi dalam 10 minit. Jika anda belum membuka kedai, cuba Buku Untung Rugi
3. Jika ia nampaknya sesuai dengan anda, cuba Buku Kehadiran percuma selama tiga bulan. Notis tiba apabila tarikh akhir menghampiri, jadi anda tidak akan dikenakan bayaran walaupun anda membiarkannya

Jika anda ada soalan, tanya melalui Buku Bantuan (AgendaQA). AI menjawab soalan operasi dengan serta-merta, dan saya sendiri membaca soalan tentang spesifikasi dan pepijat.

Jualan restoran bergantung pada cuaca dan musim. Bilangan tempat duduk dan waktu perniagaan kedua-duanya ada had. Jualan alat, sebaliknya, tiada had tempat duduk. Menjalankan kedai sambil mengagihkan alat yang lahir daripada masalah kedai sendiri, dan membiarkan itu perlahan-lahan menjadi pendapatan: saya percaya ini boleh menjadi satu lagi cara bagi kedai persendirian untuk menjana pendapatan tambahan.

#### Kekal Syarikat Kecil, Mendunia

Ada satu lagi perkara yang saya putuskan tentang siri Agenda sejak awal. Saya tidak akan membinanya dalam bahasa Jepun sahaja.

Buku Kehadiran, Buku Untung Rugi dan Buku Bantuan semuanya boleh digunakan dalam 20 bahasa. Teks skrin dan soalan lazim, semuanya. Alat yang dibina untuk sebuah bar 19 tempat duduk di Tokyo berfungsi dengan cara yang sama dalam bahasa Inggeris, dalam bahasa Korea, dalam bahasa Vietnam.

Ada dua sebab. Satu ialah masalah restoran tidak berubah apabila negara berubah. Anda mahu merekod bila kakitangan datang dan pergi. Anda mahu tahu keuntungan anda sebelum membuka kedai. Anda mahu memberitahu pelanggan bahawa waktu tutup telah dilanjutkan. Ini semua masalah yang dikongsi kedai persendirian di seluruh dunia. Satu lagi ialah bilangan kedai persendirian di Jepun terus menurun. Jika saya hanya melayani pasaran berbahasa Jepun, jualan alat akan mempunyai had.

Pada masa lalu, untuk sebuah syarikat kecil menjual produk ke luar negara, ia memerlukan ejen tempatan, firma terjemahan dan entiti undang-undang. Kini AI membantu terjemahan dan semakan. Sistem pembayaran bersama berfungsi di seluruh dunia. Untuk pengedaran digital anda hanya memerlukan pelayan (server), dan tiada stok atau gudang di setiap negara. Alat yang dibuat seorang pemilik boleh berada di rak seluruh dunia dalam 20 bahasa sehari selepas ia dibuat. Pada masa lalu, hanya syarikat besar yang boleh melakukannya.

Syarikat yang sangat kecil yang berniaga dengan beberapa negara sejak awal: syarikat sedemikian kadangkala dipanggil micro-multinational (syarikat multinasional kecil). Bonta LLC menyasarkan tepat itu, dengan satu kedai di Higashi-Nakano dan seorang pemilik.

Sudah tentu, menterjemah kepada 20 bahasa tidak bermakna pemilik di luar negara akan segera mula menggunakannya. Sebahagian terjemahan masih menunggu semakan oleh penutur asli agar kedengaran semula jadi. Walaupun begitu, dengan menghapuskan halangan bahasa sejak awal, had tentang sejauh mana alat itu boleh sampai lenyap, sebagaimana had tempat duduk.

Bagaimana saya membina asas itu ialah kisah Bab 4.

【Rajah 3-5】Penukaran bahasa dalam Buku Bantuan. 20 bahasa disenaraikan *(Skrin dalam bahasa Jepun.)*

## Bab 4: Teknologi - Sistem untuk Membina Produk Seorang Diri, Secara Berterusan

Perkara utama bab ini

- Saya menjadikan prosedur melancarkan produk baharu sebagai dokumen, dalam bentuk (sebuah skill) yang boleh dibaca dan dilaksanakan oleh AI. Apa yang manusia lakukan hanyalah pertimbangan dan operasi yang hanya manusia boleh buat
- Bahagian bersama, seperti log masuk, pengebilan, halaman pengenalan dan panduan kepada produk lain, dibina sekali dan digunakan semula merentasi semua produk. Kos pangkalan data asas itu ialah kira-kira $35 sebulan
- Sistem ini masih terus dikembangkan. Saya terus menambah pada dokumen prosedur kegagalan, seperti satu reka bentuk ditolak lima kali berturut-turut

(Ini bab dengan banyak istilah teknikal. Jika anda tidak berminat dengan teknologinya, anda boleh melangkau ke Bab 5 dan kisahnya tetap bersambung.)

### 4-1 ProductBootstrap: Menyerahkan Prosedur Pelancaran Itu Sendiri kepada AI

Setiap kali saya membina produk, saya mengulang persediaan yang sama dan kesilapan yang sama. Mencipta repositori (gudang untuk atur cara). Menyambung log masuk. Memutuskan warna reka bentuk. Menyediakan sistem pengujian. Menyediakan persekitaran pengeluaran. Saya pasti telah melakukan semuanya untuk produk sebelumnya, tetapi saya lupa butirannya dan tersandung di tempat yang sama.

Maka saya menjadikan prosedur melancarkan produk baharu sebagai dokumen. Bentuknya yang boleh dibaca dan dilaksanakan oleh AI yang menulis kod (Claude Code) saya panggil sebuah "skill." Nama skill ini ialah ProductBootstrap. "Bootstrap" ialah istilah lazim dalam dunia komputer untuk memulakan diri sendiri daripada mekanisme minimum, dan saya menerapkannya pada pelancaran produk.

Saya tidak menyimpan atur cara templat. Saya menyalin produk terkini yang siap dan memulakan produk baharu daripadanya. Dengan cara itu, pengajaran terbaharu diwarisi secara automatik oleh produk seterusnya. Tidak perlu terus menyelenggara templat lama juga.

#### Aliran Prosedur

1. Serahkan dokumen keperluan. Jika ruangan yang diperlukan (nama produk, apa yang dilakukan, siapa yang menggunakan, harga, unit harga, warna pengenalan, lokasi induk reka bentuk, dan seterusnya) dibiarkan kosong, AI tidak bermula. Peraturannya ialah ia tidak bertanya soalan kepada pemilik di tengah jalan. Jika semuanya tidak lengkap pada permulaan, ia tidak bermula
2. Putuskan warna produk. Setiap produk dalam siri Agenda mempunyai satu warna pengenalan. AI menyemak nilai warna produk sedia ada, mencadangkan kira-kira empat calon yang tidak bertindih, dan pemilik memilih
3. Tetapkan reka bentuk. Saya meminta AI reka bentuk (Claude Design) mencipta cadangan untuk skrin. AI menjalankan semakan kendirinya sehingga tiga pusingan, dan hanya cadangan yang lulus semakan ditunjukkan kepada pemilik
4. Serahkan pelaksanaan kepada AI sehingga habis. AI membina dan membetulkan sendiri sehingga memenuhi syarat penerimaan yang ditetapkan (semakan jenis, semakan gaya, semua ujian hijau, lulus setiap semakan skrin, dan perubahan pangkalan data berjalan dengan lancar dalam persekitaran ujian)
5. Pemilik hanya memberi kelulusan apabila hendak melancarkannya ke pengeluaran. Semuanya sehingga persekitaran ujian berjalan tanpa pengawasan, dan pemilik menilai hanya operasi pengeluaran

Saya membina peringkat pelaksanaan supaya ia tidak berhenti di tengah jalan untuk menunggu kelulusan pemilik. Pada hari-hari awal, saya meneruskan dengan meminta kelulusan pada setiap peringkat, tetapi tiada apa yang bergerak ke hadapan dengan cara itu. Apabila terdapat beberapa tetingkap kerja AI, setiap satu berhenti menunggu kelulusan, dan pemilik perlu berpindah-pindah antara setiap tetingkap membuat pertimbangan. Maka saya mengubahnya: saya menyerahkan lebih awal julat yang sudah diluluskan dan syarat penerimaan yang boleh dinilai mesin, dan ia berhenti hanya apabila gagal.

Syarat berhenti juga ditetapkan. Apabila dokumen prosedur dan keputusan pemilik bercanggah. Apabila operasi yang hanya manusia boleh buat diperlukan. Apabila ia gagal maju pada ralat yang sama tiga kali berturut-turut. Apabila pengesahan tamat, kebenaran tidak mencukupi, atau operasi yang tidak boleh diundurkan diperlukan. Selain itu, AI meneruskan sendiri. Keadaan kerja direkodkan dalam fail kecil, jadi walaupun proses terhenti di tengah jalan, ia boleh disambung semula dari situ.

#### Manusia Hanya Melakukan Dua Perkara

Saya menulis ini dalam dokumen prosedur: AI melaksanakan setiap langkah. Pemilik boleh diminta hanya dua perkara berikut.

- Pertimbangan itu sendiri. Meluluskan, memutuskan, menentukan yang mana satu daripada dua pilihan
- Operasi yang hanya manusia boleh lakukan. Kunci yang hanya boleh dikeluarkan daripada skrin pentadbir perkhidmatan luar, permohonan yang melibatkan pengesahan identiti, operasi pada peranti sebenar dan penilaian visual

Jika AI menyerahkan apa-apa selain itu kepada pemilik, itu pelanggaran dokumen prosedur. Dalam jadual prosedur, saya menambah ruangan "pelaksana" pada setiap baris, dan mana-mana baris yang entri pemiliknya tidak dapat menyatakan sebab akan ditukar ke pihak AI.

Saya mempunyai sebab untuk membuat peraturan ini. Apabila saya mengemas kerja yang tinggal bagi satu produk, AI menyenaraikan "cipta projek pelayan," "daftarkan destinasi log masuk," "masukkan pemboleh ubah persekitaran," dan "bina persekitaran ujian," semuanya sebagai tugas pemilik. Setiap satu ialah operasi yang AI boleh laksanakan sendiri. "Mengapa saya yang melakukan ini?" ialah reaksi jujur saya ketika itu. AI melakukannya sendiri jika anda memintanya. Tetapi jika anda tidak meminta, ia menyerahkannya kepada manusia. Itulah sebabnya saya perlu menulisnya ke dalam dokumen prosedur.

Setiap kegagalan sistem tempahan yang saya terangkan dalam Bab 2 saya masukkan ke dalam senarai semak dokumen prosedur ini. Tulis ujian dahulu. Jangan simpan data pengeluaran dalam persekitaran pembangunan. Bina persekitaran ujian dahulu. Produk seterusnya mengelak kesilapan pahit yang sama sejak awal.

#### Masih Berkembang

Dokumen prosedur ini bukan produk yang sudah siap. Ia sesuatu yang terus saya tambah setiap kali sesuatu gagal.

Contohnya, pernah ada masa saya meminta AI reka bentuk mencipta skrin untuk satu produk lima kali berturut-turut, dan kesemua lima ditolak. Itu termasuk pusingan di mana saya menyerahkan peraturan reka bentuk seluruh siri (DESIGN.md).

Pada mulanya, AI mendiagnosis puncanya sebagai "skema warna itu sendiri." Saya menafikannya. Punca sebenar ada dua. Satu ialah warna yang tiada takrifan dalam peraturan digunakan sesuka hati. Satu lagi ialah tiga bahagian dengan peranan berbeza disusun menegak dengan warna latar yang sama dan jidar yang sama, tanpa sempadan antaranya. Tiada peraturan dilanggar, namun peranan telah hilang daripada rupa.

Maka saya menambah fasal pada peraturan reka bentuk. Jangan beri rupa yang sama kepada perkara yang berbeza peranannya. Jangan pisahkannya dengan warna sahaja. Elemen yang paling penting menjadi tumpuan pandangan yang pertama. Hanya perkara yang benar-benar setara boleh disusun dengan berat yang sama. Jangan buat susun atur yang sekadar menimbun secara menegak.

Ada satu lagi pengajaran daripada kegagalan. Jika anda menyampaikan "rupa lalai yang perlu dielakkan" hanya sebagai senarai larangan, AI berayun sepenuhnya ke lalai lain yang tiada dalam senarai. Apabila saya melarang kad, bayang dan sudut bulat serentak, yang kembali ialah skrin seperti akhbar yang dibuat daripada garisan dan jidar semata-mata. Sejak itu, saya meminta bahan permintaan ditulis dalam tiga lajur: "corak yang perlu dielakkan," "apa yang saya mahu larang," dan "apa yang perlu dilakukan sebagai ganti."

Saya juga mengubah cara saya memutuskan warna pengenalan di tengah jalan. Ketika produk melebihi lapan, jalur warna gelap telah diisi oleh produk sedia ada, dan produk kesembilan dan seterusnya tidak lagi dapat warna gelap untuk garisan dan butang tanpa berlanggar dengan yang sedia ada. Maka saya menyemak peraturan: warna pengenalan produk hanya digunakan untuk warna permukaan yang cerah, dan garisan, jidar, ikon dan butang utama semuanya diseragamkan dalam warna dakwat gelap bersama siri. Ia kekangan yang menjadi jelas hanya setelah produk bertambah.

Setiap kali sesuatu gagal, saya membetulkan dokumen prosedur. Produk seterusnya menjadi lebih mudah sebanyak itu. Saya percaya mengembangkan dokumen prosedur ialah pelaburan terbaik untuk terus membina produk seorang diri.

【Rajah 4-2】Peringkat prosedur pelancaran, dan siapa yang melaksanakannya (AI atau pemilik) *(Skrin dalam bahasa Jepun.)*

【Rajah 4-3】Warna pengenalan siri Agenda. Satu warna bagi setiap produk, digunakan hanya pada permukaan *(Skrin dalam bahasa Jepun.)*

### 4-2 AgendaHub: Pintu Depan

Apabila produk bertambah, anda akhirnya membina perkara yang sama berulang kali. Log masuk, pengebilan, halaman pengenalan, panduan kepada produk lain. Untuk menjalankan ini seorang diri, anda perlu membina bahagian bersama sekali dan menggunakannya semula merentasi semua produk.

AgendaHub ialah tempat bahagian bersama itu dihimpunkan. Saya memanggilnya "pintu depan."

Pertama, ia pintu masuk yang menghalakan daripada satu alamat ke setiap produk. Di bawah satu domain, bontallc.com, pintu masuk bagi setiap produk tersusun: /agendatimbro, /agendaoro, /agendaluce. Kepada pelanggan ia kelihatan seolah-olah produk berada di dalam satu laman, tetapi sebenarnya atur cara yang berasingan berjalan di belakang setiap satu.

Seterusnya, ia tempat halaman pengenalan produk diletakkan. Terdapat satu halaman pengenalan untuk siri ini, dan di dalamnya satu bahagian bagi setiap produk. Setiap bahagian memuatkan nama produk dan gelarannya, harga, satu masalah yang dinyatakan dalam kata-kata pemilik sendiri bermula dengan "Apabila anda...," penerangan tentang apa yang boleh dilakukannya, dan pautan ke halaman butiran. Apabila saya melancarkan produk baharu, menambah bahagian ini termasuk dalam prosedur pelancaran.

Ia juga menjadi pusat rujukan bagi peraturan reka bentuk dan prosedur pelancaran. Induk warna pengenalan, peraturan skrin (DESIGN.md), skill ProductBootstrap yang saya terangkan dalam 4-1, skill yang menyemak skrin, dan skill yang membuat perubahan pangkalan data dengan selamat. Bagi setiap peraturan yang merentasi siri, kandungan sebenar berada di sini, dan setiap produk membacanya melalui rujukan.

【Rajah 4-1】Struktur siri Agenda. Daripada pintu depan (AgendaHub) ke setiap buku, dan setiap buku bersambung kepada satu akaun (AgendaID) *(Skrin dalam bahasa Jepun.)*

### 4-3 AgendaID: Akaun Bersama dan Pengebilan

AgendaID ialah sistem bersama siri ini untuk akaun dan pengebilan.

Pemilik yang log masuk sekali dengan akaun Google boleh menggunakan setiap produk. Tidak perlu mencipta akaun bagi setiap produk. Saya juga merancang untuk akhirnya membawa tetapan bahasa merentasi produk.

Pengebilan juga satu sistem. Daripada membina sambungan kepada perkhidmatan pembayaran (Stripe) bagi setiap produk, AgendaID menanggung semuanya. Terdapat empat kategori harga: produk ringan pada ¥300 (kira-kira $2) sebulan, produk bayar ikut guna, produk pembelian sekali pada ¥600 (kira-kira $4), dan produk percuma. Produk berbayar mempunyai tempoh percuma tiga bulan tanpa pendaftaran kad, boleh digunakan sekali bagi setiap gabungan kedai dan produk. Terdapat juga mekanisme yang menambah tempoh percuma tiga bulan kepada perujuk dan orang yang dirujuk.

Sebelum tempoh percuma tamat, e-mel pemberitahuan tiba tujuh hari dan satu hari lebih awal. Pada mulanya saya membina e-mel ini di dalam Buku Kehadiran juga, tetapi apabila produk bertambah saya sedar membazir memberi setiap produk mekanisme yang sama, maka saya menyatukannya di pihak AgendaID.

#### Menyeragamkan Peraturan Pembatalan dan Pemadaman Data

Ada bahagian yang biasa tetapi penting: pembatalan dan pemadaman data.

Apabila pelanggan membatalkan, data mana yang dipadam, dan bila? Jika anda membinanya secara berasingan bagi setiap produk, sesuatu pasti terlepas di suatu tempat. Lebih-lebih lagi, siri Agenda termasuk produk yang mengendalikan data yang amat sensitif, seperti yang mengenal pasti pelanggan tetap melalui pengecaman wajah.

Maka saya membahagikan butiran pemadaman kepada empat peringkat dan menjadikannya peraturan bersama merentasi siri. Ia ialah membatalkan produk, memadam kedai, menamatkan akaun (meninggalkan seluruh siri), dan permintaan pemadaman daripada seorang kakitangan individu. Peringkat atas mengalir ke peringkat bawah, dan setiap produk mendaftarkan prosedur pemadaman datanya sendiri dengan sistem bersama. Tempoh tangguh pemadaman ialah 30 hari, dan dalam tempoh itu data itu boleh dipulihkan semula.

Satu paksi masa datang bersama ini. Rekod kehadiran, contohnya, dikehendaki oleh undang-undang untuk disimpan selama lima tahun. Walaupun bekas kakitangan meminta pemadaman, dalam tempoh pengekalan rekod mesti disimpan, dengan nama dan seumpamanya dijadikan tanpa nama, bukannya dihapuskan secara fizikal. Saya perlu memutuskan garis antara "padam" dan "simpan" dengan menyemaknya berbanding undang-undang.

#### Log Masuk Ujian untuk Menghalang AI Mencemari Pengeluaran

Saya menambah satu lagi mekanisme pada AgendaID, untuk AI: pintu masuk log masuk ujian.

Untuk meminta AI menyemak bahawa sesuatu berfungsi, AI perlu log masuk dan mengendalikan skrin. Tetapi log masuk dilakukan dengan akaun Google, jadi AI tidak boleh log masuk sendiri. Dan saya juga tidak boleh menyerahkan akaun pemilik kepada AI. Ada bahaya ujian AI akan mencemari data pengeluaran.

Maka saya membina pintu masuk yang mengeluarkan akaun sintetik (persona) yang hanya boleh digunakan dalam persekitaran ujian. Ia tidak berfungsi di pengeluaran. Pangkalan data persekitaran ujian ialah projek berasingan daripada pengeluaran dan hanya mengandungi data sintetik. AI log masuk melalui pintu masuk ini, mengendalikan skrin, dan mengesahkan bahawa sesuatu berfungsi. Akaun ujian dibina semula setiap hari, dan yang lama dipadam.

Dengan ini, AI boleh melaksanakan malah semakan akhir sendiri, dalam persekitaran yang dibina persis seperti pengeluaran, tanpa menyentuh pengeluaran.

### 4-4 Navigasi Bersama, dan Kegagalan Perkataan "Pintu Depan"

Supaya pengguna boleh pergi dari mana-mana produk ke yang lain, saya memberi setiap produk menu navigasi bersama. Ia laluan yang membolehkan pemilik bar yang menggunakan Buku Kehadiran bertanya soalan dalam Buku Bantuan, atau pergi melihat buku-buku lain.

Di sebalik navigasi bersama ini ada kisah kegagalan kecil.

Dalam versi pertama, saya telah meletakkan pautan yang berbunyi "Kembali ke pintu depan." Itu kerana, secara dalaman, saya memanggil AgendaHub "pintu depan." Tetapi apabila saya menyemak pada peranti sebenar, ada sesuatu yang tidak kena. Dua pautan, "Kembali ke pintu depan" dan "Lihat siri Agenda," menghala ke tempat yang sama. Selain itu, pautan sokongan berada di atas menu kerja harian, jadi urutan kepentingan terbalik. Dan yang paling utama, perkataan "pintu depan" tidak bermakna apa-apa kepada pemilik yang menggunakan produk buat kali pertama. Ia bahasa dalaman pembuat sendiri.

Maka saya menetapkan semula prinsip. Susun item mengikut seberapa dekat ia dengan tujuan pengguna: kerja harian di paling atas, pautan yang menuju ke luar di paling bawah. Walaupun ia pautan untuk menarik pengguna baharu, ia sekali-kali tidak boleh diletakkan di atas menu kerja harian. Sempadan mesti boleh diterangkan dengan satu baris. Tulis kata-kata dalam bahasa pengguna, bukan bahasa dalaman. Jangan sekali-kali letakkan lebih daripada satu pautan yang menghala ke tempat yang sama. Saya membuang "Kembali ke pintu depan" dan menggabungkan semuanya menjadi satu pautan, "Lihat buku-buku Agenda yang lain."

Dalam Bab 2, saya menulis tentang mempelajari istilah UI. Itu bahasa untuk pemilik gunakan apabila bercakap dengan AI. Ini sebaliknya: bahasa yang pembuat gunakan untuk bercakap dengan pengguna. Dalam kedua-dua kes, ia soal menyesuaikan kata-kata anda dengan orang yang anda bercakap dengannya.

【Rajah 4-4】Navigasi bersama selepas pembetulan. Kerja di atas, dan pautan yang menuju ke luar di paling bawah *(Skrin dalam bahasa Jepun.)*

### 4-5 Asas Itu Berharga $35 Sebulan

Kos pangkalan data bagi keseluruhan asas yang diterangkan dalam bab ini ialah kira-kira $35 sebulan. Pelan berbayar yang merangkumi projek pengeluaran ialah $25, dan projek untuk persekitaran ujian ialah $10.

Ini juga bukan jumlah dari awal. Pada satu ketika saya membayar $45 sebulan. Pangkalan data pembangunan untuk produk pengecaman wajah masih dibilkan walaupun saya tidak menggunakannya. Saya memindahkannya ke peringkat percuma dan menghentikannya, memadam projek lain yang tidak saya gunakan, dan begitulah ia sampai ke jumlah sekarang.

Saya juga memerhatikan kos AI. Kerja AI yang menulis atur cara dibilkan mengikut jumlah token (unit teks yang dibaca dan ditulis AI). Saya mengelak menumpukan kos dengan meminta tetingkap kerja berpegang pada peranan penyelaras dan menyerahkan pelaksanaan itu sendiri kepada AI lain dengan peruntukan kos berasingan. Untuk model generatif dalam tetingkap sembang juga, saya melihat harga dan memilih yang perlu dan mencukupi. Walaupun model peringkat lebih tinggi hanya berharga $1 lebih sebulan, saya memilih dengan bertanya "adakah ini cukup?"

Jika anda membina kecil, jualan kecil pun boleh menampung anda. Kisah pengewangan dalam Bab 3 disokong oleh kecilnya kos asas ini.

### 4-6 AI Penyelaras, dan Orang yang Membuat Keputusan

Akhir sekali, izinkan saya menerangkan bentuk hari kerja saya.

Saya membuka beberapa tetingkap kerja AI pada masa yang sama. Ada tetingkap untuk sistem tempahan, tetingkap bagi setiap produk, dan tetingkap penyelaras yang menghantar arahan kepada mereka dan mengumpulkan hasilnya. Saya menamakan tetingkap penyelaras itu AgendaRegia (buku penyelaras).

Yang membuat keputusan, iaitu memutuskan "hala mana yang hendak dituju," ialah saya dan AI di pihak sembang. AI di pihak sembang mencari jurang dan percanggahan dalam spesifikasi lebih awal, melampirkan keputusan lalai pada setiap satu, dan mencadangkan semuanya sekali gus. Saya membacanya dan memutuskan. Apa yang diputuskan dihimpunkan dalam helaian arahan yang dipanggil Goal dan ditampal ke dalam tetingkap kerja. Ia termasuk kelulusan awal dan syarat lulus yang boleh dinilai mesin. Tetingkap kerja membacanya dan meneruskan hingga akhir, berhenti hanya apabila sesuatu gagal.

Saya juga meminta helaian arahan memasukkan anggaran bila kerja akan siap. Saya menyelitkan kerja ini di antara waktu buka bar, jadi jika saya tidak tahu berapa lama sesuatu akan mengambil masa, saya tidak dapat merancang hari saya.

Peranan pemilik bukan membaca tetapi memutuskan. Saya tidak perlu membaca kesemua 1,775 log perbualan. Saya menjawab soalan tentang fakta bar. Saya membuat keputusan tentang perkara yang hanya boleh diputuskan oleh dasar bar. Selepas sesuatu dilancarkan, saya sendiri mencuba dan mengendalikannya lima atau enam kali untuk menyemak sama ada ada yang terasa tidak kena. Itu sahaja.

Sebelum sampai ke bentuk ini, saya mengulang kerja berkali-kali. AI menambah ciri sendiri dan skrin menjadi tidak stabil. Kerja membesar tanpa had daripada satu arahan. Menunggu kelulusan pada setiap peringkat bermakna tiada apa yang bergerak ke hadapan. Setiap kali, saya menambah satu peraturan, dan begitulah ia sampai ke bentuknya sekarang. Ini juga masih berkembang.

#### Apa yang Boleh Anda Bawa Pulang daripada Bab Ini

- Untuk kerja yang berulang, jadikan prosedur itu sendiri sebagai dokumen dan serahkan kepada AI. Jika anda membetulkan dokumen prosedur setiap kali ia gagal, kali berikutnya menjadi lebih mudah
- Bina bahagian bersama (log masuk, pengebilan, navigasi) sekali sahaja dan gunakan semula merentasi semua produk. Jika asasnya kecil, jualan kecil pun boleh menampung anda
- Manusia hanya melakukan pertimbangan dan operasi yang hanya manusia boleh buat. Jika AI menyerahkan apa-apa selain itu kepada anda, tambahkannya ke dalam dokumen prosedur

Sambungan bab ini (buku-buku seterusnya yang saya bina, dan pengajaran yang saya tambah pada dokumen prosedur) ada di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Bab 5: Masa Depan Sebuah Bar Kecil

### 5-1 Daripada Zatta Gohan kepada Tamuro

Saya memasuki perniagaan makanan dan minuman pada usia 39 tahun.

Pencetusnya ialah sebuah bar kejiranan bernama Zatta. Sebulan sekali, kadangkala setiap dua minggu, mereka membenarkan saya menghidangkan makanan di sana. Saya telah belajar memasak sendiri sejak lama, tetapi ketika itu saya mempunyai tempat di mana orang makan masakan saya dan berasa gembira. Itulah pengalaman asal saya.

Pada 2014, saya membuka restoran bernama Zatta Gohan di Arai-Yakushi. Ia tempat kecil yang menghidangkan makanan set. Saya menjalankannya selama tujuh tahun.

Namun di Arai-Yakushi, saya merasakan had pada bilangan pelanggan. Kemudian saya menemui sebuah premis di Higashi-Nakano. Berjalan kaki dari pintu timur stesen mengambil masa kurang dari seminit. Malah pada hari hujan, anda boleh sampai ke sana tanpa terlalu basah.

Pada November 2018, saya membuka Tamuro di sana. "Tamuro" bermaksud tempat orang berkumpul. Ia mempunyai 11 tempat duduk di kaunter dan 8 tempat duduk tatami, 19 kesemuanya. Selama tiga tahun saya menjalankan dua tempat serentak, Arai-Yakushi dan Higashi-Nakano. Semasa tempoh COVID, mengekalkan kedua-duanya menjadi sukar, jadi saya menutup kedai Arai-Yakushi dan menumpukan perhatian pada Tamuro sahaja.

#### Bar Kurasi

Tamuro menggelar dirinya "bar kurasi."

Kurasi bermaksud mempunyai mata yang tajam. Sebelum menjadi tukang masak, saya mahu menjadi kurator. Makanan, minuman, suasana bar: saya membuat semuanya dengan memilih menggunakan mata yang tajam. Itulah Tamuro.

Saya kerap mengembara untuk makan, di luar negara dan di Jepun. Vietnam, Kemboja, Itali, Shanghai, Beijing, Mexico. Makan sambil mengembara ialah keseronokan, dan pada masa yang sama ia cara mencari apa yang hendak dihidangkan di Tamuro. Saya mencipta semula bahan yang mahal dengan bahan yang mudah didapati. Contohnya, jika anda mengeringkan kuning telur dan memarutnya, anda mendapat rasa yang hampir dengan bottarga. Saya menganggap penggantian seperti ini (penyetempatan) sebagai peranan saya.

Saya belajar memasak semula semasa tempoh COVID. Saya mengambil kursus masakan Perancis sebanyak lapan sesi, dan saya juga menghadiri kursus masakan Jepun. Cara mengendalikan umami, dan cara memasak dengan haba. Apa yang saya pelajari di sana ialah asas masakan saya hari ini.

Menu Tamuro dibina daripada empat pembuka selera dan satu hidangan utama. Saya memberikannya pelbagai bahan supaya pelanggan yang tinggal sendirian dapat mengambil banyak sayur. Saya menyusunnya supaya kaedah memasak (goreng, bercuka, rebus, bakar) dan perisa (manis, pedas, masam) tidak bertindih. Hidangan paling popular ialah tonteki, stik babi. Ia mempunyai sos yang sedikit manis dibuat dengan kicap Kyushu, dengan banyak bawang putih.

#### Tempat Orang Berkumpul

Kira-kira separuh pelanggan Tamuro datang sendirian. Mereka kebanyakannya berumur 30-an hingga 50-an, dan ramai ialah jiran dari Higashi-Nakano, tetapi orang juga datang dari sekitar Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo dan Eifukucho.

Ciri istimewa bar ini ialah betapa banyak pelanggan berbual sesama sendiri. Saya membina kaunter supaya mudah bercakap dengan orang di sebelah, dan saya atau kakitangan menentukan tempat duduk dengan menilai siapa yang akan serasi. Pelanggan yang datang sendirian kadangkala kembali bersama-sama kemudian. Seperti yang dikatakan oleh namanya, ia telah menjadi tempat orang berkumpul. Saya berkongsi suasana hari-hari bar di [Instagram](https://www.instagram.com/tamuro.higashinakano/).

Dalam hidangan berbilang sajian yang diadakan kira-kira sekali sebulan, saya menghidangkan tujuh hingga lapan hidangan dalam dua hingga tiga jam, bersama padanan wain. Setiap bulan temanya berubah: Itali, Perancis, Jepun. Kelas memasak ialah bengkel tiga jam, dan selepas memasak, semua orang bersulang, makan dan pulang. Ada aperitivo, menghidangkan wain dan hidangan kecil pada awal petang sebelum buka. Ada barbeku kira-kira dua kali setahun. Ada majlis hujung tahun sekali setahun. Dan ada festival yukata yang saya tulis dalam Bab 1.

Sistem tempahan yang saya tulis dalam Bab 1, tetingkap sembang, dan MCP semuanya alat untuk membawa orang ke bar ini. AI ialah cara untuk mengumpulkan orang, bukan matlamat.

### 5-2 Kari Hamburg Quatre Épices

Tamuro ialah bar waktu malam. Pada siang hari, ruang itu kosong.

Menggunakan waktu itu, saya memulakan Quatre Épices pada Januari 2024. Ia kedai kari hamburg yang beroperasi hanya pada waktu makan tengah hari di tempat yang sama, dan dijalankan oleh kakitangan.

Quatre Épices bermaksud "empat rempah" dalam bahasa Perancis. Sesuai dengan namanya, daripada melapiskan banyak rempah, kami memilih dan menyempitkannya supaya garis besar rasa jelas. Kari itu tidak menggunakan tepung; ia disiapkan dengan kepekatan semula jadi sayur dan daging itu sendiri. Kepuasan apabila selesai makan, dan tiada rasa berat di perut. Dan keharmonian dengan hamburg. Saya mereka bentuknya berlandaskan tiga prinsip itu.

Kami amat menitikberatkan cara hamburg dimasak. Kami menetapkan campuran supaya ia keluar rangup di luar dan gebu di dalam, dan kami memasak sesuai dengan campuran itu. Cara memasak dengan haba yang saya pelajari pada waktu malam di Tamuro turut menjadi asas hidangan siang hari.

Harga, hari perniagaan dan waktu boleh berubah, jadi sila semak Instagram Tamuro (https://www.instagram.com/tamuro.higashinakano/) untuk maklumat terkini.

Quatre Épices turut menjalankan dapur komuniti kanak-kanak (kodomo shokudo) di tempat yang sama. Ia aktiviti yang menggunakan kemudahan dan saluran pembelian bahan bar sedia ada untuk menghidangkan makanan kepada kanak-kanak di kawasan kejiranan. Melalui hubungan itu, kami juga membina hubungan dengan dewan komuniti setempat. Kami kadangkala menghidangkan kari dan sandwic di acara sukan tempatan, acara dewan komuniti dan festival tarian Bon.

Sejujurnya, menggunakan waktu siang tidak semuanya berjalan lancar. Saya mencipta hari minum siang hari dan menyewakan ruang kepada orang lain, tetapi pelanggan tidak datang seperti yang saya harapkan. Daya tarikan bar tersampai secara berbeza apabila pemilik ada pada waktu malam dan apabila hanya kakitangan siang hari ada. Mengembangkan kedai siang hari dengan daya tarikan yang berbeza daripada kedai malam masih tugas yang belum siap.

### 5-3 Bonta LLC: Dua Tonggak

Syarikat kecil yang menjalankan Tamuro dan Quatre Épices ialah Bonta LLC. Saya ahli pengurus syarikat itu.

Syarikat ini mempunyai dua tonggak. Satu ialah makanan dan minuman: Tamuro dan Quatre Épices. Satu lagi ialah IT: pembangunan siri Agenda, dan perundingan.

Makanan dan minuman serta alat berbeza dalam cara menjana pendapatan. Menyokong syarikat dengan dua tonggak yang berbeza sifat ialah bentuk yang saya fikirkan.

Dan kedua-dua tonggak membekalkan bahan antara satu sama lain. Masalah di bar menjadi benih sesuatu alat. Apa yang saya pelajari daripada membina alat kembali ke dalam menjalankan bar. Buku Lampu lahir daripada waktu tutup yang lewat, dan rekod waktu dilanjutkan daripada Buku Lampu menjadi asas anggaran keuntungan dan syif. "Soalan yang tidak dapat kami jawab" yang bertimbun dalam tetingkap sembang memperbaik panduan bar. Kitaran ini ialah sebab saya boleh menguruskan kedua-dua bar dan pembangunan seorang diri.

Saya tidak berfikir untuk membesarkan syarikat. Kecil, banyak, dan murah. Itulah bentuk syarikat ini.

### 5-4 Menulis sebagai Raku Bonta

Apabila saya menulis dan menerbitkan, saya menggunakan nama pena "Raku Bonta." Saya menulis buku ini dengan nama itu juga.

Buku saya sebelum ini, *Penolong Pengurus AI*, ialah buku tentang AI generatif. Ia menduduki tempat nombor satu dalam kategori pengurusan masa Amazon dan dibaca ramai orang. Buku ini sekuelnya.

Selain buku, saya juga menulis di note. Saya menulis tentang usaha bar dengan AI, apa yang saya temui dalam lawatan latihan, kemajuan penerbitan buku saya, dan siri Agenda. Anda boleh mengikuti sambungan yang tidak dapat saya muatkan dalam buku ini di note (https://note.com/bontallc).

Bagi saya, menulis juga cara untuk meletakkan kedua-dua bar dan pembangunan dalam kata-kata dan menyemaknya. Seperti yang saya tulis dalam Bab 1, pengetahuan pertama tetingkap sembang "T-AI-MURO" dibina daripada kata-kata yang saya tinggalkan di X. Apa yang saya tulis menjadi bahan untuk AI. Mulai sekarang juga, apa yang saya tulis akan kembali kepada kedua-dua bar dan AI.

Ada satu lagi perkara yang saya putuskan tentang menulis. Saya tidak mengumumkan perkara yang belum siap dengan "akan datang." Saya menyiapkannya, membuat halaman pengenalan, dan barulah mengeluarkannya. Saya percaya mengekalkan urutan itu ialah apa yang meraih kepercayaan bagi sebuah syarikat kecil.

### 5-5 Masa Depan Kedai Persendirian

Akhir sekali, saya akan menghimpunkan apa yang telah saya tulis dalam buku ini menjadi satu gambaran.

【Rajah 5-1】Gambaran besar apa yang diterangkan buku ini. Sebuah bar kecil membuka tetingkapnya sendiri (kisah pertama), dan menjadikan masalahnya alat untuk diberikan kepada bar lain (kisah kedua) *(Skrin dalam bahasa Jepun.)*

Pelanggan akan meminta AI mereka sendiri mencari bar dan membuat tempahan. Pada Ogos 2026, menjadi mungkin untuk menempah restoran daripada ChatGPT melalui perkhidmatan tempahan utama. Pintu masuk beralih daripada carian dan laman ulasan makanan kepada AI setiap orang sendiri.

Pada ketika itu, bar yang tidak tersenarai pada perkhidmatan tempahan utama tidak kelihatan oleh AI. Tetapi walaupun anda tidak berada pada perkhidmatan utama, ada jalan untuk sebuah bar menyambung terus kepada AI. Tamuro memilih jalan itu dengan membuka tetingkap bernama MCP. Sebuah bar kecil membuka tetingkapnya sendiri secara bersendirian. Itulah kisah pertama buku ini.

Pemilik bar akan dapat menjadikan masalah mereka sendiri alat dan mengagihkannya kepada bar lain. Buku Lampu lahir daripada masalah Tamuro yang mahu memberitahu orang bahawa waktu tutup akan lewat, dan ia boleh digunakan di mana-mana bar. Kuasa untuk membina menjadi sesuatu yang tidak lagi hanya untuk orang atau syarikat tertentu. Pemilik bar kecil beralih daripada pihak yang menggunakan alat kepada pihak yang membina dan mengagihkannya. Itulah kisah kedua buku ini.

Apa yang dikongsi oleh kedua-duanya ialah semakin kecil sesebuah bar, semakin kuat karakternya boleh menjadi.

Rangkaian besar menyeragamkan sistem mereka supaya setiap cawangan menyampaikan mutu yang sama. Tamuro sebaliknya. Pelanggan solo membentuk separuh, hampir 90% tempahan dibuat pada hari yang sama, dan pelanggan berbual sesama sendiri. Untuk menepati sifat Tamuro itu, saya telah membina sistem tempahan, diskaun dan tetingkap sembang dengan terperinci. Kerana ia tidak diseragamkan, ia berkarakter kuat. Kerana berkarakter kuat, ia menjadi sebab pelanggan memilihnya.

Dan semakin kuat karakter sebuah bar, semakin banyak benih alat yang ditemuinya. Semakin anda menghadapi sifat bar, semakin spesifik masalah anda. Masalah yang spesifik menjadi alat yang spesifik. Alat yang spesifik membantu bar lain yang mempunyai masalah yang sama.

AI telah membolehkan seorang pemilik melakukan kedua-duanya. Mengukuhkan karakter bar, dan mengagihkan alat. Dahulu, anda perlu memilih salah satu. Kini anda boleh melakukan kedua-duanya.

Sudah tentu, ia masih kerja dalam proses. Kadar lulus tetingkap sembang masih dinaikkan. Dokumen prosedur ditambah pada setiap kegagalan. Cara mengembangkan kedai siang hari kekal sebagai cabaran. Orang yang menempah melalui AI masih tidak ramai.

Walaupun begitu, saya percaya masa depan bar kecil cerah. Menjadi kecil bukan kelemahan. Kerana kecil, kita boleh menguji dengan pantas, membuang dengan pantas dan membetulkan dengan pantas. Kerana kecil, kita boleh menjadi berkarakter kuat. Dan masalah sebuah bar yang berkarakter kuat menjadi alat dan diturunkan kepada bar kecil lain.

Saya menulis buku ini dari sebuah bar 19 tempat duduk di Higashi-Nakano.

## Penutup

Terima kasih kerana membaca sehingga ke sini.

Apa yang saya tulis dalam buku ini ialah rekod setakat Oktober 2026. Alat AI berubah bentuk dalam masa beberapa bulan. Sebahagian mekanisme yang saya terangkan mungkin sudah mengambil bentuk lain apabila buku ini diterbitkan. Walaupun begitu, saya menuliskannya, dengan keyakinan bahawa rekod tentang apa yang dibina sebuah bar kecil dengan AI dan bagaimana, di mana ia gagal dan apa yang dipelajarinya, harus kekal berguna untuk beberapa ketika.

Siri Agenda: https://bontallc.com/agenda?via=b2-ms-{{FMT}}

Ikuti aktiviti saya: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Jika anda ke Higashi-Nakano, singgahlah ke Tamuro. Anda boleh menempah melalui laman tempahan, melalui tetingkap sembang "T-AI-MURO" di laman itu, dan tentu sekali melalui AI anda sendiri.

Laman tempahan Tamuro: https://tamuroreservation.vercel.app/?src=b2-ms-{{FMT}}

Instagram Tamuro: https://www.instagram.com/tamuro.higashinakano/

Bagi yang ingin mencuba menempah melalui AI. Alamat sambungan pelayan MCP Tamuro ialah URL berikut.

https://tamuroreservation.vercel.app/api/mcp

Dalam tetapan AI anda (seperti Claude atau ChatGPT), buka skrin untuk menambah alat luar (penyambung, pelayan MCP) dan daftarkan URL ini. Cara mendaftar berbeza mengikut AI dan berubah mengikut masa, jadi cara terbaik ialah mencari "MCP" atau "penyambung" dalam bantuan setiap AI. Bergantung pada pelan yang anda miliki, anda mungkin tidak dapat menyambung pelayan MCP pilihan anda sendiri. Setelah didaftarkan, tanya AI anda, "Tamuro ada tempat kosong malam ini?" Ia akan menyemak slot kosong dan harga serta membimbing anda ke halaman tempahan. Anda sendiri yang menekan butang pengesahan.

Bagi yang datang selepas membaca buku ini. Semasa menempah, sila masukkan kod kupon "BOOK." Kami akan menghidangkan satu minuman percuma untuk pusingan pertama anda. Jika anda datang tanpa tempahan, cukup katakan "Saya baca bukunya" semasa membuat pesanan pertama. Kami akan menghidangkan minuman yang sama. Ia helah kecil yang membolehkan saya mengira berapa ramai orang yang datang kerana buku ini.

Anda boleh masuk tanpa tempahan. Walaupun seorang diri, anda tidak akan berasa kekok. Malah, anda mungkin berbual rancak dengan orang di sebelah.

Saya menunggu anda di kedai tempat orang berkumpul ini.

Raku Bonta

### Rujukan

- OpenAI Help Center, "ChatGPT — Release Notes," 10 Ogos 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (contoh pelayan MCP di AS yang membolehkan AI membuat pesanan untuk saham dan sekuriti lain) https://docs.alpaca.markets/docs/alpaca-mcp-server
- Perdebatan "kematian SaaS": kenyataan Satya Nadella dalam podcast BG2 (Disember 2024), kejatuhan mendadak saham perisian pada Februari 2026 dan apa yang ia dinamakan, serta sanggahan Jensen Huang diambil daripada laporan dan ulasan berikut. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
