# __main__ adalah top level code environment

# __name__ == "__main__" akan terjadi jika ada di program utama

## __name__ pada file program utama:
print(f"nilai __name__ pada main.py = '{__name__}'")

## __name__ pada file program eksternal:
# import 1-tkinter: bakal dinamain sesuai filenya

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int, b:int) -> int:
    return a + b

# fungsi utama
if __name__ == "__main__":
    angka1 = 4
    angka2 = 5
    hasil = fungsi_tambah(angka1, angka2)
    print(f"hasil tambah = {hasil}")