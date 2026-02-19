# Program Menghitung Luas dan Keliling Persegi Panjang

import os
# os.system("cls")

# # Membuat Header Program
# print(f"{'='*38:^40}")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN':^40}")
# print(f"{'KELILING PERSEGI PANJANG':^40}")
# print(f"{'='*38:^40}\n")

# # Mengambil Input User
# PANJANG = int(input("Masukkan nilai panjang: "))
# LEBAR = int(input("Masukkan nilai lebar: "))

# # Program Menghitung Luas & Keliling
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG + LEBAR)

# # Tampilkan Hasilnya
# print(f"Hasil Perhitungan Luas: {LUAS} persegi")
# print(f"Hasil Perhitungan Keliling: {KELILING}")

def header():
    '''Fungsi Header'''
    os.system("cls")
    print(f"{'='*38:^40}")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN':^40}")
    print(f"{'KELILING PERSEGI PANJANG':^40}")
    print(f"{'='*38:^40}\n")

def input_user():
    '''Fungsi Input User'''
    # Mengambil Input User
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))

    return panjang,lebar

def hitung_luas(panjang,lebar):
    '''Fungsi Luas'''
    return panjang*lebar

def hitung_keliling(panjang,lebar):
    '''Fungsi Keliling'''
    return 2*(panjang + lebar)

# Program Utama
while True:
    header()
    PANJANG, LEBAR = input_user()
    LUAS = hitung_luas(PANJANG,LEBAR)
    KELILING = hitung_keliling(PANJANG,LEBAR)

    print(f"Hasil Perhitungan Luas: {LUAS} persegi")
    print(f"Hasil Perhitungan Keliling: {KELILING}")

    LanjutGA = input("Apakah ingin lanjut? (y/n): ")
    if LanjutGA == "n":
        break
print("\nProgram selesai, terima kasih.")