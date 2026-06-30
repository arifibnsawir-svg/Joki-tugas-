# -*- coding: utf-8 -*-
# Konten Mini Book PKN - Lidya Ellen Febriasalsa (Buku #4).
# DNA: dialogis/tanya-jawab kritis, kotak tanya-jawab + tabel ringkas, nomor halaman tengah atas,
# daftar isi tanpa leader (indentasi rapi), daftar pustaka MLA. Humanized, beda dari Buku 1/2/3.
# Blok: ('p',teks) | ('h2',teks) | ('tanya',{'judul','pairs':[(t,j),...]}) | ('tabel',{'judul','head','rows'})

PENULIS = "Lidya Ellen Febriasalsa"

KATA_PENGANTAR = [
 "Buku kecil ini ditulis dengan satu cara berpikir yang sederhana, yaitu bertanya lalu mencari jawaban. Penulis percaya bahwa banyak hal dalam Pendidikan Kewarganegaraan baru benar-benar dimengerti ketika kita berani mengajukan pertanyaan, bukan sekadar menghafal rumusan yang sudah jadi.",
 "Karena itu, pembahasan dalam naskah ini sering dibuka dengan pertanyaan yang mungkin juga muncul di benak pembaca. Dari pertanyaan itu, uraian bergerak menuju jawaban yang ditata serapi mungkin, dilengkapi kotak tanya-jawab dan tabel ringkas agar gagasan yang rumit menjadi lebih mudah ditelusuri.",
 "Latar penulis sebagai mahasiswa Bimbingan dan Konseling pada Universitas Indraprasta PGRI menumbuhkan kebiasaan untuk menyimak lebih dahulu sebelum menanggapi. Kebiasaan itu ikut mewarnai naskah ini, sehingga pembaca diajak berdialog, bukan hanya menerima penjelasan secara searah.",
 "Ucapan terima kasih penulis sampaikan kepada Ibu Ajeng Radyati S.H., M.H. selaku dosen pengampu, serta kepada keluarga dan teman-teman yang selalu mendukung. Penulis sadar naskah ini belum sempurna, sehingga setiap tanya dan saran dari pembaca akan disambut dengan senang hati.",
 "Jakarta, 2026",
 "Penulis,",
 "Lidya Ellen Febriasalsa",
]

# Daftar Pustaka format MLA (Author. *Judul*. Tahun. Situs, URL. Diakses tanggal.), urut alfabetis.
# Tiap entri: ('teks sebelum judul', 'judul yang dimiringkan', 'sisa teks termasuk tautan')
DAFTAR_PUSTAKA = [
 ("Komisi Pemberantasan Korupsi. ", "Anti-Corruption Learning Center: Materi Pembelajaran Antikorupsi", ". 2024. ACLC KPK, https://aclc.kpk.go.id/materi-pembelajaran. Diakses 28 Juni 2026."),
 ("Perserikatan Bangsa-Bangsa. ", "Universal Declaration of Human Rights", ". 1948. United Nations, https://www.un.org/en/about-us/universal-declaration-of-human-rights. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Dasar Negara Republik Indonesia Tahun 1945", ". 1945. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Dasar_Negara_Republik_Indonesia_Tahun_1945. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 12 Tahun 2006 tentang Kewarganegaraan Republik Indonesia", ". 2006. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2006. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 12 Tahun 2012 tentang Pendidikan Tinggi", ". 2012. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2012. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 2 Tahun 2002 tentang Kepolisian Negara Republik Indonesia", ". 2002. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_2_Tahun_2002. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional", ". 2003. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_20_Tahun_2003. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 24 Tahun 2009 tentang Bendera, Bahasa, dan Lambang Negara, serta Lagu Kebangsaan", ". 2009. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_24_Tahun_2009. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 31 Tahun 1999 tentang Pemberantasan Tindak Pidana Korupsi", ". 1999. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_31_Tahun_1999. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 39 Tahun 1999 tentang Hak Asasi Manusia", ". 1999. Wikisource, https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_39_Tahun_1999. Diakses 28 Juni 2026."),
 ("Republik Indonesia. ", "Undang-Undang Nomor 48 Tahun 2009 tentang Kekuasaan Kehakiman", ". 2009. Wikimedia Commons, https://commons.wikimedia.org/wiki/File:Undang-Undang_Republik_Indonesia_Nomor_48_Tahun_2009.pdf. Diakses 28 Juni 2026."),
]

BAB = []


# ===================== BAB 1 =====================
BAB.append({
 "no": "1",
 "judul": "HAKIKAT PENDIDIKAN KEWARGANEGARAAN",
 "isi": [
  ("p", "Mengapa mahasiswa teknik, ekonomi, atau konseling tetap diwajibkan mengikuti Pendidikan Kewarganegaraan? Pertanyaan ini sering terdengar pada awal perkuliahan, dan justru dari sanalah bab ini berangkat. Daripada langsung menyodorkan definisi, ada baiknya kita telusuri dulu apa yang sebenarnya ingin dicapai oleh mata kuliah ini."),

  ("h2", "Apa Sebenarnya Pendidikan Kewarganegaraan Itu"),
  ("p", "Bila disederhanakan, Pendidikan Kewarganegaraan adalah upaya membekali mahasiswa agar mampu hidup sebagai warga negara yang berpikir jernih, bersikap adil, dan mau ikut bertanggung jawab atas kehidupan bersama. Bahasannya memang menyentuh negara, hukum, dan demokrasi, tetapi tujuan akhirnya selalu kembali pada sikap dan tindakan sehari-hari."),
  ("p", "Lalu, apakah ia sekadar pelajaran teori? Tentu tidak. Ketika seorang mahasiswa memilih berdiskusi alih-alih menyebar fitnah, atau menolak menyontek meski ada kesempatan, di situ pelajaran ini sedang bekerja. Maknanya hidup dalam keputusan kecil, bukan berhenti pada catatan kuliah."),

  ("tanya", {
    "judul": "Tanya Jawab: Salah Paham yang Sering Muncul",
    "pairs": [
      ("Bukankah materi ini hanya mengulang pelajaran sekolah?", "Topiknya memang mirip, tetapi kedalamannya berbeda. Di perguruan tinggi, mahasiswa diajak menganalisis dan memperdebatkan, bukan sekadar menghafal."),
      ("Apa gunanya bagi jurusan yang tidak berkaitan dengan politik?", "Setiap lulusan akan hidup di tengah masyarakat dan dunia kerja yang menuntut kejujuran, kerja sama, serta sikap menghargai perbedaan. Semua itu dilatih di sini."),
    ],
  }),

  ("h2", "Di Atas Dasar Hukum Apa Mata Kuliah Ini Berdiri"),
  ("p", "Sebagian orang mengira mata kuliah ini hanya kebijakan masing-masing kampus. Anggapan itu keliru. Kedudukannya ditopang oleh sejumlah aturan yang menjadikannya bagian resmi dari sistem pendidikan nasional."),
  ("tabel", {"judul": "Tabel 1.1 Pijakan hukum Pendidikan Kewarganegaraan",
            "head": ["Sumber", "Inti Pengaturan"],
            "rows": [
              ["Pancasila", "Sumber nilai dan arah moral kehidupan berbangsa"],
              ["UUD NRI Tahun 1945", "Amanat mencerdaskan kehidupan bangsa"],
              ["UU No. 20 Tahun 2003", "Pendidikan kewarganegaraan wajib dalam kurikulum"],
              ["UU No. 12 Tahun 2012", "Mata kuliah wajib pada jenjang perguruan tinggi"],
            ]}),
  ("p", "Dengan pijakan sekuat itu, jelas bahwa mata kuliah ini bukan tempelan. Ia diniatkan agar lulusan tidak hanya pandai di bidangnya, tetapi juga matang sebagai anggota masyarakat."),

  ("h2", "Apa yang Ingin Dicapai dan Bagaimana Caranya"),
  ("p", "Sasaran utamanya adalah membentuk mahasiswa yang berpikiran terbuka, berwatak jujur, dan bersedia terlibat dalam urusan bersama. Untuk sampai ke sana, pembelajarannya tidak cukup lewat ceramah, melainkan lewat diskusi, studi kasus, dan latihan menimbang persoalan dari banyak sisi."),
  ("p", "Bagaimana mengukur keberhasilannya? Tanda paling sederhana adalah perubahan sikap. Mahasiswa yang dulu acuh mulai peduli, yang dulu cepat menghakimi mulai mau mendengar. Perubahan semacam itu lebih berarti daripada sekadar nilai ujian yang tinggi."),

  ("h2", "Tantangan Apa yang Dihadapi di Zaman Sekarang"),
  ("p", "Zaman ini membawa banjir informasi yang datang lebih cepat daripada kemampuan kita memeriksanya. Di sinilah Pendidikan Kewarganegaraan diuji. Mampukah ia membuat mahasiswa berhenti sejenak untuk berpikir sebelum membagikan sesuatu, atau sebelum ikut menghakimi orang lain di dunia maya?"),
  ("p", "Tantangan lain adalah sikap masa bodoh. Ketika seseorang merasa urusan bangsa bukan urusannya, kepedulian pelan-pelan menghilang. Mata kuliah ini berusaha melawan kecenderungan itu dengan menumbuhkan kesadaran bahwa setiap orang memikul bagian, sekecil apa pun perannya."),

  ("h2", "Benang Merah Bab"),
  ("p", "Jadi, untuk apa Pendidikan Kewarganegaraan? Jawabannya adalah untuk menyiapkan warga negara yang berpikir kritis, berwatak baik, dan mau terlibat. Landasannya kuat, mulai dari Pancasila hingga undang-undang tentang pendidikan tinggi."),
  ("p", "Inti yang perlu dibawa dari bab ini sederhana, yaitu bahwa kewarganegaraan bukan status di atas kertas, melainkan peran yang dijalani setiap hari. Pertanyaan demi pertanyaan dalam bab-bab berikutnya akan terus mengasah peran itu."),
 ]
})


# ===================== BAB 2 =====================
BAB.append({
 "no": "2",
 "judul": "IDENTITAS NASIONAL",
 "isi": [
  ("p", "Apa yang membuat seseorang merasa sebagai orang Indonesia, padahal ia mungkin belum pernah bertemu sebagian besar penduduk negeri ini? Pertanyaan itu membuka pembahasan tentang identitas nasional, yaitu hal-hal yang membuat kita merasa menjadi satu bangsa meski tersebar di ribuan pulau."),

  ("h2", "Apa yang Dimaksud Identitas Nasional"),
  ("p", "Identitas nasional adalah kumpulan ciri yang membuat sebuah bangsa dikenali dan berbeda dari bangsa lain. Sebagiannya kasat mata, seperti bendera dan lagu kebangsaan. Sebagian lagi tidak terlihat, seperti nilai bersama, kenangan sejarah, dan cara memandang hidup."),
  ("p", "Apakah identitas itu sesuatu yang langsung jadi? Tidak. Ia tumbuh melalui pengalaman panjang, dari masa perjuangan sampai kebiasaan sehari-hari. Bangsa ini terus membentuk dirinya, dan setiap generasi ikut menambah maknanya."),

  ("h2", "Dari Mana Identitas Nasional Terbentuk"),
  ("p", "Bila ditanya unsur pembentuknya, jawabannya bukan satu hal tunggal, melainkan beberapa yang saling menopang. Tabel berikut meringkasnya agar lebih mudah dilihat."),
  ("tabel", {"judul": "Tabel 2.1 Unsur pembentuk identitas nasional",
            "head": ["Unsur", "Perannya"],
            "rows": [
              ["Sejarah perjuangan", "Kenangan bersama yang menumbuhkan rasa sebangsa"],
              ["Bahasa Indonesia", "Alat yang mempertemukan penutur ratusan bahasa daerah"],
              ["Kebudayaan", "Kekayaan yang memperlihatkan kemampuan merangkul perbedaan"],
              ["Lambang negara", "Penanda jati diri yang diatur UU No. 24 Tahun 2009"],
            ]}),
  ("p", "Di ruang kuliah, unsur-unsur itu terasa nyata. Mahasiswa dari berbagai daerah berbicara dalam bahasa Indonesia, lalu saling mengenalkan tradisi masing-masing. Tanpa disadari, mereka sedang merawat identitas bangsa."),

  ("tanya", {
    "judul": "Tanya Jawab: Pancasila dan Jati Diri Bangsa",
    "pairs": [
      ("Mengapa Pancasila disebut pengikat identitas?", "Karena nilai di dalamnya, dari ketuhanan sampai keadilan sosial, menjadi titik temu yang diterima oleh masyarakat yang sangat beragam."),
      ("Apakah Pancasila masih relevan saat banyak ketimpangan?", "Justru relevan. Yang perlu dikoreksi bukan dasarnya, melainkan pelaksanaannya yang belum sepenuhnya setia pada nilai itu."),
    ],
  }),

  ("h2", "Apa yang Mengancam Identitas Kita Hari Ini"),
  ("p", "Globalisasi membuat budaya luar masuk dengan sangat mudah lewat layar gawai. Apakah itu buruk? Tidak selalu. Persoalan baru muncul ketika seseorang justru malu pada budayanya sendiri dan menganggap segala yang dari luar lebih bernilai."),
  ("p", "Ada pula tantangan berupa lunturnya minat pada sejarah. Bila generasi muda tidak lagi mengenal perjalanan bangsanya, alasan untuk menjaga persatuan menjadi kabur. Padahal sulit mencintai sesuatu yang tidak kita kenal."),

  ("h2", "Bagaimana Mahasiswa Bisa Merawatnya"),
  ("p", "Apakah merawat identitas harus lewat hal besar? Tidak. Menggunakan bahasa Indonesia dengan baik, memperkenalkan budaya daerah lewat karya digital, dan menolak ujaran yang merendahkan kelompok lain sudah merupakan kontribusi nyata. Kepekaan terhadap keragaman ini juga menjadi bekal berharga bagi siapa pun yang kelak bekerja mendampingi orang lain."),

  ("h2", "Benang Merah Bab"),
  ("p", "Identitas nasional adalah jawaban atas pertanyaan tentang apa yang menyatukan kita. Ia dibangun dari sejarah, bahasa, budaya, dan lambang negara, lalu diikat oleh Pancasila."),
  ("p", "Ancaman terbesarnya bukan budaya luar itu sendiri, melainkan hilangnya kebanggaan pada milik sendiri. Maka merawat identitas sebenarnya dimulai dari sikap sederhana yang kita pilih setiap hari."),
 ]
})



# ===================== BAB 3 =====================
BAB.append({
 "no": "3",
 "judul": "INTEGRASI NASIONAL",
 "isi": [
  ("p", "Jika bangsa ini terdiri atas ratusan suku dengan bahasa dan adat yang berlainan, mengapa ia tidak tercerai-berai? Pertanyaan inilah yang menuntun kita pada gagasan integrasi nasional, yakni kemampuan menyatukan banyak perbedaan menjadi satu bangsa yang tetap utuh."),

  ("h2", "Apa Arti Menyatu dalam Konteks Bangsa"),
  ("p", "Menyatu di sini tidak berarti menyeragamkan. Tidak ada niat membuat semua orang berpikir, berpakaian, atau beribadah dengan cara yang sama. Yang dimaksud adalah menjaga agar perbedaan tetap berjalan beriringan tanpa berubah menjadi pertikaian."),
  ("p", "Apakah persatuan semacam itu mudah dijaga? Tidak. Ia menuntut kesediaan untuk saling memahami dan mendahulukan kepentingan bersama pada saat yang tepat. Tanpa kesediaan itu, perbedaan kecil pun bisa membesar menjadi konflik."),

  ("h2", "Apa yang Mempererat dan Apa yang Merenggangkan"),
  ("p", "Untuk menjawabnya, kita perlu mengenali dua sisi sekaligus, yaitu hal yang merekatkan dan hal yang berpotensi memecah. Keduanya disajikan berdampingan agar mudah dibandingkan."),
  ("tabel", {"judul": "Tabel 3.1 Perekat dan pemicu renggang dalam integrasi",
            "head": ["Yang Mempererat", "Yang Merenggangkan"],
            "rows": [
              ["Rasa senasib dan cita-cita bersama", "Jurang ekonomi antardaerah"],
              ["Bahasa Indonesia dan nilai Pancasila", "Sentimen suku dan agama yang ditunggangi"],
              ["Gotong royong dalam keseharian", "Berita palsu yang sengaja diembuskan"],
            ]}),
  ("p", "Dari tabel itu terlihat bahwa banyak pemicu renggang sebenarnya bisa dicegah. Berita palsu, misalnya, kehilangan daya rusaknya bila masyarakat terbiasa memeriksa kebenaran sebelum ikut menyebarkan."),

  ("tanya", {
    "judul": "Tanya Jawab: Toleransi dan Batasnya",
    "pairs": [
      ("Apakah toleransi berarti menerima segala hal?", "Tidak. Toleransi berarti menghormati perbedaan, tetapi tetap menolak tindakan yang melanggar hukum atau merugikan orang lain."),
      ("Kalau begitu, di mana batasnya?", "Batasnya ada pada hak orang lain dan aturan bersama. Selama tidak melukai keduanya, perbedaan layak dihormati."),
    ],
  }),

  ("h2", "Apa Peran Nyata Mahasiswa"),
  ("p", "Pertanyaan yang lebih penting bukan apakah mahasiswa bisa berperan, melainkan dari mana ia mulai. Jawabannya ada pada hal yang dekat, seperti berteman lintas daerah tanpa pamrih, aktif dalam organisasi yang terbuka, dan menahan diri dari menyebar kabar yang memanaskan suasana."),
  ("p", "Di luar kampus, mahasiswa dapat ikut kegiatan pengabdian dan mengajak masyarakat lebih bijak bermedia. Kritik terhadap keadaan bangsa tetap boleh disuarakan, asalkan dengan cara yang santun dan berdasar, bukan dengan caci maki."),

  ("h2", "Benang Merah Bab"),
  ("p", "Integrasi nasional menjawab teka-teki mengapa keberagaman tidak membuat bangsa ini pecah. Kuncinya ada pada perekat berupa rasa senasib, bahasa, dan nilai bersama, serta kewaspadaan terhadap pemicu renggang seperti ketimpangan dan kabar bohong."),
  ("p", "Yang perlu diingat, toleransi yang sehat selalu punya batas, dan mahasiswa dapat merawat persatuan mulai dari pergaulan sehari-hari yang terbuka dan jujur."),
 ]
})


# ===================== BAB 4 =====================
BAB.append({
 "no": "4",
 "judul": "NEGARA DAN KONSTITUSI",
 "isi": [
  ("p", "Seandainya sebuah negara berjalan tanpa aturan dasar, apa yang akan terjadi? Kemungkinan besar muncul kekacauan, karena tidak ada pegangan bersama tentang siapa boleh melakukan apa. Dari kebutuhan akan pegangan itulah lahir konstitusi, dan bab ini menelusuri hubungan antara negara dan konstitusi."),

  ("h2", "Apa Itu Konstitusi dan Mengapa Penting"),
  ("p", "Konstitusi adalah hukum dasar yang menjadi pegangan tertinggi dalam menjalankan negara. Ia menata hubungan antara penguasa dan rakyat, mengatur kerja antarlembaga, serta menetapkan hak dan kewajiban masing-masing pihak. Karena posisinya paling tinggi, semua aturan lain harus tunduk padanya."),
  ("p", "Konstitusi tertulis yang dianut Indonesia adalah Undang-Undang Dasar Negara Republik Indonesia Tahun 1945. Selain naskah resmi itu, ada pula kebiasaan ketatanegaraan yang dijalankan secara taat asas walau tidak tertulis, dan kebiasaan itu turut menjaga jalannya pemerintahan."),

  ("h2", "Apa Saja Tugas yang Diemban Konstitusi"),
  ("p", "Bila ditanya untuk apa konstitusi ada, jawabannya bisa diringkas ke dalam beberapa tugas pokok yang membuat negara berjalan tertib dan adil."),
  ("tabel", {"judul": "Tabel 4.1 Tugas pokok konstitusi",
            "head": ["Tugas", "Penjelasan Singkat"],
            "rows": [
              ["Membatasi kekuasaan", "Mencegah kewenangan menumpuk pada satu pihak"],
              ["Menata antarlembaga", "Mengatur kerja lembaga agar tidak berbenturan"],
              ["Melindungi warga", "Menjaga hak rakyat dari perlakuan sewenang-wenang"],
              ["Menjadi acuan tertinggi", "Mempersatukan semua aturan di bawahnya"],
            ]}),
  ("p", "Terbelahnya kekuasaan menjadi cabang eksekutif, legislatif, dan yudikatif adalah bentuk konkret dari fungsi pembatasan yang dimaksud. Setiap cabang punya kewenangan sendiri sekaligus saling mengawasi."),

  ("tanya", {
    "judul": "Tanya Jawab: Perjalanan UUD 1945",
    "pairs": [
      ("Kapan UUD 1945 disahkan?", "Pada 18 Agustus 1945, sehari setelah proklamasi, oleh Panitia Persiapan Kemerdekaan Indonesia."),
      ("Apakah naskahnya tidak pernah berubah?", "Pernah. Pada masa reformasi tahun 1999 sampai 2002, naskah ini empat kali diubah, antara lain untuk menegaskan hak asasi dan membatasi masa jabatan presiden."),
    ],
  }),

  ("h2", "Siapa Saja Lembaga yang Menjalankan Negara"),
  ("p", "Pertanyaan ini penting agar mahasiswa tahu ke mana arah pertanggungjawaban kekuasaan. Secara umum, lembaga negara dikelompokkan menurut cabang kekuasaannya, dengan tugas yang sudah ditetapkan."),
  ("tabel", {"judul": "Tabel 4.2 Cabang kekuasaan dan lembaganya",
            "head": ["Cabang", "Lembaga Utama"],
            "rows": [
              ["Legislatif", "Majelis Permusyawaratan Rakyat, Dewan Perwakilan Rakyat, Dewan Perwakilan Daerah"],
              ["Eksekutif", "Presiden dan Wakil Presiden"],
              ["Yudikatif", "Mahkamah Agung, Mahkamah Konstitusi, Komisi Yudisial"],
            ]}),
  ("p", "Pengelompokan ini bukan sekadar urusan tata negara. Ia adalah cara agar tidak ada satu lembaga pun yang berkuasa tanpa kendali, sehingga keseimbangan tetap terjaga."),

  ("h2", "Mengapa Konstitusi Harus Dijunjung Paling Tinggi"),
  ("p", "Apa jadinya bila ada pihak yang merasa boleh berada di atas konstitusi? Hak warga akan mudah dilanggar dan kekuasaan gampang disalahgunakan. Karena itu prinsip menjunjung konstitusi sebagai yang tertinggi menjadi penjaga utama negara hukum."),
  ("p", "Mahasiswa dapat ikut menjaganya dengan cara yang tampak sepele namun bermakna, seperti membaca aturan sebelum berkomentar, menilai kebijakan dengan kepala dingin, dan menaati aturan kecil di kampus. Kesetiaan pada aturan kecil melatih kesetiaan pada aturan yang lebih besar."),

  ("h2", "Benang Merah Bab"),
  ("p", "Negara membutuhkan konstitusi sebagaimana sebuah perjalanan membutuhkan peta. Konstitusi membatasi kekuasaan, menata antarlembaga, dan melindungi warga, dengan Undang-Undang Dasar Tahun 1945 sebagai naskah tertingginya."),
  ("p", "Lembaga negara dibagi agar saling mengawasi, dan prinsip menjunjung konstitusi memastikan tidak ada yang kebal aturan. Mahasiswa turut menjaganya lewat ketaatan pada hal-hal kecil."),
 ]
})



# ===================== BAB 5 =====================
BAB.append({
 "no": "5",
 "judul": "HAK DAN KEWAJIBAN WARGA NEGARA",
 "isi": [
  ("p", "Mana yang lebih dulu, hak atau kewajiban? Pertanyaan ini sering memancing perdebatan. Sebagian orang sibuk menuntut hak, sebagian lain lupa bahwa hak selalu berpasangan dengan kewajiban. Bab ini menelusuri keduanya, termasuk hak asasi manusia yang menjadi bagian penting di dalamnya."),

  ("h2", "Apa Beda Hak dan Kewajiban Warga Negara"),
  ("p", "Hak warga negara adalah kewenangan yang dimiliki seseorang karena ia menjadi anggota sebuah negara, dan kewenangan itu dijamin oleh hukum. Sementara kewajiban adalah hal yang harus dijalankan sebagai imbalan dari keanggotaan tersebut, seperti menaati aturan dan menghormati hak sesama."),
  ("p", "Mungkinkah menuntut hak tanpa menjalankan kewajiban? Secara logika tidak, sebab keduanya seperti dua sisi mata uang. Warga yang hanya menuntut tanpa memberi akan membuat kehidupan bersama timpang."),

  ("h2", "Hak Apa Saja yang Dimiliki Warga"),
  ("p", "Hak warga negara menyebar ke banyak bidang kehidupan. Mengenalinya membantu kita menuntut yang memang menjadi hak sekaligus menghormati hak orang lain."),
  ("tabel", {"judul": "Tabel 5.1 Hak warga negara menurut bidangnya",
            "head": ["Bidang", "Contoh Hak"],
            "rows": [
              ["Politik", "Memilih dan dipilih dalam pemilihan"],
              ["Ekonomi", "Bekerja, berusaha, dan memiliki harta"],
              ["Sosial budaya", "Memperoleh pendidikan dan mengembangkan budaya"],
              ["Sipil", "Berpendapat, beragama, dan berkumpul"],
            ]}),
  ("p", "Karena bidang-bidang itu saling berkaitan, terabaikannya satu hak sering menyeret hak yang lain. Hak pendidikan yang terhambat, misalnya, dapat mempersempit peluang ekonomi di kemudian hari."),

  ("h2", "Bagaimana Kedudukan Hak Asasi Manusia"),
  ("p", "Apa bedanya hak asasi dengan hak warga negara? Hak asasi melekat pada manusia sejak lahir, tanpa memandang suku, agama, atau kewarganegaraan. Maka dari itu, warga negara asing yang sedang menetap di Indonesia sekalipun tetap menyandang hak asasi yang wajib dihargai."),
  ("p", "Indonesia menegaskan perlindungan ini lewat Undang-Undang Dasar Tahun 1945 dan Undang-Undang Nomor 39 Tahun 1999, serta membentuk Komisi Nasional Hak Asasi Manusia. Di tingkat internasional, asasnya dirumuskan lewat Deklarasi Universal Hak Asasi Manusia yang disahkan Perserikatan Bangsa-Bangsa pada 1948."),

  ("tanya", {
    "judul": "Tanya Jawab: Hak Asasi di Dunia Maya",
    "pairs": [
      ("Apakah menghina orang di media sosial termasuk pelanggaran hak asasi?", "Bisa jadi ya. Ujaran kebencian, perundungan, dan penyebaran data pribadi tanpa izin termasuk melanggar hak orang lain, meski terjadi di ruang digital."),
      ("Bukankah saya bebas berpendapat?", "Bebas, tetapi kebebasan Anda berhenti di titik hak orang lain dimulai. Pendapat boleh tajam, asalkan tidak merampas martabat orang lain."),
    ],
  }),

  ("h2", "Mengapa Tanggung Jawab Menjadi Penghubung"),
  ("p", "Hak dan kewajiban sebaiknya dibaca dalam bingkai yang lebih luas, yaitu tanggung jawab. Apa maksudnya? Tanggung jawab adalah kesadaran menjalankan apa yang semestinya, bukan karena takut sanksi, melainkan karena paham itu benar."),
  ("p", "Bagi mahasiswa yang kelak banyak berhubungan dengan orang lain, kesadaran ini sangat berharga. Menghargai martabat setiap orang, bersikap adil, dan menjaga kepercayaan adalah cerminan langsung dari nilai hak asasi yang dipelajari di bab ini."),

  ("h2", "Benang Merah Bab"),
  ("p", "Pertanyaan tentang mana yang lebih dulu antara hak dan kewajiban sebenarnya keliru, sebab keduanya berjalan beriringan. Jangkauan hak asasi lebih lebar, dan jaminannya hadir dalam Undang-Undang Dasar Tahun 1945 bersama Undang-Undang Nomor 39 Tahun 1999."),
  ("p", "Di era digital, hak dan kewajiban bertemu dalam etika bermedia sosial. Semuanya bermuara pada tanggung jawab, yaitu kesadaran untuk melakukan yang benar walau tidak ada yang mengawasi."),
 ]
})


# ===================== BAB 6 =====================
BAB.append({
 "no": "6",
 "judul": "PENEGAKAN HUKUM YANG BERKEADILAN",
 "isi": [
  ("p", "Apa gunanya hukum yang bagus di atas kertas bila penegakannya pilih kasih? Pertanyaan tajam ini menjadi titik tolak bab ini. Hukum baru terasa adil ketika ditegakkan dengan jujur, dan di situlah letak ujian sebenarnya."),

  ("h2", "Apa Maksud Negara Hukum"),
  ("p", "Negara hukum adalah negara yang dijalankan berdasarkan hukum, bukan berdasarkan kehendak pribadi penguasa. Artinya, setiap langkah pemerintah harus punya dasar hukum, dan tidak ada orang yang boleh bertindak seenaknya. Indonesia menegaskan hal ini melalui Pasal 1 ayat (3) Undang-Undang Dasar Tahun 1945."),
  ("p", "Apakah hukum hanya berlaku bagi rakyat? Tentu tidak. Dalam negara hukum, pemerintah pun terikat aturan yang sama. Bila penguasa keliru, rakyat berhak menempuh jalur sah untuk menuntut keadilan."),

  ("h2", "Prinsip Apa yang Menopang Negara Hukum"),
  ("p", "Negara hukum tidak berdiri di atas satu tiang, melainkan beberapa prinsip yang saling melengkapi. Tabel berikut merangkumnya."),
  ("tabel", {"judul": "Tabel 6.1 Prinsip penopang negara hukum",
            "head": ["Prinsip", "Makna Ringkas"],
            "rows": [
              ["Kesetaraan di mata hukum", "Semua orang berkedudukan sama tanpa kecuali"],
              ["Jaminan hak warga", "Negara wajib melindungi hak dasar rakyat"],
              ["Pembatasan kekuasaan", "Kekuasaan diawasi agar tidak terpusat"],
              ["Peradilan merdeka", "Hakim memutus berdasar hukum, bukan tekanan"],
            ]}),
  ("p", "Bila salah satu prinsip ini diabaikan, keadilan menjadi timpang. Kesetaraan kehilangan arti tanpa jaminan hak, dan jaminan hak rapuh bila kekuasaan tidak dibatasi."),

  ("tanya", {
    "judul": "Tanya Jawab: Sistem Peradilan Kita",
    "pairs": [
      ("Apa dasar hukum kekuasaan kehakiman?", "Diatur dalam Undang-Undang Nomor 48 Tahun 2009, sedangkan peran kepolisian diatur lewat Undang-Undang Nomor 2 Tahun 2002."),
      ("Pengadilan apa saja yang ada di Indonesia?", "Ada peradilan umum, agama, militer, dan tata usaha negara, ditambah Mahkamah Konstitusi yang menguji undang-undang terhadap UUD 1945."),
    ],
  }),

  ("h2", "Mengapa Penegakan Hukum Masih Tersendat"),
  ("p", "Kalau aturannya sudah ada, mengapa keadilan belum selalu terwujud? Salah satu sebabnya adalah akses yang tidak merata. Tidak semua orang mampu membayar pendampingan hukum, dan jarak ke pengadilan kadang menjadi penghalang tersendiri."),
  ("p", "Sebab lain adalah lemahnya integritas sebagian aparat. Begitu hukum terasa galak kepada rakyat kecil namun lunak kepada yang berkuasa, kepercayaan publik perlahan luruh. Maka penegakan hukum membutuhkan aparat yang jujur sekaligus warga yang mau ikut mengawasi."),

  ("h2", "Bagaimana Budaya Hukum Dibangun"),
  ("p", "Budaya hukum adalah kebiasaan masyarakat dalam memahami dan menaati hukum. Ia tidak lahir dari hukuman semata, melainkan dari pembiasaan. Di kampus, budaya ini tumbuh lewat sikap menaati aturan akademik, menolak menyontek, dan menyelesaikan perselisihan dengan cara baik."),
  ("p", "Mahasiswa dapat menyuarakan keadilan tanpa main hakim sendiri, misalnya melalui tulisan, dialog, atau laporan ke pihak berwenang. Kepekaan terhadap hukum ini berguna pula bagi siapa pun yang kelak mendampingi orang lain, agar tidak gegabah menyalahkan korban."),

  ("h2", "Benang Merah Bab"),
  ("p", "Hukum yang baik belum cukup bila penegakannya pilih kasih. Negara hukum bertumpu pada kesetaraan, jaminan hak, pembatasan kekuasaan, dan peradilan yang merdeka, sebagaimana ditegaskan dalam Pasal 1 ayat (3) Undang-Undang Dasar Tahun 1945."),
  ("p", "Hambatan utamanya berupa akses yang timpang dan integritas yang lemah. Budaya hukum yang sehat serta keterlibatan mahasiswa menjadi penjaga agar keadilan benar-benar terasa."),
 ]
})



# ===================== BAB 7 =====================
BAB.append({
 "no": "7",
 "judul": "GEOPOLITIK DAN GEOSTRATEGI",
 "isi": [
  ("p", "Bagaimana sebuah negara yang wilayahnya terpisah-pisah oleh lautan bisa tetap merasa sebagai satu kesatuan? Jawaban atas pertanyaan ini terletak pada cara pandang yang disebut wawasan nusantara, dan bab ini membahasnya bersama ketahanan nasional."),

  ("h2", "Apa Itu Wawasan Nusantara"),
  ("p", "Wawasan nusantara dapat dimaknai sebagai sikap bangsa Indonesia dalam menatap diri dan sekelilingnya, bertumpu pada Pancasila dan Undang-Undang Dasar Tahun 1945, dengan mengedepankan keutuhan wilayah. Sebagai negara kepulauan terbesar di dunia, Indonesia menyimpan ribuan pulau yang sekaligus menjadi kekayaan dan tantangan."),
  ("p", "Dengan kacamata ini, seantero wilayah dari Sabang hingga Merauke dipahami sebagai satu kesatuan yang pantang dipecah. Lautan di antara pulau bukan dianggap pemisah, justru jembatan yang merangkai kehidupan bangsa."),

  ("h2", "Apa Saja Unsur dan Kedudukannya"),
  ("p", "Bila ditanya dari apa wawasan nusantara tersusun, jawabannya mencakup beberapa unsur yang saling terkait, dan kedudukannya terasa dalam berbagai bidang kehidupan."),
  ("tabel", {"judul": "Tabel 7.1 Unsur wawasan nusantara",
            "head": ["Unsur", "Cakupan"],
            "rows": [
              ["Wilayah", "Darat, laut, dan udara dalam batas kedaulatan"],
              ["Bangsa", "Ratusan suku yang direkatkan sejarah dan cita-cita bersama"],
              ["Budaya", "Kekayaan daerah yang hidup berdampingan"],
            ]}),
  ("p", "Dalam pembangunan, cara pandang ini menuntut pemerataan agar kemajuan tidak menumpuk di kota besar. Daerah perbatasan dan pulau kecil perlu diperhatikan supaya setiap warga merasa menjadi bagian dari bangsa."),

  ("h2", "Bagaimana Ketahanan Nasional Dijaga"),
  ("p", "Geostrategi pada hakikatnya adalah rancangan langkah bangsa yang memperhitungkan posisi geografis dan aneka aspek kehidupan untuk meraih tujuan bernegara. Perwujudan utamanya berupa ketahanan nasional, yaitu keuletan bangsa dalam mempertahankan diri dan kesatuannya ketika menghadapi berbagai ujian. Dasar pertahanannya antara lain tertuang dalam Undang-Undang Nomor 3 Tahun 2002."),
  ("p", "Apakah ketahanan nasional hanya soal militer? Tidak. Ia mencakup banyak dimensi yang harus dibangun seimbang, mulai dari ideologi, politik, ekonomi, sosial budaya, hingga pertahanan dan keamanan. Negara yang kuat ekonominya tetapi rapuh secara sosial tetap mudah goyah."),

  ("tanya", {
    "judul": "Tanya Jawab: Ancaman Zaman Sekarang",
    "pairs": [
      ("Apa ancaman ketahanan nasional yang paling terasa kini?", "Disinformasi digital. Berita palsu dapat memecah masyarakat lebih cepat daripada ancaman fisik."),
      ("Apa yang bisa dilakukan mahasiswa?", "Menjadi penyaring informasi, menjaga persatuan dalam keragaman, dan menghargai budaya daerah lewat sikap sehari-hari."),
    ],
  }),

  ("h2", "Mengapa Laut dan Pemerataan Penting"),
  ("p", "Mengingat lautan mendominasi peta Indonesia, jiwa sebagai bangsa pelaut menjadi unsur penting dalam wawasan nusantara. Laut bukan sekadar batas, melainkan sumber pangan, energi, dan jalur dagang yang harus dijaga."),
  ("p", "Pemerataan pembangunan pun bukan semata urusan ekonomi. Ketika setiap daerah merasa diperhatikan, ikatan terhadap bangsa menguat, dan ketahanan nasional ikut kokoh dari dalam. Pada lingkup pribadi, ketahanan juga menyangkut kekuatan mental, dan di sinilah kemampuan menolong orang lain bertahan turut menyumbang bagi bangsa."),

  ("h2", "Benang Merah Bab"),
  ("p", "Wawasan nusantara menjawab teka-teki mengapa wilayah yang terpisah lautan tetap satu, yaitu karena cara pandang yang menempatkan seluruh wilayah sebagai satu tubuh. Geostrategi mewujud dalam ketahanan nasional yang mencakup banyak dimensi."),
  ("p", "Ancaman terbesar saat ini berwujud disinformasi digital. Mahasiswa mengambil peran merawat persatuan, memilah informasi, dan turut memperhatikan kekuatan mental orang-orang di sekelilingnya."),
 ]
})


# ===================== BAB 8 =====================
BAB.append({
 "no": "8",
 "judul": "ANTI KORUPSI",
 "isi": [
  ("p", "Apakah korupsi selalu berupa pencurian uang bermiliar oleh pejabat tinggi? Jika kita berpikir begitu, kita akan luput melihat benihnya yang sering tumbuh dari hal kecil di sekitar kita. Bab pamungkas ini mengajak membedah korupsi sebagai soal integritas yang sebenarnya akrab dengan keseharian mahasiswa."),

  ("h2", "Sebenarnya Apa Itu Korupsi"),
  ("p", "Secara ringkas, korupsi adalah tindakan memanfaatkan jabatan atau kepercayaan untuk kepentingan diri sendiri maupun golongan, yang pada ujungnya membuat masyarakat luas dirugikan. Bentuknya tidak selalu berupa perampasan uang secara kasatmata, karena suap, pemberian terselubung, dan penyelewengan wewenang pun tergolong di dalamnya."),
  ("p", "Mengapa korupsi disebut berbahaya melebihi pelanggaran biasa? Sebab apabila didiamkan, pelan-pelan masyarakat akan memandang ketidakjujuran sebagai sesuatu yang biasa. Bila sudah sampai di titik itu, masalahnya bergeser dari urusan hukum menjadi urusan kebiasaan, dan justru itulah yang jauh lebih sukar dibasmi."),

  ("h2", "Apa Dasar Hukum untuk Melawannya"),
  ("p", "Dalam upaya membasmi korupsi, Indonesia memiliki beberapa landasan hukum yang tegas serta lembaga yang khusus menanganinya. Tabel berikut meringkasnya."),
  ("tabel", {"judul": "Tabel 8.1 Pijakan pemberantasan korupsi",
            "head": ["Pijakan", "Peran"],
            "rows": [
              ["UU No. 31 Tahun 1999", "Dasar pemberantasan tindak pidana korupsi"],
              ["UU No. 20 Tahun 2001", "Penguatan atas undang-undang sebelumnya"],
              ["Komisi Pemberantasan Korupsi", "Lembaga pencegahan sekaligus penindakan"],
            ]}),
  ("p", "Selain menindak, Komisi Pemberantasan Korupsi juga menyiapkan bahan ajar antikorupsi yang terbuka untuk umum. Hal ini menegaskan bahwa melawan korupsi tidak cukup dengan hukuman, sebab penyadaran perlu ditanam sejak dini."),

  ("tanya", {
    "judul": "Tanya Jawab: Korupsi di Sekitar Kita",
    "pairs": [
      ("Apakah memberi uang pelicin agar urusan cepat termasuk korupsi?", "Ya, itu termasuk benih korupsi. Kebiasaan kecil semacam ini yang justru memuluskan praktik yang lebih besar."),
      ("Apa bentuk korupsi yang sering tidak disadari mahasiswa?", "Menyontek, menitip absen, dan mengakali laporan kegiatan. Semuanya melatih sikap tidak jujur yang berbahaya jika dibiarkan."),
    ],
  }),

  ("h2", "Nilai Apa yang Perlu Ditanam"),
  ("p", "Jantung pendidikan antikorupsi ada pada penanaman nilai, bukan pada hafalan pasal semata. Nilai-nilai inilah yang membuat seseorang menolak korupsi bahkan sebelum niat itu sempat tumbuh."),
  ("tabel", {"judul": "Tabel 8.2 Nilai antikorupsi dan wujudnya di kampus",
            "head": ["Nilai", "Wujud Nyata"],
            "rows": [
              ["Kejujuran", "Mengerjakan ujian dan tugas tanpa kecurangan"],
              ["Tanggung jawab", "Memikul amanah tanpa menyelewengkannya"],
              ["Keberanian", "Berani menampik ajakan curang serta melaporkan kejanggalan"],
              ["Kesederhanaan", "Hidup secukupnya tanpa berlebih-lebihan"],
            ]}),
  ("p", "Nilai-nilai itu tampak sederhana, tetapi justru di sanalah ujian sesungguhnya. Hasrat kaya secara instan dan gaya hidup berlebihan kerap menjadi pintu masuk perilaku korup, sehingga membiasakan nilai baik sejak kuliah terasa mendesak."),

  ("h2", "Apa Peran Kampus dan Mahasiswa"),
  ("p", "Kampus memikul tugas menumbuhkan sikap antikorupsi, tidak hanya lewat materi, tetapi juga lewat budaya akademik dan tata kelolanya. Kampus yang menutup mata terhadap penjiplakan sebenarnya sedang memupuk bibit korupsi."),
  ("p", "Lewat pilihan kecil setiap hari, mahasiswa bisa memelopori kejujuran, misalnya menggarap tugas tanpa curang dan berani menolak ajakan berbuat tidak benar. Bagi siapa pun yang kelak dipercaya mendampingi orang lain, integritas menjadi syarat utama, sebab pekerjaan semacam itu bertumpu pada kepercayaan."),

  ("h2", "Benang Merah Bab"),
  ("p", "Korupsi bukan hanya soal angka besar, melainkan soal amanah yang diselewengkan, dan benihnya kerap muncul dari hal kecil yang dianggap lumrah. Ketentuan utamanya bersandar pada Undang-Undang Nomor 31 Tahun 1999 yang kemudian diperkuat Undang-Undang Nomor 20 Tahun 2001."),
  ("p", "Menangkalnya berarti memupuk kejujuran, tanggung jawab, serta keberanian mulai dari hal-hal sehari-hari. Sebagai penutup buku ini, bahasan antikorupsi merangkai semangat seluruh bab, yaitu menyiapkan mahasiswa menjadi warga negara yang jujur, paham hukum, dan siap berbuat bagi bangsa."),
 ]
})


# ===================== Penomoran sub-bab otomatis X.Y =====================
import re as _re

def _renumber():
    for bab in BAB:
        no = bab["no"]; n = 0; new = []
        for blk in bab["isi"]:
            if blk[0] == "h2":
                n += 1
                t2 = _re.sub(r"^\s*\d+\.\d+\s+", "", blk[1])
                new.append(("h2", "%s.%d %s" % (no, n, t2)))
            else:
                new.append(blk)
        bab["isi"] = new

_renumber()



# ===================== PENDALAMAN TAHAP 1 (disisipkan sebelum "Benang Merah") =====================
def _splice(extra):
    for bab in BAB:
        no = bab["no"]; isi = bab["isi"]
        if no in extra:
            idx = next((i for i, blk in enumerate(isi) if blk[0] == "h2" and "Benang Merah" in blk[1]), len(isi))
            bab["isi"] = isi[:idx] + extra[no] + isi[idx:]
    _renumber()

EXTRA1 = {
 "1": [
  ("h2", "Apa Bedanya Warga yang Cerdas dan Sekadar Pintar"),
  ("p", "Banyak orang pintar secara akademik, tetapi apakah semuanya bijak dalam bersikap? Tidak selalu. Di sinilah Pendidikan Kewarganegaraan membedakan diri. Ia tidak berhenti pada kepandaian berpikir, melainkan menambahkan kepekaan untuk menggunakan kepandaian itu demi kebaikan bersama."),
  ("p", "Warga yang cerdas tahu kapan harus bersuara dan kapan harus mendengar. Ia mampu menimbang dampak tindakannya terhadap orang lain. Kepintaran tanpa kepekaan justru bisa berbahaya, karena ilmu yang besar di tangan yang tidak peduli dapat menyakiti banyak orang."),
  ("h2", "Bagaimana Mata Kuliah Ini Ikut Membentuk Karakter"),
  ("p", "Bisakah karakter dibentuk lewat satu mata kuliah? Tidak secara instan, tetapi prosesnya dimulai di sini. Ketika mahasiswa berlatih berargumen dengan sopan, menghargai pendapat berbeda, dan jujur dalam tugas, ia sedang menempa watak yang akan terbawa hingga dunia kerja."),
  ("p", "Karakter tidak tumbuh dari hafalan, melainkan dari kebiasaan. Itulah sebabnya ruang kelas Pendidikan Kewarganegaraan sebaiknya menjadi tempat berlatih, bukan sekadar tempat mencatat. Watak jujur dan bertanggung jawab yang terasah di kampus akan menjadi modal sosial yang berharga kelak."),
  ("h2", "Mengapa Berpikir Kritis Begitu Ditekankan"),
  ("p", "Apa untungnya berpikir kritis di tengah derasnya informasi? Keuntungannya besar. Orang yang kritis tidak mudah ditipu kabar bohong, tidak gampang dihasut, dan mampu memilah mana yang benar dari mana yang sekadar ramai. Kemampuan ini menjadi tameng di zaman ketika kebohongan bisa menyebar secepat kebenaran."),
  ("p", "Berpikir kritis bukan berarti suka membantah. Ia berarti terbiasa bertanya, memeriksa sumber, dan menahan diri sebelum menyimpulkan. Sikap inilah yang ingin ditumbuhkan, agar mahasiswa menjadi penimbang yang tenang, bukan penyebar keributan."),
 ],
 "2": [
  ("h2", "Mengapa Sejarah Penting bagi Jati Diri"),
  ("p", "Apakah mungkin mencintai sesuatu yang tidak kita kenal? Sulit. Begitu pula dengan bangsa. Tanpa mengenal sejarah perjuangan, alasan untuk menjaga persatuan terasa kabur. Sejarah memberi kita konteks, yaitu pemahaman tentang betapa mahal harga kemerdekaan yang kini dinikmati."),
  ("p", "Mengenang peristiwa seperti Kebangkitan Nasional dan Sumpah Pemuda bukan berarti hidup di masa lalu. Justru dari sana kita belajar bahwa persatuan adalah hasil kerja keras lintas suku dan daerah, bukan pemberian yang turun begitu saja."),
  ("h2", "Bagaimana Generasi Digital Menyikapi Budaya Luar"),
  ("p", "Apakah menyukai budaya luar berarti tidak nasionalis? Tidak juga. Persoalannya bukan pada menyukai, melainkan pada kehilangan keseimbangan. Generasi digital boleh menyerap hal baik dari mana saja, asalkan tidak sampai memandang rendah budayanya sendiri."),
  ("p", "Menariknya, teknologi yang sama bisa dipakai untuk memperkenalkan budaya bangsa ke panggung dunia. Banyak anak muda kini mengemas tarian, musik, dan kuliner daerah menjadi konten yang ditonton lintas negara. Di tangan yang tepat, dunia digital menjadi sarana memperkuat jati diri."),
  ("h2", "Apa Itu Bela Negara dalam Bentuk Sederhana"),
  ("p", "Haruskah bela negara selalu berarti mengangkat senjata? Tidak. Bela negara juga berarti menjaga jati diri bangsa dari hal yang dapat memecah belah, seperti hasutan dan kabar bohong. Bentuknya bisa sangat sederhana dan dekat dengan keseharian."),
  ("p", "Bagi mahasiswa, bela negara dapat berupa belajar sungguh-sungguh, berprestasi, dan menyebarkan sikap positif di ruang digital. Menjaga nama baik bangsa lewat karya yang bermutu adalah bentuk bela negara yang bisa dilakukan siapa saja."),
 ],
 "3": [
  ("h2", "Bagaimana Gotong Royong Merawat Persatuan"),
  ("p", "Mengapa gotong royong masih relevan di zaman serba mandiri ini? Karena banyak persoalan terlalu berat bila dipikul sendiri. Saat mahasiswa bahu-membahu menyiapkan acara atau membantu teman yang kesulitan, mereka sedang membuktikan bahwa kebersamaan meringankan beban."),
  ("p", "Gotong royong mengajarkan bahwa kepentingan bersama kadang perlu didahulukan. Nilai ini sederhana, tetapi justru menjadi perekat yang menahan masyarakat agar tidak terpecah oleh sikap mementingkan diri sendiri."),
  ("h2", "Apa Peran Pendidikan dalam Menyatukan Bangsa"),
  ("p", "Bisakah bangsa bersatu tanpa pendidikan yang merawat kesadaran itu? Sulit. Lewat pendidikan, generasi muda diperkenalkan pada sejarah, nilai Pancasila, dan bahaya perpecahan. Dari sanalah tumbuh pemahaman bahwa perbedaan tidak harus berujung permusuhan."),
  ("p", "Pendidikan juga melatih cara berkomunikasi yang sehat. Mahasiswa yang terbiasa berdiskusi tanpa saling menjatuhkan akan membawa kebiasaan itu ke masyarakat. Dengan begitu, pendidikan tidak hanya mencerdaskan, tetapi juga merekatkan."),
  ("h2", "Mengapa Semangat Sumpah Pemuda Masih Diperlukan"),
  ("p", "Apa pelajaran dari para pemuda tahun 1928 bagi kita hari ini? Mereka rela mengesampingkan perbedaan suku dan daerah demi satu tekad bersama. Semangat itu mengingatkan bahwa persatuan menuntut kerelaan, bukan sekadar slogan."),
  ("p", "Generasi mahasiswa sekarang bisa melanjutkan semangat itu lewat langkah konkret, misalnya menjalin pertemanan lintas daerah dan menjauhi sikap menutup diri. Dengan cara itu, Sumpah Pemuda tidak berhenti sebagai catatan sejarah, melainkan tetap hidup dalam keseharian."),
 ],
 "4": [
  ("h2", "Mengapa Kekuasaan Justru Perlu Dibatasi"),
  ("p", "Bukankah pemimpin yang kuat itu baik? Bisa baik, tetapi sejarah mengajarkan bahwa kekuasaan tanpa batas cenderung disalahgunakan. Karena itu konstitusi menetapkan batas kewenangan, agar tidak ada pihak yang merasa boleh berbuat apa saja."),
  ("p", "Pembatasan ini diwujudkan lewat pembagian tugas dan mekanisme saling mengawasi antarlembaga. Bagi rakyat, batas itu sekaligus menjadi pelindung, karena kebijakan yang melanggar hak dapat digugat melalui jalur yang sah."),
  ("h2", "Bagaimana Aturan Negara Tersusun Berjenjang"),
  ("p", "Apakah semua aturan punya kedudukan yang sama? Tidak. Aturan tersusun bertingkat, dengan Undang-Undang Dasar Tahun 1945 di puncaknya, lalu undang-undang, hingga peraturan di tingkat daerah. Ketentuan yang berada di tingkat bawah dilarang berseberangan dengan yang di atasnya."),
  ("p", "Susunan berjenjang ini menjaga ketertiban agar tidak terjadi tumpang tindih. Bila ada aturan yang dinilai menyimpang dari konstitusi, tersedia jalur pengujian lewat lembaga peradilan, sehingga semua tetap berpijak pada satu sumber acuan."),
  ("h2", "Apa Makna Konstitusi bagi Warga Biasa"),
  ("p", "Apakah konstitusi hanya urusan pejabat? Sama sekali tidak. Konstitusi menjamin hak warga atas keadilan, pendidikan, rasa aman, dan kebebasan menyampaikan pendapat. Jaminan ini membuat warga tidak boleh diperlakukan semena-mena."),
  ("p", "Sayangnya, banyak orang tidak menyadari bahwa haknya dilindungi konstitusi. Padahal dengan memahaminya, seseorang lebih siap membela diri lewat cara yang sah ketika menghadapi ketidakadilan."),
 ],
 "5": [
  ("h2", "Apa Saja Kewajiban yang Sering Terlupakan"),
  ("p", "Kita fasih menyebut hak, tetapi seberapa sering kita ingat kewajiban? Menaati aturan, menghormati hak orang lain, menjaga lingkungan, dan ikut menjaga ketertiban adalah kewajiban yang kerap dianggap sepele. Padahal tanpa itu, hak orang lain ikut terganggu."),
  ("p", "Menjalankan kewajiban bukanlah beban, melainkan sumbangan bagi kehidupan bersama. Ketika warga sadar akan kewajibannya, lingkungan pun menjadi lebih teratur dan nyaman bagi siapa saja, dirinya termasuk."),
  ("h2", "Bagaimana Hak dan Kewajiban Diseimbangkan dalam Demokrasi"),
  ("p", "Apakah kebebasan dalam demokrasi tidak ada batasnya? Ada. Demokrasi memberi ruang untuk bersuara dan memilih, tetapi menuntut kedewasaan agar kebebasan tidak berubah menjadi kekacauan. Hak memilih, misalnya, harus dipakai dengan jujur, bukan dijual."),
  ("p", "Keseimbangan ini bisa dilatih sejak di kampus. Menyampaikan pendapat dalam forum sambil menghormati pendapat lain adalah bentuk nyata kedewasaan berdemokrasi yang sederhana namun bermakna."),
  ("h2", "Mengapa Menghargai Kelompok Rentan Itu Penting"),
  ("p", "Bagaimana kita tahu sebuah lingkungan benar-benar adil? Salah satu tandanya tampak dari cara ia memperlakukan kelompok yang rentan, misalnya penyandang disabilitas. Kampus yang ramah menyiapkan jalur akses yang memadai serta memperlakukan tiap mahasiswa setara."),
  ("p", "Penghargaan berangkat dari perkara kecil, misalnya tidak meremehkan dan mau menolong tanpa membuat yang dibantu merasa direndahkan. Membuka peluang yang setara bagi setiap orang adalah cerminan paling tulus dari penghormatan pada martabat manusia."),
 ],
 "6": [
  ("h2", "Mengapa Akses Keadilan Belum Merata"),
  ("p", "Apakah setiap orang punya peluang yang sama untuk mendapat keadilan? Kenyataannya belum. Biaya, jarak ke pengadilan, dan minimnya informasi membuat sebagian warga, terutama yang kurang mampu, sulit memperjuangkan haknya."),
  ("p", "Jurang semacam ini sepatutnya dijembatani lewat penyuluhan hukum yang lebih merata serta layanan pendampingan yang gampang dijangkau. Program pengabdian yang digerakkan kampus bisa menjadi satu cara membantu warga mengerti sekaligus menuntut haknya."),
  ("h2", "Bagaimana Kesadaran Hukum Tumbuh dari Hal Kecil"),
  ("p", "Haruskah kesadaran hukum dimulai dari peristiwa besar? Tidak. Kesadaran itu terbentuk dari rutinitas keseharian, misalnya tertib di jalan, mengembalikan barang yang bukan miliknya, serta menjauhi kebiasaan menyontek. Hal-hal kecil inilah yang membentuk budaya hukum dalam jangka panjang."),
  ("p", "Kejujuran ketika tidak ada yang mengawasi adalah ujian kesadaran hukum yang sebenarnya. Mahasiswa yang menyerahkan barang temuan ke pos keamanan, misalnya, sedang membuktikan bahwa menghormati hak orang lain tidak bergantung pada ada atau tidaknya pengawasan."),
  ("h2", "Apa Pentingnya Peradilan yang Merdeka"),
  ("p", "Mengapa hakim harus bebas dari tekanan? Karena keadilan hanya mungkin bila putusan didasarkan pada hukum dan fakta, bukan pada kepentingan pihak yang kuat. Peradilan yang merdeka adalah syarat agar masyarakat percaya untuk mencari keadilan lewat jalur resmi."),
  ("p", "Hanya saja, kemerdekaan itu mesti diimbangi pengawasan atas perilaku hakim supaya tidak berubah menjadi tindakan sewenang-wenang. Titik temu antara kemandirian dan kontrol itulah yang menjaga mutu peradilan."),
 ],
 "7": [
  ("h2", "Mengapa Pembangunan Harus Merata"),
  ("p", "Apa jadinya bila pembangunan hanya menumpuk di kota besar? Daerah lain akan merasa ditinggalkan, dan perasaan itu bila dibiarkan dapat menumbuhkan ketidakpuasan. Wawasan nusantara menuntut pemerataan agar setiap warga ikut menikmati hasil kemerdekaan."),
  ("p", "Ketika daerah perbatasan dan pulau kecil diperhatikan, ikatan terhadap bangsa menguat. Pemerataan dengan demikian bukan sekadar urusan ekonomi, melainkan juga cara menjaga persatuan dari dalam."),
  ("h2", "Bagaimana Menjaga Ketahanan di Ruang Digital"),
  ("p", "Di mana medan ketahanan nasional yang paling ramai hari ini? Jawabannya ada di ruang digital. Kabar yang memecah belah sering melaju lebih kencang ketimbang waktu yang dibutuhkan orang untuk memeriksanya, sehingga daya tahan terhadap informasi menjadi amat penting."),
  ("p", "Mahasiswa dapat berperan sebagai penyaring, yaitu memeriksa kebenaran sebelum membagikan dan menahan komentar yang memperkeruh suasana. Satu sikap tenang di tengah keramaian sering lebih berguna daripada seratus komentar yang memanaskan."),
  ("h2", "Apa Wujud Cinta Tanah Air Sehari-hari"),
  ("p", "Apakah cinta tanah air harus ditunjukkan lewat hal besar? Tidak. Ia dapat tampak pada perbuatan sederhana, misalnya memakai produk buatan negeri sendiri, menjaga kebersihan sekitar, dan tekun dalam belajar."),
  ("p", "Bagi mahasiswa, berprestasi dan menjaga integritas adalah bentuk cinta tanah air yang nyata. Dengan menjadi pribadi yang berkualitas, seseorang turut memperkuat bangsanya tanpa harus menunggu kesempatan yang besar."),
 ],
 "8": [
  ("h2", "Apa Saja Bentuk Korupsi yang Perlu Diwaspadai"),
  ("p", "Apakah korupsi selalu mudah dikenali? Tidak. Ia hadir dalam banyak rupa, dan sebagiannya menyamar sebagai hal yang wajar. Mengenali ragamnya membuat kita lebih waspada agar tidak menganggap suatu praktik sebagai kelaziman."),
  ("p", "Suap dipakai untuk memuluskan urusan, gratifikasi menyamar sebagai hadiah yang berkaitan dengan jabatan, dan pemerasan memaksa orang lain memberi sesuatu. Memberi uang pelicin agar layanan dipercepat pun termasuk benih korupsi, meski sering dianggap biasa."),
  ("h2", "Bagaimana Mencegah Korupsi lewat Sistem dan Watak"),
  ("p", "Cukupkah melawan korupsi hanya dengan hukuman? Tidak. Pencegahan menuntut dua hal sekaligus, yaitu sistem yang baik dan watak yang jujur. Sistem yang terbuka mempersempit celah, sedangkan watak yang lurus menutup niat sejak awal."),
  ("p", "Keduanya harus berjalan beriringan. Betapapun rapi sebuah sistem, ia mudah disiasati jika manusianya tidak jujur, sebaliknya orang jujur pun akan terseok ketika sistem di sekitarnya rusak. Karena itu, perbaikan tata kelola dan pembentukan karakter perlu dikerjakan bersama."),
  ("h2", "Mengapa Integritas Menjadi Bekal Masa Depan"),
  ("p", "Apa yang paling dicari dari seseorang di dunia kerja? Sering kali bukan sekadar kepandaian, melainkan kepercayaan. Di sinilah integritas menjadi bekal yang menentukan, karena orang yang dapat dipercaya akan selalu dibutuhkan."),
  ("p", "Integritas terbentuk dari hal-hal kecil yang dibiasakan, misalnya menepati janji, mau mengaku salah, dan enggan menempuh jalan pintas yang curang. Mahasiswa yang melatihnya sejak kuliah sedang menyiapkan diri menjadi pribadi yang sulit digoyahkan oleh godaan di kemudian hari."),
 ],
}

_splice(EXTRA1)



# ===================== PENDALAMAN TAHAP 2 =====================
EXTRA2 = {
 "1": [
  ("h2", "Apakah Materi Ini Hanya Teori yang Jauh dari Kenyataan"),
  ("p", "Sering terdengar keluhan bahwa pelajaran kewarganegaraan terasa melayang dan jauh dari kehidupan. Benarkah demikian? Jika dicermati, justru materinya sangat dekat. Setiap kali kita berurusan dengan aturan kampus, antrean layanan publik, atau perdebatan di media sosial, di situ persoalan kewarganegaraan sedang hadir."),
  ("p", "Yang membuatnya terasa jauh biasanya cara penyampaiannya, bukan materinya. Bila dikaitkan dengan persoalan nyata yang dialami mahasiswa, pelajaran ini berubah menjadi bekal yang terasa berguna, bukan sekadar hafalan untuk ujian."),
  ("h2", "Bagaimana Kewarganegaraan Terasa di Dunia Kerja"),
  ("p", "Apa hubungan mata kuliah ini dengan pekerjaan nanti? Lebih erat dari yang dikira. Dunia kerja menuntut orang yang jujur, mampu bekerja sama dengan latar berbeda, dan menghormati aturan. Semua itu adalah nilai kewarganegaraan yang dilatih sejak di kampus."),
  ("p", "Seorang pekerja yang dapat dipercaya dan mampu menjaga sikap biasanya lebih dihargai daripada yang sekadar pandai. Maka membiasakan nilai baik sejak kuliah sebenarnya sedang menyiapkan diri untuk diterima di lingkungan kerja mana pun."),
  ("h2", "Mengapa Terlibat Lebih Berarti daripada Sekadar Tahu"),
  ("p", "Apakah cukup hanya mengetahui hak dan kewajiban tanpa menjalankannya? Tentu tidak. Pengetahuan yang tidak diwujudkan dalam tindakan ibarat peta yang tidak pernah dipakai berjalan. Karena itu, mata kuliah ini mendorong keterlibatan, bukan sekadar pemahaman."),
  ("p", "Keterlibatan bisa dimulai dari hal sederhana, seperti aktif dalam organisasi, peduli pada lingkungan, dan menyuarakan aspirasi lewat jalur yang tepat. Dari keterlibatan kecil yang konsisten, lahir warga negara yang tidak apatis."),
 ],
 "2": [
  ("h2", "Bagaimana Bahasa Indonesia Menyatukan di Kampus"),
  ("p", "Pernahkah membayangkan betapa sulitnya kuliah bila setiap mahasiswa bertahan dengan bahasa daerahnya? Di sinilah peran bahasa Indonesia terasa. Ia menjadi jembatan yang membuat mahasiswa dari berbagai daerah dapat saling memahami tanpa harus meninggalkan bahasa ibu masing-masing."),
  ("p", "Memakai bahasa Indonesia secara baik turut menandakan kita menghargai orang yang diajak bicara. Dalam diskusi akademik, kemampuan menyusun gagasan secara jelas dan santun membuat percakapan berjalan sehat. Bahasa, dengan demikian, bukan sekadar alat, melainkan cermin sikap."),
  ("h2", "Apa Peran Lambang Negara dalam Keseharian"),
  ("p", "Apakah bendera, lambang Garuda, dan lagu kebangsaan hanya hadir saat upacara? Seharusnya tidak. Lambang-lambang itu berkedudukan hukum lewat Undang-Undang Nomor 24 Tahun 2009 dan berfungsi sebagai penanda jati diri yang layak dihormati setiap saat."),
  ("p", "Penghormatan pada simbol negara dapat ditunjukkan lewat hal sederhana, misalnya bersikap khidmat saat upacara dan melagukan Indonesia Raya dengan sepenuh hati. Sikap kecil ini menumbuhkan rasa bangga sebagai bangsa."),
  ("h2", "Mengapa Keberagaman Disebut Kekayaan"),
  ("p", "Apakah perbedaan suku dan budaya itu hambatan atau justru anugerah? Jawabannya bergantung pada cara mengelolanya. Bila perbedaan dihormati, ia menjadi kekayaan yang tidak dimiliki banyak negara lain. Bila dipertajam, ia bisa menjadi sumber gesekan."),
  ("p", "Di lingkungan kampus, keberagaman memberi peluang menimba hal baru dari kawan lintas daerah, baik soal cara berpikir maupun kebiasaan baiknya. Sikap terbuka inilah yang mengubah perbedaan menjadi berkah, bukan beban."),
 ],
 "3": [
  ("h2", "Bagaimana Menyikapi Perbedaan Pilihan"),
  ("p", "Apa yang sebaiknya dilakukan ketika teman memilih jalan yang berbeda, entah dalam organisasi atau pandangan? Jawaban dewasanya adalah menghormati, selama pilihan itu tidak melanggar hak orang lain. Perbedaan pilihan adalah hal lumrah dalam masyarakat yang sehat."),
  ("p", "Yang merusak persatuan bukan perbedaan itu sendiri, melainkan cara menyikapinya dengan kebencian. Bila perbedaan disikapi dengan dialog dan kepala dingin, ia justru memperkaya pertimbangan dan memperkuat keputusan bersama."),
  ("h2", "Apa Bahaya Berita Palsu bagi Persatuan"),
  ("p", "Mengapa kabar bohong begitu ditakuti dalam konteks integrasi? Karena ia menyebar cepat dan menyentuh emosi sebelum sempat diperiksa. Satu kabar palsu yang menyinggung suku atau agama bisa memantik keributan yang sulit dipadamkan."),
  ("p", "Mahasiswa sebagai kelompok terdidik diharapkan menjadi penyaring, bukan penyambung kebohongan. Memeriksa sumber sebelum membagikan adalah langkah kecil yang berdampak besar bagi ketenangan bersama."),
  ("h2", "Mengapa Kerukunan Dimulai dari Lingkungan Terdekat"),
  ("p", "Bisakah seseorang menjaga persatuan bangsa bila dengan tetangga kos saja sering berselisih? Sulit. Kerukunan berskala besar sebenarnya berakar dari kerukunan kecil di lingkungan terdekat, seperti kos, kelas, dan kelompok tugas."),
  ("p", "Menghargai jam istirahat sesama, membagi giliran bersih-bersih, serta memecahkan persoalan lewat musyawarah merupakan latihan yang nyata. Dari kebiasaan baik di lingkungan kecil inilah kemampuan menjaga kerukunan yang lebih luas tumbuh."),
 ],
 "4": [
  ("h2", "Apa Beda Konstitusi Tertulis dan Kebiasaan Ketatanegaraan"),
  ("p", "Apakah aturan dasar negara hanya yang tertulis? Tidak sepenuhnya. Selain naskah resmi seperti Undang-Undang Dasar Tahun 1945, ada kebiasaan ketatanegaraan yang dijalankan secara taat asas walau tidak tertulis. Keduanya sama-sama menjaga jalannya pemerintahan."),
  ("p", "Kebiasaan semacam ini muncul dari praktik yang berulang dan diterima bersama. Walau tidak dibukukan, ia dihormati karena memberi kepastian tentang bagaimana sesuatu biasa dijalankan dalam kehidupan bernegara."),
  ("h2", "Bagaimana Lembaga Negara Saling Mengimbangi"),
  ("p", "Mengapa kekuasaan dibagi kepada beberapa lembaga, bukan dipegang satu tangan? Agar tidak ada yang berkuasa tanpa kendali. Dewan pembentuk undang-undang mengawasi kerja pemerintah, badan peradilan menguji sah tidaknya sebuah aturan, sementara pemerintah menjalankan ketetapan yang telah disepakati bersama."),
  ("p", "Mekanisme saling mengimbangi ini menjaga agar setiap lembaga tetap berada di jalurnya. Ketika satu lembaga mencoba melampaui batas, lembaga lain dapat mengoreksi, sehingga keseimbangan tetap terpelihara."),
  ("h2", "Mengapa Kesadaran Berkonstitusi Perlu Dilatih"),
  ("p", "Apakah memahami konstitusi cukup hanya dengan membacanya sekali? Tidak. Kesadaran berkonstitusi dipupuk lewat kebiasaan, misalnya patuh pada tata tertib kampus, berpendapat dengan santun, dan menuntaskan perselisihan melalui saluran yang resmi."),
  ("p", "Mahasiswa juga dapat berlatih dengan menilai kebijakan publik secara kritis namun berdasar. Bila ada aturan yang dinilai bertentangan dengan hak dasar, kritik dapat disampaikan melalui forum atau tulisan, bukan lewat keributan."),
 ],
 "5": [
  ("h2", "Apa yang Membedakan Hak Warga Negara dan Hak Asasi"),
  ("p", "Apakah keduanya sama? Tidak persis. Hak warga negara lahir dari status kewarganegaraan seseorang dan berada di bawah hukum nasional. Sementara hak asasi melekat pada manusia sejak lahir dan berlaku universal, sehingga tidak dapat dirampas oleh negara mana pun."),
  ("p", "Perbedaan ini penting agar kita tidak keliru menempatkan keduanya. Seorang warga asing, misalnya, tidak memiliki semua hak warga negara Indonesia, tetapi hak asasinya tetap wajib dihormati selama ia berada di wilayah ini."),
  ("h2", "Bagaimana Menjaga Privasi Orang Lain di Era Digital"),
  ("p", "Apakah menyebar tangkapan layar percakapan teman itu sekadar candaan? Tidak sesederhana itu. Membagikan foto, percakapan, atau data pribadi tanpa izin adalah pelanggaran yang sering dianggap remeh, padahal dampaknya bisa serius bagi yang bersangkutan."),
  ("p", "Menjaga privasi berarti meminta persetujuan sebelum menyebarkan milik orang lain sekaligus mengekang rasa penasaran yang kelewatan. Sikap ini adalah bentuk paling nyata dari menghargai hak orang lain di ruang digital."),
  ("h2", "Mengapa Tanggung Jawab Sosial Tetap Diperlukan"),
  ("p", "Apakah cukup menjadi warga yang taat hukum tanpa peduli sekitar? Belum cukup. Selain kewajiban hukum, ada tanggung jawab sosial berupa kepedulian terhadap lingkungan dan kesediaan membantu sesama. Tanggung jawab inilah yang membuat masyarakat terasa hidup."),
  ("p", "Jika setiap orang hanya tenggelam dalam urusan pribadinya, semangat kebersamaan lambat laun memudar. Mahasiswa dapat merawatnya lewat aksi sosial dan kepedulian pada persoalan di sekitarnya, sekecil apa pun bentuknya."),
 ],
 "6": [
  ("h2", "Apa Itu Asas Praduga Tak Bersalah"),
  ("p", "Mengapa seseorang tidak boleh langsung dicap bersalah sebelum diadili? Sebab hukum di negeri ini memegang asas praduga tak bersalah, yakni seseorang dipandang belum bersalah hingga kesalahannya terbukti lewat proses yang sah. Asas tersebut menjaga siapa pun agar tidak divonis secara tergesa-gesa."),
  ("p", "Di era media sosial, asas ini sering dilupakan. Seseorang bisa dihujat cuma berbekal kabar yang belum tentu benar. Di titik ini mahasiswa sebaiknya menahan diri dan menghormati proses hukum, alih-alih ikut menjatuhkan vonis lebih dahulu."),
  ("h2", "Bagaimana Masyarakat Ikut Mengawal Jalannya Hukum"),
  ("p", "Apakah penegakan hukum hanya urusan aparat? Tidak. Masyarakat dapat ikut mengawal agar prosesnya tetap adil, tentu dengan cara yang sehat, yaitu berdasarkan data dan fakta, bukan tekanan massa yang justru bisa mengganggu."),
  ("p", "Peran mahasiswa bisa hadir melalui perbincangan yang bermutu, karya tulis yang beralasan kuat, serta daya kritis yang disertai tanggung jawab. Mengawal bukan berarti menghakimi, melainkan memastikan keadilan ditegakkan secara terbuka."),
  ("h2", "Mengapa Kepercayaan pada Hukum Mudah Rusak"),
  ("p", "Apa yang terjadi bila masyarakat sekali saja merasa hukum tidak adil? Kepercayaan yang dibangun lama bisa runtuh seketika dan sulit dipulihkan. Padahal tanpa kepercayaan, orang cenderung mengambil jalan sendiri yang justru menambah masalah."),
  ("p", "Memulihkan kepercayaan menuntut bukti, bukan janji. Menegakkan hukum secara ajeg tanpa tebang pilih adalah cara yang paling kelihatan hasilnya, dan keikutsertaan warga dalam mengawasi turut menjaga marwah hukum."),
 ],
 "7": [
  ("h2", "Apa Makna Indonesia sebagai Negara Maritim"),
  ("p", "Mengapa laut begitu sering disebut saat membahas Indonesia? Karena sebagian besar wilayah negeri ini memang berupa lautan. Kesadaran sebagai bangsa bahari menjadikan laut bukan sekadar batas, melainkan sumber pangan, energi, dan jalur dagang yang harus dijaga."),
  ("p", "Menjaga laut berarti menjaga masa depan. Pencemaran dan pengambilan ikan secara ilegal adalah persoalan yang menyangkut kedaulatan sekaligus kesejahteraan. Generasi muda perlu memandang laut sebagai bagian penting dari kehidupan bangsa, bukan sekadar latar pada peta."),
  ("h2", "Bagaimana Astagatra Menjelaskan Ketahanan Nasional"),
  ("p", "Mengapa ketahanan nasional tidak diukur dari satu hal saja? Karena kekuatan bangsa berdiri di atas banyak sisi yang saling menopang. Konsep astagatra menggambarkan hal ini, yaitu gabungan aspek alamiah seperti wilayah dan kekayaan alam dengan aspek sosial seperti ideologi, politik, ekonomi, sosial budaya, serta pertahanan."),
  ("p", "Pelajaran dari konsep ini sederhana, yaitu bahwa membangun bangsa tidak bisa berat sebelah. Negara yang kuat ekonominya tetapi lemah persatuannya tetap rapuh, begitu pula sebaliknya. Keseimbanganlah yang menjadi kunci."),
  ("h2", "Mengapa Ketahanan Mental Termasuk Diperhitungkan"),
  ("p", "Apakah ketahanan nasional hanya soal negara dan tidak menyentuh pribadi? Ternyata menyentuh. Pada lingkup paling kecil, ketahanan dimulai dari kemampuan tiap orang mengelola tekanan dan tetap berpikir jernih dalam situasi sulit."),
  ("p", "Kesanggupan menolong sesama agar tahan menghadapi tekanan juga termasuk ketahanan sosial. Lingkungan yang saling menopang melahirkan pribadi yang tangguh, dan pribadi semacam itulah fondasi bangsa yang kuat."),
 ],
 "8": [
  ("h2", "Apa Dampak Korupsi bagi Rakyat Kecil"),
  ("p", "Siapa yang paling dirugikan ketika anggaran dikorupsi? Sering kali justru rakyat kecil. Dana yang seharusnya untuk sekolah, jalan, atau layanan kesehatan berpindah ke segelintir orang, sehingga yang paling membutuhkan malah paling menderita."),
  ("p", "Dampaknya tidak berhenti pada angka. Korupsi menurunkan kepercayaan terhadap negara dan menumbuhkan sikap permisif terhadap ketidakjujuran. Dengan begitu, memerangi korupsi pada dasarnya berarti berpihak kepada kelompok yang paling lemah."),
  ("h2", "Bagaimana Membangun Budaya Jujur di Organisasi"),
  ("p", "Di mana mahasiswa bisa berlatih melawan korupsi secara nyata? Salah satunya di organisasi kemahasiswaan. Keuangan yang dilaporkan secara terbuka, dana yang jelas pertanggungjawabannya, serta keputusan yang dimusyawarahkan bersama anggota merupakan latihan integritas yang nyata."),
  ("p", "Organisasi yang dikelola jujur menjadi latihan kepemimpinan yang berharga. Berani menegur kejanggalan dengan cara yang baik, serta terbuka menerima koreksi, akan menumbuhkan budaya yang sehat dan menular kepada anggota lain."),
  ("h2", "Mengapa Keberanian Termasuk Nilai Antikorupsi"),
  ("p", "Mengapa menolak korupsi membutuhkan keberanian? Karena godaan dan tekanan sering datang dari lingkungan sendiri. Berkata tidak pada ajakan menyontek atau berbuat curang kadang terasa berat, dan di situlah keberanian seseorang diuji."),
  ("p", "Keberanian moral tidak harus berupa tindakan besar. Berani jujur sekalipun merugikan diri, serta berani melaporkan kejanggalan, merupakan keberanian yang menempa watak. Mahasiswa yang terbiasa demikian akan sukar ditaklukkan oleh godaan korupsi."),
 ],
}

_splice(EXTRA2)



# ===================== PENDALAMAN TAHAP 3 =====================
EXTRA3 = {
 "1": [
  ("h2", "Apakah Setiap Jurusan Benar-Benar Membutuhkannya"),
  ("p", "Mengapa mahasiswa dari jurusan apa pun tetap mengikuti mata kuliah ini? Karena setiap lulusan, apa pun bidangnya, akan hidup di tengah masyarakat. Insinyur, perawat, akuntan, dan konselor sama-sama membutuhkan kejujuran, kerja sama, dan kepekaan sosial."),
  ("p", "Ilmu teknis membuat seseorang ahli, tetapi nilai kewarganegaraan membuat keahlian itu berguna bagi banyak orang. Tanpa landasan ini, keahlian bisa dipakai untuk kepentingan sempit yang merugikan sesama."),
  ("h2", "Bagaimana Menjadi Penyaring Informasi yang Baik"),
  ("p", "Apa yang membedakan orang yang bijak bermedia dari yang mudah terhasut? Kebiasaan memeriksa sebelum mempercayai. Penyaring informasi yang baik bertanya dari mana sumbernya, apa buktinya, dan siapa yang diuntungkan dari sebuah kabar."),
  ("p", "Sikap ini menjaga seseorang dari menjadi penyebar kebohongan tanpa sadar. Mahasiswa yang terlatih menyaring informasi turut menjaga ketenangan lingkungannya, karena ia tidak ikut memperkeruh suasana dengan kabar yang belum jelas."),
  ("h2", "Mengapa Sikap Toleran Termasuk Hasil Belajar"),
  ("p", "Bisakah toleransi diajarkan? Bisa, terutama lewat kebiasaan. Ketika mahasiswa terbiasa berdiskusi dengan orang yang berbeda pandangan tanpa memusuhi, ia sedang belajar toleransi secara nyata, bukan sekadar teori."),
  ("p", "Toleransi yang matang bukan berarti tidak punya pendirian. Ia berarti tetap berpegang pada nilai sambil menghormati hak orang lain untuk berbeda. Sikap inilah yang ingin ditumbuhkan oleh Pendidikan Kewarganegaraan."),
 ],
 "2": [
  ("h2", "Bagaimana Identitas Memengaruhi Rasa Percaya Diri"),
  ("p", "Apa hubungan jati diri bangsa dengan kepercayaan diri seseorang? Cukup erat. Seseorang yang akrab dengan akar budayanya biasanya lebih teguh melangkah dan tak gampang goyah oleh arus dari luar."),
  ("p", "Jati diri yang kuat justru membuat seseorang lebih leluasa menyerap hal baru tanpa kehilangan arah. Ia bisa terbuka pada kemajuan dunia sambil tetap memegang nilai bangsanya, sehingga maju tanpa tercerabut dari akarnya."),
  ("h2", "Apa Peran Keluarga dalam Menanamkan Jati Diri"),
  ("p", "Di mana nilai kebangsaan pertama kali dikenal? Biasanya di rumah. Keluarga menanamkan kejujuran, sopan santun, dan cinta tanah air jauh sebelum kampus melanjutkannya. Bila fondasi di rumah kuat, upaya kampus dan masyarakat menjadi lebih ringan."),
  ("p", "Karena itu, merawat identitas nasional sebenarnya kerja bersama antara keluarga, kampus, dan masyarakat. Mahasiswa pun kelak akan meneruskan nilai itu kepada lingkungan dan keluarganya sendiri."),
  ("h2", "Mengapa Kampus Disebut Miniatur Indonesia"),
  ("p", "Mengapa kehidupan kampus sering disebut sebagai Indonesia dalam ukuran kecil? Karena di sana berkumpul mahasiswa dari berbagai daerah, suku, dan latar yang berbeda, lalu belajar dan berkegiatan bersama."),
  ("p", "Apabila ruang itu dijaga dengan sikap saling menghormati, Bhinneka Tunggal Ika berhenti menjadi sekadar tulisan dan berubah menjadi pengalaman yang nyata tiap hari. Kampus menjadi tempat berlatih hidup berbangsa sebelum terjun ke masyarakat luas."),
 ],
 "3": [
  ("h2", "Apa Hubungan Keadilan Sosial dengan Persatuan"),
  ("p", "Mengapa rasa adil memengaruhi keutuhan bangsa? Karena masyarakat yang merasa diperlakukan adil cenderung lebih setia dan tidak mudah dipecah. Sebaliknya, jurang ketimpangan yang didiamkan bisa menumbuhkan kekecewaan yang membahayakan."),
  ("p", "Pemerataan kesempatan, baik dalam pendidikan maupun ekonomi, menjadi perekat yang menghubungkan warga dengan negaranya. Karena itu, menjaga keadilan sosial sebenarnya juga menjaga persatuan."),
  ("h2", "Bagaimana Mahasiswa Bisa Menjadi Penengah Konflik"),
  ("p", "Apa yang dapat dilakukan mahasiswa ketika melihat gesekan di sekitarnya? Ia bisa menjadi penengah, yaitu pihak yang menenangkan dan membuka ruang dialog, bukan yang menambah panas suasana. Kemampuan mendengarkan menjadi modal utama di sini."),
  ("p", "Banyak konflik bermula dari salah paham yang dibiarkan membesar. Mahasiswa yang mampu menjelaskan duduk perkara dengan tenang sering kali dapat mencairkan ketegangan sebelum berubah menjadi pertikaian."),
  ("h2", "Mengapa Sikap Eksklusif Berbahaya bagi Bangsa"),
  ("p", "Apa salahnya berkumpul hanya dengan kelompok yang sama? Tidak salah sepenuhnya, tetapi bila berubah menjadi sikap menutup diri dan memandang rendah kelompok lain, di situ bahayanya. Sikap eksklusif menanam jarak yang lama-lama bisa memecah."),
  ("p", "Lawan dari sikap ini adalah keterbukaan untuk bergaul lintas kelompok. Mahasiswa yang terbiasa berbaur akan lebih mudah memahami perbedaan dan lebih tahan terhadap hasutan yang ingin mengadu domba."),
 ],
 "4": [
  ("h2", "Apa Manfaat Membaca Konstitusi secara Langsung"),
  ("p", "Mengapa sebaiknya membaca naskah konstitusi sendiri, bukan hanya mendengar tafsir orang? Karena dengan membaca langsung, kita memahami maknanya secara utuh dan tidak mudah disesatkan oleh penafsiran yang keliru atau sepotong-sepotong."),
  ("p", "Dokumen Undang-Undang Dasar Tahun 1945 sekarang gampang dijangkau melalui sumber resmi yang dapat dipercaya. Terbiasa kembali ke naskah aslinya akan menajamkan daya kritis sekaligus menumbuhkan penghormatan pada hukum dasar negara."),
  ("h2", "Bagaimana Konstitusi Melindungi Kelompok Minoritas"),
  ("p", "Dalam demokrasi yang menghargai suara terbanyak, bagaimana nasib kelompok kecil? Di sinilah konstitusi berperan. Ia memastikan hak kelompok minoritas tetap dihormati, sehingga demokrasi tidak berubah menjadi penindasan atas nama mayoritas."),
  ("p", "Perlindungan ini penting agar setiap warga merasa aman menjadi dirinya. Bangsa yang melindungi yang lemah dan yang berbeda menunjukkan kematangan dalam berdemokrasi."),
  ("h2", "Mengapa Masa Jabatan Pemimpin Dibatasi"),
  ("p", "Mengapa seorang pemimpin tidak boleh berkuasa selamanya? Sebab sejarah memperlihatkan bahwa kuasa yang digenggam terlalu lama rawan diselewengkan. Adanya batas masa jabatan mengingatkan bahwa setiap kekuasaan ada ujungnya."),
  ("p", "Prinsip yang sama berlaku di organisasi mahasiswa. Pergantian kepengurusan secara berkala mencegah kekuasaan menumpuk dan membuka jalan bagi munculnya pemimpin baru yang segar."),
 ],
 "5": [
  ("h2", "Bagaimana Menjadi Pemilih yang Cerdas"),
  ("p", "Apa arti menggunakan hak pilih secara cerdas? Maksudnya, suara ditentukan dengan menimbang rekam jejak serta gagasan calon, bukan tergoda uang atau sekadar mengekor. Pemilih yang cerdas turut menentukan mutu pemimpin yang terpilih."),
  ("p", "Kebiasaan ini bisa dilatih sejak dari pemilihan ketua organisasi di kampus. Memilih berdasarkan kemampuan, bukan kedekatan pribadi, adalah latihan berharga sebelum kelak ikut menentukan arah bangsa."),
  ("h2", "Apa Arti Kebebasan Berpendapat yang Bertanggung Jawab"),
  ("p", "Apakah kebebasan berpendapat berarti boleh mengatakan apa saja? Tidak. Pendapat tetap harus menghormati hak orang lain dan tidak menyebarkan kebencian atau kebohongan. Kebebasan tanpa tanggung jawab justru bisa melukai."),
  ("p", "Di kampus, kebebasan ini terlihat saat mahasiswa mengkritik kebijakan lewat forum yang tepat. Kritik yang disertai data dan disampaikan santun jauh lebih didengar daripada yang dilontarkan dengan emosi."),
  ("h2", "Mengapa Hak atas Pendidikan Begitu Mendasar"),
  ("p", "Mengapa pendidikan disebut hak yang mendasar? Karena melalui pendidikan, seseorang memperoleh kesempatan untuk memperbaiki hidupnya dan ikut membangun masyarakat. Tanpa akses pendidikan, banyak hak lain ikut sulit diraih."),
  ("p", "Menyadari hal ini, mahasiswa yang beruntung mengenyam pendidikan tinggi sebaiknya tidak menyia-nyiakannya. Bersungguh-sungguh dalam belajar adalah salah satu cara menghargai hak yang belum tentu dimiliki semua orang."),
 ],
 "6": [
  ("h2", "Bagaimana Edukasi Hukum Menjangkau Masyarakat"),
  ("p", "Mengapa banyak orang tidak tahu cara memperjuangkan haknya? Sering kali karena minimnya informasi hukum. Edukasi hukum yang sederhana dan mudah dipahami dapat menutup celah ini, sehingga warga tahu ke mana harus mengadu."),
  ("p", "Kampus dapat ikut berperan lewat kegiatan pengabdian, misalnya penyuluhan tentang hak dasar atau perlindungan data pribadi. Lewat cara ini, ilmu yang dipelajari di kelas menjadi manfaat nyata bagi masyarakat."),
  ("h2", "Apa Peran Lembaga Penegak Hukum"),
  ("p", "Siapa saja yang menegakkan hukum, dan apa bedanya peran mereka? Kepolisian menjaga keamanan dan menyelidiki pelanggaran, kejaksaan menuntut perkara, sedangkan pengadilan memutus secara adil. Masing-masing punya batas wewenang yang jelas."),
  ("p", "Memahami pembagian peran ini membantu masyarakat tahu ke lembaga mana harus melapor. Kerja sama yang sehat antarlembaga, disertai pengawasan publik, menjadi syarat agar hukum ditegakkan dengan adil."),
  ("h2", "Mengapa Hukum Harus Berpihak pada Kebenaran"),
  ("p", "Kepada siapa hukum seharusnya berpihak? Jawabannya jelas, yaitu kepada yang benar dan yang adil, bukan kepada pihak yang bermodal kuasa. Ketika hukum ditegakkan dengan jujur, masyarakat merasa terlindungi, dan kepercayaan pun tumbuh."),
  ("p", "Mewujudkan hukum yang berpihak pada kebenaran menuntut aparat yang berintegritas dan warga yang ikut mengawasi. Salah satu peran mahasiswa adalah konsisten menampik suap dalam rupa apa pun, betapapun kecil nilainya, pada keseharian."),
 ],
 "7": [
  ("h2", "Bagaimana Menghargai Budaya Daerah Lain"),
  ("p", "Apakah mencintai budaya sendiri berarti meremehkan budaya daerah lain? Justru sebaliknya. Mahasiswa yang berwawasan nusantara belajar menghargai budaya daerah lain sambil tetap melestarikan budayanya sendiri."),
  ("p", "Mengenal tarian, bahasa, atau kuliner dari daerah lain menumbuhkan rasa kagum, bukan curiga. Dari kekaguman itulah lahir penghargaan yang memperkuat rasa kebersamaan sebagai satu bangsa."),
  ("h2", "Apa Tantangan Generasi Muda terhadap Wawasan Nusantara"),
  ("p", "Apa yang paling menantang bagi generasi muda dalam menjaga wawasan nusantara? Derasnya informasi digital turut menghadirkan beragam nilai asing, dan tidak semuanya selaras dengan budaya bangsa. Tanpa kemampuan menyaring, seseorang mudah terombang-ambing."),
  ("p", "Tantangan lain adalah sikap individualistis yang membuat orang abai pada kepentingan bersama. Padahal ketahanan bangsa membutuhkan kepedulian dan kerja sama, bukan sekadar pencapaian pribadi."),
  ("h2", "Mengapa Lingkungan Hidup Termasuk Urusan Bela Negara"),
  ("p", "Apa kaitan menjaga lingkungan dengan membela negara? Sangat erat. Karena nasib bangsa bergantung pada kelestarian alam, terjaganya hutan, sungai, dan laut menjadi warisan berharga bagi anak cucu kelak."),
  ("p", "Mahasiswa dapat berkontribusi lewat kebiasaan sederhana, seperti mengurangi sampah plastik dan ikut kegiatan pelestarian. Langkah kecil yang ditempuh oleh banyak orang pada akhirnya membawa pengaruh besar bagi negeri."),
 ],
 "8": [
  ("h2", "Apa Peran Lembaga Negara dalam Pemberantasan Korupsi"),
  ("p", "Siapa yang menangani korupsi di Indonesia? Ada sejumlah lembaga yang turut menangani, antara lain Komisi Pemberantasan Korupsi, kepolisian, kejaksaan, sampai pengadilan. Komisi Pemberantasan Korupsi mengemban peran istimewa sebab menggarap pencegahan dan penindakan sekaligus."),
  ("p", "Namun, memberantas korupsi tidak bisa dibebankan kepada aparat saja. Ia menuntut perbaikan tata kelola, transparansi, dan keterlibatan masyarakat. Keberhasilannya bergantung pada kerja sama banyak pihak."),
  ("h2", "Bagaimana Pendidikan Antikorupsi Ditanam di Kampus"),
  ("p", "Apakah cukup mengajarkan antikorupsi lewat satu mata kuliah? Belum cukup. Nilai antikorupsi perlu tercermin dalam budaya dan tata kelola kampus, mulai dari penilaian yang adil hingga ketegasan terhadap kecurangan."),
  ("p", "Konsistensi antara yang diajarkan dan yang dipraktikkan menjadi kunci. Kampus yang menindak plagiarisme dan mengelola dana secara terbuka sedang menanam fondasi integritas yang nyata bagi mahasiswanya."),
  ("h2", "Mengapa Kejujuran Kecil Menentukan Masa Depan"),
  ("p", "Apakah kejujuran dalam hal kecil benar-benar berpengaruh? Sangat. Orang yang terbiasa jujur dalam perkara kecil akan lebih mudah jujur saat memegang amanah besar. Sebaliknya, kebiasaan curang kecil dapat tumbuh menjadi penyimpangan besar."),
  ("p", "Oleh sebab itu, pendidikan antikorupsi semestinya menjangkau hal-hal sehari-hari, tidak melulu mengupas kasus kakap yang terasa jauh. Membiasakan jujur dalam tugas dan laporan adalah latihan paling nyata membangun masa depan yang bersih."),
 ],
}

_splice(EXTRA3)



# ===================== PENDALAMAN TAHAP 4 (top-up ke sasaran 62-66) =====================
EXTRA4 = {
 "1": [
  ("h2", "Bagaimana Menyikapi Anggapan Materi Ini Membosankan"),
  ("p", "Mengapa sebagian mahasiswa merasa mata kuliah ini membosankan? Biasanya karena membayangkannya sebagai deretan teori yang harus dihafal. Padahal bila didekati lewat pertanyaan dan persoalan nyata, materinya bisa terasa hidup dan dekat."),
  ("p", "Sikap yang membantu adalah membaca dengan rasa ingin tahu, bukan sekadar mengejar nilai. Ketika mahasiswa mulai mengaitkan materi dengan apa yang ia alami sehari-hari, kebosanan perlahan berganti menjadi minat."),
 ],
 "2": [
  ("h2", "Mengapa Merawat Identitas Adalah Kerja Bersama"),
  ("p", "Apakah menjaga jati diri bangsa bisa dibebankan kepada satu pihak saja? Tidak. Ia menuntut peran keluarga yang menanamkan nilai, kampus yang merawat kesadaran, dan masyarakat yang memberi teladan. Ketiganya saling melengkapi."),
  ("p", "Mahasiswa berada di posisi yang strategis karena bisa menjadi penghubung. Lewat karya, sikap, dan pergaulan yang terbuka, ia ikut menularkan kebanggaan pada budaya bangsa kepada lingkungan sekitarnya."),
 ],
 "3": [
  ("h2", "Bagaimana Solidaritas Terlihat saat Menghadapi Bencana"),
  ("p", "Kapan rasa sebangsa paling terasa? Sering kali justru saat bencana melanda. Pada saat itu, bantuan mengalir dari berbagai daerah tanpa banyak orang mempersoalkan suku atau agama. Solidaritas semacam ini membuktikan bahwa persatuan masih hidup."),
  ("p", "Mahasiswa bisa ikut ambil bagian dalam solidaritas tersebut melalui penggalangan donasi maupun aksi kemanusiaan. Pengalaman menolong sesama yang sedang kesulitan menumbuhkan empati sekaligus mempererat rasa kebersamaan."),
 ],
 "4": [
  ("h2", "Mengapa Hubungan Negara dan Warga Bersifat Timbal Balik"),
  ("p", "Apakah negara hanya berhak memerintah dan warga hanya wajib menurut? Tidak sesederhana itu. Negara berwenang membuat aturan, tetapi kewenangannya dibatasi agar tidak melanggar hak. Sebaliknya, warga wajib menaati aturan, namun berhak menuntut pelayanan dan perlindungan."),
  ("p", "Hubungan dua arah ini sebaiknya dijalani dengan saling menghormati. Negara hadir guna melayani, sementara warga turut ambil bagian secara bertanggung jawab. Ketika keduanya menjalankan perannya, kehidupan bernegara berjalan tertib."),
 ],
 "5": [
  ("h2", "Mengapa Menghormati Hak Orang Lain Menandai Kedewasaan"),
  ("p", "Apa tanda seseorang dewasa dalam berdemokrasi? Salah satunya adalah kesediaan menghormati hak orang lain, bahkan ketika ia tidak sepakat. Kebebasan diri berhenti di titik kebebasan orang lain dimulai, dan kesadaran itu menandai kematangan."),
  ("p", "Di kampus, sikap ini terlihat saat mahasiswa memberi kesempatan teman untuk berbicara, menghargai keputusan bersama, dan tidak memaksakan kehendak. Kebiasaan kecil ini menyiapkan seseorang untuk hidup di masyarakat yang beragam."),
 ],
 "6": [
  ("h2", "Bagaimana Kepercayaan pada Hukum Dapat Dibangun"),
  ("p", "Apa yang membuat masyarakat mau menyelesaikan masalah lewat jalur hukum? Kepercayaan. Ketika orang yakin bahwa hukum ditegakkan secara jujur dan tidak pandang bulu, mereka akan memilih jalur resmi daripada main hakim sendiri."),
  ("p", "Kepercayaan ini dibangun lewat bukti, bukan janji, yaitu penegakan hukum yang konsisten dan terbuka. Mahasiswa dapat ikut menjaga dengan bersikap kritis yang bertanggung jawab dan menolak praktik suap dalam bentuk apa pun."),
 ],
 "7": [
  ("h2", "Mengapa Persatuan Wilayah Perlu Dirasakan Setiap Hari"),
  ("p", "Apakah kesatuan wilayah cukup dipahami sebagai garis pada peta? Tidak. Ia perlu dirasakan dalam sikap, yaitu merasa ikut memiliki seluruh Indonesia, bukan hanya daerah asal. Tanpa rasa memiliki ini, kepentingan daerah mudah dipertentangkan dengan kepentingan bangsa."),
  ("p", "Bagi mahasiswa, rasa memiliki itu tumbuh melalui pertemanan dengan kawan dari beragam daerah. Berkenalan dengan sudut pandang yang berlainan memperlihatkan bahwa perbedaan wilayah justru menambah kaya, bukan memecah belah."),
 ],
 "8": [
  ("h2", "Bagaimana Generasi Berintegritas Dibentuk"),
  ("p", "Dari mana lahir generasi yang berintegritas? Bukan dari ceramah semata, melainkan dari keteladanan. Teladan nyata bisa datang dari pengajar yang berlaku adil, kampus yang tidak menoleransi kecurangan, hingga keluarga yang membiasakan kejujuran."),
  ("p", "Mahasiswa pun ikut membentuk dirinya lewat pilihan kecil setiap hari, seperti menggarap tugas dengan jujur dan mengakui kesalahan. Dari kebiasaan inilah tumbuh pribadi yang kelak sulit digoyahkan oleh godaan menyimpang."),
 ],
}

_splice(EXTRA4)
