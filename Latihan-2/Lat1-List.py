# Program List Buku

list_buku = []
while True:
    print("Masukkan Data Buku")
    judul = input("Judul Buku: ").capitalize()
    penulis = input("Nama Penulis: ").capitalize()

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    lanjut = input("Lanjut? (y/n): ").lower()

    if lanjut == "n":
        break
print("\nPROGRAM SELESAI.")