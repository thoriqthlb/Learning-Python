# Kalkulator Sederhana

print(20*"=")
print("Kalkulator Sederhana")
print(20*"="+"\n")

angka_pertama = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka_kedua = float(input("Masukkan angka kedua: "))

# Percabangannya

if operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"Hasilnya adalah: {hasil}")
elif operator == "-":
    hasil = angka_pertama - angka_kedua
    print(f"Hasilnya adalah: {hasil}")
elif operator == "*":
    hasil = angka_pertama * angka_kedua
    print(f"Hasilnya adalah: {hasil}")
elif operator == "/":
    hasil = angka_pertama / angka_kedua
    print(f"Hasilnya adalah: {hasil}")
else: print("Masukkan operator yang sesuai!")
print("\nSelesai.")


# Nyari nilai tertinggi

nilai_siswa = [60, 85, 70, 90, 50]

# 1. Anggap nilai pertama adalah yang tertinggi sementara
juara = nilai_siswa[0] 

# 2. Cek satu per satu
for nilai in nilai_siswa:
    
    # 3. Jika ketemu nilai yang LEBIH BESAR dari juara saat ini...
    # if nilai == max(nilai_siswa): (cara cepet)
    if nilai > juara: # sesuai algoritma

        # 4. Ganti posisi juara dengan nilai tersebut
        juara = nilai

print(f"\nNilai tertinggi adalah: {juara}\n")