# Program List Buku

list_buku = []
while True:
    print("Masukkan Data Buku")
    judul = input("Judul Buku: ").title()
    penulis = input("Nama Penulis: ").title()

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    lanjut = input("Lanjut? (ketik 'n' jika ingin stop): ").lower()

    if lanjut == "n":
        break
print("\nPROGRAM SELESAI.")


# Copy
import copy

# Menu pusat punya paket combo
menu_pusat = [["Ayam", "Teh"], "Sate"] 

# Kita kloning total buat Cabang Bali
menu_cabang_bali = copy.deepcopy(menu_pusat)

# Cabang Bali ganti isi paket pertama: Ayam jadi Bebek
menu_cabang_bali[0][0] = "Bebek"

print("\n--- Skenario 3 ---")
print(f"Menu Pusat: {menu_pusat}") # TETAP AYAM (AMAN!)
print(f"Menu Bali: {menu_cabang_bali}") # JADI BEBEK
