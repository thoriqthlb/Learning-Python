# Setiap hasil dari operasi komparasi adalah boolean

# 1. lebih besar dari (>)
a = 2
b = 3

print("===== LEBIH BESAR DARI =====")
hasil = b > a
print(b, ">", a, "=", hasil)
hasil = a > b
print(a, ">", b, "=", hasil)
hasil = a > a
print(a, ">", a, "=", hasil)

# 2. kurang dari (<)
a = 2
b = 3

print("===== KURANG DARI =====")
hasil = b < a
print(b, "<", a, "=", hasil)
hasil = a < b
print(a, "<", b, "=", hasil)
hasil = a < a
print(a, "<", a, "=", hasil)

# 3. lebih besar dari sama dengan (>=)
a = 2
b = 3

print("===== LEBIH BESAR DARI SAMA DENGAN =====")
hasil = b >= a
print(b, ">=", a, "=", hasil)
hasil = a >= b
print(a, ">=", b, "=", hasil)
hasil = a >= a
print(a, ">=", a, "=", hasil)

# 4. kurang dari sama dengan (<=)
a = 2
b = 3

print("===== KURANG DARI SAMA DENGAN =====")
hasil = b <= a
print(b, "<=", a, "=", hasil)
hasil = a <= b
print(a, "<=", b, "=", hasil)
hasil = a <= a
print(a, "<=", a, "=", hasil)

# 5. sama dengan (==)
a = 2
b = 3

print("===== SAMA DENGAN =====")
hasil = b == a
print(b, "==", a, "=", hasil)
hasil = a == b
print(a, "==", b, "=", hasil)
hasil = a == a
print(a, "==", a, "=", hasil)

# 6. tidak sama dengan (!=)
a = 2
b = 3

print("===== TIDAK SAMA DENGAN =====")
hasil = b != a
print(b, "!=", a, "=", hasil)
hasil = a != b
print(a, "!=", b, "=", hasil)
hasil = a != a
print(a, "!=", a, "=", hasil)

# 7. identitas objek atau (perbandingan untuk identitas objek bukan ke "literal" [yang ga disimpen ke memory])
x = 2 # ini assignment membuat objek 
y = 2

print("===== IDENTITAS OBJEK IS =====")
print("nilai x =", x, "id = ", hex(id(x)))
print("nilai y =", y, "id = ", hex(id(y)))

hasil = x is y
print("x is y =", hasil)

x = 2
y = 3

print("===== IDENTITAS OBJEK IS =====")
print("nilai x =", x, "id = ", hex(id(x)))
print("nilai y =", y, "id = ", hex(id(y)))

hasil = x is y
print("x is y =", hasil)

# 8. identitas objek atau (perbandingan untuk identitas objek bukan ke "literal" [yang ga disimpen ke memory])
x = 2
y = 2

print("===== IDENTITAS OBJEK IS NOT =====")
print("nilai x =", x, "id = ", hex(id(x)))
print("nilai y =", y, "id = ", hex(id(y)))

hasil = x is not y
print("x is not y =", hasil)

x = 2
y = 3

print("===== IDENTITAS OBJEK IS NOT =====")
print("nilai x =", x, "id = ", hex(id(x)))
print("nilai y =", y, "id = ", hex(id(y)))

hasil = x is not y
print("x is not y =", hasil)