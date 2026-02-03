print(10*"=","KALKULATOR UPAH LEMBUR",10*"=")

nama = input("Nama Anda: ").title()
jam = float(input("Total jam kerja: "))

lembur = jam > 8
upah = (jam - 8) * lembur
jatah = upah * 15000
jatah_int = int(jatah)

print(f"\nAtas nama: {nama}")
print(f"Status lembur: {lembur}")
print(f"Upah lembur Anda: Rp{jatah:,}")