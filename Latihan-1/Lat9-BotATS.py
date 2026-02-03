print("\n===== PENYARINGAN CV OTOMATIS =====\n")

# Input
nama = input("Masukkan nama: ")
ipk = float(input("Masukkan IPK Anda: "))
usia = int(input("Masukkan usia Anda: "))
skill = input("Apakah bisa 'python'/'java'? ketikkan yang Anda bisa (kosongkan jika tidak ada): ").lower()
pengalaman = int(input("Berapa lama pengalaman Anda sebelumnya? (dalam bulan): "))
sertif = input("Punya sertifikat kompetensi? (ya/tidak): ").lower()

# Syarat
min_ipk = ipk >= 3.00
maks_usia = usia <= 25
skillnya = (skill == "python") or (skill == "java")
boleh = pengalaman >= 24 or sertif == "ya"
lolos = min_ipk and maks_usia and skillnya and boleh

# Output
print("\n<--------------------------------------->\n")
print(f"Hasil penyaringan CV otomatis atas nama: {nama}\n")

print(f"IPK = {ipk} (minimal 3.00): {min_ipk}")
print(f"Usia = ({usia} tahun) (maksimal 25 tahun): {maks_usia}")
print(f"Skill yang dimiliki = {skill} (minimal ada satu skill): {skillnya}")
print(f"Pengalaman sebelumnya = ({pengalaman} bulan) (minimal 24 bulan/ada sertif): {boleh}")

print("\n<--------------------------------------->\n")

# Kesimpulan
print("Berdasarkan penilaian bot maka status Anda:", lolos)

# ILMU BARU

# kasih .lower() di akhir buat jadiin input otomatis lowercase