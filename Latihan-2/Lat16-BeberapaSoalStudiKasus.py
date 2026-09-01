### Studi Kasus 1: 
'''Program Diskon Toko Buku'''

def hitung_total_bayar(total_belanja):
    if total_belanja > 100000:
        diskon = total_belanja * 0.1  # Diskon 10%
    else: 
        diskon = 0  # Tidak ada diskon
    total_bayar = total_belanja - diskon
    return total_bayar

pelanggan_a = hitung_total_bayar(150000)
pelanggan_b = hitung_total_bayar(80000)

print("Total bayar pelanggan A: Rp", pelanggan_a)
print("Total bayar pelanggan B: Rp", pelanggan_b)

### Studi Kasus 2: 
'''Scan Otomatis Transaksi Gagal'''
print("=== Memulai Scan Laporan Transaksi ===")

# 1. Buka file eksternal log transaksi sebagai variabel 'laporan'
with open("Latihan-2/log_transaksi.txt", mode="r") as laporan:
    
    # 2. Kita baca baris demi baris dari atas sampai bawah
    for baris in laporan:
        
        # 3. Jika di dalam baris tersebut ada kata "ERROR"
        if "ERROR" in baris:
            # 4. Ambil dan print baris yang bermasalah tersebut
            print(f"PERINGATAN: Temukan masalah! -> {baris.strip()}") # .strip() dipake biar hasil print-nya rapi

print("=== Scan Selesai ===")