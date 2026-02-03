print(10*"=", "AUTOMATIC PARKING SYSTEM", 10*"=" + "\n")

total = 0

while True:
    print("\n---- MENU KASIR ----")
    kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ").lower()
    
    if kendaraan == "motor" or kendaraan == "mobil":
        durasi = int(input("Berapa lama? (dalam jam): "))
    
        if durasi <= 0:
            continue
      
        if kendaraan == "motor":
            tarif = 3000 * durasi

        elif kendaraan == "mobil":
            tarif = 5000 * durasi 

        if durasi > 24:
            print(">> KENDARAAN MENGINAP (+Rp 50.000)")
            tarif += 50000  

        print(f"""---------------------
Struk: {kendaraan.capitalize()} | {durasi} jam
Biaya: Rp{tarif:,}
---------------------""".replace(",","."))

        total += tarif

    elif kendaraan == "admin007":
        print(f"""Sistem Dimatikan.

    ========== LAPORAN PENDAPATAN ==========
              
Total Uang Masuk: Rp{total:,}""".replace(",","."))
        break
    
    else: print("ERROR! kendaraan tidak dikenali.")
    continue


##### ACUAN DI BAWAH

# print(10*"=", "SISTEM PARKIR MALL", 10*"=" + "\n")

# total_pendapatan = 0

# while True:
#     print("\n--- MENU KASIR ---") # Biar ada jeda antar pelanggan
#     kendaraan = input("Jenis kendaraan (motor/mobil): ").lower() 
#     # .lower() -> Biar kalau user ngetik "MoToR" tetap terbaca "motor"

#     # --- 1. CEK ADMIN (EXIT STRATEGY) ---
#     if kendaraan == "admin007":
#         print("\nSISTEM DIMATIKAN.")
#         print(10*"=")
#         # Format string dipisah biar rapi
#         formatted_total = f"Rp {total_pendapatan:,}".replace(",", ".")
#         print(f"TOTAL PENDAPATAN HARI INI: {formatted_total}")
#         print(10*"=")
#         break # Keluar loop

#     # --- 2. VALIDASI JENIS KENDARAAN ---
#     # Kalau bukan motor DAN bukan mobil, langsung skip ke atas
#     if kendaraan != "motor" and kendaraan != "mobil":
#         print("ERROR: Kendaraan tidak dikenali!")
#         continue 

#     # --- 3. INPUT JAM ---
#     durasi = int(input("Lama parkir (jam): "))

#     # --- 4. VALIDASI JAM ---
#     if durasi <= 0:
#         print("ERROR: Jam tidak valid!")
#         continue

#     # --- 5. HITUNG TARIF DASAR ---
#     # Variabel 'tagihan' ini adalah "Kertas Nota" sementara
#     tagihan = 0 
    
#     if kendaraan == "motor":
#         tagihan = durasi * 3000
#     elif kendaraan == "mobil":
#         tagihan = durasi * 5000

#     # --- 6. CEK DENDA MENGINAP ---
#     if durasi > 24:
#         print(">> KENDARAAN MENGINAP (+Rp 50.000)")
#         tagihan += 50000

#     # --- 7. CETAK STRUK ---
#     formatted_tagihan = f"Rp {tagihan:,}".replace(",", ".")
    
#     print("-" * 30)
#     print(f"STRUK: {kendaraan.capitalize()} | {durasi} Jam")
#     print(f"TOTAL: {formatted_tagihan}")
#     print("-" * 30)

#     # --- 8. MASUK BRANKAS ---
#     total_pendapatan += tagihan