print("KASIR BIOSKOP CINEMA")

nama = input("Nama Pembeli: ")
umur = int(input("Umur Pembeli: "))

if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")
else:
    print("     DAFTAR HARGA TIKET    ")
    print("1. Reguler : Rp 50.000")
    print("2. Premium : Rp 75.000")
    print("3. VIP     : Rp 100.000")

    jenis_tiket = input("Jenis Tiket: ")

    if jenis_tiket == "Reguler":
        harga_tiket = 50000
    elif jenis_tiket == "Premium":
        harga_tiket = 75000
    elif jenis_tiket == "VIP":
        harga_tiket = 100000
    else:
        harga_tiket = None

    if harga_tiket == None:
        print("*PERINGATAN* Jenis tiket tidak valid!")
    else:
        status_member = input("Status Member (Ya/Tidak): ")

        diskon = 0.20 if status_member == "Ya" else 0.0
        biaya_admin = 0 if status_member == "Ya" else 2000

        nominal_diskon = harga_tiket * diskon
        total_bayar = (harga_tiket - nominal_diskon) + biaya_admin

        print("Total bayar: ", total_bayar)
        uang_bayar = int(input("Nominal Uang Bayar: "))

        if uang_bayar < total_bayar:
            print("*PERINGATAN* Uang bayar kurang dari total bayar!")
        else:
            kembalian = uang_bayar - total_bayar

            print("================================================")
            print("                STRUK PEMBELIAN                 ")
            print("================================================")
            print("Nama Pembeli   : ", nama)
            print("Umur           : ", umur)
            print("Jenis Tiket    : ", jenis_tiket)
            print("Status Member  : ", status_member)
            print("------------------------------------------------")
            print("Harga Tiket    : Rp", harga_tiket)
            print("Diskon Member  : Rp", diskon)
            print("Biaya Admin    : Rp", biaya_admin)
            print("------------------------------------------------")
            print("Total Bayar    : Rp", total_bayar)
            print("Uang Bayar     : Rp", uang_bayar)
            print("Kembalian      : Rp", kembalian)
            print("================================================")
            print(" Selamat Menonton & Semoga Harimu Menyenangkan! ")