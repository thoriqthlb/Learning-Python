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