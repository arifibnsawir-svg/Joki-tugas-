# -*- coding: utf-8 -*-
# Konten Mini Book PKN - Nurjali Sangadji (Buku #5).
# DNA: ekspositori ringkas-padat + kotak "Poin Inti" (bernomor) + kotak "Istilah Kunci" (glosarium),
# warna indigo/slate, nomor halaman bawah-tengah (dgn garis), daftar isi banded, pustaka Chicago.
# Humanizer di semua bagian. Beda dari Buku 1/2/3/4.
# Blok: ('p',teks) | ('h2',teks) | ('poin',{'judul','items':[...]}) | ('istilah',{'judul','pairs':[(istilah,arti)]})

PENULIS = "Nurjali Sangadji"

KATA_PENGANTAR = [
 "Mini book ini saya tulis dengan satu tujuan, yaitu menyajikan materi Pendidikan Kewarganegaraan secara ringkas namun tetap berisi. Banyak buku terasa berat karena penjelasannya berputar-putar, sehingga di sini saya memilih bahasa yang lugas dan langsung pada pokok persoalan.",
 "Untuk membantu pembaca, setiap bab saya lengkapi dengan kotak poin inti dan kotak istilah kunci. Poin inti merangkum gagasan utama dalam butir-butir singkat, sedangkan istilah kunci menjelaskan kata-kata penting agar tidak menimbulkan salah paham. Dengan begitu, pembaca dapat menangkap isi bab dengan cepat sekaligus memahami detailnya.",
 "Sebagai mahasiswa Bimbingan dan Konseling di Universitas Indraprasta PGRI, saya melihat materi kewarganegaraan sebagai bekal mengenali manusia beserta lingkungannya. Cara pandang itu saya bawa dalam menyusun naskah ini, sehingga pembahasan diusahakan dekat dengan kehidupan nyata.",
 "Ucapan terima kasih saya haturkan kepada dosen pengampu, keluarga, serta sahabat yang menemani sepanjang proses penulisan. Saya menyadari naskah ini masih memiliki kekurangan, sehingga kritik dan saran yang membangun akan saya terima dengan terbuka.",
 "Jakarta, 2026",
 "Penulis,",
 "Nurjali Sangadji",
]

# Daftar Pustaka format Chicago (author-date: Author. Year. Judul. Diakses. URL.), urut alfabetis.
# Tiap entri: ('teks sebelum judul', 'judul miring', 'sisa teks termasuk tautan')
DAFTAR_PUSTAKA = [
 ("Komisi Pemberantasan Korupsi. 2024. ", "Anti-Corruption Learning Center: Materi Pembelajaran Antikorupsi", ". Diakses 28 Juni 2026. https://aclc.kpk.go.id/materi-pembelajaran."),
 ("Perserikatan Bangsa-Bangsa. 1948. ", "Universal Declaration of Human Rights", ". Diakses 28 Juni 2026. https://www.un.org/en/about-us/universal-declaration-of-human-rights."),
 ("Republik Indonesia. 1945. ", "Undang-Undang Dasar Negara Republik Indonesia Tahun 1945", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Dasar_Negara_Republik_Indonesia_Tahun_1945."),
 ("Republik Indonesia. 1999. ", "Undang-Undang Nomor 31 Tahun 1999 tentang Pemberantasan Tindak Pidana Korupsi", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_31_Tahun_1999."),
 ("Republik Indonesia. 1999. ", "Undang-Undang Nomor 39 Tahun 1999 tentang Hak Asasi Manusia", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_39_Tahun_1999."),
 ("Republik Indonesia. 2001. ", "Undang-Undang Nomor 20 Tahun 2001 tentang Perubahan atas Undang-Undang Nomor 31 Tahun 1999", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_20_Tahun_2001."),
 ("Republik Indonesia. 2002. ", "Undang-Undang Nomor 3 Tahun 2002 tentang Pertahanan Negara", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_3_Tahun_2002."),
 ("Republik Indonesia. 2003. ", "Undang-Undang Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_20_Tahun_2003."),
 ("Republik Indonesia. 2006. ", "Undang-Undang Nomor 12 Tahun 2006 tentang Kewarganegaraan Republik Indonesia", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2006."),
 ("Republik Indonesia. 2009. ", "Undang-Undang Nomor 24 Tahun 2009 tentang Bendera, Bahasa, dan Lambang Negara, serta Lagu Kebangsaan", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_24_Tahun_2009."),
 ("Republik Indonesia. 2009. ", "Undang-Undang Nomor 48 Tahun 2009 tentang Kekuasaan Kehakiman", ". Diakses 28 Juni 2026. https://commons.wikimedia.org/wiki/File:Undang-Undang_Republik_Indonesia_Nomor_48_Tahun_2009.pdf."),
 ("Republik Indonesia. 2012. ", "Undang-Undang Nomor 12 Tahun 2012 tentang Pendidikan Tinggi", ". Diakses 28 Juni 2026. https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2012."),
]

BAB = []


# ===================== BAB 1 =====================
BAB.append({
 "no": "1",
 "judul": "HAKIKAT PENDIDIKAN KEWARGANEGARAAN",
 "isi": [
  ("p", "Bab ini menjelaskan dasar dari Pendidikan Kewarganegaraan secara ringkas. Pembahasan bergerak dari pengertian, landasan hukum, tujuan, sampai urgensinya bagi mahasiswa. Tujuannya agar pembaca cepat menangkap mengapa mata kuliah ini wajib ditempuh di perguruan tinggi."),

  ("h2", "Pengertian Pendidikan Kewarganegaraan"),
  ("p", "Pendidikan Kewarganegaraan pada dasarnya merupakan pembelajaran untuk membentuk pribadi yang memahami hak, kewajiban, serta perannya selaku warga negara. Mata kuliah ini memadukan tiga unsur sekaligus, yakni wawasan tentang kenegaraan, sikap menghormati sesama, dan kecakapan ikut serta dalam kehidupan publik."),
  ("p", "Berbeda dengan pelajaran di sekolah yang menekankan pengenalan, di perguruan tinggi penekanannya pada analisis dan penerapan. Mahasiswa diajak menimbang persoalan, bukan sekadar menghafal aturan."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Civic knowledge", "Pengetahuan dasar tentang negara, hukum, dan demokrasi."),
      ("Civic disposition", "Sikap dan watak sebagai warga negara, seperti jujur dan toleran."),
      ("Civic skill", "Keterampilan berperan di ruang publik, seperti berdiskusi dan menyampaikan pendapat."),
    ]}),

  ("h2", "Landasan Hukum"),
  ("p", "Kedudukan Pendidikan Kewarganegaraan di perguruan tinggi memiliki dasar hukum yang kuat, sehingga bukan sekadar kebijakan kampus. Landasan ini menempatkannya sebagai bagian wajib dari sistem pendidikan nasional."),
  ("poin", {"judul": "Poin Inti: Dasar Hukum",
    "items": [
      "Pancasila sebagai sumber nilai dan arah moral kehidupan berbangsa.",
      "Undang-Undang Dasar Negara Republik Indonesia Tahun 1945, yang memerintahkan agar pendidikan mencerdaskan kehidupan bangsa.",
      "Undang-Undang Nomor 20 Tahun 2003 yang memuat pendidikan kewarganegaraan dalam kurikulum.",
      "Undang-Undang Nomor 12 Tahun 2012 yang menetapkannya sebagai mata kuliah wajib di perguruan tinggi.",
    ]}),

  ("h2", "Tujuan dan Kompetensi"),
  ("p", "Sasaran pokok mata kuliah ini ialah mencetak warga yang berpikiran tajam, berwatak baik, dan mau turun tangan. Sasaran tersebut diterjemahkan ke dalam sejumlah kemampuan yang diharapkan dimiliki mahasiswa setelah menempuhnya."),
  ("poin", {"judul": "Poin Inti: Kompetensi yang Diharapkan",
    "items": [
      "Memahami dasar kehidupan bernegara dan nilai Pancasila.",
      "Berpikir kritis dalam menyikapi informasi dan persoalan bangsa.",
      "Bersikap toleran dan menghargai keberagaman.",
      "Berpartisipasi secara bertanggung jawab di lingkungan kampus dan masyarakat.",
    ]}),

  ("h2", "Urgensi di Era Digital"),
  ("p", "Pada era digital, informasi mengalir cepat dan tidak semuanya benar. Tanpa dasar kewarganegaraan yang kuat, seseorang mudah terhasut atau ikut menyebarkan kabar yang keliru. Pendidikan Kewarganegaraan melatih sikap selektif dan kritis dalam menyikapi arus informasi."),
  ("p", "Kepentingan ini kian terasa mengingat Indonesia merupakan bangsa yang majemuk. Kemampuan menghargai perbedaan menjadi syarat agar keberagaman tidak berubah menjadi perpecahan."),

  ("h2", "Relevansi bagi Mahasiswa"),
  ("p", "Bagi mahasiswa, nilai yang dipelajari di sini terpakai dalam keseharian, mulai dari menaati aturan akademik sampai bersikap adil terhadap teman. Bagi yang menekuni bidang pendampingan manusia, kebiasaan menghargai martabat orang lain menjadi bekal langsung untuk profesinya kelak."),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Pendidikan Kewarganegaraan ialah mata kuliah wajib yang mencetak warga berpikiran tajam, berwatak baik, dan gemar terlibat, dengan pijakan hukum yang tegas. Penekanannya di perguruan tinggi ada pada analisis dan penerapan, bukan hafalan. Di era digital, perannya sebagai penyaring informasi semakin penting."),
 ]
})


# ===================== BAB 2 =====================
BAB.append({
 "no": "2",
 "judul": "IDENTITAS NASIONAL",
 "isi": [
  ("p", "Bab ini menelaah identitas nasional, yakni penanda yang membuat suatu bangsa dikenali sekaligus berbeda dari bangsa lainnya. Pembahasan mencakup pengertian, unsur pembentuk, kedudukan Pancasila, serta tantangan yang dihadapi di era keterbukaan."),

  ("h2", "Pengertian Identitas Nasional"),
  ("p", "Identitas nasional pada hakikatnya merupakan jati diri sebuah bangsa. Wujudnya ada dua, yaitu yang kasat mata seperti bendera dan lagu kebangsaan, serta yang tidak kasat mata seperti nilai bersama dan kesadaran sejarah. Keduanya berpadu menjadi rasa sebagai satu bangsa."),
  ("p", "Identitas ini tidak muncul seketika. Ia terbentuk melalui pengalaman sejarah yang panjang dan terus dirawat oleh setiap generasi."),

  ("h2", "Unsur Pembentuk"),
  ("p", "Identitas nasional disusun oleh beberapa unsur yang saling menopang. Mengenali unsur-unsur ini memudahkan kita memahami dari mana rasa kebangsaan berasal."),
  ("poin", {"judul": "Poin Inti: Unsur Identitas Nasional",
    "items": [
      "Sejarah perjuangan sebagai ingatan bersama yang menumbuhkan rasa sebangsa.",
      "Bahasa Indonesia sebagai alat pemersatu penutur ratusan bahasa daerah.",
      "Kebudayaan yang beragam sebagai kekayaan yang merangkul perbedaan.",
      "Simbol negara, yakni bendera, lambang, serta lagu kebangsaan, yang ketentuannya diatur Undang-Undang Nomor 24 Tahun 2009.",
    ]}),

  ("h2", "Pancasila sebagai Pengikat"),
  ("p", "Pancasila menduduki posisi istimewa di dalam identitas nasional. Perannya tak terbatas sebagai dasar negara, melainkan juga titik temu nilai yang dipegang sebagian besar rakyat. Kelima sila merangkum ketuhanan, kemanusiaan, persatuan, kerakyatan, dan keadilan sosial menjadi satu kesatuan."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Identitas nasional", "Jati diri bangsa yang membedakannya dari bangsa lain."),
      ("Bhinneka Tunggal Ika", "Semboyan yang berarti berbeda-beda tetapi tetap satu."),
      ("Pemersatu", "Unsur yang menyatukan keberagaman tanpa menghapus perbedaan."),
    ]}),

  ("h2", "Tantangan di Era Keterbukaan"),
  ("p", "Keterbukaan global membuat budaya luar mudah masuk melalui layar gawai. Dampaknya tak melulu negatif, namun menjadi soal begitu seseorang lebih mengagungkan budaya asing daripada budaya sendiri."),
  ("p", "Tantangan lain adalah menyusutnya minat pada sejarah bangsa. Tanpa mengenal sejarah, alasan untuk menjaga persatuan menjadi kabur."),
  ("poin", {"judul": "Poin Inti: Merawat Identitas",
    "items": [
      "Menggunakan bahasa Indonesia dengan baik tanpa meninggalkan bahasa daerah.",
      "Memperkenalkan budaya daerah lewat karya yang positif.",
      "Menyelami sejarah bangsa supaya punya alasan kuat untuk merawat persatuan.",
      "Menampik ucapan yang melecehkan suku, agama, maupun daerah lain.",
    ]}),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Pada dasarnya, identitas nasional ialah jati diri bangsa yang terbangun dari sejarah, bahasa, kebudayaan, dan lambang negara, lalu dipersatukan oleh Pancasila. Tantangan terbesarnya adalah lunturnya kebanggaan pada budaya sendiri. Merawatnya dimulai dari sikap sederhana sehari-hari."),
 ]
})


# ===================== BAB 3 =====================
BAB.append({
 "no": "3",
 "judul": "INTEGRASI NASIONAL",
 "isi": [
  ("p", "Bagian ini mengupas integrasi nasional, yakni upaya merajut beragam kelompok menjadi satu bangsa yang utuh. Cakupannya meliputi pengertian, faktor pendorong dan penghambat, serta peran mahasiswa dalam merawat persatuan."),

  ("h2", "Pengertian Integrasi Nasional"),
  ("p", "Integrasi nasional berarti merangkai perbedaan menjadi satu kesatuan bangsa tanpa menghapus keragamannya. Indonesia teramat beragam, dari suku, agama, bahasa, hingga taraf ekonomi, sehingga persatuan tidak datang otomatis dan harus diperjuangkan."),
  ("p", "Menyatu di sini bukan berarti menyeragamkan. Yang dijaga adalah agar perbedaan tetap berjalan berdampingan tanpa berubah menjadi konflik."),

  ("h2", "Faktor Pendorong dan Penghambat"),
  ("p", "Integrasi dipengaruhi oleh hal yang memperkuat dan hal yang melemahkan. Mengenali keduanya membantu kita lebih waspada."),
  ("poin", {"judul": "Poin Inti: Pendorong dan Penghambat",
    "items": [
      "Pendorong: rasa seperjuangan, bahasa Indonesia, dan nilai Pancasila.",
      "Pendorong: semangat gotong royong dalam keseharian.",
      "Penghambat: kesenjangan ekonomi antardaerah.",
      "Penghambat: sentimen suku dan agama yang ditunggangi, serta kabar bohong.",
    ]}),

  ("h2", "Toleransi sebagai Perekat"),
  ("p", "Integrasi membutuhkan toleransi. Bersikap toleran berarti bersedia hidup berdampingan dengan yang berbeda sambil menghormati hak tiap orang. Namun toleransi tetap berbatas, yakni tidak merestui perbuatan yang menabrak hukum atau merugikan sesama."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Integrasi nasional", "Proses menyatukan keberagaman menjadi satu bangsa yang utuh."),
      ("Disintegrasi", "Keadaan terpecahnya persatuan akibat konflik yang tidak terkelola."),
      ("Toleransi", "Sikap menghargai perbedaan tanpa kehilangan prinsip."),
    ]}),

  ("h2", "Peran Mahasiswa"),
  ("p", "Mahasiswa berada pada posisi penting untuk menjaga integrasi. Perannya dimulai dari hal yang dekat dan terjangkau, bukan dari aksi besar yang muluk."),
  ("poin", {"judul": "Poin Inti: Peran Mahasiswa",
    "items": [
      "Berteman lintas daerah dan menolak sikap menutup diri.",
      "Giat berorganisasi dalam wadah yang terbuka serta terbiasa bermusyawarah.",
      "Memeriksa kebenaran informasi sebelum membagikan.",
      "Menyampaikan kritik dengan cara santun dan berdasar.",
    ]}),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Integrasi nasional adalah upaya merajut keberagaman menjadi satu bangsa tanpa meniadakan perbedaan. Pendorongnya rasa seperjuangan, bahasa, dan nilai Pancasila, sedangkan penghambatnya kesenjangan, sentimen sempit, dan kabar bohong. Toleransi yang berprinsip menjadi perekat, dan mahasiswa dapat merawatnya dari pergaulan sehari-hari."),
 ]
})


# ===================== BAB 4 =====================
BAB.append({
 "no": "4",
 "judul": "NEGARA DAN KONSTITUSI",
 "isi": [
  ("p", "Bab ini mengulas negara dan konstitusi selaku rangka yang menopang kehidupan bernegara. Pembahasan mencakup pengertian konstitusi, kedudukan Undang-Undang Dasar Tahun 1945, lembaga negara, serta prinsip menjunjung konstitusi sebagai hukum tertinggi."),

  ("h2", "Pengertian Konstitusi"),
  ("p", "Konstitusi merupakan hukum dasar yang berfungsi sebagai acuan paling tinggi dalam menjalankan roda negara. Ia menata pertalian penguasa dengan rakyatnya, kerja antarlembaga, serta hak dan kewajiban tiap pihak. Konstitusi tertulis yang dipakai Indonesia adalah Undang-Undang Dasar Negara Republik Indonesia Tahun 1945."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Konstitusi", "Hukum dasar tertinggi yang mengatur penyelenggaraan negara."),
      ("Amandemen", "Perubahan resmi terhadap naskah undang-undang dasar."),
      ("Supremasi konstitusi", "Prinsip bahwa konstitusi berada di atas semua aturan dan kekuasaan."),
    ]}),

  ("h2", "Sejarah Singkat dan Amandemen"),
  ("p", "Naskah Undang-Undang Dasar Tahun 1945 disahkan tanggal 18 Agustus 1945, tepat sehari sesudah proklamasi. Indonesia sempat memakai Konstitusi Republik Indonesia Serikat dan Undang-Undang Dasar Sementara, sebelum kembali ke naskah semula. Pada masa reformasi, naskah ini diubah empat kali sepanjang tahun 1999 hingga 2002."),
  ("poin", {"judul": "Poin Inti: Hasil Amandemen",
    "items": [
      "Penegasan jaminan hak asasi manusia.",
      "Pembatasan masa jabatan presiden.",
      "Penataan kembali lembaga negara.",
      "Pengaturan pemilihan umum yang lebih demokratis.",
    ]}),

  ("h2", "Fungsi Konstitusi"),
  ("p", "Konstitusi mengemban beragam peran agar penyelenggaraan negara berlangsung tertib sekaligus berkeadilan. Peran-peran itulah yang menjadi alasan setiap negara modern membutuhkan hukum dasar."),
  ("poin", {"judul": "Poin Inti: Fungsi Konstitusi",
    "items": [
      "Membatasi kekuasaan agar tidak menumpuk pada satu pihak.",
      "Menata hubungan antarlembaga negara agar tidak berbenturan.",
      "Melindungi hak warga dari tindakan sewenang-wenang.",
      "Menjadi rujukan paling tinggi yang mengikat segenap aturan di bawahnya.",
    ]}),

  ("h2", "Lembaga Negara dan Pengawasan"),
  ("p", "Undang-Undang Dasar Tahun 1945 membagi kekuasaan ke dalam tiga cabang agar tidak ada lembaga yang berkuasa tanpa kendali. Cabang legislatif membentuk undang-undang, cabang eksekutif menjalankan pemerintahan, dan cabang yudikatif menegakkan keadilan. Ketiganya saling mengawasi melalui mekanisme yang dikenal sebagai saling mengimbangi."),

  ("h2", "Supremasi Konstitusi"),
  ("p", "Menjunjung konstitusi sebagai hukum tertinggi berarti tidak ada pihak yang boleh bertindak di luar batasnya. Prinsip ini menjadi penjaga utama negara hukum. Mahasiswa dapat ikut menjaganya lewat sikap kecil, seperti membaca aturan sebelum berkomentar dan menaati tata tertib kampus."),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Konstitusi berkedudukan sebagai aturan pokok tertinggi yang membatasi kekuasaan, menata jalinan antarlembaga, serta mengawal hak warga. Undang-Undang Dasar Tahun 1945 sudah mengalami empat kali amandemen. Lembaga negara dipisah supaya saling mengontrol, dan supremasi konstitusi menjamin tidak ada pihak yang kebal aturan."),
 ]
})


# ===================== BAB 5 =====================
BAB.append({
 "no": "5",
 "judul": "HAK DAN KEWAJIBAN WARGA NEGARA",
 "isi": [
  ("p", "Pada bagian ini diuraikan hak serta kewajiban warga negara, dengan hak asasi manusia sebagai salah satu pokok pentingnya. Penekanannya terletak pada kenyataan bahwa hak dan kewajiban senantiasa berjalan seiring dalam bingkai tanggung jawab."),

  ("h2", "Pengertian Hak dan Kewajiban"),
  ("p", "Hak warga negara pada hakikatnya adalah kewenangan yang lahir dari status keanggotaan seseorang pada sebuah negara, dan kewenangan tersebut dijamin oleh hukum. Adapun kewajiban adalah hal yang wajib dipenuhi sebagai konsekuensi keanggotaan itu, misalnya menaati peraturan dan menghormati hak sesama. Keduanya tidak bisa dipisah-pisahkan."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Hak warga negara", "Kewenangan yang melekat karena status kewarganegaraan."),
      ("Kewajiban", "Hal yang harus dijalankan sebagai konsekuensi keanggotaan dalam negara."),
      ("Hak asasi manusia", "Hak yang melekat pada manusia sejak lahir, bersifat universal."),
    ]}),

  ("h2", "Ragam Hak Warga Negara"),
  ("p", "Hak warga negara menyentuh banyak bidang kehidupan. Lantaran saling terhubung, terabaikannya satu hak kerap menyeret hak yang lain."),
  ("poin", {"judul": "Poin Inti: Hak Menurut Bidangnya",
    "items": [
      "Politik, misalnya hak memilih dan dipilih.",
      "Ekonomi, misalnya hak bekerja dan memiliki harta.",
      "Bidang sosial budaya, contohnya hak memperoleh pendidikan dan mengembangkan kebudayaan.",
      "Sipil, misalnya kebebasan berpendapat, beragama, dan berkumpul.",
    ]}),

  ("h2", "Hak Asasi Manusia"),
  ("p", "Hak asasi manusia berlingkup lebih luas ketimbang hak warga negara. Ia telah melekat pada diri manusia semenjak kelahirannya, tanpa memandang suku, agama, maupun status kewarganegaraan. Maka, orang asing yang tinggal di Indonesia pun tetap memikul hak asasi yang harus dihormati."),
  ("p", "Di Indonesia, jaminan hak asasi berpijak pada Undang-Undang Dasar Tahun 1945 serta Undang-Undang Nomor 39 Tahun 1999, dan pemantauannya dipegang Komisi Nasional Hak Asasi Manusia. Di panggung internasional, asasnya termaktub dalam Deklarasi Universal Hak Asasi Manusia, dokumen yang ditetapkan Perserikatan Bangsa-Bangsa pada 1948."),

  ("h2", "Keseimbangan dan Tanggung Jawab"),
  ("p", "Hak dan kewajiban lebih tepat ditinjau dalam bingkai tanggung jawab. Tanggung jawab tumbuh dari kesadaran mengerjakan yang sepatutnya, bukan lantaran takut hukuman, melainkan karena yakin hal itu benar. Di ruang digital, kesadaran ini tampak dari etika bermedia sosial."),
  ("poin", {"judul": "Poin Inti: Etika Hak di Dunia Maya",
    "items": [
      "Memeriksa kebenaran informasi sebelum menyebarkannya.",
      "Menghindari ujaran kebencian dan serangan pribadi.",
      "Menghormati privasi dengan tidak menyebar data orang lain tanpa izin.",
      "Tetap kritis tanpa melontarkan kata-kata yang kasar.",
    ]}),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Hak dan kewajiban warga negara berjalan beriringan dalam kerangka tanggung jawab. Hak asasi manusia berlaku menyeluruh dan dijamin lewat Undang-Undang Dasar Tahun 1945 berikut Undang-Undang Nomor 39 Tahun 1999. Etika bermedia sosial menjadi wujud nyata tanggung jawab kewarganegaraan masa kini."),
 ]
})


# ===================== BAB 6 =====================
BAB.append({
 "no": "6",
 "judul": "PENEGAKAN HUKUM YANG BERKEADILAN",
 "isi": [
  ("p", "Bagian ini menyoroti penegakan hukum yang berkeadilan, dengan bertumpu pada gagasan negara hukum. Cakupannya meliputi pengertian negara hukum, prinsipnya, sistem peradilan, tantangan, sampai peran mahasiswa dalam menumbuhkan budaya hukum."),

  ("h2", "Pengertian Negara Hukum"),
  ("p", "Negara hukum ialah negara yang dijalankan berdasarkan hukum, bukan menurut selera penguasa. Setiap tindakan pemerintah harus berpijak pada aturan, sehingga tidak ada seorang pun yang boleh bertindak sewenang-wenang. Indonesia menegaskan jati dirinya selaku negara hukum melalui Pasal 1 ayat (3) Undang-Undang Dasar Tahun 1945."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Negara hukum", "Negara yang seluruh penyelenggaraannya berlandaskan hukum."),
      ("Supremasi hukum", "Keadaan ketika hukum berada di posisi tertinggi bagi semua pihak."),
      ("Budaya hukum", "Kebiasaan masyarakat dalam memahami dan menaati hukum."),
    ]}),

  ("h2", "Prinsip Negara Hukum"),
  ("p", "Negara hukum bertumpu pada sejumlah prinsip yang saling melengkapi. Bila salah satu diabaikan, keadilan menjadi timpang."),
  ("poin", {"judul": "Poin Inti: Prinsip Negara Hukum",
    "items": [
      "Kesetaraan di mata hukum bagi semua orang tanpa kecuali.",
      "Jaminan atas hak dasar warga negara.",
      "Pembatasan kekuasaan melalui pengawasan antarlembaga.",
      "Peradilan yang merdeka dan tidak memihak.",
    ]}),

  ("h2", "Sistem Peradilan"),
  ("p", "Sistem peradilan adalah mekanisme negara untuk menyelesaikan sengketa dan mengadili pelanggaran. Dasar kewenangan kekuasaan kehakiman termuat dalam Undang-Undang Nomor 48 Tahun 2009, sementara peran kepolisian menegakkan hukum diatur oleh Undang-Undang Nomor 2 Tahun 2002."),
  ("poin", {"judul": "Poin Inti: Lingkungan Peradilan",
    "items": [
      "Peradilan umum untuk perkara pidana dan perdata.",
      "Peradilan agama untuk perkara nikah, waris, dan keluarga bagi umat Islam.",
      "Peradilan militer untuk pelanggaran oleh prajurit.",
      "Peradilan tata usaha negara untuk sengketa warga dengan pejabat.",
      "Mahkamah Konstitusi untuk menguji undang-undang terhadap konstitusi.",
    ]}),

  ("h2", "Tantangan dan Budaya Hukum"),
  ("p", "Penegakan hukum masih tersendat akibat akses keadilan yang belum merata serta rapuhnya integritas sebagian penegak. Manakala hukum tampak garang kepada yang lemah tetapi lunak kepada yang berkuasa, kepercayaan publik pun luntur. Itulah sebabnya dibutuhkan aparat yang lurus dan masyarakat yang ikut mengawasi."),
  ("p", "Budaya hukum tumbuh dari kebiasaan, bukan dari hukuman semata. Di kampus, hal itu terlihat lewat ketaatan pada aturan akademik, penolakan terhadap sontek-menyontek, dan penyelesaian perselisihan secara baik. Mahasiswa dapat menyuarakan keadilan lewat jalur sah, seperti tulisan dan dialog, bukan main hakim sendiri."),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Pada negara hukum, hukum ditempatkan sebagai tumpuan utama untuk membatasi kekuasaan sekaligus mengayomi warga, sesuai amanat Pasal 1 ayat (3) Undang-Undang Dasar Tahun 1945. Sistem peradilan membuka jalan menuju keadilan, kendati pelaksanaannya kerap terganjal akses yang timpang serta integritas yang lemah. Budaya hukum berikut peran mahasiswa menjadi penyangganya."),
 ]
})


# ===================== BAB 7 =====================
BAB.append({
 "no": "7",
 "judul": "GEOPOLITIK DAN GEOSTRATEGI",
 "isi": [
  ("p", "Bab ini mengupas geopolitik serta geostrategi Indonesia lewat dua konsep, yakni wawasan nusantara dan ketahanan nasional. Pembahasan mencakup pengertian, unsur, dimensi ketahanan, ancaman, serta peran mahasiswa."),

  ("h2", "Wawasan Nusantara"),
  ("p", "Wawasan nusantara ialah sikap bangsa Indonesia dalam menatap diri serta sekelilingnya, bertumpu pada Pancasila dan Undang-Undang Dasar Tahun 1945, seraya menomorsatukan keutuhan wilayah. Sebagai negara kepulauan terbesar di dunia, Indonesia memandang seluruh wilayah dari Sabang sampai Merauke sebagai satu kesatuan, dan laut dilihat sebagai penghubung, bukan pemisah."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Geopolitik", "Cara pandang negara terhadap wilayah dan kepentingan nasionalnya."),
      ("Geostrategi", "Siasat nasional berdasarkan kondisi geografis untuk mencapai tujuan negara."),
      ("Ketahanan nasional", "Kemampuan bangsa bertahan dan tetap bersatu menghadapi tantangan."),
    ]}),

  ("h2", "Unsur dan Kedudukan"),
  ("p", "Wawasan nusantara berperan penting bagi pertahanan, pembangunan, maupun kehidupan sosial budaya. Unsur pembentuknya dapat dikenali dengan ringkas."),
  ("poin", {"judul": "Poin Inti: Unsur Wawasan Nusantara",
    "items": [
      "Wilayah, yang meliputi daratan, lautan, dan ruang udara di dalam batas kedaulatan.",
      "Bangsa, terdiri atas ratusan suku yang dipersatukan sejarah dan cita-cita.",
      "Budaya, sebagai kekayaan daerah yang hidup berdampingan.",
    ]}),
  ("p", "Dalam hal pembangunan, wawasan nusantara mengharuskan pemerataan supaya kemajuan tidak hanya berpusat di kota besar. Wilayah tepi dan pulau-pulau terluar patut dirawat agar tiap penduduknya merasa benar-benar diakui sebagai bagian bangsa."),

  ("h2", "Ketahanan Nasional"),
  ("p", "Geostrategi diwujudkan melalui ketahanan nasional, yaitu kemampuan bangsa menjaga kelangsungan hidup dan persatuan. Landasan pertahanannya, salah satunya, ditetapkan dalam Undang-Undang Nomor 3 Tahun 2002. Ketahanan ini bukan hanya soal militer, melainkan mencakup banyak dimensi yang dibangun seimbang."),
  ("poin", {"judul": "Poin Inti: Dimensi Ketahanan Nasional",
    "items": [
      "Ideologi, menjaga Pancasila sebagai pegangan hidup.",
      "Politik, menjaga stabilitas pemerintahan yang demokratis.",
      "Ekonomi, membangun kemandirian dan pemerataan.",
      "Sosial budaya, merawat kemampuan hidup dalam keberagaman.",
      "Pertahanan dan keamanan, melindungi kedaulatan negara.",
    ]}),

  ("h2", "Ancaman dan Peran Mahasiswa"),
  ("p", "Ancaman terhadap ketahanan nasional tidak selalu berbentuk fisik. Pada era digital, kabar bohong dan informasi sesat menjadi ancaman serius karena dapat memecah masyarakat dengan cepat. Oleh sebab itu, daya tahan terhadap informasi menjelma unsur penting dalam ketahanan nasional."),
  ("p", "Mahasiswa dapat berperan dengan menjaga persatuan, menyaring informasi, menghargai budaya daerah, serta menjaga kesehatan mental diri dan sekitarnya. Hamparan laut yang luas turut menuntut kesadaran sebagai bangsa bahari, sebab laut adalah lumbung pangan, sumber energi, dan urat dagang yang wajib dijaga."),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Wawasan nusantara menatap seluruh wilayah Indonesia sebagai satu kesatuan utuh, sekaligus menjadi geopolitik bangsa. Geostrategi mewujud dalam ketahanan nasional yang mencakup dimensi ideologi, politik, ekonomi, dan sosial budaya, ditambah pertahanan serta keamanan. Ancaman zaman sekarang kerap berupa disinformasi digital yang bisa dibendung lewat literasi."),
 ]
})


# ===================== BAB 8 =====================
BAB.append({
 "no": "8",
 "judul": "ANTI KORUPSI",
 "isi": [
  ("p", "Bab penutup ini menyoroti anti korupsi sebagai persoalan integritas yang sejatinya dekat dengan keseharian mahasiswa. Uraiannya meliputi pengertian, dasar hukum, dampak, nilai antikorupsi, hingga peran kampus dan mahasiswa."),

  ("h2", "Pengertian Korupsi"),
  ("p", "Korupsi merupakan penyelewengan kekuasaan, jabatan, atau amanah demi keuntungan pribadi maupun kelompok yang merugikan kepentingan umum. Wujudnya tidak selalu pencurian uang secara langsung, sebab suap, gratifikasi, dan penyalahgunaan wewenang termasuk di dalamnya. Apabila didiamkan, perlahan masyarakat akan memandang ketidakjujuran sebagai sesuatu yang lumrah."),
  ("istilah", {"judul": "Istilah Kunci",
    "pairs": [
      ("Korupsi", "Penyalahgunaan amanah demi keuntungan diri yang merugikan publik."),
      ("Gratifikasi", "Pemberian yang berkaitan dengan jabatan seseorang."),
      ("Integritas", "Kesesuaian antara ucapan dan perbuatan disertai kejujuran."),
    ]}),

  ("h2", "Dasar Hukum Pemberantasan Korupsi"),
  ("p", "Indonesia berbekal dasar hukum yang kuat untuk menumpas korupsi, dilengkapi lembaga khusus yang menanganinya. Pemberantasannya tidak cukup melalui hukuman semata, sebab kesadaran perlu ditanam sejak dini."),
  ("poin", {"judul": "Poin Inti: Pijakan Antikorupsi",
    "items": [
      "Undang-Undang Nomor 31 Tahun 1999 sebagai dasar pemberantasan tindak pidana korupsi.",
      "Undang-Undang Nomor 20 Tahun 2001 sebagai penguatannya.",
      "Komisi Pemberantasan Korupsi yang bertugas mencegah sekaligus menindak.",
      "Pendidikan antikorupsi sebagai upaya menumbuhkan kesadaran.",
    ]}),

  ("h2", "Dampak Korupsi"),
  ("p", "Dampak korupsi terasa pada banyak sisi kehidupan. Dengan mengenalinya, seseorang menjadi lebih awas terhadap praktik yang kerap dianggap remeh, semisal menyetor uang pelicin demi layanan yang lebih cepat."),
  ("poin", {"judul": "Poin Inti: Dampak Korupsi",
    "items": [
      "Ekonomi: dana untuk pendidikan dan kesehatan berpindah ke segelintir pihak.",
      "Sosial: ketimpangan melebar dan kepercayaan kepada negara menurun.",
      "Moral: tumbuh sikap permisif terhadap ketidakjujuran.",
    ]}),

  ("h2", "Nilai Antikorupsi"),
  ("p", "Pendidikan antikorupsi berpijak pada penyemaian nilai, bukan semata hafalan pasal. Nilai semacam inilah yang membuat seseorang menampik korupsi bahkan sejak dalam niat. Pencegahan mensyaratkan dua hal sekaligus, yakni tata kelola yang sehat dan pribadi yang jujur."),
  ("poin", {"judul": "Poin Inti: Nilai Antikorupsi di Kampus",
    "items": [
      "Kejujuran, dengan mengerjakan ujian dan tugas tanpa kecurangan.",
      "Tanggung jawab, dengan memikul amanah tanpa menyelewengkannya.",
      "Keberanian, dengan menampik ajakan curang dan melaporkan kejanggalan.",
      "Kesederhanaan, dengan hidup secukupnya tanpa berlebih-lebihan.",
    ]}),

  ("h2", "Peran Kampus dan Mahasiswa"),
  ("p", "Tugas menanam sikap antikorupsi ada di pundak kampus, bukan sebatas lewat kuliah, melainkan juga melalui suasana akademik dan cara pengelolaannya. Kampus yang memaklumi penjiplakan sebenarnya sedang melumrahkan bibit korupsi. Mahasiswa bisa merintis budaya jujur lewat keputusan kecil saban hari, misalnya mengerjakan tugas tanpa kecurangan dan tegas menampik ajakan berlaku menyimpang."),

  ("h2", "Catatan Akhir Bab"),
  ("p", "Korupsi adalah pengkhianatan atas amanah yang merugikan kepentingan umum, dengan dampak luas pada ekonomi, kehidupan sosial, dan moral bangsa. Ketentuan utamanya berpijak pada Undang-Undang Nomor 31 Tahun 1999 yang kemudian diperkuat oleh Undang-Undang Nomor 20 Tahun 2001. Pencegahannya berakar pada penyemaian nilai kejujuran sejak dari keseharian. Sebagai penutup, ulasan ini menyimpulkan semangat semua bab, yakni membekali mahasiswa agar menjadi warga yang jujur, paham hukum, dan siap berbakti bagi bangsa."),
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



# ===================== PENDALAMAN TAHAP 1 =====================
def _splice(extra):
    for bab in BAB:
        no = bab["no"]; isi = bab["isi"]
        if no in extra:
            idx = next((i for i, blk in enumerate(isi) if blk[0] == "h2" and "Catatan Akhir" in blk[1]), len(isi))
            bab["isi"] = isi[:idx] + extra[no] + isi[idx:]
    _renumber()

EXTRA1 = {
 "1": [
  ("h2", "Sejarah Singkat Mata Kuliah"),
  ("p", "Pendidikan Kewarganegaraan di Indonesia tumbuh mengikuti perjalanan bangsa. Sejak awal kemerdekaan, negara menyadari perlunya membentuk warga yang setia dan paham akan tanggung jawabnya. Bentuk dan namanya sempat berubah dari masa ke masa, tetapi tujuan dasarnya tetap, yaitu menanamkan kesadaran berbangsa."),
  ("p", "Di perguruan tinggi, mata kuliah ini ditegaskan kedudukannya melalui Undang-Undang Nomor 12 Tahun 2012. Penegasan itu memastikan setiap lulusan memperoleh bekal kebangsaan, apa pun bidang ilmunya."),
  ("h2", "Bahan Kajian Pokok"),
  ("p", "Cakupan Pendidikan Kewarganegaraan cukup luas karena menyentuh banyak sisi kehidupan bernegara. Materi disusun agar mahasiswa memperoleh gambaran yang utuh, bukan sepotong-sepotong."),
  ("poin", {"judul": "Poin Inti: Bahan Kajian",
    "items": [
      "Hakikat dan urgensi Pendidikan Kewarganegaraan.",
      "Identitas nasional dan integrasi bangsa.",
      "Negara, konstitusi, serta hak dan kewajiban warga.",
      "Penegakan hukum, geopolitik, dan antikorupsi.",
    ]}),
  ("h2", "Pendekatan Pembelajaran"),
  ("p", "Pembelajaran yang efektif tidak berhenti pada ceramah. Mahasiswa diajak berdiskusi, menelaah kasus, dan menyimpulkan sendiri. Cara ini melatih nalar sekaligus keberanian menyampaikan pendapat secara tertib."),
  ("p", "Dengan pendekatan tersebut, materi yang tampak abstrak menjadi lebih dekat dengan pengalaman. Mahasiswa tidak sekadar tahu, tetapi terbiasa menerapkan apa yang dipelajari."),
 ],
 "2": [
  ("h2", "Pancasila sebagai Kepribadian Bangsa"),
  ("p", "Pancasila bukan sekadar rumusan yang dihafal, melainkan kepribadian yang mencerminkan cara hidup bangsa Indonesia. Nilai ketuhanan, kemanusiaan, persatuan, kerakyatan, dan keadilan menjadi pegangan dalam menata kehidupan bersama."),
  ("p", "Sebagai kepribadian, Pancasila membedakan Indonesia dari bangsa lain. Ia menjadi alasan mengapa keberagaman dapat dirangkul tanpa harus menyeragamkan, dan mengapa musyawarah lebih diutamakan daripada paksaan."),
  ("h2", "Bahasa dan Simbol Negara"),
  ("p", "Bahasa Indonesia, bendera Merah Putih, lambang Garuda, dan lagu Indonesia Raya adalah simbol yang berkedudukan hukum melalui Undang-Undang Nomor 24 Tahun 2009. Simbol ini bukan hiasan, melainkan penanda jati diri yang patut dihormati."),
  ("p", "Menghormatinya dapat dilakukan lewat hal sederhana, seperti memakai bahasa Indonesia dengan baik dan mengikuti upacara dengan khidmat. Tindakan kecil semacam itu menumbuhkan kebanggaan sebagai bangsa."),
  ("h2", "Generasi Muda dan Jati Diri"),
  ("p", "Generasi muda tumbuh bersama teknologi dan menyerap banyak nilai dari luar. Jati diri bisa pudar jika mereka lebih mengagumi yang asing daripada milik sendiri. Namun teknologi juga membuka peluang untuk memperkenalkan budaya bangsa ke khalayak yang lebih luas."),
  ("p", "Kuncinya ada pada sikap. Bila digunakan dengan bijak, teknologi justru menjadi sarana memperkuat jati diri, bukan menggerusnya."),
 ],
 "3": [
  ("h2", "Bhinneka Tunggal Ika dalam Praktik"),
  ("p", "Semboyan Bhinneka Tunggal Ika bermakna beraneka ragam namun tetap menyatu. Artinya jauh melampaui tulisan pada lambang negara, sebab ia adalah pedoman hidup yang mesti dijalani. Keberagaman hanya menjadi kekuatan bila disertai sikap saling menghormati."),
  ("p", "Di kampus, asas ini terbukti saat mahasiswa lintas latar mampu menimba ilmu dan berkegiatan dalam satu wadah. Praktik kecil itulah yang menjaga keberagaman tetap menjadi kekayaan."),
  ("h2", "Peran Media dalam Persatuan"),
  ("p", "Media memiliki dua sisi dalam menjaga persatuan. Di satu sisi ia mempererat hubungan dan menyebarkan pesan baik, di sisi lain ia bisa menjadi alat penyebar kebencian dan kabar bohong."),
  ("p", "Mahasiswa sebagai kalangan terpelajar diharapkan memakai media secara bijak, yaitu menebar konten positif dan menahan diri dari komentar yang memanaskan suasana."),
  ("h2", "Gotong Royong sebagai Modal Sosial"),
  ("p", "Gotong royong merupakan nilai warisan yang masih sangat berguna untuk menjaga integrasi. Banyak persoalan terasa ringan ketika dipikul bersama. Di kampus, semangat ini tampak saat mahasiswa bahu-membahu menyiapkan kegiatan atau menolong teman yang kesulitan."),
  ("p", "Nilai ini mengajarkan bahwa kepentingan bersama kadang perlu didahulukan. Kebiasaan tersebut menjadi perekat yang menahan masyarakat dari sikap mementingkan diri sendiri."),
 ],
 "4": [
  ("h2", "Struktur dan Pembukaan Undang-Undang Dasar"),
  ("p", "Undang-Undang Dasar Tahun 1945 terdiri atas Pembukaan dan Batang Tubuh. Pembukaan memuat pernyataan kemerdekaan, sikap menentang penjajahan, serta cita-cita bangsa, dan di dalamnya termaktub rumusan Pancasila. Karena itu, Pembukaan dipandang memiliki kedudukan yang sangat penting."),
  ("p", "Batang Tubuh memuat pasal-pasal yang mengatur penyelenggaraan negara. Keduanya merupakan satu kesatuan yang tidak dapat dipisahkan dalam memahami konstitusi."),
  ("h2", "Tujuan Negara"),
  ("p", "Pembukaan Undang-Undang Dasar Tahun 1945 menegaskan tujuan negara yang menjadi arah seluruh kebijakan. Tujuan ini menjadi tolok ukur apakah penyelenggaraan negara sudah berjalan pada relnya."),
  ("poin", {"judul": "Poin Inti: Tujuan Negara",
    "items": [
      "Melindungi segenap bangsa dan seluruh tumpah darah Indonesia.",
      "Memajukan kesejahteraan umum.",
      "Mencerdaskan kehidupan bangsa.",
      "Ikut melaksanakan ketertiban dunia berdasarkan perdamaian abadi dan keadilan sosial.",
    ]}),
  ("h2", "Konstitusi dalam Keseharian"),
  ("p", "Konstitusi terasa jauh bila hanya dibayangkan sebagai naskah di ruang sidang. Padahal jaminan atas pendidikan, rasa aman, dan kebebasan berpendapat yang dinikmati warga berakar pada konstitusi."),
  ("p", "Menyadari hal ini membuat seseorang lebih menghargai haknya sekaligus memahami batasnya. Konstitusi pun menjadi milik rakyat, bukan sekadar urusan pejabat."),
 ],
 "5": [
  ("h2", "Macam-Macam Hak Asasi Manusia"),
  ("p", "Hak asasi manusia mencakup berbagai bidang kehidupan. Pembagian ini membantu kita mengenali bahwa perlindungan manusia menyentuh banyak aspek sekaligus."),
  ("poin", {"judul": "Poin Inti: Ragam Hak Asasi",
    "items": [
      "Hak pribadi, seperti kebebasan beragama dan berpendapat.",
      "Hak politik, seperti ikut serta dalam pemerintahan.",
      "Hak ekonomi, seperti bekerja dan memiliki harta.",
      "Hak sosial budaya, seperti memperoleh pendidikan.",
      "Hak memperoleh perlakuan adil dalam hukum.",
    ]}),
  ("h2", "Pelanggaran dan Penegakan HAM"),
  ("p", "Pelanggaran hak asasi dapat berupa pelanggaran biasa maupun pelanggaran berat, seperti kekerasan yang dilakukan secara sistematis. Penegakannya berjalan lewat dua jalur, yaitu pencegahan melalui pendidikan dan penindakan melalui peradilan."),
  ("p", "Tantangan masih ada, antara lain penyelesaian kasus masa lalu dan perlindungan kelompok yang rentan. Karena itu, kesadaran masyarakat untuk menghormati hak sesama tetap perlu ditumbuhkan."),
  ("h2", "Penghormatan terhadap Kelompok Rentan"),
  ("p", "Penghargaan terhadap hak asasi benar-benar teruji tatkala berhadapan dengan kelompok lemah, misalnya penyandang disabilitas. Lingkungan yang ramah menyediakan akses memadai dan memperlakukan setiap orang secara setara."),
  ("p", "Sikap itu bermula dari hal kecil, yaitu tidak memandang rendah orang lain dan bersedia membantu tanpa menjadikan yang ditolong merasa dikasihani. Memberi peluang yang setara merupakan bentuk nyata penghormatan atas martabat manusia."),
 ],
 "6": [
  ("h2", "Lembaga Penegak Hukum"),
  ("p", "Penegakan hukum ditangani oleh sejumlah lembaga yang perannya berlainan namun saling menopang. Kepolisian merawat keamanan dan mengusut pelanggaran, kejaksaan mengajukan tuntutan, sedangkan pengadilan menjatuhkan putusan yang adil."),
  ("p", "Memahami pembagian peran ini membantu masyarakat mengetahui ke mana harus mengadu. Sinergi yang sehat antarlembaga, ditambah kontrol dari masyarakat, menjadi prasyarat tegaknya hukum yang adil."),
  ("h2", "Asas Praduga Tak Bersalah"),
  ("p", "Hukum di negeri ini menjunjung asas praduga tidak bersalah, artinya seseorang dipandang bersih selama kesalahannya belum dibuktikan melalui mekanisme yang sah. Asas ini melindungi tiap orang dari penghakiman yang tergesa-gesa."),
  ("p", "Pada masa media sosial, asas tersebut kerap dilupakan. Mahasiswa perlu menjadi pihak yang menahan diri dan menghormati proses hukum, bukan ikut menjatuhkan vonis lebih dulu."),
  ("h2", "Akses Keadilan"),
  ("p", "Tidak setiap orang menikmati kemudahan yang setara dalam menggapai keadilan. Biaya, jarak, dan minimnya informasi sering menghalangi warga yang lemah secara ekonomi. Ketimpangan ini perlu dijawab dengan penyuluhan hukum dan bantuan yang mudah dijangkau."),
  ("p", "Kampus pun bisa turut berperan melalui pengabdian, contohnya menyuluh hak dasar kepada warga. Dengan begitu, ilmu yang dipelajari berbuah manfaat nyata."),
 ],
 "7": [
  ("h2", "Bela Negara sebagai Sikap Hidup"),
  ("p", "Bela negara sering disalahartikan sebagai urusan ketentaraan semata. Padahal, bela negara juga berarti menjaga keutuhan bangsa melalui sikap sehari-hari, seperti menjaga kerukunan, menolak hasutan, dan berprestasi di bidang masing-masing."),
  ("p", "Bagi mahasiswa, bela negara dapat diwujudkan lewat kesungguhan belajar dan menjaga nama baik bangsa. Sikap ini menjadikan bela negara sebagai bagian dari cara hidup, bukan sekadar kewajiban formal."),
  ("h2", "Negara Kepulauan dan Deklarasi Djuanda"),
  ("p", "Indonesia adalah negara kepulauan dengan laut yang luas. Deklarasi Djuanda menegaskan bahwa laut di antara pulau merupakan bagian dari wilayah negara, bukan pemisah. Penegasan ini memperkuat kedaulatan sekaligus kesatuan wilayah."),
  ("p", "Kesadaran sebagai bangsa bahari menuntut kita menjaga laut sebagai sumber pangan, energi, dan jalur dagang. Menjaga laut berarti menjaga masa depan bangsa."),
  ("h2", "Tantangan Maritim"),
  ("p", "Wilayah laut yang luas membawa tantangan tersendiri, seperti pencurian ikan, pencemaran, dan pelanggaran batas wilayah. Tantangan ini menyangkut kedaulatan sekaligus kesejahteraan."),
  ("p", "Mengelola laut menuntut kerja sama banyak pihak dan kesadaran masyarakat. Anak muda sepatutnya melihat laut sebagai urat nadi kehidupan bangsa, bukan cuma garis biru pada peta."),
 ],
 "8": [
  ("h2", "Tata Kelola yang Baik sebagai Penangkal Korupsi"),
  ("p", "Korupsi mematikan esensi tata kelola yang baik. Tata kelola yang sehat menekankan keterbukaan, partisipasi publik, dan pertanggungjawaban. Ketiganya mempersempit ruang gerak penyimpangan."),
  ("poin", {"judul": "Poin Inti: Ciri Tata Kelola yang Baik",
    "items": [
      "Keterbukaan informasi kepada publik.",
      "Pertanggungjawaban atas setiap kebijakan dan anggaran.",
      "Partisipasi masyarakat dalam pengawasan.",
      "Penegakan hukum yang adil dan tidak pandang bulu.",
    ]}),
  ("h2", "Bentuk Korupsi yang Perlu Diwaspadai"),
  ("p", "Korupsi muncul dalam beragam bentuk, dan sebagian di antaranya berkedok sesuatu yang seakan lumrah. Dengan mengenali macamnya, kita lebih waspada supaya tidak menganggapnya hal yang biasa."),
  ("p", "Suap dipakai untuk melancarkan urusan, gratifikasi berkedok hadiah yang berkaitan dengan jabatan, sedangkan pemerasan memaksa orang lain memberi sesuatu. Menyodorkan uang pelicin supaya urusan cepat selesai pun tergolong bibit korupsi."),
  ("h2", "Tiga Pendekatan Pemberantasan"),
  ("p", "Pemberantasan korupsi yang berhasil memadukan tiga pendekatan. Ketiganya saling melengkapi dan tidak bisa berdiri sendiri."),
  ("poin", {"judul": "Poin Inti: Pendekatan Antikorupsi",
    "items": [
      "Pendidikan, yaitu menumbuhkan budaya jujur sejak dini.",
      "Pencegahan, yaitu memperbaiki birokrasi dan menutup celah penyimpangan.",
      "Penindakan, yaitu menegakkan hukum secara tegas terhadap pelaku.",
    ]}),
 ],
}

_splice(EXTRA1)



# ===================== PENDALAMAN TAHAP 2 =====================
EXTRA2 = {
 "1": [
  ("h2", "Pengetahuan Kewarganegaraan dan Penerapannya"),
  ("p", "Pengetahuan kewarganegaraan membantu mahasiswa memahami dasar kehidupan bernegara. Namun pengetahuan saja tidak cukup. Ia baru bermakna ketika diwujudkan dalam sikap dan tindakan nyata, seperti menaati aturan dan menghargai sesama."),
  ("p", "Karena itu, mata kuliah ini tidak berhenti pada teori. Mahasiswa diajak menautkan apa yang dipelajari dengan keputusan yang ia ambil sehari-hari, sehingga ilmu berubah menjadi perilaku."),
  ("h2", "Tantangan di Era Industri 4.0"),
  ("p", "Era industri 4.0 membawa perubahan besar dalam cara orang berkomunikasi dan memperoleh informasi. Mahasiswa dituntut memiliki kesadaran kewarganegaraan digital, yaitu sikap bertanggung jawab dalam memakai teknologi."),
  ("p", "Tanpa kesadaran ini, kemajuan teknologi justru dapat menyuburkan kebohongan dan kebencian. Pendidikan Kewarganegaraan hadir untuk membekali mahasiswa agar bijak menyikapi perubahan tersebut."),
  ("h2", "Kewarganegaraan dan Pembentukan Karakter"),
  ("p", "Satu penanda khas mata kuliah ini terletak pada hubungannya yang rapat dengan penempaan watak. Pengetahuan tentang negara akan kehilangan makna bila tidak disertai sikap jujur dan bertanggung jawab."),
  ("p", "Watak tumbuh dari kebiasaan, bukan dari hafalan. Maka ruang kuliah sebaiknya menjadi tempat berlatih bersikap, bukan sekadar tempat menerima materi."),
 ],
 "2": [
  ("h2", "Sejarah Pembentukan Identitas"),
  ("p", "Jati diri bangsa tumbuh dari pengalaman sejarah yang panjang. Penjajahan yang berkepanjangan justru menumbuhkan kesadaran bahwa beragam suku dan daerah berbagi nasib serupa dan perlu bersatu."),
  ("p", "Peristiwa semacam Kebangkitan Nasional dan Sumpah Pemuda mengukuhkan kesadaran tersebut. Menyelami sejarah membantu mahasiswa menyadari bahwa persatuan ditempa melalui perjuangan panjang, bukan sesuatu yang datang dengan sendirinya."),
  ("h2", "Keberagaman sebagai Kekayaan"),
  ("p", "Indonesia dikaruniai beragam suku, bahasa, dan tradisi. Kemajemukan ini sering dipandang sebagai kendala, padahal justru kekayaan yang langka. Kuncinya terletak pada cara mengelolanya."),
  ("p", "Bila perbedaan dihormati, ia memperkaya kehidupan bersama. Di kampus, mahasiswa bisa menyerap banyak hal dari kawan beda daerah, dari cara berpikir sampai kebiasaan baiknya."),
  ("h2", "Peran Mahasiswa Merawat Identitas"),
  ("p", "Mahasiswa berada pada posisi strategis untuk merawat jati diri bangsa. Sebagai kalangan terpelajar, mereka mampu berpikir kritis sekaligus cukup muda untuk menggerakkan perubahan."),
  ("p", "Perannya dapat berupa memakai bahasa Indonesia dengan baik, memperkenalkan budaya daerah, dan menolak ujaran yang merendahkan kelompok lain. Hal-hal kecil ini menjaga identitas tetap hidup."),
 ],
 "3": [
  ("h2", "Negara Kesatuan sebagai Wujud Integrasi"),
  ("p", "Negara Kesatuan Republik Indonesia adalah bentuk nyata dari integrasi nasional. Ia lebih dari sekadar gagasan, sebab menjelma sebagai realitas politik dan hukum yang dijaga oleh konstitusi berikut ideologi Pancasila."),
  ("p", "Merawat keutuhannya adalah beban bersama segenap rakyat, tidak semata urusan aparat. Setiap warga ikut menentukan apakah persatuan ini bertahan atau merapuh."),
  ("h2", "Mengelola Perbedaan Pendapat"),
  ("p", "Perbedaan pendapat adalah hal yang wajar dalam masyarakat yang sehat. Penentunya bukan hadir atau tidaknya perbedaan, melainkan bagaimana kita menanggapinya. Perbedaan yang dikelola dengan kepala dingin menghasilkan keputusan yang lebih matang."),
  ("p", "Sebaliknya, perbedaan yang disikapi dengan kebencian akan merusak kebersamaan. Mahasiswa perlu terbiasa berdialog dan mencari titik temu, bukan saling menjatuhkan."),
  ("h2", "Solidaritas saat Menghadapi Musibah"),
  ("p", "Rasa sebangsa paling terasa ketika musibah datang. Ketika bencana datang, uluran tangan berdatangan dari banyak penjuru tanpa lagi memperdebatkan asal suku maupun agama. Kesetiakawanan seperti itu menjadi bukti bahwa persatuan masih menyala."),
  ("p", "Mahasiswa dapat ikut ambil bagian lewat penggalangan bantuan dan aksi kemanusiaan. Pengalaman menolong sesama menumbuhkan empati sekaligus mempererat rasa kebersamaan."),
 ],
 "4": [
  ("h2", "Sistem Pemerintahan"),
  ("p", "Indonesia menganut sistem pemerintahan presidensial, dengan presiden sebagai kepala negara sekaligus kepala pemerintahan. Sistem ini menempatkan presiden dan lembaga perwakilan pada kedudukan yang sejajar serta saling mengawasi."),
  ("p", "Pengaturan semacam ini bertujuan menjaga keseimbangan kekuasaan. Tidak ada satu pun lembaga yang boleh berjalan tanpa pengawasan dari lembaga lain."),
  ("h2", "Mekanisme Saling Mengimbangi"),
  ("p", "Pembagian kekuasaan diiringi mekanisme saling mengimbangi. Dewan pembentuk undang-undang mengawasi pemerintah, badan peradilan menilai keabsahan aturan, sedangkan pemerintah menjalankan ketetapan yang telah disepakati."),
  ("p", "Lewat mekanisme ini, setiap lembaga tetap berada pada jalurnya. Begitu satu lembaga berusaha melewati batas, lembaga lainnya dapat meluruskannya."),
  ("h2", "Kesadaran Berkonstitusi"),
  ("p", "Kesadaran berkonstitusi bermakna kerelaan untuk memahami, menaati, dan menjalankan hukum dasar negara. Pada mahasiswa, kesadaran semacam ini dilatih melalui hal sederhana, seperti mematuhi tata tertib kampus serta menyuarakan pendapat dengan santun."),
  ("p", "Andai sebuah kebijakan dinilai berbenturan dengan hak dasar, kritik bisa dilayangkan melalui forum atau tulisan yang beralasan. Sikap ini menunjukkan kesadaran konstitusional yang sehat."),
 ],
 "5": [
  ("h2", "Instrumen HAM Nasional dan Internasional"),
  ("p", "Perlindungan hak asasi diatur baik di tingkat nasional maupun internasional. Pada lingkup global, asasnya dituangkan dalam Deklarasi Universal Hak Asasi Manusia yang disahkan Perserikatan Bangsa-Bangsa tahun 1948."),
  ("p", "Pada lingkup nasional, perangkatnya meliputi Undang-Undang Dasar Tahun 1945 dan Undang-Undang Nomor 39 Tahun 1999, dilengkapi keberadaan Komisi Nasional Hak Asasi Manusia. Keselarasan keduanya menunjukkan bahwa isu kemanusiaan menjadi perhatian bersama."),
  ("h2", "Hak dan Kewajiban dalam Demokrasi"),
  ("p", "Di tengah kehidupan demokrasi, hak dan kewajiban mesti ditimbang secara berimbang. Demokrasi menyediakan ruang menyuarakan pendapat dan menentukan pilihan, namun memerlukan kematangan supaya kebebasan tak berbelok menjadi kekacauan."),
  ("p", "Pada pemilihan umum, misalnya, warga menggenggam hak untuk memilih sekaligus kewajiban menggunakannya dengan penuh tanggung jawab, menolak menjual suara, dan tahan terhadap hasutan. Keseimbangan semacam inilah yang menjaga demokrasi tetap sehat."),
  ("h2", "Tanggung Jawab Sosial"),
  ("p", "Di luar hak dan kewajiban yang digariskan hukum, warga negara memikul pula tanggung jawab sosial. Bentuknya tampak pada kepedulian terhadap lingkungan dan kesediaan membantu sesama."),
  ("p", "Andai tiap orang cuma tenggelam dalam urusannya sendiri, rasa kebersamaan lambat laun menyusut. Mahasiswa bisa menjaganya melalui kegiatan sosial dan kepedulian terhadap masalah di sekelilingnya."),
 ],
 "6": [
  ("h2", "Independensi Peradilan"),
  ("p", "Penegakan hukum yang adil membutuhkan peradilan yang merdeka. Hakim harus bebas dari tekanan agar putusannya berpijak pada fakta dan hukum, bukan pada kepentingan pihak yang kuat."),
  ("p", "Kemandirian itu mesti diiringi pemantauan atas tingkah laku hakim agar tidak berbelok menjadi kesewenang-wenangan. Titik temu antara kemandirian dan pengawasan itulah yang menjaga mutu peradilan."),
  ("h2", "Kepercayaan Publik terhadap Hukum"),
  ("p", "Kepercayaan masyarakat adalah modal berharga yang mudah rusak. Sekali masyarakat menilai hukum tidak adil, kepercayaan itu sukar dipulihkan, dan orang cenderung menempuh jalannya sendiri."),
  ("p", "Mengembalikan kepercayaan menuntut bukti alih-alih janji, yakni penegakan hukum yang ajeg dan tanpa tebang pilih. Partisipasi masyarakat dalam mengawasi turut menjaga wibawa hukum."),
  ("h2", "Peran Mahasiswa dalam Budaya Hukum"),
  ("p", "Mahasiswa dapat membangun budaya hukum dari lingkungan kampus, yaitu dengan menaati aturan akademik dan menolak segala bentuk kecurangan. Kebiasaan kecil ini menjadi fondasi ketaatan pada hukum yang lebih luas."),
  ("p", "Selain itu, mahasiswa dapat menyuarakan keadilan lewat cara yang sah, seperti diskusi yang berbobot dan tulisan yang berdasar. Mengawal hukum tidak sama dengan menghakimi, sebab tujuannya memastikan keadilan tegak secara terbuka."),
 ],
 "7": [
  ("h2", "Demokrasi dan Ketahanan Politik"),
  ("p", "Ketahanan politik bertumpu pada demokrasi yang sehat. Demokrasi memberi ruang bagi rakyat untuk menentukan pemimpin dan mengawasi pemerintahan. Stabilitas politik yang demokratis membuat bangsa lebih tahan terhadap goncangan."),
  ("p", "Sebaliknya, demokrasi yang dibajak kepentingan sempit dapat melemahkan ketahanan. Karena itu, partisipasi warga yang cerdas menjadi penopang penting bagi ketahanan politik."),
  ("h2", "Pemerataan Pembangunan"),
  ("p", "Wawasan nusantara menghendaki pembangunan yang tidak terpusat di perkotaan besar. Kawasan perbatasan beserta pulau terpencil layak memperoleh perhatian agar seluruh warga turut merasakan buah pembangunan."),
  ("p", "Ketika seluruh daerah merasa diperhatikan, rasa keterikatan pada bangsa pun menebal. Pemerataan dengan demikian bukan semata urusan ekonomi, melainkan cara menjaga persatuan dari dalam."),
  ("h2", "Literasi Digital dan Ketahanan Informasi"),
  ("p", "Ancaman terhadap ketahanan kini banyak hadir di ruang digital. Berita yang memecah belah mampu melaju lebih kencang daripada kesanggupan orang memeriksanya."),
  ("p", "Mahasiswa mengambil peran sebagai penapis, yakni menelaah kebenaran sebelum meneruskan dan menahan ucapan yang memanaskan keadaan. Satu sikap tenang sering lebih berguna daripada banyak komentar yang memanaskan."),
 ],
 "8": [
  ("h2", "Otonomi Daerah dan Pengawasannya"),
  ("p", "Otonomi daerah memberi kewenangan kepada daerah untuk mengurus rumah tangganya sendiri. Kewenangan ini mempercepat pembangunan, tetapi membuka pula peluang penyimpangan bila tidak diawasi."),
  ("p", "Karena itu, otonomi daerah harus berjalan seiring dengan tata kelola yang baik. Pengawasan dari lembaga berwenang dan masyarakat mencegah kekuasaan lokal berubah menjadi monopoli."),
  ("h2", "Peran Masyarakat Sipil"),
  ("p", "Masyarakat sipil, seperti lembaga swadaya, pers, dan akademisi, berperan sebagai pengawas sekaligus penghubung. Mereka membantu menjaga agar kebijakan tetap berpihak pada kepentingan publik."),
  ("p", "Peran ini kerap menghadapi hambatan, mulai dari keterbatasan dana sampai tekanan. Meski demikian, keberadaan masyarakat sipil yang aktif menjadi penanda demokrasi yang sehat."),
  ("h2", "Membangun Generasi Berintegritas"),
  ("p", "Tujuan akhir pendidikan antikorupsi ialah hadirnya generasi yang menjunjung integritas. Generasi semacam ini tidak menunggu menjabat untuk menampik korupsi, sebab kejujuran telah dibiasakan sejak masa kuliah."),
  ("p", "Membentuknya menuntut keteladanan dari banyak pihak, mulai dari pengajar yang adil sampai keluarga yang menanam kejujuran. Dari kebiasaan jujur yang dilatih setiap hari, lahir pemimpin masa depan yang bersih."),
 ],
}

_splice(EXTRA2)



# ===================== PENDALAMAN TAHAP 3 =====================
EXTRA3 = {
 "1": [
  ("h2", "Bekal bagi Dunia Kerja"),
  ("p", "Nilai yang ditimba lewat Pendidikan Kewarganegaraan tidak terhenti di dinding ruang kuliah. Kejujuran, kemampuan bekerja sama, dan sikap menghormati aturan adalah bekal yang dibutuhkan di dunia kerja."),
  ("p", "Pihak pemberi kerja umumnya memburu pribadi yang layak dipercaya. Mahasiswa yang lazim mengamalkan nilai kewarganegaraan akan lebih mudah diterima di tempat kerja mana pun."),
  ("h2", "Menjadi Warga Negara yang Aktif"),
  ("p", "Warga yang aktif bukan sekadar menagih hak, melainkan juga rela ambil bagian dalam kehidupan bersama. Bagi mahasiswa, sikap ini dimulai dari menyampaikan aspirasi lewat jalur resmi dan peduli pada persoalan di lingkungannya."),
  ("p", "Keterlibatan semacam ini berlainan dengan sekadar gaduh di media sosial. Warga yang aktif menyertai pendapatnya dengan tindakan, bukan hanya keluhan."),
  ("h2", "Bersikap Kritis terhadap Informasi"),
  ("p", "Kemampuan bersikap kritis menjadi salah satu hasil yang diharapkan dari mata kuliah ini. Mahasiswa diajak menelusuri sumber, mempertimbangkan pandangan lain, lalu menahan diri sebelum menarik kesimpulan."),
  ("p", "Sikap semacam ini menghindarkan seseorang dari peran sebagai penyebar dusta tanpa ia sadari. Di tengah derasnya informasi, kemampuan menyaring menjadi sangat berharga."),
 ],
 "2": [
  ("h2", "Pancasila sebagai Pandangan Hidup"),
  ("p", "Selain dasar negara, Pancasila berkedudukan sebagai pandangan hidup bangsa. Artinya, nilai-nilainya menjadi pedoman dalam menyikapi persoalan sehari-hari, mulai dari cara bermusyawarah sampai cara memperlakukan sesama."),
  ("p", "Sebagai pandangan hidup, Pancasila menuntun warga untuk mengutamakan kebersamaan tanpa mengorbankan keadilan. Nilai ini menjadi penjaga arah di tengah perubahan zaman."),
  ("h2", "Identitas dan Rasa Percaya Diri"),
  ("p", "Mengenali akar budaya sendiri menumbuhkan rasa percaya diri. Seseorang yang paham jati dirinya cenderung lebih kukuh melangkah dan tidak mudah terombang-ambing oleh pengaruh luar."),
  ("p", "Jati diri yang kokoh malah mempermudah seseorang menyerap hal-hal baru tanpa kehilangan pijakan. Ia mampu menyambut kemajuan sambil tetap menggenggam nilai bangsanya."),
  ("h2", "Kampus sebagai Miniatur Bangsa"),
  ("p", "Kehidupan kampus sering disebut Indonesia dalam ukuran kecil. Di sana berkumpul mahasiswa dari beragam daerah dan latar, lalu belajar serta berkegiatan bersama."),
  ("p", "Bila ruang itu dikelola dengan saling menghormati, semboyan Bhinneka Tunggal Ika berubah dari hafalan menjadi pengalaman nyata. Kampus menjadi tempat berlatih hidup berbangsa."),
 ],
 "3": [
  ("h2", "Peran Pendidikan dalam Persatuan"),
  ("p", "Dunia pendidikan memikul peran besar dalam merawat integrasi. Lewat pendidikan, generasi muda mengenal sejarah bangsa, nilai Pancasila, dan bahaya perpecahan."),
  ("p", "Pendidikan turut mengasah cara berkomunikasi yang sehat. Mahasiswa yang lazim bertukar pikiran tanpa menjatuhkan lawan bicara akan menularkan kebiasaan baik itu ke tengah masyarakat."),
  ("h2", "Menyikapi Perbedaan Pilihan"),
  ("p", "Dalam kehidupan bersama, perbedaan pilihan adalah hal biasa, baik dalam organisasi maupun pandangan. Cara bersikap yang matang ialah menghormatinya sepanjang pilihan tersebut tidak menabrak hak orang lain."),
  ("p", "Yang merusak persatuan bukan perbedaan, melainkan cara menyikapinya dengan kebencian. Perbedaan yang disikapi dengan dialog justru memperkaya pertimbangan bersama."),
  ("h2", "Mewaspadai Politik Pecah Belah"),
  ("p", "Salah satu ancaman integrasi adalah upaya memecah belah dengan memainkan isu suku dan agama. Cara ini berbahaya karena menyentuh emosi sebelum sempat dipikirkan dengan jernih."),
  ("p", "Mahasiswa perlu mengenali pola semacam itu agar tidak mudah terprovokasi. Menahan diri dan memeriksa kebenaran adalah langkah sederhana untuk menggagalkannya."),
 ],
 "4": [
  ("h2", "Konstitusi sebagai Pelindung Warga"),
  ("p", "Satu bukti konkret dari hadirnya konstitusi ialah adanya perlindungan bagi warga. Konstitusi memberi jaminan atas keadilan, pendidikan, rasa aman, serta kemerdekaan menyatakan pendapat."),
  ("p", "Perlindungan ini baru efektif bila warga memahami haknya. Banyak orang menanggung ketidakadilan tanpa menyadari bahwa konstitusi sebenarnya melindungi mereka."),
  ("h2", "Pembatasan Kekuasaan"),
  ("p", "Sejarah menunjukkan bahwa kuasa yang dibiarkan tanpa batas cenderung diselewengkan. Karena itu konstitusi menetapkan batas kewenangan setiap pemegang kekuasaan."),
  ("p", "Pembatasan ini diwujudkan lewat pembagian tugas antarlembaga dan mekanisme saling mengawasi. Bagi warga, batas itu sekaligus menjadi pelindung dari tindakan sewenang-wenang."),
  ("h2", "Aturan yang Tersusun Berjenjang"),
  ("p", "Aturan di Indonesia tersusun bertingkat, dengan Undang-Undang Dasar Tahun 1945 pada puncaknya. Ketentuan yang berkedudukan lebih rendah dilarang berseberangan dengan yang lebih tinggi."),
  ("p", "Susunan ini menjaga ketertiban hukum agar tidak tumpang tindih. Andai sebuah aturan dianggap melenceng dari konstitusi, ada mekanisme pengujian melalui lembaga peradilan."),
 ],
 "5": [
  ("h2", "Kebebasan Berpendapat yang Bertanggung Jawab"),
  ("p", "Kebebasan berpendapat termasuk hak yang penting dalam demokrasi, tetapi bukan tanpa batas. Pendapat apa pun tetap wajib menghargai hak sesama serta menjauhi penyebaran kebencian maupun kebohongan."),
  ("p", "Di lingkungan kampus, kebebasan itu terlihat saat mahasiswa menyampaikan kritik atas kebijakan lewat forum yang semestinya. Kritik yang berbasis data dan disampaikan dengan santun lebih mudah diterima ketimbang yang dilemparkan dengan amarah."),
  ("h2", "Hak atas Pendidikan"),
  ("p", "Pendidikan termasuk hak yang mendasar karena membuka kesempatan seseorang memperbaiki hidupnya. Tanpa jalan menuju pendidikan, beragam hak lain pun ikut sukar dicapai."),
  ("p", "Menyadari hal ini, mahasiswa yang beruntung menempuh pendidikan tinggi sebaiknya tidak menyia-nyiakannya. Menuntut ilmu dengan sepenuh hati merupakan cara menghormati hak yang belum tentu dimiliki setiap orang."),
  ("h2", "Menjaga Privasi Orang Lain"),
  ("p", "Salah satu cara menghormati hak pada era digital adalah menjaga ranah pribadi. Menyebarkan foto, obrolan, atau data milik orang lain tanpa persetujuan tergolong pelanggaran yang kerap diremehkan, padahal akibatnya berat."),
  ("p", "Menjaga privasi berarti meminta izin sebelum membagikan milik orang lain dan menahan rasa ingin tahu yang berlebihan. Sikap ini adalah wujud nyata menghargai sesama."),
 ],
 "6": [
  ("h2", "Hukum yang Memihak Kebenaran"),
  ("p", "Hukum yang baik selalu memihak kebenaran serta keadilan, bukan kekuatan atau kekuasaan. Ketika ditegakkan secara jujur, hukum membuat masyarakat merasa aman."),
  ("p", "Mewujudkannya membutuhkan aparat berintegritas sekaligus warga yang turut mengawasi. Mahasiswa berperan lewat penolakan atas segala rupa suap, sekecil apa pun nilainya, pada keseharian."),
  ("h2", "Kesadaran Hukum dari Hal Kecil"),
  ("p", "Kesadaran hukum tak harus berawal dari kejadian besar. Ia tumbuh dari kebiasaan sehari-hari, seperti tertib di jalan, mengembalikan barang yang bukan haknya, dan menjauhi kebiasaan menyontek."),
  ("p", "Berlaku jujur saat tak ada yang mengawasi merupakan ujian sejati bagi kesadaran hukum. Justru kebiasaan kecil semacam inilah yang menyusun budaya hukum dalam rentang panjang."),
  ("h2", "Edukasi Hukum bagi Masyarakat"),
  ("p", "Banyak warga tidak tahu cara memperjuangkan haknya karena minimnya informasi hukum. Penyuluhan yang mudah dicerna mampu menambal kekosongan itu, sehingga warga mengerti ke mana mesti melapor."),
  ("p", "Kampus bisa mengambil peran melalui pengabdian, contohnya menyuluh soal hak dasar atau perlindungan data pribadi. Dengan cara ini, ilmu yang dipelajari menjadi manfaat nyata bagi masyarakat."),
 ],
 "7": [
  ("h2", "Cinta Tanah Air dalam Tindakan"),
  ("p", "Cinta tanah air tidak harus diwujudkan lewat hal besar. Ia dapat hadir dalam perbuatan sederhana, seperti memakai produk dalam negeri, menjaga kebersihan lingkungan, dan tekun belajar."),
  ("p", "Untuk mahasiswa, meraih prestasi sambil memegang integritas merupakan wujud cinta tanah air yang konkret. Dengan menjadi pribadi berkualitas, seseorang turut memperkuat bangsanya."),
  ("h2", "Menjaga Lingkungan sebagai Bela Negara"),
  ("p", "Menjaga lingkungan hidup termasuk bentuk bela negara, sebab kelestarian alam menyangkut keberlangsungan bangsa. Hutan, sungai, beserta laut yang lestari menjadi warisan berharga untuk anak cucu kelak."),
  ("p", "Mahasiswa bisa menyumbang lewat kebiasaan sederhana, misalnya menekan timbunan sampah dan turut dalam gerakan pelestarian. Tindakan kecil yang dilakukan banyak orang membawa dampak besar."),
  ("h2", "Ketahanan Diri menghadapi Tekanan"),
  ("p", "Ketahanan nasional pada lingkup paling kecil dimulai dari ketahanan diri. Mahasiswa yang mampu mengelola tekanan dan tetap berpikir jernih turut menyumbang pada kekuatan bangsa."),
  ("p", "Kesanggupan membantu sesama supaya kuat menahan tekanan pun tergolong bentuk ketahanan sosial. Lingkungan yang saling menguatkan akan melahirkan pribadi yang tangguh."),
 ],
 "8": [
  ("h2", "Korupsi dalam Keseharian"),
  ("p", "Korupsi kerap dikira hanya ulah pembesar, padahal benihnya justru tumbuh di urusan sehari-hari. Menyontek, menitip tanda tangan kehadiran, atau mengakali laporan kegiatan mencerminkan sikap tidak jujur."),
  ("p", "Jika diremehkan, kebiasaan tersebut bisa membesar menjadi penyimpangan serius tatkala seseorang menggenggam wewenang. Karena itu, kejujuran dalam hal kecil adalah latihan paling nyata membangun integritas."),
  ("h2", "Keberanian Menolak Ajakan Curang"),
  ("p", "Menolak korupsi menuntut keberanian, sebab godaan sering datang dari lingkungan sendiri. Mengucapkan penolakan atas ajakan menyontek atau berlaku curang adakalanya terasa berat."),
  ("p", "Keberanian moral tak selalu mewujud dalam tindakan besar. Berani berkata jujur kendati merugikan diri sendiri serta sigap melaporkan kejanggalan merupakan bentuk keberanian yang menempa karakter."),
  ("h2", "Pemerintahan yang Terbuka"),
  ("p", "Pemerintahan yang terbuka menjadi salah satu kunci mencegah korupsi. Keterbukaan informasi membuat masyarakat dapat ikut mengawasi penggunaan anggaran dan jalannya kebijakan."),
  ("p", "Kemajuan teknologi mempermudah keterbukaan ini melalui layanan berbasis daring. Semakin terbuka sebuah pemerintahan, semakin sempit ruang gerak penyimpangan."),
 ],
}

_splice(EXTRA3)



# ===================== PENDALAMAN TAHAP 4 (menuju sasaran 62-66) =====================
EXTRA4 = {
 "1": [
  ("h2", "Empat Pilar Kebangsaan"),
  ("p", "Kehidupan berbangsa di Indonesia bertumpu pada empat pilar, yaitu Pancasila, Undang-Undang Dasar Tahun 1945, Negara Kesatuan Republik Indonesia, dan Bhinneka Tunggal Ika. Keempatnya saling menguatkan dalam menjaga keutuhan bangsa."),
  ("p", "Pendidikan Kewarganegaraan membantu mahasiswa memahami keterkaitan keempat pilar tersebut. Pemahaman ini penting agar kecintaan pada bangsa berpijak pada dasar yang jelas, bukan sekadar perasaan sesaat."),
  ("h2", "Mahasiswa dan Perubahan Sosial"),
  ("p", "Sepanjang sejarah, mahasiswa kerap menjadi penggerak perubahan sosial. Posisi mereka sebagai kalangan terpelajar memberi ruang untuk menyuarakan persoalan masyarakat secara kritis dan tertib."),
  ("p", "Peran ini menuntut tanggung jawab. Kritik yang disampaikan sebaiknya berdasar dan disertai usulan jalan keluar, bukan sekadar menyalahkan tanpa solusi."),
  ("h2", "Belajar Berdemokrasi di Ruang Kelas"),
  ("p", "Ruang kelas adalah tempat pertama mahasiswa berlatih berdemokrasi. Ketika mereka menghargai pendapat berbeda dan menerima keputusan bersama, mereka sedang mempraktikkan nilai demokrasi dalam skala kecil."),
  ("p", "Kebiasaan ini terbawa ke kehidupan yang lebih luas. Demokrasi yang sehat di masyarakat berakar dari kebiasaan menghargai perbedaan yang ditanam sejak bangku kuliah."),
 ],
 "2": [
  ("h2", "Lambang Garuda dan Maknanya"),
  ("p", "Garuda Pancasila bukan sekadar gambar burung, melainkan lambang yang sarat makna. Pada perisainya termuat simbol kelima sila, sedangkan semboyan Bhinneka Tunggal Ika tertulis pada pita yang dicengkeramnya."),
  ("p", "Memahami makna lambang ini menumbuhkan penghormatan yang lebih dalam. Lambang negara menjadi pengingat akan nilai yang harus dijaga, bukan sekadar atribut resmi."),
  ("h2", "Lagu Kebangsaan dan Semangat Sumpah Pemuda"),
  ("p", "Lagu Indonesia Raya terlahir dari semangat persatuan yang serupa dengan Sumpah Pemuda. Keduanya meneguhkan ikrar persatuan, yakni bertanah air satu, berbangsa satu, dan menjunjung bahasa yang satu."),
  ("p", "Menyanyikan lagu kebangsaan dengan khidmat adalah cara sederhana merawat semangat itu. Di balik liriknya tersimpan harapan akan bangsa yang merdeka dan bersatu."),
  ("h2", "Globalisasi dan Budaya Lokal"),
  ("p", "Globalisasi membuat budaya dari berbagai penjuru dunia mudah saling bertemu. Tantangannya adalah menjaga agar budaya lokal tidak tergerus dan tetap dihargai oleh pemiliknya sendiri."),
  ("p", "Sikap yang sehat bukan menolak globalisasi, melainkan menyaringnya. Budaya lokal bahkan bisa diperkenalkan ke dunia bila dikemas dengan kreatif melalui teknologi."),
 ],
 "3": [
  ("h2", "Kerukunan Antarumat Beragama"),
  ("p", "Indonesia dihuni pemeluk beragam agama yang hidup berdampingan. Kerukunan antarumat beragama menjadi syarat penting bagi integrasi, sebab gesekan keagamaan mudah memantik konflik yang luas."),
  ("p", "Kerukunan dijaga lewat sikap saling menghormati ibadah dan keyakinan masing-masing. Di kampus, hal ini tampak dari kesediaan bekerja sama tanpa mempersoalkan perbedaan agama."),
  ("h2", "Menyelesaikan Konflik Sosial"),
  ("p", "Konflik sosial dapat muncul dari kesalahpahaman, ketimpangan, atau hasutan. Yang menentukan bukan ada atau tidaknya konflik, melainkan cara menyelesaikannya secara damai."),
  ("p", "Dialog, mediasi, dan kesediaan mendengar menjadi jalan untuk meredakan ketegangan. Mahasiswa dapat berperan sebagai penengah yang menenangkan, bukan penambah keruh suasana."),
  ("h2", "Peran Pemuda Lintas Zaman"),
  ("p", "Dari masa ke masa, pemuda selalu memiliki peran dalam menjaga persatuan. Pada masa perjuangan, mereka menyatukan tekad kemerdekaan; pada masa kini, mereka menjaga persatuan di ruang nyata maupun digital."),
  ("p", "Peran ini menuntut kesadaran bahwa persatuan tidak diwariskan secara otomatis. Setiap generasi perlu merawatnya dengan caranya sendiri sesuai tantangan zamannya."),
 ],
 "4": [
  ("h2", "Hak dan Kewajiban dalam Undang-Undang Dasar"),
  ("p", "Undang-Undang Dasar Tahun 1945 bukan hanya menata lembaga negara, melainkan juga menjamin hak sekaligus menetapkan kewajiban warga. Hak yang dijamin mencakup pendidikan, pekerjaan yang layak, dan perlindungan hukum."),
  ("p", "Di sisi lain, warga berkewajiban menaati hukum dan menghormati hak orang lain. Hak dan kewajiban ini berjalan seiring sebagai pilar masyarakat yang adil."),
  ("h2", "Lembaga Negara yang Mandiri"),
  ("p", "Selain tiga cabang kekuasaan utama, terdapat lembaga negara yang bersifat mandiri, seperti lembaga pemilihan umum dan lembaga pengawas keuangan. Kemandirian ini menjaga agar tugasnya bebas dari tekanan kepentingan."),
  ("p", "Keberadaan lembaga mandiri memperkuat pengawasan dalam negara. Mereka menjadi penyeimbang tambahan agar kekuasaan tetap terkendali."),
  ("h2", "Hubungan Pemerintah Pusat dan Daerah"),
  ("p", "Konstitusi mengatur pembagian urusan antara pemerintah pusat dan daerah. Sebagian urusan dipegang pusat, sebagian diserahkan kepada daerah agar pelayanan lebih dekat dengan masyarakat."),
  ("p", "Hubungan ini menuntut keselarasan. Kewenangan daerah perlu diiringi tanggung jawab dan pengawasan agar tujuan bernegara tetap terjaga."),
 ],
 "5": [
  ("h2", "Kewajiban Menaati Hukum"),
  ("p", "Salah satu kewajiban pokok warga negara adalah menaati hukum. Ketaatan ini menjaga ketertiban dan melindungi hak setiap orang dari tindakan sewenang-wenang."),
  ("p", "Menaati hukum bukan berarti tunduk tanpa sikap. Warga tetap dapat mengkritik aturan yang dinilai keliru, tetapi lewat jalur yang sah, bukan dengan melanggarnya."),
  ("h2", "Hak Memperoleh Keadilan"),
  ("p", "Setiap warga berhak memperoleh perlakuan adil di hadapan hukum. Hak ini menuntut proses yang terbuka, kesempatan membela diri, dan putusan yang berdasarkan bukti."),
  ("p", "Hak atas keadilan baru bermakna bila dapat dijangkau semua orang. Karena itu, kemudahan akses terhadap bantuan hukum menjadi bagian penting dari penghormatan hak ini."),
  ("h2", "Menghargai Pendapat yang Berbeda"),
  ("p", "Menghargai pendapat yang berbeda adalah tanda kedewasaan berwarganegara. Kebebasan diri berhenti pada titik kebebasan orang lain dimulai."),
  ("p", "Di kampus, sikap tersebut tampak ketika mahasiswa memberi ruang bicara bagi temannya dan menahan diri dari memaksakan kemauan. Kebiasaan kecil ini menyiapkan seseorang hidup dalam masyarakat yang beragam."),
 ],
 "6": [
  ("h2", "Korupsi sebagai Musuh Keadilan"),
  ("p", "Korupsi merusak penegakan hukum karena membuat keadilan dapat dibeli. Ketika hukum tunduk pada uang, yang lemah semakin tersisih dan kepercayaan publik runtuh."),
  ("p", "Melawan korupsi karena itu menjadi bagian dari menegakkan keadilan. Hukum yang bersih adalah syarat agar setiap warga memperoleh perlakuan yang setara."),
  ("h2", "Peradilan yang Terbuka"),
  ("p", "Peradilan yang terbuka memberi ruang bagi masyarakat untuk mengawasi jalannya perkara. Keterbukaan tersebut memastikan keadilan bukan saja ditegakkan, melainkan juga tampak ditegakkan."),
  ("p", "Pengawasan publik yang sehat dilakukan berdasarkan fakta, bukan tekanan massa. Mahasiswa dapat ikut mengawal dengan sikap kritis yang bertanggung jawab."),
  ("h2", "Bantuan Hukum bagi yang Lemah"),
  ("p", "Tidak semua orang mampu membiayai pendampingan hukum. Bantuan hukum bagi warga yang lemah secara ekonomi menjadi penanda bahwa keadilan benar-benar untuk semua."),
  ("p", "Negara dan masyarakat dapat berperan menyediakan layanan ini. Kampus pun bisa membantu melalui kegiatan pengabdian yang mendekatkan akses keadilan kepada warga."),
 ],
 "7": [
  ("h2", "Astagatra dan Keseimbangan"),
  ("p", "Ketahanan nasional sering digambarkan melalui konsep yang memadukan aspek alamiah dan aspek sosial. Aspek alamiah mencakup wilayah dan kekayaan alam, sedangkan aspek sosial mencakup ideologi, politik, ekonomi, sosial budaya, serta pertahanan."),
  ("p", "Pelajaran dari konsep ini adalah pentingnya keseimbangan. Bangsa yang kuat di satu sisi tetapi lemah di sisi lain tetap rapuh, sehingga semua aspek perlu dibangun bersama."),
  ("h2", "Ancaman Nonmiliter"),
  ("p", "Ancaman terhadap bangsa kini banyak berbentuk nonmiliter, seperti penyebaran kabar bohong, kejahatan siber, dan perpecahan akibat hasutan. Ancaman semacam ini sulit dilihat namun nyata dampaknya."),
  ("p", "Menghadapinya menuntut kesadaran dan literasi, bukan sekadar kekuatan fisik. Masyarakat yang cerdas menyaring informasi menjadi benteng pertama bagi ketahanan bangsa."),
  ("h2", "Kerja Sama Antarbangsa"),
  ("p", "Geostrategi juga diwujudkan lewat kerja sama dengan bangsa lain. Hubungan yang saling menghormati membantu menjaga kedaulatan sekaligus membuka peluang kemajuan bersama."),
  ("p", "Indonesia menempuh jalur kerja sama yang menjunjung perdamaian. Sikap ini sejalan dengan cita-cita ikut menjaga ketertiban dunia yang termuat dalam Pembukaan Undang-Undang Dasar Tahun 1945."),
 ],
 "8": [
  ("h2", "Indikator Tata Kelola yang Baik"),
  ("p", "Kualitas tata kelola dapat diukur lewat sejumlah penanda, seperti tingkat layanan publik, keterbukaan anggaran, dan rendahnya praktik korupsi. Penanda ini membantu menilai apakah pemerintahan berjalan sehat."),
  ("p", "Penilaian semacam ini penting agar perbaikan berjalan terarah. Tanpa ukuran yang jelas, upaya membenahi tata kelola mudah kehilangan arah."),
  ("h2", "Korupsi dan Pelayanan Publik"),
  ("p", "Korupsi paling terasa dampaknya pada pelayanan publik. Ketika dana diselewengkan, layanan kesehatan, pendidikan, dan infrastruktur menjadi buruk, dan rakyat kecil yang paling dirugikan."),
  ("p", "Memperbaiki pelayanan publik karena itu berkaitan erat dengan memberantas korupsi. Pelayanan yang sederhana dan terbuka mempersempit ruang bagi pungutan yang tidak semestinya."),
  ("h2", "Mahasiswa sebagai Pengawas"),
  ("p", "Mahasiswa dapat berperan sebagai pengawas yang kritis dan objektif terhadap kebijakan publik. Pengawasan ini dilakukan berdasarkan data, bukan sekadar prasangka."),
  ("p", "Selain mengawasi, mahasiswa perlu menjadi teladan integritas dari lingkungan kampus. Sikap jujur dalam hal kecil memberi bobot pada setiap kritik yang disuarakan."),
 ],
}

_splice(EXTRA4)



# ===================== PENDALAMAN TAHAP 5 (top-up) =====================
EXTRA5 = {
 "1": [
  ("h2", "Watak Warga Negara"),
  ("p", "Selain pengetahuan dan keterampilan, Pendidikan Kewarganegaraan menekankan watak. Watak warga negara mencakup kejujuran, kepedulian, dan kesediaan menaati aturan yang disepakati bersama."),
  ("p", "Watak tidak dapat dibentuk hanya lewat ceramah, melainkan lewat kebiasaan. Karena itu, latihan bersikap di kampus sama pentingnya dengan penguasaan materi."),
 ],
 "2": [
  ("h2", "Menghargai Jasa Pahlawan"),
  ("p", "Kemerdekaan yang dinikmati saat ini adalah hasil perjuangan para pahlawan. Menghargai jasa mereka merupakan bagian dari merawat identitas nasional."),
  ("p", "Penghargaan itu tidak cukup lewat upacara. Ia diwujudkan dengan mengisi kemerdekaan secara bermakna, seperti belajar sungguh-sungguh dan menjaga persatuan."),
 ],
 "3": [
  ("h2", "Toleransi sebagai Kebiasaan"),
  ("p", "Toleransi akan kokoh bila menjadi kebiasaan, bukan sekadar ucapan. Membiasakan diri menghormati perbedaan dalam pergaulan sehari-hari membuat sikap toleran tumbuh secara alami."),
  ("p", "Kebiasaan ini melatih kepekaan terhadap perasaan orang lain. Dari sanalah lahir masyarakat yang mampu hidup berdampingan secara damai."),
 ],
 "4": [
  ("h2", "Membaca Konstitusi secara Langsung"),
  ("p", "Satu kebiasaan baik yang patut ditiru mahasiswa ialah menyimak naskah konstitusi langsung, alih-alih bergantung pada ringkasan buatan orang lain. Dengan begitu, pemahaman menjadi utuh dan tidak mudah disesatkan."),
  ("p", "Naskah Undang-Undang Dasar Tahun 1945 kini mudah dijangkau lewat sumber resmi. Terbiasa menengok sumber asli mengasah daya kritis sekaligus rasa hormat pada aturan dasar negara."),
 ],
 "5": [
  ("h2", "Hak Asasi dan Martabat Manusia"),
  ("p", "Inti dari hak asasi manusia adalah pengakuan atas martabat setiap orang. Karena martabat itu melekat sejak lahir, tidak seorang pun boleh merampasnya secara sewenang-wenang."),
  ("p", "Menghormati martabat manusia berarti memperlakukan orang lain secara adil tanpa memandang latar belakangnya. Sikap ini menjadi dasar bagi hubungan yang sehat di masyarakat."),
 ],
 "6": [
  ("h2", "Tertib sebagai Cermin Kesadaran Hukum"),
  ("p", "Kesadaran hukum tercermin pada hal-hal yang tampak sederhana, seperti tertib mengantre dan mematuhi rambu. Kebiasaan tertib menunjukkan bahwa seseorang menghargai hak orang lain dan aturan bersama."),
  ("p", "Bila kebiasaan tertib menyebar, kehidupan masyarakat menjadi lebih nyaman dan adil. Hal kecil ini sebenarnya merupakan wujud nyata budaya hukum yang sehat."),
 ],
 "7": [
  ("h2", "Wawasan Nusantara di Ruang Digital"),
  ("p", "Ruang digital kini menjadi medan baru bagi wawasan nusantara. Konten yang menebar kebencian antardaerah atau suku dapat mengikis rasa persatuan dengan cepat."),
  ("p", "Mahasiswa dapat merawat wawasan nusantara dengan menyebarkan konten yang menyejukkan dan memperkenalkan kekayaan daerah. Sikap ini menjaga persatuan di tempat orang kini paling banyak berinteraksi."),
 ],
 "8": [
  ("h2", "Integritas sebagai Gaya Hidup"),
  ("p", "Integritas akan bertahan bila dijadikan gaya hidup, bukan sikap sesaat. Seseorang yang lurus dalam urusan kecil cenderung tetap lurus tatkala dipercaya mengemban amanah besar."),
  ("p", "Menjadikan integritas sebagai gaya hidup menuntut konsistensi. Dari konsistensi itulah lahir pribadi yang sulit digoyahkan oleh godaan menyimpang di kemudian hari."),
 ],
}

_splice(EXTRA5)
