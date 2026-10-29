#Membuat Fungsi dalam Python
def sapa():
    print("Hallo nama")

sapa()

#Fungsi Tanpa Parameter
def luas_persegi():
    sisi = 2
    luas = sisi * sisi
    return luas
luas = luas_persegi()
print(luas)

def luas_persegi():
    sisi = 2
    luas = sisi * sisi
    print(luas)
print(luas_persegi())

kamu = "Kamu global"
def kamu():
    print("Kamu di sini")
print(kamu)

#Fungsi dengan Parameter
def sapa(nama):
    print(f"halo {nama}")
nama = "budi"
sapa(nama)

#Prosedur
def tampilkan_menu():
    print("1. Lihat buku")
    print("2. Beli buku")
    print("3. Keluar")
tampilkan_menu()

#Variabel Global dan Lokal
nama = "Shasa"
umur = 19
asal = "Balikpapan"

def data_diri():
  nama = "Haekal"
  umur = 19
  asal = "Samarinda"
  print(nama)

data_diri()

#Fungsi Rekursif
def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1)
print(faktorial(4))

#Pengenalan try-except
def luas(sisi):
    luas = sisi ** 2
    return luas

while True:
    try:
        sisi = int(input("Masukkan nilai sisi: "))
    except ValueError:
        print("Input sisi bukan angka")
        continue
    print(luas(sisi))
    break