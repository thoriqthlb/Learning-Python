# Profil Server
server_it = {
    "nama":"iNews-Server-01",
    "ip":"192.168.10.1",
    "ram":16,
    "status":"Aktif"
}

# Status sekarang
print(f"Server {server_it['nama']} dengan IP {server_it['ip']} saat ini sedang {server_it['status']}\n")

# Upgrade RAM
server_it["ram"] = 32

# Tambah Item
server_it["lokasi"] = "Lantai 3"

# Profil diperbarui
for k,v in server_it.items():
    print(f"kode = {k} \t| isi = {v}")


# Latihan Tuple
koordinat_kumpul = (-6.200000, 106.816666)  # (Lintang, Bujur)

# 1. Ambil garis Lintang (angka pertama) dari Tuple di atas
lintang = koordinat_kumpul[0]

# 2. Ambil garis Bujur (angka kedua)
bujur = koordinat_kumpul[1]

print("Titik kumpul berada di garis lintang:", lintang)


# Latihan Set
# Tumpukan data mentah dari survei (List)
jawaban_survei = ["Membaca", "Berenang", "Membaca", "Lari", "Berenang", "Membaca"]

# 1. Sulap list 'jawaban_survei' di atas menjadi Set agar duplikatnya terbuang!
hobi_unik = set(jawaban_survei)

# 2. Hitung ada BERAPA BANYAK macam hobi di dalam 'hobi_unik' sekarang
jumlah_hobi = len(hobi_unik)

print("Hobi unik yang ditemukan:", hobi_unik)
print("Total macam hobi:", jumlah_hobi)