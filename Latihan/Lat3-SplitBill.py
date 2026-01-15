print("\n===PATUNGAN SPLIT BILL===\n")

tagihan = int(input("Berapa total tagihan: "))
persen_pajak = int(input("Berapa pajaknya (dalam persen): "))
orang = int(input("Berapa jumlah orang: "))

print("-----------------------")

pajak = tagihan * persen_pajak/100
total = tagihan + pajak
bagi = (total/orang)
print("Pajak: Rp", pajak)
print("Total: Rp", total)

print("-----------------------\n")

print("===TOTAL DIBAGI JUMLAH ORANG===\n")
print(f"Per orang bayar: Rp{bagi:,.2f}" .replace(",", "."))