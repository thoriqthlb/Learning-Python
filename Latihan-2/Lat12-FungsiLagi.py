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


# 3. Menggunakan Return Untuk Data Yang Perlu Diolah
def hitung_kembalian(total_belanja, uang_bayar):
    selisih = uang_bayar - total_belanja

    return selisih

kembalian_budi = hitung_kembalian(100000, 120000)

print(f"Kembalian Anda: {kembalian_budi}")