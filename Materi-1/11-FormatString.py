# string
nama = "Udin"
format_str = f"Hallo {nama}!"
print(format_str)

# boolean
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"Angka = {angka}"
print(format_str)

# integer
angka = 15
format_str = f"Bilangan bulat = {angka:d}" # "d" khusus integer, ga begitu penting
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"Ribuan = {angka:,}" # jadi mudah dibaca
print(format_str)

# bilangan desimal
desimal = 2005.54192419
format_str = f"Desimal = {desimal:.2f}" # membatasi angka di belakang koma
print(format_str)

# menampilkan leading zero
desimal = 2005.54192419
format_str = f"Desimal = {desimal:08.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"Minus = {angka_minus}"
format_plus = f"Plus = {angka_plus:+}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"Persen = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_str = f"harga total = Rp{harga*jumlah:,}".replace(",",".")
print(format_str)