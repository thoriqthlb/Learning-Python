'''Keyword Args (**kwargs)'''

def fungsi(nama,tinggi,berat):
    '''Fungsi Biasa'''
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Udin",180,75)

def fungsi(**kwargs):
    '''Fungsi Kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")
    
fungsi(nama="Udin",tinggi=180,berat=75)

# Studi Kasus

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak Ada Operasi")
    return output

hasil = math(1,2,3,4,option="tambah")
print(f"hasil tambah = {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"hasil kali = {hasil}")