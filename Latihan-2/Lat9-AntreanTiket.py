# List berisi dictionary (detail informasi)
antrean_tiket = [
    {"no": 101, 
    "user": "Andi", 
    "kendala": "Lupa Password",
    "status": "Open"},
    
    {"no": 102, 
     "user": "Budi", 
     "kendala": "Layar Blank",
     "status": "Open"}
]

while True:
    print(f"""\n=== MENU IT SUPPORT ===
1. Tambah Tiket Baru
2. Lihat Semua Tiket
3. Ubah Status tiket          
4. Keluar                   
""")
    
    pilihan = (input("Pilih menu (1-4): "))

    if pilihan == "1":
        # Tambahan dari input user 
        print("\n=== INPUT TIKET BARU ===")
        nama = input("Masukkan nama: ").title()
        kendala = input("Sebutkan kendalanya: ").title()
        status = input("Status saat ini (tiket baru ketik 'open'): ").title()

        # Membuat urutan nomor selanjutnya dari nomor paling terakhir
        nomor_terakhir = antrean_tiket[-1]["no"]
        nomor_baru = nomor_terakhir + 1

        # Buat dictionary baru untuk dimasukin ke list (sebagai inputan user)
        tiket_baru = {
            "no": nomor_baru, 
            "user": nama, 
            "kendala": kendala,
            "status": status
        }

        # Tambah dictionary yang baru dibuat ke list
        antrean_tiket.append(tiket_baru)
        print("Tiket berhasil didaftarkan!")

    elif pilihan == "2":
        # Cetak hasil akhir
        print("\n=== DAFTAR ANTREAN SAAT INI ===")
        for tiket in antrean_tiket:
            print(f"No: {tiket.get('no')} \t| Nama: {tiket.get('user')} \t| Kendala: {tiket.get('kendala')} \t| Status: {tiket.get('status')}")

    elif pilihan == "3":
        cek = int(input("Masukkan nomor tiket yang ingin dicek: "))
        ketemu = False

        for tiket in antrean_tiket:
            if tiket["no"] == cek:
                ketemu = True
                print("Status berhasil diubah!")
                tiket["status"] = "Selesai"
                break
        if not ketemu:
            print("Data tidak ditemukan.")
        

    elif pilihan == "4":
        print("Sistem dimatikan. Bye!")
        break

    else: 
        print("ERROR. INPUT INVALID!!!")



##### CATATAN #####

# antrean_tiket => Adalah List (Gunakan .append(), .pop(), atau index []).
# antrean_tiket[-1] => Adalah Dictionary (Gunakan .get() atau ["key"]).
# antrean_tiket[-1]["no"] => Adalah Isi/Value dari dictionary tersebut (dalam hal ini, Angka).