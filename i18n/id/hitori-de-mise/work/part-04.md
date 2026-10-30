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

