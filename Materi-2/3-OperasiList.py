data_angka = [1,6,5,7,4,7,8,3,2,6,7,1,8,4,7,2,9,8,3,6,0,7,1]

print(f"data angka = \n{data_angka}")

### Count Data (menghitung jumlah data)

jumlah_data_7 = data_angka.count(7)
jumlah_data_6 = data_angka.count(6)

print(f"Jumlah data 6 = {jumlah_data_6}")
print(f"Jumlah data 7 = {jumlah_data_7}")

### Ambil Posisi Data (index)

data = ["Udin", "Rizki", "Hilmy", "Ucup"]

print(f"data = {data}")

index_rizki = data.index("Rizki")

print(f"index Rizki = {index_rizki}")

### Mengurutkan List (sort)

# data angka
print(f"data angka sebelum disort = {data_angka}")

data_angka.sort()
print(f"data angka setelah disort = {data_angka}")

# data string
print(f"data sebelum disort = {data}")

data.sort()
print(f"data setelah disort = {data}")

### Reverse List

data.reverse()
data_angka.reverse()
print(f"data direverse = \n{data} \n{data_angka}")