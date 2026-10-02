punya_kartu = False
terdaftar_online = False
mendapat_undangan = True

boleh_masuk = punya_kartu or terdaftar_online or mendapat_undangan

if boleh_masuk:
    print("Boleh mengikuti kegiatan")
else:
    print("Tidak boleh mengikuti kegiatan")