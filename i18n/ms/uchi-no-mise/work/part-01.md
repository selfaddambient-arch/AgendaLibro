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
