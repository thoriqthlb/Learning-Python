# 1. Menyambung string

nama_pertama = "ucup"
nama_tengah = "awal"
nama_akhir = "udin"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string

panjang = len(nama_lengkap)
print(panjang)

# 3. Operator untuk string
# mengecek apakah ada komponen "char" atau "string" di string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)

# indexing
print("index ke-0: " + nama_lengkap[0])
print("index ke-[0-3]: " + nama_lengkap[0:4])
print("index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:12:2])

# item paling kecil
print("Paling kecil: " + min(nama_lengkap))

# item paling besar
print("Paling besar: " + max(nama_lengkap))

# ascii code
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "udin awaludin"
jumlah = data.count("i")
print("Jumlah 'i' = " + str(jumlah))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek semuanya huruf dan angka
# isdecimal() <-- untuk mengecek semuanya angka
#isspace() <-- spasi, tab, newline
#istitle() <-- semua kata dimulai dengan kapital

judul = "Udin Ganteng Banget"
cek_judul = judul.istitle() # hasil bool
print(judul + " apakah ia is title?: " + str(cek_judul))

# ngecek komponen startswith() endswith()
cek_start = "Udin Awaludin".startswith("Udin")
print("start = " + str(cek_start))

cek_end = "Udin Awaludin".endswith("Awaludin")
print("end = " + str(cek_end))