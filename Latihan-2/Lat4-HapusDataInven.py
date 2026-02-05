gudang = ["TV", "Kulkas", "Mesin Cuci", "Setrika", "Blender"]

print("=== DAFTAR BARANG DI GUDANG ===\n")
for index,barang in enumerate(gudang):
    print(f"{index+1}. {barang}")

while True:
    ukuran = len(gudang)
    hapus = int(input(f"\nMau hapus nomor berapa? (1-{ukuran}): "))
    if hapus < 1 or hapus > ukuran:
        print("ERROR. MASUKKAN ANGKA YANG SESUAI!")
        continue

    dihapus = gudang.pop(hapus-1)
    break

print(f"""\n======== BERHASIL ======== 
Barang ({dihapus}) sudah dibuang.

Sisa barang di gudang:
{gudang}""")