print(10*"=", "KASIR WARUNG BAKSO", 10*"=" + "\n")

keranjang = []
total_bayar = 0

while True:
    nama = input("Nama barang: ")
    keranjang.append(nama)
    harga = int(input("Masukkan harga: "))
    total_bayar += harga
    tanya = input("ada lagi? (y/n): ")
    if tanya == "n":
        break

print("Barang yang dibeli:")
for nama in keranjang:
    print(nama)
print(f"Jadi totalnya adalah: Rp{total_bayar}".replace(",","."))