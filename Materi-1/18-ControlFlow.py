# Pass, Continue, Break

# 1. Pass => dummy (tidak akan dieksekusi)

angka = 0

while angka < 5:

    if angka == 3:
        pass    # tidak akan dieksekusi 
                #(fungsinya untuk menghindari error pada blok kode yang wajib diisi)
    print(angka)
    angka += 1

# 2. Continue => skip (men-skip aksi di bawahnya sehingga balik ke awal loop)

angka = 0

while angka < 5:
    print(f"Angka sekarang => {angka}")
    angka += 1

    if angka == 3:
        print("Nice!")
        continue    # akan skip aksi di bawahnya dan kembali ke atas

    print("Wassup!")

print("Selesai.")

# 3. Break => mengakhiri (memutus infinite loop atau mencari sesuatu)

angka = 0

while angka < 5:
    angka += 1
    print(f"Angka sekarang => {angka}")

    if angka == 3:
        print("Nice!")
        break

    print("Wassup!")

print("Selesai.")

angka = 0
hitung = int(input("Mau hitung sampe berapa?: "))

while True:
    angka += 1
    print(angka)

    if angka == hitung:
        print("Oke!")
        # break
print("Selesai.")