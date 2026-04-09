### Latihan Lanjutan Fungsi (Bedah dari Awal)


# 1. Membuat Pembatas 
def pembatas_tiap_pesanan():
    print("="*20)
    print("Terima Kasih!")
    print("="*20)

pembatas_tiap_pesanan()
print("\n--- Jeda 5 menit ---\n")
pembatas_tiap_pesanan()


# 2. Menambahkan Parameter/Argumen
def cetak_struk(nama):
    print("="*20)
    print(f"Terima Kasih, {nama}!")
    print("Pesanan segera disiapkan.")
    print("="*20)

cetak_struk("Udin")
print("\n--- Jeda 5 menit ---\n")
cetak_struk("Rizky")


# 3. Menggunakan Return untuk Data yang Perlu Diolah
def hitung_kembalian(nama, total_belanja, uang_bayar):
    selisih = uang_bayar - total_belanja

    return nama, selisih

nama, kembalian = hitung_kembalian("Udin", 100000, 120000)

print(f"Kembalian Anda atas nama {nama}: {kembalian}")


# 4. Menggunakan Return dan Default Parameter
def hitung_tiket(nama, harga_dasar, status="reguler"):
    if status == "member":
        harga_dasar -= 10000
    
    return nama, harga_dasar, status

n_Hilmy, h_Hilmy, s_Hilmy = hitung_tiket("Hilmy", 45000, "member")
n_Rizky, h_Rizky, s_Rizky = hitung_tiket("Rizky", 70000)

print(f"Total belanja atas nama {n_Hilmy} dengan status {s_Hilmy}: Rp{h_Hilmy}")
print(f"Total belanja atas nama {n_Rizky} dengan status {s_Rizky}: Rp{h_Rizky}")


# 5. Menggunakan *Args 1
def cetak_struk(kasir, *pesanan):
    print(f"\nKasir yang melayani: {kasir}")
    print("\nDaftar Pesanan: ")

    for item in pesanan:
        print(item)

pesanan_1 = cetak_struk("Hilmy", "buah", "sayur", "daging", "susu")


# 6. Menggunakan *Args 2
def hitung_skor_lomba(nama_peserta, *skor_juri):
    
    total = 0
    for skor in skor_juri:
        total += skor

    return nama_peserta, total

p_reki, s_reki = hitung_skor_lomba("Reki", 100, 90, 89, 100, 88, 96)
print(f"Peserta atas nama {p_reki} mendapatkan total skor: {s_reki}!")


# 6. Menggunakan **Kwargs
def buat_profil(nama, **data_diri):
    print(f"===== Profil {nama} =====")

    for label, isi in data_diri.items():
        print(f"{label}: {isi}")

buat_profil("Rizky", gender="pria", kota="Bandung", profesi="Mahasiswa" )