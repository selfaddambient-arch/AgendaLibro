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

