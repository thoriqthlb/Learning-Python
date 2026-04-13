# Latihan Final Fungsi (Health Metrics & Nutrition Planner)
import os
os.system("cls")

def hitung_bmi(berat, tinggi_cm):
    '''menampilkan hasil BMI'''

    tinggi = tinggi_cm / 100
    bmi = berat / (tinggi**2)

    return bmi

def kategori_kesehatan(skor_bmi):
    '''menerjemahkan angka BMI menjadi status kesehatan'''

    if skor_bmi < 18.5:
        status_kes = "Kurus"
    elif skor_bmi <= 24.9:
        status_kes = "Ideal"
    elif skor_bmi >= 25:
        status_kes = "Obesitas"

    return status_kes

def kebutuhan_air(*data_fisik):
    '''menentukan berapa kebutuhan harian'''

    data_air = (data_fisik[0] * 0.033) + (data_fisik[1] * 0.5)

    return data_air

def buat_laporan(nama, **hasil_analisis):
    '''laporan dari hasil-hasil yang ada'''

    print("\n----- GENERATING REPORT... -----\n")

    print(20*"=",)
    print(f"HASIL ANALISIS KESEHATAN: {nama}")
    print(20*"=",)

    print(f"Skor BMI Anda: {hasil_analisis['bmi']:.2f}")
    print(f"Status Kesehatan: {hasil_analisis['sehat']}")
    print(f"Kebutuhan Air: {hasil_analisis['air']:.2f} liter")

    print(40*"-")
    print("CATATAN: Jaga kondisi tubuh Anda dengan rutin berolahraga!")
    print(40*"=")

# Program Utama
print("--- FORM INPUT KESEHATAN ---")

nama = input("Masukkan nama Anda: ").capitalize()
berat_badan = int(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = int(input("Masukkan tinggi badan Anda (cm): "))
jam_olaraga = float(input("Masukkan jam olahraga hari ini: "))

bmi_user = hitung_bmi(berat_badan, tinggi_badan)
kesehatan_user = kategori_kesehatan(bmi_user)
air_user = kebutuhan_air(berat_badan, jam_olaraga)

buat_laporan(nama, bmi = bmi_user, sehat = kesehatan_user, air = air_user)