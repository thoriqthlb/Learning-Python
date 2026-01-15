# Operasi aritmatika

a = 10
b = 3

# Operasi tambah (+)
hasil = a + b 
print(a, "+", b, "=", hasil)

# Operasi kurang (-)
hasil = a - b 
print(a, "-", b, "=", hasil)

# Operasi kali (*)
hasil = a * b 
print(a, "*", b, "=", hasil)

# Operasi bagi (/)
hasil = a / b 
print(a, "/", b, "=", hasil)

# Operasi pangkat (**)
hasil = a ** b 
print(a, "**", b, "=", hasil)

# Operasi modulus (%)
hasil = a % b 
print(a, "%", b, "=", hasil)

# Operasi bagi ke bawah (floor division) (//)
hasil = a // b 
print(a, "//", b, "=", hasil)

# Prioritas operasi

x = 2
y = 3
z = 4

hasil = x ** y / x + z * (z + y) + z ** z % x
print(x,"**",y,"/",x,"+",z,"(",z,"+",y,")","+",z,"**",z,"%",x,"=", hasil)