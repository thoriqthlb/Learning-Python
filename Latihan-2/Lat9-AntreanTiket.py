antrean_tiket = [
    {"no": 101, 
    "user": "Andi", 
    "kendala": "Lupa Password"},
    
    {"no": 102, 
     "user": "Budi", 
     "kendala": "Layar Blank"}
]

print("\n=== INPUT TIKET BARU ===")
nama = input("Masukkan nama: ").title()
kendala = input("Sebutkan kendalanya: ").title()

tiket_baru = {
    "no": 103, 
    "user": nama, 
    "kendala": kendala
}

antrean_tiket.append(tiket_baru)

print("\n=== DAFTAR ANTREAN SAAT INI ===")
for tiket in antrean_tiket:
    print(f"No: {tiket.get('no')} \t| Nama: {tiket.get('user')} \t| Kendala: {tiket.get('kendala')}")