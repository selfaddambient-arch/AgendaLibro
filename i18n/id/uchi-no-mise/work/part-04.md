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

