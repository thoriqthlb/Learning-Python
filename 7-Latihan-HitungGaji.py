print("\n===SLIP GAJI MAGANG===\n")

nama = input("Masukkan nama: ")
hari = int(input("Berapa hari Anda masuk: "))

print("------------------------")

saku = int(input("Saku harian: Rp"))
gaji = int(input("Gaji harian: Rp"))

print("------------------------")

total = (saku + gaji) * hari

# MENAMBAHKAN TITIK DI TIAP RIBUAN (PENYEMPURNAAN)
print(f"{nama} secara total menerima: Rp{total:,}" .replace(",", "."), "dalam", hari, "hari.")

### KODE AWAL YANG DIBUAT UNTUK ANGKA (TANPA TITIK)
# print(nama, "secara total menerima: Rp", total, "dalam", hari, "hari.")


### ILMU BARU UNTUK (INT) AGAR BISA ADA TITIKNYA (f-string/format string)
# print(f"{nama} secara total menerima: Rp{total:,}".replace(',', '.') + " dalam", hari, "hari.")