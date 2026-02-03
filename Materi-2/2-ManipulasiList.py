### Operasi

# index    0       1       2
data = ["Ucup", "Udin", "Siti"]

## Mengambil data dari list
data_0 = data[0]
print(f"Data pertama (index 0) = {data_0}")

# kalo gatau terakhir berapa, bisa dari -1
data_terakhir = data[-1]
print(f"Data terakhir (index -1)= {data_terakhir}")

# Mengambil info jumlah data dalam list
jumlah_data = len(data)
print(f"Jumlah data ada = {jumlah_data}")


### Manipulasi Data List
print(f"Data sebelum ditambah = {data}")

## ---- 1. Menambahkan item pada list sesuai posisi (INSERT)

data.insert(2, "Yudi") # Aturan >>>> list.insert(urutan, item)
print(f"Data setelah ditambah = {data}")

## ---- 2. Menambahkan item di akhir list (APPEND)

data.append("Mahmud") # Aturan >>>> list.append(item)
print(f"Data ditambah lagi = {data}")

## ---- 3. Menambah list dengan list (EXTEND)

data_baru = ["Yahya", "Hilmy", "Rizki"]
print(f"Data list baru = {data_baru}")

data.extend(data_baru) # Aturan >>>> list.extend(list_baru)
print(f"Data gabungan = {data}")


## ---- 4. Mengubah data dengan data  baru

# misal data index 2 diubah dengan data baru
data[2] = "Ipul"
print(f"Data setelah diubah = {data}")

## ---- 5. Membuang data (REMOVE)

data.remove("Mahmud") # Aturan >>>> list.remove(data_yang_mau_dihapus)
print(f"Data setelah dihapus {data}")

## ---- 6. Membuang data paling belakang (POP)

data.pop() # Aturan >>>> list.pop()
print(f"Data Akhir {data}")