import datetime as dt

print("\n"+5*"=","EXPIRED CHECKER APP",5*"="+"\n")

produk = input("Masukkan nama produknya\t\t: ").capitalize()
tanggal = int(input("Masukkan tanggal produksi\t: "))
bulan = int(input("Masukkan bulan produksi\t\t: "))
tahun = int(input("Masukkan tahun produksi\t\t: "))
simpan = int(input("Masukkan masa simpan (hari)\t: "))

print(35*"-"+"\n")

# date
tanggal_prod = dt.date(tahun,bulan,tanggal)
today = dt.date.today()
basi = tanggal_prod + dt.timedelta(days=simpan)

# Output
print(f"""Nama produk\t\t: {produk}
Tanggal produksi\t: {tanggal_prod:%A, %d, %B, %Y}
Masa simpan\t\t: {simpan} hari
Tanggal kedaluarsa\t: {basi}""")

print(35*"-"+"\n")

print(f"STATUS KEDALUARSA: {today > basi}")