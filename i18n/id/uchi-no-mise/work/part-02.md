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

