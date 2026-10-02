aktif_organisasi = False
ikut_lomba = True
menjadi_panitia = False

nilai_tambahan = aktif_organisasi or ikut_lomba or menjadi_panitia

if nilai_tambahan:
    print("Mendapat nilai tambahan")
else:
    print("Tidak mendapat nilai tambahan")