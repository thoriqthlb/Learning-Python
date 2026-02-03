# Latihan membuat tes kelayakan pengunjung untuk naik roller coaster

print(12*"=", "LOKET ROLLER COASTER", 12*"=" + "\n")

# LOGIKA INTI
tinggi = float(input("Masukkan tinggi badan (cm): "))

if tinggi >= 120:
    print("Selamat Anda boleh masuk!\n")
    umur = int(input("Masukkan umur Anda: "))
    if umur < 10: 
        harga = 30000
    elif 10 <= umur <= 17: 
        harga = 40000
    elif umur > 17:
        harga = 50000
    foto = input("Mau cetak foto? (y/n): ").lower()
    if foto == "y":
        hargaf = 10000
    else: 
        hargaf = 0
    
    # LANJUTAN LOGIKA HARUS DI DALAM TERNYATA
    total = harga + hargaf
    print(25*"-"+ "\n")

    print(F"""DETAIL PEMBAYARAN: 
    Harga Tiket : Rp{harga:,}
    Foto        : Rp{hargaf:,}

    TOTAL: {total:,}
    {25*"-"}""")    
else: print("Maaf Anda tidak diperkenankan masuk.")
print(36*"="+ "\n")