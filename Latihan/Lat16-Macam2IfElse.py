# # 1. PASSWORD (easy)

# pasw = input("Masukkan password: ")

# if pasw == "kopi":
#     print("Oke, masuk.")
# else: print("Password salah!")

# # 2. SISTEM TILANG (med-easy)

# velo = int(input("Masukkan kecepatan (km/h): "))

# if velo > 60:
#     denda = (velo - 60) * 10000
#     print(f"Anda didenda sebesar: Rp{denda:,}".replace(",","."))
# else: print("Selamat jalan, tetap hati-hati!")

# # 3. DISKON SEDERHANA (med)

# beli = int(input("Jumlah beli berapa: "))
# martabak = 30000
# total = beli * martabak

# if beli >= 3:
#     diskon = total * 10/100
# else: diskon = 0

# harga = total - diskon

# print(f"""Harga awal = {total}
# Potongan: {diskon}
# Total: {harga}""")

# 4. MEMILIH MAKANAN (med)

nasgor = 15000
beli = int(input("Beli berapa?: "))
telur = input("Mau nambah telur? (y/n): ")
ati = input("Mau nambah ati? (y/n): ")
total = nasgor * beli

if telur == "y":
    total = total + 3000 * beli
if ati == "y":
    total = total + 5000 * beli

print(f"TOTAL BAYAR: Rp{total:,}".replace(",","."))