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

print(f"Total yang harus dibayarkan: Rp{total_penggunaan:,}".replace(",","."))
print(30*"-")


# 2. Kalkulator Ongkos Kirim
def hitung_ongkir(jarak, layanan):
    tarif = jarak * 2500
    
    if layanan.lower() == "express":
        tarif += 15000
    else: 0

    return tarif

print(5*'-', "Express Delivery", 5*'-')

jarak_pengiriman = int(input("\nBerapa jarak tempuh pengiriman? (km): "))
jenis_layanan = input("Pilih jenis layanan Express/Reguler: ")

total_biaya = hitung_ongkir(jarak_pengiriman, jenis_layanan)

print(f"\n> Total biaya ongkir Anda adalah: Rp{total_biaya:,}".replace(",","."))
print(30*"-")