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

## Bab 2: Dasar-Dasar - "Vibe Coding" dari Nol Pengetahuan

~ Program bukan sesuatu yang Anda "tulis," melainkan sesuatu yang Anda "minta AI buatkan lewat percakapan." ~

### 2-1. Tak Ada yang Membaca "Pesan LINE yang Panjang." Keajaiban "Diagram" yang Selesai dalam 30 Detik

Mendengar kata "membangun sistem dengan AI" mungkin masih terasa seperti rintangan yang cukup tinggi.

Jadi mari kita mulai dari "cara memanfaatkan AI" yang lebih dekat dengan keseharian kita, yang bisa Anda pakai langsung mulai hari ini.

Ini adalah revolusi dalam "memberi instruksi kepada staf."

Banyak dari kita para pemilik memakai LINE *(aplikasi pesan yang paling banyak dipakai di Jepang)* untuk menghubungi staf.\
Biasanya saya menjalankan kedai dengan jumlah orang yang terbatas, dan saat jam sibuk tidak ada waktu untuk memberi instruksi dengan tenang.

Maka penyampaian informasi mau tak mau bergantung pada pesan LINE setelah tutup.

Tetapi sangat sulit menyampaikan hanya dengan kata-kata gambaran "beginilah saya ingin ini dikerjakan" yang hanya ada di kepala saya kepada staf yang kurang berpengalaman atau staf bantuan yang sesekali datang.

Dari situlah "pesan LINE yang panjang" muncul.

Semakin terperinci Anda berusaha menjelaskan, semakin panjang teksnya, dan akibatnya...

"Oh, maaf, saya tidak membaca sampai sejauh itu."

"Isinya teks semua, saya tidak bisa tahu bagian mana yang penting."

Bukankah kesalahan seperti ini terjadi juga di tempat Anda?

Itu terjadi juga pada saya.

Suatu hari, untuk aplikasi yang sedang saya kembangkan, saya mencoba meminta seorang staf mengambil "foto bahan makanan."

Syaratnya agak rumit, sehingga instruksi yang saya ketik di ponsel menjadi pesan panjang seperti ini.

![Pesan LINE panjang yang benar-benar saya kirim kepada staf, lengkap dengan salah ketiknya](images/fig-03.jpg)

Bahkan saat melihat ini, staf dapur yang sibuk akan membacanya sekilas dengan pikiran "Intinya saya tinggal memotret, kan?" dan melewatkan spesifikasi tentang "sudut" dan "arah wadah."

Tetapi saya tidak punya waktu untuk membuka PowerPoint, menyusun berbagai bentuk dan bagan untuk membuat lembar instruksi.

Maka saya memasukkan teks ini apa adanya ke AI (alat AI seperti Manus, atau Gemini) dan meminta:

"Rangkum isi teks ini dalam satu slide, sebagai 'lembar instruksi kerja' yang bisa dipahami staf sekilas."

### 2-2. AI Adalah "Penerjemah yang Hebat"

Setelah menunggu beberapa detik, hasil AI adalah "slide diagram" yang luar biasa mudah dipahami.

![Slide "Instruksi Kerja Pengumpulan Data dan Pemotretan" yang dibuat otomatis oleh AI](images/fig-04.jpg)

Saya tidak merancang apa pun. Saya hanya berkata, "Ini teksnya, tolong rangkum."

Dari tulisan saya yang bertele-tele, AI langsung memahami "apa yang penting" dan "bagaimana seharusnya dikelompokkan," lalu "menerjemahkannya" ke dalam tata letak yang bisa ditangkap manusia secara intuitif.

### 2-3. Bebas dari "Stres karena Pesan Tak Sampai"

Saya menempelkan gambar ini ke LINE dan mengirimkannya.

Efeknya langsung terasa.

Staf itu tidak bertanya apa pun, dan mengirim kembali data foto yang sempurna dalam "orientasi potret" dengan "3 sudut" pada percobaan pertama.

Sebelumnya, saya kesal kepada staf, berpikir "Kenapa mereka tidak mau membaca?" dan khawatir, "Jangan-jangan saya yang menjelaskan dengan buruk."

Tetapi yang patut disalahkan bukan staf, bukan pula saya. Melainkan "komunikasi hanya dengan teks."

Pengalaman ini mengubah cara saya memandang AI.

AI bukan hanya alat untuk "membuat dari nol" teks dan gambar baru.

AI adalah "alat yang 'mengubah' 'kata-kata yang tidak tersampaikan dengan baik' menjadi bentuk yang sampai kepada lawan bicara."

### 2-4. "Vibe Coding," Jenis Dialog Baru

Setelah terbiasa berbicara dengan AI, berikutnya akhirnya adalah "membuat alat."

Anda mungkin berpikir, "Pemrograman mustahil bagi saya," tetapi jangan khawatir.

Saat ini, di kalangan insinyur, istilah "vibe coding" sedang jadi bahan perbincangan.

Ini adalah metode di mana, alih-alih manusia menulis kode yang sulit, Anda membangun sistem dengan berbicara kepada AI seolah menyelaraskan "vibe" (rasa dan suasana).

Sota Fujii, Meijin shogi *(catur tradisional Jepang)* (pemegang gelar), menyebut "vibe coding" sebagai sesuatu yang ia tekuni pada tahun ini, 2025. Bahkan seseorang dari dunia shogi, yang tampaknya sama sekali tak berkaitan dengan membangun sistem, konon menyampaikan keinginannya kepada AI dalam bahasa Jepang dan membuat alat-alat yang praktis.

Dengan berbicara kepada AI, kita pun dapat membangun sistem tanpa pengetahuan khusus.

Yang Anda pakai hanyalah bahasa sehari-hari (bagi penulis, bahasa Jepang). Ketika Anda berkata, "Saya ingin ini bekerja begini" atau "Bagian ini sulit dipakai," wakil manajer (AI) menulis kodenya di balik layar.

Dengan kata lain, Anda tidak perlu menjadi "programmer."

Anda hanya perlu menjadi "pengawas lapangan" yang memberi instruksi kepada "insinyur yang hebat (AI)."

### 2-5. "Keluhan" di Kedai Anda Menjadi Prompt Terkuat

Instruksi kepada AI (prompt) tidak perlu berupa kata-kata yang muluk.

Prompt terkuat yang saya temukan adalah "'ketidaknyamanan' dan 'kekesalan' di kedai Anda, dengan kata lain, keluhan Anda."

- "Repot sekali menghitung ini setiap hari."

- "Saya tidak mau mengubah ukuran gambar secara manual."

Bagi AI, ini sudah merupakan "persyaratan pengembangan" yang sangat memadai.

Perasaan seperti "saya benci ini" lebih mudah memunculkan solusi konkret daripada tujuan seperti "saya ingin melakukan ini."

### 2-6. Error Bukanlah "Kegagalan." Error Adalah "Awal dari Sebuah Dialog."

Ketika mulai membuat sesuatu dengan AI, Anda pasti akan menemui "error."

Tetapi dalam vibe coding, error bukanlah kegagalan.

Error adalah "sinyal bahwa permainan lempar-tangkap dengan AI telah dimulai."

Bahkan antarmanusia, jarang maksud kita tersampaikan sempurna pada percobaan pertama.

Ketika AI memberi error, cukup tepis dengan ringan, "Ah, belum nyambung," lalu sampaikan kembali, "Bukan, yang saya mau itu begini."

Teruskan lemparan bolanya tanpa menyerah. Jika Anda bisa sebatas itu saja, Anda yang mulai dari nol pun pasti dapat membangun "sistem yang hanya milik Anda."

### 2-7. Tingkatkan Efisiensi Secara Dramatis dengan "Tombol Fisik" - Memakai Sub-Keyboard

Dalam vibe coding, yang paling penting adalah "memperhatikan cara memasukkan input."

Semakin cepat percakapan Anda dengan AI, semakin jarang pikiran Anda terhenti, dan semakin cepat pengembangan berjalan. Sebaliknya, jika Anda kerepotan saat memasukkan input, ide sebagus apa pun bisa lenyap.

Tadi saya sudah bilang, "Saat muncul error, langkah yang tepat adalah mengambil tangkapan layar lalu menempelkannya."

Tetapi menekan [Windows] + [Shift] + [S] (Mac: [Cmd] + [Shift] + [4]) puluhan kali sehari, memilih area dengan mouse, kembali ke layar Gemini, lalu menekan [Ctrl] + [V] (Mac: [Cmd] + [V])...

Jujur saja, itu melelahkan jari, bukan?

Maka yang saya pakai adalah "sub-keyboard 6 tombol."

Ini keyboard kecil buatan Tiongkok seharga beberapa ratus hingga sekitar seribu yen, yang muncul jika Anda mencari "programmable keyboard" di Amazon atau situs sejenis.

![Foto sub-keyboard 6 tombol yang saya pakai](images/fig-05.jpg)

Pada keenam tombol ini saya menetapkan pintasan berikut.

1.  Mengambil tangkapan layar

2.  Pilih semua (Ctrl + A; Mac: Cmd + A)

3.  Salin (Ctrl + C; Mac: Cmd + C)

4.  Tempel (Ctrl + V; Mac: Cmd + V)

5.  Enter (kirim)

6.  (Cadangan)

Hanya itu. Tetapi efeknya dramatis.

Muncul sebuah error.

↓

Dengan tangan kiri, saya menekan "Tombol 1 (tangkapan layar)."

↓

Saya memilih area, lalu menekan "Tombol 4 (tempel)" di layar Gemini.

↓

Tekan "Tombol 5 (kirim)."

Semua ini hanya memakan waktu 2 detik.

Anda tidak perlu mengingat pintasan keyboard atau menggerakkan jari secara rumit.

Anda bisa melempar informasi ke AI seperti memainkan controller game.

Seperti yang akan Anda lihat di bab-bab berikutnya, ketika Anda memperbaiki kode sumber yang dikeluarkan AI, pilih semua (Ctrl + A), salin (Ctrl + C), dan tempel (Ctrl + V) memungkinkan Anda menjalankannya lagi seketika, dan itu praktis.

Sebelum Anda mempelajari pengetahuan pemrograman tingkat lanjut, cobalah dulu memiliki satu perangkat kecil ini.

Menghilangkan secara fisik "kerepotan memasukkan input." Itulah jalan pintas paling pasti untuk mempercepat percakapan dengan mitra AI Anda.

## Bab 3: Praktik 1 - Mengotomatiskan Pekerjaan Kreatif dan Menarik Pelanggan

~ "Tempel tangkapan layar lalu serahkan semuanya" ternyata metode pengembangan terkuat ~

### 3-1. Coba-Coba untuk Menghapus "Kesan AI" (Stiker LINE)

Setelah terbiasa berdialog lewat teks (vibe coding), akhirnya saya memutuskan menjajal "pembuatan gambar."

Sebagai latihan, saya memilih membuat "stiker LINE," yang juga bisa membantu membangun penggemar bagi kedai.

Tetapi "gambar mulus ala CG" yang khas pada gambar buatan AI tidak cocok dengan suasana kedai saya.

Yang saya incar adalah "desain flat ala tahun 1980-an yang retro, dengan nuansa gambar tangan, mempertahankan tekstur krayon dan kuas."

Dari sinilah dimulai "dialog" panjang antara saya dan wakil manajer (AI).

Pada awalnya, saya mulai dengan karakter "dua anak laki-laki dan seekor anjing Shiba Inu."

"Buatkan 25 pola percakapan sehari-hari."

"Buat ketebalan garisnya acak, seperti goresan kuas."

Satu per satu, seperti memberi instruksi revisi kepada ilustrator manusia, saya dengan sabar mengajarkan selera yang saya sukai.

![Ilustrasi yang dibuat untuk stiker LINE](images/fig-06.png)

### 3-2. Permintaan Berani: "Ubah Hanya Anjingnya Menjadi Kucing"

Setelah semuanya mulai berbentuk, saya memutuskan perubahan arah besar: "Sebenarnya saya ingin gadis-gadis dan seekor kucing."

Ilustrator biasa mungkin akan cemberut dan berkata, "Apa, mulai dari awal lagi?" Tetapi wakil manajer (AI) tidak mengeluh sekali pun.

"Ubah karakternya menjadi dua gadis, satu berambut panjang dan satu berambut pendek. Pakaian berwarna kuning dan hijau, dengan gaya gambar tangan yang sama seperti sebelumnya."

"Ubah anjingnya menjadi kucing, ganti kata-katanya dengan bahasa kucing yang tadi Anda buat, dan buat pose yang sesuai."

"Jadikan kucingnya kucing Siam, bukan kucing tabby oranye."

Selain itu, saya mengajukan permintaan yang menguji batas AI.

"Pertahankan persis komposisi 'anak laki-laki dan anjing Shiba Inu' yang tadi Anda buat, dan ganti hanya bagian anjingnya dengan kucing Siam."

Yang mengejutkan saya, AI memahami instruksi yang rumit ini. Posisi dan pose anak laki-laki tetap sama, sementara orang-orang dan hewannya diganti dengan rapi menjadi "kucing Siam."

![Lembar ilustrasi jadi untuk stiker LINE](images/fig-07.png)

Namun, untuk memakainya sebagai stiker di LINE, Anda perlu memotong ilustrasinya, membuat thumbnail, memampatkan semuanya ke dalam ZIP, dan mengunggahnya.

Ini pun bisa dilakukan lewat dialog dengan Gemini, tetapi akan saya jelaskan lagi nanti di 3-6. Rintangan Pertama: Pemotongan Sederhana dan "Jebakan Kualitas Gambar."

### 3-3. Kasus 2: "Banner Natal" yang Dibuat dalam 22 Putaran Dialog

Setelah stiker LINE, ada satu karya besar lagi yang saya buat bergandengan tangan dengan AI. Yaitu banner pengumuman untuk "makan malam Natal," acara terbesar tahunan kedai.

Saya memakai sebuah AI bernama "Nano Banana" (model pembuat gambar yang terpasang di Gemini milik Google).

#### Fase 1: Menyesuaikan Tata Letak dan Teks

Pada awalnya, saya mulai dengan menempatkan elemen-elemen yang diperlukan (Sinterklas, rusa kutub, informasi teks) pada kanvas lebar.

Sambil melihat gambar yang dihasilkan, saya memberi instruksi.

"Rasanya agak kosong. Tambahkan ilustrasi pohon Natal dan sampanye."

"Menunya berupa daftar berpoin dan sulit dibaca. Ringkas menjadi 'enam hidangan seluruhnya,' dan buat judulnya lebih besar dan lebih mencolok."

![Gambar yang dihasilkan pada tahap awal. Masih terlihat agak kosong](images/fig-08.png)

#### Fase 2: Menyetel "Kemeriahan"

Setelah tata letak ditentukan, berikutnya adalah suasana. Gambar itu kurang "nuansa pesta."

Saya menginstruksikan, "Buat lebih meriah! Taburkan banyak Sinterklas kecil dan rusa kutub, balon, dan konfeti."

Kali ini layarnya menjadi terlalu penuh.

"Maaf, elemennya terlalu banyak. Kurangi dulu karakternya agar tampilannya bersih."

Kemampuan mengulang penyetelan halus "menambah dan mengurangi" ini adalah kekuatan AI.

#### Fase 3: Gagasan Tak Terduga tentang "Mengulang Seluruhnya"

Di tengah pembuatan, muncul keraguan. "Bukankah akan tampak lebih lezat jika menampilkan gambar makanan daripada menjadikan karakter sebagai fokus utama?"

Maka saya berani menginstruksikan, "Sebagai alternatif, buat desain yang menampilkan ilustrasi hidangan sebenarnya sebagai elemen utama."

![Usulan ilustrasi yang menampilkan hidangan (sebagian teks kacau)](images/fig-09.png)

AI langsung menghasilkan ide ilustrasi makanan yang menggugah selera, tetapi setelah membandingkan, saya memutuskan tetap memakai desain karakter yang semula. Bahkan permintaan "ayo kembali ke yang tadi" seperti ini bisa diajukan kepada AI tanpa ragu.

#### Fase 4: Garis Pertahanan Terakhir adalah Mata "Manusia"

Setelah desain akhir diputuskan, saya juga menyerahkan variasi ukuran kepada AI, untuk unggahan Instagram (vertikal) dan untuk Stories (lebih tinggi lagi).

Dan tepat ketika hampir selesai, saya menyadari kesalahan serius.

"Tunggu, hari dalam seminggu pada tanggalnya salah!"

AI pandai menggambar, tetapi tidak memahami hari dalam seminggu pada kalender. Seandainya saya mengunggahnya apa adanya, itu akan jadi bencana.

Saya buru-buru menginstruksikan, "Perbaiki tanggalnya menjadi '12/24 (Rabu) dan 25 (Kamis)'!" lalu menyelesaikan versi akhirnya.

![Banner akhir setelah dikoreksi](images/fig-10.png)

Total 22 putaran revisi dan dialog.

AI bukan tongkat sihir, tetapi jika Anda berbicara dengannya dengan sabar, tidak ada mitra desain yang lebih bisa diandalkan.

### 3-4. Kasus 3: Pengumuman Buka di Tahun Baru yang Berkembang Mengikuti Situasi

Semarak Natal baru saja mereda ketika acara berikutnya tiba: operasional akhir tahun dan Tahun Baru.

Bagi restoran atau bar, menyebarkan kabar pada masa ini adalah perlombaan melawan waktu. "Sampai kapan buka di akhir tahun?" "Kapan buka lagi di tahun baru?" Pelanggan selalu mencari informasi.

Tetapi informasi berubah setiap saat.

"Setelah layanan akhir tahun selesai, saya ingin menulis ulang agar hanya menampilkan pengumuman Tahun Baru."

"Saya sudah mengunggahnya di X (lanskap), tetapi saya ingin menayangkannya juga di Instagram (potret)."

Jika saya meminta desainer luar mengerjakan ini, biaya revisinya saja sudah mimpi buruk, dan terutama tidak akan selesai tepat waktu.

Maka sekali lagi saya bekerja sama dengan AI pembuat gambar (Nano Banana) dan mulai membuat banner untuk menemani saya melewati akhir tahun dan Tahun Baru.

#### Langkah 1: Gayanya "Gambar Krayon Tahun 80-an"

Pertama, saya membangun tampilan dan nuansa keseluruhan.

Yang cocok untuk bar saya bukan CG yang mengilap.

"Gaya hangat seperti gambar krayon tangan era 80-an, dengan goresan kuas yang terlihat. Biarkan latarnya putih polos."

Dengan instruksi ini sebagai inti, dan dengan pengumuman di X (dulu Twitter) dalam benak, saya mulai bekerja pada kanvas lanskap.

#### Langkah 2: Ular yang Pergi dan Kuda yang Datang. Bersulang untuk Menyerahkan Tongkat Estafet

Awalnya saya berpikir menggambar hanya satu hewan shio, tetapi ini bagaimanapun adalah pergantian tahun.

Saya punya gagasan: "Saya ingin hewan tahun yang pergi (shio tahun ini) dan hewan tahun yang datang (tahun depan) sama-sama muncul."

Jadi saya memberi AI instruksi ini:

"Taruh sekelompok ular (tahun Ular) di sisi kiri layar dan sekelompok kuda (tahun Kuda) di sisi kanan. Suruh masing-masing memegang gelas bir dan bersulang dengan riang, seolah menyerahkan tongkat estafet di akhir tahun."

Gambar yang dihasilkan AI persis seperti yang saya bayangkan.

Ular-ular yang menggemaskan di kiri, kuda-kuda yang tampak bisa diandalkan di kanan, minum bersama melintasi batas antarspesies.

Dari "akhir tahun (Ular)" menuju "Tahun Baru (Kuda)."

Dalam satu gambar, berlalunya waktu dan suasana perayaan terangkum dengan indah.

![Gambar buatan berupa ular di kiri dan kuda di kanan yang bersulang, mengungkapkan tahun lama yang digantikan tahun baru](images/fig-11.png)

#### Langkah 3: "Pengarahan Akting" dan "Pencocokan Kostum" untuk Para Hewan

Setelah komposisi ditetapkan, pekerjaan berikutnya adalah penataan yang lebih halus. Di sini pun AI dengan setia meladeni perhatian saya pada detail.

Pada gambar-gambar pertama, hewan-hewan itu hanya berdiri berjajar, atau memegang gelas dengan cara yang tidak wajar.

"Buat mereka tampak lebih bahagia! Seperti pelanggan tetap yang bersenang-senang bersama."

"Saya juga ingin nuansa musiman. Pakaikan syal dan dasi kupu-kupu, beri tampilan musim dingin."

Dengan satu ucapan itu, hewan-hewan di layar membungkus diri dengan syal merah dan hijau yang tampak hangat dan seketika berubah menjadi bintang "pesta musim dingin."

"Ya, sekarang ada perasaan hangat khas minum di siang hari saat cuaca dingin."

Jika diamati dengan saksama, sebagian gerakan tangan dan cara memegang gelas masih tidak wajar. Tetapi terlalu terpaku pada detail berarti memakan lebih banyak waktu. Menimbang waktu dan seberapa baik pesannya tersampaikan, saya menerima hasil yang cukup baik.

#### Langkah 4: Seiring Waktu Berlalu, Informasi Berubah

Dari sini adalah bagian ketika AI benar-benar menunjukkan nilainya.

Banner aslinya menampilkan jadwal Desember dan Januari sebagai "Jadwal Operasional Akhir Tahun dan Tahun Baru."

Tetapi setelah 31 Desember lewat, informasi akhir tahun tidak diperlukan lagi.

Saya membuka proyek yang sedang saya kerjakan dan meminta perubahan besar pada teksnya.

1.  Ubah judul: dari "Jam Buka Akhir Tahun dan Tahun Baru" menjadi "Buka Minum Siang di Tahun Baru."

2.  Rapikan informasi: hapus jadwal Desember yang sudah lewat dan persempit menjadi hanya "jadwal Tahun Baru (2–4 Januari)."

3.  Perbaiki karakter shio: ubah ular tahun yang pergi menjadi kuda.

4.  Tambahkan daya tarik: tambahkan penawaran menarik, "highball dan ayam goreng sepuasnya," sebagai daya tarik baru bagi pelanggan.

![Langkah 4: Seiring Waktu Berlalu, Informasi Berubah](images/fig-12.png)

Tanpa membuat ulang gambar dari awal, saya bisa menyegarkan informasinya seolah menulis ulang kata-kata di papan tulis. Itulah kekuatan desain AI.

#### Langkah 5: Dari X ke Instagram. Format yang Berubah dengan Luwes

Dan sekarang, sentuhan akhir.

"Saya sudah mengumumkannya di X. Berikutnya saya ingin menayangkannya di Instagram Stories."

Tetapi Stories memakai ukuran "potret" yang memenuhi seluruh layar ponsel. Jika Anda memasukkan gambar lanskap apa adanya, akan ada ruang kosong di bagian atas dan bawah, dan tampilannya buruk.

Dengan ilustrasi biasa, perubahan semacam ini berarti menggambar ulang.

Tetapi yang saya lakukan hanya mengatakan kepada AI:

"Pertahankan desain ini, tetapi susun ulang menjadi tata letak potret untuk Instagram Stories."

AI menata ulang hewan-hewan yang tadinya tersebar ke samping menjadi susunan vertikal, menyesuaikan keseimbangan teksnya, dan seketika menghasilkan desain yang pas untuk ponsel.

![Gambar potret jadi untuk Instagram Stories](images/fig-13.png)

### 3-5. Kasus 4: Membuat Logo Bar - Dialog yang Mengubah "Makna" menjadi "Bentuk"

Selain "gambar" seperti banner dan stiker, saya juga menjajal tantangan yang lebih abstrak bersama AI: merancang logo baru.

Logo ini dimaksudkan untuk disematkan pada banner dan sejenisnya, agar orang bisa mengenali Tamuro sekilas.

Subjeknya adalah Tamuro, bar dengan sistem rujukan yang saya kelola pada malam hari. Nama ini membawa harapan yang kuat: "menjadi tempat berkumpulnya berbagai macam orang dengan bebas dan gembira (tamuro-suru, nongkrong) di kota Higashi-Nakano."

Bagaimana cara memadatkan "cerita" yang tak kasatmata ini menjadi sebuah logo yang kecil? Dimulailah dialog yang sabar dengan AI.

#### Langkah 1: Memilih Huruf dan Arah Desain

Pada awalnya saya melemparkan ide kepada AI, seperti "tampilan sederhana dengan kanji 屯" dan "sesuatu yang pop dengan katakana," lalu memintanya membuat beberapa draf kasar.

Tetapi tidak ada yang terasa pas. Mengingat sifat bar ini, saya menginginkan sesuatu yang lebih modern, dengan nuansa netral yang menyambut keberagaman.

Maka saya mengubah arah.

"Mari kita berpijak pada alfabet yang sangat serbaguna, 'TAMURO.' Gayanya 'flat design' tanpa hiasan yang rumit. Dan warnanya harus tetap tampak kuat meski hanya satu warna."

AI segera mengusulkan "TAMURO" bergaya sans-serif yang sederhana dan tebal.

![Logo bergaya sans-serif](images/fig-14.png)

#### Langkah 2: Menghembuskan "Makna" ke dalam Bentuk

Di sinilah ujian sesungguhnya dimulai. Huruf polos tidak bermakna apa-apa. Dan hanya dengan "M" di tengah pun tidak banyak yang tersampaikan.

"Saya ingin mengungkapkan asal nama itu, 'orang-orang berkumpul.' Bisakah Anda menyusun keseluruhannya menjadi bentuk 'lingkaran' yang ramah, sambil membentuk setiap huruf alfabet agar tampak seperti orang yang bergerak riang?"

Ini permintaan yang sangat abstrak. Tetapi imajinasi wakil manajer saya (AI) melampaui harapan saya.

Yang dihasilkan AI adalah desain di mana kerangka huruf "T," "A," "M," dan lainnya diubah menjadi siluet orang yang menari dengan tangan dan kaki terentang.

![Logo yang memetakan alfabet menjadi orang-orang](images/fig-15.png)

#### Langkah 3: Tarik Tambang antara Desain dan Keterbacaan

"Menarik! Tetapi kalau begini, kita tidak bisa membaca 'TAMURO'..."

Jika terlalu menekankan desain, ia tak lagi dikenali sebagai huruf, dan jika menekankan hurufnya, daya tariknya hilang. Saya menghadapi dilema ini.

Dari sini, pekerjaannya adalah penyetelan halus yang berulang.

"Huruf 'A' tampak seperti orang, dan itu bagus, tetapi tekankan sedikit lagi strukturnya sebagai 'A.' Buat palangnya tegas."

"Keseimbangan keseluruhannya bagus, tetapi orang-orangnya terlalu rapat dan tampak sesak. Sisakan sedikit ruang yang ceria."

"Gabungkan orang-orang yang menari tadi dengan huruf TAMURO, dan jadikan lingkaran!"

![Logo "TAMURO" berbentuk lingkaran, selesai setelah coba-coba](images/fig-16.png)

Meski terbuat dari siluet orang yang bersemangat, sekali melihat bagian bawahnya, Anda bisa membaca "TAMURO" dengan jelas.

Dengan melempar ide bolak-balik bersama AI berkali-kali, saya mendapat logo yang saya sukai, yang memadukan keterbacaan, mutu desain, dan terutama "harapan" yang saya taruh pada bar ini.

Logo ini sekarang dipakai sebagai ikon untuk akun X (dulu Twitter) dan Instagram bar.

### 3-6. Rintangan Pertama: Pemotongan Sederhana dan "Jebakan Kualitas Gambar"

Tantangan kreatif membuat logo telah selesai.

Tetapi pekerjaan belum selesai.

Kembali ke stiker LINE. Yang saya pegang adalah sebuah "lembar" dengan 25 ilustrasi yang digambar pada satu halaman.

Untuk mendaftarkannya sebagai stiker LINE, saya harus memotong masing-masing, membuat latarnya transparan, dan mengubah ukurannya. Itu pekerjaan melelahkan yang terus saya tunda.

"Tidak mungkin saya memotong semua ini dengan tangan..."

Saya berkonsultasi dengan Gemini dan meminta solusi. Gemini berkata dengan enteng:

"Mari kita otomatiskan memakai bahasa pemrograman bernama Python."

Terus terang, saya hampir menyerah saat itu juga.

"Python? Namanya pernah dengar, tapi memasang perangkat lunak seperti itu di komputer saya menakutkan. Penyiapannya juga kedengarannya sulit. Tolong jangan berharap sebanyak itu dari orang yang mengelola bar..."

Tetapi ini salah satu bagian terpenting buku ini. Seolah merasakan apa yang saya pikirkan, Gemini membuat saran yang mengejutkan.

Gemini:

"Anda tidak perlu menyiapkan lingkungan pengembangan apa pun. Gunakan alat gratis dari Google yang bernama 'Google Colab.' Alat ini berjalan di browser Anda, jadi yang perlu Anda lakukan hanyalah menyalin dan menempelkan kode yang saya tulis ke dalamnya."

"Apa? Ada yang seperti itu?"

Saya hampir tidak percaya mendengarnya. Saya tak pernah membayangkan ada lingkungan pengembangan tempat pemrograman berjalan hanya di browser, tanpa memasang apa pun di PC saya.

Bukan "setelah saya belajar Python," melainkan "dengan AI mengajari saya bahkan tentang keberadaan alat itu (Colab)."

Pada saat itu, anggapan saya bahwa "pemrograman berarti banyak persiapan" runtuh.

### 3-7. Jangan "Baca" Layar Error, "Potret dan Kirim"

Sesuai petunjuk, saya membuka Google Colab, menempelkan kodenya, dan menekan tombol "Run" (jalankan).

Namun kenyataannya tidak semudah itu. Yang muncul di layar adalah deretan teks merah menyala... pesan error.

"Error: Image file not found..."

Saya yang dulu akan langsung alergi hanya dengan melihat error ini dan langsung menutup browser begitu saja.

Tetapi sekarang saya punya sekutu: AI "multimodal," AI yang punya mata.

Saya bahkan tidak mencoba membaca pesan error itu.

Saya hanya mengambil tangkapan layar dan menempelkannya begitu saja ke kotak obrolan Gemini.

Dan saya menambahkan satu baris: "Muncul semacam error."

![Menempelkan layar error Google Colab apa adanya ke Gemini](images/fig-17.png)

Gemini segera menganalisis gambar itu dan mengirim jawaban.

Gemini:

"Ah, nama file gambar yang dimuat salah. Saya sudah memperbaiki kodenya agar memakai '.jpg'. Silakan jalankan lagi dengan versi ini."

"...Wah, ini seru!"

Alih-alih seperti memprogram, pertukaran ini lebih terasa seperti permainan "cari perbedaan" atau permainan lempar-tangkap.

- Saya: (menempelkan tangkapan layar) "Berhenti lagi."

- Gemini: "Ukuran gambarnya tidak cocok. Saya akan menambahkan fungsi yang menyesuaikannya secara otomatis."

- Saya: (menempelkan tangkapan layar) "Kali ini gambarnya tampak kasar."

- Gemini: "Saya lupa menambahkan proses bernama 'LANCZOS' yang menjaga kualitas gambar. Saya perbaiki."

Saya tidak mengerti satu baris pun dari kodenya. Saat muncul error, saya hanya mengambil tangkapan layar dan melemparkannya ke AI dengan "Lihat!"

"Menyerahkan analisis error" ini adalah rahasia terbesar bagaimana saya, dengan nol pengetahuan, berhasil membangun sebuah sistem, dan sekaligus merupakan pengalaman paling mendebarkan dari semuanya.

### 3-8. Tembok Terbesar: "Ketidaksejajaran Gambar Tangan" dan "Keluar Garis"

Seiring saya melanjutkan "percakapan bernama error" ini, sistemnya menjadi semakin halus.

Dan akhirnya saya memasuki tantangan terbesar: "Fase 2: Pemotongan Otomatis Tata Letak Gambar Tangan."

Saya jadi ingin bereksperimen lebih jauh.

"Mari buat lembar 5×5, 25 stiker. Dan karena saya menginginkan nuansa buatan tangan yang lebih kuat, saya ingin menempatkannya dengan bebas, tanpa terikat garis kisi."

Dengan kode yang sekadar membagi lembar secara rata, tangan atau tulisan sebuah karakter menjorok keluar ke sel sebelah dan terpotong dengan menyedihkan.

Saya juga mencoba metode "memotong semuanya kecuali latar putih," tetapi marginnya tidak rata dan gagal.

Saya nyaris menyerah. Lalu, dengan memanfaatkan naluri dari masa saya sebagai orang sistem, saya berkata kepada Gemini:

"Saya ingin Anda meninggalkan gagasan memotong gambar dengan gunting. Sebagai gantinya, lihat di sel mana 'titik pusat' setiap gambar berada. Jika pusatnya di sel itu, maka meski sedikit keluar garis, perlakukan seluruh gambar sebagai 'milik sel itu' dan masukkan ke dalam ember sel tersebut."

Inilah solusi yang saya beri nama "metode ember kisi."

Mengapa saya terpikir "memasukkan ke ember berdasarkan titik pusat" alih-alih "memotong dengan gunting"?

Cara berpikir orang awam (analog): Anda membayangkan "menggunting satu gambar dengan gunting." Dengan cara itu, Anda memotong tepat di sepanjang garis, dan tangan serta kaki karakter terpotong.

Cara berpikir orang sistem (digital): Komputer tidak punya rasa fisik tentang "memotong." Sebagai gantinya, ia punya "koordinat (posisi)." Beginilah cara saya melihatnya: "Meski sedikit meluap, selama 'pusar (titik pusat)' gambar berada di dalam sel, kita bisa menganggap seluruh gambar 'milik sel ini.'"

![Gagasan analog "memotong di sepanjang garis" dan gagasan digital "memilih berdasarkan titik"](images/fig-18.png)

Inilah arti "menerjemahkan pekerjaan analog yang samar menjadi aturan digital yang jelas." Saat Anda memberi instruksi kepada AI, memikirkan aturan seperti ini, yang jawabannya keluar sama "siapa pun yang melihat (atau menghitung)," sangat efektif.

Gemini mengubah permintaan abstrak ini menjadi kode dengan indah. Hasilnya sempurna.

Tulisan "Terima kasih!" dan ekor-ekor yang tadinya keluar ke sel-sel tetangga semuanya dikenali dengan bersih dan dikumpulkan sebagai stiker tunggal.

Ia bahkan memenuhi permintaan egois saya, "Yang terakhir (ke-25) tidak diperlukan, jadi lewati." Akhirnya saya punya alat yang "tinggal memasukkan gambar dan menekan tombol, maka terbentuk satu set gambar lengkap untuk pengajuan stiker LINE."

Yang saya lakukan hanyalah menyampaikan "masalah di lapangan (gambar terpotong)" dan mengusulkan "solusi logis (menentukan berdasarkan titik pusat)." AI menulis semua kode yang sulit.

Inilah inti dari "vibe coding," membangun sistem mulai dari nol pengetahuan.

#### Ringkasan Bab 3

1.  Menggambar dengan AI bukan "sekali jadi." Anda bisa membuat ulang sebanyak yang Anda mau sesuai situasi: mengganti karakter, menambah nuansa musiman, berganti media.

2.  Bahkan "konsep (orang-orang berkumpul)" yang abstrak dapat diubah menjadi "bentuk (logo)" lewat dialog berulang.

3.  Pekerjaan yang merepotkan (memotong gambar) justru dapat diotomatiskan oleh Gemini × Google Colab. Error bisa diselesaikan dengan tangkapan layar.

#### Kolom 1: Kursus Kilat "Google Colab" untuk Pemilik Usaha yang Awam Teknologi

~Pakai "dapur sewaan" dan biarkan PC Anda apa adanya~

"Google Colab," yang muncul dalam isi utama. Melakukan pemrograman (Python) di komputer sendiri seperti "membuat ramen otentik dari nol, mulai dari kuahnya, di dapur rumah." Persiapannya sangat merepotkan.

Google Colab, di sisi lain, adalah "dapur sewaan gratis yang peralatan masaknya lengkap." Cukup buka browser dan alat terbaik sudah siap. Anda tidak perlu mengubah pengaturan apa pun di komputer. Anda bisa memprogram hanya dengan browser sambil menjaga komputer Anda tetap bersih. Pertama, cari "Google Colab" dan intiplah dapur sewaan ini.

#### Kolom 2: Tidak "Membaca" Layar Error adalah Jawaban yang Benar

~Kuasai senjata pamungkas: tangkapan layar~

Saat muncul error, apakah Anda bersungguh-sungguh mencoba menguraikan pesan berbahasa Inggrisnya? Itu buang-buang waktu.

Saat rasa masakan terasa janggal ketika memasak, Anda meminta koki mencicipinya. Dengan cara yang sama, cukup tunjukkan kepada AI sebuah "tangkapan layar (screenshot)."

- Windows: \[Win\] + \[Shift\] + \[S\]

- Mac: \[Cmd\] + \[Shift\] + \[4\]\
  Tekan tombol-tombol ini, gambar kotak di sekitar error, lalu tempelkan ke Gemini. Hanya itu. Jangan "baca errornya," "tunjukkan errornya." Hanya dengan mengubah pola pikir seperti ini, kecepatan pengembangan Anda akan menjadi tiga kali lipat.

Saya sudah memperkenalkan beberapa contoh sejauh ini, dan semua yang saya lakukan bermuara pada tiga hal berikut.

・Jangan menuntut bentuk jadi sekaligus (anggap saja ini sebuah dialog)\
・Katakan "bukan, bukan begitu" tanpa ragu\
・Anggap biaya revisi nol dan lemparkan permintaan dengan santai

Anda tidak butuh bakat desain. Yang Anda butuhkan hanyalah keberanian untuk mengungkapkan "ada yang mengganjal" dengan kata-kata.

## Bab 4: Praktik Bagian 2 - Membuat Pekerjaan Harian Lebih Efisien (Memakai AI Multimodal)

~Selesaikan "pemasukan data yang membosankan" hanya dengan satu ponsel~

### 4-1. Masalah dalam Memperbarui Daftar Wine

Bagi pemilik bar atau restoran, memperbarui buku menu adalah beban yang tidak glamor tetapi berat.

Yang paling merepotkan saya adalah membuat "daftar wine."

Setiap kali ada wine baru yang datang, pekerjaan berikut ini diperlukan.

1.  Melihat label botol (tulisan bersambung berbahasa asing, sulit dibaca).

2.  Mengetik nama merek dan vintage (tahun) ke PC tanpa kesalahan.

3.  Mencari karakteristik dan rasa wine itu secara daring.

4.  Menulis "deskripsi" yang membuat pelanggan ingin membacanya.

5.  Memikirkan hidangan yang cocok dengan wine itu (pairing).

Melakukan semua ini sambil membuka kamus, di sela-sela jam operasional yang sibuk, hampir mustahil. Saya menundanya dengan "nanti saja," dan daftar rekomendasi pun sering tidak pernah diperbarui.

### 4-2. Cukup Potret dengan Ponsel. Kejutan dari "Gem Daftar Wine"

Maka saya memutuskan mencoba "fitur multimodal (pengenalan gambar)" milik Gemini.

Caranya begitu mudah sampai membuat saya terheran-heran.

1.  Potret botol wine dengan ponsel Anda.

2.  Kirim foto itu ke Gemini.

3.  Tambahkan satu baris: "Jadikan daftar."

Hanya itu.

![Foto label botol wine sungguhan yang diambil dengan ponsel](images/fig-19.jpg)

Gemini lalu langsung membaca informasi label dari foto itu.

Ia tidak hanya menyalin nama merek, seperti "Cave d'Occi Winery, Tsukimi de Ippai 2024," tetapi juga mencari karakteristiknya di basis data daring yang sangat besar dan secara otomatis menghasilkan deskripsi yang menarik.

Yang lebih mengejutkan saya, ia juga mengeluarkan "saran pairing" sekaligus.

Saran seperti "Aroma kaya wine ini cocok dengan ○○" muncul di layar dalam hitungan detik.

Jam-jam yang dulu saya habiskan bergulat dengan kamus kini menyusut menjadi satu klik rana ponsel.

### 4-3. Membuat "Gem" Anda Sendiri

Agar pekerjaan ini jauh lebih efisien, saya melanjutkan dengan memakai fitur bernama "Gems."

Ini adalah "fitur AI kustom milik Anda sendiri" di mana Anda dapat membuat AI menghafal peran dan aturan tertentu sebelumnya.

Menjelaskan segalanya dari awal setiap kali, "Anda adalah seorang sommelier. Lihat foto ini dan..." sangat merepotkan.

Maka saya mendaftarkan "instruksi (prompt)" berikut kepada Gemini lebih dulu. Inilah isi kepala "AI sommelier khusus" bar saya.

#### Instruksi yang Benar-Benar Saya Daftarkan

> Baca gambar dan buat daftar wine dalam format berikut.
>
> Untuk harga, jangan pakai harga pasar. Hitung dengan mengasumsikan harga botol di restoran pada umumnya (sekitar 2,5 sampai 3 kali harga pokok).
>
> Jangan pakai format tabel. Buat agar muat dalam satu atau dua lembar kertas A4.
>
> Format ini hanya sebagai acuan; buat daftar hanya dengan apa yang telah dimasukkan.
>
> Formatnya di bawah ini.
>
> Inggris 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8.500 (sekitar $57)
>
>  Emas pucat dengan gelembung yang menyenangkan. Sentuhan melon dan madu di antara aroma sitrus... (sisanya dihilangkan)

Sebenarnya, bagian bawah prompt ini, bagian "format (contoh)."

Saya tidak memikirkannya dari nol.

Dulu, saat mencari informasi wine secara daring, saya sering berpikir, "Oh, deskripsi kedai ini mudah dipahami," atau "Cara situs ini menulis membuatnya terdengar lezat," dan saya terus-menerus menyalin dan menempelkan kutipan seperti itu ke notepad.

Saya melemparkan "memo tambal sulam" itu apa adanya ke Gemini.

"Ini adalah kutipan yang dulu saya salin dan kumpulkan. Tirulah nuansanya dan tulis juga tentang wine di foto yang baru."

Hanya itu yang saya katakan.

Meski begitu, instruksi ini mengandung tiga trik yang mengurangi beban di lapangan.

① "Logika perhitungan harga"

Ini penghemat waktu terbesar. Karena saya menginstruksikan "harga yang akan ditagih restoran" alih-alih "harga pasar," AI menghitung mundur dari harga beli yang lazim dan memberi saya angka seperti "¥8.500 (sekitar $57)" yang bisa langsung masuk menu. (Tentu keputusan akhir ada di tangan pemilik, tetapi punya patokan membuat segalanya lebih mudah.)

② "Bukan format tabel, tetapi muat di kertas A4"

Jika keluarannya berformat tabel seperti Excel, tata letaknya berantakan saat ditempelkan ke buku menu. Dengan memintanya menulis dalam "format menu A4" sejak awal, saya mengincar keluaran yang bisa dicetak dan dipakai apa adanya.

③ Memakai teks web hasil salin-tempel sebagai "contoh"

Alih-alih meminta secara samar, "Tulis deskripsi yang bagus," saya menunjukkan contoh konkret (memo salin-tempel saya): "bendera 🇬🇧 + nama wine + harga + deskripsi yang menggugah indra."

Ketika AI diperlihatkan contoh, ia memahami, "Oh, begini nada dan gaya yang harus saya tulis," dan akurasi keluarannya melonjak. Dalam istilah teknis ini disebut "few-shot prompting," tetapi pada dasarnya sama dengan "mengajar lewat teladan, dengan membiarkan orang melihat punggung kita saat bekerja."

Dan "punggung" itu sangat boleh terbuat dari teks temuan, padanan tertulis dari foto temuan dari web.

![Teks daftar wine jadi yang dikeluarkan Gemini](images/fig-20.png)

### 4-4. Tak Harus Gambar. Revolusi Salin-Tempel dari LINE

Hal bagus dari "Gem Daftar Wine" ini adalah inputnya tidak terbatas pada foto.

Sebenarnya, di bar kita sering memesan ke toko minuman lewat LINE, bukan?

Setelah pemesanan selesai, pesan seperti ini datang dari toko minuman.

> "Terima kasih atas pesanannya. Kami telah menerima pesanan Anda sebagai berikut.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 botol
>
> ・Ridgeview Bloomsbury 6 botol
>
> ・○○ (wine baru) 2 botol
>
> Kami akan mengantar besok."

Suatu hari tiba-tiba terpikir oleh saya: "Bukankah teks ini bisa saya pakai apa adanya?"

Sebagai uji coba, saya menyalin pesan LINE ini dengan jari dan melemparkannya langsung ke Gemini.

Hasilnya sempurna.

Gemini hanya mengenali "nama produk" dalam pesan LINE itu, mencari informasinya secara daring, dan membuat daftar dalam format yang biasa (bendera + harga + deskripsi).

Dengan kata lain, saya bahkan tidak perlu menunggu botolnya tiba lalu memotretnya.

Tepat saat saya memesan, hanya dengan salin-tempel di dalam ponsel, daftar menu selesai sebelum barangnya tiba.

Tak perlu membuka PC, tak perlu menyalakan kamera.

Di sudut dapur, atau di kereta saat bepergian, pekerjaan selesai hanya lewat ponsel.

Bukankah ini "efisiensi sejati" yang layak didapat pemilik tunggal yang bekerja sendirian?

### 4-5. Saran AI × Penilaian di Lapangan (Realitas)

Meski begitu, saya tidak menelan mentah-mentah saran AI. Yang penting di sini adalah "penilaian manusia kita di lapangan."

Suatu kali, AI memberi saran ini untuk dipasangkan dengan sebuah wine:

AI: "Untuk wine merah ini, bebek panggang dengan saus jeruk adalah pairing yang sempurna."

Saran yang sangat bagus, tetapi sayangnya hari itu tidak ada bebek di kulkas kedai.

Saya tidak berpikir, "AI bilang begitu, jadi saya harus membeli bebek." Beginilah cara saya berpikir:

Saya (di lapangan): "Kita tidak punya bebek, tapi hari ini ada ayam kampung bagus yang masuk. Lemaknya sebanding dengan bebek, jadi ayam ini akan saya panggang sampai kulitnya renyah dan saya selesaikan dengan saus rasa jeruk, persis seperti kata AI."

"Pengetahuan AI (bebek dan jeruk cocok)" × "stok di lapangan (kita punya ayam)" = "menu baru yang jitu dan realistis."

Kombinasi ini adalah kesenangan sejati dalam mengembangkan menu bersama AI.

AI memberi jawaban buku teks, tetapi ia tidak tahu apa yang ada di kulkas hari ini. Menutup celah itu adalah tugas Anda sebagai pemilik.

### 4-6. Satu Mil Terakhir: AI Tidak Bisa "Mencicipi"

Ada satu hal lagi yang tidak boleh Anda serahkan kepada AI.

Yaitu mencicipi yang Anda lakukan sebelum apa pun dihidangkan kepada pelanggan.

Deskripsi dan pairing yang ditulis AI didasarkan pada "data umum dari dunia luas."

Tetapi wine adalah makhluk hidup. Bahkan label yang sama berubah rasanya menurut vintage dan cara penyimpanannya.

Pernah, AI menulis deskripsi untuk sebuah wine putih: "Wine kering yang segar dan ringan. Sempurna dengan carpaccio makanan laut."

Tetapi ketika saya benar-benar membuka botolnya dan mencicipi, wine itu lebih matang daripada dugaan saya, dengan nuansa kaya seperti madu.

"Jika saya sajikan ini sebagai 'wine kering yang ringan,' pelanggan akan kecewa... Ini lebih cocok dengan ayam saus krim daripada dengan carpaccio."

Saya segera mengoreksi teks yang dihasilkan Gemini.

- Sebelum (AI): "Segar dan ringan. Cocok untuk hidangan pembuka"

- Sesudah (manusia): "Kaya, bertubuh penuh berkat pematangan. Cukup kuat untuk mendampingi hidangan utama"

AI membuat 90% draf, dan manusia mencicipinya lalu menambahkan "10% terakhir (jiwanya)."

Pemeriksaan ini adalah tanggung jawab pemilik restoran, dan AI tidak akan pernah bisa menirunya.

Bukan "karena AI yang bilang," melainkan "karena saya meminumnya dan rasanya enak."

Untuk menyajikan dengan keyakinan itu, hari ini pun saya masih mencicipi wine yang baru dibuka, dengan daftar buatan AI di satu tangan.

#### Kolom 3: Tips Memotret agar AI Melihatnya dengan "Benar"

~ Seperti menunjukkan label kepada sommelier ~

Saat Anda mengirim foto ke Gemini, beberapa trik kecil dapat meningkatkan secara dramatis seberapa baik ia mengenali apa yang dilihatnya.

1.  Hindari silau: Label botol mudah memantulkan cahaya, jadi ubah sedikit sudutnya, atau buat bayangan dengan tubuh Anda saat memotret.

2.  Ambil beberapa foto dan kirim sekaligus: Untuk hal seperti isi kulkas, kirim foto lebar dan foto jarak dekat sekaligus, maka AI akan mengenali bahkan barang di titik buta.

3.  Tunjuk dengan jari: Menunjuk bagian yang Anda ingin AI perhatikan saat memotret juga membantu. Tuliskan sesuatu seperti "Saya menunjuk dengan jari" di prompt. Ini sama dengan menunjuk menu di restoran di luar negeri.

## Bab 5: Penerapan - Analisis Bisnis dan Peningkatan Laba

~ Gali "tambang emas yang tak terlihat." Rapat manajemen dengan konsultan AI Anda ~

### 5-1. Malam Ketika Saya Memeras Otak di Depan Kalkulator Setiap Akhir Bulan

Bagi kami para pemilik restoran mandiri yang kecil, tak ada waktu yang membebani seperti pekerjaan tutup buku bulanan.

Dalam keheningan larut malam, menjumlahkan data kasir dan mengetiknya ke Excel, yang terdengar hanyalah desahan sendiri.

"Target penjualan bulan ini ○○0.000 yen. ...Meleset."

"Jumlah pelanggan tidak buruk. Akhir pekan penuh. Tapi entah kenapa belanja per pelanggan tidak naik."

Mengapa saya tidak bisa mencapai target? Makanannya seharusnya enak. Saya sudah berusaha keras pada pelayanan.

"Mungkin harganya terlalu tinggi?"

"Tidak, kalau lebih murah lagi saya tidak untung. Dan biaya bahan juga naik."

Pertanyaan tanpa jawaban berputar-putar di kepala, dan akhirnya saya menutupnya hanya dengan mengandalkan semangat: "Bulan depan saya akan lebih semangat dan lebih gencar merekomendasikan." Inilah kebiasaan buruk saya, dan kebiasaan banyak pemilik.

Tetapi sekarang saya punya penasihat tanpa emosi.

Saya berhadapan dengan Gemini membawa data penjualan bulan itu dan data dari menu kedai.

### 5-2. Eksperimen: Membuat AI Membaca "Visual" dan "Angka" Sekaligus

Kali ini, saya memberi Gemini tiga informasi.

Saya melemparkan, tercampur jadi satu, "desain (otak kanan)" dan "angka (otak kiri)" yang selama ini selalu saya kelola secara terpisah.

1.  "Target penjualan bulan ini"

- Harapan tulus saya. Angka yang mutlak harus saya capai.

2.  "Seluruh data dari nota penjualan terbaru (CSV/Excel)"

- Hasil dalam kenyataan. Fakta tanpa basa-basi tentang siapa memesan apa, dan dengan harga berapa.

3.  "File PDF menu saat ini"

- Dunia yang dilihat pelanggan. Informasi visual seperti penempatan foto, ukuran dan warna teks.

Lalu saya mengajukan ini.

Ini bukan perintah kerja seperti "buat gambar" tadi. Ini pertanyaan, jenis pertanyaan yang diajukan seorang pemilik.

> "Bandingkan data penjualan saat ini (kenyataan) dengan tata letak menu (tampilan).
>
> Tunjukkan hambatannya: apa yang kurang untuk mencapai target ○○0.000 yen?"

### 5-3. "Asumsi Pemilik" yang Ditembus AI

Beberapa detik kemudian, jawaban Gemini datang, dan tepat mengenai titik buta saya.

Saya sudah mengira akan mendapat saran umum seperti "Mari kembangkan menu baru" atau "Mari berpromosi di media sosial."

Tetapi yang ditunjukkan AI adalah fakta yang selama ini tanpa sadar ingin saya sembunyikan.

Jawaban Gemini:

> "Dengan mencocokkan data dengan menu, saya menemukan peluang besar yang terlewatkan.
>
> Paket minum sepuasnya, yang margin labanya tinggi dan dapat menaikkan belanja per pelanggan dengan pasti, saat ini hanya tercantum sebagai teks pada menu (Sebelum), secara diam-diam di kiri bawah paling dasar.
>
> Sementara itu, tempat terbaik pada menu, di paling atas, diisi 'Set ¥2.200 (sekitar $15)' yang berharga murah. Dengan begini, pelanggan terbawa ke paket yang lebih murah dan bahkan tak menyadari pilihan minum sepuasnya yang lebih mahal."

Melihat layar, saya tak kuasa menahan erangan. Tepat sekali.

Kami memang punya paket minum sepuasnya. Tetapi di suatu sudut pikiran, saya selama ini berpikir begini:

"Kami bukan jaringan izakaya *(pub kasual Jepang yang menyajikan makanan dan minuman)*. Menjual minum sepuasnya dengan huruf besar terlihat murahan."

"Saya ingin orang menikmati rasa wine, jadi cukup dipesan oleh mereka yang sudah tahu saja."

"Asumsi" saya itu muncul dalam tata letak menu, pada teks di paling bawah.

![Menu Sebelum. Daftar minum sepuasnya ada di kiri bawah dan tidak menonjol. Juga sulit dikenali bahwa makanan terpisah](images/fig-21.png)

AI tidak melewatkannya.

"Pemilik, Anda ingin mencapai angka target, bukan? Kalau begitu, Anda harus menaruh course yang paling ingin Anda jual, yang dengan minum sepuasnya, tepat di paling atas, dengan bangga."

### 5-4. Tak Ada Bahan Gambar? Kalau Begitu, Serahkan Itu pada AI Juga

Tekad saya sudah bulat. "Kalau tampil keren justru membuat penjualan turun, saya akan mencobanya, apa pun yang terjadi."

Tetapi di sini muncul masalah.

"Meskipun ditaruh besar di bagian paling atas, kalau hanya teks rasanya lemah..."

Dan kalau saya ambil foto orang bersulang bir dari situs stok gratis, seketika tampilannya seperti restoran jaringan besar. Itu tidak cocok dengan suasana kedai saya.

Saya tidak berbakat menggambar, dan menyewa ilustrator butuh uang dan waktu.

Saya mulai cemas, "Bagaimana ini...?" tetapi lalu langsung teringat.

"Benar, saya punya wakil manajer (AI) yang bisa menggambar."

Saya telah menemukan sesuatu yang mendekati gambaran saya di situs bahan stok. Tertulis bahwa modifikasi diperbolehkan.

Saya melanjutkan dengan mengetik ini ke kotak obrolan:

> "Gambarkan ilustrasi untuk ditaruh di bagian atas menu. Pakai gambar terlampir sebagai dasarnya.
>
> Saya ingin nuansa orang-orang bersulang dengan gembira, tetapi tanpa terlihat murahan.
>
> Tolong buat dalam gaya gambar garis yang sederhana."

Beberapa detik kemudian, empat kandidat ilustrasi muncul di layar.

Dari antaranya, saya memilih ilustrasi "Cheers!" yang sederhana dan hangat, yang paling cocok dengan suasana kedai.

![Ilustrasi "Cheers!" yang dihasilkan AI hanya dalam 10 detik](images/fig-22.png)

Hanya butuh 10 detik.

Bukan hanya analisisnya: "bahan" yang diperlukan untuk perbaikan pun bisa diadakan saat itu juga.

Inilah kekuatan sejati dari menanamkan AI generatif ke dalam manajemen Anda.

### 5-5. Hanya Mengubah Tata Letak Menaikkan Belanja per Pelanggan Sekitar 40%

Maka saya mendesain ulang menu.

#### Sebelum: Menu Lama

- Tempat terbaik (paling atas): Item berharga murah seperti "Set ¥2.200 (sekitar $15)" dan "Set Course ¥3.300 (sekitar $22)."

- Minum sepuasnya: Dicantumkan hanya dengan teks, di sudut kiri bawah, sebagai "Minum sepuasnya mulai ¥3.000 (sekitar $20)." Sepenuhnya terkubur.

#### Sesudah: Menu yang Direvisi

- Tempat terbaik (paling atas): Paket berharga tinggi ¥4.500–¥5.700 (sekitar $30–$38), disajikan sebagai "Pilihan utama kami! Course Nikmat Penuh (dengan minum sepuasnya)."

- Desain: Dengan ilustrasi "Cheers!" buatan AI yang ditambahkan, ia dengan kuat mengarahkan mata, secara visual, ke "Lihat di sini dulu."

- Perubahan tata letak: Menu set murah yang tadinya jadi bintang dipindahkan ke bawah.

![Menu Sesudah. Course minum sepuasnya ditempatkan di paling atas](images/fig-23.png)

Makanan, harga, dan kualitas minumannya sebenarnya hampir tidak berubah. Yang saya ubah hanyalah "cara menampilkannya" dan "penempatannya."

Dan hasilnya?

Mulai keesokan harinya, perilaku pemesanan pelanggan berubah drastis.

Kata-kata pertama dari pelanggan yang membuka menu bukan lagi "Bir dulu," *(kebiasaan memesan bir lebih dulu di izakaya Jepang)* melainkan "Kalau begitu, kami ambil 'Course Pilihan Utama (¥4.900 (sekitar $33))' yang ada ilustrasinya ini."

Pelanggan yang dulu mengakhiri dengan "Set (¥2.200 (sekitar $15)) ditambah dua minuman" (belanja sekitar ¥3.500 (sekitar $23) per pelanggan) kini sejak awal memilih course ¥4.900 (sekitar $33).

Hanya dengan ini, belanja per pelanggan melonjak ¥1.400 (sekitar $9,3).

Selain itu, pelanggan juga mendapat manfaat "bisa minum tanpa khawatir soal tagihan," sehingga kepuasan justru naik, bukan turun.

### 5-6. Mencocokkan Hasil dengan PDF Penjualan Desember (PDCA)

Satu bulan telah berlalu sejak saya menjalankan langkah itu.

Tidak berhenti di sini adalah inti dari memakai AI.

Banyak pemilik menilai hasil dengan perasaan lalu berhenti: "Kami sibuk, jadi pasti berhasil," atau "Penjualan naik, jadi bagus."

Tetapi saya menghadapi Gemini lagi.

Kali ini saya mengunggah "PDF data penjualan Desember," yang hasilnya sudah keluar, dan bertanya begini:

> "Hasil langkah bulan lalu (perubahan menu) sudah ada.
>
> Lihat data penjualan Desember ini dan cocokkan hasilnya (evaluasi): apakah jumlah pesanan 'Course Pilihan Utama' naik sesuai harapan, dan bagaimana pengaruhnya terhadap belanja per pelanggan?"

Gemini menganalisis datanya seketika dan mengirimkan laporan kepada saya.

![Layar laporan analisis penjualan Gemini: saya membuat ringkasan untuk publikasi, jadi isinya sebagian berbeda dari teks di bawah](images/fig-24.png)

Analisis Gemini:

> "Ini hasil yang sangat baik. Melihat tren pada data, jumlah pesanan 'Course Nikmat Penuh' naik menjadi sekitar 1,8 kali bulan sebelumnya.
>
> Akibatnya, belanja per pelanggan secara keseluruhan naik rata-rata ○○ yen.
>
> Faktor utamanya adalah menempatkan paket minum sepuasnya lebih tinggi menaikkan nilai pesanan, terutama untuk rombongan."

Mendengar kata-kata itu, untuk pertama kalinya saya merasa benar-benar lega.

Bukan "entah bagaimana kami menghasilkan uang," melainkan keyakinan "saya membidik, dan saya membuat angkanya."

Ini menjadi tenaga pendorong untuk langkah berikutnya.

1.  Plan (Rencana): Lihat data penjualan dan menu, lalu temukan masalahnya (paket minum sepuasnya tersembunyi).

2.  Do (Kerjakan): Minta AI menggambar ilustrasi dan ubah tata letak menu.

3.  Check (Periksa): Minta ia membaca PDF penjualan Desember dan verifikasi hasilnya.

4.  Act (Tindak lanjut): Pikirkan meninjau tata letak menu makanan berikutnya.

"Siklus PDCA" yang dijalankan perusahaan besar dengan biaya sangat besar dapat dijalankan oleh seorang pemilik perorangan seperti saya, hanya dengan ponsel, jika saya punya AI sebagai mitra.

## Bab 6: Tantangan - Mengembangkan Sistem Khusus untuk Kedai Saya Sendiri

~ "Kalau belum ada, buat sendiri." Proyek pengembangan sistem tanpa ahli ~

※Sekadar informasi, Anda tidak perlu melakukan semua yang ada di buku ini.

・Kirim gambar dan minta AI menulis teks\
・Ubah pesan LINE yang panjang menjadi diagram

Dua hal ini sudah cukup untuk memulai. Bahkan itu pun pasti akan meringankan pekerjaan Anda.\
Cukup membaca ini sebagai sebuah cerita dan berpikir, "Oh, sejauh ini pun bisa dilakukan dengan AI," juga sudah cukup.

### 6-1. Aplikasi Siap Pakai Tak Mampu Menjawab Kebutuhan Khusus Saya

Sejauh ini saya telah berbicara tentang memakai AI di atas platform yang sudah ada, seperti pembuatan gambar dan analisis menu.

Tetapi seiring Anda terus menjalankan usaha, muncul kekhawatiran yang sama sekali tak bisa diselesaikan oleh "aplikasi siap pakai."

Khususnya, untuk model bisnis tak lazim seperti kami, "kari di siang hari, bar di malam hari," aliran uang masuk dan keluar pun rumit.

"Saya ingin mencocokkan saldo PayPay Bank saya dengan pembayaran yang akan datang dan mengetahui jumlah yang akan tersisa di akhir bulan."

"Tanggal pembayaran terbagi antara tanggal 10 dan 25. Saya ingin menyimulasikannya."

Perangkat lunak akuntansi yang ada sangat mumpuni, tetapi tidak ada yang tepat menjawab "kekhawatiran di kepala saya saat ini."

Maka saya bertekad.

"Kalau belum ada, saya akan membuatnya. Saya punya Gemini, insinyur terkuat."

### 6-2. Fase 1-3: Dari Catatan Coretan ke "Cloud"

Pengembangan dimulai dengan menunjukkan catatan saya di Google Keep kepada Gemini.

![Catatan Keep yang menjadi titik awal pengembangan](images/fig-25.png)

#### Fase 1: Membangun Logika

"Saya ingin mengotomatiskan perhitungan dalam catatan ini."

Menanggapi permintaan saya, Gemini dengan cepat menyusun logika perhitungannya.

- Ketika saya mengubah jumlah untuk sebuah item, ia langsung menghitung saldo akhir.

- Jika dana hampir habis, ia menampilkan "peringatan" berwarna merah.

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

Tetapi saya belajar bahwa membawa "tongkat sihir (literasi)" dan "perisai (langkah keamanan)" untuk memakai sihir itu pun mulai sekarang termasuk pekerjaan seorang pemilik.

### 6-6. "Tanggung Jawab" dan "Asuransi" yang Menyertai Kebebasan

#### Penting: Privasi dan Informasi Pribadi

"Sistem pengenalan wajah" ini adalah prototipe eksperimental yang saya buat untuk menguji apa yang mungkin secara teknis. Jika Anda memakainya di kedai sungguhan, data wajah pelanggan Anda akan tergolong "informasi pribadi (data biometrik)," dan harus dilindungi secara ketat menurut hukum (Undang-Undang Perlindungan Informasi Pribadi Jepang).

Jika Anda berpikir untuk menerapkan sesuatu seperti ini, mohon pegang dua hal ini tanpa gagal.

Beri tahu pelanggan dan dapatkan persetujuan mereka: Anda memerlukan proses seperti memasang papan di pintu masuk yang menyatakan "Kami memakai pengenalan wajah AI" dan meminta persetujuan saat pelanggan mendaftar sebagai anggota. Merekam secara diam-diam sama sekali tidak diperbolehkan.

Lindungi datanya: Anda memerlukan langkah yang menekan risiko kebocoran hingga nol, seperti mengelola data di lingkungan yang terputus dari internet.

Mampu membangun sesuatu tidak sama dengan diizinkan melakukannya. Jika Anda pemilik yang punya keterampilan teknis, mohon ingat bahwa tanggung jawab memakai teknologi itu menyertainya.

Sejauh ini saya berbicara tentang betapa hebatnya sistem buatan sendiri. Tetapi sebagai pemilik usaha, saya juga harus memberi tahu Anda tentang kenyataan yang keras.

Yaitu ini: "Segala sesuatu yang Anda bangun sendiri adalah tanggung jawab Anda sendiri."

Pada layanan berlangganan bulanan (SaaS), jika server mati, perusahaan meminta maaf dan menjalankannya kembali.

Tetapi sistem yang dibangun dengan vibe coding tidak punya "dukungan pelanggan."

Jika aplikasi Anda tiba-tiba berhenti bekerja pada puncak jam makan siang, tidak ada yang akan datang membantu.

Ketika Google mengubah suatu spesifikasi, kode yang kemarin berjalan baik lalu hari ini memunculkan error adalah kejadian sehari-hari.

Karena itu saya membuat dua persiapan.

Pertama adalah "cadangan analog."

"Jika pengenalan wajah berhenti, lihat buku besar pelanggan di kertas." "Jika aplikasi kasir mati, pakai kalkulator dan nota tulisan tangan."

Alat digital hanyalah "alat yang praktis." Anda tidak boleh bergantung padanya sampai ketika ia berhenti, kedai Anda pun berhenti.

Yang kedua adalah "asuransi" yang saya sebutkan tadi.

Asuransi tanggung gugat siber tidak hanya menanggung risiko kebocoran informasi, tetapi juga ganti rugi atas kehilangan bisnis ketika kesalahan Anda sendiri menghentikan sistem. Bagi pemilik perorangan yang membekali diri dengan TI, itu bagian dari menjadi orang dewasa yang bertanggung jawab.

"Terkadang segalanya akan berhenti. Terkadang saya akan membuat kesalahan."

Anggap itu sebagai hal yang pasti, terima risikonya, dan ambil langkah menghadapinya.

Hanya ketika kita punya tekad ini, kita benar-benar dapat memakai "sistem bebas" yang tidak terikat oleh siapa pun.

### 6-7. Anda Tidak Butuh Ahli. Anda Butuh Ketekunan

Saya tidak membayar satu yen pun biaya alih daya untuk pengembangan dua sistem ini.

Yang saya pakai hanyalah langganan AI beberapa ribu yen per bulan, dan ketekunan seorang pemilik yang berpikir, "Saya mutlak harus menghilangkan kekhawatiran ini (soal arus kas)" dan "Saya ingin membuat pelanggan saya senang."

Ini bukan soal "saya tidak bisa, karena saya tidak bisa memprogram."

Jika Anda punya sesuatu yang ingin dibangun (Want), AI akan mengajari Anda cara membangunnya (How).

Bahkan ketika muncul kata-kata yang tidak Anda pahami (Node.js, PowerShell, Firestore...), tidak ada yang perlu ditakuti.

Kita punya mitra terkuat yang ada, "Gemini," untuk menerjemahkannya dan membimbing kita.

#### Kolom 4: Apa Bedanya Excel dengan Basis Data (Firestore)?

~ Apakah ia "memo untuk Anda baca," atau "buku besar untuk dibaca sistem"? ~

Firebase (Firestore) muncul dalam pengembangan aplikasi arus kas. Anda mungkin bertanya-tanya, mengapa tidak Excel?

Spreadsheet (Excel) adalah "buku catatan yang dilihat dan diketik manusia." Ia sangat fleksibel, tetapi bagi sebuah sistem, ia kabur soal "apa ada di mana."

Basis data (Firestore), di sisi lain, adalah "loker yang tertata rapi dan dibuat untuk sistem." Karena sudah ditetapkan bahwa "tanggal masuk ke slot 1 dan jumlah ke slot 2," sebuah program dapat menanganinya seketika. Ia juga tidak rusak ketika beberapa orang mengaksesnya pada saat yang sama.

"Jika Anda membangun aplikasi, pakai basis data, bukan Excel." Hanya dengan mengetahui ini, tingkat instruksi Anda kepada AI akan naik.

## Penutup: "Resep Masa Depan" yang Hanya Dimiliki Kedai Anda

~ AI bukan teknologi yang sulit. Ia adalah mitra baru untuk "percakapan" ~

Terima kasih telah membaca buku ini sampai akhir.

Jika Anda hanya mencoba satu hal dari buku ini, cobalah ini: "Tempelkan pesan LINE yang merepotkan itu langsung ke AI dan minta ia 'mengubahnya menjadi diagram.'"

Saya bukan ahli AI yang istimewa. Saya hanya mengulang setiap hari praktik "berbicara dengan AI dalam bahasa tempat kerja," \
di medan tempur sebuah restoran.

Karena itu saya rasa sudah cukup jika Anda membawa pulang dari buku ini bukan "kumpulan jawaban yang benar," melainkan hanya "cara berpikir."

Ketika Anda membuka halaman pertama, gambaran apa yang Anda miliki tentang kata-kata "memakai AI"?

"Kedengarannya sulit." "Butuh pengetahuan pemrograman, kan?" "Tidak ada hubungannya dengan kedai kecil seperti milik saya."

Mungkin Anda berpikir seperti itu.

Tetapi sekarang setelah Anda membaca catatan "coba-coba" saya ini sampai sejauh ini, mungkin gambaran itu sedikit berubah.

Yang saya lakukan bukan memanfaatkan sepenuhnya teknologi TI tingkat lanjut.

Saya menggerutu, "Kalau manual begini mustahil." Saya mengeluh, "Ini sulit dipakai." Dan saya banyak menuntut, berkata, "Saya ingin sistemnya bekerja seperti ini."

Akhir-akhir ini, di dunia para insinyur, istilah "vibe coding" sedang tren.

Itu adalah metode membangun sistem secara intuitif, sambil berdialog dengan AI.

Sebagaimana seorang pemain shogi berbicara dengan AI untuk membaca langkah-langkah berikutnya, kita pun dapat berbicara dengan AI dan membangun "masa depan kedai kita."

Seperti berkata kepada staf dapur Anda, "Tambah sedikit lagi garamnya."

Seperti bertanya kepada penjual ikan di pasar, "Ada ikan bagus hari ini?"

Berbicara kepada AI dan berkata, "Buat pekerjaan ini lebih mudah." Dari situlah segalanya dimulai.

Dulu saya bekerja di departemen sistem sebuah perusahaan, berkoordinasi antara "lapangan" dan "pengembang."

Sekarang saya melakukan hal yang sama antara "kedai saya sendiri" dan "AI."

Dan saya yakin akan hal ini:

"Pemilik yang tahu masalah di lapangan dapat menjadi komandan AI terkuat."

Mulailah hari ini, Anda juga.

Pertama, keluarkan ponsel Anda dan berbicaralah kepada Gemini.

"Hei, persiapan hari ini sebaiknya mulai dari mana?"

"Bagaimana cara membuat item menu ini lebih laku?"

"Urusan administrasi ini merepotkan. Bisa bantu carikan solusinya?"

Jangan khawatir jika muncul error. Itu tanda bahwa "percakapan" telah dimulai.

Cukup ambil tangkapan layar dan kirimkan kembali sambil menulis pesan "sepertinya ada yang janggal."

Di ujung tumpukan percakapan itu, menunggu "waktu luang" dan "keleluasaan hidup" yang tak pernah Anda bayangkan, dan "masa depan yang hanya milik kedai Anda."

Nah, mari kita pekerjakan "wakil manajer" yang bisa diandalkan untuk kedai Anda juga.

Karena resep masa depan akan lahir dari percakapan antara Anda dan AI.

### Tiga Langkah Lanjutan dari Buku Ini

Buku ini gratis dibaca sebagai PDF, di note, dan di Google Play. (Hanya di Kindle, aturan kedai mewajibkan harga minimum.) Sebagai gantinya, saya menyiapkan tiga tempat yang bisa Anda tuju setelah selesai membaca. Jika Anda memakai satu saja di antaranya, menulis buku ini akan terasa berharga.

1. Coba di kedai Anda sendiri. Seri Agenda bisa dimulai dengan buku catatan yang gratis. https://bontallc.com/agenda?via=b1-id-{{FMT}}
2. Ikuti kegiatan saya. Saya menulis tentang alat yang akan saya buat berikutnya dan keseharian di bar, di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
3. Jika suatu saat Anda ke Tokyo, kunjungi Tamuro. Satu menit dari pintu timur Stasiun Higashi-Nakano. Anda bisa masuk tanpa reservasi. Ketika buku ini pertama kali ditulis, Tamuro memakai sistem rujukan. Kini siapa pun dipersilakan masuk, tanpa perlu reservasi. Situs reservasi https://tamuroreservation.vercel.app/?src=b1-id-{{FMT}}

Bagi Anda yang datang karena buku ini: saat membuat reservasi, mohon masukkan kode kupon "BOOK". Kami akan memberikan satu minuman gratis pada kunjungan pertama Anda. Jika Anda datang tanpa reservasi, cukup katakan "Saya tahu dari buku ini" saat memesan pertama kali. Kami akan memberikan minuman gratis yang sama. Ini sebuah cara kecil agar saya bisa menghitung berapa orang yang datang karena buku ini.

### Tentang Penulis

Raku Bonta

Pemilik tunggal yang menjalankan restoran dengan 11 kursi konter dan 8 tempat duduk di area tatami di Higashi-Nakano, Tokyo.

Pada siang hari tempat ini menjadi kedai kari hamburg steak yang harum rempah. Pada malam hari tempat ini menjadi dining bar dengan sistem rujukan yang menyajikan menu set yang berganti setiap hari.

▼ Quatre Epice Hamburger Curry

https://www.instagram.com/quatre.epice.hamburg.curry/

![Quatre Epice Hamburger Curry](images/fig-28.png)

▼ Bar dengan sistem rujukan "Tamuro"

https://www.instagram.com/tamuro.higashinakano/

![Bar dengan sistem rujukan "Tamuro"](images/fig-29.png)

Kedai ini juga mencurahkan tenaga untuk membangun komunitas lewat makanan, dengan acara wine dua mingguan, kelas memasak bulanan, dan makan malam course.

Sebelum membuka kedai sendiri 12 tahun lalu, penulis bekerja di sebuah perusahaan dalam "perencanaan sistem" dan "arsitektur solusi."

Jabatannya terdengar sulit, tetapi pekerjaan sebenarnya adalah "koordinator yang menyampaikan dengan tepat keinginan lapangan 'kami ingin melakukan ini' kepada vendor TI dan membuatnya terwujud." Bukan insinyur yang melakukan pemrograman tingkat lanjut, penulis memiliki karier sebagai "penerjemah" yang menghubungkan manusia dan teknologi.

Kini, dengan memanfaatkan pengalaman itu, penulis memakai AI generatif seperti Google Gemini untuk menjalankan kedainya sendiri, mempraktikkan dan membagikan "reformasi operasional yang bisa dilakukan meski tanpa pengetahuan khusus sama sekali."
