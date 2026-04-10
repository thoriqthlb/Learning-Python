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


# 4. Sistem Bonus Reporter
def hitung_bonus(jumlah_berita):
    bonus = 0

    if jumlah_berita > 20:
        bonus = 100000 * (jumlah_berita - 10) 
    elif jumlah_berita > 10:
        bonus = 50000 * (jumlah_berita - 10)
    
    return bonus

print(5*'-', "SISTEM BONUS REPORTER", 5*'-')

# input
beritamu = int(input("Berapa jumlah berita bulan ini? (min. 10): "))

# hasil dari fungsi
bonus_didapat = hitung_bonus(beritamu)

if bonus_didapat > 0: # selalu pakai hasil dari fungsi bukan input, jadi kalo butuh perubahan yang diubah fungsi bukan program utamanya.
    print(f"\nSELAMAT! ANDA MENDAPATKAN BONUS Rp{bonus_didapat:,}!".replace(",","."))
else: print(f"\nANDA TIDAK MENDAPATKAN BONUS BULAN INI, TETAP SEMANGAT!")

print(42*"-")


# 5. RPG Battle Engine (Elemental Mastery)
def damage_monster(base_power, hero_el, monster_el):
    '''Logika damage yang diberikan hero ke monster'''

    damage = 0

    # api
    if hero_el.lower() == "api" and monster_el.lower() == "daun":
        damage = base_power * 2
        status_menang = "SUPER EFFECTIVE!"
    
    elif hero_el.lower() == "api" and monster_el.lower() == "air":
        damage = base_power // 2
        status_menang = "RESISTED!"
    
    elif hero_el.lower() == "api" and monster_el.lower() == "api":
        damage = base_power
        status_menang = "NORMAL!"
    
    # daun
    elif hero_el.lower() == "daun" and monster_el.lower() == "air":
        damage = base_power * 2
        status_menang = "SUPER EFFECTIVE!"
    
    elif hero_el.lower() == "daun" and monster_el.lower() == "api":
        damage = base_power // 2
        status_menang = "RESISTED!"
    
    elif hero_el.lower() == "daun" and monster_el.lower() == "daun":
        damage = base_power
        status_menang = "NORMAL!"
    
    # air
    elif hero_el.lower() == "air" and monster_el.lower() == "api":
        damage = base_power * 2
        status_menang = "SUPER EFFECTIVE!"
    
    elif hero_el.lower() == "air" and monster_el.lower() == "daun":
        damage = base_power // 2
        status_menang = "RESISTED!"
    
    elif hero_el.lower() == "air" and monster_el.lower() == "air":
        damage = base_power
        status_menang = "NORMAL!"

    return {"skor":damage, "status":status_menang}

skor_hero = int(input("Masukkan skor kekuatan hero: "))
elemen_hero = input("Masukkan elemen kekuatan hero: ")
elemen_monster = input("Masukkan elemen kekuatan monster: ")

print(5*'-', "BATLE ARENA", 5*'-')

print(f"\nPower Hero: {skor_hero}")
print(f"Elemen Hero: {elemen_hero}")
print(f"Elemen Monster: {elemen_monster}")

hasil = damage_monster(skor_hero, elemen_hero, elemen_monster)

print(f">> BATTLE LOG: {hasil['status']}")
print(f">> MONSTER MENERIMA {hasil['skor']} DAMAGE!!!\n")

print(42*"-")


# 6. Mesin Auto-Triage Keluhan
def buat_tiket(nama_pelapor, teks_keluhan):
    id_tiket = f"TKT-{nama_pelapor.upper()}-{len(teks_keluhan)}"

    keluhan_lower = teks_keluhan.lower()

    if "mati" in keluhan_lower or "bocor" in keluhan_lower or "meledak" in keluhan_lower:
        prioritas = "KRITIS"
        target = "1 jam"
    
    elif "lupa" in keluhan_lower or "lambat" in keluhan_lower or "error" in keluhan_lower:
        prioritas = "SEDANG"
        target = "24 jam"

    else: 
        prioritas = "RENDAH"
        target = "3 hari"

    return {"tiket":id_tiket, "urgen":prioritas, "target_selesai":target}

print(5*'-', "TIKET ADUAN", 5*'-')

nama = input("Masukkan nama: ")
keluhan = input("Masukkan keluhannya: ")

print("\n>> TIKET BERHASIL DIBUAT <<")

hasil = buat_tiket(nama, keluhan)

print(f"\nID TIKET: {hasil['tiket']}")
print(f"Prioritas: {hasil['urgen']}")
print(f"Target: {hasil['target_selesai']}\n")

print(42*"-")