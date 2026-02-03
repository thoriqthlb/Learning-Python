print("\n===KONVERTER DURASI\n")

detik_awal = int(input("Masukkan Detik: "))

jam = detik_awal // 3600
sisa_detik = detik_awal % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("Hasil konversi: ", jam, "Jam", menit, "Menit", detik, "Detik")