# Kumpulan data (di bahasa lain namanya Array)

# Kumpulan data angka
data_angka = [1,2,3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup","udin","siti"]
print(data_string)

# Kumpulan data boolean
data_bool = [True, False, True, True]
print(data_bool)

# Kumpulan campuran
data_campuran = [1, "bakwan",3, "udin", True]
print(data_campuran)

### Cara Alternatif Membuat List
data_range = range(0,10)
print(data_range)
data_list = list(data_range)
print(data_list)

### Membuat List Dengan For Loop, List Comprehension
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)


### Membuat List Pakai For Pakai If
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

# Ganjil
list_pake_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_pake_for_if)

# Genap
list_pake_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_pake_for_if)