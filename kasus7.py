jalur_reguler = True
jalur_prestasi = False

pilihan_valid = jalur_reguler ^ jalur_prestasi

if pilihan_valid:
    print("Pilihan jalur VALID")
else:
    print("Pilihan jalur TIDAK VALID")