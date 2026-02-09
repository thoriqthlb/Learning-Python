# operator dictionary

data_dict = {
    "my":"Hilmy",
    "rz":"Rizki",
    "ya":"Yahya",
    "jt":"Jhet"
}

# Panjang Dictionary
LENDICT = len(data_dict)
print(f"Panjang data dict: {LENDICT}")

# Mengecek Key Ada Atau Tidak
KEY = "jt"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict: {CHECKKEY}")

# Mengakses value (read) dengan get
print(data_dict.get("my"))
print(data_dict.get("rd")) # tujuannya biar tau, ada atau ngga tanpa error

# Mengupdate data
data_dict["ya"] = "Reky"
print(data_dict)

# nambah
data_dict["ud"] = "Udin"
print(data_dict)

#delete
del data_dict["ud"]
print(data_dict)