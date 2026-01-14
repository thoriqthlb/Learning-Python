# Macam-macam data yang bisa digunakan

# 1: Angka non-desimal (Integer)
data_integer = 1000
print("data: ", data_integer, "bertipe", type(data_integer))

# 2: Angka desimal (Float)
data_float = 10.5
print("data: ", data_float, "bertipe", type(data_float))

# 3: Kumpulan karakter (String)
data_string = "AbCd"
print("data: ", data_string, "bertipe", type(data_string))

# 4: Biner atau True/False (Boolean)
data_bool = True
print("data: ", data_bool, "bertipe", type(data_bool))


## Tipe Data Khusus
# bilangan kompleks
data_kompleks = complex(5, 6)
print("data: ", data_kompleks, "bertipe", type(data_kompleks))

# tipe data dari bahasa C
from ctypes import c_double, c_longlong