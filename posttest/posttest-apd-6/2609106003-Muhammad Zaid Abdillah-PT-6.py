import os

data_pengguna = {
    "zaid": {"password": "zaidganteng003", "role": "admin"},
    "zia": {"password": "zia018", "role": "admin"}
}

data_jersey = {
    "Bayern Munchen": {"ukuran": "M", "stok": 20},
    "Liverpool": {"ukuran": "L", "stok": 15},
    "Borneo FC": {"ukuran": "XL", "stok": 10},
    "Aston Villa": {"ukuran": "S", "stok": 12},
    "Persija Jakarta": {"ukuran": "XXL", "stok": 25},
    "Como": {"ukuran": "L", "stok": 30},
    "Real Madrid": {"ukuran": "S", "stok": 5}
}

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

        if pilihan == "":
            print("*Error* Pilihan menu tidak boleh kosong!")
            input("Tekan Enter untuk lanjut...")
        elif pilihan == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- LOGIN ---")
            user = input("Username: ")
            password = input("Password: ")

            if user == "" or password == "":
                print("*Error* Username dan password tidak boleh kosong!")
            else:
                login_sukses = False
                if user in data_pengguna and data_pengguna[user]["password"] == password:
                    login_sukses = True
                    user_aktif = user
                    role_aktif = data_pengguna[user]["role"]

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
            elif user_baru in data_pengguna:
                print("*Error* Username tersebut sudah terdaftar!")
            else:
                data_pengguna[user_baru]= {"password": password_baru, "role": "user"}
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

        if pilih_menu == "":
            print("*Error* Pilihan menu tidak boleh kosong!")
            input("Tekan Enter untuk lanjut...")

        elif pilih_menu == "1" and role_aktif == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- TAMBAH DATA JERSEY ---")

            klub_baru = input("Masukkan Nama Klub Bola: ")
            if klub_baru == "":
                print("*Error* Klub tidak boleh kosong!")
            elif klub_baru.isdigit():
                print("*Error* Klub tidak valid!")
            else:
                ukuran_baru = input("Masukkan Ukuran (S/M/L/XL/XXL): ")
                if ukuran_baru == "":
                    print("*Error* Ukuran tidak boleh kosong!")
                elif ukuran_baru not in ["S", "M", "L", "XL", "XXL"]:
                    print("*Error* Ukuran tidak valid!")
                else:
                    stok_baru = input("Masukkan Jumlah Stok: ")
                    if stok_baru == "":
                        print("*Error* Jumlah stok tidak boleh kosong!")
                    elif not stok_baru.isdigit():
                        print("*Error* Jumlah stok tidak valid!")
                    else:
                        data_jersey[klub_baru] = {"ukuran": ukuran_baru, "stok": int(stok_baru)}
                        print(f"Data jersey klub {klub_baru} berhasil ditambahkan ke gudang.")
            input("Tekan Enter untuk kembali ke menu utama...")

        elif pilih_menu == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 58)
            print("                 REKAPITULASI STOK JERSEY")
            print("=" * 58)
            for klub, data in data_jersey.items():
                print(f"Klub: {klub:<18} | Ukuran: {data['ukuran']:<6} | Stok Fisik: {data['stok']}")
            print("=" * 58)
            input("Tekan Enter untuk kembali ke menu utama...")

        elif pilih_menu == "3" and role_aktif == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- PERBARUI JUMLAH STOK ---")
            for klub, data in data_jersey.items():
                print(f"Klub: {klub:<18} | Stok: {data['stok']}")
            print("-" * 35)

            cari_klub = input("Masukkan nama klub yang ingin diupdate stoknya: ")
            if cari_klub == "":
                print("*Error* Klub tidak boleh kosong!")
            elif cari_klub not in data_jersey:
                print("*Error* Klub tidak ditemukan!")
            else:
                print(f"Stok saat ini: {data_jersey[cari_klub]['stok']}")
                stok_pengganti = input("Masukkan jumlah stok baru: ")

                if stok_pengganti == "":
                    print("*Error* Jumlah stok tidak boleh kosong!")
                elif not stok_pengganti.isdigit():
                    print("*Error* Jumlah stok tidak valid")
                else: 
                    data_jersey[cari_klub]['stok'] = int(stok_pengganti)
                    print("Stok jersey berhasil diupdate.")
            input("Tekan Enter untuk kembali ke menu utama...")

        elif pilih_menu == "4" and role_aktif == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- HAPUS DATA JERSEY ---")
            for klub, data in data_jersey.items():
                print(f"Klub: {klub:<18} | Stok: {data['stok']}")
            print("-" * 35)

            cari_hapus = input("Masukkan nama klub yang ingin dihapus: ")
            if cari_hapus == "":
                print("*Error* Klub tidak boleh kosong!")
            elif cari_hapus not in data_jersey:
                print("*Error* Klub tidak ditemukan!")
            else:
                del data_jersey[cari_hapus]
                print("Data jersey berhasil dihapus.")
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