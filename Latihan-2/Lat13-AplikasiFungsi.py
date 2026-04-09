import os

os.system("cls")

# 1. Kalkulator Tagihan Listrik Sederhana
def hitung_bayar(kwh):
    '''Hitung total biaya penggunaan listrik'''
    bayar = kwh * 1500

    return bayar

print(5*"-", "Kalkulator Listrik", 5*"-")

input_user = int(input("Masukkan jumlah penggunaan listrik (kWh): "))
total_penggunaan = hitung_bayar(input_user)

print(f"Total yang harus dibayarkan: Rp{total_penggunaan:,}".replace(",", "."))
print(30*"-")