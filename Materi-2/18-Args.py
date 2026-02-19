# *args

def fungsi(nama,tinggi,berat):
    print(f"{nama} tingginya {tinggi} dan beratnya {berat}")

fungsi("Thoriq",180,80)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} tingginya {tinggi} dan beratnya {berat}")

fungsi(["Udin",175,78])

# pakai *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} tingginya {tinggi} dan beratnya {berat}")

fungsi("Ucup",170,60)

# Studi Kasus

def tambah(*data):
    # data tipenya adalah tuple dan bisa diiterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil = {hasil}")

hasil = tambah(15,10,5)
print(f"Hasil = {hasil}")