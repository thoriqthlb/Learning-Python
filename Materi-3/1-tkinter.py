# Untuk membuat GUI standar 

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk() 
window.configure(bg="white")
window.geometry("400x300")
window.resizable(False,False)
window.title("UDIN_APP")

# Variable dan fungsi
nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()

def tombol_klik():
    '''Pesan ini akan dipanggil oleh tombol'''
    print(nama_belakang.get())
    print("WELCOME TO UDIN APP!")
    pesan = f"Halo {nama_depan.get()} {nama_belakang.get()}!"
    showinfo(title="123", message=pesan)

# Frame input
input_frame = ttk.Frame(window)

# Untuk penempatan ada grid, pack, dan place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(fill="x", expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=nama_depan)
nama_depan_entry.pack(fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(fill="x", expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=nama_belakang)
nama_belakang_entry.pack(fill="x", expand=True)

# 5. Tombol
tombol_sapa = tk.Button(input_frame, text="sapa", command=tombol_klik)
tombol_sapa.pack(fill="x", expand=True, padx=10, pady=10)

# Main loop window
window.mainloop()