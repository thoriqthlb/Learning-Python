# Membuat gabungan area rentang dari angka

# 1. Kurang dari 3 atau lebih dari 10

inputUser = float(input("\nMasukkan angka yang kurang dari 3 ATAU lebih besar dari 10: "))

#+++++++3----------------
# Memeriksa angka kurang dari 3

isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

#---------------10+++++++
# Memeriksa angka lebih dari 10

isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

#+++++++3-------10+++++++

isCorrect = isKurangDari or isLebihDari
print("Angka yang Anda masukkan: ", isCorrect)

print("\n<-------------------------->")

# 2. Lebih dari 3 dan kurang dari 10

inputUser = float(input("\nMasukkan angka yang lebih dari 3 DAN kurang dari 10: "))

#-------3++++++++++++++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3  :", isLebihDari)

#++++++++++++++10--------
# Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10:", isKurangDari)

#------3++++++++10--------
isCorrect = isKurangDari and isLebihDari
print("Angka yang Anda masukkan:", isCorrect)

print("\n<-------------------------->")

# 3. Lebih dari 0, kurang dari 5, lebih dari 8, dan kurang dari 11

inputUser = float(input("\nMasukkan angka yang lebih dari 0 DAN kurang dari 5 ATAU lebih dari 8 DAN kurang dari 11: "))

#-------0++++++++++++++++
# Lebih dari 0
isLebihDari1 = inputUser > 0
print("Lebih dari 0  :", isLebihDari1)

#++++++++++++++5---------
# Kurang dari 5
isKurangDari1 = inputUser < 5
print("Kurang dari 5 :", isKurangDari1)

#-------8++++++++++++++++
# Lebih dari 8
isLebihDari2 = inputUser > 8
print("Lebih dari 8  :", isLebihDari2)

#++++++++++++++11---------
# Kurang dari 11
isKurangDari2 = inputUser < 11
print("Kurang dari 11:", isKurangDari2)

#------0+++++++++5--------8+++++++++11--------
isCorrect = (isLebihDari1 and isKurangDari1) or (isLebihDari2 and isKurangDari2)
print("Angka yang Anda masukkan:", isCorrect)

print("\n<-------------------------->")

# 4. Kurang dari 0, lebih dari 5, kurang dari 8, dan lebih dari 11

inputUser = float(input("\nMasukkan angka yang kurang dari 0 ATAU lebih dari 5 DAN kurang dari 8 ATAU lebih dari 11: "))

#+++++++0---------------
# Kurang dari 0
isKurangDari1 = inputUser < 0
print("Kurang dari 0  :", isKurangDari1)

#-------------5++++++++++
# Lebih dari 5
isLebihDari1 = inputUser > 5
print("Lebih dari 5 :", isLebihDari1)

#+++++++8----------------
# Kurang dari 8
isKurangDari2 = inputUser < 8
print("Kurang dari 8  :", isKurangDari2)

#--------------11++++++++
# Lebih dari 11
isLebihDari2 = inputUser > 11
print("Lebih dari 11:", isLebihDari2)

#+++++0---------5+++++8---------11+++++
isCorrect = isKurangDari1 or (isLebihDari1 and isKurangDari2) or isLebihDari2
print("Angka yang Anda masukkan:", isCorrect)


#ILMU BARU (DI AKHIR), "AND" BISA DIPERSINGKAT PAKE LOGIKA MTK YANG BIASANYA

# # 4. Kurang dari 0, lebih dari 5, kurang dari 8, dan lebih dari 11

# inputUser = float(input("\nMasukkan angka yang kurang dari 0 atau lebih dari 5 dan kurang dari 8 atau lebih dari 11: "))

# #+++++++0---------------
# # Kurang dari 0
# isKurangDari1 = inputUser < 0
# print("Kurang dari 0  :", isKurangDari1)

# #-------------5++++++++++
# # Lebih dari 5
# isLebihDari1 = inputUser > 5
# print("Lebih dari 5 :", isLebihDari1)

# #+++++++8----------------
# # Kurang dari 8
# isKurangDari2 = inputUser < 8
# print("Kurang dari 8  :", isKurangDari2)

# #--------------11++++++++
# # Lebih dari 11
# isLebihDari2 = inputUser > 11
# print("Lebih dari 11:", isLebihDari2)

# #+++++0---------5+++++8---------11+++++
# isCorrect = (inputUser < 0) or (5 < inputUser < 8) or (inputUser > 11)
# print("Angka yang Anda masukkan:", isCorrect)