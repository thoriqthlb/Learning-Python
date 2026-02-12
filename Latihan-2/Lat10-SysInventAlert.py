# Latihan Sistem Manajemen Inventaris Perangkat IT

inventaris_it = [
    {"id":1,
     "nama":"Laptop Asus",
     "kategori":"Laptop",
     "stok":10,
     "harga":7000000
    },

    {"id":2,
     "nama":"Mouse Logitech",
     "kategori":"Aksesoris",
     "stok":3,
     "harga":150000
    },

    {"id":3,
     "nama":"Monitor Dell",
     "kategori":"Monitor",
     "stok":12,
     "harga":2000000
    }
]

while True:
    print("""=== MENU INVENTARIS IT ===
1. Tambah Aset Baru
2. Lihat Daftar Inventaris & Laporan
3. Update Stok Aset
4. Hapus Aset
5. Keluar
""")
    
    pilih = input("Pilih Menu: ")

    if pilih == "1":
        aset = input("Nama aset: ").title()
        jenis = input("Kategori: ").title()
        stok = int(input("Jumlah barang: "))
        harga = int(input("Harga satuan: "))

        # Urutan nomor id
        id_baru = inventaris_it[-1]["id"] + 1 if inventaris_it else 1

        # dict yang mau ditambahin
        inven_baru = {
            "id":id_baru,
            "nama":aset,
            "kategori":jenis,
            "stok":stok,
            "harga":harga
        }

        # Validasi + tambahkan
        inventaris_it.append(inven_baru)
        print("Berhasil ditambahkan!")

    elif pilih == "2":
        print(75*"=")
        print(f"{'ID':<6}| {'NAMA':<15}| {'KATEGORI':<15}| {'STOK':<7}| {'HARGA':<11}| {'TOTAL':<11}")
        print(75*"-")
        
        total_seluruh = 0 # buat variabel kosong di luar loop sebagai flag penjumlah
        for inven in inventaris_it:
            peringatan = ""
            if inven["stok"] < 5:
                peringatan = "LOW STOCK!!!"
            total_per_item = inven['stok'] * inven['harga']
            total_seluruh += total_per_item
            print(f"{inven['id']:<6}| {inven['nama']:<15}| {inven['kategori']:<15}| {inven['stok']:<7}| {inven['harga']:<11}| {total_per_item:<11} {peringatan}")
        
        print(75*"-")
        print(f">>> TOTAL NILAI SELURUH ASET: Rp{total_seluruh:,}".replace(",","."))
        print(75*"=")
    
    elif pilih == "3":
        ubah = int(input("Masukkan id yang ingin diubah: "))
        ketemu = False
        
        for inven in inventaris_it:
            if ubah == inven["id"]:
                ketemu = True
                print("1. Tambah \n2. Kurang")
                ubah_apa = input("Pilih 1/2?: ")
                
                if ubah_apa == "1":
                    tambah_brp = int(input("Berapa: "))
                    if tambah_brp <= 0:
                        print("INVALID!!!")
                        continue
                    inven["stok"] += tambah_brp
                    print("Berhasil diubah!")
                
                elif ubah_apa == "2":
                    kurang_brp = int(input("Berapa: "))
                    if kurang_brp > inven["stok"]:
                        print("INVALID!!!")
                        continue
                    inven["stok"] -= kurang_brp
                    print("Berhasil diubah!")
                
                else: print("ERROR. INPUT INVALID!!!")
                break
        
        if not ketemu:
            print("Data tidak ada.")
    
    elif pilih == "4":
        hapus = int(input("Masukkan id aset yang ingin dihapus: "))
        ketemu = False

        for i,inven in enumerate(inventaris_it):
            if inven["id"] == hapus:
                ketemu = True
                yakin = input(f"Yakin hapus inven {inven['nama']}? (y/n): ")
                if yakin.lower() == 'y':
                    inventaris_it.pop(i)
                    print("Inven dihapus!")
                else:
                    print("Hapus dibatalkan.")
                break
    elif pilih == "5":
        print("Sampai jumpa!")
        break

    else: 
        print("ERROR. INPUT INVALID!!!")