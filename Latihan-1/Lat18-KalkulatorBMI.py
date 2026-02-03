print(15*"=", "KALKULATOR BMI", 15*"=")

# input
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

# konversi
tinggi_m = tinggi / 100
imt = berat / (tinggi_m * tinggi_m)

# kondisi
if imt < 18.5:
    hasil = "Kurus"
elif 18.5 <= imt <= 24.9:
    hasil = "Ideal"
elif 25 <= imt <= 29.9:
    hasil = "Gemuk"
else: hasil = "Obesitas"

# output
print(f"""\nHasil Perhitungan BMI: {hasil}
Dengan Nilai IMT: {imt:,.2f}""")