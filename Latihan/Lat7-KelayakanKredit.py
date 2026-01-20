# Sistem kelayakan kredit motor

print("\n===== SISTEM CEK KREDIT DEALER =====\n")

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
gaji = int(input("Masukkan gaji: "))
status = input("Input Rumah 'sendiri' atau 'sewa': ")
cicilan = int(input("Masukkan biaya cicilan: "))
tabungan = int(input("Masukkan sisa tabungan: "))

print("---------------------------------------\n")
print(f"Hasil analisis sistem kredit atas nama: {nama}")

# Kumpulan syarat
syarat_umur = 21 <= umur <= 55
syarat_gaji = gaji >= 3000000
syarat_rumah = (status == "sendiri") or (status == "sewa" and gaji >= 5000000)
syarat_uang = tabungan >= 3 * cicilan

# Output analisis
print(f"Apakah usia ({umur}th) memenuhi:  {syarat_umur}")
print(f"Apakah gaji (Rp{gaji:,}) memenuhi:  {syarat_gaji}".replace(",","."))
print(f"Apakah status rumah ({status}) memenuhi:  {syarat_rumah}")
print(f"Syarat tabungan memenuhi (Rp{tabungan:,}):  {syarat_uang}".replace(",","."))

print("---------------------------------------\n")

keputusan = syarat_umur and syarat_gaji and syarat_rumah and syarat_uang
print(f"Keputusan akhir kelayakan kredit:  {keputusan}")
print("=======================================")



# Saran beberapa perbaikan
# print("\n===== SISTEM CEK KREDIT DEALER =====\n")

# nama = input("Masukkan nama: ")
# umur = int(input("Masukkan umur: "))
# # Kita simpan angka asli (int) untuk logika, tapi nanti ditampilkan pakai format
# gaji = int(input("Masukkan gaji: "))
# status = input("Input Rumah ('sendiri'/'sewa'): ")
# cicilan = int(input("Masukkan biaya cicilan: "))
# tabungan = int(input("Masukkan sisa tabungan: "))

# print("---------------------------------------\n")
# print(f"Analisa Kredit Atas Nama: {nama}")

# # --- LOGIKA (COPY PASTE DARI KODEMU) ---
# syarat1_umur = 21 <= umur <= 55
# syarat2_gaji = gaji >= 3000000
# # Bagian ini jenius!
# syarat3_rumah = (status == "sendiri") or (status == "sewa" and gaji >= 5000000)
# syarat4_nabung = tabungan >= (3 * cicilan)

# # --- OUTPUT DENGAN F-STRING ---
# # Perhatikan cara menampilkan True/False tapi ada penjelasannya
# print(f"1. Usia ({umur} th) Layak (21-55)?       : {syarat1_umur}")
# print(f"2. Gaji (Rp {gaji:,}) Cukup?             : {syarat2_gaji}")
# print(f"3. Status Rumah ({status}) Valid?        : {syarat3_rumah}")
# print(f"4. Tabungan Aman (>= 3x Cicilan)?      : {syarat4_nabung}")

# print("---------------------------------------")

# keputusan = syarat1_umur and syarat2_gaji and syarat3_rumah and syarat4_nabung
# print(f"KEPUTUSAN AKHIR (Disetujui?): {keputusan}")
# print("\n=======================================\n")