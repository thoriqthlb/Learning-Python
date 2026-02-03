print(10*"=", "ATM MACHINE SIMULATION", 10*"=" + "\n")

pin = 1234
saldo = 0
akses = False

for i in range(3):
    masuk_pin = int(input("Masukkan PIN-nya: "))
    if masuk_pin == pin:
        akses = True
        print("\nPIN benar.")
        break
else: print("KARTU TERBLOKIR")

if akses == True:
    while True:
        print("""
        MENU:
        1. Cek Saldo
        2. Setor Tunai
        3. Tarik Tunai
        4. Keluar
        """)
        
        pilih = int(input("Pilih nomor berapa?: "))
        if pilih == 1:
            print(f"Saldo Anda: Rp{saldo:,}".replace(",", "."))
            
        elif pilih == 2:
            setor = int(input("Ingin setor berapa?: "))
            saldo += setor
            print("Setor berhasil!")
            
        elif pilih == 3:
            tarik = int(input("Ingin tarik berapa?: "))
            
            if tarik < 0:
                print("Error: Tidak bisa tarik minus.")
            elif tarik > saldo:
                print("Saldo tidak cukup!")
            else:
                saldo -= tarik
                print("Tarik tunai berhasil.")
                
        elif pilih == 4:
            print("Terima kasih, kartu keluar.")
            break # Hentikan Loop Menu
            
        else:
            print("Menu tidak tersedia, coba lagi.")
            # Otomatis loop balik ke atas karena 'while True'

print("Program selesai.")