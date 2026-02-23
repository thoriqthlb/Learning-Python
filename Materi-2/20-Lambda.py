# Lambda Function

# Biasanya
def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# Pakai Lambda
# output = lambda argument: expression
kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pang: num**pang
print(f"hasil lambda pangkat = {pangkat(3,3)}")

# Kegunaan

# Sorting untuk list biasa
data_list = ["Udin","Ucup","Abdul"]
data_list.sort()
print(f"sorted list = {data_list}")

# Sorting pakai panjang
data_list = ["Ucup","Udin","Abdul"]
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

# Sort pakai lambda
data_list = ["Ucup","Udin","Abdul"]
data_list.sort (key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")