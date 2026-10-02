aktif = True
nilai_memenuhi = True
prasyarat = True

lulus = aktif and nilai_memenuhi and prasyarat

if lulus:
    print("Peserta LULUS")
else:
    print("Peserta TIDAK LULUS")