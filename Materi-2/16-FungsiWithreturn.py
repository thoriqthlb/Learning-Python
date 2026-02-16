'''fungsi dengan kembalian'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#       badan fungsi
#       return output

# Fungsi Kuadrat

def kuadrat(input_angka):
    '''Fungsi Kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat # KEMBALI ke PEMANGGIL

y = kuadrat(5) # PEMANGGIL
print(y)

print(kuadrat(6)) # Langsung tanpa tambahan variable

z = 10 + kuadrat(9) # Bisa Juga Ada Tambahan Operasi di Luar Fungsi
print(z)

# Fungsi Tambah

def fungsi_tambah(angka_1,angka_2):
    '''Penjumlahan'''
    return angka_1 + angka_2 # TANPA VARIABLE BARU, langsung eksekusi dan dikembalikan

a = fungsi_tambah(10,8)
print(a)

# Fungsi Dengan Return Banyak

def operasi_MTK(angka_1,angka_2):
    '''Menghitung 2 angka dengan multi-output'''
    tambah  = angka_1 + angka_2
    kurang  = angka_1 - angka_2
    kali    = angka_1 * angka_2
    bagi    = angka_1 / angka_2
    return tambah,kurang,kali,bagi

p,q,r,s = operasi_MTK(10,5)

print(f"Hasil dari tambah   = {p}")
print(f"Hasil dari kurang   = {q}")
print(f"Hasil dari kali     = {r}")
print(f"Hasil dari bagi     = {s}")