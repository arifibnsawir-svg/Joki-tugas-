# -*- coding: utf-8 -*-
"""
Konten Laporan Wawancara dengan Helper Pemberi Layanan.
Mata kuliah: Pengembangan Profesi Konseling.
Satu laporan kelompok (4 mahasiswa), 4 helper, instrumen 15 pertanyaan berbasis RPS.

Aturan gaya (humanizer): tanpa em-dash, tanpa en-dash sebagai tanda baca,
tanpa kutip keriting, tanpa emoji. Bahasa baku, alami, tidak kaku.

Blok konten: ('p', teks) | ('h2', teks) | ('h3', teks) |
             ('num', [item, ...]) | ('table', {'judul','head','rows'})
"""

# =====================================================================
# IDENTITAS HALAMAN JUDUL
# =====================================================================
IDENTITAS = {
    "judul": "LAPORAN WAWANCARA DENGAN HELPER PEMBERI LAYANAN",
    "subjudul": ("Telaah Karakteristik dan Peran Helper pada Empat Bidang Layanan "
                 "dalam Perspektif Pengembangan Profesi Konseling"),
    "matakuliah": "Pengembangan Profesi Konseling",
    "dosen": "Burju Ruth, M.Pd., Kons.",
    "penyusun": [
        ("Nurul Syifa", "202501500526"),
        ("Lidya Ellen Febriasalsa", "202501500538"),
        ("Balqis Sandra Lejla", "202501500525"),
        ("Devia Zahra", "202501500511"),
    ],
    "prodi": "Program Studi Bimbingan dan Konseling",
    "fakultas": "Fakultas Ilmu Pendidikan dan Pengetahuan Sosial",
    "universitas": "Universitas Indraprasta PGRI",
    "tahun": "2026",
}

# =====================================================================
# KATA PENGANTAR
# =====================================================================
KATA_PENGANTAR = [
    "Puji syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas rahmat dan karunia-Nya sehingga laporan yang berjudul \"Laporan Wawancara dengan Helper Pemberi Layanan\" ini dapat kami selesaikan dengan baik. Laporan ini disusun untuk memenuhi tugas mata kuliah Pengembangan Profesi Konseling pada Program Studi Bimbingan dan Konseling, Fakultas Ilmu Pendidikan dan Pengetahuan Sosial, Universitas Indraprasta PGRI.",
    "Penyusunan laporan ini bertujuan untuk memahami secara langsung pengalaman para helper atau pemberi layanan bantuan di lapangan. Kami melakukan wawancara terhadap empat narasumber dari bidang yang berbeda, yaitu anggota TNI Angkatan Darat, petugas pemadam kebakaran, bidan, dan guru bimbingan dan konseling. Melalui kegiatan ini kami berusaha melihat benang merah antara praktik membantu di berbagai profesi dengan konsep helper yang dipelajari dalam ilmu bimbingan dan konseling.",
    "Kami menyadari bahwa kegiatan wawancara dan penulisan laporan ini tidak akan terlaksana tanpa bantuan banyak pihak. Oleh karena itu, kami mengucapkan terima kasih kepada Ibu Burju Ruth, M.Pd., Kons. selaku dosen pengampu yang telah membimbing kami, kepada keempat narasumber yang telah meluangkan waktu dan berbagi pengalaman, serta kepada rekan-rekan dan keluarga yang telah memberikan dukungan selama proses penyusunan.",
    "Kami menyadari laporan ini masih memiliki kekurangan. Oleh sebab itu, kritik dan saran yang membangun sangat kami harapkan demi penyempurnaan pada penulisan berikutnya. Semoga laporan ini bermanfaat bagi pembaca, khususnya bagi mahasiswa bimbingan dan konseling yang sedang mendalami profesi membantu.",
    "Jakarta, 2026",
    "Tim Penyusun",
]

# =====================================================================
# DAFTAR 15 PERTANYAAN (INSTRUMEN, BERBASIS RPS)
# =====================================================================
PERTANYAAN = [
    "Apa makna profesi Bapak/Ibu dan apa peran utamanya dalam memberikan pelayanan kepada masyarakat?",
    "Bagaimana perkembangan profesi ini sejak awal Bapak/Ibu bekerja hingga sekarang?",
    "Kompetensi atau keterampilan apa yang paling penting untuk memberikan pelayanan yang berkualitas?",
    "Bagaimana peran organisasi atau asosiasi profesi dalam meningkatkan profesionalisme Bapak/Ibu?",
    "Adakah situasi yang menuntut penerapan kode etik profesi, dan bagaimana Bapak/Ibu menyikapinya?",
    "Isu atau permasalahan apa yang paling sering dihadapi saat memberikan pelayanan?",
    "Seberapa penting pengakuan kompetensi resmi seperti sertifikasi bagi mutu dan keamanan layanan?",
    "Bagaimana Bapak/Ibu menerapkan pelayanan yang berpusat pada masyarakat atau klien?",
    "Apa tugas pokok yang paling sering dilakukan dan bagaimana memastikan tetap sesuai kewenangan?",
    "Apa peluang terbesar dan tantangan terbesar profesi ini di masa depan?",
    "Apa pengalaman yang paling berkesan selama Bapak/Ibu menjalankan profesi ini?",
    "Bagaimana cara Bapak/Ibu berkomunikasi dengan masyarakat, termasuk menenangkan orang yang sedang panik?",
    "Bagaimana kerja sama tim antar-petugas berjalan dalam memberikan layanan?",
    "Bagaimana pengaruh pandemi Covid-19 terhadap pelayanan yang Bapak/Ibu berikan?",
    "Apa motivasi yang membuat Bapak/Ibu bertahan menjalankan profesi ini hingga kini?",
]

# =====================================================================
# BAB I PENDAHULUAN
# =====================================================================
BAB1 = {
    "no": "I", "judul": "PENDAHULUAN",
    "isi": [
        ("h2", "1.1 Latar Belakang"),
        ("p", "Profesi konseling merupakan salah satu profesi yang berperan penting dalam membantu individu mengatasi berbagai permasalahan kehidupan. Dalam praktiknya, layanan bantuan tidak hanya diberikan oleh konselor profesional, tetapi juga oleh berbagai pihak lain yang dalam keseharian disebut helper. Guru bimbingan dan konseling, tenaga kesehatan, aparat keamanan, hingga petugas penyelamatan adalah contoh pihak yang setiap hari berhadapan dengan orang lain dalam situasi yang menuntut kepedulian, ketenangan, dan kemampuan menolong."),
        ("p", "Bagi mahasiswa bimbingan dan konseling, memahami sosok helper bukan sekadar mengenal pekerjaan orang lain. Konsep helper adalah inti dari ilmu yang kami pelajari. Prayitno dan Amti (2004) menegaskan bahwa bimbingan adalah proses pemberian bantuan oleh orang yang ahli kepada individu agar yang dibantu mampu mengembangkan diri dan mandiri. Dari rumusan ini terlihat bahwa kegiatan membantu memiliki landasan, tujuan, dan keterampilan tertentu yang dapat ditemukan pula pada profesi di luar konseling."),
        ("p", "Mata kuliah Pengembangan Profesi Konseling mengajak mahasiswa menelaah bagaimana sebuah profesi tumbuh, diatur oleh kode etik, didukung organisasi profesi, dan dijaga mutunya melalui kredensial. Untuk mendekatkan teori dengan kenyataan, kami memilih cara yang sederhana namun bermakna, yaitu mewawancarai langsung empat helper dari bidang yang berbeda. Keempatnya adalah anggota TNI Angkatan Darat, petugas pemadam kebakaran, bidan, dan guru bimbingan dan konseling. Perbedaan latar tugas ini sengaja kami pilih agar kami dapat melihat keterampilan membantu yang bersifat universal sekaligus yang bersifat khas pada tiap bidang."),
        ("p", "Kegiatan wawancara juga penting karena banyak hal dalam profesi membantu tidak dapat dipahami hanya melalui buku. Pengalaman menenangkan orang yang panik, menjaga kerahasiaan, menghadapi tekanan di lapangan, atau bertahan dengan motivasi yang kuat adalah hal yang lebih hidup ketika diceritakan oleh pelakunya. Oleh karena itu, laporan ini berupaya merekam pengalaman nyata para helper dan membacanya kembali dengan kacamata teori konseling."),

        ("h2", "1.2 Tujuan"),
        ("p", "Secara umum kegiatan wawancara ini bertujuan untuk memahami praktik nyata profesi membantu dari sudut pandang para helper di lapangan. Secara khusus, tujuan kegiatan ini diuraikan sebagai berikut."),
        ("num", [
            "Mengetahui peran helper dalam memberikan layanan bantuan kepada masyarakat.",
            "Memahami pengalaman helper dalam menangani klien atau masyarakat yang dilayani.",
            "Mengidentifikasi keterampilan yang dibutuhkan dalam profesi membantu.",
            "Mengetahui tantangan yang dihadapi helper dalam memberikan layanan.",
            "Mengaitkan temuan lapangan dengan teori karakteristik dan peran helper dalam bimbingan dan konseling.",
        ]),

        ("h2", "1.3 Manfaat"),
        ("h3", "1.3.1 Manfaat Teoretis"),
        ("p", "Laporan ini diharapkan menambah wawasan tentang praktik profesi membantu dan memperkaya pemahaman mengenai konsep helper dalam ilmu bimbingan dan konseling. Hasil kajian juga dapat menjadi bahan pembanding antara teori karakteristik helper yang dikemukakan para ahli dengan kenyataan di berbagai bidang layanan."),
        ("h3", "1.3.2 Manfaat Praktis"),
        ("p", "Bagi mahasiswa, kegiatan ini memberikan pengalaman langsung dalam memahami profesi helper sekaligus melatih keterampilan wawancara dan penulisan laporan. Bagi pembaca yang lebih luas, laporan ini diharapkan menumbuhkan kesadaran bahwa keterampilan membantu seperti mendengarkan, berempati, dan menjaga kepercayaan dibutuhkan di banyak bidang pekerjaan, tidak terbatas pada ruang konseling."),
    ],
}

# =====================================================================
# BAB II LANDASAN TEORI
# =====================================================================
BAB2 = {
    "no": "II", "judul": "LANDASAN TEORI",
    "isi": [
        ("h2", "2.1 Pengertian Helper"),
        ("p", "Istilah helper secara sederhana dapat diartikan sebagai orang yang memberikan bantuan kepada orang lain agar mampu menghadapi atau menyelesaikan persoalan yang dihadapinya. Dalam konteks bimbingan dan konseling, helper adalah pihak yang terlibat dalam hubungan membantu, baik secara formal sebagai konselor maupun secara lebih luas sebagai siapa pun yang menjalankan peran menolong."),
        ("p", "Brammer dan MacDonald (2003) menjelaskan bahwa hubungan membantu pada dasarnya adalah proses ketika seseorang menolong orang lain untuk tumbuh ke arah tujuan pribadinya dan memperkuat kemampuannya menghadapi kehidupan. Dari pandangan ini, helper tidak menggantikan peran orang yang dibantu, melainkan mendampingi agar yang bersangkutan mampu menolong dirinya sendiri. Hubungan membantu karena itu bersifat memberdayakan, bukan menciptakan ketergantungan."),
        ("p", "Dalam khazanah keilmuan di Indonesia, Prayitno dan Amti (2004) memandang bantuan sebagai proses yang dilakukan oleh orang yang ahli agar individu dapat mengembangkan dirinya dan mandiri berdasarkan norma yang berlaku. Sejalan dengan itu, Willis (2013) menekankan bahwa konseling merupakan upaya membantu individu melalui hubungan yang bersifat profesional. Lubis (2011) juga menegaskan bahwa keberhasilan bantuan banyak ditentukan oleh kualitas pribadi pemberi bantuan, bukan sekadar teknik yang dikuasainya. Berdasarkan beberapa pandangan tersebut dapat disimpulkan bahwa helper adalah individu yang melalui hubungan yang penuh kepedulian membantu orang lain agar tumbuh, mandiri, dan mampu mengatasi persoalannya."),

        ("h2", "2.2 Karakteristik Helper yang Efektif"),
        ("p", "Tidak semua orang yang menolong dapat disebut helper yang efektif. Para ahli telah merumuskan sejumlah karakteristik atau kualitas pribadi yang membuat bantuan menjadi bermakna. Tiga rujukan utama yang sering dipakai adalah pandangan Carl Rogers, Gerald Corey, dan Lawrence Brammer."),
        ("h3", "2.2.1 Pandangan Carl Rogers"),
        ("p", "Rogers (1961) melalui pendekatan yang berpusat pada pribadi merumuskan tiga sikap inti yang harus dimiliki seorang helper. Pertama, kongruensi atau keselarasan, yaitu helper bersikap jujur dan apa adanya, tidak berpura-pura di hadapan orang yang dibantu. Kedua, penerimaan positif tanpa syarat, yaitu menerima dan menghargai orang yang dibantu tanpa menilai atau menghakimi. Ketiga, empati, yaitu kemampuan memahami perasaan dan dunia orang lain seakan-akan dialami sendiri tanpa kehilangan jarak yang sehat. Ketiga sikap ini diyakini menjadi syarat tumbuhnya perubahan yang positif pada diri orang yang dibantu."),
        ("h3", "2.2.2 Pandangan Gerald Corey"),
        ("p", "Corey (2017) menyoroti pentingnya kualitas pribadi konselor sebagai instrumen utama dalam proses bantuan. Menurutnya, helper yang efektif adalah pribadi yang memiliki kesadaran diri, mampu hadir secara penuh bagi orang lain, terbuka, jujur, menghargai keberagaman, serta bersedia terus belajar dan mengembangkan diri. Corey menekankan bahwa teknik konseling akan kehilangan makna apabila tidak ditopang oleh pribadi konselor yang sehat dan berintegritas."),
        ("h3", "2.2.3 Pandangan Lawrence Brammer"),
        ("p", "Brammer dan MacDonald (2003) memerinci karakteristik helper ke dalam kesadaran akan diri dan nilai, kemampuan menganalisis perasaan, kemampuan menjadi teladan, sikap altruistik, serta rasa tanggung jawab etis. Selain sikap, Brammer juga menekankan keterampilan membantu yang dapat dilatih, seperti mendengarkan, memimpin pembicaraan, memantulkan perasaan, dan menyimpulkan. Dengan demikian, menjadi helper yang baik menuntut perpaduan antara kualitas pribadi dan keterampilan yang terus diasah."),
        ("p", "Apabila ketiga pandangan tersebut dipadukan, dapat ditarik sejumlah karakteristik kunci helper yang efektif, antara lain empati, kongruensi, penerimaan tanpa syarat, kesadaran diri, kemampuan komunikasi, serta tanggung jawab etis. Karakteristik inilah yang kemudian kami jadikan acuan untuk membaca hasil wawancara pada Bab IV."),

        ("h2", "2.3 Peran Helper dalam Layanan"),
        ("p", "Selain memiliki karakteristik tertentu, helper juga menjalankan sejumlah peran. Gladding (2018) menjelaskan bahwa pemberi bantuan dapat berperan sebagai pendengar yang aktif, pemberi informasi, fasilitator, penghubung dengan sumber daya lain, sekaligus pendamping dalam proses perubahan. Peran-peran ini tidak selalu hadir bersamaan, melainkan menyesuaikan kebutuhan orang yang dibantu dan situasi yang dihadapi."),
        ("p", "Dalam konteks bimbingan dan konseling, peran helper mencakup membantu individu memahami dirinya, mengambil keputusan, menyesuaikan diri dengan lingkungan, serta mengembangkan potensi secara optimal. Peran tersebut tetap relevan ketika kita melihat profesi lain. Seorang aparat keamanan, petugas penyelamatan, tenaga kesehatan, maupun guru bimbingan dan konseling sama-sama menjalankan peran melindungi, menenangkan, memberi informasi, dan mendampingi orang yang sedang dalam kesulitan. Kesamaan inilah yang menjadi titik tolak kajian pada laporan ini."),
    ],
}

# =====================================================================
# BAB III METODE KEGIATAN
# =====================================================================
BAB3 = {
    "no": "III", "judul": "METODE KEGIATAN",
    "isi": [
        ("h2", "3.1 Jenis Kegiatan"),
        ("p", "Kegiatan ini menggunakan pendekatan kualitatif deskriptif. Pendekatan ini dipilih karena tujuan kegiatan adalah menggambarkan pengalaman, pandangan, dan keterampilan para helper apa adanya, bukan menguji hubungan antarvariabel atau mengukurnya secara angka. Data yang terkumpul berupa penjelasan dan cerita yang kemudian disusun, dikelompokkan, dan ditafsirkan secara naratif."),

        ("h2", "3.2 Subjek Wawancara"),
        ("p", "Subjek dalam kegiatan ini berjumlah empat orang helper yang berasal dari bidang layanan yang berbeda. Pemilihan subjek dilakukan secara sengaja dengan pertimbangan keragaman bidang dan ketersediaan narasumber. Keempat subjek tersebut disajikan pada tabel berikut."),
        ("table", {
            "judul": "Tabel 3.1 Profil singkat subjek wawancara",
            "head": ["Kode", "Nama", "Profesi", "Tempat Bertugas", "Pengalaman"],
            "rows": [
                ["Helper A", "Lukman Hidayat", "TNI Angkatan Darat", "Pusenopik 1", "5 tahun"],
                ["Helper B", "Rinno", "Petugas Pemadam Kebakaran", "Sektor Ciracas", "1 tahun"],
                ["Helper C", "Priska Ayu Anjastari", "Bidan", "TPMB Rukiyati S.Keb", "10 tahun (sejak 2016)"],
                ["Helper D", "Ibu Fulana (nama samaran)", "Guru Bimbingan dan Konseling", "SMA", "Sekitar 30 tahun"],
            ],
        }),
        ("p", "Khusus untuk Helper D, nama yang digunakan adalah nama samaran atas permintaan narasumber. Hal ini sekaligus menjadi penerapan asas kerahasiaan yang dijunjung dalam praktik bimbingan dan konseling."),

        ("h2", "3.3 Teknik Pengumpulan Data"),
        ("p", "Teknik pengumpulan data yang digunakan adalah wawancara semi terstruktur. Melalui teknik ini, pewawancara berpegang pada daftar pertanyaan pokok yang telah disiapkan, namun tetap memberi ruang bagi narasumber untuk menjawab secara leluasa dan bagi pewawancara untuk menggali jawaban lebih dalam. Dengan begitu, jawaban yang diperoleh lebih kaya tanpa kehilangan arah pembahasan."),

        ("h2", "3.4 Instrumen Wawancara"),
        ("p", "Instrumen yang digunakan berupa pedoman wawancara yang memuat lima belas butir pertanyaan. Butir-butir pertanyaan disusun berdasarkan capaian pembelajaran pada Rencana Pembelajaran Semester mata kuliah Pengembangan Profesi Konseling, kemudian disesuaikan bahasanya dengan masing-masing profesi. Pertanyaan tersebut mencakup makna dan peran profesi, perkembangan profesi, kompetensi, organisasi profesi, kode etik, isu layanan, kredensial, pelayanan berpusat pada klien, tugas pokok dan kewenangan, peluang dan tantangan, pengalaman berkesan, komunikasi, kerja sama tim, pengaruh pandemi, dan motivasi. Daftar lengkap kelima belas pertanyaan disajikan pada Lampiran 1."),

        ("h2", "3.5 Waktu dan Tempat Kegiatan"),
        ("p", "Wawancara dilaksanakan pada rentang waktu yang telah disepakati bersama narasumber pada tahun 2026. Pelaksanaan dilakukan di tempat yang memudahkan narasumber, antara lain di lingkungan kesatuan, kantor sektor pemadam kebakaran, tempat praktik mandiri bidan, dan sekolah. Sebagian wawancara dilakukan secara tatap muka langsung dan sebagian dilengkapi komunikasi lanjutan untuk melengkapi data. Seluruh kegiatan didokumentasikan dalam bentuk catatan dan foto yang dapat dilihat pada Lampiran 3."),
    ],
}

# =====================================================================
# DATA EMPAT HELPER (15 POIN PER HELPER)
# Tiap poin = (judul_poin, jawaban/uraian)
# =====================================================================

HELPER_A = {
    "kode": "Helper A", "nama": "Lukman Hidayat", "profesi": "TNI Angkatan Darat",
    "tempat": "Pusat Persenjataan Optronik (Pusenopik) 1", "lama": "5 tahun",
    "foto": "TNI.jpg",
    "poin": [
        ("Makna profesi dan peran utama", "Bapak Lukman memaknai profesinya sebagai TNI Angkatan Darat sebagai pengabdian untuk menjaga kedaulatan Negara Kesatuan Republik Indonesia dari ancaman militer maupun non-militer. Peran utamanya tidak hanya bertempur, tetapi juga melindungi dan melayani masyarakat, termasuk melalui patroli rutin di objek vital nasional dan kegiatan teritorial yang bersentuhan langsung dengan warga."),
        ("Perkembangan profesi dari awal hingga kini", "Selama lima tahun bertugas, ia merasakan tugas berkembang dari penguasaan keterampilan dasar keprajuritan menuju penguasaan teknologi alat utama sistem persenjataan yang semakin modern. Tuntutan adaptasi terhadap teknologi membuatnya terus belajar agar tidak tertinggal."),
        ("Kompetensi paling penting", "Menurutnya, kompetensi paling penting adalah penguasaan teknis dan taktis militer yang dipadukan dengan kepemimpinan, kedisiplinan, serta ketahanan mental. Kemampuan mengambil keputusan yang cepat dan tepat di lapangan menjadi penentu keselamatan banyak orang."),
        ("Peran organisasi atau kesatuan", "Ia menjelaskan bahwa kesatuan dan institusi TNI berperan besar dalam menjaga profesionalisme melalui pendidikan berjenjang, pelatihan, dan pembinaan yang ketat. Rantai komando memastikan setiap anggota bekerja sesuai standar dan terus ditingkatkan kemampuannya."),
        ("Penerapan kode etik", "Bapak Lukman menegaskan bahwa setiap prajurit terikat pada Sapta Marga, Sumpah Prajurit, dan Delapan Wajib TNI. Dalam berhadapan dengan masyarakat, ia berpegang pada sikap ramah, sopan, dan menjunjung tinggi kepentingan rakyat. Setiap tindakan harus tetap berada dalam koridor hukum dan prosedur yang berlaku."),
        ("Isu yang sering dihadapi", "Isu yang kerap muncul adalah tantangan geografis dan logistik ketika bertugas di wilayah terpencil, serta ancaman perang informasi berupa berita bohong yang dapat mengganggu stabilitas dan memecah belah masyarakat."),
        ("Pentingnya pengakuan kompetensi resmi", "Ia memandang pengakuan kompetensi melalui pendidikan dan sertifikasi kecabangan sebagai hal yang mutlak. Pengakuan resmi memastikan setiap prajurit benar-benar mampu mengoperasikan persenjataan dan menjalankan tugas dengan aman dan bertanggung jawab."),
        ("Pelayanan berpusat pada masyarakat", "Dalam kegiatan teritorial, ia menerapkan pendekatan humanis dengan senyum, sapa, dan salam, serta bergotong royong bersama warga. Pelayanan diarahkan agar kehadiran TNI dirasakan manfaatnya secara langsung oleh masyarakat."),
        ("Tugas pokok dan kewenangan", "Tugas pokok yang paling sering dilakukan adalah pengamanan dan patroli di objek vital serta pembinaan teritorial. Ia memastikan setiap tindakan tetap berada dalam kewenangan dengan mematuhi rantai komando dan prosedur operasi standar."),
        ("Peluang dan tantangan masa depan", "Peluang terbesar terletak pada modernisasi persenjataan dan peningkatan kualitas sumber daya prajurit. Tantangan terbesar adalah ancaman siber, perang informasi, serta tuntutan untuk terus menyesuaikan diri dengan perkembangan teknologi pertahanan."),
        ("Pengalaman paling berkesan", "Pengalaman yang berkesan baginya adalah penugasan hingga ke wilayah pedalaman dari Sabang sampai Merauke. Di sana ia merasakan langsung keterbatasan komunikasi dengan keluarga, namun sekaligus menemukan makna pengabdian ketika diterima dan dibantu oleh masyarakat setempat."),
        ("Komunikasi dengan masyarakat", "Ia berkomunikasi dengan menyesuaikan diri pada budaya lokal dan menggunakan bahasa yang santun. Saat situasi krisis, ia berusaha menenangkan masyarakat dengan informasi yang jelas agar tidak timbul kepanikan."),
        ("Kerja sama tim antar-petugas", "Kerja sama tim ia anggap sebagai kunci. Selain solid di internal kesatuan, ia kerap bersinergi secara taktis dengan Kepolisian dan instansi pemerintah lain dalam pengamanan maupun penanganan situasi tertentu."),
        ("Pengaruh pandemi Covid-19", "Saat pandemi, ia dilibatkan dalam pengamanan pelaksanaan protokol kesehatan dan membantu penanganan di masyarakat. Pendidikan dan latihan militer pun menyesuaikan dengan pembatasan interaksi demi mencegah penularan."),
        ("Motivasi menjalankan profesi", "Motivasi terbesarnya adalah rasa cinta tanah air dan kebanggaan dapat mengabdi untuk bangsa. Keinginan melindungi rakyat dan menjaga keutuhan negara membuatnya tetap teguh menjalani profesi ini."),
    ],
}

HELPER_B = {
    "kode": "Helper B", "nama": "Rinno", "profesi": "Petugas Pemadam Kebakaran",
    "tempat": "Kantor Sektor Pemadam Kebakaran Ciracas", "lama": "1 tahun",
    "foto": "Pemadam.jpg",
    "poin": [
        ("Makna profesi dan peran utama", "Bapak Rinno memaknai profesinya sebagai pelayan keselamatan masyarakat. Peran utamanya mencakup lima tugas pokok, yaitu pencegahan kebakaran, pemadaman, penyelamatan, penanganan bahan berbahaya, dan penyuluhan keselamatan kepada warga."),
        ("Perkembangan profesi dari awal hingga kini", "Meskipun baru satu tahun bertugas, ia melihat bahwa pekerjaan pemadam kebakaran kini tidak lagi terbatas pada memadamkan api. Layanan penyelamatan non-kebakaran justru semakin dominan, mulai dari evakuasi hewan liar hingga penanganan warga yang berada dalam kondisi darurat."),
        ("Kompetensi paling penting", "Kompetensi yang paling penting menurutnya adalah penguasaan teknis operasional, mulai dari penggunaan alat penyelamatan, taktik pemadaman, hingga pemahaman prosedur keselamatan yang mengutamakan keselamatan diri dan korban."),
        ("Peran organisasi atau institusi", "Ia menyebut bahwa pendidikan dan pelatihan resmi dari instansi terkait, termasuk pembinaan di bawah pemerintah daerah, sangat membantu meningkatkan profesionalisme. Pelatihan berkala memastikan petugas siap menghadapi situasi yang berubah-ubah."),
        ("Penerapan kode etik", "Kode etik yang dipegangnya adalah mengutamakan keselamatan masyarakat di atas kepentingan pribadi serta bekerja dengan prinsip keselamatan terlebih dahulu. Ia berusaha cepat tanggap tanpa mengabaikan keselamatan tim."),
        ("Isu yang sering dihadapi", "Isu yang paling sering ia hadapi adalah hambatan akses menuju lokasi, seperti warga yang berkerumun dan jalan atau gang yang sempit. Selain itu, laporan palsu juga menjadi persoalan karena dapat mengganggu waktu tanggap yang ditargetkan."),
        ("Pentingnya pengakuan kompetensi resmi", "Ia menilai sertifikasi dan pendidikan resmi sangat penting karena pekerjaan ini berisiko tinggi. Pengakuan kompetensi memastikan setiap petugas benar-benar terlatih sehingga aman bagi dirinya maupun masyarakat yang ditolong."),
        ("Pelayanan berpusat pada masyarakat", "Pelayanan ia arahkan pada kebutuhan warga yang sedang dalam kesulitan. Ia menyebut layanan darurat berjalan selama dua puluh empat jam dan petugas siap membantu meski persoalannya tampak kecil di mata orang lain."),
        ("Tugas pokok dan kewenangan", "Tugas pokok yang paling sering ia lakukan saat ini adalah penyelamatan non-kebakaran. Ia memastikan setiap tindakan sesuai kewenangan dengan berkoordinasi bersama pihak terkait, termasuk pengurus lingkungan setempat."),
        ("Peluang dan tantangan masa depan", "Peluang ke depan ada pada pemanfaatan teknologi baru seperti peralatan rescue modern. Tantangannya adalah keterbatasan personel dan kesadaran masyarakat yang masih perlu ditingkatkan agar tidak menghambat penanganan darurat."),
        ("Pengalaman paling berkesan", "Pengalaman yang berkesan baginya adalah ketika menyelamatkan korban yang terjebak di balik teralis pada lantai dua saat kebakaran besar di kawasan Jatinegara. Pengalaman lain yang menyentuh adalah membantu mengevakuasi ponsel anak yang tercebur ke selokan tertutup pada tengah malam dengan tetap berkoordinasi bersama warga."),
        ("Komunikasi dengan masyarakat", "Saat tiba di lokasi, ia berusaha menenangkan warga yang panik dengan memberi arahan yang tegas namun tidak menambah ketegangan. Edukasi singkat di tempat kejadian ia anggap penting agar warga ikut membantu kelancaran penanganan."),
        ("Kerja sama tim antar-petugas", "Ia menekankan bahwa kerja sama tim adalah kekuatan utama. Dengan keterbatasan personel, koordinasi antar-unit menjadi cara untuk tetap menangani situasi dengan baik dan aman."),
        ("Pengaruh pandemi Covid-19", "Pada masa pandemi, tugasnya bertambah dengan kegiatan penyemprotan disinfektan secara massal di lingkungan masyarakat. Hal ini menambah beban kerja sekaligus memperluas peran petugas dalam membantu warga."),
        ("Motivasi menjalankan profesi", "Motivasinya adalah kepuasan batin ketika dapat menolong orang lain. Baginya, melihat warga selamat dan merasa terbantu adalah penghargaan yang membuatnya tetap semangat menjalani profesi ini."),
    ],
}

HELPER_C = {
    "kode": "Helper C", "nama": "Priska Ayu Anjastari", "profesi": "Bidan",
    "tempat": "TPMB Rukiyati S.Keb", "lama": "10 tahun (sejak 2016)",
    "foto": "Bidan.jpg",
    "poin": [
        ("Makna profesi dan peran utama", "Ibu Priska memaknai profesi bidan sebagai pendamping perempuan dan keluarga dalam menjaga kesehatan reproduksi, kehamilan, persalinan, dan tumbuh kembang anak. Peran utamanya adalah memberi layanan yang aman sekaligus menenangkan secara psikologis."),
        ("Perkembangan profesi dari awal hingga kini", "Sejak tahun 2016, ia merasakan layanan kebidanan berkembang menjadi lebih lengkap, mulai dari pemeriksaan kehamilan, pemantauan tumbuh kembang, hingga edukasi keluarga berencana dan gizi. Selama sepuluh tahun ia melayani banyak pasien dengan beragam kondisi."),
        ("Kompetensi paling penting", "Menurutnya, kompetensi paling penting adalah komunikasi interpersonal yang empatik dan menenangkan. Kemampuan ini menjadi dasar untuk membangun kepercayaan pasien, di samping keterampilan klinis kebidanan yang harus dikuasai."),
        ("Peran organisasi profesi", "Ia menyebut Ikatan Bidan Indonesia berperan penting dalam menjaga standar layanan melalui pelatihan, pembaruan ilmu, dan penerbitan rekomendasi untuk perpanjangan izin praktik. Organisasi profesi membantu bidan tetap mengikuti perkembangan ilmu kebidanan."),
        ("Penerapan kode etik", "Kode etik ia terapkan dengan menjaga kerahasiaan pasien dan mengutamakan keselamatan ibu serta bayi. Ketika menemui kasus di luar kewenangannya, ia merujuk pasien ke fasilitas kesehatan yang lebih lengkap sesuai prosedur."),
        ("Isu yang sering dihadapi", "Isu yang sering dihadapi adalah pasien yang masih memercayai mitos kehamilan yang dapat membahayakan janin, kurang patuh menjalani kontrol rutin, serta kecemasan berlebih pada ibu yang baru pertama kali hamil."),
        ("Pentingnya pengakuan kompetensi resmi", "Ia menegaskan bahwa surat tanda registrasi dan izin praktik adalah syarat mutlak. Pengakuan kompetensi resmi memastikan layanan yang diberikan aman, sah secara hukum, dan dapat dipertanggungjawabkan."),
        ("Pelayanan berpusat pada pasien", "Ia berusaha memberikan layanan yang berpusat pada kebutuhan pasien dengan mendengarkan keluhan, menjelaskan kondisi secara sabar, dan melibatkan pasien dalam mengambil keputusan terkait kesehatannya."),
        ("Tugas pokok dan kewenangan", "Tugas pokok yang paling sering ia lakukan adalah pemeriksaan kehamilan dari trimester pertama hingga ketiga, pemeriksaan laboratorium sederhana, senam hamil, serta edukasi. Ia menjaga agar setiap tindakan sesuai kewenangan bidan dan merujuk bila diperlukan."),
        ("Peluang dan tantangan masa depan", "Peluang ke depan terletak pada pemanfaatan teknologi kesehatan dan meningkatnya kesadaran masyarakat terhadap pemeriksaan rutin. Tantangannya adalah mengubah keyakinan keliru di masyarakat dan mengelola kecemasan pasien."),
        ("Pengalaman paling berkesan", "Pengalaman paling berkesan baginya adalah mendampingi proses persalinan dan menyaksikan kelahiran bayi yang sehat. Momen tersebut selalu memberi rasa haru sekaligus tanggung jawab yang besar."),
        ("Komunikasi dengan pasien", "Ia berkomunikasi dengan bahasa yang lembut dan menenangkan, terutama kepada ibu hamil yang cemas. Ia berusaha hadir sebagai pendengar agar pasien merasa aman dan dipahami."),
        ("Kerja sama tim antar-petugas", "Ia bekerja sama dengan tenaga kesehatan lain, seperti dokter dan petugas di fasilitas rujukan, untuk memastikan pasien mendapat penanganan terbaik ketika kondisinya memerlukan tindakan lanjutan."),
        ("Pengaruh pandemi Covid-19", "Pada masa pandemi, ia menyesuaikan layanan dengan menerapkan protokol kesehatan yang ketat. Sebagian konsultasi dilakukan dengan lebih hati-hati untuk melindungi ibu hamil yang termasuk kelompok rentan."),
        ("Motivasi menjalankan profesi", "Motivasinya adalah panggilan untuk membantu perempuan menjalani kehamilan dan persalinan dengan selamat. Kepercayaan pasien yang terus kembali membuatnya merasa pekerjaannya bermakna."),
    ],
}

HELPER_D = {
    "kode": "Helper D", "nama": "Ibu Fulana (nama samaran)", "profesi": "Guru Bimbingan dan Konseling",
    "tempat": "SMA", "lama": "Sekitar 30 tahun",
    "foto": "guru bk.jpg",
    "poin": [
        ("Makna profesi dan peran utama", "Ibu Fulana memaknai profesi guru bimbingan dan konseling sebagai pendamping perkembangan peserta didik. Peran utamanya bukan menghukum, melainkan membantu siswa mengenali diri, menyelesaikan masalah, dan merencanakan masa depan."),
        ("Perkembangan profesi dari awal hingga kini", "Selama hampir tiga puluh tahun mengabdi dan kini menjelang masa pensiun, ia menyaksikan layanan bimbingan dan konseling berkembang dari peran yang sering disalahpahami menjadi layanan yang semakin diakui penting bagi kesejahteraan siswa."),
        ("Kompetensi paling penting", "Menurutnya, kompetensi yang paling penting adalah keterampilan mendengar aktif, empati, serta kemampuan membangun kepercayaan. Tanpa kepercayaan, siswa tidak akan terbuka menceritakan persoalannya."),
        ("Peran organisasi profesi", "Ia menyebut Asosiasi Bimbingan dan Konseling Indonesia berperan dalam menjaga mutu layanan melalui pelatihan, pengembangan keprofesian, dan penegakan kode etik. Organisasi profesi juga memperkuat posisi guru bimbingan dan konseling di sekolah."),
        ("Penerapan kode etik", "Kode etik ia terapkan terutama melalui asas kerahasiaan. Informasi yang disampaikan siswa ia jaga dengan ketat dan hanya dibuka untuk kepentingan siswa sesuai prosedur. Ia juga menghindari sikap menghakimi."),
        ("Isu yang sering dihadapi", "Isu yang sering ia hadapi adalah stigma bahwa bimbingan dan konseling adalah polisi sekolah, beban administratif yang cukup berat, serta kesenjangan teknologi yang memengaruhi cara melayani siswa generasi sekarang."),
        ("Pentingnya pengakuan kompetensi resmi", "Ia menilai pengakuan kompetensi melalui pendidikan profesi dan sertifikasi sangat penting agar layanan bimbingan dan konseling diberikan oleh tenaga yang benar-benar kompeten dan diakui secara profesional."),
        ("Pelayanan berpusat pada siswa", "Ia menerapkan layanan yang berpusat pada siswa dengan menempatkan kebutuhan dan suara siswa sebagai dasar. Ragam layanan yang diberikan mencakup orientasi, informasi, konseling individu dan kelompok, mediasi, serta pendampingan belajar, karier, pribadi, dan sosial."),
        ("Tugas pokok dan kewenangan", "Tugas pokok yang paling sering ia lakukan adalah konseling individu, layanan informasi, dan mediasi ketika terjadi perselisihan antarsiswa. Ia memastikan setiap layanan berada dalam kewenangan profesinya dan berkolaborasi dengan pihak lain bila diperlukan."),
        ("Peluang dan tantangan masa depan", "Peluang ke depan adalah semakin diakuinya pentingnya kesehatan mental siswa. Tantangannya adalah menghapus stigma lama, mengurangi beban administratif, dan menjawab kebutuhan generasi digital. Ia juga menekankan pentingnya regenerasi konselor yang berkualitas."),
        ("Pengalaman paling berkesan", "Pengalaman paling berkesan baginya adalah ketika siswa yang dahulu bermasalah kembali menemuinya untuk berterima kasih setelah berhasil melanjutkan hidup dengan baik. Momen itu menegaskan bahwa pendampingan yang sabar membuahkan hasil."),
        ("Komunikasi dengan siswa", "Ia berkomunikasi dengan pendekatan yang hangat dan tidak menggurui. Ketika siswa gelisah atau menangis, ia memberi ruang dan mendengarkan terlebih dahulu sebelum mengajak mencari jalan keluar."),
        ("Kerja sama tim antar-petugas", "Ia berkolaborasi dengan wali kelas, guru mata pelajaran, orang tua, serta pihak luar seperti tenaga kesehatan bila kasus membutuhkannya. Kolaborasi ini memastikan penanganan masalah siswa berjalan menyeluruh."),
        ("Pengaruh pandemi Covid-19", "Saat pandemi, layanan banyak berpindah ke bentuk jarak jauh. Ia menghadapi tantangan kesenjangan teknologi dan keterbatasan kedekatan emosional, namun tetap berusaha menjaga komunikasi dengan siswa."),
        ("Motivasi menjalankan profesi", "Motivasinya adalah kecintaan pada dunia pendidikan dan keinginan melihat siswa tumbuh menjadi pribadi yang utuh. Menjelang pensiun, ia berpesan agar muncul generasi konselor baru yang siap melanjutkan tugas mendampingi siswa."),
    ],
}

HELPERS = [HELPER_A, HELPER_B, HELPER_C, HELPER_D]

# =====================================================================
# BAB IV - PEMBAHASAN (4.5) + TABEL RINGKASAN
# =====================================================================
PEMBAHASAN = [
    ("h2", "4.5 Pembahasan"),
    ("p", "Setelah memaparkan hasil wawancara terhadap empat helper, bagian ini membahas temuan dengan menelaah persamaan, perbedaan, keterampilan kunci yang muncul, serta kaitannya dengan teori karakteristik dan peran helper pada Bab II."),
    ("h3", "4.5.1 Persamaan Hasil Wawancara"),
    ("p", "Keempat helper menunjukkan sejumlah kesamaan yang menarik meskipun berasal dari bidang yang berbeda. Pertama, semuanya menempatkan keselamatan dan kepentingan orang yang dilayani sebagai prioritas utama. Kedua, semuanya menekankan pentingnya kemampuan berkomunikasi dan menenangkan orang lain, terutama dalam situasi yang menegangkan. Ketiga, semuanya terikat pada kode etik dan prosedur yang menjaga agar bantuan diberikan secara bertanggung jawab. Keempat, semuanya digerakkan oleh motivasi pengabdian, bukan semata-mata pekerjaan."),
    ("h3", "4.5.2 Perbedaan Pengalaman Helper"),
    ("p", "Perbedaan tampak pada bentuk layanan dan tantangan yang dihadapi. Helper dari TNI menghadapi tantangan geografis dan ancaman perang informasi. Petugas pemadam kebakaran berhadapan dengan situasi darurat yang menuntut kecepatan dan keselamatan fisik. Bidan berfokus pada pendampingan kesehatan ibu dan anak dengan kedekatan emosional yang tinggi. Guru bimbingan dan konseling menekankan kerahasiaan dan pendampingan psikologis dalam jangka panjang. Perbedaan ini menunjukkan bahwa keterampilan membantu selalu menyesuaikan konteks bidangnya."),
    ("h3", "4.5.3 Keterampilan Kunci yang Muncul"),
    ("p", "Dari seluruh wawancara, beberapa keterampilan kunci muncul berulang, yaitu kemampuan mendengarkan dan berkomunikasi, empati, ketenangan dalam tekanan, penguasaan teknis sesuai bidang, kerja sama tim, dan tanggung jawab etis. Keterampilan ini hadir di keempat profesi meski dengan kadar dan penekanan yang berbeda."),
    ("h3", "4.5.4 Kaitan dengan Teori Helper"),
    ("p", "Temuan lapangan ternyata sejalan dengan teori pada Bab II. Sikap empati, kejujuran, dan penerimaan yang dikemukakan Rogers (1961) tampak pada cara bidan menenangkan ibu hamil dan cara guru bimbingan dan konseling mendampingi siswa tanpa menghakimi. Penekanan Corey (2017) pada kualitas pribadi dan kesadaran diri terlihat pada motivasi pengabdian yang menggerakkan keempat helper. Adapun keterampilan membantu yang dapat dilatih sebagaimana dijelaskan Brammer dan MacDonald (2003) tampak nyata pada kemampuan komunikasi krisis petugas pemadam kebakaran dan pendekatan teritorial anggota TNI. Peran helper sebagai pendengar, pemberi informasi, fasilitator, dan pendamping yang dijelaskan Gladding (2018) juga terwakili di seluruh bidang. Dengan demikian, konsep helper dalam bimbingan dan konseling terbukti bersifat lintas profesi."),
    ("table", {
        "judul": "Tabel 4.1 Ringkasan hasil wawancara empat helper",
        "head": ["Aspek", "Helper A (TNI AD)", "Helper B (Pemadam)", "Helper C (Bidan)", "Helper D (Guru BK)"],
        "rows": [
            ["Fokus layanan", "Pertahanan dan teritorial", "Keselamatan dan penyelamatan", "Kesehatan ibu dan anak", "Pendampingan perkembangan siswa"],
            ["Keterampilan utama", "Teknis taktis, kepemimpinan", "Teknis operasional, komunikasi krisis", "Komunikasi empatik, klinis", "Mendengar aktif, empati"],
            ["Kode etik kunci", "Sapta Marga, Delapan Wajib", "Keselamatan diutamakan", "Kerahasiaan, keselamatan pasien", "Kerahasiaan, tanpa menghakimi"],
            ["Tantangan utama", "Geografis, perang informasi", "Akses lokasi, laporan palsu", "Mitos, kepatuhan, kecemasan", "Stigma, beban administratif"],
            ["Motivasi", "Cinta tanah air", "Kepuasan menolong", "Panggilan mendampingi", "Cinta pendidikan, regenerasi"],
        ],
    }),
    ("p", "Tabel di atas menegaskan bahwa keempat profesi memiliki titik temu pada peran membantu, sekaligus kekhasan pada fokus dan tantangannya. Inilah yang menjadikan kajian lintas bidang ini bermanfaat bagi calon konselor."),
]

# =====================================================================
# BAB V PENUTUP
# =====================================================================
BAB5 = {
    "no": "V", "judul": "PENUTUP",
    "isi": [
        ("h2", "5.1 Kesimpulan"),
        ("p", "Berdasarkan hasil wawancara terhadap empat helper dari bidang yang berbeda, dapat disimpulkan bahwa keberhasilan dalam memberikan layanan bantuan sangat dipengaruhi oleh keterampilan komunikasi, empati, dan kemampuan memahami kebutuhan orang yang dilayani secara menyeluruh. Meskipun berasal dari profesi yang berlainan, anggota TNI, petugas pemadam kebakaran, bidan, dan guru bimbingan dan konseling sama-sama menjalankan peran sebagai helper yang melindungi, menenangkan, memberi informasi, dan mendampingi."),
        ("p", "Kajian ini juga menunjukkan bahwa karakteristik helper yang dirumuskan Rogers, Corey, dan Brammer terbukti relevan di lapangan. Empati, kejujuran, penerimaan, kesadaran diri, keterampilan komunikasi, dan tanggung jawab etis hadir pada keempat profesi. Dengan demikian, konsep helper dalam bimbingan dan konseling tidak terbatas pada ruang konseling, melainkan dapat ditemukan pada berbagai bidang layanan."),
        ("h2", "5.2 Saran"),
        ("p", "Berdasarkan temuan tersebut, kami menyampaikan beberapa saran sebagai berikut."),
        ("num", [
            "Mahasiswa bimbingan dan konseling perlu terus meningkatkan keterampilan komunikasi dan empati sebagai bekal utama menjadi helper yang efektif.",
            "Kegiatan praktik lapangan dan wawancara dengan praktisi perlu diperbanyak agar mahasiswa memahami realitas profesi membantu secara langsung.",
            "Mahasiswa hendaknya membiasakan diri menjaga kerahasiaan dan bersikap tidak menghakimi sejak dini, sebagaimana dijunjung dalam kode etik profesi.",
            "Perlu adanya perhatian terhadap regenerasi tenaga helper yang berkualitas, khususnya guru bimbingan dan konseling, agar layanan tetap terjaga di masa mendatang.",
        ]),
    ],
}

# =====================================================================
# DAFTAR PUSTAKA (APA edisi ke-7) - seluruh entri terverifikasi
# =====================================================================
DAFTAR_PUSTAKA = [
    "Brammer, L. M., & MacDonald, G. (2003). The helping relationship: Process and skills (8th ed.). Allyn & Bacon. https://www.pearson.com/en-us/subject-catalog/p/helping-relationship-the-process-and-skills/P200000000826/9780205355204",
    "Corey, G. (2017). Theory and practice of counseling and psychotherapy (10th ed.). Cengage Learning. https://www.cengage.com/c/student/9780357671429/",
    "Gladding, S. T. (2018). Counseling: A comprehensive profession (8th ed.). Pearson. https://www.pearson.com/en-us/subject-catalog/p/counseling:-a-comprehensive-profession/P200000001101/9780136874720",
    "Lubis, N. L. (2011). Memahami dasar-dasar konseling dalam teori dan praktik. Kencana. https://www.gramedia.com/author/author-namora-lumongga-lubis-msc-phd-dan-hasnida-phd-psikolog",
    "Prayitno, & Amti, E. (2004). Dasar-dasar bimbingan dan konseling. Rineka Cipta. https://ejournal.unp.ac.id/index.php/konselor/article/view/8754",
    "Rogers, C. R. (1961). On becoming a person: A therapist's view of psychotherapy. Houghton Mifflin. https://archive.org/details/onbecomingperson00roge",
    "Willis, S. S. (2013). Konseling individual: Teori dan praktek. Alfabeta. https://www.goodreads.com/author/show/15165184.Sofyan_S_Willis",
]



# =====================================================================
# PENYUSUN BLOK BAB IV (HASIL 4.1-4.4 + PEMBAHASAN 4.5)
# Dipakai bersama oleh gen_pdf.py dan build_docx.py agar konsisten.
# =====================================================================
def build_bab4():
    isi = []
    isi.append(("p", "Bab ini memaparkan hasil wawancara terhadap empat helper. "
                      "Hasil disusun mengikuti lima belas butir pertanyaan pada pedoman wawancara, "
                      "kemudian dilanjutkan dengan pembahasan yang mengaitkan temuan dengan teori pada Bab II."))
    for idx, h in enumerate(HELPERS, 1):
        isi.append(("h2", "4.%d Hasil Wawancara %s (%s)" % (idx, h["kode"], h["profesi"])))
        isi.append(("p", "Narasumber pada bagian ini adalah %s, %s di %s, dengan pengalaman %s. "
                         "Berikut ringkasan jawaban narasumber atas lima belas butir pertanyaan."
                         % (h["nama"], h["profesi"].lower(), h["tempat"], h["lama"])))
        for i, (judul, teks) in enumerate(h["poin"], 1):
            isi.append(("lead", "%d. %s. %s" % (i, judul, teks)))
    isi.extend(PEMBAHASAN)
    return {"no": "IV", "judul": "HASIL WAWANCARA DAN PEMBAHASAN", "isi": isi}


BAB4 = build_bab4()
BAB_LIST = [BAB1, BAB2, BAB3, BAB4, BAB5]
