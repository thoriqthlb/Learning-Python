data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()

print(f"Data 2D = {data_2D}")
print(f"Data 2D copy = {data_2D_copy}")

# Mengambil Data Dari Nested List

data = data_2D[0][0] # >>> Untuk mengambil yang di dalamnya
print(f"data = {data}")

# Address Semuanya

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print("\nAddress member ke-1:")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

from copy import deepcopy # untuk mencopy nested list

data_2D_deepcopy = deepcopy(data_2D)
print(f"Address deepcopy = {hex(id(data_2D_deepcopy))}")