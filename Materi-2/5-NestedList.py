data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1,7,8,9]
print(f" list 2D = {list_2D}")

# Contoh Penggunaan

peserta_0 = ["Rizki",18,"Laki-laki"]
peserta_1 = ["Hilmy",15,"Laki-laki"]
peserta_2 = ["Siti",21,"Perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"peserta = {list_peserta}")

print("\nDAFTAR PESERTA:\n")
for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")