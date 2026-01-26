# # Aplikasi toko game online sederhana 

# print(15*"=", "TOKO GAME ONLINE", 15*"=")
# print("Harga Game: Rp300.000\n")

# game = 300000
# dismember = 0
# diskode = 0
# gamexmember = game * 20/100
# gamexkode = 50000

# member = input("Punya kartu member? (y/n): ")
# kode = input("Ada kode?: ")
# saldo = int(input("Masukkan nominal saldo: "))

# if member == "y":
#     dismember = gamexmember
# elif kode == "jadijago":
#     diskode = gamexkode

# total = game - dismember - diskode
# saldo_kurang = total - saldo

# if saldo >= total:
#     status_sukses = "BERHASIL DIBELI"
# else: status_gagal = f"GAGAL, SALDO KURANG ({saldo_kurang})"

# print(30*"-"+"\n")

# print(f"""STRUK PEMBAYARAN:
# HARGA AWAL      : Rp{game:,}
# DISKON MEMBER   : Rp{dismember:,}
# DISKON KODE     : Rp{diskode:,}
# -------------------------------
# TOTAL BAYAR     : Rp{total:,}
# STATUS          : {status_gagal or status_sukses}""".replace(",","."))