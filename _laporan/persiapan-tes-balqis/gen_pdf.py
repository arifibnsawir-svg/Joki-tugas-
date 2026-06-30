# -*- coding: utf-8 -*-
"""
Render lembar persiapan tes lisan wawancara helper untuk Balqis Sandra Lejla -> PDF.
Pendekatan mengikuti _laporan/wawancara-helper/gen_pdf.py (WeasyPrint, A4,
Liberation Serif yang kompatibel Times New Roman, spasi 1.5, margin kiri 4cm /
kanan 3cm / atas 3cm / bawah 3cm, nomor halaman Arab di bawah-tengah,
hyphens:none, humanizer-clean: tanpa em-dash/en-dash/kutip melengkung/emoji).
"""
import os
import html as _html

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "PERSIAPAN_TES")
OUTDIR = os.path.abspath(OUTDIR)
OUTPDF = os.path.join(
    OUTDIR,
    "Persiapan Tes Wawancara - Balqis Sandra Lejla - Pengembangan Profesi Konseling.pdf",
)


def esc(t):
    return _html.escape(str(t))


IDENTITAS = {
    "judul": "PERSIAPAN TES LISAN WAWANCARA HELPER",
    "subjudul": "Prediksi Pertanyaan dan Jawaban - Pengembangan Profesi Konseling",
    "nama": "Balqis Sandra Lejla",
    "nim": "202501500525",
    "prodi": "Program Studi Bimbingan dan Konseling",
    "fakultas": "Fakultas Ilmu Pendidikan dan Pengetahuan Sosial (FIPPS)",
    "universitas": "Universitas Indraprasta PGRI",
    "matakuliah": "Pengembangan Profesi Konseling",
    "dosen": "Burju Ruth, M.Pd., Kons.",
    "tahun": "2026",
}

INTRO = (
    "Lembar ini merupakan alat bantu belajar yang disusun berdasarkan Rencana "
    "Pembelajaran Semester dan laporan wawancara helper kelompok. Jawaban di bawah "
    "merupakan jawaban model yang sebaiknya dipahami dan dilatih dengan bahasa "
    "sendiri, bukan dihafal kata demi kata."
)

QA = [
    (
        "Coba jelaskan secara singkat isi laporan wawancara kelompok kalian.",
        "Laporan kami berjudul Laporan Wawancara dengan Helper Pemberi Layanan. "
        "Tujuannya memahami praktik nyata profesi membantu melalui wawancara langsung "
        "terhadap empat helper dari bidang yang berbeda, yaitu anggota TNI Angkatan "
        "Darat, petugas pemadam kebakaran, bidan, dan guru bimbingan dan konseling. "
        "Kami menggunakan pendekatan kualitatif deskriptif dengan wawancara semi "
        "terstruktur. Setelah memaparkan hasil tiap helper, kami menganalisis "
        "persamaan, perbedaan, dan keterampilan kunci, lalu mengaitkannya dengan teori "
        "karakteristik dan peran helper dalam bimbingan dan konseling. Kesimpulannya, "
        "keterampilan menolong seperti empati, komunikasi, dan menjaga kepercayaan "
        "bersifat lintas profesi, tidak terbatas pada ruang konseling.",
    ),
    (
        "Kalian mewawancarai helper siapa saja dan mengapa memilih profesi itu?",
        "Kami mewawancarai empat helper, yaitu Bapak Lukman Hidayat dari TNI Angkatan "
        "Darat dengan pengalaman lima tahun, Bapak Rinno petugas pemadam kebakaran "
        "dengan pengalaman satu tahun, Ibu Priska Ayu Anjastari seorang bidan dengan "
        "pengalaman sepuluh tahun, dan Ibu Elisabeth Suwartini guru bimbingan dan "
        "konseling dengan pengalaman tiga puluh dua tahun. Kami sengaja memilih bidang "
        "yang berbeda agar terlihat keterampilan membantu yang bersifat universal "
        "sekaligus yang khas pada tiap profesi, sehingga kami dapat membandingkan "
        "bagaimana peran helper muncul di bidang keamanan, penyelamatan, kesehatan, "
        "dan pendidikan.",
    ),
    (
        "Apa kontribusi dan peranmu dalam pengerjaan tugas kelompok ini?",
        "Dalam kelompok, saya ikut menyusun pedoman pertanyaan wawancara, melakukan "
        "wawancara dan mencatat hasilnya, lalu membantu menulis dan merapikan bagian "
        "hasil serta pembahasan. Saya juga ikut memeriksa agar laporan sesuai format "
        "dosen dan sumber teorinya benar. (Catatan untuk Balqis: sesuaikan kalimat ini "
        "dengan peran nyatamu saat mengerjakan tugas.)",
    ),
    (
        "Apa persamaan dan perbedaan yang kalian temukan antar helper?",
        "Persamaannya, keempat helper sama-sama menempatkan keselamatan dan "
        "kepentingan orang yang dilayani sebagai prioritas utama, menekankan "
        "komunikasi yang menenangkan, terikat pada kode etik dan prosedur, serta "
        "digerakkan oleh motivasi pengabdian. Perbedaannya terletak pada bentuk "
        "layanan dan tantangannya. Anggota TNI menghadapi tantangan geografis dan "
        "ancaman perang informasi, petugas pemadam berhadapan dengan situasi darurat "
        "yang menuntut kecepatan, bidan menekankan kedekatan emosional dengan ibu dan "
        "anak, sedangkan guru bimbingan dan konseling menekankan kerahasiaan dan "
        "pendampingan psikologis jangka panjang.",
    ),
    (
        "Helper mana yang menurutmu paling dekat dengan profesi konselor, dan mengapa?",
        "Menurut saya guru bimbingan dan konseling, yaitu Ibu Elisabeth Suwartini, "
        "paling dekat dengan profesi konselor. Tugasnya langsung berkaitan dengan "
        "pendampingan psikologis, konseling individu dan kelompok, mendengar aktif, "
        "dan menjaga kerahasiaan, yang merupakan inti layanan bimbingan dan "
        "konseling. Meski demikian, helper lain tetap relevan karena menunjukkan "
        "keterampilan menolong yang juga dibutuhkan seorang konselor.",
    ),
    (
        "Apa itu helper, jelaskan dengan kata-katamu sendiri?",
        "Helper adalah orang yang memberikan bantuan kepada orang lain agar mampu "
        "menghadapi atau menyelesaikan persoalan yang dihadapinya. Dalam bimbingan dan "
        "konseling, helper tidak menggantikan peran orang yang dibantu, melainkan "
        "mendampingi agar yang bersangkutan mampu menolong dirinya sendiri. Dengan "
        "begitu hubungan membantu bersifat memberdayakan, bukan menciptakan "
        "ketergantungan.",
    ),
    (
        "Sebutkan karakteristik helper yang efektif menurut Carl Rogers.",
        "Carl Rogers melalui pendekatan yang berpusat pada pribadi menyebut tiga sikap "
        "inti. Pertama, kongruensi atau keselarasan, yaitu helper bersikap jujur dan "
        "apa adanya. Kedua, penerimaan positif tanpa syarat, yaitu menerima dan "
        "menghargai orang yang dibantu tanpa menghakimi. Ketiga, empati, yaitu "
        "kemampuan memahami perasaan dan dunia orang lain seakan-akan dialami sendiri "
        "tanpa kehilangan jarak yang sehat.",
    ),
    (
        "Apa perbedaan pandangan Rogers, Corey, dan Brammer tentang helper?",
        "Rogers menekankan tiga sikap inti berupa kongruensi, penerimaan tanpa syarat, "
        "dan empati. Corey menekankan kualitas pribadi konselor sebagai instrumen "
        "utama, seperti kesadaran diri, kejujuran, dan kesediaan terus belajar, karena "
        "teknik tanpa pribadi yang sehat akan kehilangan makna. Brammer memerinci "
        "karakteristik helper menjadi kesadaran akan diri dan nilai, kemampuan "
        "menganalisis perasaan, sikap altruistik, dan tanggung jawab etis, sekaligus "
        "menekankan keterampilan membantu yang dapat dilatih seperti mendengarkan dan "
        "memantulkan perasaan.",
    ),
    (
        "Apa saja peran helper dalam layanan?",
        "Menurut Gladding, helper dapat berperan sebagai pendengar yang aktif, pemberi "
        "informasi, fasilitator, penghubung dengan sumber daya lain, dan pendamping "
        "dalam proses perubahan. Dalam bimbingan dan konseling, peran ini mencakup "
        "membantu individu memahami diri, mengambil keputusan, menyesuaikan diri "
        "dengan lingkungan, dan mengembangkan potensinya secara optimal.",
    ),
    (
        "Apakah semua helper itu konselor? Jelaskan hubungannya.",
        "Tidak. Semua konselor adalah helper, tetapi tidak semua helper adalah "
        "konselor. Helper merupakan konsep yang luas yang mencakup siapa pun yang "
        "menjalankan peran menolong, sedangkan konselor adalah helper profesional yang "
        "terlatih secara akademik dan terikat oleh kode etik profesi.",
    ),
    (
        "Metode apa yang kalian pakai dalam wawancara, dan mengapa kualitatif "
        "deskriptif?",
        "Kami menggunakan pendekatan kualitatif deskriptif karena tujuan kegiatan "
        "adalah menggambarkan pengalaman, pandangan, dan keterampilan para helper apa "
        "adanya, bukan menguji hubungan antarvariabel atau mengukurnya dengan angka. "
        "Data yang terkumpul berupa penjelasan dan cerita yang kemudian disusun, "
        "dikelompokkan, dan ditafsirkan secara naratif.",
    ),
    (
        "Apa itu wawancara semi terstruktur, dan mengapa dipilih?",
        "Wawancara semi terstruktur adalah wawancara yang berpegang pada daftar "
        "pertanyaan pokok yang sudah disiapkan, tetapi tetap memberi ruang bagi "
        "narasumber untuk menjawab secara leluasa dan bagi pewawancara untuk menggali "
        "jawaban lebih dalam. Kami memilih teknik ini supaya jawaban yang diperoleh "
        "lebih kaya tanpa kehilangan arah pembahasan.",
    ),
    (
        "Bagaimana kalian menyusun pertanyaan wawancaranya?",
        "Pertanyaan kami susun berdasarkan capaian pembelajaran pada Rencana "
        "Pembelajaran Semester mata kuliah, seperti wawasan dasar profesi, kompetensi, "
        "kode etik, isu pelayanan, kredensial, tugas pokok, serta peluang dan "
        "tantangan. Setelah itu bahasanya kami sesuaikan dengan masing-masing profesi "
        "helper agar mudah dipahami narasumber.",
    ),
    (
        "Apa kaitan tugas wawancara ini dengan mata kuliah Pengembangan Profesi "
        "Konseling?",
        "Mata kuliah Pengembangan Profesi Konseling membahas wawasan dasar profesi, "
        "kompetensi, etika, organisasi profesi, dan tantangan profesi. Melalui tugas "
        "ini kami memahami secara nyata bagaimana sosok helper bekerja, keterampilan "
        "dan etika yang dibutuhkan, serta tantangan yang dihadapi, yang merupakan inti "
        "dari pengembangan profesi seorang konselor.",
    ),
    (
        "Keterampilan helper apa saja yang juga harus dimiliki seorang konselor?",
        "Keterampilan yang muncul berulang dari hasil wawancara adalah kemampuan "
        "mendengarkan dan berkomunikasi, empati, ketenangan dalam tekanan, kerja sama "
        "tim, serta tanggung jawab etis termasuk menjaga kerahasiaan. Semua "
        "keterampilan ini juga merupakan keterampilan inti yang harus dimiliki seorang "
        "guru bimbingan dan konseling atau konselor.",
    ),
    (
        "Apa itu kode etik, dan bagaimana helper yang kalian wawancara menjaga etika "
        "serta kerahasiaan?",
        "Kode etik adalah pedoman perilaku profesional yang mengatur hal yang perlu "
        "dilakukan dan dihindari dalam memberikan layanan. Setiap helper yang kami "
        "wawancarai memegang etika profesinya. Ibu Elisabeth sebagai guru bimbingan "
        "dan konseling menjaga kerahasiaan siswa dan menghindari sikap menghakimi, "
        "bidan menjaga kerahasiaan pasien dan mengutamakan keselamatan, sedangkan "
        "petugas keamanan dan penyelamatan berpegang pada prosedur. Dalam bimbingan "
        "dan konseling, etika ini diatur oleh kode etik ABKIN dan IKI, dengan asas "
        "kerahasiaan sebagai salah satu yang utama.",
    ),
    (
        "Menurut RPS, apa kualifikasi dan kompetensi seorang konselor?",
        "Menurut Rencana Pembelajaran Semester, kualifikasi dan kompetensi konselor "
        "mengacu pada Peraturan Menteri Pendidikan Nasional Nomor 27 Tahun 2008 "
        "tentang Standar Kualifikasi Akademik dan Kompetensi Konselor. Konselor harus "
        "berlatar pendidikan yang sesuai dan menguasai kompetensi pedagogik, "
        "kepribadian, sosial, dan profesional.",
    ),
    (
        "Apa peluang dan tantangan profesi helper atau konselor di abad 21?",
        "Peluangnya adalah semakin diakuinya pentingnya kesehatan mental dan layanan "
        "bimbingan bagi masyarakat. Tantangannya mencakup perkembangan teknologi dan "
        "dunia digital, kesenjangan generasi, stigma terhadap layanan bimbingan dan "
        "konseling, beban administratif, serta kebutuhan akan kompetensi baru dan "
        "regenerasi tenaga yang berkualitas.",
    ),
    (
        "Pelajaran apa yang kamu peroleh dari tugas ini sebagai calon guru bimbingan "
        "dan konseling?",
        "Saya belajar bahwa keterampilan menolong seperti empati, mendengar aktif, dan "
        "menjaga kepercayaan dibutuhkan di banyak profesi, tidak hanya di ruang "
        "konseling. Sebagai calon guru bimbingan dan konseling, saya semakin menyadari "
        "pentingnya menguasai keterampilan komunikasi, menjaga etika, dan hadir secara "
        "tulus bagi orang yang dibantu.",
    ),
    (
        "Bagaimana kamu akan menerapkan hasil wawancara ini ketika menjadi konselor "
        "nanti?",
        "Saya akan menerapkannya dengan menempatkan kebutuhan klien sebagai pusat "
        "layanan, mendengarkan tanpa menghakimi, menjaga kerahasiaan, dan "
        "berkolaborasi dengan pihak lain ketika sebuah kasus membutuhkannya, sama "
        "seperti yang dilakukan para helper yang kami wawancarai.",
    ),
]

FAKTA_KUNCI = [
    "Trilogi Profesi dan wawasan dasar: Profesi Bermartabat, Pelayanan Bermanfaat, "
    "Petugas Bermandat, Pengakuan dari Masyarakat.",
    "Kompetensi konselor mengacu pada Permendiknas Nomor 27 Tahun 2008 tentang SKAKK.",
    "Kode etik profesi bimbingan dan konseling: ABKIN dan IKI.",
    "Pola layanan: Pola 17 plus (Permendikbud Nomor 81A Tahun 2013) dan BK "
    "Komprehensif (Permendikbud Nomor 111 Tahun 2014).",
    "Tokoh teori helper: Rogers, Corey, Brammer, Gladding, dan Prayitno.",
]

CSS = r"""
@page {
  size: A4;
  margin: 3cm 3cm 3cm 4cm;
  @bottom-center { content: counter(page); font-family:'Liberation Serif',serif; font-size:11pt; color:#000; }
}

html { font-family:'Liberation Serif','Times New Roman',serif; }
body { font-size:12pt; line-height:1.5; text-align:justify; color:#000; hyphens:none; }
p { margin:0 0 6pt 0; orphans:2; widows:2; }

/* ====== HEADER BLOCK ====== */
.header { text-align:center; margin:0 0 14pt 0; padding-bottom:10pt; border-bottom:0.75pt solid #BBBBBB; }
.header .judul { font-size:16pt; font-weight:bold; color:#000; text-transform:uppercase; line-height:1.35; }
.header .subjudul { font-size:12pt; font-style:italic; color:#000; margin-top:6pt; }
.identitas { margin:12pt 0 0 0; text-align:center; line-height:1.45; }
.identitas .nm { font-weight:bold; font-size:12.5pt; }
.identitas .baris { font-size:11.5pt; }

/* ====== INTRO ====== */
.intro { margin:14pt 0 16pt 0; text-align:justify; }

h2.bagian { font-size:13pt; font-weight:bold; color:#000; text-align:center;
  margin:18pt 0 12pt 0; padding-bottom:5pt; border-bottom:0.5pt solid #BBBBBB; break-after:avoid; }

/* ====== QA ====== */
.qa { margin:0 0 12pt 0; break-inside:avoid; }
.qa .q { font-weight:bold; color:#000; margin:0 0 4pt 0; }
.qa .a { color:#000; }
.qa .a .lbl { font-style:italic; }

/* ====== FAKTA KUNCI ====== */
ul.fakta { margin:4pt 0 0 0; padding-left:1.0cm; }
ul.fakta li { margin:0 0 6pt 0; text-align:justify; }
"""


def header_block():
    I = IDENTITAS
    p = ['<div class="header">']
    p.append('<div class="judul">%s</div>' % esc(I["judul"]))
    p.append('<div class="subjudul">%s</div>' % esc(I["subjudul"]))
    p.append("</div>")
    p.append('<div class="identitas">')
    p.append('<div class="nm">%s</div>' % esc(I["nama"]))
    p.append('<div class="baris">NIM. %s</div>' % esc(I["nim"]))
    p.append('<div class="baris">%s</div>' % esc(I["prodi"]))
    p.append('<div class="baris">%s</div>' % esc(I["fakultas"]))
    p.append('<div class="baris">%s</div>' % esc(I["universitas"]))
    p.append('<div class="baris">Mata Kuliah: %s (Dosen: %s)</div>' % (esc(I["matakuliah"]), esc(I["dosen"])))
    p.append('<div class="baris">%s</div>' % esc(I["tahun"]))
    p.append("</div>")
    p.append('<p class="intro">%s</p>' % esc(INTRO))
    return "".join(p)


def qa_block():
    p = ['<h2 class="bagian">Prediksi Pertanyaan dan Jawaban</h2>']
    for i, (q, a) in enumerate(QA, 1):
        p.append('<div class="qa">')
        p.append('<div class="q">%d. %s</div>' % (i, esc(q)))
        p.append('<div class="a"><span class="lbl">Jawaban:</span> %s</div>' % esc(a))
        p.append("</div>")
    return "".join(p)


def fakta_block():
    p = ['<h2 class="bagian">Fakta Kunci untuk Diingat</h2>']
    p.append("<ul class=fakta>")
    for f in FAKTA_KUNCI:
        p.append("<li>%s</li>" % esc(f))
    p.append("</ul>")
    return "".join(p)


def content_html():
    p = ['<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS]
    p.append(header_block())
    p.append(qa_block())
    p.append(fakta_block())
    p.append("</body></html>")
    return "".join(p)


def main():
    from weasyprint import HTML
    os.makedirs(OUTDIR, exist_ok=True)
    html = content_html()
    doc = HTML(string=html).render()
    print("Total halaman PDF:", len(doc.pages))
    doc.write_pdf(OUTPDF)
    print("SAVED:", OUTPDF, os.path.getsize(OUTPDF), "bytes")


if __name__ == "__main__":
    main()
