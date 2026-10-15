import os

data_pengguna = [
    ["zaid", "zaidganteng003", "admin"],
    ["zia", "zia018", "admin"]
]

data_jersey = [
    ["Bayern Munchen", "M", 20],
    ["Liverpool", "L", 15],
    ["Borneo FC", "XL", 10],
    ["Aston Villa", "S", 12],
    ["Persija Jakarta", "M", 25],
    ["Como", "L", 30],
    ["Real Madrid", "S", 5]
]

status_login = False
user_aktif = ""
role_aktif = "" 

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 45)
    print("     SISTEM PENGELOLAAN STOK JERSEY BOLA")
    print("=" * 45)

    if not status_login:
        print("1. Login")
        print("2. Registrasi Akun")
        print("3. Keluar Program")
        print("-" * 45)
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- LOGIN ---")
            user = input("Username: ")
            password = input("Password: ")

            login_sukses = False
            i = 0
            while i < len(data_pengguna):
                if data_pengguna[i][0] == user and data_pengguna[i][1] == password:
                    login_sukses = True
                    user_aktif = data_pengguna[i][0]
                    role_aktif = data_pengguna[i][2]
                    break
                i += 1

            if login_sukses:
                print(f"Login berhasil. Selamat datang, {user_aktif} ({role_aktif})")
                status_login = True
            else:
                print("*Error* Username atau password salah!")
            input("Tekan Enter untuk lanjut...")

        elif pilihan == "2":
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("--- REGISTRASI AKUN ---")
            user_baru = input("Username: ")
            password_baru = input("Password: ")

            if user_baru == "" or password_baru == "":
                print("*Error* Username dan password tidak boleh kosong!")
            else:
                user_sudah_ada = False
                i = 0
                while i < len(data_pengguna):
                    if data_pengguna[i][0] == user_baru:
                        user_sudah_ada = True
                        break
                    i += 1

                if user_sudah_ada:
                    print("*Error* Username tersebut sudah terdaftar!")

                else:
                    data_pengguna.append([user_baru, password_baru, "user"])
                    print("Registrasi berhasil. Silakan login.")
            input("Tekan Enter untuk lanjut...")

        elif pilihan == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Program selesai. Terima kasih sudah menggunakan.")
            break
        else:
            print("*Error* Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")

    else:
        print(f"Login sebagai : {user_aktif} ({role_aktif})")
        print("-" * 45)

        if role_aktif == "admin":
            print("1. Tambah Data Jersey Baru")
            print("2. Lihat Rekapitulasi Stok Jersey")
            print("3. Perbarui Jumlah Stok")
            print("4. Hapus Data Jersey")
            print("5. Logout")
            pilih_menu = input("Pilih menu (1-5): ")
        else:
            print("1. Lihat Rekapitulasi Stok Jersey")
            print("2. Logout")
            pilih_menu = input("Pilih menu (1-2): ")
            if pilih_menu == "1":
                pilih_menu = "2"
            elif pilih_menu == "2":
                pilih_menu = "5"

        if pilih_menu == "1" and role_aktif == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- TAMBAH DATA JERSEY ---")
            klub_baru = input("Masukkan Nama Klub Bola  : ")
            ukuran_baru = input("Masukkan Ukuran (S/M/L/XL): ")
            stok_baru = int(input("Masukkan Jumlah Stok : "))

            if klub_baru == "" or ukuran_baru == "":
                print("*Error* Data tidak boleh kosong!")
            else:
                data_jersey.append([klub_baru, ukuran_baru, stok_baru])
                print(f"Data jersey klub {klub_baru} berhasil ditambahkan ke gudang.")
                input("Tekan Enter untuk kembali ke menu utama...")
            

        elif pilih_menu == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 58)
            print("          REKAPITULASI STOK JERSEY")
            print("=" * 58)
            for item in data_jersey:
                print(f"Klub: {item[0]:<18} | Ukuran: {item[1]:<6} | Stok Fisik: {item[2]}")
            print("=" * 58)
            input("Tekan Enter untuk kembali ke menu utama...")

        elif pilih_menu == "3" and role_aktif == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- PERBARUI JUMLAH STOK ---")
            for item in data_jersey:
                print(f"Klub: {item[0]} | Stok: {item[2]}")
            print("-" * 40)

            cari_klub = input("Masukkan nama klub yang ingin diupdate stoknya: ")
            ketemu = False
            i = 0
            while i < len(data_jersey):
                if data_jersey[i][0] == cari_klub:
                    ketemu = True
                    print(f"Stok saat ini: {data_jersey[i][2]}")
                    stok_pengganti = int(input("Masukkan jumlah stok baru: "))
                    data_jersey[i][2] = stok_pengganti
                    print("Stok jersey berhasil diperbarui.")
                    break
                i += 1
            if not ketemu:
                print("*Error* Klub tidak ditemukan!")
            input("Tekan Enter untuk kembali ke menu utama...")

        elif pilih_menu == "4" and role_aktif == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- HAPUS DATA JERSEY ---")   
            for item in data_jersey:
                print(f"Klub: {item[0]} | Stok: {item[2]}")
            print("-" * 40)

            cari_hapus = input("Masukkan nama klub yang ingin dihapus: ")
            ketemu = False
            i = 0
            while i < len(data_jersey):
                if data_jersey[i][0] == cari_hapus:
                    ketemu = True
                    del data_jersey[i]
                    print("Data jersey berhasil dihapus.")
                    break
                i += 1
            if not ketemu:
                    print("*Error* Klub tidak ditemukan!")
            input("Tekan Enter untuk kembali ke menu utama...")
                
        elif pilih_menu == "5":
            status_login = False
            user_aktif = "" 
            role_aktif = "" 
            print("Anda telah logout.")
            input("Tekan Enter untuk lanjut...")
        else:
            print("*Error* Pilihan menu tidak valid!")
            input("Tekan Enter untuk lanjut...")