barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
barang_slicing = barang[0:5:2]

total_bayar = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
pajak = total_bayar * 0.15
total_bayar_keseluruhan = total_bayar + pajak

rata_rata = total_bayar_keseluruhan / len(barang)

total_usd = total_bayar_keseluruhan / 17754
total_eur = total_bayar_keseluruhan / 20380

nim = 3
bolean = nim < rata_rata

print("BARANG")
print("List Harga Barang :", barang)
print("Barang 1,3,dan 5 :", barang_slicing)
print()
print("HASIL BELANJA ANDI")
print("Total Bayar : Rp", total_bayar)
print("Pajak (15%) : Rp", pajak)
print("Total Bayar (setelah pajak) : Rp", total_bayar_keseluruhan)
print()
print("RATA-RATA")
print("Rata-rata : Rp", rata_rata)
print()
print("KONVERSI KE DUA MATA UANG BERBEDA")
print("Total Bayar (USD) : $", total_usd)
print("Total Bayar (EUR) : €", total_eur)
print()
print("NIM :", nim)
print("Bolean :", bolean)