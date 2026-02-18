'''Default Argumen'''

# def fungsi(argumen = nilai defaultnya):

# contoh 1
def say_hello(nama = "Kamu"):
    '''Fungsi dengan default argumen'''
    print(f"Hallo {nama}")

say_hello("udin")
say_hello()

# contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
    '''Fungsi satu input biasa, satu default'''
    print(f"Hai {nama}, {pesan}")

sapa_dia("Dudung", "HaLoo")
sapa_dia("Udin")

# contoh 3
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(3, 3))

hasil = hitung_pangkat(pangkat=2,angka=3)
print(hasil)