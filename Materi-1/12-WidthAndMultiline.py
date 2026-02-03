# Width and multiline

# Data
data_nama = "Udin Awaludin"
data_umur = 17
data_tinggi = 150.5
data_nomor_sepatu = 44

# String Standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"=", "DATA STRING", 5*"=")
print(data_string)

# String Multiline (pake enter [\n])
data_string = f"nama = {data_nama} \numur = {data_umur} \ntinggi = {data_tinggi} \nsepatu = {data_nomor_sepatu}"
print("\n"+ 5*"=", "DATA STRING", 5*"=")
print(data_string)

# String Multiline (pake kutip triplete [""*3])
data_string = f"""nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+ 5*"=", "DATA STRING", 5*"=")
print(data_string)