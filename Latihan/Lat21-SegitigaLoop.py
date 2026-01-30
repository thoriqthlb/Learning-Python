# latihan membuat segitiga dengan perulangan

sisi = 10

# 1. Menggunakan for

# dummy variable
count = 1

print("Awal For")
for i in range(sisi):
    print("+"*count)
    count +=1

# 2. Menggunakan while

count = 1

print("Awal While")
while True:
    print("+"*count)
    count +=1

    if count > sisi:
        break

# 3. Hanya ganjil

count = 1

print("Hanya Ganjil")
while True:
    if count%2:
        print("+"*count)
        count +=1
    else: 
        count +=1
        continue

    if count > sisi:
        break

# 4. Segitiga samakaki

count = 1
spasi = int(sisi/2)

print("Segitiga Samakaki")
while True:
    if count%2:
        print(" "*spasi, "+"*count)
        spasi -= 1
        count +=1
    else: 
        count +=1
        continue

    if count > sisi:
        break  