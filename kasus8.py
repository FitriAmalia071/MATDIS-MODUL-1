bayar_cash = True
bayar_transfer = True

metode_valid = bayar_cash ^ bayar_transfer

if metode_valid:
    print("Metode pembayaran VALID")
else:
    print("Pilih salah satu metode pembayaran")