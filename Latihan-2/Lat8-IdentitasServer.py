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