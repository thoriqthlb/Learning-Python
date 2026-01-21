# operasi biner

a = 9
b = 5

# bitwise Or (|)
c = a | b

print("\n============= OR =============\n")
print(f"nilai", a, "binary-nya :", format(a, "08b"))
print(f"nilai", b, "binary-nya :", format(b, "08b"))
print("----------------------------- (|)")
print(f"nilai", c, "binary-nya:", format(c, "08b"))

# bitwise And (&)
c = a & b

print("\n============= AND =============\n")
print(f"nilai", a, "binary-nya :", format(a, "08b"))
print(f"nilai", b, "binary-nya :", format(b, "08b"))
print("----------------------------- (&)")
print(f"nilai", c, "binary-nya :", format(c, "08b"))

# bitwise Xor (^)
c = a ^ b

print("\n============= XOR =============\n")
print(f"nilai", a, "binary-nya :", format(a, "08b"))
print(f"nilai", b, "binary-nya :", format(b, "08b"))
print("----------------------------- (^)")
print(f"nilai", c, "binary-nya:", format(c, "08b"))

# shifting

# right shift (>>)
c = a >> 2
print("\n============= RIGHT SHIFT =============\n")
print(f"nilai", a, "binary-nya :", format(a, "08b"))
print("----------------------------- (>>)")
print(f"nilai", c, "binary-nya:", format(c, "08b"))

# left shift (>>)
c = a << 2
print("\n============= LEFT SHIFT =============\n")
print(f"nilai", a, "binary-nya :", format(a, "08b"))
print("----------------------------- (<<)")
print(f"nilai", c, "binary-nya:", format(c, "08b"))