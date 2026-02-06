# Latihan Admin Panel Asset Tracker

print("=== Admin Panel Asset Tracker ===\n")

pin = 2026
akses = False
daftar_barang = []
daftar_harga = []

for i in range(3):
    masuk_pin = int(input("Masukkan PIN: "))
    if masuk_pin == pin:
        akses = True
        print("ACCESS GRANTED!")
        break
else: print("ACCESS DENIED.")

if akses == True:
    while True:
        print("""\n===== ASSET MANAGER MENU =====
1. Tambah Aset
2. Lihat Daftar
3. Hapus Aset
4. Laporan Statistik
5. Keluar\n""")
        
        pilih = int(input("Pilih menu nomor berapa?: "))
        total = sum(daftar_harga)
        panjang = len(daftar_barang)
        
        if pilih == 1:
            barang = input("Masukkan nama barang: ")
            harga = int(input("Masukkan harga barang: "))
            daftar_barang.append(barang)
            daftar_harga.append(harga)
            print("BERHASIL DITAMBAHKAN!")
        
        elif pilih == 2:
            print("\n--- DAFTAR ASET ---")
            for index,barang in enumerate(daftar_barang):
                harga = daftar_harga[index]
                print(f"{index+1}. {barang} | Rp{harga:,}".replace(",","."))
        
        elif pilih == 3:
            berapa = int(input(f"Menu nomor berapa yang ingin dihapus? (1-{panjang}): "))
            if berapa < 1 or berapa > len(daftar_barang):
                print("ERROR. INPUT SALAH!")
                continue
                
            else: 
                daftar_barang.pop(berapa-1)
                daftar_harga.pop(berapa-1)
                print("BERHASIL DIHAPUS!")
        
        elif pilih == 4:
            print("--- LAPORAN STATISTIK ---")
            if len(daftar_barang) <= 0:
                print("Data tidak ada.")
            else: 
                print(f"Total Barang: {panjang} unit.")
                print(f"Total Nilai Aset: Rp{total:,}")
                print(f"Rata-rata Nilai Aset: Rp{total/panjang:,}")
        
        elif pilih == 5:
            print("Terima kasih, selamat kembali bertugas!")
            break
        else: 
            print("ERROR. INPUT SALAH!")
            continue