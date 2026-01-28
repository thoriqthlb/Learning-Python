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

# 4. Latihan tebak angka
angka_rahasia = 7
angka = int(input("Masukkkan angka yang dimaksud: "))

while angka != angka_rahasia:
    if angka > angka_rahasia:
        print("Ketinggian! coba turunin.\n")
    if angka < angka_rahasia:
        print("Kerendahan! coba naikin.\n")
    angka = int(input("Coba tebak lagi: "))
print("Benar!\n")

# 5. Latihan hitung mundur roket
angka = range(10,0,-1)

for i in angka:
    print(i)
print("Meluncur!\n")

# 6. Latihan charge baterai
baterai = 0 # kondisi

while baterai <= 100: # syarat
    print(f"Mengisi baterai... {baterai}%") # aksi
    baterai += 20 # update kondisi
print("Baterai penuh!")

# 7. Latihan pake string
kata = "merdeka"

for i in kata:
    print(i)

ucap = input("Katakan sesuatu:")

while ucap != "berhenti":
    print(ucap)
    ucap = input("Katakan sesuatu:")
print("Oke.")