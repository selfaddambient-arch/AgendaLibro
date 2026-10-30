## Bab 4: Amali Bahagian 2 - Menjadikan Kerja Harian Lebih Cekap (Menggunakan AI Multimodal)

~Siapkan "kerja memasukkan data yang meletihkan" dengan sebuah telefon pintar~

### 4-1. Kesukaran Mengemas Kini Senarai Wain

Bagi pemilik bar atau restoran, mengemas kini buku menu ialah beban yang tidak glamor tetapi berat.

Yang paling menyusahkan saya ialah membuat "senarai wain."

Setiap kali wain baharu tiba, kerja berikut diperlukan.

1.  Melihat label botol (tulisan berangkai bahasa asing, sukar dibaca).

2.  Menaip nama jenama dan vintaj (tahun) ke dalam PC tanpa kesilapan.

3.  Mencari ciri dan rasa wain itu dalam talian.

4.  Menulis "pengenalan" yang membuatkan pelanggan mahu membacanya.

5.  Memikirkan hidangan yang sepadan dengan wain itu (padanan).

Melakukan semua ini dengan kamus di tangan, di celah-celah waktu sibuk, hampir mustahil. Saya akan menangguhkannya dengan "nanti saja," dan senarai cadangan sering kali tidak pernah dikemas kini.

### 4-2. Ambil Gambar Sahaja. Kejutan "Gem Senarai Wain"

Maka saya memutuskan untuk mencuba "ciri multimodal (pengecaman imej)" Gemini.

Kaedahnya begitu mudah sehingga tidak disangka-sangka.

1.  Ambil gambar botol wain dengan telefon pintar anda.

2.  Hantar gambar itu kepada Gemini.

3.  Tambah satu baris: "Jadikan senarai."

Itu sahaja.

![Gambar label botol wain sebenar yang diambil dengan telefon pintar](images/fig-19.jpg)

Gemini kemudian serta-merta membaca maklumat label daripada gambar itu.

Ia bukan sahaja menyalin nama jenama, seperti "Cave d'Occi Winery, Tsukimi de Ippai 2024," tetapi juga mencari cirinya dalam pangkalan data dalam talian yang besar dan menjana huraian yang menarik secara automatik.

Yang lebih mengejutkan saya ialah ia turut mengeluarkan "cadangan padanan" sebagai satu set.

Cadangan seperti "Aroma pekat wain ini sesuai dengan ○○" muncul di skrin dalam beberapa saat.

Berjam-jam yang dahulu saya habiskan bergelut dengan kamus kini tinggal satu klik pada pengatup telefon.

### 4-3. Membuat "Gem" Anda Sendiri

Untuk menjadikan kerja ini jauh lebih cekap, saya seterusnya menggunakan ciri bernama "Gems."

Ia "ciri AI tersuai milik anda sendiri" di mana anda boleh meminta AI menghafal peranan dan peraturan tertentu terlebih dahulu.

Menerangkan semuanya dari awal setiap kali, "Anda seorang sommelier. Lihat gambar ini dan..." sangat meletihkan.

Maka saya mendaftarkan "arahan (prompt)" berikut kepada Gemini terlebih dahulu. Ini ialah isi kepala "AI sommelier khas" bar saya.

#### Arahan yang Benar-benar Saya Daftarkan

> Baca imej dan buat senarai wain dalam format berikut.
>
> Untuk harga, jangan gunakan harga pasaran. Kira dengan menganggap harga botol di restoran biasa (kira-kira 2.5 hingga 3 kali ganda kos).
>
> Jangan gunakan format jadual. Buatkan supaya muat pada satu atau dua helai kertas A4.
>
> Format hanyalah rujukan; buat senarai dengan menggunakan hanya apa yang telah dimasukkan.
>
> Formatnya di bawah.
>
> United Kingdom 🇬🇧
>
>  Ridgeview Bloomsbury NV  ¥8,500 (kira-kira $57)
>
>  Emas pucat dengan gelembung yang menyenangkan. Bayangan tembikai dan madu di celah aroma sitrus... (selebihnya ditinggalkan)

Sebenarnya, separuh bawah prompt ini, bahagian "format (contoh)".

Saya tidak mencipta daripada kosong.

Dahulu, ketika mencari maklumat wain dalam talian, saya akan berfikir, "Oh, huraian kedai ini mudah difahami," atau "Cara laman ini menulis membuatnya kedengaran sedap," dan saya hanya menyalin dan menampal petikan seperti itu ke dalam buku nota, berulang kali.

Saya melontarkan "memo kain perca" itu kepada Gemini seadanya.

"Ini petikan yang saya salin dan kumpulkan beberapa lama dahulu. Tirulah nada ini dan tulis tentang wain dalam gambar baharu juga."

Itu sahaja yang saya katakan.

Namun arahan ini mengandungi tiga kaedah bijak yang mengurangkan beban di kedai.

① "Logik pengiraan harga"

Ini penjimat masa terbesar. Kerana saya mengarahkan ia memberi "harga yang akan dikenakan restoran" dan bukan "harga pasaran," AI mengira ke belakang daripada harga belian lazim dan memberi angka seperti "¥8,500 (kira-kira $57)" yang boleh terus masuk ke menu. (Sudah tentu keputusan akhir di tangan pemilik, tetapi adanya panduan memudahkan segalanya.)

② "Bukan format jadual, tetapi muat pada kertas A4"

Jika output datang dalam format jadual seperti Excel, susun atur menjadi kucar-kacir apabila ditampal ke dalam buku menu. Dengan meminta ia menulis dalam "format menu A4" sejak awal, saya menyasarkan output yang boleh dicetak dan digunakan seadanya.

③ Menggunakan teks web yang disalin-tampal sebagai "contoh"

Daripada meminta secara kabur, "Tulis huraian yang bagus," saya menunjukkan contoh konkrit (memo salin-tampal saya): "bendera 🇬🇧 + nama wain + harga + huraian yang menggamit deria."

Apabila AI ditunjukkan contoh, ia faham, "Oh, inilah nada dan cara yang patut saya tulis," dan ketepatan output melonjak. Dalam istilah teknikal ini dipanggil "few-shot prompting," tetapi pada dasarnya ia sama seperti "mengajar melalui teladan."

Dan "teladan" itu boleh terdiri sepenuhnya daripada teks yang ditemui, setara bertulis kepada gambar yang ditemui dari web.

![Teks senarai wain siap yang dikeluarkan oleh Gemini](images/fig-20.png)

### 4-4. Tidak Perlu Imej Pun. Revolusi Salin-Tampal daripada LINE

Kelebihan "Gem Senarai Wain" ini ialah inputnya tidak terhad kepada gambar.

Sebenarnya, di bar anda kerap membuat pesanan dengan kedai arak melalui LINE, bukan?

Apabila pesanan selesai, mesej seperti ini tiba daripada kedai arak.

> "Terima kasih seperti biasa. Kami telah menerima pesanan anda seperti berikut.
>
> ・Cave d'Occi Tsukimi de Ippai Blanc 24 3 botol
>
> ・Ridgeview Bloomsbury 6 botol
>
> ・○○ (wain baharu) 2 botol
>
> Kami akan menghantar esok."

Suatu hari terlintas di fikiran saya: "Bolehkah saya gunakan teks ini seadanya?"

Sebagai ujian, saya menyalin mesej LINE ini dengan jari dan terus melontarkannya ke dalam Gemini.

Hasilnya sempurna.

Gemini hanya mengenali "nama produk" dalam mesej LINE itu, mencari maklumat dalam talian, dan membuat senarai dalam format biasa (bendera + harga + huraian).

Dengan kata lain, saya tidak perlu menunggu botol tiba dan mengambil gambar.

Pada saat saya membuat pesanan, hanya dengan menyalin dan menampal di dalam telefon, senarai menu siap sebelum produk tiba.

Tidak perlu membuka PC, tidak perlu memulakan kamera.

Di satu sudut dapur, atau di dalam kereta api, kerja selesai hanya dengan beberapa sentuhan pada telefon.

Bukankah ini "kecekapan sebenar" yang patut dimiliki oleh pemilik solo yang bekerja seorang diri?

### 4-5. Cadangan AI × Pertimbangan Lantai Kedai (Realiti)

Walau begitu, saya tidak menelan cadangan AI bulat-bulat. Yang penting di sini ialah "pertimbangan manusia kita di kedai."

Suatu ketika, AI membuat cadangan ini untuk dipadankan dengan sebuah wain:

AI: "Untuk wain merah ini, itik panggang dengan sos oren ialah padanan yang sempurna."

Cadangan yang indah, tetapi malangnya hari itu tiada itik dalam peti sejuk kedai.

Saya tidak berfikir, "AI kata begitu, jadi saya mesti beli itik." Beginilah cara saya berfikir:

Saya (di kedai): "Kita tiada itik, tetapi hari ini ada ayam kampung yang bagus masuk. Lemaknya setanding itik, jadi saya akan bakar ayam ini sehingga kulitnya rangup dan menyiapkannya dengan sos berperisa oren, seperti yang dikatakan AI."

"Pengetahuan AI (itik dan oren sepadan)" × "stok di kedai (kita ada ayam)" = "item menu baharu yang meyakinkan dan realistik."

Gabungan inilah kegembiraan sebenar membangunkan menu dengan AI.

AI memberi jawapan buku teks, tetapi ia tidak tahu apa yang ada dalam peti sejuk hari ini. Mengisi jurang itu ialah tugas anda sebagai pemilik.

### 4-6. Langkah Terakhir: AI Tidak Boleh "Merasa"

Ada satu lagi perkara yang tidak boleh sekali-kali diserahkan kepada AI.

Iaitu sesi merasa yang anda lakukan sebelum apa-apa dihidangkan kepada pelanggan.

Huraian dan padanan yang ditulis AI berdasarkan "data am dari dunia luas."

Tetapi wain ialah benda hidup. Walaupun label yang sama, rasanya berubah mengikut vintaj dan cara ia disimpan.

Pernah sekali, AI menulis huraian untuk wain putih: "Wain kering yang segar dan ringan. Sempurna dengan carpaccio makanan laut."

Tetapi apabila saya benar-benar membuka botol itu dan merasanya, ia lebih matang daripada jangkaan saya, dengan nota pekat seperti madu.

"Jika saya hidangkan ini sebagai 'wain kering yang ringan,' pelanggan akan kecewa... Ia lebih sesuai dengan ayam sos krim berbanding carpaccio."

Saya segera membetulkan teks yang dihasilkan Gemini.

- Sebelum (AI): "Segar dan ringan. Sesuai untuk pembuka selera"

- Selepas (manusia): "Pekat, berbadan penuh daripada pematangan. Cukup kuat untuk menemani hidangan utama"

AI membuat 90% draf, dan manusia merasanya serta menambah "10% terakhir (jiwa)."

Semakan ini tanggungjawab seorang pemilik restoran, dan ia sesuatu yang tidak akan dapat ditiru oleh AI.

Bukan "kerana AI kata begitu," tetapi "kerana saya meminumnya dan ia sedap."

Untuk menghidangkan dengan keyakinan itu, hari ini pun saya masih merasa wain yang baru dibuka, dengan senarai buatan AI di sebelah tangan.

#### Ruangan 3: Petua Mengambil Gambar supaya AI Melihatnya dengan "Betul"

~ Seperti menunjukkan label kepada seorang sommelier ~

Apabila anda menghantar gambar kepada Gemini, beberapa tip kecil boleh meningkatkan secara mendadak sejauh mana ia mengecam apa yang dilihatnya.

1.  Elakkan silau: Label botol mudah memantulkan cahaya, jadi ubah sudut sedikit, atau hadang cahaya dengan badan anda semasa mengambil gambar.

2.  Ambil beberapa keping dan hantar bersama: Untuk perkara seperti isi peti sejuk, hantar gambar lebar dan gambar dekat bersama-sama, dan AI akan mengecam malah barang di sudut tersembunyi.

3.  Tunjuk dengan jari: Ia juga membantu jika anda menunjuk bahagian yang anda mahu AI lihat semasa mengambil gambar. Letakkan sesuatu seperti "Saya menunjuk dengan jari" dalam prompt. Ia sama seperti menunjuk pada menu di restoran di luar negara.
