# for kondisi:
#    aksi

# Bisa dipakai unutik kasus yang pasti (bisa dihitung)

# Dengan List
angka2_list = [0,1,2,3,4] # ini adalah list
print(angka2_list)

for i in angka2_list:
    print(f"i sekarang => {i}")

print("Akhir dari program 1\n")


# Dengan Range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang => {i}")

print("Akhir dari program 2\n")


# Dengan Range_2
angka2_range = range(1,5) # start ditulis, stop tidak.

for i in angka2_range:
    print(f"i sekarang => {i}")

print("Akhir dari program 3\n")


# Menggunakan String
data_str = "udin awaludin"

for huruf in data_str:
    print(huruf)

print("Akhir dari program 4\n")