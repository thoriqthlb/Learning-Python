list_kegiatan = []

while True:
    kegiatan = input("Masukkan kegiatan: ").capitalize()

    if kegiatan == "Stop":
        break
    list_kegiatan.append(kegiatan)


print("\nKEGIATAN HARI INI:")
for aktivitas in list_kegiatan:
    print("-",aktivitas)