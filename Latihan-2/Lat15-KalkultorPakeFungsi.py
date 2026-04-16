import os
os.system("cls")

# Mempraktikkan fungsi untuk membuat logika kalkulator

# THE FUNCTION (MAKE SURE IT JUST CONTAIN 1 TASK [exp: to count] )
def kalkulator(angka_1, angka_2, operator):
    '''membuat perhitungan dari kalkulator'''

    if operator == "+":
        hasil = angka_1 + angka_2
    elif operator == "-":
        hasil = angka_1 - angka_2
    elif operator == "*":
        hasil = angka_1 * angka_2
    elif operator == "/":
        hasil = angka_1 / angka_2

    return hasil


# THE PROGRAM
while True:

    input_angka_1 = float(input("\nMasukkan angka pertama: "))
    input_angka_2 = float(input("Masukkan angka kedua: "))
    input_operator = (input("Masukkan operatornya: "))

    if input_operator != "+" and input_operator != "-" and input_operator != "*" and input_operator != "/":
        print("\nOperator yang dimasukkan salah.\n")
        continue
    
    elif input_operator == "/" and input_angka_2 == 0:
        print("\nError! pembagian dengan 0 tidak terdefinisi.\n")
        continue
    
    jawaban = kalkulator(input_angka_1, input_angka_2, input_operator)
    print(f"Hasil dari {input_angka_1} {input_operator} {input_angka_2} = {jawaban:.2f}")

    tanya = input("\nLanjut? (y/n): ")

    if tanya == "n":
        print("\nProgram selesai, terima kasih!")
        break