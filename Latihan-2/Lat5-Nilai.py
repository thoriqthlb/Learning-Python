# Latihan menghitung rata-rata nilai mahasiswa

nilai_mahasiswa = []

while True:
     nilai = (input("Masukkan nilai Anda: "))
     if nilai == "selesai":
        break
     nilai = int(nilai)
     nilai_mahasiswa.append(nilai)

print(f"""\nBERIKUT DAFTAR NILAI MAHASISWA:
{nilai_mahasiswa}

Total nilai: {sum(nilai_mahasiswa)}""")
if len(nilai_mahasiswa) > 0:
    print(f"Rata-rata nilai: {round(sum(nilai_mahasiswa)/len(nilai_mahasiswa), 2)}")
else: print("Tidak ada data nilai yang masuk.")