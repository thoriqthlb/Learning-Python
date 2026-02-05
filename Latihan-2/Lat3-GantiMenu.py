list_makanan = ["Nasgor", "Kebab", "Bakso", "Martabak", "Sayur_Asem"]

print("=== DAFTAR MAKANAN ===")
for index,makanan in enumerate(list_makanan):
    print(f"No. {index+1} | {makanan}")

while True:
    jumlah_menu = len(list_makanan) # kalo diedit ga perlu nambah 1-1
    ganti = int(input(f"Mau ganti nomor berapa?: (1-{jumlah_menu})"))
    if ganti < 1 or ganti > jumlah_menu:
        print("ERROR. PILIH ANGKA YANG SESUAI!")
        continue # biar balik lagi
    makanan_2 = input("Ganti apa?: ").title()

    list_makanan[ganti-1] = makanan_2
    print(list_makanan)
    break