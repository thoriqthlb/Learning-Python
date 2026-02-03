# If dan Else Statement

# 1. if
# 2. kondisi
# 3. aksi

nama = input("Siapa nama Anda?: ")

# 1. Program IF Inline
if nama == "udin": print("Cek DM")   # DIPAKE KALO SATU BARIS AJA 
print(f"Terima kasih {nama}")

# 2. Program IF Indentation
if nama == "udin":                   # DIPAKE KALO UNTUK BANYAK KONDISI
    print("Cek DM!")
    print("Udah Blom?")
print(f"Terima kasih {nama}")

# 3. Else Statement
if nama == "udin":
    print("Cek DM!")
else:                                # BIASAIN NULISNYA KE BAWAH BIAR RAPI
    print("Maaf bukan Anda!")