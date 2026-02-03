# Mesin Perkalian Otomatis
print(10*"=", "MESIN PERKALIAN OTOMATIS", 10*"=" + "\n")

angka = int(input("Mau belajar perkalian berapa?: "))
tanya = "ya"

while tanya == "ya":
    kali = range(1,11)
    for pengali in kali:
        print(f"Berikut adalah perkalian {angka} x {pengali}: {pengali*angka}")
    tanya = (input("\nApakah mau lanjut belajar lagi? (ya/tidak): "))
    if tanya == "ya":
        angka = int(input("Mau belajar perkalian berapa?: "))
    else: print("Terima kasih!")
print("Program selesai.")