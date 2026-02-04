list_makanan = ["Nasgor", "Kebab", "Bakso", "Martabak", "Sayur_Asem"]

print("=== DAFTAR MAKANAN ===")
for index,makanan in enumerate(list_makanan):
    print(f"No. {index+1} | {makanan}")

ganti = int(input("Mau ganti nomor berapa? (1-5): "))
makanan_2 = input("Ganti apa?: ").title()

list_makanan[ganti-1] = makanan_2
print(list_makanan)