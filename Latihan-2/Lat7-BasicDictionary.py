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
        print(f"Nama yang mengandung huruf 'i' adalah {value}")

# lebih rapi
hasil = [nama for nama in nama_nama.values() if "i" in nama.lower()]
print(hasil)


# Latihan Dictionary Lagi
skor = {"Andi": 120, "Budi": 145, "Cici": 130}

# 1. Jadikan Andi sebagai patokan Juara Sementara
nama_juara = "Andi"
nilai_juara = skor["Andi"]  # Ini nilainya 120

# 2. Cek satu per satu nama di dalam buku catatan
for nama in skor:
    
    # 3. Ambil angka milik si 'nama' yang sedang dicek saat ini
    nilai_sekarang = skor[nama]
    
    # 4. Jika nilai orang ini LEBIH BESAR dari nilai_juara saat ini...
    if nilai_sekarang > nilai_juara:
        
        # 5. Ganti nama_juara dan nilai_juara dengan yang baru!
        nama_juara = nama
        nilai_juara = nilai_sekarang

print("Lompatan tertinggi dilakukan oleh:", nama_juara)


# Lanjutan Latihan Dictionary
pelamar = {"Dina": 80, "Eko": 70, "Fina": 90, "Gani": 65}

# 1. Siapkan daftar kosong untuk menampung nama yang lulus
daftar_lulus = []

# 2. Cek satu per satu pelamar
for nama in pelamar:
    
    # 3. Ambil nilainya
    nilai = pelamar[nama]
    
    # 4. Jika nilainya LEBIH BESAR dari 75...
    if nilai > 75:
        
        # 5. Masukkan 'nama' tersebut ke dalam list daftar_lulus
        daftar_lulus.append(nama)

print("Pelamar yang lolos:", daftar_lulus)


# Mengubah Isi List Menjadi Dict
suara = ["Budi", "Siti", "Budi", "Andi", "Siti", "Budi"]

# 1. Siapkan papan tulis kosong (Dictionary)
rekap = {}

# 2. Buka gulungan kertas satu per satu
for nama in suara:
    
    # 3. Cek papan tulis: Apakah nama ini SUDAH ADA di dalam dictionary rekap?
    if nama in rekap:
        
        # 4. Jika SUDAH ADA, tambahkan angka milik nama tersebut dengan 1
        rekap[nama] += 1
        
    else:
        
        # 5. Jika BELUM ADA, buat nama tersebut di papan dan beri nilai perdana 1
        rekap[nama] = 1

print("Hasil rekapitulasi:", rekap)