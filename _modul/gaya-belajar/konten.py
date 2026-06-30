# -*- coding: utf-8 -*-
"""Konten Modul "Gaya Belajar" (Kelompok 10) - mata kuliah Belajar dan Pembelajaran.
Disusun premium sesuai FORMAT MODUL BnP 2026. Humanized (tanpa em-dash/kutip keriting/emoji).
Blok isi: ('h2',teks) | ('p',teks) | ('nlist',[..]) | ('blist',[..])
         | ('table',{no,judul,head,rows,sumber}) | ('fig',{no,judul,file,sumber})
         | ('box',{kind,judul,body:[blok]})  kind: tujuan|contoh|aktivitas|ringkasan|tips
Target: 100% rubrik dosen (materi, struktur, penyajian, aktivitas/refleksi/evaluasi,
kreativitas/tampilan, referensi).
"""

JUDUL = "GAYA BELAJAR"
SUBJUDUL = "Mengenal dan Mengoptimalkan Cara Belajar Mahasiswa"
MATKUL = "Mata Kuliah Belajar dan Pembelajaran"
TIM = [
    ("Balqis Sandra Lejla", "202501500525"),
    ("Motiara Sangadji", "202501500515"),
    ("Nurjali Sangadji", "202501500505"),
]
PRODI = "Program Studi Bimbingan dan Konseling"
FAKULTAS = "Fakultas Ilmu Pendidikan dan Pengetahuan Sosial"
KAMPUS = "Universitas Indraprasta PGRI"
TAHUN = "2026"
KELOMPOK = "Kelompok 10"

KATA_PENGANTAR = [
    "Segala puji bagi Allah Subhanahu wa Ta'ala atas limpahan rahmat, taufik, serta hidayah-Nya, sehingga modul pembelajaran berjudul Gaya Belajar: Mengenal dan Mengoptimalkan Cara Belajar Mahasiswa ini dapat penulis selesaikan dengan baik. Shalawat dan salam semoga senantiasa tercurah kepada Nabi Muhammad shallallahu alaihi wa sallam beserta keluarga dan para sahabatnya.",
    "Modul ini disusun untuk memenuhi tugas kelompok pada mata kuliah Belajar dan Pembelajaran, Program Studi Bimbingan dan Konseling, Fakultas Ilmu Pendidikan dan Pengetahuan Sosial, Universitas Indraprasta PGRI. Penyusunannya berangkat dari satu kenyataan sederhana, yaitu bahwa setiap mahasiswa memiliki cara belajar yang berbeda, namun belum semua menyadari dan memanfaatkannya. Pemahaman tentang gaya belajar membantu mahasiswa memilih strategi yang paling sesuai dengan dirinya, sehingga proses belajar terasa lebih efektif, efisien, dan menyenangkan.",
    "Materi disajikan secara sistematis dan dilengkapi contoh konkret, ilustrasi, tabel, diagram, aktivitas belajar, refleksi, serta evaluasi agar mudah dipahami dan diterapkan. Penulis menyampaikan terima kasih kepada dosen pengampu mata kuliah Belajar dan Pembelajaran atas bimbingannya, serta kepada semua pihak yang telah membantu penyusunan modul ini.",
    "Penulis menyadari modul ini masih jauh dari sempurna. Oleh karena itu, kritik dan saran yang membangun sangat penulis harapkan demi penyempurnaan pada kesempatan berikutnya. Semoga modul ini bermanfaat bagi mahasiswa dan pembaca lain dalam menumbuhkan kebiasaan belajar yang efektif sesuai gaya belajar pribadinya.",
]

# PENDAHULUAN: list blok
PENDAHULUAN = [
    ("h2", "Apa yang Akan Dipelajari?"),
    ("p", "Modul ini membahas gaya belajar, yaitu cara yang menjadi preferensi seseorang dalam menerima, mengolah, dan menyimpan informasi selama proses belajar. Pembaca akan diajak memahami konsep dasar gaya belajar, mengenali tiga tipe utamanya, yaitu visual, auditorial, dan kinestetik, serta mempelajari beragam strategi belajar efektif yang sesuai dengan masing-masing gaya. Pada akhirnya, pembaca diharapkan mampu mengenali gaya belajarnya sendiri dan menerapkan strategi yang tepat agar proses belajar menjadi lebih optimal."),
    ("h2", "Tujuan Pembelajaran"),
    ("p", "Setelah mempelajari modul ini secara lengkap, pembaca diharapkan mampu:"),
    ("nlist", [
        "Menjelaskan pengertian, hakikat, dan pentingnya gaya belajar dalam proses pembelajaran.",
        "Mengidentifikasi teori-teori utama yang melandasi konsep gaya belajar.",
        "Membedakan karakteristik tiga tipe gaya belajar, yaitu visual, auditorial, dan kinestetik.",
        "Menganalisis gaya belajar pribadi melalui aktivitas identifikasi diri.",
        "Menerapkan strategi belajar yang sesuai dengan gaya belajar masing-masing.",
        "Mengembangkan kebiasaan belajar yang efektif dan adaptif sesuai karakteristik diri.",
    ]),
    ("h2", "Cara Menggunakan Modul"),
    ("p", "Modul ini dirancang untuk pembelajaran mandiri sehingga dapat dipelajari secara bertahap dan sistematis. Pembaca disarankan membaca modul secara berurutan mulai dari Pendahuluan hingga Penutup. Setiap bab dilengkapi tujuan pembelajaran, uraian materi, contoh atau ilustrasi, aktivitas, serta ringkasan. Setelah mempelajari ketiga bab, pembaca diarahkan melakukan refleksi terhadap proses belajarnya dan mengerjakan evaluasi untuk mengukur pemahaman. Ikuti setiap petunjuk aktivitas dengan saksama dan kerjakan tugas secara mandiri."),
    ("h2", "Sasaran Pembaca"),
    ("p", "Modul ini ditujukan terutama bagi mahasiswa semester awal yang sedang mempelajari mata kuliah Belajar dan Pembelajaran atau mata kuliah pengantar lainnya. Modul ini juga dapat dimanfaatkan oleh siswa SMA atau MA kelas akhir yang ingin mempersiapkan diri memasuki perguruan tinggi, serta siapa saja yang tertarik memahami cara belajar yang efektif sesuai karakteristik dirinya. Bahasa yang digunakan disusun agar mudah dipahami oleh pembaca pemula di bidang ilmu pendidikan."),
    ("h2", "Manfaat Memahami Gaya Belajar"),
    ("p", "Pemahaman tentang gaya belajar memberikan banyak manfaat praktis bagi mahasiswa. Berikut manfaat-manfaat utamanya:"),
    ("nlist", [
        "Meningkatkan efektivitas belajar. Mahasiswa yang memahami gaya belajarnya dapat memilih strategi yang paling tepat, sehingga hasil belajar lebih maksimal dengan waktu yang lebih singkat.",
        "Menghemat waktu dan tenaga. Dengan strategi yang sesuai, mahasiswa tidak perlu mencoba berbagai cara yang kurang efektif, sehingga energi dapat difokuskan pada cara yang paling produktif.",
        "Meningkatkan motivasi dan kepercayaan diri. Ketika belajar terasa mudah dan menyenangkan, motivasi untuk terus belajar pun meningkat.",
        "Mengurangi stres akademik. Kesesuaian strategi belajar dengan gaya belajar mengurangi kebosanan dan frustrasi yang sering muncul saat belajar.",
        "Membantu perencanaan karier. Pemahaman tentang gaya belajar turut membantu mahasiswa memilih bidang dan lingkungan kerja yang sesuai dengan karakteristik dirinya.",
    ]),
]

BAB = []  # diisi via append di file berikutnya



# ===================== BAB I =====================
BAB.append({
 "no": "I", "judul": "MEMAHAMI KONSEP DAN TEORI GAYA BELAJAR",
 "isi": [
  ("box", {"kind": "tujuan", "judul": "Tujuan Pembelajaran", "body": [
     ("p", "Setelah mempelajari bab ini, pembaca diharapkan mampu:"),
     ("nlist", [
        "Menjelaskan pengertian dan hakikat gaya belajar.",
        "Menguraikan teori-teori yang melandasi konsep gaya belajar.",
        "Menjelaskan pentingnya memahami gaya belajar bagi mahasiswa.",
        "Menganalisis hubungan antara gaya belajar dan keberhasilan akademik.",
     ]),
  ]}),
  ("h2", "1.1 Pengertian Gaya Belajar"),
  ("p", "Gaya belajar atau learning style merupakan cara khas atau kecenderungan individu dalam menyerap, mengolah, mengorganisasi, dan memahami informasi selama proses belajar. Setiap individu memiliki gaya belajar yang berbeda, dan tidak ada gaya belajar yang lebih baik atau lebih buruk dibandingkan yang lain. Gaya belajar bersifat netral; yang menentukan keberhasilan belajar adalah kesesuaian antara gaya belajar dengan strategi yang digunakan (DePorter, Reardon, & Singer-Nourie, 2014)."),
  ("p", "Menurut DePorter, Reardon, dan Singer-Nourie (2014), gaya belajar adalah gabungan dari bagaimana seseorang menyerap, mengatur, dan mengolah informasi. Pritchard (2017) menambahkan bahwa gaya belajar mengacu pada cara alami atau kebiasaan yang dimiliki seseorang dalam memperoleh dan memproses informasi baru. Dengan demikian, gaya belajar merupakan karakteristik individu yang relatif menetap dan memengaruhi cara seseorang merespons lingkungan belajarnya."),
  ("h2", "1.2 Hakikat dan Karakteristik Gaya Belajar"),
  ("p", "Gaya belajar memiliki beberapa karakteristik penting yang perlu dipahami. Pertama, gaya belajar bersifat unik pada setiap individu; tidak ada dua orang yang memiliki gaya belajar persis sama. Kedua, gaya belajar relatif stabil, tetapi tetap dapat dikembangkan seiring pengalaman belajar. Ketiga, gaya belajar bersifat netral, artinya tidak ada gaya belajar yang lebih unggul secara mutlak. Keempat, pemahaman terhadap gaya belajar membantu individu memilih strategi belajar yang paling efektif bagi dirinya."),
  ("p", "Slavin (dalam Schunk, 2020) menjelaskan bahwa perbedaan gaya belajar antarindividu merupakan salah satu faktor yang menjelaskan mengapa strategi pembelajaran yang sama dapat memberikan hasil berbeda pada peserta didik yang berbeda. Inilah pentingnya pendekatan belajar yang berpusat pada karakteristik pembelajar."),
  ("h2", "1.3 Teori-Teori Gaya Belajar"),
  ("p", "Berbagai ahli telah mengemukakan teori tentang gaya belajar. Tiga teori yang paling banyak dirujuk adalah model Visual-Auditorial-Kinestetik (VAK) dari Fleming, teori Multiple Intelligences dari Gardner, dan model belajar pengalaman dari David Kolb. Perbandingan ketiganya disajikan pada tabel berikut."),
  ("table", {"no": "1.1", "judul": "Perbandingan Teori Gaya Belajar",
     "head": ["Aspek", "VAK (Fleming)", "Multiple Intelligences (Gardner)", "Experiential (Kolb)"],
     "rows": [
        ["Fokus", "Modalitas indra", "Jenis kecerdasan", "Siklus pengalaman"],
        ["Jumlah", "3 tipe (VAK)", "8 kecerdasan", "4 tahap siklus"],
        ["Pendekatan", "Preferensi indra", "Kekuatan kecerdasan", "Proses pengalaman"],
        ["Penerapan", "Strategi belajar", "Kurikulum variatif", "Refleksi dan aksi"],
     ], "sumber": "Diolah penulis dari Fleming (1987), Schunk (2020), dan Pritchard (2017)."}),
  ("p", "Modul ini berfokus pada model VAK (Visual, Auditorial, Kinestetik) yang dikembangkan oleh Neil Fleming karena model ini paling mudah dipahami dan paling banyak digunakan dalam konteks pembelajaran, terutama untuk pembelajar pemula. Model VAK juga telah dipakai secara luas dan tersedia instrumen identifikasi gaya belajar yang dapat diakses secara gratis melalui laman resmi VARK-Learn (Fleming, 1987)."),
  ("h2", "1.4 Pentingnya Memahami Gaya Belajar bagi Mahasiswa"),
  ("p", "Bagi mahasiswa, terutama mahasiswa semester awal, memahami gaya belajar memiliki manfaat yang besar. Pertama, pemahaman ini membantu mahasiswa memilih strategi belajar yang sesuai sehingga waktu belajar menjadi lebih efisien. Kedua, mahasiswa dapat mengoptimalkan pemanfaatan media belajar, misalnya memilih cara mencatat tertentu atau memanfaatkan rekaman kuliah. Ketiga, kesadaran terhadap gaya belajar meningkatkan motivasi dan kepercayaan diri karena mahasiswa merasa memiliki kendali atas proses belajarnya."),
  ("p", "Penelitian Widodo dan Sari (2021) terhadap siswa berprestasi menunjukkan bahwa mereka cenderung menggunakan strategi belajar yang sesuai dengan gaya belajarnya, baik visual, auditorial, maupun kinestetik. Pola serupa juga teramati pada mahasiswa, yaitu mereka yang menyelaraskan strategi belajar dengan gaya belajarnya cenderung memperoleh hasil belajar yang lebih baik. Temuan ini memperkuat pandangan Slavin bahwa kesesuaian strategi pembelajaran dengan karakteristik pembelajar merupakan faktor penting dalam keberhasilan akademik."),
  ("h2", "1.5 Hubungan Gaya Belajar dengan Keberhasilan Akademik"),
  ("p", "Gaya belajar bukan satu-satunya penentu keberhasilan akademik, tetapi memiliki peran penting. Keberhasilan akademik dipengaruhi oleh banyak faktor, di antaranya motivasi, kemandirian, lingkungan belajar, kualitas pengajaran, dan strategi belajar yang sesuai dengan gaya belajar. Ketika seorang mahasiswa memahami gaya belajarnya dan mampu memilih strategi yang tepat, proses belajar akan lebih efektif dan efisien, yang pada akhirnya berdampak pada pencapaian akademik yang lebih baik."),
  ("box", {"kind": "contoh", "judul": "Contoh atau Ilustrasi", "body": [
     ("p", "Bayangkan dua mahasiswa yang mempelajari materi sama, misalnya struktur sel tumbuhan. Mahasiswa A lebih mudah paham dengan melihat diagram dan gambar sel berwarna yang menampilkan setiap organel. Mahasiswa B justru lebih cepat paham ketika mendengarkan dosen menjelaskan fungsi tiap organel sambil berdiskusi. Perbedaan ini mencerminkan gaya belajar yang berbeda: A cenderung visual, sedangkan B cenderung auditorial. Keduanya sama-sama dapat berhasil asalkan memakai pendekatan yang sesuai."),
     ("p", "Skema pada Gambar 1.1 menggambarkan bagaimana informasi dari lingkungan diterima oleh indra, lalu diproses sesuai gaya belajar individu, dan akhirnya tersimpan dalam memori jangka panjang sebagai pengetahuan."),
  ]}),
  ("fig", {"no": "1.1", "judul": "Skema Proses Belajar Berdasarkan Gaya Belajar", "file": "fig_1_1.png",
     "sumber": "Diolah penulis dari konsep pemrosesan informasi (Schunk, 2020); ilustrasi dibuat dengan bantuan AI (ChatGPT)."}),
  ("box", {"kind": "aktivitas", "judul": "Aktivitas 1.1: Jurnal Belajar Singkat", "body": [
     ("p", "Sebelum melanjutkan ke Bab II, kerjakan aktivitas berikut untuk menggali pemahaman awal Anda tentang gaya belajar. Ingat kembali pengalaman belajar Anda selama satu bulan terakhir, lalu jawab pertanyaan berikut secara jujur pada buku catatan atau file pribadi Anda:"),
     ("nlist", [
        "Saat belajar materi baru, cara mana yang paling membuat Anda cepat paham: membaca sendiri, mendengarkan penjelasan, atau praktik langsung?",
        "Jika Anda harus menghafal sesuatu, misalnya rumus atau istilah, strategi apa yang biasa Anda gunakan?",
        "Saat menghadapi kesulitan belajar, langkah apa yang biasanya Anda lakukan?",
        "Menurut Anda, apakah gaya belajar Anda sudah sesuai dengan strategi yang Anda gunakan? Jelaskan.",
     ]),
     ("p", "Catatan: aktivitas ini bersifat reflektif. Tidak ada jawaban benar atau salah. Tujuannya membangun kesadaran tentang cara belajar pribadi Anda."),
  ]}),
  ("h2", "1.6 Faktor-Faktor yang Memengaruhi Gaya Belajar"),
  ("p", "Gaya belajar seseorang tidak terbentuk dengan sendirinya, melainkan dipengaruhi oleh berbagai faktor yang bekerja secara kombinasi dan saling berinteraksi. Pemahaman terhadap faktor-faktor ini penting agar pembaca melihat gaya belajar sebagai sesuatu yang dinamis dan dapat dikembangkan."),
  ("p", "Faktor pertama adalah faktor biologis dan genetik. Struktur otak dan sistem saraf setiap individu memiliki keunikan yang memengaruhi cara memproses informasi. Faktor kedua adalah faktor lingkungan, mencakup keluarga, sekolah, dan masyarakat. Lingkungan yang kaya stimulus visual, auditorial, atau kinestetik akan mendorong berkembangnya gaya belajar yang sesuai. Faktor ketiga adalah pengalaman belajar masa lalu yang membentuk kebiasaan dan preferensi. Faktor keempat adalah sosial-budaya tempat seseorang tumbuh, dan faktor kelima adalah motivasi serta kepribadian, yang membuat individu dengan motivasi tinggi cenderung lebih aktif mengembangkan strategi belajar bervariasi."),
  ("p", "Kelima faktor tersebut diringkas pada Gambar 1.2 berikut agar lebih mudah diingat."),
  ("fig", {"no": "1.2", "judul": "Faktor yang Memengaruhi Gaya Belajar", "file": "fig_1_2.png",
     "sumber": "Diolah penulis dari Schunk (2020) dan Pritchard (2017); ilustrasi dibuat dengan bantuan AI (ChatGPT)."}),
  ("h2", "1.7 Mitos dan Fakta tentang Gaya Belajar"),
  ("p", "Seiring populernya konsep gaya belajar, muncul sejumlah mitos yang perlu diluruskan. Mitos pertama menyebut gaya belajar bersifat tetap dan tidak bisa berubah; faktanya, gaya belajar dapat berkembang seiring pengalaman dan latihan. Mitos kedua menyatakan gaya belajar tertentu lebih unggul; faktanya, setiap gaya memiliki kelebihan masing-masing dan tidak ada yang superior secara mutlak."),
  ("p", "Mitos ketiga menganggap pengajaran harus selalu disesuaikan secara ketat dengan gaya belajar siswa; faktanya, pendekatan multimodal yang melibatkan banyak indra justru lebih efektif bagi semua pembelajar. Mitos keempat menyatakan tes gaya belajar selalu akurat; faktanya, hasil tes hanya memberikan gambaran preferensi dan dapat berubah seiring waktu. Karena itu, tes gaya belajar sebaiknya dijadikan panduan, bukan label permanen."),
  ("h2", "1.8 Perkembangan Studi Gaya Belajar"),
  ("p", "Kajian tentang gaya belajar berkembang sejak pertengahan abad ke-20. Pada tahun 1950-an, para ahli psikologi pendidikan mulai tertarik pada perbedaan individu dalam cara belajar. Pada tahun 1980-an, konsep gaya belajar memperoleh perhatian besar dengan munculnya berbagai model, termasuk model VAK dari Fleming dan model Kolb. Pada tahun 1990-an hingga 2000-an, muncul kritik terhadap sebagian klaim gaya belajar yang dinilai belum sepenuhnya didukung bukti empiris kuat. Meskipun begitu, aspek preferensi modalitas belajar tetap diakui relevan dalam pembelajaran."),
  ("p", "Di Indonesia, kajian gaya belajar berkembang pesat seiring reformasi pendidikan yang menekankan pembelajaran berpusat pada peserta didik. Buku Quantum Teaching karya DePorter diterjemahkan ke bahasa Indonesia dan menjadi rujukan populer di kalangan guru serta dosen. Beragam penelitian dan karya ilmiah di Indonesia membahas identifikasi gaya belajar siswa dan mahasiswa beserta implikasinya bagi pembelajaran."),
  ("h2", "1.9 Implikasi Gaya Belajar bagi Praktik Pembelajaran"),
  ("p", "Pemahaman tentang gaya belajar bermanfaat bagi pembelajar sekaligus pendidik. Bagi dosen dan guru, kesadaran akan keragaman gaya belajar mendorong penggunaan metode yang variatif. Pembelajaran multimodal yang melibatkan visual, auditorial, dan kinestetik secara seimbang dapat mengakomodasi berbagai gaya belajar di kelas. Sebagai contoh, dalam satu pertemuan kuliah, dosen dapat memadukan ceramah untuk auditorial, slide berdiagram untuk visual, serta studi kasus dan praktik untuk kinestetik."),
  ("p", "Bagi mahasiswa, pemahaman gaya belajar menjadi modal untuk belajar mandiri secara efektif. Mahasiswa tidak lagi terpaku pada satu cara belajar yang mungkin tidak sesuai, melainkan dapat mengeksplorasi berbagai strategi. Selain itu, mahasiswa dapat saling membantu teman belajarnya dengan memahami keberagaman gaya belajar dalam kelompok, sehingga kolaborasi antaranggota dengan gaya berbeda justru memperkaya proses belajar bersama."),
  ("box", {"kind": "ringkasan", "judul": "Ringkasan", "body": [
     ("p", "Gaya belajar adalah cara khas individu dalam menerima, mengolah, dan menyimpan informasi. Karakteristiknya meliputi keunikan, kestabilan, netralitas, dan kemampuan untuk dikembangkan. Teori yang banyak dirujuk adalah VAK/VARK dari Fleming, Multiple Intelligences dari Gardner, dan Experiential Learning dari Kolb; modul ini berfokus pada VAK. Gaya belajar dipengaruhi faktor biologis, lingkungan, pengalaman, sosial-budaya, serta motivasi. Pemahaman gaya belajar penting karena membantu memilih strategi yang efektif, meningkatkan motivasi, dan mendukung keberhasilan akademik."),
  ]}),
 ]})



# ===================== BAB II =====================
BAB.append({
 "no": "II", "judul": "MENGENAL TIGA TIPE GAYA BELAJAR (VAK)",
 "isi": [
  ("box", {"kind": "tujuan", "judul": "Tujuan Pembelajaran", "body": [
     ("p", "Setelah mempelajari bab ini, pembaca diharapkan mampu:"),
     ("nlist", [
        "Menjelaskan karakteristik gaya belajar visual, auditorial, dan kinestetik.",
        "Membedakan ketiga tipe gaya belajar berdasarkan ciri-cirinya.",
        "Mengidentifikasi gaya belajar diri sendiri melalui aktivitas penilaian mandiri.",
        "Menganalisis kelebihan dan tantangan setiap tipe gaya belajar.",
     ]),
  ]}),
  ("h2", "2.1 Model VAK dari Neil Fleming"),
  ("p", "Model VAK (Visual, Auditorial, Kinestetik) dikembangkan oleh Neil Fleming pada tahun 1987. Model ini mengelompokkan gaya belajar berdasarkan modalitas indra yang paling dominan digunakan seseorang dalam memproses informasi. Fleming kemudian mengembangkan model VARK dengan menambahkan satu modalitas, yaitu Read/Write atau membaca dan menulis. Namun dalam praktik pembelajaran sehari-hari, ketiga modalitas pertama merupakan yang paling sering digunakan (Fleming, 1987)."),
  ("p", "Perlu dipahami bahwa seseorang tidak selalu memiliki hanya satu gaya belajar. Banyak individu memiliki gaya belajar kombinasi atau multimodal, misalnya visual-kinestetik atau auditorial-visual. Karena itu, pemahaman tentang ketiga tipe ini membantu pembaca mengenali pola dominan dalam dirinya sekaligus mengembangkan gaya belajar lain sebagai pelengkap. Gambar 2.1 menyajikan ilustrasi ketiga tipe tersebut."),
  ("fig", {"no": "2.1", "judul": "Ilustrasi Tiga Tipe Gaya Belajar (VAK)", "file": "fig_2_1.png",
     "sumber": "Diolah penulis dari model VAK (Fleming, 1987); ilustrasi dibuat dengan bantuan AI (ChatGPT)."}),
  ("h2", "2.2 Gaya Belajar Visual"),
  ("p", "Gaya belajar visual adalah gaya belajar ketika seseorang lebih mudah menerima, memahami, dan mengingat informasi yang disajikan dalam bentuk gambar, diagram, warna, simbol, atau visualisasi lain. Pembelajar visual cenderung berpikir dalam gambar dan lebih responsif terhadap stimulus visual. Mereka lebih cepat memahami peta, grafik, bagan, dan ilustrasi dibandingkan penjelasan verbal yang panjang."),
  ("p", "Karakteristik pembelajar visual antara lain lebih mudah mengingat wajah dibandingkan nama, menyukai presentasi yang dilengkapi gambar atau slide berwarna, sering mencoret-coret saat berpikir, peka terhadap tata letak dan warna, serta lebih mudah mengingat informasi yang telah dituliskan. Kelebihannya adalah kemampuan mengorganisasi informasi secara spasial dan memahami hubungan antarkonsep. Tantangannya, pembelajar visual dapat kesulitan mengikuti penjelasan lisan yang panjang tanpa bantuan visualisasi."),
  ("h2", "2.3 Gaya Belajar Auditorial"),
  ("p", "Gaya belajar auditorial adalah gaya belajar ketika seseorang lebih mudah menerima dan memahami informasi melalui pendengaran. Pembelajar auditorial belajar optimal melalui mendengarkan ceramah, diskusi, podcast, atau penjelasan lisan. Mereka peka terhadap nada suara, ritme, dan intonasi, serta sering mengulang informasi secara verbal untuk mengingatnya."),
  ("p", "Karakteristik pembelajar auditorial antara lain lebih mudah mengingat nama dibandingkan wajah, senang berdiskusi dan bertanya, sering membaca dengan bersuara saat belajar, mudah terganggu oleh suara bising, serta mampu mengikuti petunjuk lisan dengan baik. Kelebihannya adalah kemampuan menyerap informasi dari ceramah dan diskusi secara cepat. Tantangannya, pembelajar auditorial dapat kesulitan memahami informasi yang hanya tersaji dalam bentuk teks panjang atau diagram tanpa penjelasan."),
  ("h2", "2.4 Gaya Belajar Kinestetik"),
  ("p", "Gaya belajar kinestetik adalah gaya belajar ketika seseorang belajar optimal melalui gerakan, sentuhan, dan praktik langsung. Pembelajar kinestetik sukar duduk diam dalam waktu lama; mereka belajar dengan cara melakukan, mencoba, dan mengalami. Mereka menyukai eksperimen, simulasi, bermain peran, dan kegiatan fisik."),
  ("p", "Karakteristik pembelajar kinestetik antara lain sulit duduk diam dalam waktu lama, belajar lebih baik saat tubuh bergerak, menyukai praktikum dan kegiatan langsung, sering menggunakan isyarat tubuh saat berbicara, serta terampil dalam kegiatan fisik. Kelebihannya adalah kemampuan memahami konsep melalui pengalaman langsung yang menghasilkan ingatan jangka panjang. Tantangannya, pembelajar kinestetik dapat kesulitan dalam lingkungan belajar yang sangat pasif seperti ceramah murni. Tabel 2.1 merangkum karakteristik ketiga tipe."),
  ("table", {"no": "2.1", "judul": "Karakteristik Tiga Tipe Gaya Belajar",
     "head": ["Aspek", "Visual", "Auditorial", "Kinestetik"],
     "rows": [
        ["Cara belajar", "Melihat gambar dan diagram", "Mendengarkan dan berdiskusi", "Praktik langsung"],
        ["Kekuatan", "Mengingat wajah dan peta", "Mengingat nama dan penjelasan", "Keterampilan fisik"],
        ["Tantangan", "Ceramah tanpa visual", "Gangguan suara bising", "Sulit duduk diam"],
        ["Media cocok", "Video dan peta pikiran", "Podcast dan rekaman", "Praktikum dan simulasi"],
     ], "sumber": "Diolah penulis dari Fleming (1987) dan Sukmawati & Nugraha (2021)."}),
  ("h2", "2.5 Cara Mengidentifikasi Gaya Belajar Diri"),
  ("p", "Untuk mengenali gaya belajar pribadi, terdapat beberapa cara yang dapat dilakukan. Cara yang paling valid adalah menggunakan instrumen kuesioner yang telah teruji, seperti VARK Questionnaire yang dikembangkan Fleming dan tersedia gratis secara daring. Selain itu, observasi terhadap kebiasaan belajar sehari-hari juga memberikan petunjuk yang kuat. Tabel 2.2 menyajikan panduan singkat untuk identifikasi awal."),
  ("table", {"no": "2.2", "judul": "Panduan Mengidentifikasi Gaya Belajar Diri",
     "head": ["Indikator", "Cenderung Visual", "Cenderung Auditorial", "Cenderung Kinestetik"],
     "rows": [
        ["Saat mengingat", "Membayangkan gambar", "Mengucapkan ulang", "Mengingat gerakan"],
        ["Saat belajar suka", "Melihat diagram", "Mendengar penjelasan", "Mencoba langsung"],
        ["Saat jenuh", "Melamun dan mencoret", "Berbicara sendiri", "Gelisah ingin bergerak"],
        ["Media favorit", "Video dan infografis", "Diskusi dan rekaman", "Alat peraga dan simulasi"],
     ], "sumber": "Diolah penulis dari karakteristik VAK (Fleming, 1987)."}),
  ("box", {"kind": "contoh", "judul": "Contoh atau Ilustrasi", "body": [
     ("p", "Perhatikan tiga mahasiswa berikut yang memiliki gaya belajar berbeda dan menghadapi tugas sama, yaitu memahami konsep fotosintesis."),
     ("blist", [
        "Rina (Visual): Rina membuka buku dan mencari diagram fotosintesis berwarna. Ia menggambar ulang skema kloroplas dan jalur reaksi dengan pensil warna. Setelah melihat gambarnya, ia langsung memahami urutan prosesnya.",
        "Bayu (Auditorial): Bayu lebih suka mendengarkan rekaman penjelasan dosen. Ia juga berdiskusi dengan teman sambil menjelaskan ulang konsepnya secara lisan. Dengan mendengar dan berbicara, Bayu cepat menguasai materi.",
        "Dewi (Kinestetik): Dewi melakukan praktikum sederhana di rumah dengan menanam biji pada dua kondisi cahaya berbeda. Dengan melihat langsung perbedaan pertumbuhan tanaman, Dewi memahami peran cahaya dalam fotosintesis.",
     ]),
  ]}),
  ("box", {"kind": "aktivitas", "judul": "Aktivitas 2.1: Tes Identifikasi Gaya Belajar", "body": [
     ("p", "Kerjakan VARK Questionnaire resmi melalui laman VARK-Learn (lihat Daftar Pustaka). Setelah selesai, catat skor Anda untuk masing-masing modalitas, lalu jawab pertanyaan berikut:"),
     ("nlist", [
        "Berapa skor Anda untuk setiap modalitas (V, A, R, K)?",
        "Modalitas mana yang dominan pada diri Anda?",
        "Apakah hasil tes sesuai dengan persepsi Anda selama ini? Jelaskan.",
        "Apa implikasi hasil tes ini terhadap cara belajar Anda ke depan?",
     ]),
  ]}),
  ("h2", "2.6 Gaya Belajar Multimodal"),
  ("p", "Sebagian besar individu tidak hanya memiliki satu gaya belajar, melainkan kombinasi dari dua gaya atau lebih. Kondisi ini dikenal sebagai gaya belajar multimodal. Dalam model VARK, Fleming mengidentifikasi bahwa sebagian besar orang memiliki profil multimodal. Sebagai contoh, seseorang dapat memperoleh skor tinggi pada visual dan kinestetik sekaligus, atau bahkan pada tiga modalitas sekaligus."),
  ("p", "Gaya belajar multimodal memiliki kelebihan tersendiri. Pertama, pembelajar multimodal lebih fleksibel menghadapi berbagai situasi belajar. Kedua, mereka dapat memanfaatkan kekuatan beberapa modalitas secara bersamaan sehingga pemahaman menjadi lebih mendalam. Ketiga, mereka lebih adaptif ketika harus belajar dalam kondisi yang tidak ideal. Tantangannya, pembelajar multimodal kadang bingung menentukan strategi mana yang paling efektif untuk situasi tertentu."),
  ("h2", "2.7 Tipe Read/Write dalam Model VARK"),
  ("p", "Selain tiga tipe VAK, Fleming menambahkan satu tipe dalam model VARK, yaitu Read/Write atau membaca dan menulis. Pembelajar tipe ini belajar optimal melalui teks tertulis, baik membaca buku dan artikel maupun menulis catatan dan esai. Mereka menyukai informasi yang disajikan dalam bentuk kata dan kalimat, serta gemar menggunakan kamus, ensiklopedia, dan dokumentasi tertulis sebagai sumber utama."),
  ("p", "Karakteristik pembelajar Read/Write antara lain menyukai membaca buku teks dan artikel, mengandalkan catatan tertulis yang rapi, senang menyusun ringkasan dan esai, serta lebih mudah memahami informasi yang tersaji dalam bentuk daftar dan poin. Walaupun model VAK lebih populer, pemahaman tentang tipe Read/Write melengkapi gambaran tentang keragaman gaya belajar. Gambar 2.2 dan Tabel 2.3 berikut merangkum keempat modalitas VARK."),
  ("fig", {"no": "2.2", "judul": "Empat Modalitas Gaya Belajar VARK", "file": "fig_2_2.png",
     "sumber": "Diolah penulis dari model VARK (Fleming, 1987); ilustrasi dibuat dengan bantuan AI (ChatGPT)."}),
  ("table", {"no": "2.3", "judul": "Perbandingan Empat Tipe Gaya Belajar VARK",
     "head": ["Tipe", "Cara Belajar Utama", "Media Favorit", "Contoh Aktivitas"],
     "rows": [
        ["Visual", "Melihat gambar dan diagram", "Infografis dan video", "Membuat peta pikiran"],
        ["Auditorial", "Mendengar dan berbicara", "Podcast dan diskusi", "Merekam penjelasan"],
        ["Read/Write", "Membaca dan menulis", "Buku dan catatan", "Menyusun ringkasan"],
        ["Kinestetik", "Bergerak dan praktik", "Alat peraga dan simulasi", "Eksperimen sederhana"],
     ], "sumber": "Diolah penulis dari model VARK (Fleming, 1987)."}),
  ("h2", "2.8 Studi Kasus: Gaya Belajar di Lingkungan Kampus"),
  ("p", "Untuk memperdalam pemahaman, mari menganalisis sebuah studi kasus. Bayangkan sebuah kelas dengan empat puluh mahasiswa yang mempelajari materi psikologi perkembangan. Dosen menyampaikan materi melalui kombinasi ceramah, slide berisi diagram tahap perkembangan, dan tugas presentasi kelompok. Hasil pengamatan menunjukkan bahwa mahasiswa yang paling antusias melihat slide dan menggambar diagram adalah pembelajar visual, mahasiswa yang sering bertanya dan berdiskusi adalah pembelajar auditorial, sedangkan mahasiswa yang bersemangat saat bermain peran dalam presentasi adalah pembelajar kinestetik."),
  ("p", "Kasus ini menggambarkan pentingnya pengakuan terhadap keragaman gaya belajar di kelas. Ketika dosen hanya menggunakan metode ceramah tanpa variasi, banyak mahasiswa yang sebenarnya berpotensi justru tertinggal. Sebaliknya, pengajaran multimodal memberi kesempatan bagi semua mahasiswa untuk belajar sesuai gaya belajarnya. Inilah pentingnya pendekatan pembelajaran yang inklusif dan variatif."),
  ("box", {"kind": "ringkasan", "judul": "Ringkasan", "body": [
     ("p", "Bab ini membahas tiga tipe gaya belajar menurut model VAK: visual yang belajar lewat penglihatan, auditorial yang belajar lewat pendengaran, dan kinestetik yang belajar lewat gerakan dan praktik. Setiap tipe memiliki karakteristik, kelebihan, dan tantangan tersendiri, dan tidak ada tipe yang lebih unggul. Model VARK menambahkan tipe Read/Write. Sebagian besar orang sebenarnya multimodal. Identifikasi gaya belajar dapat dilakukan melalui kuesioner VARK maupun observasi terhadap kebiasaan belajar sehari-hari."),
  ]}),
 ]})



# ===================== BAB III =====================
BAB.append({
 "no": "III", "judul": "STRATEGI BELAJAR EFEKTIF SESUAI GAYA BELAJAR",
 "isi": [
  ("box", {"kind": "tujuan", "judul": "Tujuan Pembelajaran", "body": [
     ("p", "Setelah mempelajari bab ini, pembaca diharapkan mampu:"),
     ("nlist", [
        "Menjelaskan berbagai strategi belajar yang sesuai untuk masing-masing gaya belajar.",
        "Memilih dan menerapkan strategi belajar yang tepat sesuai gaya belajar pribadi.",
        "Mengoptimalkan media dan lingkungan belajar agar mendukung gaya belajar.",
        "Menyusun rencana belajar pribadi yang adaptif terhadap gaya belajar.",
     ]),
  ]}),
  ("h2", "3.1 Pentingnya Strategi Belajar yang Sesuai"),
  ("p", "Strategi belajar adalah rencana atau cara yang digunakan seseorang untuk mencapai tujuan belajar. Menurut Schunk (2020), strategi belajar yang sesuai dengan karakteristik pembelajar akan meningkatkan efektivitas dan efisiensi proses belajar. Sebaliknya, ketidaksesuaian strategi dapat menimbulkan kebosanan, kesulitan memahami materi, dan penurunan motivasi. Karena itu, setelah mengenali gaya belajar pribadi, langkah penting berikutnya adalah memilih strategi yang tepat."),
  ("h2", "3.2 Strategi Belajar untuk Pembelajar Visual"),
  ("p", "Pembelajar visual akan belajar optimal jika strategi yang digunakan memanfaatkan elemen visual. Beberapa strategi yang direkomendasikan adalah sebagai berikut:"),
  ("blist", [
     "Gunakan peta pikiran. Hubungkan konsep dalam bentuk cabang bergambar dengan warna berbeda.",
     "Beri warna pada catatan. Manfaatkan stabilo atau pena berwarna untuk menandai informasi penting.",
     "Manfaatkan video pembelajaran. Tonton animasi atau tutorial visual dari sumber kredibel.",
     "Ubah teks menjadi diagram. Sajikan penjelasan naratif dalam bentuk bagan, tabel, atau infografis.",
     "Visualisasikan konsep abstrak. Bayangkan atau gambarkan konsep untuk memudahkan pemahaman.",
  ]),
  ("h2", "3.3 Strategi Belajar untuk Pembelajar Auditorial"),
  ("p", "Pembelajar auditorial akan belajar optimal dengan strategi yang melibatkan pendengaran dan verbalisasi. Strategi yang direkomendasikan antara lain:"),
  ("blist", [
     "Rekam dan dengarkan kuliah. Dengan izin, rekam kuliah lalu dengarkan ulang saat belajar mandiri.",
     "Bergabung dalam kelompok diskusi. Diskusi memungkinkan pertukaran ide secara lisan.",
     "Bacalah materi dengan bersuara. Membaca sambil bersuara membantu memproses informasi.",
     "Gunakan podcast edukasi. Dengarkan podcast tentang topik yang sedang dipelajari.",
     "Jelaskan ulang pada orang lain. Mengajarkan konsep secara lisan memperkuat pemahaman.",
  ]),
  ("h2", "3.4 Strategi Belajar untuk Pembelajar Kinestetik"),
  ("p", "Pembelajar kinestetik akan belajar optimal dengan strategi yang melibatkan gerakan dan praktik langsung. Beberapa strategi yang efektif adalah:"),
  ("blist", [
     "Lakukan praktikum dan eksperimen. Praktik langsung memberi pengalaman konkret yang mudah diingat.",
     "Gunakan bermain peran atau simulasi. Memerankan situasi membantu memahami konsep dalam konteks nyata.",
     "Belajar sambil bergerak. Berjalan atau berdiri saat menghafal dapat meningkatkan konsentrasi.",
     "Manfaatkan alat peraga dan model. Sentuhan dan manipulasi objek memperkuat pemahaman.",
     "Pecah belajar menjadi sesi singkat. Gunakan teknik Pomodoro dengan jeda gerakan ringan.",
  ]),
  ("table", {"no": "3.1", "judul": "Strategi Belajar Sesuai Gaya Belajar",
     "head": ["Gaya Belajar", "Strategi Utama", "Contoh Aktivitas"],
     "rows": [
        ["Visual", "Peta pikiran dan diagram", "Membuat mind map berwarna"],
        ["Auditorial", "Diskusi dan rekaman", "Merekam dan mendengar ulang"],
        ["Kinestetik", "Praktikum dan simulasi", "Eksperimen sederhana"],
        ["Read/Write", "Mencatat dan meringkas", "Menyusun outline materi"],
     ], "sumber": "Diolah penulis dari Schunk (2020) dan Widodo & Sari (2021)."}),
  ("h2", "3.5 Mengembangkan Gaya Belajar Kombinasi"),
  ("p", "Banyak mahasiswa memiliki gaya belajar kombinasi atau multimodal, misalnya dominan visual-kinestetik. Untuk pengembangannya, saran utamanya adalah memanfaatkan kekuatan masing-masing gaya secara saling melengkapi. Sebagai contoh, saat mempelajari konsep biologi, pembelajar visual-kinestetik dapat membuat diagram sekaligus melakukan praktikum. Pendekatan multimodal cenderung lebih kuat karena melibatkan banyak indra sekaligus (Slavin, 2015)."),
  ("h2", "3.6 Contoh Penerapan dalam Kehidupan Sehari-hari"),
  ("p", "Tabel 3.2 menyajikan contoh konkret penerapan strategi belajar sesuai gaya belajar pada situasi yang sering dihadapi mahasiswa."),
  ("table", {"no": "3.2", "judul": "Contoh Penerapan Strategi Belajar",
     "head": ["Situasi Belajar", "Visual", "Auditorial", "Kinestetik"],
     "rows": [
        ["Menghafal istilah", "Membuat kartu bergambar", "Mengucapkan berulang", "Menulis sambil bergerak"],
        ["Memahami konsep", "Menggambar diagram alur", "Mendengar dan berdiskusi", "Memeragakan langsung"],
        ["Persiapan ujian", "Membuat ringkasan visual", "Menjelaskan ke teman", "Mengerjakan soal praktik"],
        ["Kerja kelompok", "Menyiapkan slide", "Memimpin diskusi", "Membuat purwarupa atau demo"],
     ], "sumber": "Diolah penulis dari Yuliana & Anggraini (2021)."}),
  ("box", {"kind": "contoh", "judul": "Contoh atau Ilustrasi", "body": [
     ("p", "Misalkan Anda mahasiswa dengan gaya belajar visual yang harus menyiapkan presentasi tentang teori belajar. Alih-alih hanya membaca teks, Anda dapat membuat peta pikiran yang menghubungkan tokoh teori dengan konsepnya, mendesain slide dengan ikon dan warna konsisten, menambahkan video pendek ilustratif, lalu menyusun ringkasan akhir dalam bentuk infografis. Dengan strategi ini, Anda tidak hanya memahami materi, tetapi juga mampu menyajikannya secara menarik. Gambar 3.1 membantu Anda memilih strategi sesuai gaya dominan."),
  ]}),
  ("fig", {"no": "3.1", "judul": "Diagram Pemilihan Strategi Belajar", "file": "fig_3_1.png",
     "sumber": "Diolah penulis dari strategi belajar VAK (Schunk, 2020); ilustrasi dibuat dengan bantuan AI (ChatGPT)."}),
  ("box", {"kind": "aktivitas", "judul": "Aktivitas 3.1: Rencana Belajar Pribadi", "body": [
     ("p", "Berdasarkan hasil tes gaya belajar Anda pada Bab II, susunlah rencana belajar pribadi untuk satu minggu ke depan dengan format berikut:"),
     ("nlist", [
        "Tuliskan gaya belajar dominan Anda.",
        "Pilih tiga strategi belajar yang akan Anda coba.",
        "Susun jadwal mingguan dengan menerapkan strategi tersebut.",
        "Catat hasil dan perasaan Anda setelah satu minggu menerapkannya.",
        "Evaluasi strategi mana yang paling efektif untuk Anda.",
     ]),
  ]}),
  ("h2", "3.7 Strategi Belajar untuk Pembelajar Read/Write"),
  ("p", "Bagi pembelajar dengan gaya Read/Write, strategi yang efektif adalah memanfaatkan teks dan tulisan secara maksimal. Beberapa strategi yang direkomendasikan adalah membuat catatan terstruktur dengan format kerangka yang rapi, menuliskan ulang materi dengan kata-kata sendiri, memecah informasi kompleks menjadi daftar poin, membaca sumber pustaka tambahan untuk memperdalam pemahaman, serta menyusun esai ringkas untuk melatih kemampuan analisis."),
  ("h2", "3.8 Optimalisasi Lingkungan Belajar"),
  ("p", "Lingkungan belajar memegang peranan penting dalam menunjang keberhasilan belajar. Lingkungan yang sesuai dengan gaya belajar akan meningkatkan konsentrasi, motivasi, dan daya ingat. Sebaliknya, lingkungan yang tidak kondusif dapat mengganggu proses belajar sekalipun strategi yang dipakai sudah tepat. Setiap gaya belajar membutuhkan karakteristik lingkungan yang berbeda."),
  ("p", "Bagi pembelajar visual, lingkungan ideal adalah ruangan yang rapi, terang, dan memiliki papan atau dinding untuk menempelkan diagram. Bagi pembelajar auditorial, lingkungan yang tenang dan bebas kebisingan sangat penting, dan musik instrumental lembut terkadang membantu. Bagi pembelajar kinestetik, lingkungan yang fleksibel dan memungkinkan gerakan, seperti meja tinggi atau ruang yang lapang, akan sangat membantu. Pengaturan cahaya, suhu, dan ventilasi juga berpengaruh pada kenyamanan belajar secara umum."),
  ("table", {"no": "3.3", "judul": "Optimalisasi Lingkungan Belajar Sesuai Gaya Belajar",
     "head": ["Gaya Belajar", "Lingkungan yang Mendukung", "Sebaiknya Dihindari"],
     "rows": [
        ["Visual", "Ruang rapi dan terang, ada papan untuk diagram", "Tempat berantakan dan minim visual"],
        ["Auditorial", "Tempat tenang, boleh musik instrumental lembut", "Kebisingan dan gangguan suara"],
        ["Kinestetik", "Ruang lapang, leluasa bergerak, meja fleksibel", "Duduk diam dalam waktu lama"],
     ], "sumber": "Diolah penulis dari Schunk (2020)."}),
  ("h2", "3.9 Manajemen Waktu Belajar Sesuai Gaya Belajar"),
  ("p", "Manajemen waktu yang baik adalah kunci keberhasilan belajar, namun pendekatannya perlu disesuaikan dengan gaya belajar. Pembelajar visual dapat menggunakan kalender berwarna atau peta jadwal untuk merencanakan belajar. Pembelajar auditorial dapat memanfaatkan pengingat suara atau alarm. Pembelajar kinestetik dapat menerapkan teknik Pomodoro, yaitu belajar selama dua puluh lima menit lalu beristirahat bergerak selama lima menit, agar tetap fokus."),
  ("p", "Teknik Pomodoro dikembangkan oleh Francesco Cirillo pada akhir 1980-an dan terbukti membantu meningkatkan produktivitas. Teknik ini cocok bagi pembelajar kinestetik karena memberi kesempatan bergerak secara berkala. Bagi pembelajar visual, Pomodoro dapat dipadukan dengan daftar centang berwarna, sedangkan bagi pembelajar auditorial, jeda Pomodoro dapat diisi dengan mendengarkan musik atau podcast edukatif singkat."),
  ("h2", "3.10 Mengatasi Tantangan Belajar Sesuai Gaya Belajar"),
  ("p", "Setiap gaya belajar memiliki tantangan tersendiri. Pembelajar visual sering kesulitan dengan ceramah panjang tanpa visualisasi, sehingga solusinya adalah mencatat dalam bentuk sketsa atau peta pikiran selama ceramah. Pembelajar auditorial dapat terganggu oleh suara bising, sehingga solusinya adalah memakai penyumbat telinga peredam bising atau mencari sudut yang tenang. Pembelajar kinestetik dapat gelisah saat harus duduk lama, sehingga solusinya adalah berdiri sesekali atau memakai meja yang bisa dinaikturunkan."),
  ("p", "Selain tantangan internal, ada pula tantangan eksternal, seperti materi yang hanya tersedia dalam satu format. Buku teks tebal mungkin menyulitkan pembelajar auditorial, sehingga solusinya adalah mencari versi audio atau membaca dengan bersuara. Materi praktikum yang terbatas mungkin menyulitkan pembelajar kinestetik, sehingga solusinya adalah mencari simulasi virtual atau melakukan eksperimen sederhana di rumah. Kunci utamanya adalah kreativitas dalam mengadaptasi situasi belajar agar sesuai dengan gaya belajar pribadi."),
  ("h2", "3.11 Membangun Kebiasaan Belajar Berkelanjutan"),
  ("p", "Memahami gaya belajar hanyalah langkah awal. Yang lebih penting adalah membangun kebiasaan belajar yang berkelanjutan melalui pengulangan dan konsistensi. Sejumlah kajian menyebut bahwa pembentukan kebiasaan baru membutuhkan waktu yang bervariasi, umumnya beberapa pekan hingga beberapa bulan. Karena itu, mahasiswa perlu bersabar dan konsisten dalam menerapkan strategi belajar baru yang sesuai dengan gaya belajarnya."),
  ("p", "Beberapa kiat membangun kebiasaan belajar berkelanjutan adalah memulai dari target kecil yang realistis, mengaitkan belajar dengan aktivitas rutin yang sudah ada, memberi penghargaan sederhana setelah mencapai target, mencatat kemajuan dalam jurnal belajar, serta tidak terlalu keras pada diri sendiri saat gagal dan segera memulai lagi. Konsistensi lebih penting daripada kesempurnaan dalam membangun kebiasaan."),
  ("p", "Langkah membangun kebiasaan belajar tersebut dapat digambarkan sebagai satu rangkaian yang berkesinambungan, seperti tampak pada Gambar 3.2."),
  ("fig", {"no": "3.2", "judul": "Siklus Membangun Kebiasaan Belajar", "file": "fig_3_2.png",
     "sumber": "Diolah penulis dari prinsip pembentukan kebiasaan (Schunk, 2020); ilustrasi dibuat dengan bantuan AI (ChatGPT)."}),
  ("box", {"kind": "tips", "judul": "Tahukah Anda?", "body": [
     ("p", "Pembelajaran yang melibatkan lebih dari satu indra sekaligus, misalnya melihat diagram sambil menjelaskannya dengan suara, cenderung menghasilkan ingatan yang lebih kuat. Inilah sebabnya pendekatan multimodal sering dianjurkan, bahkan bagi orang yang sudah mengetahui gaya belajar dominannya."),
  ]}),
  ("box", {"kind": "ringkasan", "judul": "Ringkasan", "body": [
     ("p", "Bab ini membahas strategi belajar efektif sesuai gaya belajar. Pembelajar visual dapat memanfaatkan peta pikiran, warna, diagram, dan video. Pembelajar auditorial dapat merekam kuliah, berdiskusi, dan menjelaskan ulang materi. Pembelajar kinestetik dapat melakukan praktikum, simulasi, dan belajar sambil bergerak, sedangkan pembelajar Read/Write mengandalkan catatan dan ringkasan. Bagi pembelajar multimodal, kombinasi strategi memberi hasil paling optimal. Lingkungan belajar, manajemen waktu, dan kebiasaan yang konsisten turut menentukan keberhasilan. Yang terpenting adalah kesungguhan menerapkan strategi yang sesuai."),
  ]}),
 ]})



# ===================== REFLEKSI =====================
REFLEKSI = {
 "intro": "Refleksi merupakan bagian penting dari proses belajar. Melalui refleksi, pembaca diajak mengevaluasi pemahaman, mengaitkan materi dengan pengalaman pribadi, serta merencanakan tindakan nyata untuk meningkatkan cara belajar. Jawablah pertanyaan refleksi berikut secara jujur dan mendalam pada buku catatan atau jurnal belajar Anda.",
 "pertanyaan": [
    "Apa pengetahuan atau wawasan baru yang Anda peroleh setelah mempelajari modul ini?",
    "Materi apa yang paling menarik atau paling bermanfaat bagi Anda? Mengapa?",
    "Bagaimana Anda dapat menerapkan materi yang telah dipelajari dalam kehidupan sehari-hari sebagai mahasiswa?",
    "Kesulitan apa yang Anda alami selama mempelajari modul ini?",
    "Apa yang akan Anda lakukan untuk meningkatkan pemahaman atau keterampilan terkait gaya belajar?",
    "Setelah mempelajari modul ini, perubahan positif apa yang ingin Anda lakukan dalam kebiasaan belajar?",
 ],
 "tabel_judul": "Tabel Refleksi Pribadi",
 "tabel_intro": "Gunakan tabel berikut untuk mencatat hasil refleksi pribadi Anda secara terstruktur. Tuliskan jawaban pada kolom yang tersedia.",
 "tabel": {
    "head": ["Pertanyaan Refleksi", "Jawaban Saya"],
    "rows": [
       ["Hal terpenting yang saya pelajari dari modul ini", ""],
       ["Materi yang paling bermanfaat bagi saya", ""],
       ["Materi yang masih perlu saya pelajari lebih dalam", ""],
       ["Cara saya menerapkan materi ini dalam belajar", ""],
       ["Target yang ingin saya capai setelah mempelajari modul ini", ""],
    ],
 },
}

# ===================== EVALUASI =====================
EVALUASI = {
 "intro": "Evaluasi ini bertujuan mengukur pemahaman Anda terhadap seluruh materi dalam modul Gaya Belajar. Kerjakan soal berikut secara mandiri tanpa melihat materi. Setelah selesai, gunakan kunci jawaban di bagian akhir untuk memeriksa hasil pekerjaan Anda.",
 "pg": [
    ("Gaya belajar merupakan cara khas individu dalam", [
        "Menghafal materi tanpa pemahaman",
        "Menerima, mengolah, dan menyimpan informasi",
        "Meniru kebiasaan belajar orang lain",
        "Menghindari kegiatan belajar"], 1),
    ("Model VAK dikembangkan oleh", [
        "Howard Gardner", "David Kolb", "Neil Fleming", "Robert Slavin"], 2),
    ("Pembelajar yang paling mudah memahami informasi melalui gambar dan diagram memiliki gaya belajar", [
        "Visual", "Auditorial", "Kinestetik", "Read/Write"], 0),
    ("Berikut adalah karakteristik pembelajar auditorial, kecuali", [
        "Senang berdiskusi", "Mudah mengingat nama", "Suka mencoret-coret saat berpikir", "Membaca dengan bersuara"], 2),
    ("Strategi belajar yang paling sesuai untuk pembelajar kinestetik adalah", [
        "Membuat peta pikiran berwarna", "Mendengarkan podcast", "Melakukan praktikum dan simulasi", "Membaca buku teks"], 2),
    ("Kondisi seseorang yang memiliki kombinasi dua gaya belajar atau lebih disebut", [
        "Unimodal", "Multimodal", "Bimodal tunggal", "Nonmodal"], 1),
    ("Pernyataan yang benar tentang gaya belajar adalah", [
        "Ada gaya belajar yang mutlak lebih unggul",
        "Gaya belajar bersifat tetap dan tidak dapat berubah",
        "Gaya belajar bersifat netral dan dapat dikembangkan",
        "Gaya belajar tidak memengaruhi cara belajar"], 2),
    ("Instrumen yang umum digunakan untuk mengidentifikasi gaya belajar adalah", [
        "VARK Questionnaire", "Tes Wartegg", "Skala Likert umum", "Tes Buta Warna"], 0),
    ("Teknik Pomodoro paling membantu pembelajar kinestetik karena", [
        "Melarang istirahat sama sekali",
        "Memberi kesempatan bergerak secara berkala",
        "Hanya mengandalkan bacaan", "Menghapus jadwal belajar"], 1),
    ("Pendekatan pembelajaran yang dianggap efektif bagi hampir semua pembelajar adalah", [
        "Ceramah satu arah", "Pendekatan multimodal", "Menghafal tanpa konteks", "Belajar tanpa istirahat"], 1),
 ],
 "bs": [
    ("Setiap individu memiliki gaya belajar yang sama dengan orang lain.", False),
    ("Gaya belajar bersifat netral, tidak ada yang lebih unggul secara mutlak.", True),
    ("Sebagian besar orang memiliki gaya belajar kombinasi atau multimodal.", True),
    ("Pembelajar visual kesulitan memahami diagram dan gambar.", False),
    ("Strategi belajar yang sesuai gaya belajar dapat meningkatkan efektivitas belajar.", True),
 ],
 "esai": [
    "Jelaskan perbedaan antara gaya belajar visual, auditorial, dan kinestetik.",
    "Mengapa pemahaman tentang gaya belajar penting bagi mahasiswa?",
    "Sebutkan dua strategi belajar untuk masing-masing tipe gaya belajar.",
    "Bagaimana cara Anda mengidentifikasi gaya belajar diri sendiri?",
    "Jelaskan satu contoh penerapan strategi belajar sesuai gaya belajar dalam kehidupan sehari-hari.",
 ],
 "pedoman_esai": "Jawaban esai bersifat terbuka. Pedoman penskoran: setiap nomor bernilai 0 sampai 20 dengan kriteria ketepatan konsep, kelengkapan, dan kejelasan penjelasan. Skor maksimal bagian esai adalah 100.",
}

# ===================== DAFTAR PUSTAKA (APA 7th, alfabetis) =====================
# tuple: (teks_lurus, url)  -> bagian judul akan dimiringkan oleh renderer berdasar pola
DAFTAR_PUSTAKA = [
 ("DePorter, B., Reardon, M., & Singer-Nourie, S. (2014). ", "Quantum teaching: Mempraktikkan quantum learning di ruang-ruang kelas", ". Kaifa.", "https://books.google.co.id/books/about/Quantum_Teaching.html?id=ZVPZfWWGin4C"),
 ("Fleming, N. D. (1987). ", "VARK: A guide to learning styles", ". VARK-Learn.", "https://vark-learn.com/"),
 ("Fleming, N. D. (2019). ", "The VARK questionnaire: How do I learn best?", " VARK-Learn.", "https://vark-learn.com/the-vark-questionnaire/"),
 ("Pritchard, A. (2017). ", "Ways of learning: Learning theories for the classroom", " (4th ed.). Routledge.", "https://www.routledge.com/Ways-of-Learning-Learning-Theories-for-the-Classroom/Pritchard/p/book/9781138207943"),
 ("Schunk, D. H. (2020). ", "Learning theories: An educational perspective", " (8th ed.). Pearson.", "https://www.pearson.com/en-us/subject-catalog/p/learning-theories-an-educational-perspective/P200000001801"),
 ("Slavin, R. E. (2015). ", "Educational psychology: Theory and practice", " (11th ed.). Pearson.", "https://archive.org/details/educationalpsych0010slav"),
 ("Sukmawati, D., & Nugraha, A. (2021). Identifikasi gaya belajar visual, auditorial, dan kinestetik mahasiswa semester awal. ", "Jurnal Pedagogik", ", 9(2), 45-58.", "https://journal.umpr.ac.id/index.php/pedagogik/article/download/1876/1810/9225"),
 ("Widodo, T., & Sari, N. (2021). Analisis gaya belajar VAK siswa berprestasi pada mata pelajaran IPA. ", "Jurnal Basicedu", ", 5(3), 2310-2322.", "https://jbasic.org/index.php/basicedu/article/view/10462"),
 ("Yuliana, R., & Anggraini, S. (2021). Hubungan minat belajar dengan gaya belajar VAK siswa sekolah dasar. ", "Jurnal Edukatif", ", 5(4), 2015-2025.", "https://edukatif.org/index.php/edukatif/article/view/5186"),
]

# ===================== PENUTUP =====================
PENUTUP = [
 "Demikian modul pembelajaran tentang Gaya Belajar yang membahas konsep dasar gaya belajar, tiga tipe utama yaitu visual, auditorial, dan kinestetik, serta strategi belajar efektif yang sesuai dengan masing-masing gaya. Pemahaman tentang gaya belajar merupakan bekal penting bagi mahasiswa untuk mengembangkan kebiasaan belajar yang adaptif, efektif, dan menyenangkan.",
 "Setiap individu adalah pembelajar yang unik. Tidak ada resep tunggal yang berlaku untuk semua orang. Kunci keberhasilan belajar terletak pada kemampuan mengenali gaya belajar diri sendiri, memilih strategi yang sesuai, dan terus mengembangkan cara belajar agar lebih optimal. Dengan kesadaran ini, mahasiswa diharapkan mampu mengelola proses belajarnya secara mandiri dan bertanggung jawab.",
 "Penulis berharap modul ini menjadi titik awal bagi pembaca untuk terus bereksplorasi dan menemukan cara belajar terbaik bagi dirinya. Belajar adalah proses sepanjang hayat, dan memahami cara diri belajar merupakan investasi yang sangat berharga. Selamat belajar, jangan ragu mencoba strategi baru, dan jadilah pembelajar yang aktif serta reflektif.",
]
MOTTO = "Kenali dirimu, kenali cara belajarmu, maka engkau akan menjadi pembelajar sejati."
