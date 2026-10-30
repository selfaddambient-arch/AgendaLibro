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

