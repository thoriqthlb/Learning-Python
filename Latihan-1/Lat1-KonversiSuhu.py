#latihan konversi satuan temperatur

print("\n===== PROGRAM KONVERSI TEMPERATUR =====\n")

# celcius
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu adalah: ", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu reamur adalah: ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu fahrenheit adalah: ", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu kelvin adalah: ", kelvin, "Kelvin")


## kelvin to fahrenheit
# print("\n===== KELVIN TO FAHRENHEIT VIA CELCIUS =====\n")

# Kelvin = float(input("Masukkan suhu dalam kelvin: "))
# celcius = Kelvin - 273
# fahrenheit = 9/5 * celcius + 32
# print("Suhu adalah: ", fahrenheit, "Fahrenheit")