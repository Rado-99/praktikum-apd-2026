import os

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "rado": {"password": "rado123", "role": "user"},
}

karyawan = {
    1: {"nama": "Andi Pratama", "jabatan": "Manager", "gaji": 12000000},
    2: {"nama": "Ahmad Rizki", "jabatan": "Staff", "gaji": 6000000},
    3: {"nama": "Rudi", "jabatan": "Programmer", "gaji": 8000000},
}

jalan = True

while jalan:
    user_aktif = None

    # ===== MENU AWAL: LOGIN / REGISTER =====
    while user_aktif is None and jalan:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== SISTEM DATA KARYAWAN ===")
        print("1. Login\n2. Register\n0. Keluar")
        pilih = input("Pilih: ").strip()

        if pilih == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if username in users and users[username]["password"] == password:
                user_aktif = username
            if user_aktif is None:
                print("Username atau password salah!")
                input("Enter...")

        elif pilih == "2":
            username = input("Username baru: ").strip()
            password = input("Password baru: ").strip()
            if username == "" or password == "":
                print("Username dan password tidak boleh kosong!")
            elif username in users:
                print("Username sudah dipakai!")
            else:
                users[username] = {"password": password, "role": "user"}
                print("Register berhasil, silakan login.")
            input("Enter...")

        elif pilih == "0":
            jalan = False
        else:
            print("Pilihan tidak valid!")
            input("Enter...")

    # ===== MENU UTAMA =====
    while user_aktif is not None:
        os.system("cls" if os.name == "nt" else "clear")
        role = users[user_aktif]["role"]
        print(f"=== MENU ({user_aktif} - {role}) ===")
        if role == "admin":
            print("1. Tambah\n2. Lihat Karyawan\n3. Ubah\n4. Hapus")
        else:
            print("1. Lihat Karyawan")
        print("0. Logout")
        pilih = input("Pilih: ").strip()

        if role == "user" and pilih == "1":
            pilih = "2"
        elif role == "user" and pilih != "0":
            pilih = "x"

        if pilih == "0":
            user_aktif = None

        elif pilih == "1":
            nama = input("Nama    : ").strip()
            jabatan = input("Jabatan : ").strip()
            gaji = input("Gaji    : ").strip()
            if nama == "" or jabatan == "":
                print("Nama dan jabatan tidak boleh kosong!")
            elif not gaji.isdecimal() or int(gaji) <= 0:
                print("Gaji harus angka lebih dari 0!")
            else:
                if len(karyawan) == 0:
                    id_baru = 1
                else:
                    id_baru = max(karyawan) + 1
                karyawan[id_baru] = {"nama": nama, "jabatan": jabatan, "gaji": int(gaji)}
                print("Data berhasil ditambahkan.")
            input("Enter...")

        elif pilih == "2":
            if len(karyawan) == 0:
                print("Belum ada data.")
            else:
                for id_k, k in karyawan.items():
                    print("ID      :", id_k)
                    print("Nama    :", k["nama"])
                    print("Jabatan :", k["jabatan"])
                    print("Gaji    :", k["gaji"])
                    print("-" * 25)
            input("Enter...")

        elif pilih == "3":
            for id_k, k in karyawan.items():
                print(id_k, "-", k["nama"])
            id_ubah = input("ID yang diubah: ").strip()
            if not id_ubah.isdecimal() or int(id_ubah) not in karyawan:
                print("ID tidak ditemukan!")
            else:
                id_ubah = int(id_ubah)
                print("Kosongkan (Enter) jika tidak diubah.")
                nama = input("Nama baru    : ").strip()
                jabatan = input("Jabatan baru : ").strip()
                gaji = input("Gaji baru    : ").strip()
                if gaji != "" and (not gaji.isdecimal() or int(gaji) <= 0):
                    print("Gaji harus angka lebih dari 0! Perubahan dibatalkan.")
                else:
                    if nama != "":
                        karyawan[id_ubah]["nama"] = nama
                    if jabatan != "":
                        karyawan[id_ubah]["jabatan"] = jabatan
                    if gaji != "":
                        karyawan[id_ubah]["gaji"] = int(gaji)
                    print("Data berhasil diubah.")
            input("Enter...")

        elif pilih == "4":
            for id_k, k in karyawan.items():
                print(id_k, "-", k["nama"])
            id_hapus = input("ID yang dihapus: ").strip()
            if not id_hapus.isdecimal() or int(id_hapus) not in karyawan:
                print("ID tidak ditemukan!")
            else:
                del karyawan[int(id_hapus)]
                print("Data berhasil dihapus.")
            input("Enter...")

        else:
            print("Pilihan tidak valid!")
            input("Enter...")

os.system("cls" if os.name == "nt" else "clear")
print("Terima kasih!")