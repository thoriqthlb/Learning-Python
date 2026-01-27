# Aplikasi toko game online sederhana 

print(15*"=", "TOKO GAME ONLINE", 15*"=")
print("Harga Game: Rp300.000\n")

harga = 300000 
game = 300000 # nilai yang bisa berubah 
stat_member = 0
stat_kode = 0

member = input("Punya kartu member? (y/n): ")
kode = input("Punya kode khusus? (lewati jika tidak punya): ")
saldo = int(input("Masukkan jumlah saldo Anda: "))

# MEMBER
if member == "y":
    stat_member = (game * 20/100)   # diskon persen duluan beda hasilnya
    game = game - stat_member       # dengan angka duluan, jadi sesuaiin sama keinginan.
                                     
# KODE
if kode == "jadijago":
    stat_kode = 50000
    game = game - stat_kode

# SALDO
if saldo >= game:
    status = "Pembelian Berhasil!"
    sisa = saldo - game
else: 
    status = "Pembelian Gagal!"
    sisa  = saldo

print("---------------------------------------\n")

print(f"""Struk Pembayaran:
      Harga Awal   : Rp{harga:,}
      Diskon Member: Rp{stat_member:,}
      Diskon Kode  : Rp{stat_kode:,}
---------------------------------------\n
Total Bayar : Rp{game:,}
Status      : {status}
Saldo Awal  : Rp{saldo:,}
Sisa Saldo  : Rp{sisa:,}
---------------------------------------\n""".replace(",","."))