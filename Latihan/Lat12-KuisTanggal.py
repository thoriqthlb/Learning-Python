import datetime as dt

print("\n" + 10*"=", "KUIS TEBAK TANGGAL", 10*"=" + "\n")

# Logika penanggalan
today = dt.date.today()
tdelta = dt.timedelta(days = 100)
kunci = today + tdelta

# Soal
print(f"""SOAL:
Hari ini tanggal {today} 
100 hari lagi tanggal berapa?\n""")
print("--- MASUKKAN JAWABANMU ---\n")
tanggal = int(input("Tanggal: "))
bulan = int(input("Bulan: "))
tahun = int(input("Tahun: "))

print(27*"-"+"\n")

# Check kesamaan
hasil = dt.date(tahun, bulan, tanggal)
benar = hasil == kunci

# Status jawaban

print(f"""KOREKSI JAWABAN:
Kunci jawaban: {kunci}
Jawaban Anda: {hasil}
Hasilnya: {benar}""")
print(27*"-")