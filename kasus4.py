file_pdf = False
file_word = True
file_gambar = False

diterima = file_pdf or file_word or file_gambar

if diterima:
    print("Tugas DITERIMA")
else:
    print("Tugas DITOLAK")