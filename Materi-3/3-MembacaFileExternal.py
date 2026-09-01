# Baca File External

print(3*"=", "Membaca file txt", 3*"=")

file = open("Materi-3/data.txt", mode="r") # Mode "r" untuk baca, "w" untuk tulis

print(f"status bisa dibaca: {file.readable()}") # Cara ngecek file bisa dibaca atau ngga
print(f"status bisa ditulis: {file.writable()}") # Cara ngecek file bisa ditulis atau ngga

# Baca seluruh file
#print(file.read())

# Baca per baris
#print(file.readline()) # Baris pertama
#print(file.readline()) # Baris kedua

# Baca semua sebagai list
#print(file.readlines())

print(f"Apakah file sudah ditutup: {file.closed}")

file.close()
print(f"Apakah file sudah ditutup: {file.closed}")

# praktik yang lebih profesional dan aman:
print("\n", 3*"=", "Membaca file txt dengan with", 3*"=")

with open("Materi-3/data.txt", mode="r") as file: # buka dan simpan sebagai VARIABLE file
    content = file.readline()
    print(content)
    print(f"Apakah file sudah ditutup: {file.closed}")
print(f"Apakah file sudah ditutup: {file.closed}")