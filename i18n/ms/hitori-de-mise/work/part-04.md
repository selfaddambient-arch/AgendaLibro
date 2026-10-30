AI segera mencadangkan "TAMURO" sans-serif yang ringkas dan tegas.

![Logo sans-serif](images/fig-14.png)

#### Langkah 2: Menghembus "Makna" ke dalam Bentuk

Di sinilah ujian sebenar bermula. Huruf biasa tidak bermakna apa-apa. Dan hanya ada "M" di tengah pun tidak menyampaikan banyak.

"Saya mahu menyatakan asal usul nama itu, 'orang berkumpul.' Bolehkah anda menyatukan keseluruhannya menjadi 'bulatan' yang mesra, sambil membentuk setiap huruf abjad supaya kelihatan seperti orang yang bergerak dengan gembira?"

Ini pesanan yang sangat abstrak. Tetapi imaginasi penolong pengurus saya (AI) melebihi jangkaan saya.

Apa yang dicetuskan AI ialah reka bentuk di mana rangka huruf "T," "A," "M" dan seterusnya diubah menjadi siluet orang yang menari dengan tangan dan kaki terbentang.

![Logo yang membentuk abjad menyerupai orang](images/fig-15.png)

#### Langkah 3: Tarik Tali antara Reka Bentuk dan Kebolehbacaan

"Menarik! Tetapi begini, kita tak dapat baca 'TAMURO'..."

Jika anda terlalu menumpukan pada reka bentuk, ia tidak lagi dikenali sebagai tulisan, dan jika anda menumpukan pada tulisan, ia kehilangan daya tarikan. Saya berdepan dengan dilema ini.

Dari sini, ia soal penalaan halus yang berulang.

"Huruf 'A' kelihatan seperti orang, bagus, tetapi tekankan sedikit lagi strukturnya sebagai 'A.' Letakkan palang tengah dengan kukuh."

"Keseimbangan keseluruhan baik, tetapi orang-orangnya terlalu rapat dan kelihatan sempit. Tinggalkan sedikit lagi ruang yang ceria."

"Gabungkan orang-orang menari tadi dengan huruf TAMURO, dan jadikan ia bulatan!"

![Tanda logo bulat "TAMURO," siap selepas cuba jaya](images/fig-16.png)

Walaupun dibuat daripada siluet orang yang bertenaga, sekali pandang pada bahagian bawah dan anda dapat membaca "TAMURO" dengan jelas.

Dengan berbalas idea bersama AI berulang kali, saya mendapat logo yang saya puas hati, yang menggabungkan kebolehbacaan, mutu reka bentuk, dan lebih-lebih lagi "hasrat" yang saya curahkan ke dalam bar ini.

Kini ia digunakan sebagai ikon akaun X (dahulu Twitter) dan Instagram bar ini.

### 3-6. Halangan Pertama: Pemotongan Mudah dan "Perangkap Kualiti Imej"

Cabaran kreatif membuat logo sudah selesai.

Tetapi kerja belum siap.

Kembali kepada pelekat LINE. Apa yang ada di tangan saya ialah "helaian" dengan 25 ilustrasi dilukis pada satu halaman.

Untuk memohon pendaftaran pelekat LINE, saya perlu memotong setiap satu, menjadikan latar telus, dan mengubah saiznya. Ia kerja meletihkan yang sudah lama saya tangguhkan.

"Mustahil saya boleh memotong semua ini dengan tangan..."

Saya berunding dengan Gemini dan meminta penyelesaian. Gemini berkata dengan selamba:

"Mari kita automasikan menggunakan bahasa pengaturcaraan bernama Python."

Jujurnya, saya hampir berputus asa di situ juga.

"Python? Saya pernah dengar namanya, tetapi memasang perisian seperti itu pada komputer saya menakutkan. Persediaannya pun kedengaran sukar. Jangan harap sebanyak itu daripada orang yang menjalankan bar..."

Tetapi ini salah satu kemuncak buku ini. Seolah-olah dapat merasai apa yang saya fikirkan, Gemini membuat cadangan yang mengejutkan.

Gemini:

"Anda tidak perlu menyediakan persekitaran apa-apa pun. Gunakan alat Google percuma bernama 'Google Colab.' Ia berjalan dalam pelayar anda, jadi anda hanya perlu menyalin dan menampal kod yang saya tulis ke dalamnya, dan ia akan terus berfungsi."

"Apa? Ada benda macam itu?"

Saya tidak percaya apa yang saya dengar. Saya tidak pernah membayangkan ada persekitaran di mana pengaturcaraan berjalan hanya dalam pelayar, tanpa apa-apa dipasang pada PC saya sendiri.

Bukan "selepas saya belajar Python," tetapi "AI memberitahu saya malah tentang kewujudan alat itu (Colab)."

Pada saat itu, andaian saya bahawa "pengaturcaraan bermaksud banyak persediaan" runtuh.

### 3-7. Jangan "Baca" Skrin Ralat, "Ambil Gambar dan Hantar"

Seperti yang diarahkan, saya membuka Google Colab, menampal kod, dan menekan butang main.

Tetapi realiti tidak semudah itu. Yang muncul di skrin ialah deretan teks merah menyala... mesej ralat.

"Error: Image file not found..."

Saya yang dahulu akan alah hanya dengan melihat ralat ini dan senyap-senyap menutup pelayar.

Tetapi kini saya mempunyai sekutu: AI "multimodal," AI yang bermata.

Saya tidak mencuba pun membaca mesej ralat itu.

Saya hanya mengambil tangkapan skrin dan terus menampalnya ke dalam kotak sembang Gemini.

Dan saya menambah satu baris: "Ada ralat muncul."

![Menampal skrin ralat Google Colab ke dalam Gemini seadanya](images/fig-17.png)

Gemini menganalisis imej itu serta-merta dan menghantar jawapan.

Gemini:

"Ah, nama fail imej yang dimuatkan salah. Saya telah membetulkan kod supaya menggunakan '.jpg'. Sila jalankan semula dengan versi ini."

"...Wah, seronoknya!"

Interaksi ini terasa kurang seperti pengaturcaraan dan lebih seperti permainan "cari perbezaan" atau permainan berbalas-balas.

- Saya: (menampal tangkapan skrin) "Berhenti lagi."

- Gemini: "Saiz imej tidak sepadan. Saya akan tambah fungsi yang melaraskannya secara automatik."

- Saya: (menampal tangkapan skrin) "Kali ini imej kelihatan pecah."

- Gemini: "Saya terlupa menambah proses bernama 'LANCZOS' yang mengekalkan kualiti imej. Saya akan betulkan."

Saya tidak faham satu baris pun kod itu. Apabila ralat muncul, saya hanya mengambil tangkapan skrin dan melontarkannya kepada AI sambil berkata "Tengok!"

"Penyerahan analisis ralat" inilah rahsia terbesar bagaimana saya, dengan pengetahuan sifar, berjaya membina sistem, dan pada masa yang sama ia pengalaman yang paling mengujakan.

### 3-8. Tembok Terbesar: "Ketidaksejajaran Lukisan Tangan" dan "Terkeluar Garisan"

Sambil saya meneruskan "perbualan bernama ralat" ini, sistem itu semakin diperhalus.

Dan akhirnya saya memasuki cabaran terbesar: "Fasa 2: Pemotongan Automatik Susun Atur Lukisan Tangan."

Saya mula mahukan lebih.

"Mari buat helaian 5×5, 25 pelekat. Dan oleh kerana saya mahu rasa buatan tangan yang lebih kuat, saya mahu meletakkannya dengan bebas, tanpa terikat pada garisan grid."

Dengan kod yang hanya membahagi helaian sama rata, tangan atau tulisan watak terkeluar ke sel sebelah dan terpotong dengan teruk.

Saya juga mencuba kaedah "memotong semuanya kecuali latar putih," tetapi jidarnya tidak sekata dan ia gagal.

Saya hampir berputus asa. Lalu, menggunakan gerak hati daripada zaman saya sebagai orang sistem, saya memberitahu Gemini:

"Saya mahu anda lupakan idea memotong imej dengan gunting. Sebaliknya, lihat sel mana 'titik tengah' setiap gambar berada. Jika titik tengahnya berada dalam sel itu, maka walaupun ia terkeluar sedikit, anggap seluruh gambar itu 'milik sel itu' dan masukkan ke dalam baldi sel itu."

Inilah penyelesaian yang saya namakan "kaedah baldi grid."

Mengapa saya terfikir "memasukkan ke dalam baldi mengikut titik tengah" dan bukan "memotong dengan gunting"?

Cara berfikir orang awam (analog): Anda membayangkan "menggunting satu gambar dengan gunting." Dengan cara itu, anda memotong tepat pada garisan, dan tangan serta kaki watak terpotong.

Cara berfikir orang sistem (digital): Komputer tidak mempunyai deria fizikal "memotong." Sebaliknya, ia mempunyai "koordinat (kedudukan)." Beginilah saya melihatnya: "Walaupun terkeluar sedikit, selagi 'pusat (titik tengah)' gambar itu berada dalam sel, kita boleh menganggap seluruh gambar itu 'milik sel ini.'"

![Idea analog "memotong mengikut garisan" dan idea digital "memilih mengikut titik"](images/fig-18.png)

Inilah maksud "menterjemahkan kerja analog yang kabur kepada peraturan digital yang jelas." Apabila anda memberi arahan kepada AI, memikirkan peraturan seperti ini, yang jawapannya keluar sama "tidak kira siapa yang melihat (atau mengira)," akan berkesan.

Gemini menukar permintaan abstrak ini kepada kod dengan indah. Hasilnya sempurna.

Tulisan "Thank you!" dan ekor yang terkeluar ke sel jiran semuanya berjaya dikesan dengan kemas dan dikumpulkan sebagai pelekat tunggal.

Ia malah menunaikan permintaan istimewa saya, "Yang terakhir (ke-25) tidak diperlukan, jadi langkaulah." Akhirnya, saya mempunyai alat di mana "anda hanya memasukkan imej dan menekan butang, lalu satu set imej lengkap untuk permohonan LINE dihasilkan."

Yang saya lakukan hanyalah menyampaikan "masalah di lapangan (gambar terpotong)" dan mencadangkan "penyelesaian logik (tentukan mengikut titik tengah)." AI menulis semua kod yang sukar.

Inilah intipati "vibe coding," membina sistem bermula daripada pengetahuan sifar.

#### Ringkasan Bab 3

1.  Melukis dengan AI bukan "sekali siap." Anda boleh membuatnya semula sebanyak mana yang anda suka mengikut keadaan: menukar watak, menambah suasana bermusim, menukar medium.

2.  Malah "konsep" yang abstrak (orang berkumpul) boleh dijadikan "bentuk" (logo) melalui dialog berulang.

3.  Kerja meletihkan (memotong imej) memang sesuai diautomasikan oleh Gemini × Google Colab. Ralat boleh diselesaikan dengan tangkapan skrin.

#### Ruangan 1: Kursus Kilat "Google Colab" untuk Pemilik Bukan Teknikal

~Gunakan "dapur sewa" dan biarkan PC anda seperti sedia ada~

"Google Colab," yang muncul dalam teks utama. Melakukan pengaturcaraan (Python) pada komputer sendiri ibarat "membuat ramen tulen dari awal, bermula dengan sup, di dapur rumah anda." Persediaannya amat menyusahkan.

Google Colab pula ialah "dapur sewa percuma yang lengkap dengan alat memasak." Buka sahaja pelayar anda dan alat terbaik sudah tersedia. Anda tidak perlu mengubah apa-apa tetapan pada komputer anda. Anda boleh mengaturcara hanya dengan pelayar sambil mengekalkan persekitaran anda bersih. Mulakan dengan mencari "Google Colab" dan jenguklah dapur sewa ini.

#### Ruangan 2: Tidak "Membaca" Skrin Ralat Ialah Jawapan yang Betul

~Kuasai senjata muktamad: tangkapan skrin~

Apabila ralat muncul, adakah anda bersungguh-sungguh cuba mentafsir mesej dalam bahasa Inggeris? Itu membuang masa.

Apabila sesuatu rasa tidak kena semasa memasak, anda minta tukang masak merasainya. Dengan cara yang sama, tunjukkan sahaja kepada AI "tangkapan skrin (screen capture)."

- Windows: \[Win\] + \[Shift\] + \[S\]

- Mac: \[Cmd\] + \[Shift\] + \[4\]\
  Tekan kekunci ini, lukis kotak di sekeliling ralat, dan tampal ke dalam Gemini. Itu sahaja. Jangan "baca ralat," "tunjukkan ralat." Hanya dengan mengubah minda seperti ini, kelajuan pembangunan anda akan meningkat tiga kali ganda.

Saya telah memperkenalkan beberapa contoh setakat ini, dan segala yang saya lakukan terangkum dalam tiga perkara berikut.

・Jangan menuntut bentuk siap sekali gus (anggaplah ia dialog)\
・Katakan "tidak, bukan begini" tanpa segan\
・Anggaplah kos pembetulan ialah sifar dan lontarkan permintaan dengan selamba

Anda tidak memerlukan bakat reka bentuk. Yang anda perlukan hanyalah keberanian untuk menyatakan "ada sesuatu yang mengganggu saya" dalam kata-kata.
