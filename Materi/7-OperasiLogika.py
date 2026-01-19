#not, or, and, xor

# 1. Not (berlawanan)
print("\n===== NOT =====")
a = True
c = not a
print("data a = ", a)
print("---------------NOT")
print("data c = ", c)

print("\n<---------------------->")

# 2. Or (jika salah satu true, maka hasilnya true)
print("\n========= OR =========")
a = True
b = True
c = a or b
print(a, " or", b, "  =", c)
a = True
b = False
c = a or b
print(a, " or", b, " =", c)
a = False
b = True
c = a or b
print(a, "or", b, "  =", c)
a = False
b = False
c = a or b
print(a, "or", b, " =", c)

print("\n<---------------------->")

# 3. And (semua harus terpenuhi agar true)
print("\n========= AND =========")
a = True
b = True
c = a and b
print(a, " and", b, "  =", c)
a = True
b = False
c = a and b
print(a, " and", b, " =", c)
a = False
b = True
c = a and b
print(a, "and", b, "  =", c)
a = False
b = False
c = a and b
print(a, "and", b, " =", c)

print("\n<---------------------->")

# 4. Xor / ^ (akan true jika salah satu true)
print("\n========= XOR =========")
a = True
b = True
c = a ^ b
print(a, " xor", b, "  =", c)
a = True
b = False
c = a ^ b
print(a, " xor", b, " =", c)
a = False
b = True
c = a ^ b
print(a, "xor", b, "  =", c)
a = False
b = False
c = a ^ b
print(a, "xor", b, " =", c)