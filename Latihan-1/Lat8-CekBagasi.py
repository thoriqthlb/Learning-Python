print("\n===== SELF CHECK IN BAGASI =====\n")

nama = input("Masukkan nama: ")
panjang_koper = int(input("Masukkan panjang koper (cm): "))
lebar_koper = int(input("Masukkan lebar koper (cm): "))
tinggi_koper = int(input("Masukkan tinggi koper (cm): "))
berat_koper = int(input("Masukkan berat koper (kg): "))
uang_koper = int(input("Masukkan uang koper yang dibayarkan: "))
powerbank = input("Apakah membawa power bank? (y/n): ")
kapasitas = int(input("Berapa kapasitasnya? (jika tidak bawa tulis '0'): "))
cairan = input("Apakah membawa benda cair? (y/n): ")
volume = int(input("Berapa volumenya? (jika tidak bawa tulis '0'): "))
packing = input("Apakah sudah dipacking? (jika tidak bawa pilih 'y') (y/n): ")


print("<--------------------------------------->\n")
print(f"Hasil analisis sistem self-checking bagasi atas nama: {nama}\n")

# Syarat-Syarat
dimensi = panjang_koper < 80 and lebar_koper < 80 and tinggi_koper < 80 
berat = (berat_koper <= 20) or (uang_koper >= 100000)
powerbank_aman = kapasitas <= 20000
cairan_aman = (volume < 100) and (packing == "y")

# Output
print(f"Dimensi Koper lolos? (max 80 cm):  {dimensi}")
print(f"Apakah berat ({berat_koper} kg) dan pembayaran aman?: {berat}")
print(f"Keamanan powerbank ({kapasitas:,} mAh):  {powerbank_aman}".replace(",","."))
print(f"Keamanan cairan ({volume} ml): {cairan_aman}")

print("<--------------------------------------->\n")

# Keputusan Akhir
keputusan = dimensi and berat and powerbank_aman and cairan_aman
print("Status Bagasi:", keputusan)
print("=======================================")