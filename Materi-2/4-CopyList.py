### Teknik Menduplikat List

a = ["Udin", "Rizki", "Hilmy"]
print(f"a = {a}")

b = a
print(f"b = {b}")

## Mencoba Mengubah Member a

# Ini akan mengubah kedua list
a[0] = "Yahya"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# Address dari list a dan b sama
print(f"Address dari a = {hex(id(a))}")
print(f"Address dari b = {hex(id(b))}")

# Menduplikasi list dengan copy
c = a.copy() # Mengopy a untuk c (beda address)

print(f"Address dari a = {hex(id(a))}")
print(f"Address dari b = {hex(id(b))}")
print(f"Address dari c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")