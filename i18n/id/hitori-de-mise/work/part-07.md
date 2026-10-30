- Ia menyimulasikan waktu pembayaran yang terbagi menjadi "tanggal 10" dan "tanggal 25 / akhir bulan."

- Data disimpan di browser (cache).

Ini saja sudah cukup praktis, tetapi saya jadi ingin bereksperimen lebih jauh. "Saya ingin datanya tetap ada meski browser ditutup. Saya juga ingin memeriksanya di ponsel."

#### Fase 2: Memakai Alat yang Asing, "Firebase"

Saya sempat berpikir untuk menautkannya ke spreadsheet, tetapi saran Gemini di luar dugaan.

"Kalau mempertimbangkan kinerja real-time dan efisiensi, mari pakai 'Firebase' dari Google. Paket gratisnya sudah cukup untuk menjalankannya."

"Firebase...?" Saya belum pernah mendengar kata itu. Tetapi dengan naluri dari masa saya sebagai koordinator sistem, saya memutuskan, "Kalau AI merekomendasikannya sekuat ini, ayo kita ikuti."

Hasilnya, dengan memakai basis data bernama Firestore, data pun tersimpan dengan aman di cloud.

#### Fase 3: Login Google dan Sistem Persetujuan

Ini soal uang, jadi buruk kalau siapa pun bisa melihatnya.

Awalnya saya terpikir sesuatu seperti "frasa sandi," tetapi Gemini menyarankan, "Jika Anda ingin keamanan yang lebih kuat, mari pakai login Google."

Lalu, ketika saya berkata, "Saya ingin hanya staf yang saya setujui yang bisa melihatnya," ia bahkan membangun "sistem di mana administrator dapat menyetujui dan menghapus anggota di layar."

### 6-3. Fase 4-5: Menghadapi Layar Hitam (Terminal)

Dari sini datang rintangan terbesar vibe coding: menerbitkan aplikasi di internet (deploy).

#### Peringatan: Mulai dari Sini, Ini Kursus "Sabuk Hitam"

Beberapa halaman berikutnya adalah bagian "praktik langsung" tersulit dalam buku ini. Anda akan mengoperasikan "layar hitam (terminal)" seperti yang dipakai peretas di film.

Saya akan jujur. Anda pasti akan mendapat error di sini. Saya pun begitu. Anda akan menabrak tembok seperti "error izin PowerShell" yang terbaca seperti mantra. Tetapi jangan takut. Yang Anda lakukan di sini sama saja: cukup "ambil tangkapan layar dari pesan error dan lemparkan ke AI."

Kebenaran yang saya pelajari di masa saya di bisnis sistem adalah ini: "Bahkan profesional pun mendapat error. Satu-satunya perbedaan adalah apakah Anda menyerah ketika error muncul, atau mencari (meminta) bantuan." Jika terasa terlalu sulit, lewati bagian ini dan cukup rasakan potensinya: "Dengan AI, sejauh ini pun bisa dilakukan."

Gemini berkata:

"Kita akan menyiapkan lingkungan pengembangan di PC Windows Anda. Pasang 'Node.js,' dan ketikkan perintah berikut di 'VS Code.'"

Saya membuka layar hitam (terminal) sesuai petunjuk, dan langsung mendapat error.

"Tidak dapat dijalankan karena pembatasan keamanan PowerShell."

Pemilik biasa akan putus asa di sini.

Tetapi saya menyalin dan menempelkan layar error itu lalu melemparkannya ke AI.

AI menjawab seketika: "Cabut pembatasannya dengan perintah bernama 'Set-ExecutionPolicy.'"

Tanpa memahami artinya, saya mengetikkan perintah itu, lalu npm run build, firebase deploy...

Setiap kali saya mengetikkan karakter-karakter seperti mantra itu, baris teks bergulir cepat di layar dan prosesnya berjalan.

Dan akhirnya, aplikasi saya muncul di web.

#### Fase 5: Menjadikannya Aplikasi Ponsel (PWA)

Aplikasi yang diterbitkan itu awalnya dalam keadaan "polos tanpa riasan" dengan desain yang berantakan, tetapi ini pun terselesaikan dengan menambahkan pengaturan bernama "Tailwind CSS."

Lalu, ketika saya meminta, "Saya ingin menaruh ikon di layar utama ponsel dan memakainya seperti aplikasi," ia mengajari saya pengaturan untuk menjadikannya "PWA (Progressive Web App)."

Dan begitulah sebuah aplikasi khusus yang saya buat (tanpa menulis satu baris kode pun) lahir di dalam ponsel saya.

![Layar aplikasi manajemen arus kas yang sudah jadi](images/fig-26.png)

### 6-4. Fase 6: Masalah Setelah 30 Hari, dan Perbaikannya

Sekitar sebulan setelah mulai memakainya, muncul masalah.

"Kemarin masih jalan, tiba-tiba tidak bisa diakses!"

Saya panik dan berkonsultasi dengan Gemini, dan penyebabnya ada di tempat yang tak terduga.

"Pengaturan basis data (Firestore) masih dalam 'mode uji coba (terbatas 30 hari).' Masanya sudah habis."

Untuk menghemat kerepotan pengaturan di awal pengembangan, AI dengan sengaja memasang aturan yang punya tanggal kedaluwarsa.

"Mari tulis ulang aturan keamanannya agar 'pengguna mana pun yang sudah login dapat terus memakainya.'"

Ketika saya menulis ulang beberapa baris file pengaturan seperti yang diinstruksikan AI, aplikasi itu berhasil pulih dan kembali berjalan normal.

Masalah ini pun menjadi pengalaman baik bagi saya.

Saya belajar bahwa "sebuah sistem adalah makhluk hidup dan membutuhkan perawatan."

Dan saya mendapat ketenangan bahwa "meski terjadi masalah, selalu ada jawaban jika saya bertanya kepada AI."

### 6-5. Studi Kasus 2: "Proyek Pengenalan Wajah" yang Bermula dari Video Demo di X (Dulu Twitter)

Ini satu lagi pengembangan sistem yang saya jalani, dan yang terbesar.

Yaitu "sistem yang mengenali pelanggan yang masuk lewat kamera, dan diam-diam memberi tahu saya nama, data, dan preferensi mereka."

Semuanya bermula dari situs media sosial X, yang sedang saya gulir sambil lalu.

Sebuah video demo yang diunggah seorang insinyur muncul di beranda saya: memakai AI yang tertanam di Google Chrome (Built-in AI) untuk menjelaskan, secara real-time, apa yang dilihat sebuah webcam.

Naluri saya sebagai mantan orang sistem langsung bekerja.

"Ini 'multimodal.' Dan kalau tertanam di browser, bukankah ini bisa berjalan sepenuhnya di PC saya sendiri, tanpa membayar cloud?"

Kalau ini berhasil, saya mungkin bisa membangun sistem keramahtamahan khusus untuk kedai saya, tanpa memasang sistem yang mahal.

Saya menyalin URL-nya dan melemparkannya ke Gemini.

"Saya ingin melakukan hal yang sama dengan ini. Beri tahu saya cara mengimplementasikannya."

#### Fase 1: Berhasil, tetapi Saya Tak Bisa Tahu "Siapa"

Saya mengubah pengaturan Chrome (flag) seperti yang diinstruksikan Gemini dan menempelkan kodenya, dan sistem yang sama dengan demonya berjalan tanpa masalah.

Ketika saya muncul di kamera, layar menampilkan ini:

"Seorang pria berkacamata sedang duduk di depan PC."

Sistem ini memakai AI bawaan browser bernama GeminiNano. Keunggulannya adalah ia bekerja sepenuhnya di dalam browser tanpa terhubung ke cloud, tetapi ia hanya dapat mengenali hal umum seperti "kacamata" dan "pria." Ia tak bisa sampai menentukan siapa orangnya.

Ini teknologi yang menakjubkan. Tetapi sebagai pemilik restoran, saya langsung kecewa.

"Ini tidak bisa dipakai."

Yang ingin saya ketahui bukan ciri umum seperti "pria berkacamata," melainkan identifikasi individunya: "Apakah ini A atau B?"

#### Fase 2: Tembok Integrasi Google Photos, dan Jawaban AI

Maka saya mengajukan gagasan yang naif kepada Gemini.

"Hubungkan sistem ini ke Google Photos saya. Di sana ada data pengelompokan wajah teman-teman dan pelanggan tetap saya, jadi kalau dicocokkan dengan itu, kita bisa mendapat namanya, bukan?"

Jawaban Gemini dingin, tetapi benar.

"Maaf, itu tidak mungkin. Data pengenalan wajah di Google Photos adalah informasi privasi yang sangat sensitif, dan demi keamanan tidak diizinkan dipakai oleh program luar."

Masuk akal. Jalannya tampak berakhir di sini.

Tetapi dari sinilah datang inti sejati "vibe coding (pengembangan lewat dialog)." AI tidak sekadar menolak.

#### Fase 3: Alternatif dan Perubahan Arah

Gemini melanjutkan dengan menyarankan ini:

"Kita tak bisa memakai Google Photos, tetapi membangun sistem pengenalan wajah sendiri di lingkungan lokal dengan pustaka sumber terbuka (seperti OpenCV atau face_recognition) itu mungkin. Mau kita coba?"

Saya langsung menjawab "Ya."

Dari sini, rencana pengembangan berubah total. Alih-alih memakai fitur Chrome, saya akan membangun sistem pengenalan wajah dari nol memakai bahasa pemrograman bernama Python.

#### Fase 4: Bergulat dengan Layar Hitam dan Menghubungkan ke Spreadsheet

Apa yang harus saya lakukan tidak berubah. Saya bertanya kepada Gemini "cara memasang pustaka yang diperlukan" dan menempelkan jawabannya ke layar hitam (command prompt).

Ketika error muncul, saya melemparkan teks merah itu kembali ke Gemini apa adanya.

Beberapa jam kemudian, sistemnya akhirnya selesai.

1.  Webcam menangkap wajah saya.

2.  Ia mencocokkannya dengan "data foto wajah" di sebuah folder di PC.

3.  Ketika menemukan kecocokan, ia mencari daftar pelanggan di Google Spreadsheet.

4.  Layar menampilkan "Bonta: sisa botol persegi ○○ g."

![Sistem pengenalan wajah yang sedang berjalan. Ia mengenali wajah pemilik dan menampilkan informasi. Gambar yang ditangkap telah dimosaik memakai Gemini](images/fig-27.png)

Biaya alih daya: ¥0 (sekitar $0,00). Pekerjaan coding saya sendiri: nol.

Itulah saat sebuah "sistem CRM pengenalan wajah" yang unik lahir di sudut Higashi-Nakano.

#### Fase 5: Lalu Saya Menyadari "Tanggung Jawab untuk Melindungi"

Sistemnya selesai. Tetapi bersama kegembiraan, saya merasakan hawa dingin merambat di punggung.

"Tunggu sebentar. Saat ini, komputer ini menyimpan data wajah pelanggan (informasi biometrik), bukan...?"

Sampai saat itu saya berpikir, "Asal jalan, tidak apa-apa." Tetapi begitu dioperasikan sungguhan, ceritanya lain.

Bagaimana kalau komputer ini terinfeksi virus? Data wajah pelanggan dan informasi preferensi mereka (informasi pribadi) mungkin bocor bersamaan.

PC standalone yang tidak terhubung ke internet akan aman, tetapi selama saya menangani reservasi dan media sosial, koneksi internet mutlak diperlukan.

"Mampu membangun alat yang berguna" dan "mampu mengelolanya dengan aman" adalah dua perkara berbeda.

Di sinilah untuk pertama kalinya saya benar-benar merasakan pentingnya "asuransi risiko siber" yang pernah dibicarakan seorang agen asuransi ketika ia datang menawarkan kepada saya.

Saya dulu tertawa, "Kedai kecil seperti kami tidak akan kena serangan siber," tetapi kini setelah AI memungkinkan kita membangun sistem canggih, kami para pemilik perorangan pun memikul tanggung jawab sebagai "pengelola data" yang semestinya.

Dengan AI, Anda bisa mendapatkan alat-alat ajaib.

