print("\n===== BOT QC VIDEO CHECKER =====\n")

resolusi = int(input("Masukkan Resolusi: "))
durasi = int(input("Masukkan Durasi (detik): "))
format_vid = input("Masukkan Format Video: ")
bitrate = int(input("Masukkan Bitrate: "))

print("--------------------------")

print("Hasil Pengecekan: \n")

vid = "mp4", "Mp4", "MP4"
print("Apakah Resolusi HD (>= 720)?: ", resolusi >= 720 )
print("Apakah Video Pendek (<= 1 Menit)?: ", durasi <= 60 )
print("Apakah Format Valid (Mp4)?: ", format_vid == vid )
print("Apakah Bitrate Aman (!= 4000)?: ", bitrate != 4000 )
