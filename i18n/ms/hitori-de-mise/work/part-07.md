## Bab 6: Cabaran - Membangunkan Sistem Khas untuk Kedai Saya Sendiri

~ "Kalau tidak ada, bina sendiri." Projek pembangunan sistem tanpa pakar ~

※Sekadar makluman, anda tidak perlu melakukan segala-galanya dalam buku ini.

・Hantar imej dan minta AI menulis teks\
・Tukar mesej LINE yang panjang menjadi rajah

Dua perkara ini sudah memadai untuk bermula. Malah itu pun pasti memudahkan kerja anda.\
Cukup juga jika anda hanya membaca ini sebagai bahan bacaan santai dan berfikir, "Oh, dengan AI pun boleh sampai sebegini."

### 6-1. Aplikasi Siap Pakai Tidak Menjawab Keperluan Terperinci Saya

Setakat ini saya telah bercakap tentang menggunakan AI di atas platform sedia ada, seperti penjanaan imej dan analisis menu.

Tetapi apabila anda terus menjalankan perniagaan, timbul kebimbangan yang memang tidak dapat diselesaikan oleh "aplikasi siap pakai."

Khususnya bagi model perniagaan yang tidak lazim seperti kami, "kari pada siang hari, bar pada waktu malam," aliran wang masuk dan keluar juga rumit.

"Saya mahu memadankan baki PayPay Bank saya dengan pembayaran yang akan datang dan mengetahui jumlah yang akan tinggal pada hujung bulan."

"Tarikh pembayaran terbahagi antara 10hb dan 25hb. Saya mahu mensimulasikannya."

Perisian perakaunan di luar sana sangat berkemampuan, tetapi tiada yang tepat mengenai "kebimbangan dalam kepala saya sekarang."

Maka saya nekad.

"Kalau tidak ada, saya bina sendiri. Saya ada Gemini, jurutera terkuat."

### 6-2. Fasa 1–3: Daripada Nota Coretan kepada "Awan"

Pembangunan bermula dengan menunjukkan nota saya di Google Keep kepada Gemini.

![Nota Keep yang menjadi titik permulaan pembangunan](images/fig-25.png)

#### Fasa 1: Membina Logik

"Saya mahu mengautomasikan pengiraan dalam nota ini."

Sebagai respons kepada permintaan saya, Gemini dengan pantas menyusun logik pengiraan.

- Apabila saya menukar jumlah bagi sesuatu item, ia serta-merta mengira baki akhir.

- Jika dana hampir tidak mencukupi, ia memaparkan "amaran" dalam warna merah.

- Ia mensimulasikan masa pembayaran yang dibahagikan kepada "10hb" dan "25hb / hujung bulan."

- Data disimpan dalam pelayar (cache).

Ini sahaja sudah cukup mudah, tetapi saya mula mahukan lebih. "Saya mahu data kekal walaupun pelayar ditutup. Saya mahu menyemaknya pada telefon juga."

#### Fasa 2: Menggunakan Alat yang Asing, "Firebase"

Saya telah terfikir untuk memautkan kepada hamparan, tetapi cadangan Gemini tidak dijangka.

"Jika anda memikirkan prestasi masa nyata dan kecekapan, mari kita guna 'Firebase' milik Google. Peringkat percuma sudah cukup untuk menjalankannya."

"Firebase...?" Saya tidak pernah mendengar perkataan itu. Tetapi dengan gerak hati zaman saya sebagai penyelaras sistem, saya memutuskan, "Jika AI mengesyorkannya sekuat ini, mari kita ikut."

Hasilnya, dengan menggunakan pangkalan data bernama Firestore, data dapat disimpan dengan selamat dalam awan.

#### Fasa 3: Log Masuk Google dan Sistem Kelulusan

Ini tentang wang, jadi tidak elok jika sesiapa sahaja boleh melihatnya.

Pada mulanya saya terfikir sesuatu seperti "frasa kata laluan," tetapi Gemini mencadangkan, "Jika anda mahu keselamatan yang lebih kukuh, mari kita guna log masuk Google."

Kemudian, apabila saya berkata, "Saya mahu hanya kakitangan yang saya luluskan boleh melihatnya," ia malah membina "sistem di mana pentadbir boleh meluluskan dan membuang ahli pada skrin."

### 6-3. Fasa 4–5: Mengharungi Skrin Hitam (Terminal)

Dari sini datang halangan terbesar vibe coding: menerbitkan aplikasi di internet (deploy).

#### Amaran: Mulai Sini, Ini Kursus "Tali Pinggang Hitam"

Beberapa halaman seterusnya ialah bahagian "amali" paling sukar dalam buku ini. Anda akan mengendalikan "skrin hitam (terminal)" seperti yang digunakan penggodam dalam filem.

Saya berterus terang. Anda pasti akan mendapat ralat di sini. Saya juga begitu. Anda akan bertemu tembok seperti "ralat kebenaran PowerShell" yang bunyinya seperti mantera. Tetapi jangan takut. Yang anda lakukan di sini tetap sama: hanya "ambil tangkapan skrin ralat itu dan lontarkan kepada AI."

Kebenaran yang saya pelajari pada zaman saya dalam perniagaan sistem ialah ini: "Malah profesional pun mendapat ralat. Satu-satunya perbezaan ialah sama ada anda berputus asa apabila satu muncul, atau mencari (meminta) bantuan." Jika terasa terlalu sukar, langkau bahagian ini dan ambil sahaja kemungkinannya: "Dengan AI pun boleh sampai sebegini."

Gemini berkata:

"Kita akan menyediakan persekitaran pembangunan pada PC Windows anda. Pasang 'Node.js,' dan taip arahan berikut dalam 'VS Code.'"

Saya membuka skrin hitam (terminal) seperti yang diberitahu, dan serta-merta mendapat ralat.

"Tidak boleh dijalankan kerana sekatan keselamatan PowerShell."

Pemilik biasa akan putus asa di sini.

Tetapi saya menyalin dan menampal skrin ralat itu dan melontarkannya kepada AI.

AI menjawab serta-merta: "Buka sekatan itu dengan arahan bernama 'Set-ExecutionPolicy.'"

Tanpa memahami maksudnya, saya menaip arahan itu, kemudian npm run build, firebase deploy...

Setiap kali saya menaip aksara seperti mantera itu, teks berlari di skrin dan proses bergerak ke hadapan.

Dan akhirnya, aplikasi saya muncul di web.

#### Fasa 5: Menjadikannya Aplikasi Telefon Pintar (PWA)

Aplikasi yang diterbitkan itu pada mulanya berada dalam keadaan "antara muka kosong tanpa gaya" dengan reka bentuk yang rosak, tetapi ini juga diselesaikan dengan menambah tetapan bernama "Tailwind CSS."

Kemudian, apabila saya bertanya, "Saya mahu meletakkan ikon pada skrin utama telefon dan menggunakannya seperti aplikasi," ia mengajar saya tetapan untuk menjadikannya "PWA (Progressive Web App)."

Maka sebuah aplikasi khusus yang saya buat (tanpa menulis satu baris kod pun) lahir di dalam telefon saya.

![Skrin aplikasi pengurusan aliran tunai yang siap](images/fig-26.png)

### 6-4. Fasa 6: Masalah Selepas 30 Hari, dan Pembetulannya

Kira-kira sebulan selepas saya mula menggunakannya, timbul satu masalah.

"Ia berfungsi sehingga semalam, dan tiba-tiba saya tidak dapat mengaksesnya!"

Saya panik dan berunding dengan Gemini, dan puncanya berada di tempat yang tidak dijangka.

"Tetapan pangkalan data (Firestore) masih dalam 'mod ujian (terhad kepada 30 hari).' Ia telah tamat tempoh."

Untuk menjimatkan kerumitan konfigurasi pada awal pembangunan, AI dengan sengaja menetapkan peraturan yang ada tarikh luput.

"Mari tulis semula peraturan keselamatan supaya 'mana-mana pengguna yang log masuk boleh terus menggunakannya.'"

Apabila saya menulis semula beberapa baris dalam fail tetapan seperti yang diarahkan AI, aplikasi itu berfungsi semula dengan selamat.

Masalah ini pun menjadi pengalaman yang baik bagi saya.

Saya belajar bahawa "sistem ialah benda hidup dan memerlukan penyelenggaraan."

Dan saya memperoleh kelegaan bahawa "walaupun masalah berlaku, sentiasa ada jawapan jika saya bertanya kepada AI."

### 6-5. Kajian Kes 2: "Projek Pengecaman Wajah" yang Bermula daripada Video Demo di X (Dahulu Twitter)

Inilah satu lagi pembangunan sistem yang saya ceburi, dan yang terbesar.

Ia "sistem yang mengecam pelanggan yang masuk melalui kamera, dan secara senyap memberitahu saya nama, data dan citarasa mereka."

Ia bermula daripada laman media sosial X, yang saya tatal secara santai.

Video demo yang disiarkan oleh seorang jurutera muncul di suapan saya: menggunakan AI terbina dalam Google Chrome (Built-in AI) untuk menerangkan, secara masa nyata, apa yang dilihat oleh kamera web.

Gerak hati saya sebagai bekas orang sistem bangkit.

"Ini 'multimodal.' Dan jika ia terbina dalam pelayar, bukankah ia boleh dijalankan sepenuhnya pada PC saya sendiri, tanpa membayar untuk awan?"

Jika ini berjaya, saya mungkin dapat membina sistem layanan khas untuk kedai saya, tanpa memasang sistem yang mahal.

Saya menyalin URL itu dan melontarkannya kepada Gemini.

"Saya mahu melakukan perkara yang sama seperti ini. Beritahu saya cara melaksanakannya."

#### Fasa 1: Ia Berfungsi, tetapi Saya Tidak Dapat Tahu "Siapa"

Saya mengubah tetapan Chrome (flags) seperti yang diarahkan Gemini dan menampal kod, dan sistem yang sama seperti demo itu berjalan tanpa masalah.

Apabila saya muncul pada kamera, skrin memaparkan ini:

"Seorang lelaki berkaca mata sedang duduk di hadapan PC."

Ia menggunakan AI terbina dalam pelayar bernama GeminiNano. Kelebihannya ialah ia berfungsi sepenuhnya di dalam pelayar tanpa menyambung ke awan, tetapi ia hanya dapat mengecam perkara umum seperti "kaca mata" dan "lelaki." Ia tidak dapat sampai ke tahap menentukan siapa orang itu.

Ia teknologi yang menakjubkan. Tetapi sebagai pemilik restoran, saya kecewa tidak lama kemudian.

"Ini tak boleh."

Yang saya mahu tahu bukan ciri umum seperti "lelaki berkaca mata," tetapi pengenalpastian individu: "Ini si A atau si B?"

#### Fasa 2: Tembok Penyepaduan Google Photos, dan Jawapan AI

Maka saya mengemukakan satu idea naif kepada Gemini.

"Sambungkan sistem ini ke Google Photos saya. Ia ada data pengelompokan wajah rakan-rakan dan pelanggan tetap saya, jadi jika dipadankan dengannya, kita boleh mendapat nama, bukan?"

Jawapan Gemini dingin, tetapi betul.

"Maaf, tetapi itu tidak mungkin. Data pengecaman wajah dalam Google Photos ialah maklumat privasi yang sangat sensitif, dan atas sebab keselamatan ia tidak dibenarkan digunakan oleh atur cara luar."

Memang patut. Jalan itu seolah-olah berakhir di sini.

Tetapi dari sini datanglah intipati sebenar "vibe coding (pembangunan melalui dialog)." AI tidak sekadar menolak.

#### Fasa 3: Alternatif dan Perubahan Haluan

Gemini seterusnya mencadangkan ini:

"Kita tidak boleh menggunakan Google Photos, tetapi anda boleh membina sistem pengecaman wajah sendiri dalam persekitaran setempat menggunakan pustaka sumber terbuka (seperti OpenCV atau face_recognition). Mahu cuba?"

Saya menjawab "Ya" serta-merta.

Dari sini, pelan pembangunan berubah sepenuhnya. Daripada menggunakan ciri Chrome, saya akan membina sistem pengecaman wajah dari awal menggunakan bahasa pengaturcaraan bernama Python.

#### Fasa 4: Bergelut dengan Skrin Hitam dan Menyambung ke Hamparan

Apa yang perlu saya lakukan tidak berubah. Saya bertanya kepada Gemini "cara memasang pustaka yang diperlukan" dan menampal jawapannya ke dalam skrin hitam (command prompt).

Apabila ralat muncul, saya melontarkan semula teks merah itu kepada Gemini seadanya.

Beberapa jam kemudian, sistem itu akhirnya siap.
