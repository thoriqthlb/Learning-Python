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




############### MATERI LENGKAP DI BAWAH ###############


### NULIS PENANGGALAN
d = dt.date(2026, 12, 12)
print(d) #bisa tanggalnya doang/lainnya pake .date dll

# nulis today
tday = dt.date.today() #tambah .today()
print(tday) #kalo mau salah satunya doang bisa ditambahin .year/day, dll

tdelta = dt.timedelta(days = 7)
print(tday - tdelta)

# nyari birthday
bday = dt.date(2026, 3, 4)
till_bday = bday - tday
print(bday)
print(till_bday.days,"Hari") #tambahin .days dll buat khususin yang mau ditampilin


### NULIS WAKTU
t = dt.time(16, 3, 49)
print(t) #bisa jamnya doang/lainnya pake .hours dll

### BISA DUA-DUANYA
dt = dt.datetime(2026, 1, 1, 9, 57, 38, 900000)
print(dt) #bisa ditambahin untuk keduanya, misal .date() atau .time()


# :%A (Hari)
# :%d (Tanggal)
# :%B (Bulan)
# :%Y (Tahun)