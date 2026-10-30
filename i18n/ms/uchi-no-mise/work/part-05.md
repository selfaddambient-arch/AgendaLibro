## Bab 4: Teknologi - Sistem untuk Membina Produk Seorang Diri, Secara Berterusan

Perkara utama bab ini

- Saya menjadikan prosedur melancarkan produk baharu sebagai dokumen, dalam bentuk (sebuah skill) yang boleh dibaca dan dilaksanakan oleh AI. Apa yang manusia lakukan hanyalah pertimbangan dan operasi yang hanya manusia boleh buat
- Bahagian bersama, seperti log masuk, pengebilan, halaman pengenalan dan panduan kepada produk lain, dibina sekali dan digunakan semula merentasi semua produk. Kos pangkalan data asas itu ialah kira-kira $35 sebulan
- Sistem ini masih terus dikembangkan. Saya terus menambah pada dokumen prosedur kegagalan, seperti satu reka bentuk ditolak lima kali berturut-turut

(Ini bab dengan banyak istilah teknikal. Jika anda tidak berminat dengan teknologinya, anda boleh melangkau ke Bab 5 dan kisahnya tetap bersambung.)

### 4-1 ProductBootstrap: Menyerahkan Prosedur Pelancaran Itu Sendiri kepada AI

Setiap kali saya membina produk, saya mengulang persediaan yang sama dan kesilapan yang sama. Mencipta repositori (gudang untuk atur cara). Menyambung log masuk. Memutuskan warna reka bentuk. Menyediakan sistem pengujian. Menyediakan persekitaran pengeluaran. Saya pasti telah melakukan semuanya untuk produk sebelumnya, tetapi saya lupa butirannya dan tersandung di tempat yang sama.

Maka saya menjadikan prosedur melancarkan produk baharu sebagai dokumen. Bentuknya yang boleh dibaca dan dilaksanakan oleh AI yang menulis kod (Claude Code) saya panggil sebuah "skill." Nama skill ini ialah ProductBootstrap. "Bootstrap" ialah istilah lazim dalam dunia komputer untuk memulakan diri sendiri daripada mekanisme minimum, dan saya menerapkannya pada pelancaran produk.

Saya tidak menyimpan atur cara templat. Saya menyalin produk terkini yang siap dan memulakan produk baharu daripadanya. Dengan cara itu, pengajaran terbaharu diwarisi secara automatik oleh produk seterusnya. Tidak perlu terus menyelenggara templat lama juga.

#### Aliran Prosedur

1. Serahkan dokumen keperluan. Jika ruangan yang diperlukan (nama produk, apa yang dilakukan, siapa yang menggunakan, harga, unit harga, warna pengenalan, lokasi induk reka bentuk, dan seterusnya) dibiarkan kosong, AI tidak bermula. Peraturannya ialah ia tidak bertanya soalan kepada pemilik di tengah jalan. Jika semuanya tidak lengkap pada permulaan, ia tidak bermula
2. Putuskan warna produk. Setiap produk dalam siri Agenda mempunyai satu warna pengenalan. AI menyemak nilai warna produk sedia ada, mencadangkan kira-kira empat calon yang tidak bertindih, dan pemilik memilih
3. Tetapkan reka bentuk. Saya meminta AI reka bentuk (Claude Design) mencipta cadangan untuk skrin. AI menjalankan semakan kendirinya sehingga tiga pusingan, dan hanya cadangan yang lulus semakan ditunjukkan kepada pemilik
4. Serahkan pelaksanaan kepada AI sehingga habis. AI membina dan membetulkan sendiri sehingga memenuhi syarat penerimaan yang ditetapkan (semakan jenis, semakan gaya, semua ujian hijau, lulus setiap semakan skrin, dan perubahan pangkalan data berjalan dengan lancar dalam persekitaran ujian)
5. Pemilik hanya memberi kelulusan apabila hendak melancarkannya ke pengeluaran. Semuanya sehingga persekitaran ujian berjalan tanpa pengawasan, dan pemilik menilai hanya operasi pengeluaran

Saya membina peringkat pelaksanaan supaya ia tidak berhenti di tengah jalan untuk menunggu kelulusan pemilik. Pada hari-hari awal, saya meneruskan dengan meminta kelulusan pada setiap peringkat, tetapi tiada apa yang bergerak ke hadapan dengan cara itu. Apabila terdapat beberapa tetingkap kerja AI, setiap satu berhenti menunggu kelulusan, dan pemilik perlu berpindah-pindah antara setiap tetingkap membuat pertimbangan. Maka saya mengubahnya: saya menyerahkan lebih awal julat yang sudah diluluskan dan syarat penerimaan yang boleh dinilai mesin, dan ia berhenti hanya apabila gagal.

Syarat berhenti juga ditetapkan. Apabila dokumen prosedur dan keputusan pemilik bercanggah. Apabila operasi yang hanya manusia boleh buat diperlukan. Apabila ia gagal maju pada ralat yang sama tiga kali berturut-turut. Apabila pengesahan tamat, kebenaran tidak mencukupi, atau operasi yang tidak boleh diundurkan diperlukan. Selain itu, AI meneruskan sendiri. Keadaan kerja direkodkan dalam fail kecil, jadi walaupun proses terhenti di tengah jalan, ia boleh disambung semula dari situ.

#### Manusia Hanya Melakukan Dua Perkara

Saya menulis ini dalam dokumen prosedur: AI melaksanakan setiap langkah. Pemilik boleh diminta hanya dua perkara berikut.

- Pertimbangan itu sendiri. Meluluskan, memutuskan, menentukan yang mana satu daripada dua pilihan
- Operasi yang hanya manusia boleh lakukan. Kunci yang hanya boleh dikeluarkan daripada skrin pentadbir perkhidmatan luar, permohonan yang melibatkan pengesahan identiti, operasi pada peranti sebenar dan penilaian visual

Jika AI menyerahkan apa-apa selain itu kepada pemilik, itu pelanggaran dokumen prosedur. Dalam jadual prosedur, saya menambah ruangan "pelaksana" pada setiap baris, dan mana-mana baris yang entri pemiliknya tidak dapat menyatakan sebab akan ditukar ke pihak AI.

Saya mempunyai sebab untuk membuat peraturan ini. Apabila saya mengemas kerja yang tinggal bagi satu produk, AI menyenaraikan "cipta projek pelayan," "daftarkan destinasi log masuk," "masukkan pemboleh ubah persekitaran," dan "bina persekitaran ujian," semuanya sebagai tugas pemilik. Setiap satu ialah operasi yang AI boleh laksanakan sendiri. "Mengapa saya yang melakukan ini?" ialah reaksi jujur saya ketika itu. AI melakukannya sendiri jika anda memintanya. Tetapi jika anda tidak meminta, ia menyerahkannya kepada manusia. Itulah sebabnya saya perlu menulisnya ke dalam dokumen prosedur.

Setiap kegagalan sistem tempahan yang saya terangkan dalam Bab 2 saya masukkan ke dalam senarai semak dokumen prosedur ini. Tulis ujian dahulu. Jangan simpan data pengeluaran dalam persekitaran pembangunan. Bina persekitaran ujian dahulu. Produk seterusnya mengelak kesilapan pahit yang sama sejak awal.

#### Masih Berkembang

Dokumen prosedur ini bukan produk yang sudah siap. Ia sesuatu yang terus saya tambah setiap kali sesuatu gagal.

Contohnya, pernah ada masa saya meminta AI reka bentuk mencipta skrin untuk satu produk lima kali berturut-turut, dan kesemua lima ditolak. Itu termasuk pusingan di mana saya menyerahkan peraturan reka bentuk seluruh siri (DESIGN.md).

Pada mulanya, AI mendiagnosis puncanya sebagai "skema warna itu sendiri." Saya menafikannya. Punca sebenar ada dua. Satu ialah warna yang tiada takrifan dalam peraturan digunakan sesuka hati. Satu lagi ialah tiga bahagian dengan peranan berbeza disusun menegak dengan warna latar yang sama dan jidar yang sama, tanpa sempadan antaranya. Tiada peraturan dilanggar, namun peranan telah hilang daripada rupa.

Maka saya menambah fasal pada peraturan reka bentuk. Jangan beri rupa yang sama kepada perkara yang berbeza peranannya. Jangan pisahkannya dengan warna sahaja. Elemen yang paling penting menjadi tumpuan pandangan yang pertama. Hanya perkara yang benar-benar setara boleh disusun dengan berat yang sama. Jangan buat susun atur yang sekadar menimbun secara menegak.

Ada satu lagi pengajaran daripada kegagalan. Jika anda menyampaikan "rupa lalai yang perlu dielakkan" hanya sebagai senarai larangan, AI berayun sepenuhnya ke lalai lain yang tiada dalam senarai. Apabila saya melarang kad, bayang dan sudut bulat serentak, yang kembali ialah skrin seperti akhbar yang dibuat daripada garisan dan jidar semata-mata. Sejak itu, saya meminta bahan permintaan ditulis dalam tiga lajur: "corak yang perlu dielakkan," "apa yang saya mahu larang," dan "apa yang perlu dilakukan sebagai ganti."

Saya juga mengubah cara saya memutuskan warna pengenalan di tengah jalan. Ketika produk melebihi lapan, jalur warna gelap telah diisi oleh produk sedia ada, dan produk kesembilan dan seterusnya tidak lagi dapat warna gelap untuk garisan dan butang tanpa berlanggar dengan yang sedia ada. Maka saya menyemak peraturan: warna pengenalan produk hanya digunakan untuk warna permukaan yang cerah, dan garisan, jidar, ikon dan butang utama semuanya diseragamkan dalam warna dakwat gelap bersama siri. Ia kekangan yang menjadi jelas hanya setelah produk bertambah.

Setiap kali sesuatu gagal, saya membetulkan dokumen prosedur. Produk seterusnya menjadi lebih mudah sebanyak itu. Saya percaya mengembangkan dokumen prosedur ialah pelaburan terbaik untuk terus membina produk seorang diri.

【Rajah 4-2】Peringkat prosedur pelancaran, dan siapa yang melaksanakannya (AI atau pemilik) *(Skrin dalam bahasa Jepun.)*

【Rajah 4-3】Warna pengenalan siri Agenda. Satu warna bagi setiap produk, digunakan hanya pada permukaan *(Skrin dalam bahasa Jepun.)*

### 4-2 AgendaHub: Pintu Depan

Apabila produk bertambah, anda akhirnya membina perkara yang sama berulang kali. Log masuk, pengebilan, halaman pengenalan, panduan kepada produk lain. Untuk menjalankan ini seorang diri, anda perlu membina bahagian bersama sekali dan menggunakannya semula merentasi semua produk.

AgendaHub ialah tempat bahagian bersama itu dihimpunkan. Saya memanggilnya "pintu depan."

Pertama, ia pintu masuk yang menghalakan daripada satu alamat ke setiap produk. Di bawah satu domain, bontallc.com, pintu masuk bagi setiap produk tersusun: /agendatimbro, /agendaoro, /agendaluce. Kepada pelanggan ia kelihatan seolah-olah produk berada di dalam satu laman, tetapi sebenarnya atur cara yang berasingan berjalan di belakang setiap satu.

Seterusnya, ia tempat halaman pengenalan produk diletakkan. Terdapat satu halaman pengenalan untuk siri ini, dan di dalamnya satu bahagian bagi setiap produk. Setiap bahagian memuatkan nama produk dan gelarannya, harga, satu masalah yang dinyatakan dalam kata-kata pemilik sendiri bermula dengan "Apabila anda...," penerangan tentang apa yang boleh dilakukannya, dan pautan ke halaman butiran. Apabila saya melancarkan produk baharu, menambah bahagian ini termasuk dalam prosedur pelancaran.

Ia juga menjadi pusat rujukan bagi peraturan reka bentuk dan prosedur pelancaran. Induk warna pengenalan, peraturan skrin (DESIGN.md), skill ProductBootstrap yang saya terangkan dalam 4-1, skill yang menyemak skrin, dan skill yang membuat perubahan pangkalan data dengan selamat. Bagi setiap peraturan yang merentasi siri, kandungan sebenar berada di sini, dan setiap produk membacanya melalui rujukan.

【Rajah 4-1】Struktur siri Agenda. Daripada pintu depan (AgendaHub) ke setiap buku, dan setiap buku bersambung kepada satu akaun (AgendaID) *(Skrin dalam bahasa Jepun.)*

### 4-3 AgendaID: Akaun Bersama dan Pengebilan

AgendaID ialah sistem bersama siri ini untuk akaun dan pengebilan.

Pemilik yang log masuk sekali dengan akaun Google boleh menggunakan setiap produk. Tidak perlu mencipta akaun bagi setiap produk. Saya juga merancang untuk akhirnya membawa tetapan bahasa merentasi produk.

Pengebilan juga satu sistem. Daripada membina sambungan kepada perkhidmatan pembayaran (Stripe) bagi setiap produk, AgendaID menanggung semuanya. Terdapat empat kategori harga: produk ringan pada ¥300 (kira-kira $2) sebulan, produk bayar ikut guna, produk pembelian sekali pada ¥600 (kira-kira $4), dan produk percuma. Produk berbayar mempunyai tempoh percuma tiga bulan tanpa pendaftaran kad, boleh digunakan sekali bagi setiap gabungan kedai dan produk. Terdapat juga mekanisme yang menambah tempoh percuma tiga bulan kepada perujuk dan orang yang dirujuk.

Sebelum tempoh percuma tamat, e-mel pemberitahuan tiba tujuh hari dan satu hari lebih awal. Pada mulanya saya membina e-mel ini di dalam Buku Kehadiran juga, tetapi apabila produk bertambah saya sedar membazir memberi setiap produk mekanisme yang sama, maka saya menyatukannya di pihak AgendaID.

#### Menyeragamkan Peraturan Pembatalan dan Pemadaman Data

Ada bahagian yang biasa tetapi penting: pembatalan dan pemadaman data.

Apabila pelanggan membatalkan, data mana yang dipadam, dan bila? Jika anda membinanya secara berasingan bagi setiap produk, sesuatu pasti terlepas di suatu tempat. Lebih-lebih lagi, siri Agenda termasuk produk yang mengendalikan data yang amat sensitif, seperti yang mengenal pasti pelanggan tetap melalui pengecaman wajah.

Maka saya membahagikan butiran pemadaman kepada empat peringkat dan menjadikannya peraturan bersama merentasi siri. Ia ialah membatalkan produk, memadam kedai, menamatkan akaun (meninggalkan seluruh siri), dan permintaan pemadaman daripada seorang kakitangan individu. Peringkat atas mengalir ke peringkat bawah, dan setiap produk mendaftarkan prosedur pemadaman datanya sendiri dengan sistem bersama. Tempoh tangguh pemadaman ialah 30 hari, dan dalam tempoh itu data itu boleh dipulihkan semula.

Satu paksi masa datang bersama ini. Rekod kehadiran, contohnya, dikehendaki oleh undang-undang untuk disimpan selama lima tahun. Walaupun bekas kakitangan meminta pemadaman, dalam tempoh pengekalan rekod mesti disimpan, dengan nama dan seumpamanya dijadikan tanpa nama, bukannya dihapuskan secara fizikal. Saya perlu memutuskan garis antara "padam" dan "simpan" dengan menyemaknya berbanding undang-undang.

#### Log Masuk Ujian untuk Menghalang AI Mencemari Pengeluaran

Saya menambah satu lagi mekanisme pada AgendaID, untuk AI: pintu masuk log masuk ujian.

Untuk meminta AI menyemak bahawa sesuatu berfungsi, AI perlu log masuk dan mengendalikan skrin. Tetapi log masuk dilakukan dengan akaun Google, jadi AI tidak boleh log masuk sendiri. Dan saya juga tidak boleh menyerahkan akaun pemilik kepada AI. Ada bahaya ujian AI akan mencemari data pengeluaran.

Maka saya membina pintu masuk yang mengeluarkan akaun sintetik (persona) yang hanya boleh digunakan dalam persekitaran ujian. Ia tidak berfungsi di pengeluaran. Pangkalan data persekitaran ujian ialah projek berasingan daripada pengeluaran dan hanya mengandungi data sintetik. AI log masuk melalui pintu masuk ini, mengendalikan skrin, dan mengesahkan bahawa sesuatu berfungsi. Akaun ujian dibina semula setiap hari, dan yang lama dipadam.

Dengan ini, AI boleh melaksanakan malah semakan akhir sendiri, dalam persekitaran yang dibina persis seperti pengeluaran, tanpa menyentuh pengeluaran.

### 4-4 Navigasi Bersama, dan Kegagalan Perkataan "Pintu Depan"

Supaya pengguna boleh pergi dari mana-mana produk ke yang lain, saya memberi setiap produk menu navigasi bersama. Ia laluan yang membolehkan pemilik bar yang menggunakan Buku Kehadiran bertanya soalan dalam Buku Bantuan, atau pergi melihat buku-buku lain.

Di sebalik navigasi bersama ini ada kisah kegagalan kecil.

Dalam versi pertama, saya telah meletakkan pautan yang berbunyi "Kembali ke pintu depan." Itu kerana, secara dalaman, saya memanggil AgendaHub "pintu depan." Tetapi apabila saya menyemak pada peranti sebenar, ada sesuatu yang tidak kena. Dua pautan, "Kembali ke pintu depan" dan "Lihat siri Agenda," menghala ke tempat yang sama. Selain itu, pautan sokongan berada di atas menu kerja harian, jadi urutan kepentingan terbalik. Dan yang paling utama, perkataan "pintu depan" tidak bermakna apa-apa kepada pemilik yang menggunakan produk buat kali pertama. Ia bahasa dalaman pembuat sendiri.

Maka saya menetapkan semula prinsip. Susun item mengikut seberapa dekat ia dengan tujuan pengguna: kerja harian di paling atas, pautan yang menuju ke luar di paling bawah. Walaupun ia pautan untuk menarik pengguna baharu, ia sekali-kali tidak boleh diletakkan di atas menu kerja harian. Sempadan mesti boleh diterangkan dengan satu baris. Tulis kata-kata dalam bahasa pengguna, bukan bahasa dalaman. Jangan sekali-kali letakkan lebih daripada satu pautan yang menghala ke tempat yang sama. Saya membuang "Kembali ke pintu depan" dan menggabungkan semuanya menjadi satu pautan, "Lihat buku-buku Agenda yang lain."

Dalam Bab 2, saya menulis tentang mempelajari istilah UI. Itu bahasa untuk pemilik gunakan apabila bercakap dengan AI. Ini sebaliknya: bahasa yang pembuat gunakan untuk bercakap dengan pengguna. Dalam kedua-dua kes, ia soal menyesuaikan kata-kata anda dengan orang yang anda bercakap dengannya.

【Rajah 4-4】Navigasi bersama selepas pembetulan. Kerja di atas, dan pautan yang menuju ke luar di paling bawah *(Skrin dalam bahasa Jepun.)*

### 4-5 Asas Itu Berharga $35 Sebulan

Kos pangkalan data bagi keseluruhan asas yang diterangkan dalam bab ini ialah kira-kira $35 sebulan. Pelan berbayar yang merangkumi projek pengeluaran ialah $25, dan projek untuk persekitaran ujian ialah $10.

Ini juga bukan jumlah dari awal. Pada satu ketika saya membayar $45 sebulan. Pangkalan data pembangunan untuk produk pengecaman wajah masih dibilkan walaupun saya tidak menggunakannya. Saya memindahkannya ke peringkat percuma dan menghentikannya, memadam projek lain yang tidak saya gunakan, dan begitulah ia sampai ke jumlah sekarang.

Saya juga memerhatikan kos AI. Kerja AI yang menulis atur cara dibilkan mengikut jumlah token (unit teks yang dibaca dan ditulis AI). Saya mengelak menumpukan kos dengan meminta tetingkap kerja berpegang pada peranan penyelaras dan menyerahkan pelaksanaan itu sendiri kepada AI lain dengan peruntukan kos berasingan. Untuk model generatif dalam tetingkap sembang juga, saya melihat harga dan memilih yang perlu dan mencukupi. Walaupun model peringkat lebih tinggi hanya berharga $1 lebih sebulan, saya memilih dengan bertanya "adakah ini cukup?"

Jika anda membina kecil, jualan kecil pun boleh menampung anda. Kisah pengewangan dalam Bab 3 disokong oleh kecilnya kos asas ini.

### 4-6 AI Penyelaras, dan Orang yang Membuat Keputusan

Akhir sekali, izinkan saya menerangkan bentuk hari kerja saya.

Saya membuka beberapa tetingkap kerja AI pada masa yang sama. Ada tetingkap untuk sistem tempahan, tetingkap bagi setiap produk, dan tetingkap penyelaras yang menghantar arahan kepada mereka dan mengumpulkan hasilnya. Saya menamakan tetingkap penyelaras itu AgendaRegia (buku penyelaras).

Yang membuat keputusan, iaitu memutuskan "hala mana yang hendak dituju," ialah saya dan AI di pihak sembang. AI di pihak sembang mencari jurang dan percanggahan dalam spesifikasi lebih awal, melampirkan keputusan lalai pada setiap satu, dan mencadangkan semuanya sekali gus. Saya membacanya dan memutuskan. Apa yang diputuskan dihimpunkan dalam helaian arahan yang dipanggil Goal dan ditampal ke dalam tetingkap kerja. Ia termasuk kelulusan awal dan syarat lulus yang boleh dinilai mesin. Tetingkap kerja membacanya dan meneruskan hingga akhir, berhenti hanya apabila sesuatu gagal.

Saya juga meminta helaian arahan memasukkan anggaran bila kerja akan siap. Saya menyelitkan kerja ini di antara waktu buka bar, jadi jika saya tidak tahu berapa lama sesuatu akan mengambil masa, saya tidak dapat merancang hari saya.

Peranan pemilik bukan membaca tetapi memutuskan. Saya tidak perlu membaca kesemua 1,775 log perbualan. Saya menjawab soalan tentang fakta bar. Saya membuat keputusan tentang perkara yang hanya boleh diputuskan oleh dasar bar. Selepas sesuatu dilancarkan, saya sendiri mencuba dan mengendalikannya lima atau enam kali untuk menyemak sama ada ada yang terasa tidak kena. Itu sahaja.

Sebelum sampai ke bentuk ini, saya mengulang kerja berkali-kali. AI menambah ciri sendiri dan skrin menjadi tidak stabil. Kerja membesar tanpa had daripada satu arahan. Menunggu kelulusan pada setiap peringkat bermakna tiada apa yang bergerak ke hadapan. Setiap kali, saya menambah satu peraturan, dan begitulah ia sampai ke bentuknya sekarang. Ini juga masih berkembang.

#### Apa yang Boleh Anda Bawa Pulang daripada Bab Ini

- Untuk kerja yang berulang, jadikan prosedur itu sendiri sebagai dokumen dan serahkan kepada AI. Jika anda membetulkan dokumen prosedur setiap kali ia gagal, kali berikutnya menjadi lebih mudah
- Bina bahagian bersama (log masuk, pengebilan, navigasi) sekali sahaja dan gunakan semula merentasi semua produk. Jika asasnya kecil, jualan kecil pun boleh menampung anda
- Manusia hanya melakukan pertimbangan dan operasi yang hanya manusia boleh buat. Jika AI menyerahkan apa-apa selain itu kepada anda, tambahkannya ke dalam dokumen prosedur

Sambungan bab ini (buku-buku seterusnya yang saya bina, dan pengajaran yang saya tambah pada dokumen prosedur) ada di note dan X. note https://note.com/bontallc / X https://x.com/tamuro\_hnakano
