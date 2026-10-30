## Pendahuluan

Buku ini adalah catatan per Januari 2026. Sebagian cara saya menjalankan kedai, serta sebagian nama dan spesifikasi alat AI, sudah berubah sejak saat itu. Kelanjutan ceritanya ada di buku kedua, *Dibuat untuk Bar Kami*.

### Mengapa Mantan "Orang Sistem" Berbicara dengan AI di Restoran Bawah Tanah

Terima kasih sudah memilih buku ini.

*Mengelola Kedai Sendirian, dan AI Hadir Mendampingi Saya.*

Saat membaca judul itu, sebagian dari Anda mungkin berpikir, "Itu persis saya." Sebagian lain mungkin bertanya-tanya, "Apa maksudnya AI hadir mendampingi kita?"

Ini bukan buku teknis tentang pemrograman yang rumit. Ini buku untuk Anda, para pemilik restoran yang setiap hari berdiri di dapur, menyiapkan bahan, dan selalu sibuk melayani tamu.

Izinkan saya bercerita sedikit tentang diri saya.

Sekarang saya menjalankan sebuah restoran kecil di ruang bawah tanah sebuah gedung di Higashi-Nakano *(kawasan permukiman di Tokyo bagian barat, tepat di sebelah barat Shinjuku)*, Tokyo.

Restoran ini punya dua wajah. Pada siang hari, tempat ini menjadi kedai khusus kari hamburg steak *(patty daging cincang ala Jepang)* yang harum rempah. Pada malam hari, tempat ini menjadi dining bar dengan sistem rujukan yang menyajikan menu set harian dan minuman.

▼ Quatre Epice Hamburger Curry (Instagram)

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry (Instagram)](images/fig-01.png)

▼ Bar dengan sistem rujukan "Tamuro" (Instagram)

https://www.instagram.com/tamuro.higashinakano/

![Bar dengan sistem rujukan "Tamuro" (Instagram)](images/fig-02.png)

Ruangnya nyaman, hanya dengan 11 kursi konter dan 8 tempat duduk di area tatami yang ditinggikan.

Tetapi kami tidak sekadar menyajikan makanan.

Kami mengadakan acara wine setiap dua minggu, dan sebulan sekali kami merencanakan kelas memasak atau hari hidangan course khusus. Meski di ruang bawah tanah yang sempit, kami sibuk dan bergerak setiap hari.

Tahun ini adalah tahun kedua belas saya menjalankan kedai.

Sebelumnya, saya bekerja sebagai karyawan perusahaan. Pekerjaan saya adalah "perencanaan sistem" dan "arsitektur solusi."

Ketika saya mengatakan itu, orang kadang menanggapi, "Berarti Anda orang yang mengembangkan sistem-sistem hebat." Sebenarnya tidak begitu.

Yang saya lakukan bukan menulis kode program yang sulit. Saya mendengarkan apa yang diinginkan orang-orang di lapangan, menyampaikannya dengan tepat kepada vendor TI (perusahaan pengembang), lalu membuatnya terwujud. Saya adalah seorang "koordinator." Di Jepang, posisi ini dikenal sebagai "orang sistem" (systems guy), penghubung antara lapangan dan tim pengembang.

Staf di lapangan berharap, "Saya ingin pekerjaan saya lebih mudah." Para insinyur berkata, "Kami butuh persyaratan yang terdefinisi secara logis."

Tugas saya adalah berdiri di antara keduanya, menerjemahkan bahasa masing-masing pihak, dan membimbing semua orang menuju tujuan.

Karena itulah saya memahami ketidaknyamanan dan kekhawatiran orang seperti Anda, yang memakai sistem, dan saya juga sedikit memahami apa yang dipikirkan pihak TI.

Saya keluar dari perusahaan dua belas tahun lalu dan membuka kedai sendiri. Sejak itu saya menghadapi kekhawatiran yang sama seperti Anda.

Persiapan yang tidak ada habisnya, kekurangan tenaga kerja, kecemasan soal menarik pelanggan, dan keputusan manajemen yang saya pikul sendirian...

Tentu saja, saat sedang ramai, kadang saya dibantu pekerja paruh waktu dan staf kontrak yang bisa diandalkan.

Tetapi mereka hanyalah mitra untuk "pekerjaan operasional."

Tidak ada orang yang bisa saya ajak berkonsultasi tentang "keputusan manajemen" yang berat, seperti "Bagaimana saya mengatur arus kas bulan depan?" atau "Apakah saya perlu bertaruh pada menu baru ini?"

Saya cemas, memutuskan, dan menanggung semua tanggung jawab. Dalam arti itu, saya selalu "menjalankan kedai sendirian." Dan yang duduk di sisi saya, sebagai teman berdiskusi bagi "saya sebagai pemilik usaha" yang kesepian. Dan sosok itu ternyata adalah AI.

Ke dalam situasi ini masuklah AI generatif, dan khususnya seorang mitra bernama "Google Gemini."

"Koordinasi" yang dulu saya lakukan antara "lapangan" dan "vendor TI," kini saya lakukan sendiri antara "masalah di kedai" dan "AI." Dan saya menyadari sesuatu.

Anda tidak perlu menghafal ejaan bahasa pemrograman yang sulit (seperti Python).\
AI sudah tahu itu. Tetapi cetak biru tentang "apa yang ingin dikerjakan, dan dalam urutan apa" hanya bisa digambar oleh manusia.\
Kemampuan yang saya asah sebagai orang sistem persis adalah "kemampuan menerjemahkan keinginan lapangan menjadi langkah-langkah yang logis."\
Dalam buku ini, saya akan membagikan bukan hanya cara mengoperasikan AI, tetapi juga "naluri logis untuk membuat AI bekerja (pemikiran sistem)" ini, tanpa menyembunyikan apa pun.\
Begitu Anda memilikinya, Anda bisa beralih dari "tanpa pengetahuan" menjadi "pemberi instruksi yang paling andal."

※ Izinkan saya jujur tentang satu hal di sini.

Saya adalah mantan orang sistem. Tetapi dalam pemakaian AI yang diperkenalkan di buku ini, hampir tidak ada saat ketika pengetahuan dari pekerjaan saya sebelumnya benar-benar membantu secara langsung.

Yang membantu bukanlah "keterampilan menulis program."\
Melainkan hanya "kebiasaan mengubah keluhan samar dari lapangan menjadi kata-kata yang berurutan."

Dan kebiasaan ini bukan bakat istimewa.\
Ini "naluri yang sudah dimiliki setiap pemilik yang menjalankan kedai setiap hari."

Dalam buku ini, dengan sengaja saya akan memisahkan apa yang hanya bisa saya lakukan\
dari apa yang bisa Anda tiru persis mulai hari ini.

## Bab 1: Konsep - Agen AI, Jenis Karyawan Baru

~ Pekerjakan AI sebagai "mitra kerja," bukan "teman berdiskusi" ~

### 1-1. Batas Kemampuan Pemilik yang Bekerja Sendirian, dan Kesalahpahaman tentang AI

Menjalankan restoran mandiri seperti kita adalah perlombaan melawan waktu yang tak ada habisnya. Persiapan, memasak, melayani, kasir, bersih-bersih... semuanya harus ditangani oleh satu orang, atau staf dalam jumlah terbatas.\
Bahkan jika kita mempekerjakan staf, kita para pemilik usaha mandiri pada dasarnya menjalankan usaha "serba sendiri."

Itu karena kita tidak punya "manajer kedai" atau "pembimbing" seperti jaringan restoran besar.

Anda memasak sambil memberi instruksi kepada staf pelayanan, mengajari karyawan baru, dan mengatur jadwal.

Semua "pemrosesan mental" ini terkumpul pada satu orang: Anda, sang pemilik.

Tangan Anda mungkin bertambah, tetapi kepala Anda tetap hanya satu. Itulah mengapa Anda butuh AI untuk membantu "kepala" itu.

"Andai saja ada satu staf yang bagus lagi..."

Anda pasti memikirkan itu berkali-kali dalam sehari.

Ketika saya berkata, "Ayo pakai AI," banyak pemilik menjawab seperti ini:

"Maksudmu ChatGPT? Sudah saya coba, tapi ia cuma menulis teks, kan? Tidak berguna untuk pekerjaan di lapangan."

Sebenarnya, di sini ada kesalahpahaman besar.

Sebagian besar AI yang selama ini kita gunakan adalah "chatbot (teman berdiskusi)." Tetapi yang kini dituju oleh AI terbaru, mulai dari Google Gemini, adalah bentuk "agen AI (mitra kerja)."

Keduanya tampak mirip tetapi berbeda. Mari kita bandingkan perbedaannya melalui contoh pekerjaan yang konkret.

### 1-2. Dari "Kamus" menjadi "Anggota Staf"

Misalnya, Anda ingin membuat poster untuk acara kedai.

Dengan AI masa lalu (chatbot):

Jika Anda bertanya, "Beri tahu saya cara membuat poster," AI menjelaskan langkah-langkahnya seperti kamus atau buku pelajaran: "Buat slogan tetap singkat," "Pilih warnanya seperti ini."

Tetapi yang benar-benar bekerja dengan tangan untuk membuat poster adalah Anda. Pengetahuan Anda bertambah, tetapi waktu kerja Anda tidak berkurang.

Dengan AI masa depan (agen AI):

Anda cukup menginstruksikan, "Buatkan poster."

Lalu AI berpikir sendiri untuk mencapai tujuan. Ia memikirkan slogan, membuat gambar latar, bahkan mengusulkan tata letaknya.

Seperti staf yang sangat baik, ia memakai alat, membuat rencana, dan menjalankan pekerjaan itu sendiri.

Yang kita inginkan bukan penasihat yang cuma menyampaikan jawaban normatif, melainkan mitra yang ikut bekerja keras bersama kita.

※ Dalam buku ini, saya akan dengan akrab menyebut mitra yang bisa diandalkan ini (AI generatif seperti Google Gemini) sebagai "wakil manajer (AI)."

※ Dalam buku ini saya memakai "Google Gemini," yang paling sering saya pakai, sebagai contoh, tetapi sebagian besar gagasan yang diperkenalkan di sini dapat diterapkan dengan cara yang hampir sama memakai AI generatif lain seperti ChatGPT dan Claude.

Yang penting bukanlah nama alatnya, melainkan "sikap memperlakukan AI bukan sebagai teman berdiskusi, tetapi sebagai mitra yang bisa diserahi pekerjaan."

### 1-3. "Multimodal" Adalah Penyelamat Restoran

Ada satu kata kunci lagi yang sangat penting dalam menjalankan restoran. Yaitu "multimodal."

Kata ini agak teknis, tetapi artinya sederhana.

Artinya "mampu memahami beberapa jenis informasi sekaligus: bukan hanya teks (membaca dan menulis), tetapi juga gambar (melihat dan menggambar) dan suara (mendengar dan berbicara)."

AI konvensional hanya bisa memahami "kata-kata." Tetapi operasional restoran tidak berjalan hanya dengan "kata-kata."

- Tampilan bahan makanan yang tersisa di kulkas

- Tulisan tangan pada nota pesanan

- Suara pelanggan dan suasana ruangan

- Desain label pada botol wine

Semua ini adalah "informasi nonverbal" yang merepotkan jika harus diubah menjadi kata-kata.

Wakil manajer (AI) dapat mengenali semua ini sebagaimana manusia.

Jika Anda memotret isi kulkas dengan ponsel dan menunjukkannya, AI mengenali, "Oh, masih ada sisa sayuran ini dan daging itu," lalu dapat menyusun menu dari sana.

Dengan kata lain, AI masa kini adalah "wakil manajer yang sangat baik, yang bisa melihat, mendengar, dan berbicara."

※ Tetapi saya tidak ingin Anda salah paham tentang satu hal.\
AI lebih pandai mengatakan hal yang terdengar masuk akal daripada hal yang benar. Untuk pengenalan gambar, angka, tanggal, dan nama diri,\
mohon pakai AI dengan anggapan bahwa manusia selalu melakukan pemeriksaan akhir.

Alasan AI bekerja dengan baik dalam buku ini\
adalah karena saya "tidak menyerahkan semuanya, dan selalu memeriksa langsung di tempat."

### 1-4. Perkuat "Firasat" Anda dengan Data

Kedai-kedai jaringan restoran besar punya data mesin kasir POS dalam jumlah besar dan tim pemasaran.

Sebaliknya, kita para pemilik kedai mandiri punya "firasat" dan "pengalaman" sebagai pemilik. Ini senjata terkuat, tetapi kadang bisa membuat kita terlalu bergantung pada penilaian pribadi atau justru membuat kita ragu.

Maka mari kita tambahkan seorang "wakil manajer."

Minta AI membandingkan intuisi (firasat) Anda, "Saya rasa pelanggan akan suka hidangan ini," dengan "data penjualan masa lalu" dan "informasi tren."

Dengan begitu Anda bisa mempertahankan "kehangatan" dan "keunikan" yang hanya dimiliki kedai mandiri, sekaligus menjalankan usaha yang kuat dan berlandaskan data.

