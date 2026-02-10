nama_nama = {
    "jt":"Jhet",
    "my":"Hilmy",
    "rk":"Reky",
    "rz":"Rizki",
    "ya":"Yahya",
    "nf":"Naufal"
}

# looping first try (yg keluar keynya)

for nama in nama_nama:
    print(nama)

# operator untuk mengambil item / iterable
keys = nama_nama.keys()
print(keys)

for key in keys:
    print(nama_nama.get(key))

values = nama_nama.values()
print(values)

for value in values:
    print(value)

for key,value in nama_nama.items():
    print(key, "=", value)