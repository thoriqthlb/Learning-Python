# 1. Latihan logika peluru
peluru = 5
while peluru > 0:
    print("Tembak!")
    peluru = peluru - 1
print("Peluru Habis!")

# 2. Latihan menulis hukuman

# for
tulisan = range(1,11)
for i in tulisan:
    print(f"Saya janji tidak akan telat lagi. {i}")
print("\nSelesai.")

# while
angka = 0
while angka < 10:
    angka += 1
    print("Saya janji tidak akan telat lagi.")
print("Selesai.")

# 3. Latihan tanya sampai dibolehin
jawaban = input("Boleh main ngga?: ")
while jawaban != "boleh":
    print("yahh")
    jawaban = input("Kalau sekarang, boleh ngga?: ")
print("Okee, makasih")