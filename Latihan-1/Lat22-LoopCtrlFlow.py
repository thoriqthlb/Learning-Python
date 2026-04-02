# 1. Latihan men-skip lantai di lift 

print(10*"=", "SKIPPING LIFT FLOOR", 10*"=" + "\n")

lantai = range(1,11)
for i in lantai:
    if i == 4:
        continue
    print(f"Lift sedang di lantai: {i}")
print(f"""\nKita sudah di puncak menara.
----------------------------\n""")

# 2. Tangkap maling

print(10*"=", "MENANGKAP JOKER", 10*"=" + "\n")

warga = ["Budi", "Siti", "Joker", "Thoriq", "Andi"]

for i in warga:
    print(f"Memeriksa {i}...")
    if i == "Joker":
        print("TANGKAP DIA!")
        break
print("""\nPencarian selesai.
------------------\n""")

# 3. Quality control

print(10*"=", "QC BOTOL DI PABRIK", 10*"=" + "\n")

botol = [10, 5, 20, 7, 30, 0, 40, 50]

for cek in botol:

    if cek == 0:
        print("\nSTOP! MESIN RUSAK.")
        break
    if cek % 2 == 1:
        continue
    print(f"Botol dengan nomor {cek} dicetak.")

print("""\nSelesai.
--------""")

# 4. Bilangan prima

print(10*"=", "Bilangan Prima 2-50", 10*"=" + "\n")

print("Daftar Bilangan Prima 2-50: ")

for angka in range(2,51):
  prima = True
   
  for pembagi in range(2,angka):
    if angka % pembagi == 0:
      prima = False
      break
  if prima == True: 
      print(f"Angka {angka} adalah bilangan prima.")

# 5. Tes loop list string

isi_tas = ["Baju", "Laptop", "Bom", "Buku"]
barang_terlarang = ["Bom", "Senjata", "Narkoba"]
status_aman = True

print("\nMulai memeriksa tas...\n")

for barang in isi_tas:
    print(f"Mengecek: {barang}")
    if barang in barang_terlarang:
        print("\n>>> STOP! ADA BARANG HARAM!")
        status_aman = False
        break

print(27 * "-")
if status_aman == True:
    print("KESIMPULAN: Tas Aman. Silakan masuk.")
else:
    print("KESIMPULAN: TANGKAP ORANG INI!")

# 6 Cek Bahan Alergi (Logika Flagging)

bahan_nasi_goreng = ["nasi", "telur", "kecap", "kacang", "bawang"]
alergi = "kacang"

# 1. Awalnya kita optimis resep ini aman
status_aman = True

# 2. Cek satu per satu
for bahan in bahan_nasi_goreng:
    
    # 3. Jika ketemu bahan yang bikin alergi...
    if bahan == alergi:
        
        # 4. Ubah status jadi TIDAK AMAN
        status_aman = False
        
        # 5. Tarik Rem Darurat agar loop langsung berhenti tanpa mengecek 'bawang'
        break

# Kesimpulan akhir
if status_aman == True:
    print("Aman dimakan!")
else:
    print("\nAWAS BAHAYA!\n")