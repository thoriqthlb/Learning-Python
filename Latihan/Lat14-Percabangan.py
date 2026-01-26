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