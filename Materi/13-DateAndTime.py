# Import dari library python

import datetime as dt

# Nyari hari dan tanggal
print(5*"=","MENCARI HARI DAN TANGGAL",5*"=")
print("Silakan masukkan tanggal lahir Anda: ")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal) # emang udah formatnya begitu (y/m/d)
print("\n"f"""Tanggal lahir Anda\t: {tanggal_lahir}
Pada hari\t\t: {tanggal_lahir:%A}""")

# Hari ini
hari_ini = dt.date.today()

# Nyari umur
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print("\n"f"Hari ini tanggal\t: {hari_ini}")
print(f"Umur Anda adalah\t: {umur_tahun} tahun {umur_bulan_sisa} bulan")


# hari_ini = dt.date.today()

# print(hari_ini)
# print(f"Hari ini adalah hari = {hari_ini:%A}")

# tanggal = dt.date(2055,12,29)
# print(tanggal)
# print(f"Hari ini adalah hari = {tanggal:%A}")