import datetime as dt

print("\n"+5*"=","APLIKASI HITUNG MUNDUR LIBURAN",5*"="+"\n")

tujuan = input("Masukkan destinasi tujuan liburan Anda: ").upper()
tanggal = int(input("Masukkan tanggal berangkat\t: "))
bulan = int(input("Masukkan bulan berangkat\t: "))
tahun = int(input("Masukkan tahun berangkat\t: "))

print(35*"-"+"\n")

berangkat = dt.date(tahun,bulan,tanggal)
hari_ini = dt.date.today()
tunggu = berangkat - hari_ini
# tunggu_tahun = tunggu.days // 365

print(f"""Halo!
Kita sudah catat bahwa Anda akan pergi ke: {tujuan}
Pada tanggal: {berangkat:%A, %d %B %Y}

SISA WAKTU MENUNGGU: {tunggu.days} HARI""")
print(35*"-"+"\n")