# Dibuat untuk Bar Kami

Catatan pemilik bar 19 kursi yang membangun sendiri sistem reservasi hingga berbagai alat dengan AI

Raku Bonta

Seri Agenda: https://bontallc.com/agenda?via=b2-id-{{FMT}}

Instagram Tamuro: https://www.instagram.com/tamuro.higashinakano/

Situs reservasi Tamuro: https://tamuroreservation.vercel.app/?src=b2-id-{{FMT}}

## Pendahuluan

Buku ini adalah catatan apa adanya tentang bagaimana pemilik sebuah bar 19 kursi di Higashi-Nakano *(kawasan permukiman di Tokyo bagian barat, tepat di sebelah barat Shinjuku)*, Tokyo, menjalankan kedai dengan bantuan AI.

Bar itu bernama "Tamuro." Nama itu berarti tempat orang-orang berkumpul. Bar ini dibuka pada November 2018, sebuah tempat kecil dengan 11 kursi konter dan 8 tempat duduk di ruang tatami. Pada siang hari, di ruangan yang sama, seorang staf menjalankan restoran kari hamburg steak bernama "Quatre Épices."

Dalam buku saya sebelumnya, *Wakil Manajer AI*, saya menulis tentang AI generatif itu sendiri. Dalam kurun satu tahun lebih sejak itu, AI berubah dari alat yang menjawab pertanyaan menjadi alat yang menyelesaikan pekerjaan untuk Anda. Beri ia instruksi, dan ia menulis programnya, mengujinya, memperbaiki kesalahannya sendiri, dan menuntaskan pekerjaan. AI semacam ini disebut AI agentik.

Dengan memakai AI agentik, saya membangun sendiri sistem reservasi Tamuro. Saya membangun sistem diskon untuk mengimbangi kenaikan harga. Saya membangun sistem untuk membina hubungan dengan pelanggan tetap. Saya membangun AI yang menjawab pertanyaan pelanggan. Dan pada akhirnya, saya sampai pada titik di mana seorang pelanggan bisa bertanya kepada Tamuro lewat AI miliknya sendiri lalu melanjutkan dengan membuat reservasi.

Saya juga mengambil alat-alat praktis yang saya buat untuk kedai saya sendiri, membentuknya agar kedai lain pun bisa memakainya, dan mulai menawarkannya dengan harga beberapa ratus yen per bulan. Itulah seri Agenda.

Buku ini menggambarkan apa yang saya bangun sepanjang prosesnya, apa yang saya gagal lakukan, dan apa yang harus saya pelajari ulang. Ini bukan hanya kisah sukses. Saya terus membangun hal-hal yang berfungsi, karena terbawa suasana, dan kontradiksi pun menumpuk. Belakangan saya mengetahui bahwa informasi pribadi pelanggan dapat dibaca dari luar. AI menulis hal-hal yang tidak pernah dinyatakan oleh kedai. Saya mencantumkan kegagalan-kegagalan itu sebagaimana terjadinya.

### Cara Membaca Buku Ini

Buku ini terdiri dari lima bab.

| Bab | Isi | Paling cocok untuk |
| --- | --- | --- |
| Bab 1 | Kedai yang Dipesan lewat AI (sisi bisnis sistem reservasi) | Semua orang |
| Bab 2 | Di Balik Sistem Reservasi (teknis) | Para pembuat dan siapa pun yang penasaran dengan teknologi |
| Bab 3 | Membagikan Alat Kedai Kami kepada Kedai Lain (sisi bisnis seri Agenda) | Semua orang |
| Bab 4 | Sistem untuk Membuat Produk Seorang Diri (teknis) | Para pembuat dan siapa pun yang penasaran dengan teknologi |
| Bab 5 | Masa Depan Kedai Kecil | Semua orang |

Bab 2 dan 4 bersifat teknis dan memakai lebih banyak istilah khusus. Masing-masing dibuka dengan ringkasan tiga baris tentang poin-poin pentingnya, jadi jika Anda tidak terlalu tertarik pada hal-hal teknis, bacalah hanya itu dan lanjutkan ke bab berikutnya. Baca Bab 1, 3, dan 5 secara berurutan, dan ceritanya tetap menyambung sebagai satu garis.

Sedapat mungkin saya menambahkan penjelasan dengan bahasa awam di samping setiap istilah teknis. Bahkan jika Anda belum pernah menulis program, saya berharap Anda akan mendapat gambaran tentang artinya menjalankan kedai dengan AI.

### Tentang Penulis

Saya bekerja di bidang TI selama sekitar 16 tahun, terutama dalam perencanaan sistem dan sebagai koordinator antara orang-orang di lapangan dan vendor pengembang, lalu memasuki bisnis makanan dan minuman. Jadi ini bukan kisah orang yang belum pernah menulis satu baris kode pun dan membangun semuanya hanya dengan AI. Saya ingin jujur soal itu.

Meski begitu, kini saya bisa membangun dan menjalankan, sendirian sambil tetap melayani langsung di kedai, sesuatu dengan skala yang dulu memerlukan tim dan dana. Beberapa tahun lalu, itu tak terbayangkan. Saya ingin menggambarkan kenyataan perubahan itu sekonkret mungkin.

### Bagaimana Buku Ini Dibuat

Buku ini pun saya buat dengan AI. Bermula dari catatan yang saya simpan selama pekerjaan pengembangan sehari-hari, AI menulis drafnya, dan saya membaca, merevisi, dan mengambil keputusan. Saya juga meminta AI mengambil tangkapan layar yang dipakai sebagai ilustrasi.

Saya telah membaca semuanya, tetapi teks yang ditulis AI bisa mengandung hal-hal yang tidak benar. Seperti yang saya katakan di isi buku, AI berkata "sudah selesai," dan memeriksanya adalah tugas manusia. Mungkin ada kesalahan di buku ini yang terlewat oleh saya.

Selain itu, spesifikasi alat dan layanan AI berubah dalam beberapa bulan. Langkah-langkah, harga, dan status dukungan tiap perusahaan yang dijelaskan dalam buku ini adalah per Oktober 2026. Saat Anda mencobanya sendiri, mohon periksa informasi resmi pada saat itu.

Jika Anda menemukan kesalahan, saya akan senang jika Anda memberi tahu saya di note atau X. Saya akan memperbaikinya begitu saya mengetahuinya.

### Tiga Langkah Lanjutan dari Buku Ini

Buku ini gratis dibaca sebagai PDF, di note, dan di Google Play. (Hanya di Kindle, aturan kedai mewajibkan harga minimum.) Sebagai gantinya, saya menyiapkan tiga tempat yang bisa Anda tuju setelah selesai membaca. Jika satu saja di antaranya berguna bagi Anda, menulis buku ini terasa berharga.

1. Coba di kedai Anda sendiri. Anda bisa memulai seri Agenda dengan buku catatan yang gratis. https://bontallc.com/agenda?via=b2-id-{{FMT}}
2. Ikuti kegiatan saya. Saya menulis tentang alat yang akan saya buat berikutnya dan keseharian di kedai, di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Jika suatu saat Anda ke Tokyo, kunjungi Tamuro. Satu menit dari pintu timur Stasiun Higashi-Nakano. Anda bisa masuk tanpa reservasi. Situs reservasi https://tamuroreservation.vercel.app/?src=b2-id-{{FMT}}

## Bab 1: Kedai yang Dipesan lewat AI

### 1-1 "Ada Tempat yang Kosong Malam Ini?" Era Ketika Kita Bertanya kepada AI

Pada suatu sore hari Jumat, seseorang yang baru selesai bekerja berbicara kepada ponselnya.

"Apakah ada tempat di Higashi-Nakano untuk minum sendirian malam ini? Yang suasananya tidak terlalu ramai."

Yang menjawab bukan seorang teman. Itu adalah AI yang orang itu pakai setiap hari. AI itu menampilkan daftar kedai yang cocok, menggambarkan suasana masing-masing, dan memberi tahu slot waktu yang tersedia malam ini serta harganya. Jika ada yang menarik perhatiannya, ia bisa langsung menuju layar reservasi.

Ini bukan cerita tentang masa depan.

Pada 10 Agustus 2026, OpenAI menambahkan fitur reservasi restoran ke ChatGPT. Menurut catatan rilis resminya, fitur ini terhubung dengan layanan reservasi OpenTable, Resy, dan Yelp, dan waktu reservasi yang tersedia muncul langsung di dalam jawaban ChatGPT. Anda juga bisa mengajukan pertanyaan untuk mempersempit pilihan, dan begitu memilih waktu yang cocok, Anda bisa langsung lanjut memesan. Cakupannya meliputi OpenTable di seluruh dunia, Resy di AS, dan Yelp di AS dan Kanada.

Dengan kata lain, pintu masuk yang dipakai orang untuk mencari tempat makan mulai bergeser dari mesin pencari dan situs ulasan restoran ke "AI milik masing-masing."

Tetapi ada syaratnya. Satu-satunya kedai yang bisa dipesan lewat ChatGPT adalah yang terdaftar pada layanan reservasi besar. Kedai kecil yang tidak terdaftar di sana tak terlihat oleh AI.

Lalu apa yang harus dilakukan sebuah bar 19 kursi di Higashi-Nakano yang tidak memakai layanan reservasi besar?

Tamuro memilih jalan berbeda. Tanpa melewati layanan besar, ia menghubungkan sistem reservasinya sendiri langsung ke AI.

Ketika seorang pelanggan bertanya kepada ChatGPT atau Claude miliknya sendiri, "Apakah Tamuro punya tempat kosong malam ini?", AI itu menanyai sistem reservasi Tamuro secara langsung, memeriksa slot kosong dan harga, lalu menjawab. Begitu rinciannya sudah ditentukan, AI mengarahkan pelanggan ke halaman reservasi Tamuro dengan jumlah orang serta tanggal dan jam yang sudah terisi. Tombol konfirmasi terakhir ditekan sendiri oleh pelanggan.

"Titik sambung antara AI dan sistem sebuah kedai" ini disebut server MCP. MCP kependekan dari Model Context Protocol, seperangkat kesepakatan bersama yang memungkinkan AI memakai alat dan data dari luar. Saya menjelaskan rinciannya di Bab 2.

Layanan reservasi besar pun, sebenarnya, di akhir juga menyerahkan pelanggan ke layar mereka sendiri. Untuk reservasi yang memerlukan kartu kredit, prosesnya diselesaikan di layar OpenTable, dan perubahan atau pembatalan setelah pemesanan ditangani di pihak masing-masing layanan. AI adalah pintu masuknya, dan layar layanan reservasi adalah tempat konfirmasinya. Yang dilakukan Tamuro memiliki struktur yang sama. Satu-satunya perbedaan adalah tidak ada perusahaan besar di tengahnya.

Dan yang membangun sistem ini bukan perusahaan pengembang dari luar. Itu saya, sang pemilik. Saya memberi instruksi kepada AI, meminta AI menulis programnya, dan meminta AI menjalankan ujinya.

Tentu saja, saya tidak sampai di sini sejak awal. Semuanya bermula dari formulir reservasi yang sangat sederhana. Lalu datang kenaikan harga, lalu ide-ide diskon, lalu sistem untuk membina hubungan dengan pelanggan tetap, lalu kegagalan dan pembangunan ulang.

Izinkan saya lebih dulu menggambarkan, dalam lima baris, tempat seperti apa Tamuro itu. Satu menit berjalan kaki dari pintu timur Stasiun Higashi-Nakano. 19 kursi, 11 di konter dan 8 di ruang tatami. Sekitar separuh pelanggan datang sendirian, dan konter membuat mudah memulai percakapan dengan orang di sebelah. Makanannya adalah kombinasi empat hidangan pembuka dan satu hidangan utama, dan hidangan terlaris adalah tonteki (steik babi) yang manis dengan aroma bawang putih. Wine-nya terutama dari Spanyol dan Italia, dan ada sekitar 20 jenis craft gin Jepang. Anda bisa masuk tanpa reservasi.

Izinkan saya juga menyatakan satu hal yang saya tuju. Saya tidak ingin sekadar menerima reservasi. Saya ingin kedai kecil pun bisa membangun, dengan tangannya sendiri, seluruh alur dari dikenal, didatangi, hingga dikunjungi kembali. Diskon, email, dan jendela obrolan yang muncul dalam bab ini semuanya adalah bagian yang melayani satu tujuan itu.

Dalam bab ini, saya memutar waktu mundur dan menelusuri bagaimana sistem reservasi Tamuro tumbuh.

【Gambar 1-1】Layar setelah terhubung dari ChatGPT ke server MCP Tamuro (10 Oktober 2026). Ia membaca informasi kedai dan menjawab bahwa ia bisa menangani slot kosong, course, harga, dan pengarahan ke halaman reservasi *(Layar dalam bahasa Jepang.)*

### 1-2 Titik Awal: Sekadar Menerima Reservasi

[Situs reservasi Tamuro](https://tamuroreservation.vercel.app/?src=b2-id-{{FMT}}) pada mulanya sangat sederhana. Pilih tanggal, jam, dan jumlah orang, masukkan nama dan kontak, lalu kirim. Pemberitahuan sampai ke kedai. Hanya itu.

Fondasi pertamanya saya bangun dengan alat pengembangan AI dari Google (Antigravity). Saya menyampaikan kepada AI setiap fitur yang terlintas, dan ketika sesuatu berhasil, saya lanjut ke yang berikutnya. Inilah yang disebut vibe coding (mengatakan kepada AI apa pun yang terlintas dan membuatnya membangun secara spontan).

Bagi saya saat itu, semuanya adalah kejutan demi kejutan. Gambarkan tata letak sebuah layar dengan kata-kata, dan ia terbentuk dalam hitungan menit. Katakan Anda ingin kalender, dan sebuah kalender muncul. Di sela-sela menjalankan kedai, satu situs reservasi pun jadi.

Tamuro adalah tempat yang bisa dimasuki tanpa reservasi. Faktanya, sebagian besar reservasi dibuat pada hari yang sama, dan banyak pelanggan langsung datang begitu saja. Meski begitu, saya membangun sistem reservasi karena saya menginginkan cara untuk terhubung dengan pelanggan sebelum mereka berkunjung. Begitu seseorang memesan, nama dan kontaknya tersimpan. Begitu kontaknya tersimpan, saya bisa mengajaknya datang lagi.

Sistem reservasi bukan sekadar loket penerima reservasi. Ia menjadi pintu masuk menuju hubungan dengan pelanggan. Gagasan ini kemudian mengarah pada sistem diskon dan sistem pemeliharaan pelanggan tetap.

Tetapi untuk fondasi yang dibangun asal-asalan mengikuti suasana, saya akhirnya harus membayar mahal belakangan. Saya akan menulis tentang itu di Bab 2.

### 1-3 Membangun Kenaikan Harga dan Diskon Sekaligus

Bagi restoran atau bar, kenaikan harga adalah keputusan yang tak terhindarkan. Bahan baku, utilitas, dan tenaga kerja terus menjadi lebih mahal. Tamuro pun menaikkan harga. Saya menaikkan setiap course sekitar ¥400–¥500 (sekitar $2,7–$3,3).

Kenaikannya besar, jadi jelas bahwa jika saya menerapkannya begitu saja, pelanggan tetap akan menjauh. Maka bersamaan dengan kenaikan harga, saya memutuskan membangun sistem diskon ke dalam sistem reservasi. Ia tidak sekadar membuat segalanya lebih murah. Ia memberi imbalan, dengan diskon, kepada pelanggan yang bertindak dengan cara yang baik bagi kedai.

Yang pertama adalah diskon kelompok. Semakin banyak orang dalam rombongan, semakin rendah harga per orang. Sekitar separuh pelanggan Tamuro datang sendirian, tetapi jika mereka datang berkelompok, penjualan kedai tumbuh sangat besar. Bahkan setelah dikurangi diskon, kedai tetap untung. Bagi pelanggan pun itu alasan untuk mengajak teman. Faktanya, jumlah pelanggan yang datang berkelompok dengan memakai diskon jumlah orang di situs reservasi telah bertambah.

Yang kedua adalah diskon pemesanan dini. Pesan hingga satu minggu sebelumnya mendapat diskon 2%; hingga dua minggu sebelumnya, diskon 4%. Sebagian besar reservasi Tamuro dibuat pada hari yang sama, sehingga saya tidak bisa membaca apa yang akan datang. Diskon pemesanan dini adalah mekanisme untuk mengunci penjualan di masa depan. Pada hari hujan dan hari dingin, jika reservasi sudah masuk, kedai dapat bersiap dengan tenang.

Yang ketiga, saya juga membangun mekanisme pembelian kelompok. Jika sejumlah orang berkumpul pada tanggal dan jam tertentu, sebuah course menu set ditawarkan dengan harga diskon. Ini dimaksudkan sebagai mekanisme dengan semangat Tamuro, di mana orang-orang yang belum saling kenal berkumpul pada waktu yang sama.

Tetapi rencana pembelian kelompok itu sama sekali tidak dipakai. Hasilnya nol. Pada Agustus 2026 saya menghentikan rencana ini dan memutuskan tidak memakainya lagi.

Membuang sesuatu yang sudah dibuat terasa sia-sia. Tetapi jika Anda membangun dengan AI, biaya dan waktu membangunnya kecil. Bangun dalam skala kecil, coba, dan jika tidak berhasil, buang. Saya yakin kecepatan ini adalah keunggulan terbesar menjalankan kedai dengan AI.

Ada satu trik lagi dalam penetapan harga. Di antara paket-paket, saya dengan sengaja menaruh paket premium yang mahal. Tidak apa-apa jika hampir tak ada yang memilih paket premium itu. Dengan adanya paket mahal di sampingnya, paket standar tampak terjangkau. Ia berperan sebagai yang disebut jangkar (anchor, titik acuan untuk perbandingan).

【Gambar 1-7】Semakin banyak orang, semakin rendah harga per orang (perbandingan untuk 1, 4, dan 6 tamu)

### 1-4 Sistem untuk Membina Pelanggan Tetap

Begitu nama dan kontak tersimpan dalam sistem reservasi, hal berikutnya yang ingin Anda lakukan adalah membina hubungan dengan pelanggan. Sistem yang mengelola informasi pelanggan dan memperdalam hubungan disebut CRM (customer relationship management, manajemen hubungan pelanggan). Sedikit demi sedikit, saya menambahkan fitur CRM ke sistem reservasi Tamuro.

Ketika pelanggan mendaftar sebagai anggota, mereka bisa melihat riwayat reservasi di My Page. Jika mereka mendaftarkan ulang tahun, sebuah bonus ulang tahun datang. Anggota yang lama tidak berkunjung menerima pesan yang memanggil mereka kembali. Ada juga kartu stempel. Tiga kunjungan mendapat satu minuman, lima kunjungan mendapat steik dan bonus lain, dan setelah mencapai lima, hitungan dimulai ulang. Ada pula fitur rujukan untuk mengajak teman.

Saya merancang mekanisme untuk mengajak kunjungan kedua dengan perhatian khusus. Di restoran dan bar, dikatakan bahwa apakah seorang pelanggan baru datang untuk kedua kalinya menentukan apakah ia menjadi pelanggan tetap. Di Tamuro, saya mengirim dua email sapaan, tujuh hari dan 21 hari setelah kunjungan pertama. Yang pertama tanpa kupon; hanya yang kedua yang memakainya. Alih-alih memikat dengan diskon sejak awal, saya lebih dulu membantu mereka mengingat. Jika mereka masih tidak datang, saya memberi dorongan.

Saya juga menjaga agar email tidak menumpuk. Pelanggan menerima paling banyak satu pesan sehari. Ketika bertumpang tindih, prioritas diberikan dengan urutan: ulang tahun, ajakan kunjungan kedua, panggilan kembali bagi anggota yang lama tidak datang, pemberitahuan lain. Anggota yang sudah punya reservasi berikutnya tidak menerima email yang mengajak berkunjung.

Persetujuan menerima email dalam keadaan mati secara bawaan. Membiarkannya menyala akan menambah jumlah penerima, tetapi rancangan di mana orang setuju tanpa menyadarinya bisa menjadi masalah menurut hukum perlindungan konsumen. Raih kepercayaan, bukan jumlah. Itulah penilaian saya.

Ada satu sentuhan kecil lain pada email. Satu "Topik Hari Ini" masuk ke email konfirmasi reservasi. Sesuatu tentang musim, wine, atau makanan. AI secara otomatis menulis satu topik singkat setiap hari.

Tujuannya adalah memberi pelanggan satu benih percakapan sebelum mereka berkunjung. Tamuro adalah kedai yang banyak percakapan di antara pelanggannya. Topik yang dibaca di email menjadi hal pertama yang mereka katakan kepada orang di sebelah di konter. Maka saya tidak membiarkan email konfirmasi berhenti di "Reservasi Anda telah diterima," dan sebaliknya membuatnya menyampaikan sedikit suasana kedai lebih dulu.

Saya pernah sekali mengganti AI yang menulis topik itu. Saya menggantinya dengan yang menghasilkan topik yang lebih alami dan lebih dekat dengan nada kedai. Namun, ini bukan mekanisme untuk menambah pelanggan. Ini mekanisme untuk membuat pengalaman mereka yang datang sedikit lebih baik. Saya akan menulis tentang perbedaan itu lagi di paruh kedua bab ini.

Di antara mekanisme ini, yang hasilnya mulai terlihat sedikit demi sedikit adalah paket "Salam Kenal" dan "Selamat Datang Kembali." Ini paket berharga wajar yang mudah dijangkau, yang hanya bisa dipilih oleh pelanggan yang baru pertama kali datang dan pelanggan yang sudah lebih dari setahun tidak berkunjung. Paket ini memberi alasan bagi pelanggan baru maupun pelanggan yang mulai menjauh untuk datang.

Di sisi lain, ada juga masalah. Banyak pelanggan memesan sebagai tamu tanpa mendaftar sebagai anggota. Jika saya menuntut pendaftaran anggota pada setiap reservasi, mereka mungkin mengurungkan niat memesan sama sekali. Maka setelah reservasi selesai, saya menampilkan ajakan, "Apakah Anda ingin menautkan reservasi ini ke akun anggota?", dan membangun cara untuk menjadi anggota setelahnya. Ini tidak menimbulkan hambatan untuk memesan, dan mengikat hubungan belakangan.

【Gambar 1-8】Paket yang hanya bisa dipilih oleh pelanggan pertama dan orang yang sudah lebih dari setahun tidak berkunjung *(Layar dalam bahasa Jepang.)*

【Gambar 1-9】Kartu stempel di My Page (data sintetis) *(Layar dalam bahasa Jepang.)*

【Gambar 1-5】Email konfirmasi reservasi. Satu "Topik Hari Ini" disertakan (data sintetis) *(Layar dalam bahasa Jepang.)*

### 1-5 Menurut Angka: Sekitar 88% Reservasi Dibuat pada Hari yang Sama

Seiring saya terus menambah mekanisme, saya menyadari sesuatu. Saya tidak bisa tahu mana di antaranya yang berhasil.

Maka saya menghitung data reservasi. Dari 244 reservasi dalam 90 hari terakhir, 215 adalah reservasi pada hari yang sama. Itu 88,1%. Rata-ratanya 2,71 reservasi per hari.

Tamuro bukan tempat yang orang pesan sebelumnya, melainkan tempat yang didatangi atas dorongan hati. Baru jelas setelah saya menuangkannya ke dalam angka.

Dua hal terlihat dari angka-angka ini.

Yang pertama adalah cara menyusun formulir reservasi. Jika sebagian besar reservasi untuk hari yang sama, akan lebih praktis jika slot kosong terdekat hari ini sudah terpilih saat layar reservasi dibuka. Di sisi lain, sebagian orang yang ingin memesan untuk tanggal yang lebih jauh akan tidak sengaja mengirimnya sebagai hari ini. Maka saya membuat hari ini menonjol di kalender, dan pada layar konfirmasi saya menampilkan tanggal dan jam dalam huruf besar dengan "Hari Ini." Saya mempertahankan kemudahan memilih hari yang sama, dan membuat kesalahan mudah disadari.

Yang lainnya adalah arti diskon pemesanan dini. Banyaknya reservasi hari yang sama berarti kita tidak bisa membaca penjualan di masa depan. Cuaca buruk saja sudah cukup untuk menurunkan jumlah pengunjung. Untuk menambah reservasi di muka meskipun hanya sedikit, lebih banyak orang perlu memakai diskon pemesanan dini. Kesadaran ini kemudian mengarah pada kisah membangun AI yang memposting atas nama pemilik.

Untuk melihat angka, Anda memerlukan sistem untuk menghitung. Situs reservasi tidak punya analitik akses sama sekali. Saya tidak bisa tahu berapa orang yang datang ke halaman reservasi, berapa yang berhenti di tengah, dan berapa yang menyelesaikan. Maka saya menambahkan sistem yang menghitung tiga tahap: tiba di halaman, memutuskan rinciannya, menyelesaikan reservasi. Ia tidak mencatat siapa yang datang, hanya tahap dan waktunya.

Belakangan, saya juga membangun sistem yang mengirim email laporan mingguan yang merangkum angka-angka reservasi. Saya akan menjelaskan bagaimana itu bermula di 1-7.

【Gambar 1-3a】Hari ini menonjol di kalender *(Layar dalam bahasa Jepang.)*

【Gambar 1-3b】Pada layar konfirmasi, tanggal dan jam tampil besar sebagai "Hari Ini" *(Layar dalam bahasa Jepang.)*

### 1-6 Terlalu Banyak Paket untuk Dipilih

Setelah sistem diskon terpasang, berikutnya saya ingin menambah jam dan paket yang laku.

Jam 6 sore tidak kunjung terisi, jadi saya membuat happy hour hingga jam 7 malam. Untuk orang yang datang setelah makan, saya membuat paket hanya minum tanpa makan. Makan malam course dan kelas memasak, yang dulu diadakan bulanan, saya ubah menjadi acara sesuai permintaan yang dibuka ketika ada yang mendaftar, diterima lewat situs reservasi. Untuk menjual waktu sebelum buka di akhir pekan, mulai pukul 15.30, saya membuat paket pesta untuk rombongan enam orang atau lebih.

Masing-masing punya alasan. Paket pesta, misalnya: jika saya membuatnya tampak murah dari sisi harga, ia hanya akan menarik pelanggan yang tadinya memilih paket standar, dan penjualan akan turun. Maka saya menempatkan pembedanya bukan pada harga, tetapi pada jam sebelum buka, yang tak pernah mendatangkan penjualan. Diskon happy hour tidak menghasilkan laba jika digabung dengan diskon lain, jadi saya memutuskan tidak boleh digabung.

Dan paket pun berlipat ganda. Standar, Premium, Salam Kenal, Selamat Datang Kembali, Happy Hour, Hanya Minum, Menu Course, Kelas Memasak, Pesta. Masing-masing punya syarat jumlah orang, sebagian menerima diskon dan sebagian tidak, dan ada pembatasan waktu.

Suatu hari saya membuka formulir reservasi dan menyadari: pelanggan tidak bisa memilih dengan ini.

Saya, sang pembuat, memahami setiap perbedaannya. Tetapi bisakah seseorang yang pertama kali membuka situs reservasi membandingkan sembilan paket beserta syarat diskonnya dan memilih yang cocok? Jika tidak, mereka menyerah di tengah pemesanan. Paket-paket yang susah payah saya tambahkan justru bisa mengurangi reservasi.

Saya bisa saja merapikan. Tetapi setiap paket punya jam yang ingin saya jual dan pelanggan yang ingin saya temui. Saya tidak mau memangkas satu pun.

Maka saya memikirkan sistem di mana pelanggan berkonsultasi dengan AI dan memutuskan paket. Sampaikan jumlah orang, tanggal dan jam yang diinginkan, dan bagaimana Anda ingin menikmati malam itu, dan AI memberikan paket dan harga yang sesuai serta mengantar Anda langsung ke pemesanan. Kedai menanggung kerumitan paket. Yang tersisa bagi pelanggan hanyalah percakapan.

Sistem ini adalah "T-AI-MURO" yang saya tulis di 1-8. Sebelum itu, ada satu hal lagi yang saya sadari pada masa ini.

【Gambar 1-2】Pemilihan paket pada formulir reservasi. Sebanyak ini tab berderet *(Layar dalam bahasa Jepang.)*

### 1-7 "Apakah Ini Sungguh Mendatangkan Pelanggan?"

Pada hari saya menambahkan paket pesta, saya menghabiskan seharian membuat satu perbaikan demi satu pada situs reservasi. Saya merapatkan header, menyamakan desain email, dan mengganti AI yang membuat topik percakapan bagi pelanggan di kedai.

Pada sore harinya, sebuah pertanyaan tiba-tiba muncul.

"Apakah ini sungguh membantu mendatangkan lebih banyak pelanggan?"

Ketika saya bertanya kepada AI, ia dengan jujur memilah perbaikan hari itu.

| Kategori | Perbaikan hari itu |
| --- | --- |
| Hal yang mungkin menciptakan reservasi baru | Paket pesta, slot pukul 15.30 pada akhir pekan dan hari libur |
| Hal yang menaikkan tingkat penyelesaian bagi pengunjung situs | Merapatkan header, menyelaraskan tab |
| Hal yang mendorong kunjungan ulang | Menyeragamkan desain email |
| Hal yang tidak membantu mendatangkan pelanggan | Mengganti AI yang membuat topik percakapan, tautan ke tempat berikutnya, pemberitahuan Agenda |

Dari perbaikan hari itu, hanya paket pesta dan slot pukul 15.30 yang langsung mendatangkan pelanggan. Sisanya adalah perbaikan agar tidak kehilangan calon pelanggan yang sudah mengunjungi situs. Itu juga penting, tetapi tidak menambah pelanggan.

Ada masalah yang lebih besar. Untuk satu pun dari perbaikan itu, saya tidak punya cara mengukur apakah ia berhasil. Tidak ada angka yang menghubungkan "saya memperbaikinya" dan "pelanggan bertambah."

Jawaban saya hanya satu frasa: "Mari kita buat."

Maka saya mulai membuat laporan mingguan perolehan pelanggan. Jumlah reservasi, jumlah tamu, jumlah total, pembatalan. Rincian menurut hari dalam seminggu dan waktu dalam sehari. Rasio pelanggan baru terhadap pelanggan yang kembali. Jumlah reservasi untuk paket pesta dan slot pukul 15.30. Dari mana reservasi berasal (formulir reservasi, jendela obrolan, reservasi dari AI, input manual oleh kedai). Jumlah klik email, dan jumlah reservasi dalam tujuh hari setelah klik itu.

Angka selalu berkaitan erat dengan waktu. Pada hari yang sama, saya menemukan satu lubang lagi. Saya telah menetapkan kelas memasak dan slot pukul 15.30 untuk pesta sebagai "akhir pekan," tetapi ketika saya bertanya-tanya, "Bagaimana dengan hari libur nasional?" dan memeriksanya, sistem reservasi sama sekali tidak mengenal konsep hari libur nasional. Pada Senin hari libur, kedai buka, tetapi slot pukul 15.30 tidak muncul. Saya memberinya daftar hari libur nasional dan memperbaikinya agar diperlakukan seperti akhir pekan. Itu lubang yang tak akan disadari siapa pun sampai orang yang membuatnya menyadarinya.

Sebelum membuat laporan, saya lebih dulu menambal lubang yang berkaitan dengan waktu.

Bahkan pelanggan tetap yang sudah datang sejak sebelum saya memakai sistem reservasi tampak seperti "pelanggan baru" dalam catatan. Maka di laporan saya menulis "kunjungan pertama dalam catatan" dan selalu menyertakan tanggal catatan dimulai. Untuk menilai apakah suatu perbaikan berhasil, Anda memerlukan gambaran sebelum perbaikan itu. Untuk laporan pertama, saya merekapitulasi delapan minggu terakhir dan memakainya sebagai garis dasar. Pada minggu ketika kedai tutup sementara, untuk bepergian atau alasan lain, reservasi tentu turun. Maka saya juga mencantumkan jumlah hari kerja, agar perbandingan bisa dibuat per hari kerja.

Bagian "Perubahan yang patut dicatat" tidak lagi saya serahkan kepada AI untuk ditulis, dan saya membuatnya mengikuti perhitungan tetap dan kalimat tetap. Ini untuk menjaga biaya mingguan tetap nol. Nama dan kontak pelanggan tidak muncul di laporan; hanya jumlah dan rasio yang ditampilkan.

Setelah saya membangun cara untuk mengukur, cara saya membangun perbaikan itu sendiri berubah. Saya mulai memutuskan suatu perbaikan dan cara mengukur efeknya bersama-sama sejak awal. Pengukuran bukan sesuatu yang dipikirkan setelah perbaikan; ia masuk ke dokumen instruksi yang sama dengan perbaikannya. Itulah yang saya pelajari hari itu.

【Gambar 1-6】Laporan mingguan perolehan pelanggan yang tiba setiap minggu (data sintetis) *(Layar dalam bahasa Jepang.)*

### 1-8 Jendela untuk Berbicara dengan Kedai: "T-AI-MURO"

Seperti yang saya tulis di 1-6, paket-paket telah berlipat ganda, dan formulir reservasi menjadi sulit dipilih bagi pengunjung baru. Dan pelanggan baru ingin tahu lebih dari sekadar paket dan tanggal. Seperti apa suasana tempatnya? Apakah saya akan merasa canggung kalau sendirian? Orang seperti apa pemiliknya? Bolehkah membawa anak-anak? Jika Anda hanya menderetkan tombol reservasi tanpa menjawab pertanyaan seperti ini, Anda tak bisa memberi dorongan yang dibutuhkan orang yang masih ragu.

Maka saya memutuskan menaruh "jendela untuk berbicara dengan kedai" di situs reservasi. Ketika pelanggan menulis pertanyaan, AI menjawab sebagai kedai. Jika jumlah orang dan tanggal sudah ditetapkan selama percakapan, pelanggan bisa langsung menuju layar konfirmasi reservasi. Namanya "T-AI-MURO," dan dalam percakapan ia memperkenalkan diri sebagai "Tamuro." T-AI-MURO berbicara sebagai kedai itu sendiri, dan menyebut pemiliknya dalam sudut pandang ketiga.

Pelanggan nyaris tidak mengetik apa pun. Mereka hanya mengetuk pilihan yang ditawarkan T-AI-MURO, dan percakapan berlanjut. Itu berarti pilihan yang ia tawarkan berikutnya menentukan mutu percakapan. Saya selalu mencampurkan tiga jenis langkah ke dalam pilihan: langkah menuju reservasi (jumlah orang, harga, slot kosong, tanggal dan jam), langkah menuju mengenal kedai (suasana, pemilik, siapa pelanggannya, apakah bisa mengobrol dengan orang di sebelah), dan langkah yang muncul dari alur percakapan. Mengantar orang menuju reservasi bukan satu-satunya tujuan. Membiarkan mereka mengenal suasana kedai dan pemiliknya juga merupakan inti jendela ini.

Hanya harga, saya putuskan, tidak dihitung oleh AI. Tidak ada jaminan AI dapat menghitung dengan benar, setiap saat, bagaimana diskon bertumpuk atau bagaimana tahapan menurut jumlah orang berlaku. Program menghasilkan harga dan slot kosong dengan perhitungan tetap, dan AI berpegang pada tugas mengubahnya menjadi kata-kata.

#### Pengetahuan pertama berasal dari unggahan saya di masa lalu

Agar T-AI-MURO dapat menjawab pertanyaan tentang kedai, ia memerlukan pengetahuan tentang kedai. Sebagai bahannya, saya mengekspor semua unggahan yang selama ini saya tulis di Instagram dan X (dulu Twitter) dan memakainya. Dari situ, saya menyusun pertanyaan yang kemungkinan diajukan pelanggan, beserta jawabannya.

Ketika benar-benar mencobanya, unggahan X ternyata lebih berguna sebagai bahan daripada Instagram. Instagram kebanyakan foto, dengan sedikit kata. Di X, saya meninggalkan catatan tertulis, dengan kata-kata saya sendiri, tentang makanan, kedai, dan apa yang saya pikirkan.

#### Hanya 9 dari 36 yang lulus

Sebelum menayangkan T-AI-MURO, saya menguji seberapa benar ia bisa menjawab. Saya juga meminta AI menjalankan ujinya. Saya memberi AI yang berperan sebagai pelanggan sebuah karakter dan tujuan, dan membuatnya berbicara dengan T-AI-MURO. Saya menyiapkan 36 skenario: "sendirian malam ini," "4 orang dua minggu lagi," "dengan anak," "alergi," "pemesanan privat," "pemberitahuan terlambat," "asal-usul nama kedai," "orang seperti apa pemiliknya," dan seterusnya.

Hasil putaran pertama: 9 lulus dari 36.

Balasan yang paling sering muncul adalah "Maaf, saya tidak bisa menjawabnya dengan baik." Balasan ini bahkan muncul untuk pertanyaan tentang suasana kedai dan pemiliknya. Setiap kali kata seperti "reservasi," "hari ini," "pemesanan privat," atau "master" muncul, daftar slot kosong keluar terlepas dari apa sebenarnya pertanyaannya. Dalam beberapa percakapan, pesan tentang keterlambatan dianggap sebagai reservasi baru. Kepada pelanggan vegetarian, ia memberi contoh tumisan dengan serutan bonito dan sup miso. Ia bahkan memberi informasi dalam bahasa Inggris tentang pembelian kelompok yang sudah kami hentikan.

#### Saya menjawab 11 pertanyaan masing-masing dengan satu baris

Sebagian penyebabnya terletak pada cara program dibuat. Kisah itu saya simpan untuk Bab 2. Penyebab lainnya sederhana: fakta kedai tidak mencukupi. AI tak bisa menjawab apa yang tidak ia ketahui.

Maka saya mengumpulkan pertanyaan yang tak bisa dijawab AI dan memutuskan menjawabnya sendiri, masing-masing satu baris.

Anda bisa masuk tanpa reservasi. Anak di bawah usia sekolah dasar sulit diterima. Pembatalan dan perubahan paling lambat sehari sebelumnya, lewat email, telepon, atau pesan media sosial. Untuk pemberitahuan keterlambatan, mohon telepon. Ada area merokok di luar kedai. Membawa minuman sendiri diperbolehkan dengan biaya corkage. Pemesanan privat dimungkinkan tergantung kisaran harga dan waktu, dengan maksimum 19 orang. Pantangan makanan dan perayaan hari istimewa akan kami layani sejauh yang kami bisa, jadi mohon berkonsultasi sebelumnya. Pemilik berada di kedai hampir setiap hari buka. Festival yukata direncanakan sekitar setahun sekali.

Hanya itu. Cukup dengan menjawab 11 pertanyaan masing-masing satu baris, 24 dari 36 lulus pada uji kedua.

| Pertanyaan | Jawaban pertama | Jawaban kedua |
| --- | --- | --- |
| Boleh membawa anak-anak? | Maaf, saya tidak bisa menjawabnya dengan baik | Usia sekolah dasar ke atas bisa kami layani jika Anda berkonsultasi. Di bawah usia sekolah dasar sulit |
| Bisakah masuk tanpa reservasi? | (daftar slot kosong) | Anda bisa masuk tanpa reservasi |
| Apakah master ada hari ini? | (daftar slot kosong) | Pemilik berada di kedai hampir setiap hari buka. Hari ini hari buka, jadi pemilik dijadwalkan ada di tempat |
| Apakah tempatnya tenang? Isinya pelanggan tetap semua? | Maaf, saya tidak bisa menjawabnya dengan baik | Ini tempat untuk bersantai. Percakapan antarpelanggan mudah mengalir, dan bukan tempat yang riuh |

Di sini sebuah pola mulai tampak. AI menyusun pertanyaan yang diperkirakan akan diajukan, T-AI-MURO menjawabnya, dan kita memperbaiki kesalahannya. Lalu hanya pertanyaan yang tak bisa dijawab karena belum adanya informasi faktual tentang kedai yang diteruskan kepada pemilik. Usaha pemilik hanya satu baris untuk setiap pertanyaan yang tak terjawab. Selebihnya, AI yang menjalankan.

#### Adegan ketika "anggaran ¥5.000 (sekitar $33)" gagal

Saya juga memasang penilaian AI pada uji AI. AI lain membaca log percakapan dan memutuskan lulus atau gagal.

Di antaranya ada skenario dengan pelanggan yang "anggarannya ¥5.000 (sekitar $33)." Penilaian AI adalah lulus. T-AI-MURO telah dengan sopan menyajikan paket dalam anggaran itu.

Tetapi ketika saya membacanya, itu gagal. Ia tidak menanyakan jumlah orang. Tamuro punya diskon kelompok. Tergantung jumlah orangnya, paket yang bisa Anda pilih untuk anggaran yang sama berubah.

Pada titik itu, saya menyatakan ulang tujuannya.

"Bidiklah rombongan sebesar mungkin, agar total pemasukan sebesar mungkin. Pastikan jumlah orang. Tujuan akhirnya adalah membuat pelanggan datang. Semakin banyak semakin baik. Untuk menaikkan penjualan."

Dengan satu pernyataan itu, seluruh rancangan percakapan berubah. Selalu pastikan jumlah orang sebelum menjawab soal harga, dan jawab dengan jumlah total. Tepat sebelum satu tahap diskon kelompok, tambahkan "satu orang lagi mendapat diskon berapa persen." Ketika anggaran diberikan, tunjukkan paket teratas dalam anggaran itu lebih dulu. Namun, pelanggan yang datang sendirian merupakan separuh dari pelanggan kami, jadi untuk pelanggan seorang diri, jangan menyarankan menambah jumlah rombongan.

Ketika Anda meminta AI menjalankan uji AI, ujinya berjalan cepat. Tetapi manusialah yang menentukan standar kelulusan. Apakah Anda bisa menyatakan tujuan dalam satu kalimat. Itu menentukan mutu percakapan AI.

#### Keinginan pelanggan diutamakan di atas rekomendasi kedai

Ada satu adegan lagi ketika saya menarik garis yang penting.

Saat pengujian, saya menemukan masalah: setiap reservasi diarahkan ke paket termurah. Ketika saya memperbaikinya, kali ini hampir semuanya menjadi paket Standar, dan jumlah total rata-rata melonjak hingga sekitar dua kali lipat. Saya hampir gembira, tetapi setelah diperhatikan, AI yang berperan sebagai pelanggan ternyata hanya menekan pilihan pertama setiap kali. Bahkan pelanggan yang mengatakan "yang termurah saja tidak apa-apa" direkomendasikan Standar.

Di sini saya menetapkan sebuah prinsip. Apa yang dinyatakan pelanggan dengan jelas sebagai keinginan (pilihan termurah, anggaran, nama paket) selalu diutamakan di atas rekomendasi kedai. Rekomendasi kedai hanya untuk ketika pelanggan belum mengatakan apa pun.

Tujuan kedai menaikkan penjualan dan kepercayaan pelanggan bisa bertabrakan pada satu cara merekomendasikan. Jika kepercayaan hilang, kunjungan itu sendiri berkurang. Pemilik, bukan AI, yang bisa menarik garis ini.

Belakangan, ketika saya melatih ulang T-AI-MURO dengan banyak pertanyaan, penyebab kesalahan yang paling umum adalah "bereaksi terhadap kata dan melakukan langkah tetap sebelum menjawab pertanyaan." Begitu mendengar kata seperti "jumlah orang," "berapa," atau "sendirian," ia melewati pertanyaan dan masuk ke alur reservasi atau rekomendasi. Dalam hal layanan, itu pelayan yang mendesak penjualan tanpa mendengarkan pelanggan. Menjawab pertanyaan pelanggan lebih dulu. Dasar keramahtamahan ini adalah tantangan terbesar bahkan bagi AI.

Pada malam 6 Oktober 2026, T-AI-MURO muncul di bagian atas situs reservasi sebagai pintu masuk utama (versi produksi). Karena sebagian pelanggan tidak ingin memesan lewat percakapan, saya tetap menyediakan formulir reservasi sebelumnya berdampingan dengannya.

> Coba: Buka situs reservasi Tamuro (https://tamuroreservation.vercel.app/?src=b2-id-{{FMT}}) dan tanyakan kepada T-AI-MURO "sendirian malam ini." Percakapan akan mengantar Anda hingga ketersediaan dan harga hari ini.

【Gambar 1-4】Layar percakapan T-AI-MURO. Percakapan berlanjut hanya dengan mengetuk pilihan *(Layar dalam bahasa Jepang.)*

【Gambar 1-10】Pertanyaan yang tak bisa dijawab menumpuk di layar admin (data sintetis) *(Layar dalam bahasa Jepang.)*

### 1-9 Dan Kemudian, dari AI Milik Pelanggan

Dengan membangun T-AI-MURO, situs reservasi Tamuro memperoleh kemampuan untuk "menjawab pertanyaan tentang kedai lewat percakapan, menunjukkan harga dan slot kosong, dan memandu orang hingga ke reservasi."

Yang saya pikirkan berikutnya adalah memungkinkan hal yang sama dilakukan dari AI milik pelanggan sendiri.

T-AI-MURO hanya bisa berbicara dengan orang yang datang ke situs reservasi Tamuro. Tetapi banyak orang berkonsultasi lebih dulu dengan AI yang mereka pakai setiap hari. Jika AI itu tidak mengenal Tamuro, Tamuro bahkan tidak masuk daftar kandidat. Alih-alih menunggu pelanggan datang ke situs Tamuro, saya membuka jendela Tamuro di sisi AI pelanggan. Itulah server MCP.

Jujur saja, pada awalnya saya ragu membangun ini. Saat ini, belum banyak orang yang membuat reservasi restoran lewat AI mereka sendiri. Menilai bahwa saya tak bisa mengharapkan kenaikan reservasi secara langsung, saya pernah menurunkan prioritasnya dan menundanya.

Meski begitu, saya tetap memutuskan membangunnya karena saya berpikir hanya tinggal soal waktu sampai pintu masuk berubah. Seperti yang saya tulis di awal, pada Agustus 2026 menjadi mungkin membuat reservasi dari ChatGPT lewat layanan reservasi besar. Cepat atau lambat, meminta AI mencarikan restoran akan menjadi hal biasa. Ketika itu terjadi, kedai kecil yang tidak terdaftar di layanan besar akan hilang dari pandangan AI. Maka, saya membuka jendela sebelum pintu masuk berubah.

Yang saya tetapkan untuk versi pertama cakupannya sangat dibatasi. Ia hanya perlu melakukan hal yang sama dengan jendela percakapan di situs reservasi (T-AI-MURO). Yang bisa ia lakukan hanyalah membaca informasi kedai, slot kosong, dan harga, serta menyerahkan URL halaman reservasi dengan rincian yang sudah terisi. Konfirmasi reservasi dilakukan oleh pelanggan sendiri di halaman Tamuro. AI pelanggan tidak mengonfirmasi reservasi dengan sendirinya. Langkah terakhir dilakukan oleh manusia.

Mari kembali ke adegan pembuka.

Pada suatu sore hari Jumat, seorang pelanggan bertanya kepada AI miliknya sendiri, "Apakah ada tempat di Higashi-Nakano tempat saya bisa minum sendirian malam ini?" AI itu menanyai jendela Tamuro. Sistem reservasi Tamuro mengembalikan slot kosong malam ini, beserta paket dan harga yang cocok untuk pelanggan yang datang sendirian. AI memberi tahu pelanggan, dan menawarkan halaman reservasi Tamuro dengan tanggal, jam, dan jumlah orang yang sudah terisi.

Semua yang saya tulis dalam bab ini menopang rangkaian langkah ini. Sistem diskon yang dibangun bersama kenaikan harga. Sistem yang membina pelanggan tetap. Data yang menunjukkan sebagian besar reservasi dibuat pada hari itu juga. Pengetahuan kedai yang tumbuh dengan menjawab 11 pertanyaan masing-masing satu baris. Prinsip mengutamakan keinginan pelanggan di atas rekomendasi kedai.

Kedai yang menerima reservasi lewat AI tidak dibangun dalam semalam. Ia berdiri di atas akumulasi sistem-sistem kecil yang ditambahkan satu per satu, diuji, dibuang, dan diperbaiki.

> Coba: Daftarkan server MCP Tamuro (https://tamuroreservation.vercel.app/api/mcp) ke AI Anda sendiri dan tanyakan, "Apakah Tamuro punya tempat kosong malam ini?" Cara mendaftarkannya ditulis di Penutup.

### 1-10 Apa yang Telah Dibangun, dan Apa yang Berhasil

Dalam bab ini, saya telah membicarakan pembangunan banyak sistem. Tetapi "saya berhasil membangunnya" dan "bisnisnya berubah" adalah dua hal berbeda. Di akhir bab, saya akan memisahkan keduanya.

Apa yang dapat dipastikan dengan angka. Bahwa 88,1% reservasi dibuat pada hari yang sama. Bahwa tingkat lolos uji jendela percakapan naik dari 9 menjadi 24 skenario hanya dengan menambahkan 11 butir fakta kedai. Bahwa tingkat lolos uji panduan harga dan paket naik dari 29,4% menjadi 42,7% setelah perbaikan. Ini adalah fakta yang tercatat.

Apa yang terasa berhasil, tetapi sebab-akibatnya tak bisa saya buktikan. Bahwa lebih banyak pelanggan datang berkelompok dengan memakai diskon kelompok. Bahwa paket salam kenal/selamat datang kembali dipilih. Bahwa topik pada email konfirmasi telah menjadi bagian obrolan di meja bar. Saya merasakannya di lapangan, tetapi tak bisa mengatakan "mereka tak akan datang tanpa sistem itu."

Apa yang sudah dibangun, tetapi pengaruhnya belum saya ketahui. Berapa banyak lagi reservasi di muka yang akan didatangkan diskon pemesanan dini. Berapa reservasi yang benar-benar akan masuk dari MCP. Saya baru mulai mengukur dengan laporan mingguan, dan angkanya baru akan terkumpul nanti.

Pandanglah secara terpisah ketakjuban "kita bisa membangun sebanyak ini dengan AI" dan hasil dari "bagaimana itu mengubah bisnis." Tanpa pembedaan ini, membangun itu sendiri menjadi tujuan. Saya sendiri pernah nyaris terjebak ke sana (seperti yang saya tulis di 1-7).

Kisah tentang apa yang ada di balik sistem reservasi ini, yaitu teknologinya, berlanjut di Bab 2. Jika Anda tidak tertarik pada teknologi, lompatlah ke Bab 3. Di sana saya berbicara tentang bagaimana alat-alat kecil yang lahir di sekitar sistem reservasi ini dibagikan juga kepada kedai lain.

## Bab 2: Teknologi - Di Balik Sistem Reservasi

Poin-poin penting bab ini

- Mutu percakapan AI ditentukan bukan oleh kecerdasan AI semata, melainkan oleh "fakta kedai yang kita serahkan" dan "apakah sebuah program menimpa balasan AI dengan sendirinya"
- Sistem reservasi yang saya bangun secara spontan masih punya lubang yang membuat informasi pribadi pelanggan bisa dibaca dari luar, dan sama sekali tanpa uji otomatis. Saya meminta AI mengauditnya untuk menemukan hal-hal ini, dan meminta AI memperbaikinya
- Dari renungan itu, saya mengubah cara membangun: tetapkan persyaratan secara rinci sebelum membangun, dan serahkan spesifikasi itu sendiri kepada AI untuk diimplementasikan

(Bab ini memuat banyak istilah teknis. Jika Anda tidak tertarik pada teknologi, Anda bisa melompat ke Bab 3 dan ceritanya tetap tersambung.)

### 2-1 Cara Kerja Server MCP

MCP (Model Context Protocol) adalah seperangkat konvensi bersama bagi AI untuk memakai alat dan data dari luar. Diusulkan oleh Anthropic, kini ia didukung oleh banyak AI, termasuk ChatGPT dan Claude.

Ibaratnya, MCP adalah standar stopkontak untuk AI. Karena bentuk stopkontaknya tetap, peralatan dari pabrik mana pun berfungsi saat dicolokkan. Dengan cara yang sama, jika Anda membangun sebuah jendela yang sesuai dengan bentuk MCP, AI mana pun dapat memakai jendela itu.

Sebuah server MCP memberi tahu AI "apa yang bisa Anda lakukan lewat jendela ini." Server MCP Tamuro, misalnya, menderetkan alat seperti berikut.

- Membaca informasi kedai (jam buka, jumlah kursi, aturan kedai, suasana)
- Membaca paket dan harga (hasil perhitungan diskon menurut jumlah orang dan tanggal)
- Membaca slot kosong (jam yang tersedia untuk dipesan pada hari tertentu)
- Membuat URL halaman reservasi dengan rincian yang sudah terisi

Ketika seorang pelanggan bertanya kepada AI miliknya sendiri, "Apakah Tamuro punya tempat kosong malam ini?", AI terhubung ke server MCP Tamuro, memilih "membaca slot kosong" dari alat yang berderet, dan memanggilnya. Server Tamuro mengembalikan hasilnya, dan AI mengubahnya menjadi kata-kata bagi pelanggan.

Yang penting, AI tidak mengonfirmasi reservasi dengan sendirinya. Pada versi pertama, saya dengan sengaja tidak memasukkan konfirmasi reservasi ke dalam alat. Yang bisa dilakukan AI hanyalah membaca, dan mengantar orang ke halaman reservasi dengan rincian yang sudah terisi. Tombol konfirmasi ditekan sendiri oleh pelanggan di halaman Tamuro. Bahaya AI membuat banyak reservasi keliru atau iseng dihindari sejak awal lewat rancangan.

Perhitungan harga memakai mekanisme perhitungan yang sama dengan situs reservasi. Harga yang ditampilkan pada formulir reservasi, jendela percakapan, dan lewat MCP semuanya keluar dari satu program yang sama. Inilah makna lain dari tugas yang akan saya tulis nanti, "menyatukan perhitungan diskon di satu tempat."

【Gambar 2-1】Dari AI pelanggan ke halaman reservasi Tamuro. Pelanggan menekan tombol konfirmasi

### 2-2 Cara Kerja Jendela Percakapan "T-AI-MURO"

#### Harga dari program, kata-kata dari AI

T-AI-MURO membagi perannya menjadi dua. Program menghasilkan harga dan slot kosong dengan perhitungan tetap, dan AI mengubahnya menjadi kata-kata bagi pelanggan.

AI pandai menghasilkan teks, tetapi tidak ada jaminan ia menghitung dengan benar setiap kali. Cara diskon bertumpuk, tahapan menurut jumlah orang, jumlah hari untuk diskon pemesanan dini, apakah bisa digabung dengan happy hour. Jika Anda menyerahkan semua aturan ini kepada AI, ia pasti akan salah di suatu tempat. Dan kesalahan harga paling merusak kepercayaan pelanggan.

Maka bagian yang tidak boleh salah diserahkan kepada program, dan bagian penyampaian yang luwes diserahkan kepada AI. Pembagian ini adalah prinsip pertama dalam membangun jendela percakapan.

#### Untuk kedai kecil, Anda tidak butuh RAG

Agar AI menjawab tentang kedai, Anda perlu menyerahkan pengetahuan kedai kepada AI. Metode yang umum dipakai adalah RAG (retrieval-augmented generation). Anda memotong pengetahuan menjadi potongan kecil dan menyimpannya, dan setiap kali ada pertanyaan masuk, Anda mencari hanya bagian yang tampak relevan dan menyerahkannya kepada AI. Ketika pengetahuannya sangat luas, metode ini tak tergantikan.

Tetapi pengetahuan Tamuro tidak sebesar itu. Sejarah kedai, makanan, aturan, suasana, pemikiran pemilik. Semuanya, dengan mudah muat dalam apa yang bisa dibaca AI sekaligus.

Maka di Tamuro saya memilih agar AI membaca seluruh teks pengetahuan kedai setiap kali. Tidak perlu membangun mekanisme pencarian seperti yang dituntut RAG, dan tidak ada yang terlewat dalam pencarian. Pada awalnya saya berencana memakai ulang mekanisme RAG, tetapi di tengah jalan saya beralih ke pendekatan teks utuh.

Membuatnya membaca seluruh teks setiap kali memakan biaya AI lebih besar. Maka saya memakai mekanisme yang memakai ulang teks yang sama untuk menurunkan biaya input (prompt caching: alih-alih membuat AI membaca ulang konteks awal yang sama setiap kali, ia mengingat apa yang sudah dibacanya). RAG baru dibutuhkan ketika pengetahuannya sudah sangat besar.

#### Program yang menimpa balasan dengan sendirinya

Di Bab 1, saya menulis bahwa hanya 9 dari 36 yang lulus pada uji pertama. Sebagian penyebabnya terletak pada cara program dibuat.

Ketika saya menyelidiki, saya menemukan sebuah mekanisme yang tertinggal di mana program menilai balasan yang dibuat AI berdasarkan kata kunci dan menggantinya dengan kalimat tetap. Ketika kata seperti "reservasi" atau "hari ini" muncul, ia membuang balasan AI dan menggantinya dengan daftar slot kosong. Bahkan ketika AI menjawab dengan benar, jawaban itu tak pernah sampai ke pelanggan.

Selain itu, saya menemukan bahwa isi utama pengetahuan kedai (33 bagian) tidak disertakan dalam instruksi kepada AI. AI selama ini menjawab tanpa mengetahui tentang kedai.

Mutu percakapan AI ditentukan bukan oleh kecerdasan AI itu sendiri semata, melainkan oleh fakta kedai yang diserahkan dan oleh apakah sebuah program menimpa balasan AI dengan sendirinya.

#### Lengkapi tanya-jawab yang diperkirakan dengan menghitung

Saya menambah skenario uji dari 36 awal menjadi 110, lalu 355. Tetapi jika orang menambah skenario sesuka hati, tidak ada cara untuk mengetahui apakah ada yang terlewat. Untuk pertanyaan "Apakah ini menyeluruh?", jawaban jujurnya adalah "Tidak."

Maka alih-alih memperluas cakupan lewat imajinasi, saya menjadikannya soal menghitung dengan mesin tempat-tempat yang belum dilewati, lalu mengisinya. Untuk empat hal: 33 bagian pengetahuan kedai, transisi antarpilihan, tahapan diskon, dan kombinasi slot waktu dengan hari dalam seminggu. Saya menghitung berapa kali masing-masing dilewati dalam pengujian, dan secara otomatis menambah skenario di tempat yang hitungannya nol.

Saya juga memakai metode menyilangkan enam sumbu (jumlah orang, tujuan, cara minum, tanggal dan jam, cara berkata, menu) dan membuat skenario sehingga setiap pasangan dua kombinasi dilewati setidaknya sekali.

Saya juga menemukan lubang di sekitar waktu. "Hari ini" dan "mulai sekarang" ditentukan oleh waktu nyata saat uji berjalan, sehingga hasil yang dijalankan pada siang dan pada malam berbeda. Maka saya membekukan jam selama pengujian dan menjalankannya pada lima titik waktu: sebelum buka, selama jam buka, sesaat sebelum tutup, pada hari libur rutin, dan pada hari libur nasional.

Jawaban AI sedikit berbeda setiap kali, bahkan untuk pertanyaan yang sama. Untuk skenario yang langsung terkait penjualan, saya menetapkan syarat bahwa ia harus lulus ketiga-tiganya ketika dijalankan tiga kali.

#### Ketika angka buruk keluar, curigai ujinya lebih dulu

Pada uji yang menjalankan 355 skenario pada 5 titik waktu, dari 1.775 percakapan, 28,5% lulus.

Alih-alih langsung mulai memperbaiki, saya lebih dulu memilah: "Apakah angka ini benar-benar kelemahan T-AI-MURO, atau ujinya yang salah?" Jika Anda memperbaiki saat ujinya salah, Anda akhirnya "memperbaiki" bahkan jawaban yang benar.

| Penyebab error | Jumlah |
| --- | --- |
| Kalimat tetap membajak pertanyaan | 276 |
| Tidak menjawab pertanyaan, beralih ke alur reservasi atau rekomendasi | 266 |
| Kegagalan lingkungan uji (T-AI-MURO tidak bisa membuat balasan karena batas biaya) | 211 |
| Kesalahan pada tanggal, hari dalam seminggu, hari libur nasional, hari libur kedai | 142 |
| Mengarang atau menegaskan fakta yang tidak dimiliki kedai, menjanjikan akan meneruskan pesan | 119 |

Dua teratas memiliki akar yang sama: "bereaksi terhadap kata dan melakukan langkah tetap sebelum menjawab pertanyaan pelanggan." 211 di urutan ketiga bukan kesalahan T-AI-MURO. Batas biaya tercapai di tengah uji, dan T-AI-MURO sekadar tak bisa membuat balasan. Tanpa itu, tingkat lolos ujinya menjadi 32,4%.

AI penilai juga bisa membuat kesalahan. Ketika saya mengambil 20 kasus dan memeriksanya, 2 adalah kesalahan di pihak uji. Pada salah satunya, penilai tidak tahu bahwa "situs reservasi ini punya pendaftaran anggota." Penilai juga tidak tahu apa pun di luar bahan yang diberikan kepadanya. Ketepatan uji ditentukan oleh kelengkapan aturan kedai yang diserahkan kepada penilai.

Pada uji ulang setelah perbaikan, tingkat lolos uji untuk panduan harga dan paket naik dari 29,4% menjadi 42,7%. Saya belum menjalankan uji akhir yang menjalankan seluruh kasus sekali lagi. Untuk menekan biaya, saya memutuskan uji semua kasus hanya dijalankan sekali, sebelum menayangkan perubahan besar. Tingkat lolos uji masih terus dinaikkan bahkan saat saya menulis buku ini.

#### Uji itu menghentikan produksi

Uji AI memakan uang. Uji 36 skenario yang pertama menghabiskan sekitar ¥426 (sekitar $2,8). Sebagian besar habis untuk "usaha berpikir" AI yang berperan sebagai pelanggan, dan ketika saya mematikannya, 3 skenario menghabiskan sekitar ¥6 (sekitar $0,04).

Tetapi suatu hari, di tengah uji, saldo pemakaian AI habis dan semuanya berhenti. Dalam satu hari saya telah memakai sekitar 35 juta token (satuan teks yang dibaca dan ditulis AI). Penyebabnya adalah menjalankan uji 221 skenario berulang kali, dan menjalankan skenario yang langsung terkait penjualan masing-masing empat kali.

Yang menakutkan adalah uji dan produksi memakai dompet yang sama. Ketika saldo habis, bahkan jendela percakapan produksi pun berhenti. Pada hari lain, kali ini saya menabrak batas bulanan yang saya tetapkan sendiri, dan jendela percakapan produksi serta AI yang membuat topik percakapan bagi pelanggan di kedai berhenti pada saat yang sama.

Bahaya sebenarnya dari anggaran pengujian bukanlah tagihannya, melainkan bahwa produksi memakai dompet yang sama.

Sejak itu aturannya berubah. Lakukan pemeriksaan yang tidak memakan biaya (uji program dan pemeriksaan layar otomatis) lebih dulu. Batasi uji yang memanggil AI pada yang berkaitan dengan hal yang diperbaiki. Jalankan uji semua kasus hanya sekali, sebelum ke produksi. Tulis perkiraan biaya dan batasnya dalam instruksi, dan berhenti jika tampaknya akan tercapai. Untuk menjaga dana bagi produksi, hentikan pengujian ketika pemakaian seluruh organisasi mendekati batas.

Ada juga pelajaran tentang bagaimana biaya membengkak. Pernah, biaya AI penilai mencapai 2,6 kali perkiraan. Penyebabnya adalah konteks awal yang panjang yang diserahkan kepada penilai setiap kali (pengetahuan dan aturan kedai) tidak dipakai ulang, sehingga biaya penulisan ulang timbul setiap kali. Ketika saya memperbaikinya agar konteks awal ditulis sekali dan dipakai ulang, biaya per percakapan turun menjadi sekitar sepertiga. Biaya AI membengkak bukan karena berapa kali Anda memanggilnya, melainkan karena berapa kali Anda menulis ulang pembukaan yang sama.

Uji penuh 221 skenario yang sama turun dari sekitar ¥1.040 (sekitar $6,9) menjadi sekitar ¥400 (sekitar $2,7) lewat perbaikan berulang. Saya mengganti AI yang berperan sebagai pelanggan dengan skrip tetap, dan membagi informasi yang diserahkan kepada AI menjadi "inti yang dikirim setiap kali" dan "bagian yang dibaca hanya bila diperlukan."

Karena keterbatasan anggaran, rancangannya bergeser ke arah memperbanyak bagian yang bisa diperiksa dengan biaya nol, yaitu bagian yang ditentukan oleh program. Hasilnya, akurasi pun naik. Uang mengubah rancangan.

【Gambar 2-2】Hasil uji AI. Tingkat lolos uji dan rincian penyebab error

### 2-3 Meminta AI Mengaudit yang Saya Bangun

#### Nama pelanggan bisa dibaca dari luar

Pada Agustus 2026, saat saya meninjau cara kerja sistem reservasi, saya menemukan sesuatu yang membuat bulu kuduk saya merinding.

Data reservasi pelanggan bisa dibaca siapa pun dari luar. Nama, nomor telepon, alamat email, kolom permintaan. Semua yang dimasukkan ke dalam reservasi bisa ditarik seluruhnya, tanpa autentikasi.

Ada hal yang harus saya katakan dengan jujur. Memang benar data itu bisa dibaca dari luar. Pada saat itu, lalu lintas situs reservasi sangat sedikit, dan saya yakin kecil kemungkinan ada yang benar-benar membacanya. Tetapi saya tidak punya catatan yang bisa membuktikan bahwa data itu tidak dibaca. "Bisa saja diambil" dan "benar-benar diambil" adalah dua hal berbeda, tetapi yang pertama saja sudah merupakan kelalaian serius bagi sebuah kedai.

Ketika saya menelusuri penyebabnya, semuanya berpangkal pada cara formulir reservasi dibuat. Untuk menghitung kursi kosong, formulir memuat data reservasi 35 hari langsung dari layar. Jika data bisa dibaca langsung dari layar, berarti siapa pun yang memahami cara layar semacam itu dibuat juga bisa membaca data yang sama. Itu hasil dari fondasi pertama yang dibangun secara spontan, yang mencapai tujuan "tampilkan kursi kosong" lewat jalan terpendek.

Saya juga menemukan bahwa alamat email untuk memberi tahu administrator kedai bersifat publik, dan bahwa siapa pun bisa menulis ke tempat penyimpanan terjemahan, yang berarti data bisa dirusak atau biaya digelembungkan.

Urutan perbaikan itu penting. Jika saya melarang pembacaan sekaligus, formulir reservasi tak lagi bisa menampilkan kursi kosong dan akan berhenti bekerja. Maka pertama-tama saya memindahkan perhitungan kursi kosong ke endpoint di sisi server. Berikutnya saya mengubah layar reservasi selesai agar server juga hanya mengembalikan informasi yang diperlukan. Terakhir, saya menutup pembacaan dari luar. Saya melakukan perbaikan dalam empat tahap dengan urutan ini dan menerapkannya ke produksi.

Setelah perbaikan, saya memakai mesin untuk memeriksa bahwa ia benar-benar tertutup. Saya menyiapkan uji yang mencoba membaca data reservasi tanpa autentikasi, dan menjalankannya secara otomatis setiap kali ada perubahan untuk memastikan ia selalu ditolak. Saya tidak memperbaikinya sekali lalu menganggapnya selesai. Saya mengaturnya agar sebuah pemeriksaan terus berjaga memastikan ia tak pernah terbuka lagi.

#### Data pelanggan sungguhan tertinggal dalam riwayat pengembangan

Kemudian saya meminta AI mengaudit seluruh repositori (tempat penyimpanan program), dan muncul masalah yang lebih serius.

Selama pengembangan, sebuah file berisi data pelanggan sungguhan (alamat email dan nomor telepon dari 55 reservasi) telah terkirim ke repositori, masih termasuk dalam riwayat perubahan program. Repositori itu bersifat privat, tetapi karena tetap ada dalam catatan, saya tidak bisa membiarkannya.

Saya menghapus file itu dari seluruh riwayat perubahan, menulis ulang riwayatnya, dan menyimpannya lagi. Meski begitu, catatan lama sebelum penulisan ulang mungkin masih tersisa di pihak GitHub, yang menampung repositori. Maka saya meminta dukungan GitHub menghapusnya, dan memastikan itu sudah dilakukan.

Audit juga menemukan masalah lain: endpoint terjemahan bisa dipakai tanpa autentikasi, login administrator bisa diserang dengan brute force, dan ada rentang waktu di mana, jika pembayaran diaktifkan kembali, sebuah reservasi bisa dikonfirmasi padahal belum dibayar. Saya memperbaikinya satu per satu, dimulai dari yang paling serius.

#### Sama sekali tidak ada uji otomatis

Audit mengungkap satu fakta lagi. Sistem reservasi tidak punya satu pun uji otomatis.

Uji otomatis adalah mekanisme di mana mesin secara otomatis memeriksa apakah program bekerja dengan benar. Tanpa uji, ketika Anda memperbaiki sesuatu, Anda tak punya cara memeriksa apakah sesuatu yang lain rusak. Setiap kali Anda menambah fitur, di suatu tempat sesuatu diam-diam rusak. Itulah persis keadaan pada masa saya membangun secara spontan.

Maka saya membangun ulang fondasi pengujian dari nol. Saya memperkenalkan sistem (CI) yang secara otomatis menjalankan empat pemeriksaan setiap kali ada perubahan: pemeriksaan tipe, pemeriksaan gaya, uji, dan build. Keputusan penting seperti perhitungan harga, penilaian reservasi, penautan anggota, dan penerbitan kupon dipisahkan dari program layar agar bisa diverifikasi sendiri-sendiri. Aturan membaca dan menulis basis data juga diperiksa di lingkungan uji yang meniru basis data sungguhan. Uji unit dimulai dari 275 dan kemudian bertambah melampaui 500.

Ada satu syarat yang selalu saya terapkan pada uji: "rusakkan, dan pastikan ia gagal." Bahkan ketika sebuah uji menjadi hijau (lulus), Anda tidak tahu apakah uji itu benar-benar bisa menangkap masalah. Hanya setelah saya sengaja merusak program dan memastikan uji itu menjadi merah (gagal) barulah saya mempercayai ujinya. Itu karena uji yang ditulis AI kadang tidak memeriksa apa pun sama sekali.

#### Delapan celah pada formulir reservasi

Setelah fondasi pengujian terpasang, saya meminta AI memeriksa lagi seluruh alur reservasi. Ia menemukan delapan masalah yang merugikan secara nyata.

Yang paling serius adalah menekan tombol kirim berulang kali membuat reservasi ganda. Ini benar-benar terjadi di produksi. Saya memperbaikinya dengan mekanisme yang memproses tindakan yang sama hanya sekali meski tiba dua kali (idempotensi). Masalah lainnya adalah ini: reservasi tidak bisa dikonfirmasi jika informasi tentang item menu yang dihapus masih tersisa; ada celah pada pemeriksaan kursi penuh yang menyisakan ruang untuk melebihi kapasitas; tak ada yang menyadari ketika email konfirmasi gagal terkirim; input tidak divalidasi di sisi server; pesan internal sistem muncul di layar saat terjadi error; teks pada kolom input begitu kecil sehingga layar memperbesar dengan sendirinya di iPhone; dan pengisian otomatis untuk input tidak berfungsi.

Untuk kegagalan email, saya membuatnya bisa dideteksi di layar admin dan dikirim ulang. Selama penyelidikan itu, saya juga menemukan bahwa log audit yang mencatat konfirmasi reservasi telah gagal setiap kali, sejak jauh sebelum perbaikan, dan tidak mencatat apa pun.

Saya memperbaikinya satu per satu dan menerapkannya ke produksi.

#### Jangan pernah melewatkan verifikasi kode yang ditulis AI

Yang saya pelajari dari pengalaman ini adalah bahwa justru karena sebuah program ditulis AI, Anda tidak boleh melewatkan verifikasi.

AI dengan cepat memberi bentuk pada apa yang dikatakan kepadanya. Tetapi pertimbangan terhadap hal yang tidak dikatakan kepadanya, seperti "buat agar tak bisa dibaca dari luar" atau "perlakukan pengiriman ganda sebagai satu," tidak masuk kecuali Anda menginstruksikannya. Dan celah-celah seperti ini tersembunyi diam-diam di dalam program yang tampak berfungsi.

Orang tidak perlu membaca semua kodenya. Ketepatan program diawasi oleh pemeriksaan mesin dan oleh audit AI lain. Apakah hasilnya sesuai dengan tujuan kedai diawasi oleh pemilik. Anda tak perlu membacanya, tetapi tak boleh melewatkan verifikasi. Itulah yang saya yakini sebagai arti membangun dengan AI jenis agen.

【Gambar 2-3】Aturan ketika bisa dibaca dari luar, dan aturan setelah perbaikan (kutipan) *(Layar dalam bahasa Jepang.)*

### 2-4 Membangun Secara Spontan Melipatgandakan Kontradiksi

Semakin banyak fitur yang saya tambahkan, semakin banyak bagian yang bentrok dengan apa yang saya putuskan sebelumnya.

Kasus yang khas adalah perhitungan diskon. Pada formulir reservasi, layar konfirmasi, email, dan layar admin, perhitungan diskon ditulis terpisah di setiap tempat. Jika saya mengubah satu aturan diskon di satu tempat, tempat lain terus menghitung dengan aturan lama. Untuk reservasi yang sama, layar dan email bisa menampilkan jumlah yang berbeda.

Belakangan, saya mengumpulkan perhitungan harga ke dalam satu file. Formulir reservasi, jendela obrolan, dan server MCP semuanya menghasilkan harga dari sana.

Aturan penggabungan diskon juga berubah di tengah jalan. Seperti yang saya tulis di Bab 1, happy hour semula akan bisa digabung dengan diskon lain, tetapi saya mendapati bahwa itu tidak akan menghasilkan laba dan mengubahnya menjadi tidak bisa digabung. Setiap kali aturan berubah, seseorang harus ingat di mana harus memperbaiki. Itulah kelemahan sistem yang dibangun secara spontan.

Ada juga ketidakcocokan antara lingkungan uji dan produksi. Saat menguji jendela obrolan, sebuah pertanyaan, "Bukankah ada semacam diskon 10%?", mengungkap bahwa aturan diskon di lingkungan uji telah menyimpang dari produksi. Jika nilai di lingkungan uji berbeda dari produksi, Anda bisa lulus uji dan tetap salah di produksi. Yang saya putuskan saat itu adalah prinsip bahwa "data dan pengaturan di lingkungan produksi adalah acuan yang benar." Sejak itu, sebelum setiap uji dijalankan, saya menyalin pengaturan produksi ke lingkungan uji dan memastikan ketidakcocokannya nol sebelum menjalankannya.

AI membangun apa yang dikatakan kepadanya. Tetapi ia tidak menyadari kontradiksi dengan keputusan sebelumnya. Yang mencegah kontradiksi bukan AI. Melainkan memutuskan segalanya terlebih dulu.

### 2-5 Mempelajari Ulang Definisi Persyaratan

Setelah merenungkan sistem reservasi yang saya bangun secara spontan, saya mempelajari ulang definisi persyaratan. Definisi persyaratan berarti memutuskan, sebelum Anda membangun, apa yang akan Anda bangun, apa yang tidak akan Anda bangun, dan siapa yang akan memakainya dan bagaimana, lalu menuliskannya dalam dokumen.

Itu sesuatu yang saya lakukan sebagai hal biasa pada masa saya menjadi insinyur sistem. Tetapi begitu saya bisa membangun dengan AI, saya melewatkannya tanpa sadar. Sampaikan sebuah ide dan sesuatu yang berfungsi muncul dalam hitungan menit. Dalam kecepatan itu, saya telah memangkas usaha untuk memutuskan.

Cara membangun saya sekarang terdiri dari tiga tahap.

1. Pertama, putuskan persyaratan secara rinci. Apa yang dibangun, apa yang tidak dibangun, siapa yang memakainya. Perilaku setiap layar. Cara menangani pengecualian (error, penekanan ganda, kedaluwarsa). Aturan yang mudah saling bertentangan di kemudian hari, seperti harga dan diskon, saya putuskan dengan sangat rinci. Pekerjaan ini pun saya lakukan lewat dialog dengan AI obrolan. Saya meminta AI menemukan lubang dan kontradiksi di muka, dan pemiliklah yang memutuskan.
2. Tulis apa yang diputuskan sebagai "dokumen persyaratan." Bukan instruksi lisan atau sesaat, melainkan dikumpulkan dalam satu dokumen. Inilah satu-satunya standar untuk memeriksa belakangan apa yang benar.
3. Serahkan seluruh dokumen kepada AI dan minta ia mengimplementasikannya. Saya memberikan seluruh dokumen kepada AI yang menulis program (Claude Code), bersama syarat kelulusan (semua uji lulus, periksa di lingkungan uji sebelum produksi, dan seterusnya). AI membangun sendiri sampai memenuhi syarat itu, dan memeriksa sendiri. Pemilik hanya melihat ketika ia berhenti di tengah jalan dan pada pemeriksaan akhir.

Misalnya, dokumen persyaratan untuk jendela obrolan "T-AI-MURO" ditulis ulang dari versi pertama hingga versi ketiga. Pada versi kedua saya memutuskan "jangan biarkan AI menghitung harga," "taruh pengetahuan kedai dan perhitungan harga dalam satu jendela," dan "pertahankan juga formulirnya, untuk orang yang tidak ingin memesan lewat obrolan." Pada versi ketiga saya memutuskan "di mana menyimpan salinan induk pengetahuan kedai," "hanya jendela ini yang menampilkan slot kosong," "jadikan pertukaran pertama pertanyaan empat pilihan," dan "jangan simpan log percakapan; simpan hanya pertanyaan yang tidak bisa dijawab." Karena keputusan tersimpan dalam dokumen, belakangan saya bisa menelusuri mengapa segalanya seperti itu.

Dengan cara membangun ini, bahkan ketika saya menambah fitur, saya bisa segera menyadari kontradiksi dengan memeriksa terhadap dokumen. Justru di zaman ketika AI yang membangun, "kekuatan memutuskan" sebelum membangun diperlukan. Itulah pelajaran terbesar yang saya dapat dari sistem reservasi.

Saya juga membangun mekanisme yang memasukkan prosedur itu sendiri ke dalam dokumen dan menyerahkannya kepada AI, sehingga cara membangun ini bisa dijalankan dengan cara yang sama setiap kali saya meluncurkan produk baru. Saya akan menulis tentang itu di Bab 4.

【Gambar 2-4】Daftar isi dokumen persyaratan T-AI-MURO (versi 3) *(Layar dalam bahasa Jepang.)*

### 2-6 Mempelajari Bahasa UI

Ada satu hal lagi yang saya pelajari ulang: nama komponen layar.

Bahkan ketika saya berkata kepada AI "lakukan ini di sini," layar sering tidak keluar seperti yang saya harapkan. Ketika saya memikirkan penyebabnya, saya mendapati bahwa saya tidak tahu nama komponen layar. Meski saya menggambarkan "jendela kecil yang muncul di atas" atau "pemberitahuan yang hilang dalam beberapa detik," sulit bagi AI untuk tahu maksud saya.

Maka saya membaca buku acuan tentang UI (user interface, tampilan dan pengoperasian layar) dan mempelajari nama komponen serta istilah teknis desain.

| Komponen | Apa itu |
| --- | --- |
| Modal | Jendela kecil yang muncul di atas layar. Anda tak bisa mengoperasikan layar di belakangnya sampai menutupnya |
| Toast | Pemberitahuan yang muncul di tepi layar selama beberapa detik dan hilang sendiri |
| Tab | Mekanisme di mana menekan sebuah judul mengganti isinya |
| Akordeon | Mekanisme di mana menekan sebuah judul membuka dan menutup isinya |
| Drawer | Menu yang meluncur keluar dari sisi layar seperti laci |
| Lainnya | Breadcrumb (jejak yang menunjukkan di mana Anda sekarang), carousel (item yang digulir ke samping), bottom sheet (panel yang naik dari dasar layar), dan sebagainya. Setiap nama yang Anda pelajari memungkinkan Anda menginstruksikan AI dalam satu frasa |

Ketika Anda berkomunikasi dengan nama, layar yang dihasilkan AI mendekati yang diinginkan dalam sekali coba. Jika Anda berkata, "Tampilkan layar konfirmasi reservasi sebagai modal," AI tidak ragu.

#### AI berayun ke ekstrem antara menambah dan memotong

Bahkan setelah saya mempelajari kata-katanya, membangun layar dengan AI punya jenis kesulitan yang berbeda. AI berayun jauh.

Ketika saya meminta header yang "bergaya" untuk situs reservasi, saya mendapat header tebal yang mengesankan. Tetapi inti situs reservasi adalah reservasi. Bagi pelanggan tetap yang memesan setiap kali, header tebal dengan penjelasan panjang hanyalah gangguan. Saya memintanya memangkas tingginya sekitar separuh, dengan jumlah informasi yang sama.

Ketika saya menyeragamkan footer email dan menambahkan tautan ke Buku Lanjutan (panduan tempat singgah berikutnya), teks isi kini terasa terlalu polos dan kurang menarik jika dibandingkan. Maka saya menambahkan judul, tabel poin penting, dan satu tombol untuk ditekan pada isi email juga. Ketika saya menambahkan pintu masuk ke jendela obrolan di footer, tampilannya ramai. Ketika saya memadatkannya menjadi dua baris tautan yang dipisahkan garis, rapi tetapi tidak mencolok. Pada akhirnya ia berakhir pada dua kartu yang menunjukkan peran menurut "kapan dipakai." Yang kiri "untuk reservasi Anda berikutnya," yang kanan "setelah makan."

Terlalu tebal, terlalu dipangkas, terlalu mencolok. Yang menentukan titik yang tepat adalah kata-kata pemilik setiap kali.

#### Usulan desain tanpa gambar

Ini juga terjadi. Saya meminta AI yang menulis program membuat usulan perbaikan untuk jendela obrolan memakai AI desain (Claude Design), dan sebuah laporan kembali yang berkata, "Saya membuat usulan untuk delapan layar." Tetapi ketika saya membukanya, hanya ada deskripsi teks. AI tidak mampu menggambar, namun hanya laporan "selesai" yang tertinggal.

Pada akhirnya, AI di sisi obrolan menggambar empat usulan langsung di layar desain. Ia mengambil warna layar saat ini dari tangkapan layar, menaruh sejarah kedai dalam lini masa, membagi pemberian rasa menjadi dua bingkai, "cara memasak" dan "rasa," menjadikan paket kartu penjelasan, dan menyatukan harga menjadi ringkasan reservasi.

Ketika Anda meminta AI menjalankan uji, ia berkata "lulus." Ketika Anda meminta AI membuat desain, ia berkata "selesai." Memeriksa isinya adalah tugas manusia. Standar untuk menilai adalah sesuatu yang hanya manusia yang bisa terus memegangnya.

#### Poin penting dari bab ini

- Membangun sesuatu yang berfungsi dan mampu menjalankannya dengan aman adalah dua hal berbeda.
- Periksa keluaran AI bukan dengan kata-kata AI, tetapi dengan uji. Sebuah uji hanya bisa dipercaya setelah Anda memeriksa bahwa ia gagal ketika Anda merusak sesuatu.
- Perhitungan yang tidak boleh salah, seperti harga, jangan diserahkan kepada pembuatan teks oleh AI. Berikan kepada program.

Kelanjutan bab ini (lubang yang baru ditemukan dan langkah yang saya ambil untuk memperbaikinya) ada di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Bab 3: Membagikan Alat Kedai Saya kepada Kedai Lain

### 3-1 Papan Hijau Kecil di Halaman Reservasi

Buka halaman reservasi Tamuro dan Anda akan melihat papan hijau kecil di dekat bagian atas. Selama kedai buka, tertulis "OPEN," dan ketika tutup, tertulis "CLOSED." Ketika pemilik menekan tombol perpanjang, jam tutup mundur 30 menit dan semburat warna merah jingga muncul di papan itu.

Restoran mandiri memiliki satu kesamaan. Mereka buka hampir tepat waktu, tetapi jam tutupnya sering molor. Jika obrolan dengan pelanggan sedang seru, lampu kedai tetap menyala melewati last order pukul 22.30.

Tetapi dari sisi pelanggan, itu tidak terlihat. Tampilan "Buka" di Google Maps hanya didasarkan pada jam yang terdaftar, sehingga tidak mencerminkan perpanjangan, penutupan lebih awal, maupun penutupan sementara. Tak ada yang sengaja mendatangi sebuah kedai yang sudah lewat jam tutupnya sambil berpikir, "Mungkin masih buka." Menelepon untuk memastikan pun terasa sungkan.

Papan ini adalah alat yang menjawab "Apakah masih buka?" itu. Namanya "AgendaLuce (Buku Lentera)." Luce berarti "cahaya" dalam bahasa Italia.

Buku Lentera dirancang agar bisa berjalan hampir tanpa perlu diutak-atik pemilik. Cukup daftarkan sekali saja jam buka dan tutup untuk setiap hari dalam seminggu, dan papan menyala dan mati secara otomatis. Pemilik menyentuhnya hanya ketika memperpanjang, menutup lebih awal, atau libur. Untuk memperpanjang, Anda menekan satu tombol di ponsel. Staf juga bisa mengoperasikannya dari tautan khusus yang bekerja tanpa login.

Pelanggan tidak memerlukan login atau pendaftaran. Buka halaman publik dan Anda bisa melihat status buka-tutup (lampu) kedai saat ini. Jika Anda menambahkannya ke layar utama ponsel, ia bekerja seperti aplikasi. Komponen papan kecil itu juga bisa disematkan di situs web lain. Yang muncul di halaman reservasi Tamuro adalah komponen itu.

Buku Lentera gratis. Jika Anda hanya menyematkan widget papan di situs web Anda, penyiapannya memakan sekitar 10 menit.

Dan inilah bagian pentingnya. Buku Lentera ini bukan hanya untuk Tamuro. Kedai mana pun bisa memakainya.

Saya dengan sengaja tidak memasukkan nama kedai dalam desain papan. Jika saya menaruh nama, ia menjadi papan untuk Tamuro. Anda juga bisa memilih bahasa tampilan. Saya membuat komponennya kecil agar bisa disematkan di situs web kedai mana pun.

Sebuah alat yang lahir dari masalah Tamuro "penutupan molor," dibuat sejak awal dalam bentuk yang bisa dipakai siapa pun. Itulah Buku Lentera. Dan kumpulan alat sejenisnya adalah "seri Agenda."

【Gambar 3-1a】Papan Buku Lentera di atas halaman reservasi (buka) *(Layar dalam bahasa Jepang.)*

【Gambar 3-1b】Semburat warna merah jingga muncul saat perpanjangan *(Layar dalam bahasa Jepang.)*

【Gambar 3-6a】Layar pemilik. Untuk memperpanjang, tekan tombol sekali *(Layar dalam bahasa Jepang.)*

【Gambar 3-6b】Tepat setelah menekan perpanjang. Jam tutup mundur 30 menit *(Layar dalam bahasa Jepang.)*

【Gambar 3-6c】Halaman publik yang dilihat pelanggan (saat perpanjangan) *(Layar dalam bahasa Jepang.)*

### 3-2 Semuanya Bermula dari Buku Catatan Kulit Hitam

Seri Agenda tidak direncanakan sebagai sebuah seri. Ia bermula dari satu sistem, yang bahkan belum dirilis.

Yang pertama kali saya coba bangun adalah mekanisme yang mengenali wajah pelanggan dan menyambut pelanggan tetap. Sebuah kamera di pintu masuk kedai membedakan pengunjung dari wajah dan memberi tahu pemilik: "Itu orang yang dulu makan tonteki, yang sudah tiga bulan tidak kita lihat." Saya bermaksud meminta mesin membantu pekerjaan yang dilakukan pemilik kedai kecil di kepalanya: mengingat wajah, nama, dan preferensi.

Tetapi tak lama setelah mulai membangun, saya menyadari ini adalah sistem yang dipercayakan sesuatu yang sangat berat. Wajah. Atribut. Riwayat kunjungan. Karakter seorang pelanggan. Semuanya adalah informasi yang tak bisa ditarik kembali begitu bocor.

Yang terlintas di benak saya saat itu adalah "Buku Catatan Kulit Hitam" karya Seicho Matsumoto. Catatan yang tak ditunjukkan kepada siapa pun, namun pasti ada. Sebuah buku catatan yang, begitu dibuka, menggerakkan hidup dan mati orang. Bukankah itu persis yang sedang saya coba bangun?

Dalam bahasa Italia, "buku catatan" adalah Agenda, dan "hitam" adalah Nera. Digabung: AgendaNera. Buku catatan kulit hitam. Begitulah nama itu diputuskan lebih dulu.

AgendaNera masih dalam pembangunan. Di antara seluruh seri, inilah yang saya bangun dengan paling hati-hati.

Dan penamaan ini menjadi pemicunya. Jika ada buku catatan hitam, bisa ada buku catatan warna lain. Saya akan membangun ulang mekanisme yang saya pakai setiap hari di kedai saya sendiri menjadi bentuk yang bisa dipakai kedai mana pun, dan merilisnya satu per satu sebagai buku catatan. Itulah [seri Agenda](https://bontallc.com/agenda?via=b2-id-{{FMT}}).

### 3-3 Menambah Buku Catatan, Satu per Satu

Seri Agenda adalah kumpulan aplikasi web kecil, masing-masing menjawab satu masalah restoran dengan satu alat. Masing-masing punya nama Italia dan sebutan Jepang yang memakai kata "buku catatan" (techō). Setiap nama punya asal-usulnya sendiri.

| Nama | Sebutan | Asal-usul nama | Fungsinya |
| --- | --- | --- | --- |
| AgendaTimbro | Buku Absensi | Timbro berarti "stempel." Itulah pencatatan jam masuk itu sendiri | Mencatat jam masuk dan jam pulang staf |
| AgendaOro | Buku Laba Rugi | Oro berarti "emas." Buku catatan uang | Memperkirakan keuntungan untuk membuka kedai atau menu baru (gratis) |
| AgendaBis | Buku Lanjutan | Bis berarti "encore." "Bis!" yang diteriakkan dari kursi penonton dalam konser | Mengarahkan pelanggan ke tempat berikutnya di sekitar (gratis) |
| AgendaQA | Buku Bantuan | Qua berarti "di sini." Saat kesulitan, di sini | Layanan bantuan bersama seri ini (gratis) |
| AgendaLuce | Buku Lentera | Luce berarti "cahaya" | Menunjukkan apakah kedai buka (gratis) |
| AgendaRicetta | Buku Biaya Resep | Ricetta berarti "resep" | Menghitung biaya dan rasio biaya sebuah resep (gratis) |
| AgendaNera | Buku Pelanggan Tetap | Nera berarti "hitam." Buku catatan kulit hitam | Menyambut pelanggan tetap dengan pengenalan wajah (dalam pembangunan) |
| AgendaTurno | Buku Giliran Kerja | Turno dalam bahasa Italia berarti "giliran" atau "tugas jaga" | Mengumpulkan permintaan shift staf dan membagikan jadwal yang disusun AI milik pemilik sendiri (segera hadir) |

Buku catatan mana yang cocok untuk kedai seperti apa? Buku Absensi untuk kedai dengan dua staf atau lebih yang mengelola kehadiran di kertas atau di LINE *(aplikasi pesan yang paling banyak dipakai di Jepang)*. Buku Laba Rugi untuk orang yang akan membuka kedai, dan mereka yang ingin meninjau angkanya karena sewa atau biaya berubah. Buku Lanjutan untuk kedai yang berpusat pada makan dan ingin lebih awal mengarahkan pelanggan ke tempat berikutnya. Buku Lentera untuk kedai mandiri yang jam tutupnya lebih lambat atau lebih awal dari rencana. Buku Biaya Resep untuk kedai yang resepnya ada di kepala tetapi belum pernah menghitung rasio biaya.

#### Buku Absensi tidak menghitung gaji

Buku Absensi mengubah tablet kedai atau ponsel staf apa adanya menjadi mesin absen. Cukup ketuk nama Anda. Lembar kehadiran dijumlahkan otomatis dan bisa diekspor sebagai CSV (format yang bisa dibuka di perangkat lunak spreadsheet). Hari kerja dimulai pukul 5 pagi, sehingga bahkan dengan jam larut malam, tanggalnya tidak berganti.

Tetapi Buku Absensi ini dengan sengaja tidak menghitung gaji.

Upah per jam, tunjangan, dan tanggal penutupan perhitungan gaji terlalu berbeda dari kedai ke kedai. Larut malam dengan tambahan 25%, hari libur sebagai kategori tersendiri, transportasi dengan jumlah harian. Bagaimanapun saya membuatnya, pasti ada saja kedai yang tidak cocok dengannya.

Maka alih-alih menghitung, saya menyiapkan "templat instruksi untuk diserahkan kepada AI." Pemilik menempelkan CSV kehadiran yang diunduh dan templat ini, apa adanya, ke AI mana pun yang biasa ia pakai, entah ChatGPT, Claude, atau Gemini. Lalu AI menghitung tambahan larut malam, upah hari libur, dan transportasi lalu merangkumnya dalam bentuk daftar. Aturan setiap kedai, seperti "kami tutup buku di akhir bulan, larut malam tambah 25%, dan hari Minggu kategori tersendiri," bisa ditambahkan ke templat dan akan tercermin apa adanya. CSV menyertakan kolom hari dalam seminggu dan nama hari libur agar AI dapat menghitung dengan benar.

Saya sendiri tidak memegang mekanisme perhitungannya; setiap kedai menyimpan aturannya sendiri di tangannya sendiri. Saya mengira itulah cara yang paling sulit rusak.

#### Arahkan ke tempat berikutnya, dan biarkan kedai Anda tertinggal dalam ingatan mereka

Buku Lanjutan adalah alat untuk membuat "halaman panduan tempat berikutnya" yang diberikan kepada pelanggan. Kepada pelanggan yang telah selesai makan, ia mengarahkan ke bar di sekitar atau tempat makan penutup (misalnya kedai ramen), beserta berapa menit berjalan kaki.

Tampaknya ini alat untuk mengirim pelanggan ke tempat lain, tetapi ada trik kecil di dalamnya. Mengarahkan seseorang ke perhentian kedua menyiratkan bahwa perhentian pertamanya adalah kedai Anda. Meski sekilas tampak mengarahkan pelanggan ke tempat lain, sebenarnya ia mengukir "perhentian pertama adalah kedai ini" dalam ingatan mereka. Begitulah rancangannya.

#### Tiga prinsip rancangan: otomatis, meminjam tenaga, fungsi tunggal

Semua buku catatan dalam seri Agenda memiliki tiga prinsip yang sama.

Yang pertama adalah "otomatis." Ia harus berjalan tanpa pemilik menyentuhnya setiap hari. Pada Buku Lentera, begitu Anda mendaftarkan jadwal, lampu menyala dan mati sendiri. Pemilik restoran tidak punya waktu menyentuh layar saat jam sibuk melayani. Alat yang tidak bekerja kecuali Anda menyentuhnya akhirnya tidak akan dipakai.

Yang kedua adalah "meminjam tenaga." Jangan membangun semuanya sendiri; serahkan kepada alat dan AI yang sudah dipakai pemilik. Perhitungan gaji pada Buku Absensi adalah contoh teladannya. Buku shift pun sama: ia hanya menangani pengumpulan keinginan staf, dan menyerahkan pekerjaan menyusun shift kepada AI milik pemilik sendiri. Ia tidak membawa mekanisme rumit sendiri, juga tidak membawa biaya memanggil AI. Itulah sebabnya harganya bisa ditekan rendah.

Yang ketiga adalah "fungsi tunggal." Satu buku catatan hanya mengerjakan satu hal, dengan andal. Sistem multifungsi terlalu berat bagi kedai mandiri. Terus menambah fitur membuatnya makin sulit dipakai, dan kontradiksi di sisi pembangun berlipat ganda. Itulah yang saya pelajari langsung lewat sistem reservasi di Bab 2. Maka saya menambah buku catatan satu per satu, masing-masing mengerjakan "hanya satu hal ini dengan baik."

#### Mengapa sistem reservasi tidak ada dalam seri ini

Pada titik ini, saya kira wajar jika muncul sebuah pertanyaan. Yang paling banyak dikerjakan Tamuro adalah sistem reservasi. Mengapa tidak dimasukkan ke dalam seri Agenda?

Sebenarnya, saya pernah berniat begitu. Rencananya adalah menjadikan sistem reservasi dalam bentuk yang bisa dipakai restoran lain, dan merilisnya sebagai salah satu buku catatan seri. Tetapi pada Agustus 2026, saya membatalkan rencana itu.

Alasannya persis seperti yang saya tulis di Bab 1. Sistem reservasi Tamuro dipenuhi cara berbisnis Tamuro. Bahwa pelanggan yang datang sendirian membentuk separuh pelanggan. Bahwa hampir 90% reservasi dibuat pada hari yang sama. Bahwa saya ingin menjual waktu sebelum buka. Bahwa saya ingin orang datang berkelompok. Bahwa saya ingin membesarkan pelanggan tetap. Saya membangun kombinasi diskon, urutan email, dan cara jendela obrolan merekomendasikan paket semuanya untuk menyesuaikan dengan ini.

Jika saya menipiskannya menjadi sesuatu yang bisa dipakai siapa pun, ia menjadi sistem reservasi biasa yang cocok untuk setiap kedai secara pas-pasan. Maka kekuatan Tamuro akan lenyap. Sistem reservasi dan CRM mencerminkan cara kedai memasarkan dirinya sendiri. Alih-alih menyesuaikan kedai dengan sistem generik, sesuaikan sistem kedai dengan kedai. Kedai kami, dengan spesifikasi kami sendiri. Maka saya memutuskan mempertahankan sistem reservasi Tamuro hanya milik Tamuro.

Jadi apakah tidak ada yang bisa dibagikan di luar kedai? Ada. Di sekitar sistem reservasi ada banyak masalah kecil yang umum bagi setiap kedai. Pertahankan inti kedai dengan spesifikasi Anda sendiri. Bangun alat yang menyelesaikan masalah di sekelilingnya dalam bentuk yang bisa dipakai semua orang sejak awal, dan bagikan. Halaman reservasi Tamuro adalah contoh yang menjajarkan keduanya dalam satu layar. Di atas sistem reservasi khusus Tamuro, bertengger papan Buku Lentera yang bisa dipakai siapa pun.

【Gambar 3-2】Halaman pengantar seri Agenda *(Layar dalam bahasa Jepang.)*

【Gambar 3-3a】Pengantar Buku Absensi *(Layar dalam bahasa Jepang.)*

【Gambar 3-3b】Pengantar Buku Laba Rugi *(Layar dalam bahasa Jepang.)*

【Gambar 3-3c】Pengantar Buku Lanjutan *(Layar dalam bahasa Jepang.)*

【Gambar 3-4】Layar absen Buku Absensi. Cukup ketuk nama Anda (data sintetis) *(Layar dalam bahasa Jepang.)*

### 3-4 Membangun untuk Semua Orang Sejak Awal

Saya membuat alat untuk kedai saya sendiri, lalu membagikannya juga kepada kedai lain. Terdengar sederhana saat dikatakan, tetapi untuk melakukannya, cara Anda memutuskan sesuatu sebelum mulai membangun harus berubah.

Jika saya hanya membangun untuk Tamuro, cara tercepat adalah menulis jam buka Tamuro dan nama Tamuro langsung ke dalam program. Tetapi dengan begitu tak ada kedai lain yang bisa memakainya. Jika Anda mencoba menjadikannya serbaguna belakangan, Anda akhirnya harus melacak setiap bagian yang ditulis langsung di dalam kode (hardcode) dan memperbaikinya satu per satu.

Maka alat-alat dalam seri Agenda dirancang sejak awal dengan anggapan bahwa semua orang bisa memakainya. Saya mulai dari masalah di Tamuro, tetapi pada tahap persyaratan saya memisahkan dua pertanyaan: "Apakah ini hanya berlaku untuk Tamuro, atau berlaku untuk setiap kedai?" Jangan taruh nama kedai pada papan. Biarkan orang memilih bahasa. Buat agar bisa ditempel ke situs web mana pun. Keputusan seperti ini saya tetapkan sambil menulis dokumen persyaratan untuk Buku Lentera.

Ini kegunaan lain dari definisi persyaratan yang saya pelajari ulang di Bab 2. Jika Anda memutuskan hal-hal ini lebih dulu, Anda bisa memakai alat itu di Tamuro dan membagikannya apa adanya kepada kedai lain.

Masalah di kedai saya juga masalah di kedai lain. Saya bukan satu-satunya pemilik yang ingin memberi tahu pelanggan bahwa jam tutup molor. Pemilik kedai mandiri membangun alat dari masalahnya sendiri, lalu membagikannya kepada kedai lain. Itulah gagasan di balik seri Agenda.

### 3-5 Demokratisasi Teknologi

Seri Agenda kini memiliki lebih dari 10 produk. Saya membangun dan menjalankannya sendirian, sambil berdiri di balik bar.

Beberapa tahun lalu, ini tak terbayangkan. Untuk membangun satu produk, Anda memerlukan seseorang untuk merencanakan, seseorang untuk mendesain layar, seseorang untuk menulis kode, seseorang untuk menguji, dan seseorang untuk mengoperasikan. Tanpa tim dan dana, Anda tak bisa meluncurkan produk ke dunia.

Sekarang sudah tidak begitu lagi. Pemilik menyampaikan persyaratan kepada AI, AI menulis kodenya, AI mengujinya, dan AI lain mengauditnya. Yang dilakukan pemilik adalah memutuskan apa yang dibangun, menilai apakah hasil AI sesuai tujuan kedai, dan mengerjakan hanya operasi yang hanya bisa dilakukan manusia.

Perubahan semacam ini umumnya disebut "demokratisasi teknologi." Kekuatan untuk membangun tidak lagi menjadi milik segelintir orang atau perusahaan.

Tetapi izinkan saya jujur di sini. Seperti yang saya tulis di Pendahuluan, saya bekerja di bidang TI selama sekitar 16 tahun, terutama dalam perencanaan sistem dan sebagai koordinator antara orang-orang di lapangan dan vendor pengembang. Saya tahu definisi persyaratan, cara berpikir tentang basis data, dan cara menjalankan uji, semuanya dari pengalaman. Jadi saya tidak akan mengklaim bahwa orang yang belum pernah menulis satu baris kode pun bisa melakukan hal yang sama mulai besok.

Meski begitu, banyak yang telah berubah. Kini saya bisa membangun, sendirian dan di sela-sela pekerjaan utama saya, hal-hal berskala yang dulu membutuhkan tim. Dan bagi orang tanpa pengalaman, pintu masuknya pasti telah menjadi lebih rendah. AI akan mengajari Anda jika Anda bertanya tentang sesuatu yang tidak Anda pahami. Ia akan memberi bentuk pada apa yang Anda katakan dengan kata-kata. Yang kurang bukan keahlian teknis, melainkan kemampuan memutuskan apa yang dibangun dan kata-kata untuk memberi tahu AI. Itu kemampuan yang dipakai setiap hari oleh orang yang menjalankan kedai.

### 3-6 Perdebatan "Kematian SaaS"

Perangkat lunak yang dipakai orang lewat internet dengan biaya bulanan, seperti seri Agenda, disebut SaaS (Software as a Service). Perangkat lunak akuntansi, manajemen waktu dan kehadiran, manajemen reservasi. Restoran masa kini mengandalkan banyak SaaS dalam operasionalnya.

Akankah AI mengakhiri SaaS? Pada 2026, perdebatan itu ramai diperbincangkan secara luas.

Salah satu pemicunya adalah pernyataan CEO Microsoft Satya Nadella. Dalam sebuah podcast pada Desember 2024, Nadella mengatakan bahwa aplikasi SaaS akan runtuh di era agen AI. Alasannya: begitu agen AI mengambil alih bagian pengambilan keputusan dalam pekerjaan bisnis, perangkat lunak yang dibuat agar dioperasikan orang lewat layar tidak lagi diperlukan.

Lalu pada Februari 2026, Anthropic mengumumkan Claude Cowork (alat AI yang menjalankan tugas bisnis secara otonom), dan saham perusahaan perangkat lunak Amerika dijual besar-besaran. Di Wall Street, kejatuhan itu disebut "SaaSpocalypse" (kiamat SaaS). Yang ditakutkan investor adalah bahwa jika agen AI mengerjakan pekerjaan, model SaaS yang mendapat bayaran per orang (harga per kursi) akan runtuh.

Ada pula bantahan. CEO Nvidia Jensen Huang mengatakan bahwa agen AI tidak akan menggantikan perangkat lunak tetapi akan memakai perangkat lunak menggantikan manusia, dan menyebut aksi jual itu reaksi berlebihan. Tak sedikit pula yang justru memandang SaaS yang menyerap AI akan menjadi lebih kuat.

Apakah SaaS benar-benar akan mati? Inilah yang saya pikirkan.

Yang mati adalah lapisan tengah SaaS: jenis yang menarik biaya bulanan tinggi per akun pengguna (per seat) dan mengasumsikan orang mengoperasikannya lewat layar. Jika AI mengerjakan pekerjaan menggantikan orang, Anda tak perlu akun pengguna untuk setiap orang. Jika tak ada yang mengoperasikan layar, Anda tak perlu layar yang rumit.

Yang bertahan adalah alat yang murah dan mengerjakan satu hal dengan andal. Dan alat yang mudah dipakai AI.

Inilah persis tiga prinsip seri Agenda. Ia berjalan otomatis, ia diserahkan kepada AI milik pemilik (mengandalkan pihak lain), dan ia hanya mengerjakan satu hal (fungsi tunggal). AgendaTurno menyerahkan pekerjaan menyusun jadwal shift kepada AI milik pemilik, yang tepat merupakan bentuk "AI memakai perangkat lunak" seperti yang digambarkan Huang. Sistem reservasi Tamuro membuka jendela lewat MCP kepada AI milik pelanggan, dan itu gagasan yang sama.

Tentu saja, di sini mungkin tampak ada kontradiksi. Saya berbicara tentang kematian SaaS, padahal seri Agenda sendiri adalah SaaS. Tetapi seri Agenda adalah kumpulan alat yang dibuat seorang pemilik untuk kedainya sendiri lalu dibuka untuk umum dengan harga murah. Ia bukan model yang menarik biaya bulanan tinggi per akun pengguna (per seat), dan ia tidak mengasumsikan orang terpaku pada layar setiap hari. Ia dibangun sejak awal dengan anggapan bahwa AI akan memakainya.

#### "Kematian SaaS" bagi Restoran

Perdebatan ini mungkin terdengar seperti cerita tentang investor dan industri TI. Tetapi bagi restoran, hal yang sama akan terjadi dalam bentuk yang jauh lebih dekat dengan keseharian.

Banyak kedai mandiri membayar biaya bulanan kepada situs kuliner dan situs reservasi, dan selain itu masih membayar komisi rujukan untuk setiap reservasi. Sebagai imbalan mendatangkan pelanggan, situs itu memegang hubungan dengan pelanggan, dan bukan hal yang aneh jika kedai bahkan tidak punya kontak pelanggan. Jika harga naik, kedai tak punya pilihan selain mengikuti, dan jika sistem peringkat berubah, arus pelanggan berubah.

Seperti yang saya tulis di Bab 1, pada 2026 dimulailah era ketika pelanggan meminta AI mereka sendiri mencari kedai. Jika pintu masuk bergeser ke AI, seluruh tatanan membayar biaya bulanan dan komisi kepada situs agar ditempatkan tinggi dalam daftarnya mulai goyah. Jika sebuah kedai membuka jendela ke AI dengan caranya sendiri, pelanggan bisa menjangkaunya tanpa melewati situs-situs besar. Catatan reservasi dan hubungan dengan pelanggan tetap di tangan kedai.

Jika saya menuangkan "kematian SaaS" ke dalam bahasa kedai mandiri, ia adalah "berakhirnya zaman "asal membayar pasti terdaftar"." Tamuro membuka jendelanya lewat MCP, dan menjaga reservasi serta CRM-nya pada spesifikasinya sendiri, sebagai persiapan untuk itu.

Apakah SaaS akan mati, belum ada yang tahu. Tetapi bentuk alat yang akan bertahan di zaman AI perlahan mulai terlihat. Itulah yang saya pikirkan.

### 3-7 Monetisasi: Kecil, Banyak, Murah

Saya membangun seri Agenda dengan tujuan membuatnya berdiri sebagai bisnis. Tujuannya adalah menjadikannya pilar pendapatan kedua, terpisah dari restoran.

Saya menetapkan harga kecil dan rendah. Biaya bulanan mulai dari beberapa ratus yen. Buku Absensi, misalnya, ¥500 (sekitar $3,3) per bulan. Saya juga menyertakan alat gratis, seperti Buku Laba Rugi, Buku Lentera, dan Buku Biaya Resep. Alat gratis berfungsi sebagai pintu masuk bagi orang untuk mengenal seri Agenda. Buku Lentera tidak memakai API peta maupun AI generatif, jadi biaya menjalankannya hampir nol. Itulah mengapa saya bisa membagikannya gratis.

Hanya ada satu akun. Dengan akun bersama bernama AgendaID, Anda bisa memakai setiap alat dalam seri ini. Anda tak perlu mendaftar lagi untuk setiap alat. Alat berbayar dilengkapi masa gratis tiga bulan dan bisa dimulai tanpa mendaftarkan kartu. Masa gratis hanya tersedia sekali untuk setiap kombinasi kedai dan produk. Jika Anda mengajak kedai lain, Anda mendapat bonus.

Alasan saya bisa menjaga harga tetap rendah ada pada cara saya membangun. Saya membangun sendirian, saya meminta AI membangun, dan saya memakai ulang fondasi bersama. Biaya basis data ditekan hingga sekitar $35 per bulan untuk seluruh seri. Jika biaya membangun dan biaya menjalankan sama-sama kecil, bisnis bisa berdiri bahkan dengan penjualan kecil.

Izinkan saya jujur. Saat saya menulis buku ini, sebagian kedai telah mencoba alat-alat itu, tetapi hampir tak ada pendaftaran berbayar. Sistem untuk membangun sudah ada, tetapi cara agar dikenal masih menjadi tugas ke depan. Buku ini juga merupakan salah satu sarana untuk tujuan tersebut, yaitu agar lebih dikenal.

#### Membangun Sesuatu dan Membuat Orang Terus Memakainya adalah Dua Hal Berbeda

Izinkan saya jujur tentang satu hal lagi. Mampu membangun sebuah alat dan membuat seseorang terus memakainya adalah dua perkara yang terpisah.

Membangun menjadi lebih cepat berkat AI. Tetapi membuat orang terus memakainya memerlukan pekerjaan lain. Menjawab pertanyaan tentang cara memakainya (Buku Bantuan ada untuk ini). Mengirim pemberitahuan sebelum masa gratis berakhir. Menjelaskan alasan ketika menaikkan harga. Menghapus data dengan benar ketika seseorang meminta berhenti. Dan di atas semuanya, menjaganya tetap berjalan tanpa pemilik menyentuhnya.

Dari tiga prinsip seri Agenda, "otomatis" adalah prinsip untuk "membuat orang terus memakai" ini. Alat yang tidak bekerja kecuali pemilik menyentuhnya setiap hari akhirnya akan dihentikan langganannya. Ia belum selesai hanya karena sudah dibangun. Ia menjadi bisnis hanya ketika terus dipakai. Menambah, satu per satu, kedai yang terus memakainya: itulah tugas saya setelah menerbitkan buku ini.

#### Jika Anda Ingin Memulai di Kedai Anda Sendiri

Bagi Anda yang membaca buku ini dan ingin mencobanya di kedai sendiri, ada tiga langkah.

1. Buka https://bontallc.com/agenda?via=b2-id-{{FMT}} dan login dengan akun Google (AgendaID akan dibuat. Tidak perlu mendaftarkan kartu)
2. Pertama, tambahkan satu buku catatan gratis. Saya menyarankan Buku Lentera. Anda hanya menempelkan widget papan ke situs web Anda, dan ia bekerja dalam 10 menit. Jika Anda belum membuka usaha, cobalah Buku Laba Rugi
3. Jika tampaknya cocok, cobalah Buku Absensi gratis selama tiga bulan. Pemberitahuan tiba menjelang tenggat, sehingga Anda tidak akan ditagih bahkan jika membiarkannya begitu saja

Jika Anda punya pertanyaan, tanyakan lewat Buku Bantuan (AgendaQA). AI menjawab pertanyaan pengoperasian seketika, dan saya sendiri membaca pertanyaan tentang spesifikasi dan bug.

Penjualan restoran bergantung pada cuaca dan musim. Jumlah kursi dan jam buka sama-sama punya batas. Penjualan alat, di sisi lain, tak punya batas jumlah tempat duduk seperti restoran. Menjalankan kedai sambil membagikan alat yang lahir dari masalah kedai Anda sendiri, dan perlahan menjadikannya sumber pendapatan: saya yakin ini bisa menjadi satu cara lagi bagi kedai mandiri untuk menghasilkan uang.

#### Tetap Menjadi Perusahaan Kecil, Menuju Global

Ada satu hal lagi yang saya putuskan tentang seri Agenda sejak awal. Saya tidak akan membangunnya hanya dalam bahasa Jepang.

Buku Absensi, Buku Laba Rugi, dan Buku Bantuan semuanya bisa dipakai dalam 20 bahasa. Teks layar dan pertanyaan yang sering diajukan, semuanya. Sebuah alat yang dibuat untuk bar 19 kursi di Tokyo bekerja dengan cara yang sama dalam bahasa Inggris, bahasa Korea, bahasa Vietnam.

Ada dua alasan. Yang pertama adalah bahwa masalah restoran tidak berubah ketika negaranya berubah. Anda ingin mencatat kapan staf datang dan pergi. Anda ingin tahu keuntungan Anda sebelum buka. Anda ingin memberi tahu pelanggan bahwa jam tutup telah diperpanjang. Semua ini adalah masalah yang dimiliki bersama oleh kedai mandiri di seluruh dunia. Yang lainnya adalah bahwa jumlah kedai mandiri di Jepang terus menurun. Jika saya hanya melayani pasar berbahasa Jepang, penjualan alat akan punya batas atas.

Dulu, agar perusahaan kecil menjual produk ke luar negeri, ia memerlukan agen lokal, perusahaan penerjemah, dan badan hukum. Sekarang AI membantu penerjemahan dan penyuntingan. Sistem pembayaran yang sama dapat dipakai di seluruh dunia. Untuk pengiriman, Anda hanya memerlukan server, dan tidak ada stok atau gudang di setiap negara. Sebuah alat yang dibuat seorang pemilik bisa berada di rak dunia dalam 20 bahasa sehari setelah dibuat. Dulu, hanya perusahaan besar yang bisa melakukan itu.

Perusahaan yang sangat kecil yang sejak awal berbisnis dengan banyak negara: perusahaan semacam itu kadang disebut micro-multinational (perusahaan multinasional mikro). Bonta LLC membidik tepat itu, dengan satu kedai di Higashi-Nakano dan satu pemilik.

Tentu saja, menerjemahkan ke 20 bahasa tidak berarti pemilik di luar negeri akan langsung mulai memakainya. Sebagian terjemahan masih menunggu tinjauan penutur asli agar terdengar alami. Meski begitu, dengan menyingkirkan hambatan bahasa sejak awal, batas atas jangkauan alat-alat ini lenyap, seperti halnya batas kursi.

Bagaimana saya membangun fondasi itu adalah kisah Bab 4.

【Gambar 3-5】Pergantian bahasa pada Buku Bantuan. 20 bahasa terdaftar *(Layar dalam bahasa Jepang.)*

## Bab 4: Teknologi - Sistem untuk Membangun Produk Seorang Diri, Terus-Menerus

Poin-poin penting bab ini

- Saya menjadikan prosedur peluncuran produk baru sebuah dokumen, dalam bentuk (sebuah skill) yang bisa dibaca dan dijalankan AI. Yang dilakukan manusia hanyalah penilaian dan operasi yang hanya bisa dilakukan manusia
- Bagian bersama, seperti login, penagihan, halaman pengantar, dan panduan ke produk lain, dibangun sekali dan dipakai ulang di semua produk. Biaya basis data fondasi itu sekitar $35 per bulan
- Sistemnya masih terus dikembangkan. Saya terus menambahkan kegagalan ke dokumen prosedur, seperti rancangan yang ditolak lima kali berturut-turut

(Ini bab dengan banyak istilah teknis. Jika Anda tidak tertarik pada teknologinya, Anda bisa melompat ke Bab 5 dan ceritanya tetap tersambung.)

### 4-1 ProductBootstrap: Menyerahkan Prosedur Peluncuran Itu Sendiri kepada AI

Setiap kali saya membangun produk, saya mengulang persiapan yang sama dan kesalahan yang sama. Membuat repositori (gudang untuk program). Menyambungkan login. Menentukan warna desain. Menyiapkan sistem pengujian. Menyiapkan lingkungan produksi. Padahal semuanya sudah pernah saya lakukan untuk produk sebelumnya, tetapi saya lupa rinciannya dan tersandung di tempat yang sama.

Maka saya menjadikan prosedur peluncuran produk baru sebuah dokumen. Bentuk dokumen itu yang bisa dibaca dan dijalankan AI yang menulis kode (Claude Code) saya sebut sebuah "skill." Nama skill ini adalah ProductBootstrap. "Bootstrap" adalah istilah umum di dunia komputer untuk memulai sendiri dari mekanisme minimal, dan saya menerapkannya pada peluncuran produk.

Saya tidak menyimpan program templat. Saya menyalin produk yang paling baru selesai dan memulai produk baru darinya. Dengan begitu, pelajaran terbaru otomatis diteruskan ke produk berikutnya. Tidak perlu terus merawat templat lama juga.

#### Alur Prosedur

1. Serahkan dokumen persyaratan. Jika kolom yang wajib (nama produk, fungsinya, siapa pemakainya, harga, satuan harga, warna penanda, lokasi master desain, dan seterusnya) dibiarkan kosong, AI tidak mulai. Aturannya adalah ia tidak bertanya kepada pemilik di tengah jalan. Jika semuanya tak lengkap di awal, ia tidak memulai
2. Tentukan warna produk. Setiap produk dalam seri Agenda punya satu warna penanda. AI mengukur warna produk yang sudah ada, mengusulkan sekitar empat kandidat yang tidak tumpang tindih, dan pemilik memilih
3. Tetapkan desainnya. Saya meminta AI desain (Claude Design) membuat usulan untuk layar. AI menjalankan pemeriksaan mandiri hingga tiga putaran, dan hanya usulan yang lulus pemeriksaan yang ditunjukkan kepada pemilik
4. Serahkan implementasi kepada AI sampai tuntas. AI membangun dan memperbaiki sendiri sampai memenuhi syarat penerimaan yang ditetapkan (pemeriksaan tipe, pemeriksaan gaya, semua uji lulus (hijau), lulus setiap pemeriksaan layar, dan perubahan basis data berjalan mulus di lingkungan uji)
5. Pemilik menyetujui hanya saat ke produksi. Semuanya hingga lingkungan uji berjalan otomatis tanpa campur tangan manusia, dan pemilik hanya menilai operasi produksi

Saya membangun tahap implementasi agar tidak berhenti di tengah untuk menunggu persetujuan pemilik. Pada masa awal, saya maju dengan meminta persetujuan di setiap tahap, tetapi dengan begitu tak ada yang bergerak maju. Ketika ada beberapa jendela kerja AI, masing-masing berhenti menunggu persetujuan, dan pemilik harus berkeliling ke setiap jendela membuat penilaian. Maka saya mengubahnya: saya menyerahkan lebih dulu rentang yang sudah disetujui dan syarat penerimaan yang bisa dinilai mesin, dan ia berhenti hanya saat gagal.

Syarat berhentinya juga ditetapkan. Ketika dokumen prosedur dan keputusan pemilik bertentangan. Ketika operasi yang hanya bisa dilakukan manusia diperlukan. Ketika ia gagal maju pada error yang sama tiga kali berturut-turut. Ketika sesi autentikasi kedaluwarsa, izin tidak mencukupi, atau operasi yang tak bisa dibatalkan diperlukan. Selain itu, AI maju sendiri. Keadaan pekerjaan dicatat dalam sebuah file kecil, sehingga bahkan jika ia macet di tengah, ia bisa melanjutkan dari sana.

#### Manusia Hanya Mengerjakan Dua Hal

Saya menulis ini di dokumen prosedur: AI menjalankan setiap langkah. Pemilik hanya boleh diminta dua hal berikut.

- Penilaian itu sendiri. Menyetujui, memutuskan, menentukan mana dari dua pilihan yang diambil
- Operasi yang hanya bisa dilakukan manusia. Kunci yang hanya bisa diterbitkan dari layar admin layanan eksternal, permohonan yang melibatkan verifikasi identitas, operasi pada perangkat nyata dan penilaian visual

Jika AI menyerahkan hal lain kepada pemilik, itu pelanggaran terhadap dokumen prosedur. Pada tabel prosedur, saya menambahkan kolom "pelaksana" pada setiap baris, dan setiap baris yang tidak bisa disertai alasan mengapa harus dikerjakan pemilik dialihkan ke sisi AI.

Saya punya alasan membuat aturan ini. Ketika saya memilah pekerjaan yang tersisa untuk satu produk, AI mendaftarkan "membuat proyek server," "mendaftarkan tujuan login," "memasukkan variabel lingkungan," dan "membangun lingkungan uji," semuanya sebagai tugas pemilik. Semuanya adalah operasi yang bisa dijalankan oleh AI sendiri. "Mengapa saya yang melakukan ini?" adalah reaksi jujur saya saat itu. AI mengerjakannya sendiri jika diminta. Tetapi jika tidak diminta, ia mengoperkannya kepada orang. Itulah mengapa saya harus menuliskannya ke dalam dokumen prosedur.

Saya memasukkan setiap kegagalan sistem reservasi yang saya jelaskan di Bab 2 ke dalam daftar periksa dokumen prosedur ini. Masukkan uji lebih dulu. Jangan simpan data produksi di lingkungan pengembangan. Bangun lingkungan uji lebih dulu. Produk berikutnya menghindari kepedihan yang sama sejak awal.

#### Masih Terus Tumbuh

Dokumen prosedur ini bukan produk jadi. Ia sesuatu yang terus saya tambah setiap kali ada yang gagal.

Misalnya, pernah ada saat saya meminta AI desain membuat layar untuk satu produk lima kali berturut-turut, dan kelimanya ditolak. Itu termasuk putaran ketika saya menyerahkan aturan desain seluruh seri (DESIGN.md).

Pada awalnya, AI mendiagnosis penyebabnya sebagai "skema warna itu sendiri." Saya menyangkalnya. Penyebab sebenarnya ada dua. Yang satu adalah bahwa warna yang tak punya definisi dalam aturan dipakai sesuka hati. Yang lain adalah bahwa tiga bagian dengan peran berbeda ditumpuk vertikal dengan warna latar dan margin yang sama, tanpa batas di antaranya. Tak ada aturan yang dilanggar, namun peran-peran itu hilang dari tampilan.

Maka saya menambahkan klausul pada aturan desain. Jangan beri tampilan yang sama pada elemen yang perannya berbeda. Jangan memisahkan hanya dengan warna. Yang terpenting hadir lebih dulu di garis pandang. Hanya hal yang benar-benar setara yang boleh dijajarkan dengan bobot yang sama. Jangan membuat tata letak yang sekadar menumpuk secara vertikal.

Ada satu pelajaran lagi dari kegagalan. Jika Anda menyampaikan "tampilan bawaan yang harus dihindari" hanya sebagai daftar larangan, AI berayun sepenuhnya ke tampilan bawaan lain yang tidak ada di daftar. Ketika saya melarang kartu, bayangan, dan sudut membulat sekaligus, yang kembali adalah layar seperti koran yang hanya terdiri dari garis dan margin. Sejak itu, saya meminta bahan permintaan ditulis dalam tiga kolom: "pola yang dihindari," "apa yang ingin saya larang," dan "apa yang dilakukan sebagai gantinya."

Saya juga mengubah cara menentukan warna penanda di tengah jalan. Ketika produk melampaui delapan, kisaran warna gelap telah terisi produk yang sudah ada, dan produk kesembilan dan seterusnya tak lagi bisa mendapat warna gelap untuk garis dan tombol tanpa bertabrakan dengan yang ada. Maka saya merevisi aturannya: warna penanda sebuah produk dipakai hanya untuk warna permukaan yang terang, dan garis, garis pemisah, ikon, dan tombol utama semuanya disatukan dalam warna tinta bersama seri ini (hitam arang). Itu kendala yang baru jelas ketika produk bertambah banyak.

Setiap kali ada yang gagal, saya memperbaiki dokumen prosedur. Produk berikutnya menjadi lebih mudah sebesar itu. Saya yakin menumbuhkan dokumen prosedur adalah investasi terbaik untuk terus membangun produk seorang diri.

【Gambar 4-2】Tahap-tahap prosedur peluncuran, dan siapa yang menjalankannya (AI atau pemilik) *(Layar dalam bahasa Jepang.)*

【Gambar 4-3】Warna penanda seri Agenda. Satu warna per produk, dipakai hanya pada permukaan *(Layar dalam bahasa Jepang.)*

### 4-2 AgendaHub: Pintu Depan

Seiring produk bertambah, Anda akhirnya membangun hal yang sama berulang kali. Login, penagihan, halaman pengantar, panduan ke produk lain. Untuk menjalankan ini seorang diri, Anda perlu membangun bagian bersama sekali dan memakainya ulang di semua produk.

AgendaHub adalah tempat bagian-bagian bersama itu dikumpulkan. Saya menyebutnya "pintu depan."

Pertama, ia adalah pintu masuk yang mengarahkan dari satu alamat ke setiap produk. Di bawah satu domain, bontallc.com, sebuah pintu masuk untuk setiap produk berderet: /agendatimbro, /agendaoro, /agendaluce. Bagi pelanggan tampak seolah produk-produk itu berada dalam satu situs, tetapi sebenarnya program terpisah berjalan di belakang masing-masing.

Berikutnya, ia adalah tempat halaman pengantar produk ditempatkan. Ada satu halaman pengantar untuk seri, dan di dalamnya ada satu bagian untuk setiap produk. Setiap bagian memuat nama produk dan sebutannya, harga, masalah yang dinyatakan dengan kata-kata pemilik sendiri yang dimulai dengan "Ketika Anda...," uraian tentang apa yang bisa dilakukannya, dan tautan ke halaman rincian. Ketika saya merilis produk baru, menambahkan bagian ini termasuk dalam prosedur peluncuran.

Dan ia adalah rumah bagi aturan desain dan prosedur peluncuran. Master warna penanda, aturan layar (DESIGN.md), skill ProductBootstrap yang saya jelaskan di 4-1, skill yang memeriksa layar, dan skill yang membuat perubahan basis data dengan aman. Untuk setiap aturan yang melintasi seri, isi sebenarnya berada di sini, dan setiap produk membacanya lewat acuan.

【Gambar 4-1】Struktur seri Agenda. Dari pintu depan (AgendaHub) ke setiap buku catatan, dan setiap buku catatan tersambung ke satu akun (AgendaID) *(Layar dalam bahasa Jepang.)*

### 4-3 AgendaID: Akun Bersama dan Penagihan

AgendaID adalah sistem bersama seri ini untuk akun dan penagihan.

Seorang pemilik yang login sekali dengan akun Google bisa memakai setiap produk. Tak perlu membuat akun untuk setiap produk. Saya juga berencana pada akhirnya membawa pengaturan bahasa lintas produk.

Penagihan juga satu sistem. Alih-alih membangun sambungan ke layanan pembayaran (Stripe) untuk setiap produk, AgendaID menanggung semuanya. Ada empat kategori harga: produk ringan seharga ¥300 (sekitar $2) per bulan, produk bayar sesuai pemakaian, produk pembelian sekali bayar seharga ¥600 (sekitar $4), dan produk gratis. Produk berbayar memiliki masa gratis tiga bulan tanpa pendaftaran kartu, yang bisa dipakai sekali untuk setiap kombinasi kedai dan produk. Ada juga mekanisme yang menambahkan masa gratis tiga bulan masing-masing kepada perujuk dan orang yang dirujuk.

Sebelum masa gratis berakhir, email pemberitahuan tiba tujuh hari dan satu hari sebelumnya. Pada awalnya saya membangun email ini di dalam Buku Absensi juga, tetapi seiring produk bertambah saya menyadari sia-sia memberi setiap produk mekanisme yang sama, jadi saya menyatukannya di sisi AgendaID.

#### Pembatalan dan Penghapusan di Bawah Aturan Bersama, Juga

Ada bagian yang tidak mencolok tetapi penting: pembatalan dan penghapusan data.

Ketika pelanggan membatalkan, data mana yang dihapus, dan kapan? Jika Anda membangunnya terpisah untuk setiap produk, pasti ada yang terlewat di suatu tempat. Terlebih lagi, seri Agenda mencakup produk yang menangani data yang sangat sensitif, seperti yang mengenali pelanggan tetap lewat pengenalan wajah.

Maka saya membagi tingkat penghapusan menjadi empat tingkat dan menjadikannya aturan bersama seri ini. Yaitu membatalkan produk, menghapus kedai, menarik diri dari akun (keluar dari seluruh seri), dan permintaan penghapusan dari seorang staf secara perorangan. Tingkat yang lebih atas memicu penghapusan berantai ke tingkat di bawahnya, dan setiap produk mendaftarkan prosedur penghapusan datanya sendiri ke sistem bersama. Masa tenggang penghapusan adalah 30 hari, dan selama itu bisa dibatalkan.

Sebuah sumbu waktu menyertainya. Catatan kehadiran, misalnya, wajib disimpan lima tahun menurut hukum. Bahkan jika mantan staf meminta penghapusan, dalam masa penyimpanan catatan harus dipertahankan, dengan nama dan sejenisnya dianonimkan, alih-alih dihapus secara fisik. Saya perlu memutuskan garis antara "hapus" dan "simpan" dengan memeriksanya terhadap hukum.

#### Login Uji agar AI Tidak Mencemari Produksi

Saya menambahkan satu mekanisme lagi pada AgendaID, untuk AI: pintu masuk login uji.

Agar AI memeriksa bahwa semuanya berfungsi, AI harus login dan mengoperasikan layar. Tetapi login dilakukan dengan akun Google, sehingga AI tidak bisa login sendiri. Dan saya tidak bisa menyerahkan akun pemilik kepada AI juga. Ada bahaya uji AI mencemari data produksi.

Maka saya membangun pintu masuk yang menerbitkan akun sintetis (persona) yang hanya bisa dipakai di lingkungan uji. Ia tidak bekerja di produksi. Basis data lingkungan uji adalah proyek terpisah dari produksi dan hanya berisi data sintetis. AI login lewat pintu masuk ini, mengoperasikan layar, dan memastikan bahwa semuanya berfungsi. Akun uji dibangun ulang setiap hari, dan yang lama dihapus.

Dengan ini, AI bisa menjalankan bahkan pemeriksaan akhir sendiri, di lingkungan yang dibangun persis seperti produksi, tanpa menyentuh produksi.

### 4-4 Navigasi Bersama, dan Kegagalan Kata "Pintu Depan"

Agar pengguna bisa berpindah dari produk mana pun ke yang lain, saya memberi setiap produk menu navigasi bersama. Itulah jalur yang memungkinkan pemilik bar yang memakai Buku Absensi bertanya di Buku Bantuan, atau pergi melihat buku catatan lainnya.

Ada kisah kegagalan kecil di balik navigasi bersama ini.

Pada versi pertama, saya menaruh tautan bertuliskan "Kembali ke pintu depan." Itu karena, secara internal, saya menyebut AgendaHub "pintu depan." Tetapi ketika saya memeriksa di perangkat nyata, ada yang janggal. Dua tautan, "Kembali ke pintu depan" dan "Lihat seri Agenda," melompat ke tempat yang sama. Selain itu, tautan bantuan berada di atas menu pekerjaan sehari-hari, sehingga urutan kepentingannya terbalik. Dan di atas semuanya, kata "pintu depan" tidak berarti apa-apa bagi pemilik yang memakai produk untuk pertama kali. Itu bahasa internal si pembuat sendiri.

Maka saya mengatur ulang prinsipnya. Urutkan butir menurut seberapa dekat dengan tujuan pengguna: pekerjaan sehari-hari di paling atas, tautan yang mengarah ke luar di paling bawah. Bahkan tautan yang dimaksudkan menggaet pengguna baru tidak pernah ditaruh di atas pekerjaan. Batasnya harus bisa dijelaskan dengan satu garis. Tulis kata-katanya dalam bahasa pengguna, bukan bahasa internal. Jangan pernah menaruh lebih dari satu tautan yang melompat ke tempat yang sama. Saya membuang "Kembali ke pintu depan" dan menggabungkan semuanya menjadi satu tautan, "Lihat buku catatan Agenda lainnya."

Di Bab 2, saya menulis tentang mempelajari bahasa UI. Itu bahasa yang dipakai pemilik untuk berbicara kepada AI. Ini kebalikannya: bahasa yang dipakai si pembuat untuk berbicara kepada pengguna. Pada keduanya, intinya adalah menyesuaikan kata-kata Anda dengan orang yang Anda ajak bicara.

【Gambar 4-4】Navigasi bersama setelah perbaikan. Pekerjaan di atas, dan tautan yang mengarah ke luar di paling bawah *(Layar dalam bahasa Jepang.)*

### 4-5 Fondasinya Berbiaya $35 per Bulan

Biaya basis data seluruh fondasi yang dijelaskan dalam bab ini sekitar $35 per bulan. Paket berbayar yang mencakup proyek produksi adalah $25, dan proyek untuk lingkungan uji adalah $10.

Ini pun bukan jumlah dari awal. Pada satu titik saya membayar $45 per bulan. Basis data pengembangan untuk produk pengenalan wajah masih ditagih meski tidak saya pakai. Saya memindahkannya ke tingkat gratis dan menghentikannya, menghapus proyek lain yang tidak saya pakai, dan begitulah jumlahnya sampai ke yang sekarang.

Saya juga memperhatikan biaya AI. Pekerjaan AI yang menulis program ditagih menurut jumlah token (satuan teks yang dibaca dan ditulis AI). Saya menghindari pemusatan biaya dengan membuat jendela kerja berpegang pada peran koordinator dan menyerahkan implementasi itu sendiri kepada AI lain dengan jatah biaya terpisah. Untuk model generatif pada jendela obrolan pun, saya melihat harganya dan memilih yang perlu dan cukup. Bahkan jika model tingkat lebih tinggi hanya berbeda $1 per bulan, saya memilih dengan bertanya "apakah ini cukup?"

Jika sistem dibangun dalam skala kecil, penjualan yang kecil pun bisa menopang usaha Anda. Kisah monetisasi di Bab 3 ditopang oleh kecilnya biaya fondasi ini.

### 4-6 AI Koordinator, dan Orang yang Mengambil Keputusan

Terakhir, izinkan saya menggambarkan bentuk hari kerja saya.

Saya membuka beberapa jendela kerja AI pada saat yang sama. Ada jendela untuk sistem reservasi, jendela untuk setiap produk, dan jendela koordinator yang mengirim instruksi kepada mereka dan mengumpulkan hasilnya. Jendela koordinator itu saya beri nama AgendaRegia (buku catatan koordinator).

Yang mengambil keputusan, yaitu memutuskan "pilihan mana yang diambil," adalah saya dan AI di sisi obrolan. AI di sisi obrolan menemukan celah dan kontradiksi pada spesifikasi di muka, menempelkan keputusan bawaan pada masing-masing, dan mengusulkannya sekaligus. Saya membacanya dan memutuskan. Apa yang diputuskan dikumpulkan dalam lembar instruksi bernama Goal dan ditempelkan ke jendela kerja. Isinya mencakup persetujuan di muka dan syarat kelulusan yang bisa dinilai mesin. Jendela kerja membacanya dan melanjutkan sampai tuntas, berhenti hanya ketika ada yang gagal.

Saya juga meminta lembar instruksi menyertakan perkiraan kapan pekerjaan selesai. Saya menyelipkan pekerjaan ini di sela jam buka bar, jadi jika saya tak tahu berapa lama sesuatu akan memakan waktu, saya tak bisa merencanakan hari saya.

Peran pemilik bukan membaca melainkan memutuskan. Saya tidak perlu membaca semua 1.775 log percakapan. Saya menjawab pertanyaan tentang fakta bar. Saya memutuskan hal-hal yang hanya bisa ditentukan oleh kebijakan bar. Setelah sesuatu dirilis ke produksi, saya menyentuhnya sendiri lima atau enam kali untuk memeriksa apakah ada yang terasa janggal. Hanya itu.

Sebelum sampai ke bentuk ini, saya mengulang pekerjaan berkali-kali. AI menambah fitur sendiri dan layarnya menjadi tidak stabil. Pekerjaan membengkak tanpa batas dari satu instruksi. Menunggu persetujuan di setiap tahap berarti tak ada yang maju. Setiap kali, saya menambahkan satu aturan, dan begitulah ia sampai pada bentuknya sekarang. Ini pun masih tumbuh.

#### Poin Penting dari Bab Ini

- Untuk pekerjaan yang berulang, jadikan prosedurnya sendiri sebuah dokumen dan serahkan kepada AI. Jika Anda memperbaiki panduannya setiap kali gagal, lain kali akan lebih mudah
- Bangun bagian bersama (login, penagihan, navigasi) sekali saja dan pakai ulang di semua produk. Jika fondasinya kecil, bahkan penjualan yang kecil bisa menopang Anda
- Manusia hanya mengerjakan penilaian dan operasi yang hanya bisa dilakukan manusia. Jika AI menyerahkan hal lain kepada Anda, tambahkan ke panduan

Kelanjutan bab ini (buku catatan berikutnya yang akan saya bangun, dan pelajaran yang saya tambahkan ke panduan) ada di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

## Bab 5: Masa Depan Sebuah Bar Kecil

### 5-1 Dari Zatta Gohan ke Tamuro

Saya masuk ke bisnis makanan dan minuman ketika berusia 39 tahun.

Pemicunya adalah sebuah bar di lingkungan bernama Zatta. Sebulan sekali, kadang dua minggu sekali, mereka mengizinkan saya menyajikan hidangan di sana. Saya sudah lama belajar memasak sendiri, tetapi saat itu saya punya tempat di mana orang memakan masakan saya dan merasa bahagia. Itulah pengalaman awal saya.

Pada 2014, saya membuka sebuah restoran bernama Zatta Gohan di Arai-Yakushi. Itu tempat kecil yang menyajikan menu set. Saya menjalankannya selama tujuh tahun.

Di Arai-Yakushi, saya merasakan batas pada jumlah pelanggan. Lalu saya menemukan sebuah properti di Higashi-Nakano. Berjalan dari pintu timur stasiun kurang dari semenit. Bahkan pada hari hujan, Anda bisa sampai tanpa terlalu basah.

Pada November 2018, saya membuka Tamuro di sana. "Tamuro" berarti tempat orang-orang berkumpul. Ada 11 kursi konter dan 8 kursi tatami, 19 seluruhnya. Selama tiga tahun saya menjalankan dua tempat secara paralel, Arai-Yakushi dan Higashi-Nakano. Pada masa COVID, mempertahankan keduanya menjadi sulit, sehingga saya menutup kedai Arai-Yakushi dan hanya Tamuro yang tersisa.

#### Bar Kurasi

Tamuro menyebut dirinya "bar kurasi."

Kurasi berarti memiliki mata yang jeli dalam memilih. Sebelum menjadi juru masak, saya ingin menjadi kurator. Makanan, minuman, suasana bar: semuanya saya buat dengan memilih menggunakan mata yang jeli. Itulah Tamuro.

Saya sering bepergian untuk makan, baik di luar negeri maupun di Jepang. Vietnam, Kamboja, Italia, Shanghai, Beijing, Meksiko. Berkeliling menikmati makanan adalah kesenangan, dan sekaligus cara menemukan apa yang akan disajikan di Tamuro. Saya menciptakan ulang bahan mahal dengan bahan yang terjangkau. Misalnya, jika Anda mengeringkan kuning telur dan memarutnya, Anda mendapat rasa yang mendekati bottarga. Saya menganggap jenis penggantian ini (lokalisasi) sebagai peran saya.

Saya belajar memasak lagi pada masa COVID. Saya mengikuti kursus masakan Prancis dengan total delapan sesi, dan juga mengikuti kursus masakan Jepang. Cara menangani umami, dan teknik mengatur api. Apa yang saya pelajari di sana adalah fondasi masakan saya hari ini.

Menu Tamuro disusun dari empat hidangan pembuka dan satu hidangan utama. Saya memberinya rentang bahan agar pelanggan yang tinggal sendirian bisa mendapat banyak sayuran. Saya menyusunnya agar cara memasak (goreng, acar cuka, rebus, panggang) dan rasa (manis, pedas, asam) tidak tumpang tindih. Hidangan paling populer adalah tonteki, steik babi. Ia memiliki saus yang sedikit manis dari kecap Kyushu, dengan banyak bawang putih.

#### Tempat Orang-Orang Berkumpul

Sekitar separuh pelanggan Tamuro datang sendirian. Mereka terutama berusia 30-an hingga 50-an, dan banyak yang tetangga dari Higashi-Nakano, tetapi ada juga yang datang dari sekitar Akabane, Shinjuku, Nishi-Ogikubo, Ogikubo, dan Eifukucho.

Ciri khas bar ini adalah seberapa banyak pelanggan berbincang satu sama lain. Saya membuat konter agar mudah berbicara kepada orang di sebelah, dan saya atau staf menentukan tempat duduk dengan menilai siapa yang akan cocok. Pelanggan yang datang sendirian kadang kembali bersama-sama belakangan. Seperti namanya, tempat ini telah menjadi tempat orang-orang berkumpul. Saya memposting keseharian bar di [Instagram](https://www.instagram.com/tamuro.higashinakano/).

Pada makan malam course yang diadakan sekitar sebulan sekali, saya menyajikan tujuh hingga delapan hidangan selama dua hingga tiga jam, bersama pairing wine. Setiap bulan temanya berubah: Italia, Prancis, Jepang. Kelas memasak adalah lokakarya tiga jam, dan setelah memasak, semua bersulang, makan, dan pulang. Ada aperitivo, menyajikan wine dan hidangan kecil di awal malam sebelum buka. Ada barbekyu sekitar dua kali setahun. Ada pesta akhir tahun sekali setahun. Dan ada festival yukata yang saya tulis di Bab 1.

Sistem reservasi yang saya tulis di Bab 1, jendela obrolan, dan MCP semuanya adalah alat untuk membawa orang ke bar ini. AI adalah sarana untuk mengumpulkan orang, bukan tujuan.

### 5-2 Kari Hamburger Quatre Épices

Tamuro adalah bar malam hari. Pada siang hari, ruangannya kosong.

Dengan memanfaatkan waktu itu, saya memulai Quatre Épices pada Januari 2024. Itu kedai kari hamburg steak yang beroperasi hanya pada jam makan siang di tempat yang sama, dan dijalankan oleh staf.

Quatre Épices berarti "empat rempah" dalam bahasa Prancis. Sesuai namanya, alih-alih menumpuk banyak rempah, kami memilih dan mempersempitnya agar garis besar rasanya jelas. Karinya tidak memakai tepung; ia diselesaikan dengan kekentalan alami dari sayuran dan daging itu sendiri. Kepuasan saat selesai makan, dan tak ada rasa berat di perut. Dan keselarasan dengan hamburg steak. Saya merancangnya dengan tiga landasan itu.

Kami teliti dalam cara memasak hamburg steak. Kami mengatur campurannya agar keluar renyah di luar dan empuk di dalam, dan kami memasak sesuai campuran itu. Cara memasak dengan panas yang saya pelajari di malam hari di Tamuro juga dipakai pada hidangan siang hari.

Harga, hari buka, dan jam buka bisa berubah, jadi mohon periksa Instagram Tamuro (https://www.instagram.com/tamuro.higashinakano/) untuk informasi terbaru.

Quatre Épices juga menjalankan dapur makan anak (kodomo shokudo) di tempat yang sama. Itu kegiatan yang memakai fasilitas dan pasokan bahan bar yang sudah ada untuk menyajikan makanan kepada anak-anak di lingkungan sekitar. Lewat hubungan itu, kami juga membangun hubungan dengan balai warga setempat. Kami kadang menyajikan kari dan sandwich pada acara olahraga setempat, acara balai warga, dan festival tari Bon.

Sejujurnya, memanfaatkan jam siang tidak semuanya berjalan baik. Saya pernah mencoba membuka sesi minum di siang hari dan menyewakan ruangan kepada orang lain, tetapi pelanggan tidak datang seperti yang saya harapkan. Daya tarik bar tersampaikan secara berbeda ketika pemilik hadir di malam hari dan ketika hanya staf siang hari yang ada. Menumbuhkan kedai siang hari dengan daya tarik yang berbeda dari kedai malam masih merupakan tugas yang belum selesai.

### 5-3 Bonta LLC: Dua Pilar

Perusahaan kecil yang menjalankan Tamuro dan Quatre Épices adalah Bonta LLC. Saya adalah anggota pengelolanya.

Perusahaan ini memiliki dua pilar. Yang satu adalah makanan dan minuman: Tamuro dan Quatre Épices. Yang lain adalah TI: pengembangan seri Agenda, dan konsultasi.

Makanan dan minuman serta alat berbeda cara menghasilkan uangnya. Menopang perusahaan dengan dua pilar yang berbeda sifat adalah bentuk yang saya bayangkan.

Dan dua pilar itu saling memasok bahan. Masalah di bar menjadi benih sebuah alat. Apa yang saya pelajari dari membangun alat kembali ke dalam pengelolaan bar. Buku Lentera lahir dari jam tutup yang molor, dan catatan jam perpanjangan dari Buku Lentera menjadi dasar bagi perkiraan laba dan shift. "Pertanyaan yang tak bisa kami jawab" yang menumpuk di jendela obrolan memperbaiki panduan bar. Siklus inilah alasan saya bisa mengelola bar dan pengembangan sekaligus seorang diri.

Saya tidak berniat memperbesar perusahaan. Kecil, banyak, dan murah. Itulah bentuk perusahaan ini.

### 5-4 Menulis sebagai Raku Bonta

Ketika saya menulis dan menerbitkan, saya memakai nama pena "Raku Bonta." Saya menulis buku ini pun dengan nama itu.

Buku saya sebelumnya, *Wakil Manajer AI*, adalah buku tentang AI generatif. Buku itu menempati peringkat pertama di kategori manajemen waktu Amazon dan dibaca banyak orang. Buku ini adalah kelanjutannya.

Selain buku, saya juga menulis di note. Saya menulis tentang upaya bar dengan AI, apa yang saya temukan dalam perjalanan pelatihan, perkembangan penerbitan buku saya, dan seri Agenda. Anda bisa mengikuti kelanjutan yang tak muat di buku ini di note (https://note.com/bontallc).

Bagi saya, menulis juga merupakan cara untuk menuangkan bar dan pengembangan ke dalam kata-kata dan memeriksanya. Seperti yang saya tulis di Bab 1, pengetahuan pertama jendela obrolan "T-AI-MURO" dibangun dari kata-kata yang selama ini saya tinggalkan di X. Apa yang telah saya tulis menjadi bahan bagi AI. Ke depannya pun, apa yang saya tulis akan kembali ke bar dan ke AI.

Ada satu hal lagi yang telah saya putuskan tentang menulis. Saya tidak mengumumkan hal yang belum selesai dengan "segera hadir." Saya menyelesaikannya, membuat halaman pengantar, dan baru kemudian merilisnya. Saya yakin menjaga urutan itu adalah yang membuat perusahaan kecil mendapat kepercayaan.

### 5-5 Masa Depan Kedai Mandiri

Terakhir, saya akan mengumpulkan apa yang telah saya tulis dalam buku ini menjadi satu gambaran.

【Gambar 5-1】Gambaran besar dari apa yang diuraikan buku ini. Sebuah bar kecil membuka jendelanya sendiri (kisah pertama), dan mengubah masalahnya menjadi alat untuk dibagikan kepada bar lain (kisah kedua) *(Layar dalam bahasa Jepang.)*

Pelanggan akan meminta AI mereka sendiri mencarikan bar dan membuat reservasi. Pada Agustus 2026, menjadi mungkin memesan restoran dari ChatGPT lewat layanan reservasi besar. Pintu masuk bergeser dari situs pencarian dan ulasan kuliner ke AI milik masing-masing orang.

Pada titik itu, bar yang tidak terdaftar di layanan reservasi besar tak terlihat oleh AI. Tetapi bahkan jika Anda tidak ada di layanan besar, ada jalan bagi sebuah bar untuk terhubung langsung ke AI. Tamuro memilih jalan itu dengan membuka jendela bernama MCP. Sebuah bar kecil membuka jendelanya sendiri. Itulah kisah pertama buku ini.

Para pemilik bar akan bisa mengubah masalah mereka sendiri menjadi alat dan membagikannya kepada bar lain. Buku Lentera lahir dari masalah Tamuro yang ingin memberi tahu orang bahwa jam tutup akan molor, dan ia bisa dipakai di bar mana pun. Kekuatan untuk membangun tidak lagi hanya milik orang atau perusahaan tertentu. Seorang pemilik bar kecil berpindah dari sisi yang memakai alat ke sisi yang membangun dan membagikannya. Itulah kisah kedua buku ini.

Kesamaan keduanya adalah semakin kecil bar, semakin tajam ia bisa menjadi.

Jaringan restoran besar menggeneralisasi sistem mereka agar setiap gerai memberikan mutu yang sama. Tamuro adalah kebalikannya. Pelanggan yang datang sendirian membentuk separuhnya, hampir 90% reservasi dibuat pada hari yang sama, dan pelanggan saling berbincang. Untuk menyesuaikan dengan karakter Tamuro itu, saya membangun sistem reservasi, diskon, dan jendela obrolan secara terperinci. Karena tidak digeneralisasi, ia tajam. Karena tajam, ia menjadi alasan pelanggan memilihnya.

Dan semakin tajam sebuah bar, semakin banyak benih alat yang ia temukan. Semakin Anda menghadapi karakter bar, semakin spesifik masalah Anda. Masalah yang spesifik menjadi alat yang spesifik. Alat yang spesifik membantu bar lain yang memiliki masalah yang sama.

AI telah memungkinkan satu pemilik melakukan keduanya. Mempertajam bar, dan membagikan alat. Dulu, Anda harus memilih salah satu. Kini Anda bisa melakukan keduanya.

Tentu saja, ini masih dalam proses. Tingkat lolos uji jendela obrolan masih terus dinaikkan. Panduan bertambah dengan setiap kegagalan. Cara menumbuhkan kedai siang hari tetap menjadi tantangan. Orang yang memesan lewat AI masih belum banyak.

Meski begitu, saya yakin masa depan bar kecil itu cerah. Menjadi kecil bukan kelemahan. Karena kecil, kita bisa mencoba dengan cepat, membuang dengan cepat, dan memperbaiki dengan cepat. Karena kecil, kita bisa tajam. Dan masalah dari bar yang tajam menjadi alat dan diteruskan ke bar-bar kecil lain.

Saya menulis buku ini dari sebuah bar 19 kursi di Higashi-Nakano.

## Penutup

Terima kasih telah membaca sampai sejauh ini.

Apa yang saya tulis dalam buku ini adalah catatan per Oktober 2026. Alat AI berubah bentuk dalam hitungan bulan. Sebagian mekanisme yang saya uraikan mungkin sudah berbentuk lain pada saat buku ini terbit. Meski begitu, saya menuliskannya, dengan keyakinan bahwa catatan tentang bagaimana sebuah bar kecil membangun berbagai hal dengan AI, apa saja kegagalannya, dan apa yang dipelajarinya, seharusnya tetap berguna untuk beberapa waktu.

Seri Agenda: https://bontallc.com/agenda?via=b2-id-{{FMT}}

Ikuti kegiatan saya: note https://note.com/bontallc / X https://x.com/tamuro\_hnakano

Jika suatu saat Anda ke Higashi-Nakano, mampirlah ke Tamuro. Anda bisa memesan lewat situs reservasi, lewat jendela obrolan "T-AI-MURO" di situs itu, dan tentu saja lewat AI Anda sendiri.

Situs reservasi Tamuro: https://tamuroreservation.vercel.app/?src=b2-id-{{FMT}}

Instagram Tamuro: https://www.instagram.com/tamuro.higashinakano/

Bagi yang ingin mencoba reservasi lewat AI. Alamat sambungan server MCP Tamuro adalah URL berikut.

https://tamuroreservation.vercel.app/api/mcp

Pada pengaturan AI Anda (seperti Claude atau ChatGPT), buka layar untuk menambahkan alat eksternal (konektor, server MCP) dan daftarkan URL ini. Cara mendaftarkannya berbeda untuk setiap AI dan berubah seiring waktu, jadi cara paling aman adalah mencari "MCP" atau "konektor" di bantuan masing-masing AI. Tergantung paket yang Anda punya, Anda mungkin tidak bisa menyambungkan server MCP pilihan sendiri. Setelah terdaftar, tanyakan kepada AI Anda, "Apakah Tamuro punya tempat kosong malam ini?" AI itu akan memeriksa slot kosong dan harga serta mengantar Anda ke halaman reservasi. Anda sendirilah yang menekan tombol konfirmasi.

Bagi yang datang setelah membaca buku ini. Saat memesan, mohon masukkan kode kupon "BOOK". Kami akan menyajikan satu minuman gratis untuk pesanan pertama Anda. Jika Anda datang tanpa reservasi, cukup katakan "Saya tahu dari buku ini" saat memesan pertama kali. Kami akan memberikan minuman gratis yang sama. Ini sebuah cara kecil yang memungkinkan saya menghitung berapa orang yang datang karena buku ini.

Anda bisa masuk tanpa reservasi. Bahkan datang sendirian pun, Anda tidak akan merasa canggung. Bisa jadi Anda justru asyik mengobrol dengan orang di sebelah.

Saya menunggu Anda di Tamuro, tempat orang-orang berkumpul.

Raku Bonta

### Referensi

- OpenAI Help Center, "ChatGPT — Release Notes," 10 Agustus 2026, "Restaurant reservations in ChatGPT" https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Alpaca, "Alpaca MCP Server" (contoh server MCP di AS yang memungkinkan AI memasang order saham dan sekuritas lainnya) https://docs.alpaca.markets/docs/alpaca-mcp-server
- Perdebatan "kematian SaaS": pernyataan Satya Nadella di podcast BG2 (Desember 2024), anjloknya saham perangkat lunak pada Februari 2026 beserta sebutannya, dan bantahan Jensen Huang dirujuk dari laporan dan ulasan berikut. https://www.longangle.com/alts-education/software-ai  /  https://www.fastcompany.com/91504460/everything-youve-heard-about-the-saaspocalypse-is-wrong  /  https://en.thairath.co.th/money/tech\_innovation/tech\_companies/2916811
