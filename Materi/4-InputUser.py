# Mengambil data dari inputan user

# Data yang dimasukkan pasti string
data = input("Masukkan data: ")

print("Data: ", data, "tipenya: ", type(data))

# Jika mau mengambil int/float, maka
angka = float(input("Masukkan angka: "))
angka = int(input("Masukkan angka: "))

print("Data angka: ", angka, "tipenya: ", type(angka))

# Khusus boolean
biner = bool(int(input("Masukkan nilai bool: ")))

print("Data bool: ", biner, "tipenya: ", type(biner))