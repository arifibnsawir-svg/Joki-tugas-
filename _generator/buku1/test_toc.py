from weasyprint import HTML

def run(label, css):
    html = """<!DOCTYPE html><html><head><meta charset='utf-8'><style>%s</style></head><body>
    <div class='cover'>COVER</div>
    <div class='content'>
      <ul class='toc'>
        <li><a href='#a'>Bab A</a></li>
        <li><a href='#b'>Bab B</a></li>
        <li><a href='#c'>Bab C</a></li>
      </ul>
      <section id='a' class='sec'>A<br>isi</section>
      <section id='b' class='sec'>B</section>
      <section id='c' class='sec'>C</section>
    </div></body></html>""" % css
    doc = HTML(string=html).render()
    # ekstrak teks toc page (page 2 = setelah cover)
    from io import BytesIO
    import pypdf
    bio = BytesIO(); doc.write_pdf(bio); bio.seek(0)
    r = pypdf.PdfReader(bio)
    print(f"[{label}] pages={len(r.pages)} | TOC page text:")
    print("   ", repr((r.pages[1].extract_text() or '')[:200]))

base_page = "@page{size:A4;margin:2cm;@bottom-center{content:counter(page);}} @page cover{margin:0;@bottom-center{content:'';}} .cover{page:cover;break-after:page;} .sec{break-before:page;} .toc a::after{content:leader('.') target-counter(attr(href url), page);}"

run("tanpa reset", base_page)
run("reset di .content", base_page + " .content{counter-reset:page 1;}")
run("reset di sec pertama (a)", base_page + " #a{counter-reset:page 1;}")
