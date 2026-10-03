username_benar = "Zaid"
password_benar = "003"
pin_benar = "003003"

saldo = 5000000
kesempatan_login = 3
login_berhasil = False

print("   SELAMAT DATANG DI APLIKASI BANK DIGITAL   ")

while kesempatan_login > 0:
    print("Kesempatan login: ", kesempatan_login)
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == username_benar and password == password_benar:
        print("Login Berhasil! Selamat datang. ")
        login_berhasil = True
        break
    elif username != username_benar and password == password_benar:
        print("Username anda salah!")
        kesempatan_login -= 1
    elif username == username_benar and password != password_benar:
        print("Password anda salah!")
        kesempatan_login -= 1
    else:
        print("Username dan Password anda salah!")
        kesempatan_login -= 1

if not login_berhasil:
    print("Akun pengguna diblokir.")
else:
    menu_aktif = True
    while menu_aktif:
        print("          MENU UTAMA         ")
        print("1. Transfer Uang")
        print("2. Logout")

        pilihan = input("Masukkan pilihan menu (1/2): ")

        if pilihan == "1":
            transfer = "y"
            while transfer == "y":
                print("          MENU TRANSFER UANG          ")
                print("Saldo saat ini: Rp ", saldo)

                penerima = input("Masukkan username penerima: ")

                nominal_valid = False
                while not nominal_valid:
                    nominal = int(input("Masukkan nominal transfer: Rp "))

                    if nominal < 50000:
                        print("Kesalahan: Nominal minimal adalah Rp 50.000! Silahkan masukkan kembali")
                        continue
                    elif nominal > saldo:
                        print("Kesalahan: Saldo tidak mencukupi! Silahkan masukkan kembali")
                        continue
                    elif nominal > 1000000:
                        print("Kesalahan: Nominal maksimal adalah Rp 1.000.000! Silahkan masukkan kembali")
                        continue
                    else:
                        nominal_valid = True
                
                    kesempatan_pin = 3
                    pin_berhasil = False

                    while kesempatan_pin > 0:
                        print("Kesempatan PIN: ", kesempatan_pin)
                        pin_input = input("Masukkan PIN konfirmasi: ")

                        if pin_input == pin_benar:
                            pin_berhasil = True
                            break
                        else:
                            print("PIN salah!")
                            kesempatan_pin -= 1

                if not pin_berhasil:
                    print("Kesempatan PIN habis. Akun pengguna diblokir.")
                    transfer = "n"
                    menu_aktif = False
                    break
        
                saldo -= nominal
                print("=======================================")
                print("          STRUK BUKTI TRANSFER         ")
                print("=======================================")
                print("Userame Pengirim  : ", username_benar)
                print("Usename Penerima  : ", penerima)
                print("Nominal Transaksi : Rp", nominal)
                print("Sisa Saldo        : Rp", saldo)
                print("=======================================")
                transfer = input("Apakah pengguna ingin melakukan transaksi lagi (y/n)? ")

        elif pilihan == "2":
            print("Anda telah Logout dari program. ")
            menu_aktif = False
        else:
            print("Pilihan tidak valid! Silahkan masukkan pilihan 1 atau 2.")