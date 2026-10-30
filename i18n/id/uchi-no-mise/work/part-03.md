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

