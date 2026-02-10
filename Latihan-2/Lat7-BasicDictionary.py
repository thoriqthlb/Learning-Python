# Perkuat Basic Dictionary

# 1
nama_nama = {
    "jt":"Jhet",
    "my":"Hilmy",
    "rk":"Reky"
}

for key in nama_nama:
    print(f"kode {key} adalah {nama_nama[key]}")

# 2
kode = "my"
print(f"Nama dengan kode {kode} adalah {nama_nama[kode]}")

# 3
for nama in nama_nama.values():
    print(nama)

# 4
for nama in nama_nama.values():
    if len(nama) > 4:
        print(nama)

# 6
nama_nama = {
    "jt":"Jhet",
    "my":"Hilmy",
    "rk":"Reky"
}

for key in nama_nama:
    print(f"kode {key} = {nama_nama[key]}".upper())

# 7
nama_nama = {
    "jt":"Jhet",
    "my":"Hilmy",
    "rk":"Reky",
    "rz":"Rizki",
    "ya":"Yahya",
}

for value in nama_nama.values():
    if "i" in value:
        print(f"Nama yang mengandung huruf 'i' adlaah {value}")

# lebih rapi
hasil = [nama for nama in nama_nama.values() if "i" in nama.lower()]
print(hasil)