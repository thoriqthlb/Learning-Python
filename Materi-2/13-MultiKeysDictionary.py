import datetime as dt
import os

mahasiswa_1 = {
    "nama":"Rizki",
    "nim":"1492752",
    "sks_lulus":130,
    "beasiswa":False,
    "lahir":dt.datetime(2006,11,10)
}

mahasiswa_2 = {
    "nama":"Hilmy",
    "nim":"1492753",
    "sks_lulus":140,
    "beasiswa":True,
    "lahir":dt.datetime(2004,8,26)
}

mahasiswa_3 = {
    "nama":"Yahya",
    "nim":"1492754",
    "sks_lulus":100,
    "beasiswa":False,
    "lahir":dt.datetime(2000,5,7)
}

data_mahasiswa = {
    "MAH001":mahasiswa_1,
    "MAH002":mahasiswa_2,
    "MAH003":mahasiswa_3
}
os.system("cls")
print(f"{'KEY':<6}| {'NAMA':<17}| {'NIM':<10}| {'SKS':<4}| {'BEASISWA':<10}| {'TTL':<10}")
print(60*"-")

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    TTL = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY:<6}| {NAMA:<17}| {NIM:<10}| {SKS:<4}| {BEASISWA:<10}| {TTL:<10}")\


###### pythonic way ######

# for KEY, data in data_mahasiswa.items():
#     print(f"{KEY:<6}| {data['nama']:<17}| {data['nim']:<10}| {data['sks_lulus']:<4}| {str(data['beasiswa']):<10}| {data['lahir'].strftime('%d/%m/%Y')}")