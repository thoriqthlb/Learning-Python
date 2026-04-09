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


# 3. Sistem Tilang Elektronik
def hitung_denda(kecepatan_mobil, batas_jalan):
    selisih = kecepatan_mobil - batas_jalan
    denda = 0

    if selisih > 20:
        denda = 500000
    elif selisih > 0:
        denda = 250000
    return denda

max_kec = 100

print(5*'-', "Kamera ETLE", 5*'-')
print(f"Batas kecepatan jalan (km/jam): {max_kec}")

kecepatan_anda = int(input("Kecepatan Mobil Anda: "))

biaya_tilang = hitung_denda(kecepatan_anda, max_kec)

if biaya_tilang > 0:
    print(f"\n> STATUS: DITILANG! Denda Anda: Rp{biaya_tilang:,}".replace(",", "."))
else: print("\n> STATUS: Aman! Anda tidak kena tilang.")

print(42*"-")


