terdaftar = True
sudah_bayar = True
memenuhi_syarat = True

boleh_ujian = terdaftar and sudah_bayar and memenuhi_syarat

if boleh_ujian:
    print("Boleh mengikuti ujian")
else:
    print("Tidak boleh mengikuti ujian")