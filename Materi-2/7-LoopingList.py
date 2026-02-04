# For loop
print("\nFor loop:")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Rizki", "Hilmy", "Yahya", "Udin", "Ucup"]
for nama in peserta:
    print(f"nama = {nama}")

# For loop dan Range
print("\nFor loop dan range:")
kumpulan_angka = [10,3,2,5,6,4]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# While loop
print("\nWhile loop:")
kumpulan_angka = [10,3,2,5,6,4]

panjang = len(kumpulan_angka)

i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# List comprehension
print("\nList Comprehension:")
data = ["Udin",1,2,3,"Ucup"]

[print(f"data = {i}") for i in data]


# Enumerate >>>> bisa gantiin for + range
print("\nEnumerate:")
data_list = ["Udin",1,2,3,"Ucup"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")