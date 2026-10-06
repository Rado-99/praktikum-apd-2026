# Username dan password
username_benar = "Rado".upper()
password_benar = "099"

# 1. Login
percobaan = 3   
login = False

while percobaan > 0:
    username = input("Username: ").upper()
    password = input("Password: ")

    if username == "" or password == "":
        print("Username dan password tidak boleh kosong")
        continue

    if username == username_benar and password == password_benar:
        print("Login berhasil")
        login = True
        break
    else:
        percobaan -= 1
        print("Login gagal. Sisa percobaan:", percobaan)

if login == False:
    print("Login gagal. Program berhenti.")
else:
    # 2. Uang saku awal
    while True:
        uang = input("Masukkan uang saku awal: ")
        if uang.isdigit() and int(uang) > 0:
            uang_bulanan = int(uang)
            break
        else:
            print("Input harus berupa angka lebih dari 0!")

    total_pengeluaran = 0

    # 3. Menu utama
    while uang_bulanan > 0:
        print("=== MENU UTAMA ===")
        print("[1] Catat Pengeluaran")
        print("[2] Cek Sisa Uang Saku")
        print("[3] Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            while True:
                nominal = input("Masukkan nominal pengeluaran: ")

                if not nominal.isdigit() or int(nominal) <= 0:
                    print("Nominal harus berupa angka lebih dari 0!")
                    continue

                nominal = int(nominal)
                if nominal > uang_bulanan:
                    print("Saldo anda tidak cukup! Sisa uang saku:", uang_bulanan)
                    continue

                uang_bulanan = uang_bulanan - nominal
                total_pengeluaran = total_pengeluaran + nominal
                print("Sisa uang saku:", uang_bulanan)

                if uang_bulanan == 0:
                    break

                lagi = input("Apakah Anda ingin mencatat pengeluaran lagi? (Y/T): ").upper()
                while lagi != "Y" and lagi != "T":
                    print("Input harus Y atau T!")
                    lagi = input("Apakah Anda ingin mencatat pengeluaran lagi? (Y/T): ").upper()

                if lagi == "T":
                    break

        elif pilihan == "2":
            print("Sisa uang saku:", uang_bulanan)
            print("Total pengeluaran:", total_pengeluaran)

        elif pilihan == "3":
            print("Terima kasih ^_^")
            break

        else:
            print("Pilihan tidak valid!")

    if uang_bulanan == 0:
        print("Uang saku anda sudah habis. Total pengeluaran:", total_pengeluaran)
        print("Terima kasih ^_^")

