# Estimator halaman: simulasi tinggi baris vs tinggi area teks (A4, margin render.py).
import math, konten

PAGE_H = 29.7*28.3465      # pt (1cm=28.3465pt)
TOP, BOT = 3*28.3465, 2.5*28.3465
TEXT_H = PAGE_H - TOP - BOT
LEFT, RIGHT = 3*28.3465, 2.5*28.3465
TEXT_W = 21*28.3465 - LEFT - RIGHT

CPL_BODY = max(1, int(TEXT_W / 6.4))   # ~ chars per line TNR 12
LH_BODY = 12*1.5                       # 18pt
SP_AFTER = 10
LH_H1 = 16*1.5
LH_H2 = 13*1.5

def body_lines(text):
    return max(1, math.ceil(len(text)/CPL_BODY))

def simulate():
    y = 0.0
    pages = 1
    def newpage():
        nonlocal y, pages
        pages += 1; y = 0.0
    def add(h):
        nonlocal y
        if y + h > TEXT_H:
            newpage()
        y += h
    # KATA PENGANTAR
    add(LH_H1*2 + SP_AFTER)
    for p in konten.KATA_PENGANTAR:
        add(body_lines(p)*LH_BODY + SP_AFTER)
    newpage()  # page break
    # DAFTAR ISI (TOC kosong ~ akan terisi Word; hitung minimal 1 hal)
    add(LH_H1 + SP_AFTER)
    add(LH_BODY*2)
    newpage()
    # BAB
    for b in konten.BAB:
        # page break sebelum tiap bab
        newpage()
        add(LH_H1 + SP_AFTER)  # BAB X
        add(LH_H1 + SP_AFTER)  # judul
        for k,t in b['isi']:
            if k=='h2':
                add(LH_H2*max(1,math.ceil(len(t)/CPL_BODY)) + 6 + 12)
            else:
                add(body_lines(t)*LH_BODY + SP_AFTER)
    # DAFTAR PUSTAKA
    newpage()
    add(LH_H1 + SP_AFTER)
    for r in konten.DAFTAR_PUSTAKA:
        add(body_lines(r)*LH_BODY + SP_AFTER)
    return pages

body_pages = simulate()
print('CPL_BODY:', CPL_BODY, 'lines/page ~', round(TEXT_H/LH_BODY,1))
print('Estimasi halaman ISI (tanpa TOC terisi):', body_pages)
print('+ 2 cover =', body_pages+2)
print('Catatan: Daftar Isi (TOC) akan menambah ~2-3 hal saat dibuka di Word.')
