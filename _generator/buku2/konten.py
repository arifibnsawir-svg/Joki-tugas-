# -*- coding: utf-8 -*-
# Konten Mini Book PKN - Naila Diyana Nabilah (Buku #2).
# DNA: akademik-terstruktur (pengertian -> dasar hukum -> analisis -> rangkuman),
# tabel berwarna, ciri khas prodi Bimbingan & Konseling. Di-humanize, beda dari Buku 1.
# Blok: ('p',teks) | ('h2',teks) | ('table', {'judul','head':[...],'rows':[[...]]})

PENULIS = "Naila Diyana Nabilah"

KATA_PENGANTAR = [
 "Puji syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas selesainya mini book berjudul \"Pendidikan Kewarganegaraan di Perguruan Tinggi\" ini. Naskah ini disusun sebagai tugas akademik sekaligus sarana untuk mendalami nilai-nilai kewarganegaraan dalam kehidupan bermasyarakat, berbangsa, dan bernegara.",
 "Pembahasan dalam mini book ini ditata mengikuti delapan pokok bahasan, yaitu hakikat Pendidikan Kewarganegaraan, identitas nasional, integrasi nasional, negara dan konstitusi, hak dan kewajiban warga negara, penegakan hukum yang berkeadilan, geopolitik dan geostrategi, serta anti korupsi. Setiap bab disusun secara terstruktur, dimulai dari pengertian, dasar hukum, hingga analisis dan keterkaitannya dengan kehidupan mahasiswa.",
 "Sebagai mahasiswa program studi Bimbingan dan Konseling, penulis berusaha mengaitkan setiap materi dengan peran calon konselor yang kelak berhadapan dengan manusia dari beragam latar belakang. Harapannya, naskah ini tidak hanya menjadi tugas, tetapi juga bekal sikap dalam menjalani kehidupan akademik dan profesi.",
 "Penulis mengucapkan terima kasih kepada dosen pengampu, keluarga, dan teman-teman yang telah memberikan dukungan. Kritik dan saran yang membangun tetap penulis harapkan demi penyempurnaan karya ini.",
 "Jakarta, 2026",
 "Penulis,",
 "Naila Diyana Nabilah",
]

# Daftar pustaka format IEEE (bernomor [n]); urut sesuai penomoran.
DAFTAR_PUSTAKA = [
 "Republik Indonesia, Undang-Undang Dasar Negara Republik Indonesia Tahun 1945. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Dasar_Negara_Republik_Indonesia_Tahun_1945",
 "Republik Indonesia, Undang-Undang Nomor 12 Tahun 2012 tentang Pendidikan Tinggi, 2012. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2012",
 "Republik Indonesia, Undang-Undang Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional, 2003. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_20_Tahun_2003",
 "Republik Indonesia, Undang-Undang Nomor 24 Tahun 2009 tentang Bendera, Bahasa, dan Lambang Negara, serta Lagu Kebangsaan, 2009. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_24_Tahun_2009",
 "Republik Indonesia, Undang-Undang Nomor 12 Tahun 2006 tentang Kewarganegaraan Republik Indonesia, 2006. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2006",
 "Republik Indonesia, Undang-Undang Nomor 12 Tahun 2011 tentang Pembentukan Peraturan Perundang-undangan, 2011. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2011",
 "Republik Indonesia, Undang-Undang Nomor 39 Tahun 1999 tentang Hak Asasi Manusia, 1999. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_39_Tahun_1999",
 "Perserikatan Bangsa-Bangsa, Universal Declaration of Human Rights, 1948. [Daring]. Tersedia: https://www.un.org/en/about-us/universal-declaration-of-human-rights",
 "Republik Indonesia, Undang-Undang Nomor 48 Tahun 2009 tentang Kekuasaan Kehakiman, 2009. [Daring]. Tersedia: https://commons.wikimedia.org/wiki/File:Undang-Undang_Republik_Indonesia_Nomor_48_Tahun_2009.pdf",
 "Republik Indonesia, Undang-Undang Nomor 2 Tahun 2002 tentang Kepolisian Negara Republik Indonesia, 2002. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_2_Tahun_2002",
 "Republik Indonesia, Undang-Undang Nomor 3 Tahun 2002 tentang Pertahanan Negara, 2002. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_3_Tahun_2002",
 "Republik Indonesia, Undang-Undang Nomor 31 Tahun 1999 tentang Pemberantasan Tindak Pidana Korupsi, 1999. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_31_Tahun_1999",
 "Republik Indonesia, Undang-Undang Nomor 20 Tahun 2001 tentang Perubahan atas Undang-Undang Nomor 31 Tahun 1999, 2001. [Daring]. Tersedia: https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_20_Tahun_2001",
 "Komisi Pemberantasan Korupsi, Anti-Corruption Learning Center (ACLC): Materi Pembelajaran Antikorupsi. [Daring]. Tersedia: https://aclc.kpk.go.id/materi-pembelajaran",
]

BAB = []

# ===================== BAB 1 =====================
BAB.append({
 "no": "1",
 "judul": "HAKIKAT PENDIDIKAN KEWARGANEGARAAN",
 "isi": [
  ("p", "Bab ini menguraikan kedudukan Pendidikan Kewarganegaraan di perguruan tinggi secara bertahap, mulai dari pengertian, dasar hukum, tujuan, hingga urgensinya bagi mahasiswa. Penyusunan yang runtut ini dimaksudkan agar pembaca dapat memahami mengapa mata kuliah ini diwajibkan dan apa yang membedakannya dari pelajaran serupa di jenjang sekolah."),

  ("h2", "1.1 Pengertian Pendidikan Kewarganegaraan"),
  ("p", "Pendidikan Kewarganegaraan dapat dipahami sebagai proses pendidikan yang bertujuan menumbuhkan kesadaran berbangsa dan bernegara, pemahaman terhadap hak dan kewajiban, serta kemampuan berpartisipasi secara aktif dalam kehidupan bermasyarakat. Mata kuliah ini tidak berhenti pada teori tentang negara, hukum, atau demokrasi, melainkan juga membentuk sikap, nilai, dan tanggung jawab sosial."),
  ("p", "Di perguruan tinggi, maknanya menjadi lebih luas. Mahasiswa tidak lagi diposisikan sebagai penerima materi, tetapi sebagai calon warga negara dewasa yang dilatih berpikir kritis, bertindak rasional, dan mengambil peran dalam kehidupan publik. Karena itu, Pendidikan Kewarganegaraan diarahkan agar mahasiswa memahami dasar kehidupan bernegara sekaligus peka terhadap persoalan kebangsaan."),
  ("p", "Banyak persoalan sosial muncul bukan karena kurangnya pengetahuan, melainkan karena lemahnya kesadaran kewarganegaraan. Sikap acuh terhadap hukum, rendahnya partisipasi sosial, dan penyebaran informasi yang tidak bertanggung jawab menunjukkan bahwa mata kuliah ini bukan pelengkap, melainkan bagian penting dari pembentukan warga negara yang cerdas dan berkarakter."),

  ("h2", "1.2 Dasar Hukum Pendidikan Kewarganegaraan"),
  ("p", "Keberadaan Pendidikan Kewarganegaraan di perguruan tinggi memiliki landasan hukum yang jelas, sehingga bukan sekadar kebijakan internal kampus. Landasan ini menempatkan mata kuliah tersebut sebagai bagian dari sistem pendidikan nasional."),
  ("table", {"judul": "Tabel 1.1 Dasar hukum Pendidikan Kewarganegaraan di perguruan tinggi",
            "head": ["Landasan", "Pokok Pengaturan"],
            "rows": [
              ["Pancasila", "Sumber nilai dan dasar moral kehidupan berbangsa"],
              ["UUD NRI Tahun 1945", "Tujuan pendidikan nasional mencerdaskan kehidupan bangsa"],
              ["UU No. 20 Tahun 2003", "Kurikulum pendidikan wajib memuat pendidikan kewarganegaraan"],
              ["UU No. 12 Tahun 2012", "Pendidikan Kewarganegaraan sebagai mata kuliah wajib di perguruan tinggi"],
            ]}),
  ("p", "Berdasarkan landasan tersebut, Pendidikan Kewarganegaraan ditempatkan sebagai mata kuliah wajib umum yang memberikan fondasi kebangsaan, kepribadian, dan integritas kepada mahasiswa. Dengan dasar hukum yang kuat, mata kuliah ini menjadi bagian yang tidak terpisahkan dari pembentukan lulusan yang cakap secara keilmuan sekaligus bertanggung jawab secara sosial."),

  ("h2", "1.3 Tujuan dan Fungsi Pendidikan Kewarganegaraan"),
  ("p", "Tujuan utama Pendidikan Kewarganegaraan adalah membentuk mahasiswa menjadi warga negara yang baik, cerdas, dan bertanggung jawab, serta memiliki komitmen terhadap nilai kebangsaan. Mahasiswa diharapkan tidak hanya mengetahui konsep negara dan demokrasi, tetapi juga menjalankan perannya secara nyata."),
  ("p", "Dari sisi fungsi, mata kuliah ini bekerja pada tiga arah. Sebagai wahana pembentukan karakter, ia menjaga agar mahasiswa tetap berpijak pada nilai Pancasila di tengah berbagai pengaruh. Sebagai sarana penajaman nalar, ia melatih mahasiswa menganalisis persoalan bangsa secara objektif. Sebagai ruang partisipasi, ia mendorong mahasiswa terlibat dalam kehidupan sosial dan kampus yang sehat, bukan sekadar mengkritik tanpa tindakan."),

  ("h2", "1.4 Urgensi bagi Mahasiswa di Era Digital"),
  ("p", "Pertanyaan yang sering muncul adalah mengapa mata kuliah ini masih penting, padahal materinya seakan mengulang pelajaran sekolah. Jika dicermati, urgensinya di perguruan tinggi justru lebih besar. Mahasiswa berada pada fase yang menuntut kedewasaan berpikir dan kesiapan mengambil peran di masyarakat."),
  ("p", "Di era digital, mahasiswa hidup dalam arus informasi yang sangat cepat dan tidak selalu akurat. Tanpa dasar kewarganegaraan yang kuat, mereka mudah terjebak sikap ekstrem, intoleransi, atau apatisme. Pendidikan Kewarganegaraan membantu membangun sikap kritis dan selektif dalam menyikapi isu yang berkembang. Urgensi ini semakin terasa karena Indonesia adalah bangsa majemuk yang menuntut pemahaman tentang toleransi dan persatuan."),

  ("h2", "1.5 Perbedaan PKn di Sekolah dan di Perguruan Tinggi"),
  ("p", "Pendidikan Kewarganegaraan memang telah diajarkan sejak sekolah dasar. Namun, orientasinya di perguruan tinggi berbeda secara mendasar. Perbedaan ini perlu dipahami agar mahasiswa tidak menganggap materi ini sebagai pengulangan belaka."),
  ("table", {"judul": "Tabel 1.2 Perbedaan orientasi PKn di sekolah dan perguruan tinggi",
            "head": ["Aspek", "Di Sekolah", "Di Perguruan Tinggi"],
            "rows": [
              ["Fokus", "Pengenalan nilai dasar & pembiasaan", "Analisis, kritik, dan penerapan"],
              ["Metode", "Penjelasan terstruktur sesuai usia", "Diskusi, studi kasus, argumentasi ilmiah"],
              ["Sasaran", "Mengenal identitas & aturan", "Kesadaran intelektual & tanggung jawab publik"],
            ]}),
  ("p", "Dengan demikian, meskipun sama-sama membahas kewarganegaraan, perguruan tinggi menekankan pendalaman dan penerapan. Mahasiswa diajak melihat kewarganegaraan bukan sebagai status administratif, melainkan sebagai peran aktif dalam kehidupan berbangsa."),

  ("h2", "1.6 Relevansi bagi Mahasiswa Bimbingan dan Konseling"),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, mata kuliah ini memiliki keterkaitan yang dekat dengan profesi. Seorang calon konselor akan berhadapan dengan individu dari beragam latar belakang sosial, budaya, dan ekonomi. Kesadaran kewarganegaraan membantu konselor bersikap adil, tidak berprasangka, dan menghormati hak setiap orang."),
  ("p", "Selain itu, banyak persoalan yang ditangani konselor, seperti perundungan, diskriminasi, atau konflik sosial, bersinggungan dengan nilai kewarganegaraan dan hukum. Pemahaman yang baik membuat calon konselor mampu menempatkan persoalan secara lebih utuh, bukan sekadar dari sisi psikologis semata."),

  ("h2", "1.7 Rangkuman"),
  ("p", "Pendidikan Kewarganegaraan di perguruan tinggi adalah mata kuliah wajib yang berlandaskan Pancasila, UUD NRI Tahun 1945, Undang-Undang Nomor 20 Tahun 2003, dan Undang-Undang Nomor 12 Tahun 2012. Tujuannya membentuk warga negara yang cerdas, berkarakter, dan partisipatif."),
  ("p", "Berbeda dari jenjang sekolah, pendekatannya menekankan analisis dan penerapan. Di era digital, perannya semakin penting sebagai penyaring informasi dan penjaga sikap kritis. Bagi mahasiswa Bimbingan dan Konseling, pemahaman ini menjadi bekal untuk menghormati keberagaman dan menempatkan persoalan secara adil."),
 ]
})


# ===================== BAB 2 =====================
BAB.append({
 "no": "2",
 "judul": "IDENTITAS NASIONAL",
 "isi": [
  ("p", "Bab ini membahas identitas nasional sebagai jati diri bangsa, dimulai dari pengertian, unsur pembentuk, kedudukan Pancasila, hingga tantangan yang dihadapi mahasiswa. Pemahaman ini penting agar mahasiswa dapat menempatkan dirinya bukan hanya sebagai individu yang sedang menempuh studi, tetapi juga sebagai bagian dari bangsa yang memiliki sejarah dan masa depan bersama."),

  ("h2", "2.1 Pengertian Identitas Nasional"),
  ("p", "Identitas nasional merujuk pada sekumpulan ciri yang membedakan satu bangsa dengan bangsa lain. Ciri ini tidak terbatas pada bendera atau lagu kebangsaan, tetapi mencakup nilai bersama, bahasa, budaya, sejarah kolektif, dan cara pandang terhadap dunia. Dengan kata lain, identitas nasional memadukan unsur yang konkret berupa simbol dengan unsur abstrak berupa nilai dan kesadaran kolektif."),
  ("p", "Identitas nasional bukan sesuatu yang muncul secara tiba-tiba. Ia terbentuk melalui proses sejarah yang panjang, mulai dari perjuangan kemerdekaan hingga interaksi sosial sehari-hari. Bangsa Indonesia tidak langsung memiliki identitas yang utuh setelah proklamasi, melainkan terus membentuknya melalui peristiwa sejarah, kebijakan negara, dan kehidupan bersama."),
  ("p", "Bagi mahasiswa yang sedang mencari jati diri, memahami identitas nasional membantu menempatkan diri dalam konteks yang lebih luas. Kesadaran ini menumbuhkan rasa memiliki terhadap bangsa, sehingga mahasiswa tidak terjebak pada sikap individualistis yang abai terhadap kepentingan bersama."),

  ("h2", "2.2 Unsur-Unsur Pembentuk Identitas Nasional"),
  ("p", "Identitas nasional terbentuk dari beberapa unsur yang saling menguatkan. Sejarah berperan sebagai ingatan kolektif yang menjadi akar kesadaran kebangsaan. Bahasa Indonesia menjadi perekat yang menyatukan penutur ratusan bahasa daerah. Budaya yang beragam justru memperlihatkan kemampuan bangsa merangkul perbedaan tanpa kehilangan kesatuan."),
  ("table", {"judul": "Tabel 2.1 Unsur pembentuk identitas nasional dan perannya",
            "head": ["Unsur", "Peran dalam Identitas Nasional"],
            "rows": [
              ["Sejarah", "Ingatan kolektif dan akar kesadaran kebangsaan"],
              ["Bahasa Indonesia", "Alat pemersatu komunikasi antardaerah"],
              ["Budaya", "Penanda keragaman yang memperkaya kesatuan"],
              ["Simbol negara", "Lambang, bendera, dan semboyan sebagai penanda jati diri"],
            ]}),
  ("p", "Di lingkungan kampus, unsur-unsur ini hadir secara nyata. Bahasa Indonesia menjadi bahasa akademik yang mempertemukan mahasiswa dari berbagai daerah, sementara pertukaran budaya antarteman memperkaya pemahaman tentang siapa kita sebagai bangsa."),

  ("h2", "2.3 Pancasila sebagai Pengikat Identitas Bangsa"),
  ("p", "Pancasila memiliki kedudukan khusus dalam identitas nasional. Ia bukan hanya dasar negara, tetapi juga pengikat yang merangkum nilai-nilai yang dianut sebagian besar rakyat Indonesia. Ketuhanan mengakui keberagaman kepercayaan, kemanusiaan menegaskan martabat manusia, persatuan menolak perpecahan, kerakyatan menempatkan rakyat sebagai subjek, dan keadilan sosial berkomitmen pada kesejahteraan bersama."),
  ("p", "Sebagai penanda, Pancasila menunjukkan bahwa Indonesia memiliki karakter khas. Berbeda dari negara yang berbasis satu agama atau satu ideologi politik tertentu, Indonesia memilih Pancasila sebagai titik temu dari keberagamannya. Pilihan ini adalah hasil pencarian panjang, bukan kebetulan sejarah."),
  ("p", "Sebagian mahasiswa kadang meragukan relevansi Pancasila ketika melihat korupsi atau ketidakadilan di sekitarnya. Keraguan ini wajar. Namun jawabannya bukan menolak Pancasila, melainkan mendorong agar nilainya benar-benar diterapkan dalam kehidupan nyata."),

  ("h2", "2.4 Bahasa, Budaya, dan Simbol Negara"),
  ("p", "Identitas nasional juga hadir melalui bahasa, budaya, dan simbol negara yang digunakan bersama. Pengaturan mengenai bendera, bahasa, lambang negara, dan lagu kebangsaan ditegaskan dalam Undang-Undang Nomor 24 Tahun 2009, yang menempatkan simbol-simbol ini sebagai sesuatu yang memiliki kedudukan hukum, bukan sekadar atribut seremonial."),
  ("p", "Bahasa Indonesia mempertemukan masyarakat dari berbagai daerah tanpa harus meninggalkan bahasa daerah. Budaya, mulai dari tradisi, kesenian, hingga kebiasaan sosial, mengajarkan nilai gotong royong, musyawarah, dan kepedulian. Unsur-unsur ini membantu masyarakat mengenali dirinya sebagai bagian dari satu bangsa."),

  ("h2", "2.5 Tantangan Identitas Nasional di Kalangan Mahasiswa"),
  ("p", "Identitas nasional tidak selalu kuat dengan sendirinya. Salah satu tantangan yang terasa adalah pengaruh budaya luar yang masuk dengan mudah melalui media digital. Pengaruh ini tidak selalu buruk, tetapi menjadi masalah ketika mahasiswa lebih menghargai budaya luar daripada budaya bangsanya sendiri."),
  ("p", "Tantangan lain adalah melemahnya minat terhadap sejarah dan kebudayaan nasional. Sebagian mahasiswa lebih mengenal tokoh luar negeri daripada tokoh bangsa sendiri, atau menganggap materi kebangsaan sebagai hafalan yang membosankan. Padahal, tanpa pemahaman sejarah, alasan menjaga persatuan menjadi sulit dipahami."),

  ("h2", "2.6 Relevansi bagi Mahasiswa Bimbingan dan Konseling"),
  ("p", "Bagi calon konselor, pemahaman identitas nasional dan keberagaman budaya menjadi modal penting. Dalam praktiknya nanti, konselor akan berhadapan dengan klien yang membawa latar budaya berbeda, dan latar itu memengaruhi cara mereka memandang masalah serta solusinya."),
  ("p", "Konselor yang memahami keberagaman akan lebih berempati dan tidak mudah berprasangka. Identitas nasional yang sehat, yang menghargai perbedaan tanpa merendahkan, sejalan dengan prinsip layanan bimbingan yang menghormati martabat setiap individu."),

  ("h2", "2.7 Rangkuman"),
  ("p", "Identitas nasional adalah jati diri bangsa yang terbentuk dari sejarah, bahasa, budaya, dan simbol negara, serta diikat oleh nilai-nilai Pancasila. Identitas ini dibangun melalui proses panjang dan perlu dirawat secara sadar."),
  ("p", "Tantangan terhadap identitas nasional di kalangan mahasiswa muncul dari pengaruh budaya luar dan melemahnya minat pada sejarah bangsa. Bagi mahasiswa Bimbingan dan Konseling, kesadaran akan identitas dan keberagaman menjadi dasar sikap empatik dalam menjalankan profesi."),
 ]
})

# ===================== BAB 3 =====================
BAB.append({
 "no": "3",
 "judul": "INTEGRASI NASIONAL",
 "isi": [
  ("p", "Bab ini membahas integrasi nasional sebagai proses menyatukan keberagaman bangsa. Pembahasan disusun dari pengertian, faktor pendorong dan penghambat, hingga peran mahasiswa, agar terlihat bahwa persatuan bukan sesuatu yang terjadi dengan sendirinya, melainkan hasil usaha bersama yang terus-menerus."),

  ("h2", "3.1 Pengertian Integrasi Nasional"),
  ("p", "Integrasi nasional adalah proses menyatukan berbagai kelompok dalam satu kehidupan bangsa yang utuh. Di Indonesia, hal ini penting karena masyarakatnya memiliki banyak perbedaan, mulai dari suku, agama, bahasa, budaya, hingga kondisi ekonomi dan pandangan politik."),
  ("p", "Integrasi nasional tidak berarti menghapus perbedaan. Sebaliknya, ia menyatukan perbedaan agar tidak berubah menjadi konflik. Bangsa Indonesia dibangun bukan di atas keseragaman, melainkan di atas kesediaan untuk hidup bersama dalam perbedaan, sebagaimana ditegaskan oleh semboyan Bhinneka Tunggal Ika."),
  ("p", "Di lingkungan kampus, integrasi terlihat dari kemampuan mahasiswa bergaul dan bekerja sama dengan teman yang berbeda latar belakang. Kampus menjadi ruang latihan yang baik, karena di sana mahasiswa bertemu banyak orang yang berbeda dari dirinya."),

  ("h2", "3.2 Faktor Pendorong dan Penghambat Integrasi"),
  ("p", "Integrasi nasional dipengaruhi oleh faktor yang mendorong sekaligus faktor yang menghambat. Memahami keduanya membantu mahasiswa bersikap lebih sadar dalam kehidupan sehari-hari."),
  ("table", {"judul": "Tabel 3.1 Faktor pendorong dan penghambat integrasi nasional",
            "head": ["Faktor Pendorong", "Faktor Penghambat"],
            "rows": [
              ["Rasa senasib sebagai bangsa yang pernah dijajah", "Ketimpangan ekonomi antardaerah"],
              ["Bahasa Indonesia sebagai pemersatu", "Sentimen suku dan agama yang tidak dikelola"],
              ["Nilai Pancasila sebagai kerangka moral bersama", "Sentimen kedaerahan yang berlebihan"],
              ["Lembaga nasional dan pendidikan", "Penyebaran informasi palsu di media sosial"],
            ]}),
  ("p", "Faktor pendorong perlu terus diperkuat, sementara faktor penghambat perlu diwaspadai. Berita palsu yang memanfaatkan isu suku, agama, ras, dan antargolongan sangat berbahaya karena dapat memancing konflik dalam waktu singkat."),

  ("h2", "3.3 Identitas dan Integrasi sebagai Dua Sisi yang Saling Menopang"),
  ("p", "Identitas nasional dan integrasi nasional berkaitan erat. Identitas yang kuat membantu masyarakat mengenali dirinya sebagai satu bangsa, sedangkan integrasi menjaga agar perbedaan tidak berubah menjadi ancaman. Keduanya saling menopang dan tidak dapat dipisahkan."),
  ("p", "Masyarakat yang memiliki identitas nasional yang kuat cenderung lebih tahan terhadap provokasi dan lebih cepat pulih dari konflik. Sebaliknya, masyarakat yang mudah terpecah oleh isu bernuansa SARA menunjukkan bahwa kesadaran integrasinya masih perlu diperkuat."),

  ("h2", "3.4 Peran Mahasiswa dalam Menjaga Integrasi"),
  ("p", "Mahasiswa memiliki posisi strategis dalam menjaga integrasi bangsa. Peran ini dimulai dari hal sederhana, seperti menghargai teman yang berbeda agama, suku, atau daerah asal, serta aktif dalam organisasi yang terbuka dan inklusif. Ketika mahasiswa terbiasa bermusyawarah dan bekerja sama dalam keberagaman, mereka sedang melatih diri menjadi warga negara yang dewasa."),
  ("p", "Di luar kampus, mahasiswa dapat berkontribusi melalui pengabdian masyarakat dan edukasi literasi digital untuk menangkal berita palsu. Menjaga integrasi tidak berarti menutup diri dari kritik. Mahasiswa tetap dapat berpikir kritis terhadap kondisi bangsa, namun menyampaikannya dengan cara yang santun dan berbasis argumen."),

  ("h2", "3.5 Relevansi bagi Mahasiswa Bimbingan dan Konseling"),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, kemampuan menjembatani perbedaan adalah keterampilan inti. Banyak konflik sosial bermula dari komunikasi yang buruk dan kesalahpahaman. Calon konselor yang memahami integrasi nasional akan lebih siap mencairkan ketegangan dan membangun dialog yang sehat."),
  ("p", "Sikap menerima keberagaman tanpa prasangka, yang menjadi inti integrasi, juga menjadi dasar hubungan yang baik antara konselor dan klien dari latar belakang apa pun. Dengan demikian, materi ini memiliki manfaat praktis yang langsung berkaitan dengan profesi."),

  ("h2", "3.6 Rangkuman"),
  ("p", "Integrasi nasional adalah proses menyatukan keberagaman menjadi satu kesatuan bangsa tanpa menghapus perbedaan. Prosesnya didorong oleh rasa senasib, bahasa pemersatu, dan nilai Pancasila, tetapi dihambat oleh ketimpangan, sentimen sempit, dan berita palsu."),
  ("p", "Identitas dan integrasi saling menopang dalam menjaga persatuan. Mahasiswa berperan menjaga integrasi melalui sikap inklusif dan literasi digital, sementara bagi calon konselor kemampuan ini menjadi keterampilan profesional yang berharga."),
 ]
})


# ===================== BAB 4 =====================
BAB.append({
 "no": "4",
 "judul": "NEGARA DAN KONSTITUSI",
 "isi": [
  ("p", "Bab ini membahas negara dan konstitusi sebagai kerangka dasar kehidupan bernegara. Uraian disusun dari pengertian konstitusi, fungsi dan kedudukannya, sejarah singkat UUD 1945, lembaga negara, hingga supremasi konstitusi, agar mahasiswa memahami bahwa seluruh kehidupan bernegara berpijak pada aturan dasar yang mengikat."),

  ("h2", "4.1 Pengertian Konstitusi"),
  ("p", "Setiap negara memerlukan aturan dasar sebagai pedoman penyelenggaraan kehidupan kenegaraan. Aturan dasar inilah yang disebut konstitusi. Tanpa konstitusi, sebuah negara sulit berjalan teratur karena tidak ada kerangka hukum yang menjadi acuan utama. Karena itu, konstitusi sering disebut sebagai hukum tertinggi dalam suatu negara."),
  ("p", "Secara umum, konstitusi mengatur hubungan antara penguasa dan rakyat, antarlembaga negara, serta antara negara dengan warganya. Di dalamnya termuat prinsip pokok tentang pembentukan negara, pembagian kekuasaan, serta hak dan kewajiban setiap pihak. Konstitusi tidak hanya dipahami sebagai dokumen tertulis, tetapi juga sebagai keseluruhan nilai yang menjadi fondasi negara."),
  ("p", "Konstitusi dikenal dalam dua bentuk, yaitu tertulis dan tidak tertulis. Indonesia menganut konstitusi tertulis berupa UUD NRI Tahun 1945, tetapi tetap mengakui konvensi ketatanegaraan, yaitu kebiasaan yang dijalankan secara konsisten dalam praktik kenegaraan."),

  ("h2", "4.2 Fungsi dan Kedudukan Konstitusi"),
  ("p", "Konstitusi menjalankan beberapa fungsi yang menjadikan negara modern bisa berjalan teratur dan adil. Fungsi pertama adalah membatasi kekuasaan agar tidak terpusat dan disalahgunakan. Fungsi kedua adalah mengatur hubungan antarlembaga negara sehingga potensi konflik dapat ditekan. Fungsi ketiga adalah melindungi hak warga negara dari kesewenang-wenangan."),
  ("p", "Pembagian kekuasaan antara lembaga eksekutif, legislatif, dan yudikatif merupakan wujud dari fungsi pembatasan tersebut. Pemerintah memiliki kewenangan, tetapi kewenangan itu tidak boleh melampaui batas yang ditetapkan konstitusi. Dengan demikian, konstitusi menjadi penjaga keseimbangan antara kekuasaan dan hak warga negara."),

  ("h2", "4.3 Sejarah Singkat UUD NRI Tahun 1945"),
  ("p", "UUD NRI Tahun 1945 disahkan pada 18 Agustus 1945 oleh Panitia Persiapan Kemerdekaan Indonesia, sehari setelah proklamasi. Pengesahan yang cepat ini menunjukkan kesadaran para pendiri bangsa akan pentingnya aturan dasar sejak awal kemerdekaan."),
  ("p", "Dalam perjalanannya, Indonesia sempat menggunakan Konstitusi RIS tahun 1949 dan UUDS 1950, sebelum kembali ke UUD 1945 melalui Dekrit Presiden 5 Juli 1959. Babak ini memperlihatkan bahwa pencarian bentuk konstitusional yang sesuai bukan proses yang singkat."),
  ("p", "Pada masa reformasi, UUD 1945 mengalami empat kali amandemen antara tahun 1999 hingga 2002. Amandemen menyentuh penegasan hak asasi manusia, pembatasan masa jabatan presiden, penataan lembaga negara, dan pengaturan pemilihan umum yang lebih demokratis. Penataan peraturan turunannya kemudian diatur melalui Undang-Undang Nomor 12 Tahun 2011 tentang Pembentukan Peraturan Perundang-undangan."),

  ("h2", "4.4 Lembaga Negara dalam Sistem Ketatanegaraan"),
  ("p", "UUD 1945 mengatur lembaga-lembaga negara yang menjalankan pemerintahan. Sistem ketatanegaraan Indonesia menganut pembagian kekuasaan menjadi legislatif, eksekutif, dan yudikatif, dengan modifikasi khas Indonesia, agar tidak ada kekuasaan yang terlalu besar pada satu lembaga."),
  ("table", {"judul": "Tabel 4.1 Lembaga negara dan fungsi pokoknya",
            "head": ["Cabang", "Lembaga", "Fungsi Pokok"],
            "rows": [
              ["Legislatif", "MPR, DPR, DPD", "Menetapkan UUD, membuat undang-undang, mewakili daerah"],
              ["Eksekutif", "Presiden & Wakil Presiden", "Menjalankan pemerintahan dan melaksanakan undang-undang"],
              ["Yudikatif", "MA, MK, KY", "Mengadili, menguji undang-undang, menjaga etika hakim"],
            ]}),
  ("p", "Pembagian ini bukan sekadar urusan tata negara, melainkan wujud pembatasan kekuasaan. Setiap lembaga memiliki kewenangan tersendiri dan saling mengawasi, sehingga kekuasaan tidak berjalan tanpa kendali."),

  ("h2", "4.5 Supremasi Konstitusi"),
  ("p", "Supremasi konstitusi berarti konstitusi berada di atas segala bentuk kekuasaan dan peraturan. Tidak ada pejabat, lembaga, atau kelompok yang boleh bertindak di luar koridor konstitusi. Prinsip ini menjadi fondasi negara hukum, karena tanpa supremasi konstitusi, hak warga mudah dilanggar dan kekuasaan rentan disalahgunakan."),
  ("p", "Di Indonesia, supremasi konstitusi dijaga melalui pengujian peraturan oleh Mahkamah Konstitusi dan Mahkamah Agung, pemilihan umum yang demokratis, kebebasan pers, serta peradilan yang independen. Seluruh aturan yang berlaku, dari tingkat daerah hingga pusat, harus dapat ditelusuri kembali ke UUD 1945 sebagai sumber otoritas tertinggi."),

  ("h2", "4.6 Peran Mahasiswa dan Relevansi bagi Calon Konselor"),
  ("p", "Mahasiswa berperan sebagai pembelajar kritis yang membaca konstitusi secara langsung, sebagai pengawas sosial yang menilai kebijakan publik, dan sebagai pelopor ketaatan hukum melalui sikap sehari-hari, seperti menolak plagiarisme dan tidak menyebarkan informasi palsu."),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, pemahaman konstitusi berguna karena banyak persoalan klien memiliki dimensi hukum, seperti perlindungan anak, kekerasan dalam rumah tangga, atau hak-hak individu. Pengetahuan ini membantu calon konselor mengenali batas kewenangannya dan mengarahkan klien pada penyelesaian yang tepat."),

  ("h2", "4.7 Rangkuman"),
  ("p", "Konstitusi adalah aturan dasar tertinggi yang membatasi kekuasaan, mengatur hubungan antarlembaga, dan melindungi hak warga negara. UUD NRI Tahun 1945 telah melewati sejarah panjang dan empat kali amandemen untuk menyempurnakan sistem ketatanegaraan."),
  ("p", "Lembaga negara dibagi ke dalam cabang legislatif, eksekutif, dan yudikatif yang saling mengawasi. Supremasi konstitusi menjamin bahwa seluruh aturan berpijak pada UUD 1945. Mahasiswa, termasuk calon konselor, perlu memahami konstitusi sebagai bekal bersikap kritis dan taat hukum."),
 ]
})

# ===================== BAB 5 =====================
BAB.append({
 "no": "5",
 "judul": "HAK DAN KEWAJIBAN WARGA NEGARA",
 "isi": [
  ("p", "Bab ini membahas hak dan kewajiban warga negara serta hak asasi manusia. Pembahasan disusun dari pengertian, hubungan antara hak, kewajiban, dan tanggung jawab, dasar hukum, hingga relevansinya dengan kehidupan mahasiswa. Pemahaman ini penting agar warga negara dapat hidup berdampingan secara adil dan teratur."),

  ("h2", "5.1 Pengertian Hak dan Kewajiban Warga Negara"),
  ("p", "Hak warga negara adalah kewenangan yang melekat pada setiap warga sebagai bagian dari keanggotaannya dalam suatu negara. Hak ini dijamin oleh konstitusi dan peraturan perundang-undangan, sehingga negara berkewajiban melindungi dan menyediakannya. Tanpa pengakuan dan perlindungan hukum, hak warga mudah dilanggar oleh pihak yang lebih berkuasa."),
  ("p", "Kewajiban warga negara adalah hal-hal yang harus dilakukan sebagai konsekuensi dari keanggotaannya, seperti menaati hukum, menghormati hak orang lain, dan ikut serta dalam pembelaan negara. Hak dan kewajiban berjalan seiring. Warga negara tidak dapat hanya menuntut hak tanpa menjalankan kewajiban, demikian pula sebaliknya."),

  ("h2", "5.2 Hubungan Hak, Kewajiban, dan Tanggung Jawab"),
  ("p", "Hak dan kewajiban sebaiknya dilihat dalam kerangka tanggung jawab yang lebih luas. Tanggung jawab adalah kesadaran menjalankan apa yang seharusnya dilakukan, bukan semata karena ada aturan yang memaksa. Kepatuhan tanpa rasa tanggung jawab hanya bersifat permukaan dan mudah hilang ketika pengawasan tidak ada."),
  ("p", "Sebagai contoh, ketika seseorang menggunakan haknya untuk berpendapat, ia juga berkewajiban untuk tidak menyinggung hak orang lain dan bertanggung jawab memastikan pendapatnya tidak menyesatkan. Ketika seseorang menjalankan hak beragama, ia berkewajiban menghormati agama orang lain dan bertanggung jawab menjaga kerukunan. Ketiganya berjalan bersama dalam setiap aspek kehidupan."),

  ("h2", "5.3 Hak Asasi Manusia dalam Kehidupan Bernegara"),
  ("p", "Hak asasi manusia memiliki cakupan yang lebih luas daripada hak warga negara. Hak asasi melekat pada setiap manusia semata karena ia manusia, tanpa memandang suku, agama, ras, jenis kelamin, atau kewarganegaraan. Karena itu, orang asing yang berada di wilayah Indonesia pun memiliki hak asasi yang harus dihormati."),
  ("p", "Berbeda dari hak warga negara yang diperoleh karena status kewarganegaraan, hak asasi bersifat universal dan tidak dapat dicabut oleh negara mana pun. Indonesia mengakui dan melindungi hak asasi melalui UUD NRI Tahun 1945 dan Undang-Undang Nomor 39 Tahun 1999 tentang Hak Asasi Manusia, serta membentuk Komisi Nasional Hak Asasi Manusia sebagai lembaga pengawas."),
  ("table", {"judul": "Tabel 5.1 Perbedaan hak warga negara dan hak asasi manusia",
            "head": ["Aspek", "Hak Warga Negara", "Hak Asasi Manusia"],
            "rows": [
              ["Dasar", "Status kewarganegaraan", "Kemanusiaan sejak lahir"],
              ["Cakupan", "Warga negara tertentu", "Setiap manusia, universal"],
              ["Sifat", "Diatur hukum nasional", "Tidak dapat dicabut negara"],
            ]}),

  ("h2", "5.4 Perlindungan dan Pelanggaran Hak Asasi Manusia"),
  ("p", "Perlindungan hak asasi di Indonesia dilakukan melalui jalur hukum dan kelembagaan. Hukum menjadi instrumen utama untuk menjamin hak dasar tidak dilanggar, sekaligus mencegah pelanggaran sejak awal. Secara kelembagaan, Komisi Nasional Hak Asasi Manusia menjalankan pengkajian, pemantauan, dan mediasi, sementara pengadilan menangani perkara pelanggaran berat."),
  ("p", "Meski kerangka perlindungan sudah ada, pelanggaran tetap bisa terjadi, mulai dari diskriminasi, kekerasan, hingga pembatasan kebebasan secara sewenang-wenang. Dampaknya luas, bukan hanya bagi korban dan keluarganya, tetapi juga bagi kepercayaan masyarakat terhadap negara. Ketika pelanggaran tidak diselesaikan secara adil, keyakinan bahwa hukum melindungi semua orang akan terkikis."),

  ("h2", "5.5 Etika Hak Asasi Manusia di Media Sosial"),
  ("p", "Salah satu tantangan nyata terkait hak asasi bagi generasi sekarang adalah penggunaan media sosial. Kebebasan berekspresi di ruang digital sangat luas, tetapi tidak tanpa batas. Menyebarkan ujaran kebencian, mempermalukan orang lain, atau menyebarkan informasi palsu yang merugikan seseorang adalah bentuk pelanggaran hak asasi, meskipun terjadi di ruang maya."),
  ("p", "Hak satu orang dibatasi oleh hak orang lain. Etika bermedia sosial yang baik mencakup memverifikasi informasi sebelum menyebarkannya, menghindari serangan pribadi, menghormati privasi, dan bersikap kritis tanpa kasar. Sikap ini merupakan bagian dari tanggung jawab kewarganegaraan di era digital."),

  ("h2", "5.6 Relevansi bagi Mahasiswa Bimbingan dan Konseling"),
  ("p", "Bagi calon konselor, penghormatan terhadap martabat manusia adalah inti dari profesi. Prinsip menghargai setiap individu tanpa diskriminasi sejalan langsung dengan nilai hak asasi manusia. Konselor dituntut menjaga kerahasiaan, bersikap adil, dan tidak menghakimi klien."),
  ("p", "Pemahaman tentang hak, kewajiban, dan hak asasi membantu calon konselor mengenali ketika persoalan klien menyangkut pelanggaran hak, seperti perundungan atau kekerasan. Dengan begitu, konselor dapat bersikap tepat, melindungi korban, dan tidak mengambil keputusan yang merugikan pihak tertentu."),

  ("h2", "5.7 Rangkuman"),
  ("p", "Hak dan kewajiban warga negara berjalan seiring dalam kerangka tanggung jawab. Hak asasi manusia memiliki cakupan universal yang melekat pada setiap manusia, dijamin oleh UUD NRI Tahun 1945 dan Undang-Undang Nomor 39 Tahun 1999."),
  ("p", "Perlindungan hak asasi dilakukan melalui jalur hukum dan kelembagaan, meski pelanggaran masih bisa terjadi dan berdampak pada kepercayaan publik. Etika di media sosial menjadi wujud tanggung jawab kewarganegaraan modern, sementara bagi calon konselor penghormatan terhadap martabat manusia adalah dasar profesi."),
 ]
})


# ===================== BAB 6 =====================
BAB.append({
 "no": "6",
 "judul": "PENEGAKAN HUKUM YANG BERKEADILAN",
 "isi": [
  ("p", "Bab ini membahas penegakan hukum yang berkeadilan dengan bertumpu pada konsep negara hukum. Uraian disusun dari pengertian negara hukum, prinsip-prinsipnya, sistem peradilan, tantangan, hingga peran mahasiswa, agar terlihat bahwa keadilan tidak cukup tertulis dalam aturan, tetapi harus ditegakkan secara nyata."),

  ("h2", "6.1 Pengertian Negara Hukum"),
  ("p", "Negara hukum adalah konsep yang menempatkan hukum sebagai dasar utama penyelenggaraan pemerintahan. Dalam negara hukum, setiap tindakan pemerintah harus memiliki dasar hukum, dan tidak ada pihak yang boleh bertindak sewenang-wenang. Konsep ini lahir sebagai respons terhadap penyalahgunaan kekuasaan yang banyak terjadi dalam sejarah ketatanegaraan."),
  ("p", "Secara sederhana, negara hukum berarti kekuasaan dibatasi oleh hukum. Pejabat negara, sekuat apa pun jabatannya, tetap tunduk pada aturan yang berlaku. Indonesia menegaskan dirinya sebagai negara hukum dalam Pasal 1 ayat (3) UUD NRI Tahun 1945. Penegasan ini membedakan Indonesia dari negara yang dijalankan semata berdasarkan kehendak penguasa."),
  ("p", "Negara hukum juga berarti warga negara berhak dilindungi dan diperlakukan adil. Hukum tidak hanya berlaku bagi rakyat, tetapi juga bagi pemerintah. Jika pemerintah keliru, rakyat berhak mengkritik dan memperjuangkan keadilan melalui jalur hukum yang tersedia."),

  ("h2", "6.2 Prinsip-Prinsip Negara Hukum"),
  ("p", "Negara hukum berpijak pada sejumlah prinsip yang memastikan hukum benar-benar menjaga keadilan. Prinsip persamaan di hadapan hukum menegaskan bahwa semua orang memiliki kedudukan yang sama tanpa memandang status. Prinsip perlindungan hak menuntut negara menjamin hak dasar warga. Prinsip pembatasan kekuasaan mencegah kekuasaan terpusat melalui mekanisme saling mengawasi."),
  ("p", "Ketiga prinsip ini tidak berdiri sendiri, melainkan saling melengkapi. Persamaan di hadapan hukum kehilangan makna tanpa perlindungan hak yang nyata, dan perlindungan hak sulit terwujud bila kekuasaan tidak dibatasi. Karena itu, penegakan hukum yang berkeadilan menuntut ketiganya berjalan bersama."),

  ("h2", "6.3 Sistem Peradilan di Indonesia"),
  ("p", "Sistem peradilan adalah mekanisme yang disediakan negara untuk menyelesaikan sengketa, mengadili pelanggaran, dan memberikan keadilan. Kewenangan kekuasaan kehakiman diatur dalam Undang-Undang Nomor 48 Tahun 2009, sedangkan tugas kepolisian dalam penegakan hukum diatur dalam Undang-Undang Nomor 2 Tahun 2002."),
  ("table", {"judul": "Tabel 6.1 Lingkungan peradilan di Indonesia",
            "head": ["Lingkungan Peradilan", "Wewenang Pokok"],
            "rows": [
              ["Peradilan Umum", "Perkara pidana dan perdata"],
              ["Peradilan Agama", "Perkara perkawinan, waris, dan keluarga bagi umat Islam"],
              ["Peradilan Militer", "Pelanggaran yang dilakukan prajurit"],
              ["Peradilan Tata Usaha Negara", "Sengketa warga dengan pejabat pemerintah"],
              ["Mahkamah Konstitusi", "Pengujian undang-undang terhadap UUD 1945"],
            ]}),
  ("p", "Prinsip utama dalam sistem peradilan adalah peradilan yang adil, terbuka, dan tidak memihak. Setiap pihak berhak didengar dan menyampaikan bukti, sedangkan putusan hakim harus berdasarkan hukum, bukan tekanan atau kepentingan tertentu."),

  ("h2", "6.4 Supremasi Hukum dan Tantangannya"),
  ("p", "Supremasi hukum menyatakan bahwa hukum berada di posisi tertinggi dalam kehidupan bernegara. Tidak ada kekuasaan atau golongan yang boleh berada di atas hukum. Ketika hukum ditegakkan tanpa pandang bulu, masyarakat merasa aman dan percaya pada negara. Sebaliknya, hukum yang tajam ke bawah tetapi tumpul ke atas akan mengikis kepercayaan publik."),
  ("p", "Penegakan supremasi hukum di Indonesia masih menghadapi tantangan. Ketimpangan akses terhadap keadilan membuat sebagian masyarakat, terutama yang lemah secara ekonomi, sulit memperjuangkan haknya. Rendahnya kesadaran hukum membuat sebagian warga rentan menjadi korban. Penyalahgunaan kekuasaan dan lemahnya integritas sebagian aparat juga menggerus kepercayaan terhadap sistem hukum."),

  ("h2", "6.5 Budaya Hukum dalam Masyarakat"),
  ("p", "Budaya hukum adalah kebiasaan masyarakat dalam memahami, menaati, dan menghargai hukum. Hukum tidak akan berjalan baik bila hanya tertulis tanpa menjadi kebiasaan sehari-hari. Budaya hukum yang baik tampak dari hal sederhana, seperti menaati aturan lalu lintas, tidak main hakim sendiri, dan menghormati hak orang lain."),
  ("p", "Sebaliknya, budaya hukum melemah ketika pelanggaran dianggap biasa, seperti membenarkan suap kecil atau menyelesaikan masalah dengan kekerasan. Di lingkungan kampus, budaya hukum tampak dari sikap menaati aturan akademik, menolak plagiarisme, dan menyelesaikan konflik dengan cara yang baik."),

  ("h2", "6.6 Peran Mahasiswa dan Relevansi bagi Calon Konselor"),
  ("p", "Mahasiswa berperan membangun budaya hukum melalui keteladanan menaati aturan, peningkatan literasi hukum, dan keberanian menyuarakan keadilan tanpa main hakim sendiri. Kritik terhadap ketidakadilan sebaiknya disampaikan melalui cara yang sah, seperti dialog, tulisan, atau pelaporan ke lembaga berwenang."),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, pemahaman negara hukum membantu mengenali kasus yang menyangkut hak dan perlindungan hukum, seperti kekerasan atau diskriminasi. Calon konselor yang peka hukum akan lebih berhati-hati, tidak menyalahkan korban, dan mampu mengarahkan klien pada penyelesaian yang tepat. Prinsip menjaga kerahasiaan dan menghormati martabat klien sejalan dengan nilai negara hukum."),

  ("h2", "6.7 Rangkuman"),
  ("p", "Negara hukum menempatkan hukum sebagai dasar utama yang membatasi kekuasaan dan melindungi hak warga, sebagaimana ditegaskan dalam Pasal 1 ayat (3) UUD NRI Tahun 1945. Prinsip persamaan di hadapan hukum, perlindungan hak, dan pembatasan kekuasaan menjadi pijakannya."),
  ("p", "Sistem peradilan menyediakan jalan bagi keadilan, namun penegakannya masih terhambat oleh ketimpangan akses dan lemahnya integritas. Budaya hukum, peran mahasiswa, dan kepekaan calon konselor menjadi penopang agar hukum benar-benar berkeadilan."),
 ]
})

# ===================== BAB 7 =====================
BAB.append({
 "no": "7",
 "judul": "GEOPOLITIK DAN GEOSTRATEGI",
 "isi": [
  ("p", "Bab ini membahas geopolitik dan geostrategi Indonesia melalui konsep wawasan nusantara dan ketahanan nasional. Uraian disusun dari pengertian, kedudukan, unsur, hingga ancaman dan peran mahasiswa, agar terlihat bahwa menjaga persatuan dan kedaulatan adalah tanggung jawab bersama seluruh warga negara."),

  ("h2", "7.1 Wawasan Nusantara sebagai Geopolitik Indonesia"),
  ("p", "Wawasan nusantara adalah cara pandang bangsa Indonesia terhadap diri dan lingkungannya berdasarkan Pancasila dan UUD NRI Tahun 1945, dengan mengutamakan persatuan dan kesatuan wilayah. Sebagai negara kepulauan terbesar di dunia, Indonesia memiliki tantangan geografis yang unik, dengan ribuan pulau dan keragaman budaya yang menjadi kekayaan sekaligus tantangan."),
  ("p", "Wawasan nusantara hadir sebagai konsep pemersatu. Seluruh wilayah Indonesia, dari Sabang sampai Merauke, dipandang sebagai satu kesatuan yang tidak terpisahkan. Laut yang memisahkan pulau bukan penghalang, melainkan penghubung. Konsep inilah yang menjadi geopolitik Indonesia, yaitu landasan negara dalam memandang wilayah dan menjaga kepentingan nasional."),
  ("p", "Dalam kehidupan sehari-hari, wawasan nusantara mendorong setiap warga berpikir dengan perspektif kebangsaan, bukan sekadar kepentingan daerah atau kelompok. Ketika seseorang hanya mementingkan kelompoknya tanpa melihat kepentingan nasional, integrasi bangsa dapat terganggu."),

  ("h2", "7.2 Kedudukan dan Unsur Wawasan Nusantara"),
  ("p", "Wawasan nusantara memiliki kedudukan penting dalam pertahanan, pembangunan, dan kehidupan sosial budaya. Dalam pertahanan, seluruh wilayah harus dijaga secara merata. Dalam pembangunan, ia mendorong pemerataan agar tidak terpusat di kota besar. Dalam sosial budaya, ia menegaskan bahwa keberagaman adalah kekayaan yang memperkuat identitas nasional."),
  ("p", "Wawasan nusantara dibangun dari beberapa unsur, yaitu wilayah, bangsa, dan budaya. Wilayah mencakup darat, laut, dan udara dalam batas kedaulatan Indonesia. Bangsa terdiri atas ratusan suku yang dipersatukan oleh sejarah dan cita-cita bersama. Budaya merupakan akumulasi kebudayaan daerah yang hidup berdampingan dan dihormati sebagai bagian dari identitas nasional."),

  ("h2", "7.3 Geostrategi dan Ketahanan Nasional"),
  ("p", "Geostrategi adalah strategi nasional yang disusun berdasarkan kondisi geografis dan berbagai aspek kehidupan bangsa untuk mencapai tujuan nasional. Salah satu wujudnya adalah ketahanan nasional, yaitu kemampuan bangsa menjaga keberlangsungan hidup, persatuan, dan stabilitas dalam menghadapi tantangan dari dalam maupun luar. Landasan pertahanannya antara lain diatur dalam Undang-Undang Nomor 3 Tahun 2002 tentang Pertahanan Negara."),
  ("p", "Ketahanan nasional tidak hanya soal kekuatan militer, melainkan mencakup banyak dimensi yang harus dibangun secara seimbang. Negara yang kuat secara ekonomi tetapi rapuh secara sosial tetap rentan, demikian pula sebaliknya."),
  ("table", {"judul": "Tabel 7.1 Dimensi ketahanan nasional",
            "head": ["Dimensi", "Fokus"],
            "rows": [
              ["Ideologi", "Menjaga Pancasila sebagai pegangan hidup"],
              ["Politik", "Stabilitas pemerintahan yang demokratis"],
              ["Ekonomi", "Kemandirian dan pemerataan kesejahteraan"],
              ["Sosial Budaya", "Hidup bersama dalam keberagaman"],
              ["Pertahanan & Keamanan", "Perlindungan kedaulatan negara"],
            ]}),

  ("h2", "7.4 Ancaman terhadap Ketahanan Nasional"),
  ("p", "Ketahanan nasional menghadapi ancaman yang tidak selalu berbentuk fisik. Disintegrasi dapat muncul dari konflik daerah dan ketimpangan ekonomi yang tidak dikelola. Konflik sosial dapat tumbuh dari perbedaan yang dipertajam oleh kepentingan tertentu."),
  ("p", "Di era digital, berita palsu dan disinformasi menjadi ancaman serius karena dapat memecah belah masyarakat dengan cepat. Penyebaran informasi yang tidak benar dapat membuat masyarakat saling curiga, mendukung kebijakan yang merugikan, atau terlibat konflik akibat informasi yang keliru. Karena itu, ketahanan informasi menjadi bagian penting dari ketahanan nasional masa kini."),

  ("h2", "7.5 Peran Mahasiswa dan Relevansi bagi Calon Konselor"),
  ("p", "Mahasiswa dapat menjaga wawasan nusantara dan ketahanan nasional melalui hal sederhana yang konsisten, seperti menjaga persatuan dalam keberagaman, meningkatkan literasi digital, menghargai budaya daerah, dan berpartisipasi dalam kegiatan positif. Literasi digital yang baik menjadi benteng pertama menghadapi ancaman informasi."),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, wawasan nusantara membantu mengembangkan empati lintas budaya, sehingga calon konselor tidak mudah berprasangka terhadap klien dari latar berbeda. Ketahanan nasional pada tingkat individu juga berkaitan dengan ketahanan psikologis, dan di sinilah peran konselor membantu individu menghadapi tekanan turut menyumbang pada kekuatan bangsa secara keseluruhan."),

  ("h2", "7.6 Rangkuman"),
  ("p", "Wawasan nusantara adalah cara pandang yang menempatkan seluruh wilayah Indonesia sebagai satu kesatuan, sekaligus menjadi geopolitik Indonesia. Geostrategi diwujudkan melalui ketahanan nasional yang mencakup dimensi ideologi, politik, ekonomi, sosial budaya, serta pertahanan dan keamanan."),
  ("p", "Ancaman terhadap ketahanan nasional kini banyak berbentuk disinformasi digital. Mahasiswa berperan menjaga persatuan dan literasi digital, sementara bagi calon konselor wawasan ini memperkuat empati lintas budaya dan kepedulian terhadap ketahanan psikologis individu."),
 ]
})


# ===================== BAB 8 (BARU) =====================
BAB.append({
 "no": "8",
 "judul": "ANTI KORUPSI",
 "isi": [
  ("p", "Bab ini membahas anti korupsi sebagai materi penutup yang merangkum pentingnya integritas dalam kehidupan berbangsa. Pembahasan disusun dari pengertian korupsi, dasar hukum, bentuk dan dampaknya, nilai-nilai antikorupsi, hingga peran perguruan tinggi dan mahasiswa. Korupsi dipandang bukan sekadar pelanggaran hukum, melainkan persoalan moral yang menuntut pencegahan sejak dini."),

  ("h2", "8.1 Pengertian Korupsi"),
  ("p", "Korupsi adalah penyalahgunaan kekuasaan, jabatan, atau kepercayaan untuk memperoleh keuntungan pribadi atau kelompok yang merugikan kepentingan umum. Korupsi tidak selalu berbentuk pencurian uang secara langsung. Suap, gratifikasi, penggelapan, penyalahgunaan wewenang, dan penggelembungan anggaran termasuk dalam wujud korupsi."),
  ("p", "Korupsi perlu dipahami sebagai persoalan sistemik yang merusak banyak sendi kehidupan. Ketika korupsi dibiarkan, masyarakat lambat laun menganggap ketidakjujuran sebagai hal biasa. Inilah yang membuat korupsi lebih berbahaya daripada pelanggaran hukum biasa, karena dampaknya menjangkau cara berpikir masyarakat secara luas."),

  ("h2", "8.2 Dasar Hukum Pemberantasan Korupsi"),
  ("p", "Indonesia memiliki landasan hukum yang tegas dalam pemberantasan korupsi. Aturan ini menjadi dasar bagi penindakan sekaligus pencegahan, dan menempatkan korupsi sebagai kejahatan serius yang merugikan negara dan masyarakat."),
  ("table", {"judul": "Tabel 8.1 Landasan pemberantasan korupsi di Indonesia",
            "head": ["Landasan", "Pokok Pengaturan"],
            "rows": [
              ["UU No. 31 Tahun 1999", "Pemberantasan tindak pidana korupsi"],
              ["UU No. 20 Tahun 2001", "Perubahan dan penguatan atas UU No. 31 Tahun 1999"],
              ["Komisi Pemberantasan Korupsi", "Lembaga pencegahan dan penindakan korupsi"],
            ]}),
  ("p", "Selain penindakan, Komisi Pemberantasan Korupsi juga mengembangkan pendidikan antikorupsi melalui berbagai materi pembelajaran yang dapat diakses publik. Hal ini menegaskan bahwa pemberantasan korupsi tidak cukup mengandalkan hukuman, tetapi juga membutuhkan pembentukan kesadaran."),

  ("h2", "8.3 Bentuk dan Dampak Korupsi"),
  ("p", "Korupsi hadir dalam beragam bentuk, mulai dari suap untuk memuluskan urusan, gratifikasi yang menyamar sebagai hadiah, hingga pemerasan oleh pihak yang memiliki kewenangan. Mengenali berbagai bentuk ini penting agar masyarakat tidak menganggap praktik tertentu sebagai hal yang wajar, misalnya memberi uang pelicin untuk mempercepat layanan."),
  ("p", "Dampak korupsi terasa pada banyak sisi. Secara ekonomi, anggaran yang seharusnya untuk pendidikan dan kesehatan justru mengalir ke pihak tertentu. Secara sosial, korupsi memperlebar ketimpangan dan menurunkan kepercayaan terhadap negara. Secara moral, korupsi menumbuhkan budaya permisif terhadap ketidakjujuran. Rakyat kecil sering kali menjadi pihak yang paling dirugikan."),

  ("h2", "8.4 Nilai-Nilai Antikorupsi"),
  ("p", "Pendidikan antikorupsi bertumpu pada penanaman nilai, bukan sekadar pengetahuan tentang hukum. Nilai-nilai ini menjadi fondasi karakter yang membuat seseorang menolak korupsi sejak dari niat."),
  ("table", {"judul": "Tabel 8.2 Nilai dasar antikorupsi dan wujudnya bagi mahasiswa",
            "head": ["Nilai", "Wujud Nyata di Kampus"],
            "rows": [
              ["Kejujuran", "Tidak menyontek dan tidak memanipulasi data"],
              ["Tanggung jawab", "Menyelesaikan tugas tanpa menyalahgunakan kepercayaan"],
              ["Disiplin", "Menaati aturan tanpa mencari jalan pintas"],
              ["Keberanian", "Menolak ajakan curang dan melaporkan penyimpangan"],
              ["Kesederhanaan", "Tidak memaksakan gaya hidup berlebihan"],
            ]}),
  ("p", "Nilai-nilai ini tampak sederhana, tetapi justru di situlah pendidikan antikorupsi diuji. Gaya hidup berlebihan dan keinginan kaya secara instan sering menjadi pintu masuk perilaku koruptif, sehingga penanaman nilai sejak masa kuliah menjadi sangat penting."),

  ("h2", "8.5 Korupsi dalam Kehidupan Sehari-Hari"),
  ("p", "Korupsi sering dibayangkan sebagai kejahatan pejabat besar, padahal benihnya muncul dalam keseharian. Menyontek, menitipkan tanda tangan kehadiran, atau memanipulasi laporan kegiatan adalah contoh kecil yang mencerminkan sikap tidak jujur. Bila dianggap sepele, kebiasaan ini dapat berkembang menjadi penyimpangan yang lebih besar ketika seseorang memegang wewenang."),
  ("p", "Karena itu, pendidikan antikorupsi harus menyentuh perilaku sehari-hari, bukan hanya membahas kasus besar yang terasa jauh. Kesadaran untuk jujur dalam hal kecil adalah latihan paling nyata dalam membangun integritas."),

  ("h2", "8.6 Peran Perguruan Tinggi dan Mahasiswa"),
  ("p", "Perguruan tinggi memikul tanggung jawab menanamkan nilai antikorupsi, tidak hanya melalui materi kuliah, tetapi juga melalui budaya dan tata kelola kampus. Kampus yang membiarkan plagiarisme atau kecurangan organisasi sebenarnya sedang menormalkan benih korupsi, sedangkan kampus yang tegas terhadap ketidakjujuran sedang menanam fondasi integritas."),
  ("p", "Mahasiswa berperan sebagai pelopor kejujuran melalui integritas akademik, serta sebagai agen yang menyebarkan kesadaran antikorupsi di lingkungannya. Keberanian moral untuk menolak korupsi tidak harus berwujud aksi besar, tetapi terutama tampak dalam keputusan jujur sehari-hari."),

  ("h2", "8.7 Relevansi bagi Mahasiswa Bimbingan dan Konseling"),
  ("p", "Bagi calon konselor, integritas adalah syarat utama profesi. Seorang konselor dipercaya menjaga kerahasiaan dan bersikap jujur terhadap klien. Kebiasaan jujur yang dilatih sejak masa kuliah menjadi modal penting agar kelak tidak menyalahgunakan kepercayaan yang diberikan."),
  ("p", "Selain itu, konselor dapat berperan menumbuhkan karakter jujur dan tanggung jawab pada individu yang dibimbingnya. Dengan demikian, nilai antikorupsi tidak berhenti pada diri konselor, tetapi turut disebarkan melalui layanan yang diberikannya kepada orang lain."),

  ("h2", "8.8 Rangkuman dan Penutup"),
  ("p", "Korupsi adalah penyalahgunaan kepercayaan untuk keuntungan pribadi yang merugikan kepentingan umum, dengan dampak luas pada ekonomi, kehidupan sosial, dan moral bangsa. Pengaturannya tertuang dalam Undang-Undang Nomor 31 Tahun 1999 dan Undang-Undang Nomor 20 Tahun 2001."),
  ("p", "Pencegahan korupsi bertumpu pada penanaman nilai kejujuran, tanggung jawab, dan keberanian, yang dimulai dari kehidupan sehari-hari dan lingkungan kampus. Sebagai penutup mini book ini, materi antikorupsi merangkum semangat seluruh pembahasan, yaitu membentuk mahasiswa menjadi warga negara yang berintegritas, sadar hukum, dan siap berkontribusi bagi bangsa."),
 ]
})


# ===================== PENDALAMAN (disisipkan sebelum Rangkuman tiap bab) =====================
import re as _re
EXTRA = {
 "1": [
  ("h2", "Tujuan dan Fungsi yang Lebih Rinci"),
  ("p", "Tujuan Pendidikan Kewarganegaraan di perguruan tinggi tidak sederhana. Mahasiswa diharapkan tidak hanya mengetahui apa itu negara, hukum, konstitusi, dan demokrasi, tetapi juga memiliki kesadaran untuk menjalankan perannya secara nyata dalam kehidupan sehari-hari. Pengetahuan menjadi bermakna ketika diwujudkan dalam sikap dan tindakan."),
  ("p", "Fungsi mata kuliah ini dapat dilihat dari tiga arah yang saling melengkapi. Sebagai wahana pembentukan karakter kebangsaan, ia menjaga agar mahasiswa tetap memiliki pijakan nilai di tengah berbagai pengaruh. Sebagai sarana penajaman nalar, ia melatih mahasiswa melihat persoalan bangsa secara objektif, menganalisis penyebabnya, dan menempatkan diri sebagai bagian dari solusi. Sebagai ruang pembentukan partisipasi, ia mendorong mahasiswa terlibat dalam kegiatan sosial dan kehidupan kampus yang sehat."),
  ("p", "Dengan ketiga fungsi tersebut, Pendidikan Kewarganegaraan menjadi lebih dari sekadar penyampaian materi. Ia menjadi proses pembentukan warga negara yang utuh, yang memadukan pengetahuan, sikap, dan keterampilan dalam menjalani kehidupan berbangsa."),
  ("h2", "Tantangan Pelaksanaan di Era Digital"),
  ("p", "Pelaksanaan Pendidikan Kewarganegaraan di era digital menghadapi tantangan yang semakin kompleks. Tantangan pertama adalah banjir informasi yang tidak selalu disertai kualitas kebenaran yang baik. Mahasiswa hidup di tengah media sosial yang menyajikan informasi secara cepat, tetapi sering tanpa proses verifikasi, sehingga berita keliru dan provokasi mudah memengaruhi cara berpikir."),
  ("p", "Tantangan berikutnya adalah meningkatnya kecenderungan individualisme dan sikap apatis terhadap persoalan bersama. Kemajuan teknologi memberi banyak manfaat, tetapi juga dapat membuat sebagian orang lebih sibuk dengan dunia pribadi. Selain itu, mahasiswa kadang menyaksikan jarak antara nilai yang diajarkan dan praktik yang terjadi di ruang publik, yang bila tidak disikapi dengan tepat dapat menumbuhkan sikap sinis."),
  ("p", "Karena itu, Pendidikan Kewarganegaraan perlu dikelola secara kontekstual dan dialogis, menyentuh persoalan nyata yang dihadapi mahasiswa. Dengan pendekatan seperti itu, mahasiswa akan melihat bahwa mata kuliah ini tetap relevan, bahkan semakin dibutuhkan di tengah perubahan zaman yang cepat."),
 ],
 "2": [
  ("h2", "Sejarah Pembentukan Identitas Nasional"),
  ("p", "Identitas nasional Indonesia terbentuk melalui pengalaman sejarah yang panjang. Pengalaman dijajah selama berabad-abad justru menumbuhkan kesadaran bahwa berbagai suku dan daerah memiliki nasib yang sama dan perlu bersatu. Dari kesadaran inilah benih identitas kebangsaan mulai tumbuh."),
  ("p", "Peristiwa seperti Kebangkitan Nasional, Sumpah Pemuda, dan Proklamasi Kemerdekaan menjadi tonggak yang memperkuat rasa kebangsaan. Identitas nasional dengan demikian bukan pemberian yang turun begitu saja, melainkan hasil perjuangan dan kesadaran kolektif yang diwariskan antargenerasi. Memahami sejarah ini membantu mahasiswa menyadari mengapa persatuan layak dijaga."),
  ("h2", "Identitas Nasional dan Generasi Digital"),
  ("p", "Generasi muda saat ini tumbuh bersama teknologi digital dan menyerap banyak nilai dari luar negeri. Identitas nasional dapat melemah bila mereka lebih mengagumi budaya asing daripada budayanya sendiri. Namun teknologi juga membuka peluang, karena banyak anak muda justru memanfaatkan media sosial untuk memperkenalkan budaya Indonesia ke panggung yang lebih luas."),
  ("p", "Kunci dari semuanya terletak pada sikap. Teknologi sebaiknya dilihat sebagai alat, bukan tujuan. Bila digunakan dengan bijak, dunia digital dapat menjadi sarana memperkuat identitas nasional. Mahasiswa dapat menjadi teladan dengan menampilkan kebanggaan terhadap bangsa melalui karya digital yang positif dan bermutu."),
 ],
 "3": [
  ("h2", "Toleransi sebagai Kunci Kerukunan"),
  ("p", "Integrasi nasional membutuhkan toleransi sebagai perekat. Toleransi berarti bersedia hidup berdampingan dengan mereka yang berbeda, sekaligus menghormati hak setiap orang untuk menjadi dirinya sendiri. Tanpa toleransi, keberagaman yang dimiliki Indonesia mudah berubah menjadi sumber gesekan."),
  ("p", "Meski demikian, toleransi tetap memiliki batas. Sikap menghargai perbedaan tidak berarti membiarkan segala hal terjadi, termasuk yang melanggar hukum atau nilai kemanusiaan. Toleransi yang sehat selalu disertai prinsip, sehingga kerukunan yang terbangun bukan kerukunan semu, melainkan kerukunan yang berpijak pada keadilan."),
  ("h2", "Relevansi dalam Kehidupan Kampus dan Masyarakat"),
  ("p", "Di kampus, identitas dan integrasi terlihat dari cara mahasiswa bergaul dan menyelesaikan perbedaan pendapat. Ketika mahasiswa dari berbagai daerah bekerja sama dalam satu kelompok tanpa mempersoalkan perbedaan, itu adalah contoh nyata integrasi yang berhasil. Sebaliknya, sikap eksklusif berdasarkan suku atau daerah menandakan kesadaran integrasi yang masih perlu diperkuat."),
  ("p", "Di masyarakat, integrasi terlihat dari kemampuan warga hidup berdampingan dan menghadapi krisis bersama. Masyarakat dengan identitas nasional yang kuat lebih tahan terhadap provokasi dan lebih cepat pulih dari konflik. Bagi mahasiswa Bimbingan dan Konseling, kepekaan terhadap keberagaman ini menjadi bekal untuk memahami klien tanpa prasangka dan membantu mereka secara lebih efektif."),
 ],
 "4": [
  ("h2", "Hak dan Kewajiban Warga Negara dalam UUD 1945"),
  ("p", "UUD NRI Tahun 1945 tidak hanya mengatur struktur pemerintahan, tetapi juga menjamin hak dan menetapkan kewajiban warga negara. Hak yang dijamin mencakup hak hidup, hak beragama, hak berpendapat, hak berserikat, hak atas pendidikan, hak atas pekerjaan yang layak, serta hak memperoleh keadilan dan perlindungan hukum."),
  ("p", "Di sisi lain, warga negara memiliki kewajiban untuk menaati hukum, ikut serta dalam pembelaan negara, dan menghormati hak asasi orang lain. Hak dan kewajiban ini berjalan seiring. Warga negara tidak dapat hanya menuntut hak tanpa menjalankan kewajiban, karena keduanya adalah pilar dalam membangun masyarakat yang adil dan beradab."),
  ("h2", "Tantangan Pelaksanaan Konstitusi"),
  ("p", "Meskipun Indonesia memiliki konstitusi yang cukup baik, pelaksanaan supremasi konstitusi masih menghadapi tantangan. Budaya hukum masyarakat yang masih rendah membuat sebagian warga belum memahami hak dan kewajibannya secara mendalam, sehingga mudah menjadi korban ketidakadilan atau tanpa sadar melanggar hukum."),
  ("p", "Tantangan lain adalah praktik korupsi dan kolusi yang masih terjadi di sebagian tubuh pemerintahan, serta polarisasi politik yang tajam. Ketika hukum dilihat dari sudut pandang kelompok, objektivitasnya terancam. Kondisi ini menegaskan pentingnya pendidikan kewarganegaraan yang baik untuk membangun kesadaran konstitusional di semua jenjang."),
 ],
 "5": [
  ("h2", "Jenis-Jenis Hak Warga Negara"),
  ("p", "Hak warga negara mencakup berbagai bidang kehidupan. Dalam bidang politik, warga negara berhak memilih dan dipilih. Dalam bidang ekonomi, warga negara berhak berusaha dan memiliki hak milik. Dalam bidang sosial dan budaya, warga negara berhak atas pendidikan dan pengembangan kebudayaan. Dalam bidang sipil, warga negara berhak atas kebebasan berpendapat, beragama, dan bergerak."),
  ("p", "Pembagian ini menunjukkan bahwa hak warga negara menyentuh hampir seluruh aspek kehidupan. Karena saling berkaitan, terabaikannya satu bidang hak sering berdampak pada bidang yang lain. Pemahaman terhadap jenis-jenis hak ini membantu mahasiswa mengenali hak yang dimilikinya sekaligus menghormati hak orang lain."),
  ("h2", "Instrumen Hak Asasi Manusia Nasional dan Internasional"),
  ("p", "Perlindungan hak asasi manusia diatur baik pada tingkat nasional maupun internasional. Di tingkat internasional, prinsip hak asasi dirumuskan dalam dokumen penting seperti Deklarasi Universal Hak Asasi Manusia yang disahkan Perserikatan Bangsa-Bangsa pada tahun 1948. Dokumen ini memuat prinsip dasar tentang martabat manusia, kesetaraan, dan kebebasan."),
  ("p", "Di tingkat nasional, instrumen hak asasi mencakup UUD NRI Tahun 1945 dan Undang-Undang Nomor 39 Tahun 1999 tentang Hak Asasi Manusia, serta keberadaan Komisi Nasional Hak Asasi Manusia. Keselarasan antara instrumen nasional dan internasional menunjukkan bahwa isu kemanusiaan telah menjadi perhatian bersama, bukan hanya kepentingan satu negara."),
  ("h2", "Tantangan Penegakan Hak Asasi Manusia"),
  ("p", "Penegakan hak asasi di Indonesia masih menghadapi tantangan. Rendahnya kesadaran hukum membuat sebagian warga tidak menyadari ketika hak mereka dilanggar, atau bahkan menganggapnya hal wajar. Diskriminasi juga masih terjadi dalam berbagai bentuk, baik berdasarkan suku, agama, kondisi fisik, maupun latar belakang ekonomi."),
  ("p", "Di lingkungan kampus, diskriminasi dapat muncul secara halus, misalnya perlakuan tidak adil terhadap mahasiswa dari latar tertentu atau ketidakpekaan terhadap mahasiswa berkebutuhan khusus. Meski terlihat kecil, sikap semacam ini merusak martabat seseorang dan bertentangan dengan prinsip hak asasi. Kesadaran inilah yang perlu terus ditumbuhkan."),
 ],
 "6": [
  ("h2", "Akses Keadilan dan Kesadaran Hukum Masyarakat"),
  ("p", "Salah satu tantangan terbesar dalam penegakan hukum adalah ketimpangan akses terhadap keadilan. Tidak semua warga memiliki kemampuan yang sama untuk mendapatkan bantuan hukum. Masalah biaya, jarak ke pengadilan, dan keterbatasan informasi membuat sebagian masyarakat, terutama yang lemah secara ekonomi, sulit memperjuangkan haknya."),
  ("p", "Rendahnya kesadaran hukum juga menjadi persoalan. Banyak warga belum memahami hak dan kewajibannya, tidak tahu cara melapor jika menjadi korban, atau bagaimana mengakses bantuan hukum. Karena itu, edukasi hukum kepada masyarakat perlu terus ditingkatkan, termasuk melalui kegiatan kampus dan pengabdian masyarakat."),
  ("h2", "Tantangan dan Harapan Penegakan Hukum"),
  ("p", "Penyalahgunaan kekuasaan menjadi tantangan serius dalam penegakan hukum. Ketika kekuasaan digunakan untuk kepentingan pribadi atau kelompok, hukum kehilangan fungsinya sebagai alat keadilan. Lemahnya integritas sebagian aparat dapat membuat masyarakat ragu terhadap sistem hukum, sehingga penegakan hukum membutuhkan aparat yang jujur dan lembaga yang kuat."),
  ("p", "Namun harapan tetap ada. Pendidikan, literasi hukum, keterbukaan informasi, dan partisipasi publik dapat memperkuat budaya hukum. Mahasiswa memiliki peran dalam harapan ini sebagai kelompok yang kritis, peduli, dan berani menyuarakan keadilan dengan cara yang bertanggung jawab. Penegakan hukum memang tidak mudah, tetapi dapat diperbaiki bila masyarakat ikut menjaga nilai keadilan dari lingkungan terkecil."),
 ],
 "7": [
  ("h2", "Kesadaran Maritim dan Pemerataan Pembangunan"),
  ("p", "Sebagai negara kepulauan, sebagian besar wilayah Indonesia adalah laut. Karena itu, kesadaran maritim menjadi bagian penting dari wawasan nusantara. Laut bukan sekadar pemisah, melainkan penghubung yang menyatukan kehidupan bangsa, sekaligus sumber pangan, energi, dan jalur perdagangan yang harus dijaga."),
  ("p", "Wawasan nusantara juga mendorong pemerataan pembangunan. Pembangunan tidak boleh hanya terpusat di kota besar, karena ketimpangan antardaerah bertentangan dengan semangat persatuan. Daerah terpencil dan perbatasan perlu mendapat perhatian agar seluruh warga merasakan manfaat dari kemerdekaan dan pembangunan nasional."),
  ("h2", "Tantangan Generasi Muda"),
  ("p", "Generasi muda menghadapi tantangan tersendiri dalam menjaga wawasan nusantara dan ketahanan nasional. Arus informasi digital yang deras membawa banyak nilai dari luar yang tidak semuanya sesuai dengan budaya bangsa. Tanpa kemampuan menyaring, generasi muda mudah terombang-ambing oleh informasi yang belum tentu benar."),
  ("p", "Tantangan lain adalah individualisme dan intoleransi. Kehidupan modern cenderung membuat orang fokus pada kepentingan pribadi, padahal ketahanan nasional membutuhkan kepedulian dan kerja sama. Sikap tidak menghargai perbedaan, bila dibiarkan, dapat merusak kerukunan. Generasi muda perlu belajar menerima perbedaan sebagai bagian dari kehidupan berbangsa."),
 ],
 "8": [
  ("h2", "Strategi Pencegahan Korupsi"),
  ("p", "Pencegahan korupsi menuntut pendekatan yang menyeluruh, bukan hanya penindakan. Dari sisi sistem, diperlukan transparansi anggaran, pelayanan publik yang sederhana, dan pengawasan yang ketat agar peluang penyimpangan dipersempit. Dari sisi manusia, diperlukan penanaman nilai integritas sejak dini melalui pendidikan dan keteladanan."),
  ("p", "Keduanya harus berjalan bersama. Sistem yang baik tanpa manusia yang jujur akan mudah disiasati, sedangkan manusia yang jujur tanpa sistem yang baik akan kesulitan bertahan. Karena itu, pemberantasan korupsi yang berhasil selalu menggabungkan perbaikan tata kelola dengan pembentukan karakter."),
  ("h2", "Membangun Budaya Integritas di Kampus"),
  ("p", "Budaya integritas berarti kesesuaian antara perkataan dan perbuatan, serta keberanian untuk tetap jujur meski ada kesempatan untuk curang. Budaya ini tidak terbentuk seketika, melainkan melalui kebiasaan yang dilatih setiap hari. Di lingkungan kampus, ia dimulai dari hal kecil seperti tidak menyontek, tidak memalsukan tanda tangan, dan mengelola organisasi secara transparan."),
  ("p", "Organisasi kemahasiswaan yang dikelola dengan jujur dan akuntabel menjadi latihan kecil bagi pembentukan karakter pemimpin masa depan. Selain itu, empati terhadap korban korupsi perlu ditumbuhkan, karena banyak masyarakat kecil dirugikan akibat pembangunan yang gagal atau pelayanan publik yang buruk. Dengan kesadaran ini, penolakan terhadap korupsi lahir dari pemahaman, bukan sekadar kewajiban menaati aturan."),
 ],
}

def _splice_naila():
    for bab in BAB:
        no = bab["no"]; isi = bab["isi"]
        if no in EXTRA:
            idx = next((i for i,(k,t) in enumerate(isi) if k=="h2" and "Rangkuman" in t), len(isi))
            isi = isi[:idx] + EXTRA[no] + isi[idx:]
        n=0; new=[]
        for blk in isi:
            if blk[0]=="h2":
                n+=1
                t2=_re.sub(r"^\s*\d+\.\d+\s+","",blk[1])
                new.append(("h2", f"{no}.{n} {t2}"))
            else:
                new.append(blk)
        bab["isi"]=new

_splice_naila()


# ===================== PENDALAMAN TAHAP 2 =====================
EXTRA2 = {
 "1": [
  ("h2", "Membangun Kesadaran Kewarganegaraan"),
  ("p", "Kesadaran kewarganegaraan tidak tumbuh secara otomatis. Ia dibentuk melalui pembiasaan, keteladanan, dan pengalaman langsung. Di lingkungan kampus, kesadaran ini dilatih ketika mahasiswa mengikuti kegiatan organisasi dengan jujur, menjaga fasilitas bersama, menghormati perbedaan pendapat dalam diskusi, serta membantu sesama yang membutuhkan."),
  ("p", "Hal-hal kecil semacam itu sebenarnya merupakan wujud nyata kewarganegaraan yang aktif. Partisipasi warga negara tidak melulu soal memilih dalam pemilihan umum, tetapi juga soal kepedulian sehari-hari terhadap lingkungan sekitar. Mahasiswa yang terbiasa peduli pada hal kecil akan lebih siap mengambil peran yang lebih besar di masyarakat."),
  ("p", "Dengan membangun kesadaran sejak masa kuliah, mahasiswa menyiapkan diri menjadi warga negara yang tidak apatis. Mereka belajar bahwa menjadi warga negara yang baik berarti bersedia terlibat secara bertanggung jawab, bukan hanya menuntut, apalagi sekadar menonton dari kejauhan."),
 ],
 "2": [
  ("h2", "Peran Mahasiswa dalam Merawat Identitas Nasional"),
  ("p", "Mahasiswa berada pada posisi yang strategis untuk merawat identitas nasional. Sebagai kelompok terdidik, mereka mampu berpikir kritis, sekaligus cukup muda untuk menjadi penggerak perubahan. Peran ini dapat diwujudkan melalui penggunaan bahasa Indonesia yang baik, penghargaan terhadap tradisi daerah lain, dan penolakan terhadap ujaran yang merendahkan kelompok tertentu."),
  ("p", "Mahasiswa juga dapat memperkuat identitas nasional melalui kegiatan akademik, seperti menulis karya ilmiah tentang isu lokal, budaya daerah, atau tokoh bangsa. Proses ini membuat identitas nasional tidak sekadar diingat, tetapi dipahami dan dihidupkan kembali dengan cara yang relevan bagi generasi muda."),
  ("p", "Kampus pada dasarnya adalah miniatur Indonesia. Di sana mahasiswa dari berbagai daerah berkumpul, berdiskusi, dan bekerja sama. Bila ruang itu dikelola dengan sikap saling menghormati, semboyan Bhinneka Tunggal Ika tidak lagi berhenti sebagai hafalan, melainkan menjadi pengalaman yang dirasakan setiap hari."),
 ],
 "3": [
  ("h2", "NKRI dan Etika Bermedia Sosial"),
  ("p", "Negara Kesatuan Republik Indonesia adalah wujud konkret dari integrasi nasional. NKRI bukan sekadar gagasan, melainkan kenyataan politik dan hukum yang dijaga oleh konstitusi serta ideologi Pancasila. Menjaga keutuhannya merupakan tanggung jawab seluruh rakyat, bukan hanya aparat negara."),
  ("p", "Di era digital, salah satu ancaman terhadap integrasi datang dari ruang media sosial. Informasi menyebar lebih cepat daripada kemampuan masyarakat memverifikasinya, sehingga konflik kadang bermula dari kesalahpahaman atau hasutan yang tidak berdasar. Di sinilah etika bermedia sosial menjadi penting."),
  ("p", "Mahasiswa dapat menjaga integrasi di ruang digital dengan memeriksa kebenaran informasi sebelum membagikannya dan menahan diri dari komentar yang memperkeruh suasana. Sebagai kelompok terdidik, mereka diharapkan menjadi penyaring informasi, bukan penyebar provokasi yang memecah belah masyarakat."),
 ],
 "4": [
  ("h2", "Kesadaran Berkonstitusi bagi Mahasiswa"),
  ("p", "Kesadaran berkonstitusi berarti kesediaan untuk memahami, menghormati, dan menjalankan aturan dasar negara. Bagi mahasiswa, kesadaran ini dapat dilatih dari hal sederhana, seperti menaati aturan kampus, menyampaikan pendapat secara santun, dan menyelesaikan perbedaan melalui jalur yang sah."),
  ("p", "Mahasiswa berperan sebagai pembelajar kritis yang membaca konstitusi secara langsung dan tidak mudah menerima tafsir yang keliru. Mereka juga berperan sebagai pengawas sosial yang menilai kebijakan publik. Jika ada kebijakan yang dinilai bertentangan dengan konstitusi, mahasiswa dapat menyuarakan kritik melalui forum diskusi atau tulisan yang berbasis argumen."),
  ("p", "Peran ketiga adalah menjadi pelopor ketaatan hukum. Konstitusi adalah hukum tertinggi, dan ketaatan terhadapnya dimulai dari ketaatan pada aturan yang lebih kecil, seperti tidak melakukan plagiarisme dan menghormati hak orang lain. Sikap ini mencerminkan kesadaran konstitusional yang sehat."),
 ],
 "5": [
  ("h2", "Peran Mahasiswa dalam Menghormati Hak dan Menjalankan Kewajiban"),
  ("p", "Mahasiswa memiliki peran yang cukup strategis dalam menghormati hak asasi dan menjalankan kewajiban warga negara. Peran ini dimulai dari hal sederhana, yaitu belajar menghargai perbedaan. Di kampus, mahasiswa bertemu teman dari latar belakang yang beragam, dan sikap tidak merendahkan orang lain karena latarnya adalah penghormatan dasar terhadap hak asasi."),
  ("p", "Mahasiswa juga perlu bersikap adil dalam pergaulan, yaitu memberi kesempatan yang sama kepada semua orang untuk didengar dan diperlakukan layak. Dalam organisasi, keputusan yang baik adalah keputusan yang mempertimbangkan kepentingan semua anggota, bukan hanya kelompok tertentu."),
  ("p", "Selain itu, mahasiswa perlu bijak dalam menggunakan media sosial. Ujaran kebencian, penyebaran berita palsu, perundungan daring, atau penyebaran informasi pribadi tanpa izin adalah bentuk pelanggaran hak asasi yang dapat dilakukan secara sadar maupun tidak. Mahasiswa yang sadar akan hal ini akan menggunakan media sosial secara bertanggung jawab."),
 ],
 "6": [
  ("h2", "Peran Mahasiswa dalam Membangun Budaya Hukum"),
  ("p", "Mahasiswa berperan penting dalam membangun budaya hukum, dimulai dari kehidupan kampus. Peran pertama adalah menjadi contoh dalam menaati aturan, seperti menghormati peraturan kampus, menolak plagiarisme, dan tidak terlibat perundungan. Kebiasaan menaati aturan di lingkungan kecil menjadi fondasi untuk menaati hukum di masyarakat yang lebih luas."),
  ("p", "Peran kedua adalah meningkatkan literasi hukum, yaitu memahami aturan dasar yang relevan dengan kehidupan, seperti perlindungan data pribadi atau hak-hak dasar lainnya. Pengetahuan ini tidak hanya melindungi diri sendiri, tetapi juga memungkinkan mahasiswa membantu orang di sekitarnya yang kurang memiliki akses informasi hukum."),
  ("p", "Peran ketiga adalah berani menyuarakan keadilan tanpa main hakim sendiri. Ketika melihat ketidakadilan, mahasiswa dapat menyampaikan kritik melalui cara yang sah, seperti dialog, tulisan, atau pelaporan ke lembaga berwenang. Mengambil keadilan dengan tangan sendiri justru menambah masalah, bukan menyelesaikannya."),
 ],
 "7": [
  ("h2", "Peran Mahasiswa dalam Menjaga Wawasan Nusantara"),
  ("p", "Mahasiswa dapat menjaga wawasan nusantara melalui sikap sederhana yang konsisten. Yang pertama adalah menjaga persatuan dalam keberagaman, yaitu saling menghargai dan tidak menjadikan perbedaan sebagai alasan untuk menjauh. Sikap terbuka terhadap kebudayaan lain merupakan wujud nyata wawasan nusantara dalam kehidupan sehari-hari."),
  ("p", "Peran berikutnya adalah meningkatkan literasi digital, yaitu menyaring informasi sebelum membagikannya dan tidak ikut menyebarkan berita palsu. Literasi digital yang baik menjadi benteng pertama dalam menghadapi ancaman informasi yang dapat merusak persatuan."),
  ("p", "Mahasiswa juga dapat menghargai keberagaman budaya dengan mempelajari budaya daerah lain dan ikut melestarikan budaya daerahnya sendiri, serta berpartisipasi dalam kegiatan positif seperti pengabdian masyarakat. Melalui kegiatan ini, mahasiswa belajar bekerja sama dan memahami persoalan masyarakat secara langsung."),
 ],
 "8": [
  ("h2", "Peran Lembaga Negara dan Tanggung Jawab Bersama"),
  ("p", "Pemberantasan korupsi di Indonesia melibatkan beberapa lembaga, seperti Komisi Pemberantasan Korupsi, Kepolisian, Kejaksaan, dan pengadilan. Komisi Pemberantasan Korupsi memiliki peran khusus karena berfokus pada pencegahan sekaligus penindakan, terutama untuk perkara yang melibatkan kerugian negara dan pejabat publik."),
  ("p", "Namun, pemberantasan korupsi tidak bisa dibebankan hanya kepada aparat. Korupsi adalah persoalan sistemik yang menuntut perbaikan tata kelola pemerintahan, transparansi anggaran, dan partisipasi masyarakat. Keberhasilannya bergantung pada kerja sama antara negara, masyarakat, media, dunia pendidikan, dan sektor swasta."),
  ("p", "Setiap warga negara memiliki tanggung jawab untuk menolak dan tidak ikut dalam praktik koruptif. Tanggung jawab ini dapat diwujudkan melalui tindakan sederhana, seperti menolak memberi uang pelicin, melaporkan penyimpangan, dan memilih pemimpin yang berintegritas. Mahasiswa, sebagai calon pemimpin masa depan, perlu membangun keberanian moral untuk melawan korupsi sejak sekarang."),
 ],
}

def _splice_naila2():
    for bab in BAB:
        no = bab["no"]; isi = bab["isi"]
        if no in EXTRA2:
            idx = next((i for i,(k,t) in enumerate(isi) if k=="h2" and "Rangkuman" in t), len(isi))
            isi = isi[:idx] + EXTRA2[no] + isi[idx:]
        n=0; new=[]
        for blk in isi:
            if blk[0]=="h2":
                n+=1
                t2=_re.sub(r"^\s*\d+\.\d+\s+","",blk[1])
                new.append(("h2", f"{no}.{n} {t2}"))
            else:
                new.append(blk)
        bab["isi"]=new

_splice_naila2()


# ===================== PENDALAMAN TAHAP 3 =====================
EXTRA3 = {
 "1": [
  ("h2", "Pendidikan Kewarganegaraan sebagai Pembentuk Karakter"),
  ("p", "Salah satu ciri khas Pendidikan Kewarganegaraan adalah keterkaitannya yang erat dengan pembentukan karakter. Pengetahuan tentang negara dan hukum akan kehilangan makna bila tidak disertai sikap yang baik. Seseorang dapat saja hafal banyak konsep, tetapi tetap berlaku tidak jujur. Di titik inilah pendidikan karakter menjadi bagian yang tidak terpisahkan dari mata kuliah ini."),
  ("p", "Nilai seperti jujur, disiplin, adil, dan bertanggung jawab tidak dapat ditanamkan hanya melalui ceramah. Nilai tumbuh melalui kebiasaan dan keteladanan. Karena itu, ruang kelas Pendidikan Kewarganegaraan sebaiknya juga menjadi ruang latihan, tempat mahasiswa belajar berargumen dengan santun, menghargai perbedaan pendapat, dan berani bersikap jujur."),
  ("p", "Pembentukan karakter melalui mata kuliah ini bersifat jangka panjang. Karakter yang terbentuk di bangku kuliah akan terbawa hingga dunia kerja. Lulusan yang terbiasa jujur dan bertanggung jawab akan menjadi tenaga profesional yang dapat dipercaya, sekaligus warga negara yang menjaga nama baik bangsanya."),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, karakter ini menjadi semakin penting karena profesi konselor menuntut kepercayaan. Kejujuran dan tanggung jawab yang dilatih sejak masa kuliah akan menjadi fondasi sikap profesional ketika kelak menangani klien."),
 ],
 "2": [
  ("h2", "Budaya sebagai Kekuatan Pemersatu"),
  ("p", "Budaya Indonesia yang beragam merupakan salah satu unsur paling kaya dalam identitas nasional. Dari tarian, musik, pakaian adat, hingga kebiasaan sosial, keberagaman ini menunjukkan kemampuan bangsa merangkul perbedaan tanpa kehilangan kesatuan. Budaya bukan sekadar tampilan dalam acara kebudayaan, melainkan cara masyarakat membangun kehidupan bersama."),
  ("p", "Nilai di balik tradisi sering kali lebih penting daripada bentuk luarnya. Gotong royong, musyawarah, sopan santun, dan kepedulian terhadap lingkungan sosial adalah nilai budaya yang masih relevan hingga kini. Nilai-nilai inilah yang sebenarnya menjadi inti identitas, sementara bentuk kesenian adalah ungkapan lahirnya."),
  ("p", "Namun budaya juga menghadapi tekanan modernisasi. Gaya hidup yang serba cepat dan sikap individualistis dapat menggeser kebiasaan lama. Karena itu, pelestarian budaya menjadi tanggung jawab bersama, termasuk generasi muda yang justru dapat mengenalkan budaya daerah ke panggung yang lebih luas melalui teknologi."),
  ("p", "Bagi calon konselor, kepekaan terhadap budaya menjadi modal penting. Latar budaya seseorang memengaruhi cara ia memandang masalah dan mencari solusi. Konselor yang menghargai budaya akan lebih mampu memahami klien secara utuh, bukan dari sudut pandang dirinya sendiri saja."),
 ],
 "3": [
  ("h2", "Sumpah Pemuda dan Semangat Persatuan"),
  ("p", "Sejarah integrasi nasional Indonesia tidak dapat dilepaskan dari peristiwa Sumpah Pemuda pada tahun 1928. Pada peristiwa itu, para pemuda dari berbagai daerah, suku, dan latar belakang bersatu dalam satu tekad, yaitu satu tanah air, satu bangsa, dan satu bahasa. Mereka rela mengesampingkan perbedaan demi tujuan yang lebih besar."),
  ("p", "Sumpah Pemuda menjadi pengingat bahwa persatuan Indonesia adalah hasil perjuangan, bukan sesuatu yang datang dengan sendirinya. Semangat ini menunjukkan bahwa keberagaman tidak harus menjadi penghalang persatuan, asalkan ada kesadaran dan kemauan untuk bersatu."),
  ("p", "Bagi generasi sekarang, Sumpah Pemuda menjadi inspirasi untuk terus menjaga persatuan di tengah perbedaan, sekaligus motivasi untuk tidak mudah terpecah oleh provokasi dan kepentingan sesaat. Semangat itu tetap relevan untuk dihidupkan dalam kehidupan kampus dan masyarakat."),
  ("p", "Mahasiswa dapat meneruskan semangat Sumpah Pemuda melalui sikap sehari-hari, seperti membangun pertemanan lintas daerah, menolak sikap eksklusif, dan aktif dalam kegiatan yang mempererat kebersamaan. Dengan cara itu, semangat persatuan tidak berhenti sebagai peristiwa sejarah, tetapi terus hidup dalam praktik."),
 ],
 "4": [
  ("h2", "Konstitusi sebagai Pelindung Warga Negara"),
  ("p", "Salah satu wujud nyata kehadiran konstitusi adalah perlindungan terhadap warga negara. Konstitusi menjamin bahwa setiap orang berhak memperoleh keadilan, pendidikan, rasa aman, dan kebebasan berpendapat. Jaminan ini membuat warga tidak boleh diperlakukan sewenang-wenang oleh kekuasaan."),
  ("p", "Namun perlindungan itu hanya berjalan baik bila warga memahami haknya. Banyak orang mengalami ketidakadilan tetapi tidak menyadari bahwa hak mereka dilindungi konstitusi, atau tidak mengetahui cara memperjuangkannya. Karena itu, pemahaman terhadap konstitusi menjadi penting agar warga dapat membela diri melalui jalur yang sah."),
  ("p", "Konstitusi juga melindungi kelompok minoritas dari dominasi mayoritas. Dalam demokrasi, suara terbanyak memang menentukan, tetapi konstitusi memastikan hak kelompok kecil tetap dihormati. Inilah yang menjaga agar demokrasi tidak berubah menjadi penindasan atas nama suara mayoritas."),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, pemahaman ini berguna karena klien yang dihadapi kadang berasal dari kelompok rentan. Kesadaran bahwa setiap orang memiliki hak yang dilindungi membantu konselor bersikap adil dan melindungi kepentingan klien tanpa diskriminasi."),
 ],
 "5": [
  ("h2", "Dampak Pelanggaran Hak Asasi Manusia bagi Masyarakat"),
  ("p", "Pelanggaran hak asasi manusia menimbulkan dampak yang luas. Dampak langsung dirasakan oleh korban dan keluarganya, yang kehilangan rasa aman, martabat, dan kepercayaan terhadap sistem hukum. Trauma yang dialami korban dapat bertahan lama dan memengaruhi kesehatan mental serta kehidupan sosialnya."),
  ("p", "Dampak yang lebih luas menyentuh masyarakat secara keseluruhan. Pelanggaran yang tidak diselesaikan dengan adil dapat menimbulkan ketidakpercayaan terhadap institusi negara. Ketika masyarakat melihat pelaku pelanggaran tidak pernah dihukum, mereka dapat kehilangan keyakinan bahwa hukum benar-benar melindungi semua orang."),
  ("p", "Kehilangan kepercayaan ini berbahaya bagi kehidupan berbangsa, karena kepercayaan publik adalah fondasi yang membuat sistem kenegaraan berjalan. Karena itu, penyelesaian kasus pelanggaran hak asasi secara adil bukan hanya soal keadilan bagi korban, tetapi juga soal menjaga kepercayaan masyarakat terhadap negara."),
  ("p", "Dalam konteks profesi Bimbingan dan Konseling, dampak psikologis dari pelanggaran hak asasi menjadi perhatian penting. Konselor dapat berperan membantu korban memulihkan rasa aman dan martabatnya, sehingga pemahaman tentang hak asasi memiliki manfaat praktis yang nyata."),
 ],
 "6": [
  ("h2", "Independensi Lembaga Peradilan"),
  ("p", "Penegakan hukum yang adil membutuhkan lembaga peradilan yang independen. Hakim harus bebas dari tekanan politik, ekonomi, maupun kepentingan pribadi agar putusan yang dihasilkan benar-benar berdasarkan fakta dan hukum. Tanpa independensi, masyarakat akan kehilangan tempat untuk mencari keadilan."),
  ("p", "Independensi peradilan juga berkaitan dengan kepercayaan publik. Ketika masyarakat yakin bahwa pengadilan tidak dapat dibeli atau ditekan, mereka akan lebih percaya untuk menyelesaikan persoalan melalui jalur hukum, bukan dengan cara sendiri. Kepercayaan ini menjadi modal penting bagi negara hukum."),
  ("p", "Pengawasan terhadap perilaku hakim turut menjaga independensi sekaligus integritas peradilan. Lembaga seperti Komisi Yudisial hadir untuk menjaga etika hakim, sehingga kemandirian tidak berubah menjadi kesewenang-wenangan. Keseimbangan antara kemandirian dan pengawasan inilah yang menjaga kualitas peradilan."),
  ("p", "Mahasiswa dapat ikut menjaga independensi peradilan dengan mengawal proses hukum yang menjadi perhatian publik secara kritis dan berbasis data. Sikap ini menunjukkan bahwa pengawasan masyarakat merupakan bagian dari mekanisme menjaga keadilan."),
 ],
 "7": [
  ("h2", "Kedudukan Wawasan Nusantara dalam Pembangunan"),
  ("p", "Wawasan nusantara memiliki kedudukan penting dalam pembangunan nasional. Konsep ini menegaskan bahwa pembangunan tidak boleh hanya terpusat di kota besar atau pulau tertentu, melainkan harus menjangkau seluruh wilayah Indonesia secara proporsional. Ketimpangan pembangunan antardaerah bertentangan dengan semangat wawasan nusantara."),
  ("p", "Daerah perbatasan, pulau kecil, dan wilayah terpencil perlu mendapat perhatian agar masyarakat di sana juga merasakan manfaat pembangunan. Ketika seluruh wilayah merasa diperhatikan, rasa memiliki terhadap bangsa akan tumbuh lebih kuat, dan persatuan nasional menjadi lebih kokoh."),
  ("p", "Pembangunan yang merata juga memperkuat ketahanan nasional. Masyarakat yang sejahtera dan merasa diperlakukan adil cenderung lebih tahan terhadap provokasi yang ingin memecah belah. Dengan demikian, pemerataan pembangunan bukan sekadar urusan ekonomi, melainkan bagian dari menjaga keutuhan bangsa."),
  ("p", "Mahasiswa dapat berkontribusi dengan kepedulian terhadap isu pemerataan, misalnya melalui penelitian, pengabdian masyarakat di daerah, atau penyebaran informasi yang membangun kesadaran tentang pentingnya pembangunan yang adil bagi seluruh wilayah."),
 ],
 "8": [
  ("h2", "Pendidikan Antikorupsi di Perguruan Tinggi"),
  ("p", "Perguruan tinggi memiliki tanggung jawab besar dalam menanamkan nilai antikorupsi. Kampus tidak boleh hanya menjadi tempat memindahkan ilmu, tetapi juga ruang pembentukan karakter. Pendidikan antikorupsi dapat dimasukkan ke dalam perkuliahan, kegiatan kemahasiswaan, budaya akademik, dan tata kelola kampus."),
  ("p", "Budaya akademik yang bersih sangat penting. Bila kampus membiarkan plagiarisme, jual beli nilai, atau penyalahgunaan jabatan organisasi, kampus justru sedang menormalkan benih korupsi. Sebaliknya, kampus yang tegas terhadap ketidakjujuran sedang menanam fondasi integritas yang kuat bagi mahasiswanya."),
  ("p", "Karena itu, pendidikan antikorupsi di perguruan tinggi harus bersifat menyeluruh. Ia tidak cukup berupa materi kuliah, tetapi juga harus tercermin dalam sistem, aturan, dan budaya kampus itu sendiri. Konsistensi antara apa yang diajarkan dan apa yang dipraktikkan menjadi kunci keberhasilannya."),
  ("p", "Bagi mahasiswa Bimbingan dan Konseling, integritas akademik menjadi latihan langsung. Kebiasaan jujur dalam mengerjakan tugas dan penelitian akan menjadi dasar sikap profesional ketika kelak menjalankan layanan konseling yang menuntut kepercayaan dan kejujuran."),
 ],
}

def _splice_naila3():
    for bab in BAB:
        no = bab["no"]; isi = bab["isi"]
        if no in EXTRA3:
            idx = next((i for i,(k,t) in enumerate(isi) if k=="h2" and "Rangkuman" in t), len(isi))
            isi = isi[:idx] + EXTRA3[no] + isi[idx:]
        n=0; new=[]
        for blk in isi:
            if blk[0]=="h2":
                n+=1
                t2=_re.sub(r"^\s*\d+\.\d+\s+","",blk[1])
                new.append(("h2", f"{no}.{n} {t2}"))
            else:
                new.append(blk)
        bab["isi"]=new

_splice_naila3()


# ===================== PENDALAMAN TAHAP 4 (agar cukup di spasi 1.5) =====================
EXTRA4 = {
 "1": [
  ("h2", "Objek dan Ruang Lingkup Kajian"),
  ("p", "Kajian Pendidikan Kewarganegaraan cukup luas karena menyangkut hubungan antara warga negara dengan negaranya. Di dalamnya termasuk persoalan identitas bangsa, persatuan, sistem ketatanegaraan, hak dan kewajiban, hukum, wilayah negara, hingga persoalan moral seperti korupsi. Cakupan yang luas ini menunjukkan bahwa mata kuliah ini menyentuh hampir seluruh aspek kehidupan berbangsa."),
  ("p", "Walaupun terlihat beragam, seluruh topik tersebut sebenarnya berpusat pada satu pertanyaan mendasar, yaitu bagaimana hidup bersama secara adil dan damai dalam sebuah negara. Pertanyaan inilah yang menjadi benang merah seluruh bab dalam mini book ini, mulai dari identitas nasional hingga pendidikan antikorupsi."),
  ("p", "Karena keterkaitan antartopik begitu erat, mahasiswa sebaiknya tidak memandang setiap bab secara terpisah. Identitas nasional berkaitan dengan integrasi, integrasi berkaitan dengan konstitusi, dan seterusnya. Semakin mahasiswa mampu melihat keterkaitan ini, semakin utuh pula pemahamannya tentang kehidupan bernegara."),
 ],
 "2": [
  ("h2", "Bela Negara sebagai Wujud Identitas"),
  ("p", "Bela negara sering disalahpahami sebagai urusan militer semata. Padahal, bela negara juga berarti menjaga identitas nasional dari berbagai ancaman yang dapat memecah belah bangsa, seperti radikalisme, provokasi bernuansa suku dan agama, serta berita bohong yang sengaja disebarkan."),
  ("p", "Setiap warga negara dapat berperan dalam bela negara melalui tindakan sehari-hari. Menjaga kerukunan, menghargai perbedaan agama, menolak ujaran kebencian, dan aktif dalam kehidupan berdemokrasi adalah bentuk bela negara yang dapat dilakukan siapa saja. Bela negara dengan demikian dimulai dari hal-hal kecil yang dekat dengan kehidupan."),
  ("p", "Bagi mahasiswa, bela negara dapat diwujudkan melalui prestasi, integritas, dan kepedulian sosial. Menjaga nama baik bangsa di kancah akademik dan menyebarkan semangat positif di ruang digital merupakan bentuk bela negara yang relevan dengan zaman sekarang, sekaligus memperkuat identitas nasional."),
 ],
 "3": [
  ("h2", "Pemerataan Pembangunan dan Keadilan Sosial"),
  ("p", "Integrasi nasional akan semakin kuat bila masyarakat merasa diperlakukan adil. Karena itu, pemerataan pembangunan menjadi bagian penting dari menjaga persatuan. Ketika daerah tertinggal tidak mendapat perhatian, masyarakat setempat dapat merasa ditinggalkan oleh negara, dan perasaan ini bila dibiarkan dapat menumbuhkan ketidakpuasan."),
  ("p", "Keadilan sosial menjadi perekat yang menghubungkan warga dengan negaranya. Pembangunan infrastruktur, pendidikan, dan layanan kesehatan yang merata di seluruh wilayah membuat masyarakat merasa menjadi bagian dari bangsa. Dengan demikian, pemerataan bukan sekadar urusan ekonomi, melainkan juga strategi menjaga keutuhan bangsa."),
  ("p", "Mahasiswa dapat berkontribusi pada kesadaran ini melalui kegiatan pengabdian masyarakat dan penelitian yang menyoroti persoalan ketimpangan. Dari keterlibatan langsung itu, mahasiswa belajar bahwa persoalan bangsa tidak hanya ada di buku, tetapi benar-benar dialami oleh masyarakat di berbagai daerah."),
 ],
 "4": [
  ("h2", "Konstitusi sebagai Pembatas Kekuasaan"),
  ("p", "Salah satu fungsi terpenting konstitusi adalah membatasi kekuasaan. Sejarah memperlihatkan bahwa kekuasaan yang tidak dibatasi cenderung disalahgunakan. Karena itu, konstitusi mengatur batas kewenangan setiap pemegang kekuasaan agar tidak bertindak melampaui aturan."),
  ("p", "Pembatasan kekuasaan diwujudkan melalui pembagian tugas antarlembaga negara serta mekanisme saling mengawasi. Presiden menjalankan pemerintahan, Dewan Perwakilan Rakyat membuat undang-undang dan mengawasi, sedangkan lembaga peradilan menegakkan keadilan. Tidak ada satu lembaga pun yang boleh menguasai seluruh kekuasaan negara."),
  ("p", "Bagi warga negara, pembatasan kekuasaan ini sekaligus menjadi pelindung. Jika ada kebijakan yang dianggap melanggar hak konstitusional, warga dapat menempuh jalur hukum yang tersedia. Dengan demikian, konstitusi bukan hanya milik penyelenggara negara, melainkan juga milik rakyat yang dilindunginya."),
 ],
 "5": [
  ("h2", "Keseimbangan Hak dan Kewajiban dalam Demokrasi"),
  ("p", "Dalam kehidupan demokrasi, hak dan kewajiban harus berjalan seimbang. Demokrasi memberi ruang bagi warga negara untuk menyampaikan pendapat, memilih pemimpin, dan mengawasi pemerintahan. Namun, hak-hak itu menuntut kedewasaan agar tidak berubah menjadi kebebasan tanpa batas yang justru merugikan orang lain."),
  ("p", "Dalam pemilihan umum, misalnya, warga negara memiliki hak memilih, tetapi juga berkewajiban menggunakan hak itu secara bertanggung jawab, tidak menjual suara, dan tidak mudah terprovokasi. Keseimbangan inilah yang membuat demokrasi berjalan sehat, bukan sekadar ajang perebutan suara."),
  ("p", "Bagi mahasiswa, latihan menyeimbangkan hak dan kewajiban dapat dimulai dari kehidupan kampus. Menyampaikan pendapat dalam diskusi sambil menghormati pendapat orang lain, atau menggunakan hak berorganisasi sambil menjalankan tanggung jawabnya, adalah bentuk nyata kedewasaan berdemokrasi."),
 ],
 "6": [
  ("h2", "Prinsip Peradilan yang Adil dan Terbuka"),
  ("p", "Penegakan hukum yang berkeadilan menuntut peradilan yang adil, terbuka, dan tidak memihak. Setiap pihak yang terlibat dalam perkara berhak untuk didengar, menyampaikan bukti, dan mempertahankan haknya. Putusan hakim harus berdasarkan hukum, bukan berdasarkan tekanan atau kepentingan pihak tertentu."),
  ("p", "Keterbukaan peradilan juga penting agar masyarakat dapat mengawasi jalannya proses hukum. Pengadilan yang terbuka untuk umum memberi ruang bagi kontrol publik, sehingga keadilan tidak hanya ditegakkan, tetapi juga terlihat ditegakkan. Prinsip ini menjadi penjamin bahwa keadilan benar-benar dapat dicapai."),
  ("p", "Bagi mahasiswa, memahami prinsip ini membantu menumbuhkan sikap kritis yang sehat terhadap praktik hukum. Ketika ada proses hukum yang dinilai tidak adil, mahasiswa dapat menyoroti melalui cara yang sah dan berbasis data, bukan dengan hasutan yang justru merusak proses peradilan."),
 ],
 "7": [
  ("h2", "Ketahanan Ekonomi dan Sosial Budaya"),
  ("p", "Ketahanan nasional sangat dipengaruhi oleh ketahanan ekonomi. Negara dengan ekonomi yang rapuh mudah tertekan oleh krisis dan ketergantungan pada pihak luar. Karena itu, kemandirian ekonomi yang dibangun melalui penguatan usaha kecil, peningkatan kualitas sumber daya manusia, dan pengelolaan kekayaan alam yang adil menjadi bagian penting dari geostrategi."),
  ("p", "Selain ekonomi, ketahanan sosial budaya juga tidak boleh diabaikan. Kemampuan masyarakat mempertahankan nilai, tradisi, dan jati diri di tengah perubahan zaman menjadi benteng dari dalam. Sikap selektif terhadap budaya luar, tanpa menutup diri dari kemajuan, menjadi kunci agar bangsa tetap maju tanpa kehilangan identitas."),
  ("p", "Mahasiswa dapat memperkuat kedua dimensi ini melalui sikap produktif dan kreatif, serta penghargaan terhadap budaya bangsa. Dengan menjadi pribadi yang mandiri dan tetap mencintai budayanya sendiri, mahasiswa turut menyumbang pada ketahanan nasional secara nyata."),
 ],
 "8": [
  ("h2", "Korupsi sebagai Penyakit Sosial dan Moral"),
  ("p", "Korupsi tidak cukup dipahami sebagai pelanggaran hukum biasa. Ia adalah penyakit sosial dan moral yang dapat merusak banyak sendi kehidupan berbangsa. Ketika korupsi dibiarkan, masyarakat lambat laun menganggap ketidakjujuran sebagai hal yang wajar, dan di titik inilah bahaya terbesarnya terletak."),
  ("p", "Dari sisi moral, korupsi menumbuhkan budaya permisif terhadap kebohongan dan penyimpangan. Orang mulai menganggap suap, titipan, atau penyalahgunaan wewenang sebagai sesuatu yang biasa. Jika budaya semacam ini tumbuh, pemberantasan korupsi akan jauh lebih sulit karena persoalannya telah berpindah dari ranah hukum ke ranah kebiasaan."),
  ("p", "Karena itu, pencegahan korupsi tidak cukup mengandalkan hukuman, tetapi juga membutuhkan pembentukan karakter. Mahasiswa berperan penting dalam memutus rantai ini dengan membiasakan kejujuran sejak masa kuliah, sehingga kelak tidak ikut melanggengkan budaya koruptif ketika memegang wewenang."),
 ],
}

def _splice_naila4():
    for bab in BAB:
        no = bab["no"]; isi = bab["isi"]
        if no in EXTRA4:
            idx = next((i for i,(k,t) in enumerate(isi) if k=="h2" and "Rangkuman" in t), len(isi))
            isi = isi[:idx] + EXTRA4[no] + isi[idx:]
        n=0; new=[]
        for blk in isi:
            if blk[0]=="h2":
                n+=1
                t2=_re.sub(r"^\s*\d+\.\d+\s+","",blk[1])
                new.append(("h2", f"{no}.{n} {t2}"))
            else:
                new.append(blk)
        bab["isi"]=new

_splice_naila4()


# ===================== PENDALAMAN TAHAP 5 (cukupkan halaman di spasi 1.5, gap kecil) =====================
EXTRA5 = {
 "1": [
  ("h2", "Peran Mahasiswa sebagai Warga Negara Terdidik"),
  ("p", "Mahasiswa sering disebut sebagai kelompok terdidik yang diharapkan menjadi penggerak perubahan. Sebutan ini bukan sekadar pujian, melainkan tanggung jawab. Sebagai warga negara yang memperoleh kesempatan belajar lebih tinggi, mahasiswa diharapkan mampu menjadi contoh dalam bersikap dan berpikir di tengah masyarakat."),
  ("p", "Peran tersebut tidak harus berbentuk hal besar. Menolak menyontek, berani jujur dalam tugas, aktif dalam kegiatan sosial, dan menjaga sikap di media sosial sudah merupakan kontribusi nyata. Dari kebiasaan kecil yang konsisten, mahasiswa melatih diri menjadi warga negara yang dapat dipercaya di kemudian hari."),
  ("p", "Selain menjadi teladan, mahasiswa juga dapat menjadi penghubung antara dunia kampus dan masyarakat melalui penelitian dan pengabdian. Dengan begitu, ilmu yang dipelajari tidak berhenti sebagai teori, tetapi berlanjut menjadi tindakan yang bermanfaat bagi orang banyak."),
 ],
 "2": [
  ("h2", "Upaya Menjaga Identitas Nasional"),
  ("p", "Menjaga identitas nasional menuntut usaha yang terus-menerus melalui pendidikan, pelestarian budaya, penggunaan bahasa Indonesia yang baik, dan sikap menghargai keberagaman. Identitas tidak cukup hanya dipelajari di ruang kelas, tetapi perlu dibiasakan dalam kehidupan sehari-hari agar tidak berhenti sebagai materi hafalan."),
  ("p", "Peran keluarga juga tidak kalah penting. Nilai dasar seperti kejujuran, tanggung jawab, dan cinta tanah air pertama kali ditanamkan di lingkungan keluarga. Bila fondasi itu kuat, upaya kampus dan negara dalam memperkuat identitas akan jauh lebih mudah. Dengan demikian, menjaga identitas nasional adalah kerja bersama keluarga, kampus, masyarakat, dan negara."),
  ("p", "Mahasiswa dapat berkontribusi dengan mengenalkan budaya daerah secara positif, mengikuti kegiatan kebangsaan, dan tidak mudah merendahkan budaya lain. Sikap terbuka terhadap kemajuan tetap diperlukan, asalkan disertai kesadaran untuk menjaga nilai-nilai bangsa."),
 ],
 "3": [
  ("h2", "Peran Pendidikan dalam Menjaga Integrasi"),
  ("p", "Pendidikan memiliki peran besar dalam merawat integrasi nasional. Melalui pendidikan, generasi muda dikenalkan pada sejarah bangsa, nilai Pancasila, dan bahaya perpecahan. Pendidikan juga membantu masyarakat memahami bahwa perbedaan bukan alasan untuk saling menjauh, melainkan kekuatan bila dikelola dengan baik."),
  ("p", "Pendidikan Kewarganegaraan secara khusus membangun kesadaran integrasi. Mahasiswa tidak hanya mempelajari konsep negara dan warga negara, tetapi juga memahami tanggung jawab sosialnya sebagai bagian dari bangsa. Dalam era digital, pendidikan integrasi perlu menekankan literasi media agar mahasiswa tidak mudah menyebarkan konten yang memecah belah."),
  ("p", "Dengan pendidikan yang baik, mahasiswa diharapkan mampu berpikir kritis tanpa kehilangan rasa kebangsaan. Kemampuan ini penting agar kritik yang disampaikan justru memperkuat persatuan, bukan merusaknya."),
 ],
 "4": [
  ("h2", "Hubungan Negara dan Warga Negara"),
  ("p", "Konstitusi mengatur hubungan timbal balik antara negara dan warga negara. Negara memiliki kewenangan membuat aturan dan menyelenggarakan pemerintahan, tetapi kewenangan itu dibatasi agar tidak melanggar hak warga. Sebaliknya, warga negara wajib menaati aturan, tetapi juga berhak menuntut pelayanan dan perlindungan."),
  ("p", "Hubungan ini idealnya berjalan saling menghormati. Negara hadir untuk melayani, sedangkan warga berpartisipasi secara bertanggung jawab. Ketika keduanya menjalankan perannya dengan baik, kehidupan bernegara berjalan tertib dan kepercayaan publik terhadap pemerintah pun terjaga."),
  ("p", "Pemahaman terhadap hubungan ini membantu mahasiswa menempatkan diri secara tepat. Mahasiswa dapat bersikap kritis terhadap negara, tetapi pada saat yang sama tetap menjalankan kewajibannya sebagai warga negara yang baik."),
 ],
 "5": [
  ("h2", "Tanggung Jawab Sosial Warga Negara"),
  ("p", "Selain hak dan kewajiban yang diatur hukum, warga negara juga memiliki tanggung jawab sosial. Tanggung jawab ini tampak dari kepedulian terhadap lingkungan, kesediaan membantu sesama, dan keterlibatan dalam kegiatan masyarakat. Tanggung jawab sosial memperkuat hubungan antarwarga dan menjaga semangat gotong royong."),
  ("p", "Jika setiap orang hanya memikirkan diri sendiri, kehidupan bersama akan melemah. Sebaliknya, ketika warga saling peduli, nilai kebersamaan tetap hidup. Tanggung jawab sosial inilah yang membuat hak dan kewajiban tidak berhenti pada urusan hukum, tetapi juga menyentuh kualitas kehidupan bermasyarakat."),
  ("p", "Mahasiswa dapat mewujudkan tanggung jawab sosial melalui kegiatan pengabdian, aksi sosial, dan kepedulian terhadap persoalan di sekitarnya. Bagi calon konselor, kepedulian sosial ini menjadi modal penting dalam memahami dan membantu individu yang menghadapi kesulitan."),
 ],
 "6": [
  ("h2", "Membangun Kepercayaan Publik terhadap Hukum"),
  ("p", "Kepercayaan publik terhadap hukum adalah modal berharga yang mudah rusak. Sekali masyarakat merasa hukum tidak adil, kepercayaan itu sulit dipulihkan. Padahal tanpa kepercayaan, masyarakat cenderung mengambil jalan sendiri yang justru menambah persoalan."),
  ("p", "Membangun kepercayaan menuntut bukti, bukan sekadar janji. Penegakan hukum yang konsisten, transparan, dan tidak pandang bulu adalah cara paling nyata untuk memulihkannya. Ketika masyarakat melihat bahwa pihak yang bersalah pun diproses secara adil, kepercayaan akan tumbuh dengan sendirinya."),
  ("p", "Partisipasi masyarakat juga menentukan. Dengan ikut mengawasi jalannya hukum, melaporkan pelanggaran, dan menolak praktik suap, masyarakat turut menjaga wibawa hukum. Mahasiswa dapat menjadi bagian dari pengawasan ini melalui sikap kritis yang bertanggung jawab."),
 ],
 "7": [
  ("h2", "Wawasan Nusantara dan Kesatuan Wilayah"),
  ("p", "Wawasan nusantara menegaskan bahwa seluruh wilayah Indonesia, dari darat, laut, hingga udara, merupakan satu kesatuan yang tidak terpisahkan. Laut yang memisahkan pulau tidak dipandang sebagai penghalang, melainkan sebagai penghubung yang menyatukan kehidupan bangsa."),
  ("p", "Cara pandang ini penting karena tanpa kesadaran akan kesatuan wilayah, Indonesia mudah terpecah berdasarkan kepentingan daerah atau kelompok. Wawasan nusantara mengajak setiap warga negara untuk merasa memiliki seluruh Indonesia, bukan hanya daerah asalnya sendiri."),
  ("p", "Bagi mahasiswa, kesadaran akan kesatuan wilayah dapat tumbuh melalui interaksi dengan teman dari berbagai daerah. Pengalaman ini memperlihatkan bahwa keberagaman wilayah dan budaya justru memperkaya, bukan melemahkan, kesatuan bangsa."),
 ],
 "8": [
  ("h2", "Membangun Generasi Berintegritas"),
  ("p", "Tujuan akhir pendidikan antikorupsi adalah lahirnya generasi yang berintegritas. Generasi berintegritas bukan hanya menolak korupsi ketika kelak menjadi pejabat, tetapi sudah membiasakan kejujuran sejak masih menjadi mahasiswa. Integritas yang dilatih sejak dini akan menjadi karakter yang kuat di kemudian hari."),
  ("p", "Membangun generasi berintegritas menuntut keteladanan dari berbagai pihak. Dosen yang adil dalam menilai, kampus yang tegas terhadap kecurangan, dan keluarga yang menanamkan kejujuran semuanya saling melengkapi. Tanpa keteladanan, ajakan untuk berintegritas hanya akan menjadi kata-kata kosong."),
  ("p", "Mahasiswa dapat menjadi bagian dari generasi ini melalui keputusan kecil setiap hari, seperti mengerjakan tugas dengan jujur, mengakui kesalahan, dan berani menolak ajakan berbuat curang. Dari kebiasaan inilah lahir pemimpin masa depan yang bersih dan dapat dipercaya."),
 ],
}

def _splice_naila5():
    for bab in BAB:
        no = bab["no"]; isi = bab["isi"]
        if no in EXTRA5:
            idx = next((i for i,(k,t) in enumerate(isi) if k=="h2" and "Rangkuman" in t), len(isi))
            isi = isi[:idx] + EXTRA5[no] + isi[idx:]
        n=0; new=[]
        for blk in isi:
            if blk[0]=="h2":
                n+=1
                t2=_re.sub(r"^\s*\d+\.\d+\s+","",blk[1])
                new.append(("h2", f"{no}.{n} {t2}"))
            else:
                new.append(blk)
        bab["isi"]=new

_splice_naila5()
