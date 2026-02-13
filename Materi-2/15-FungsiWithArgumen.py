import os
os.system("cls")


'''Fungsi dengan argumen/input (input)'''

# Template
# def nama_fungsi(argumen):
#   badan fungsi

def hello_world(nama):
    '''fungsi hello world menerima input dengan variable nama'''
    print(F"Selamat datang {nama}")

hello_world("Udin")
hello_world("Ucup")

# Program Tambah

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}\n")

tambah(3,8)
tambah(7980,6)

def say_hi(listt): # membuat fungsi untuk sapaan
    data_peserta = listt.copy() # cuma sebagai copy
    
    for peserta in data_peserta: # manggil isi 1-1 dari list
        print(f"Yang terhormat {peserta}")

list_anggota = ["Udin","Ucup","Abdul"] # listnya

say_hi(list_anggota)