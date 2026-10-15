import os

users = [["admin", "admin123", "admin"], ["rado", "rado123", "user"]]
karyawan = [
    [1, "Andi Pratama", "Manager", 12000000],
    [2, "Ahmad Rizki", "Staff", 6000000],
    [3, "Rudi", "Programmer", 8000000],
]
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
            for u in users:
                if u[0] == username and u[1] == password:
                    user_aktif = u
            if user_aktif is None:
                print("Username atau password salah!")
                input("Enter...")

        elif pilih == "2":
            username = input("Username baru: ").strip()
            password = input("Password baru: ").strip()
            ada = False
            for u in users:
                if u[0] == username:
                    ada = True
            if username == "" or password == "":
                print("Username dan password tidak boleh kosong!")
            elif ada:
                print("Username sudah dipakai!")
            else:
                users.append([username, password, "user"])
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
        role = user_aktif[2]
        print(f"=== MENU ({user_aktif[0]} - {role}) ===")
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
            elif not gaji.isdigit() or int(gaji) <= 0:
                print("Gaji harus angka lebih dari 0!")
            else:                
                if len(karyawan) == 0:
                    id_baru = 1
                else:
                    id_baru = karyawan[-1][0] + 1
                karyawan.append([id_baru, nama, jabatan, int(gaji)])
                print("Data berhasil ditambahkan.")
            input("Enter...")

        elif pilih == "2":
            if len(karyawan) == 0:
                print("Belum ada data.")
            else:
                for k in karyawan:
                    print("ID      :", k[0])
                    print("Nama    :", k[1])
                    print("Jabatan :", k[2])
                    print("Gaji    :", k[3])
                    print("-" * 25)
            input("Enter...")

        elif pilih == "3":
            for k in karyawan:
                print(k[0], "-", k[1])
            id_ubah = input("ID yang diubah: ").strip()
            index = -1
            for i in range(len(karyawan)):
                if str(karyawan[i][0]) == id_ubah:
                    index = i
            if index == -1:
                print("ID tidak ditemukan!")
            else:
                print("Kosongkan (Enter) jika tidak diubah.")
                nama = input("Nama baru    : ").strip()
                jabatan = input("Jabatan baru : ").strip()
                gaji = input("Gaji baru    : ").strip()
                if gaji != "" and (not gaji.isdigit() or int(gaji) <= 0):
                    print("Gaji harus angka lebih dari 0! Perubahan dibatalkan.")
                else:
                    if nama != "":
                        karyawan[index][1] = nama
                    if jabatan != "":
                        karyawan[index][2] = jabatan
                    if gaji != "":
                        karyawan[index][3] = int(gaji)
                    print("Data berhasil diubah.")
            input("Enter...")

        elif pilih == "4":
            for k in karyawan:
                print(k[0], "-", k[1])
            id_hapus = input("ID yang dihapus: ").strip()
            index = -1
            for i in range(len(karyawan)):
                if str(karyawan[i][0]) == id_hapus:
                    index = i
            if index == -1:
                print("ID tidak ditemukan!")
            else:
                karyawan.pop(index)
                print("Data berhasil dihapus.")
            input("Enter...")

        else:
            print("Pilihan tidak valid!")
            input("Enter...")

os.system("cls" if os.name == "nt" else "clear")
print("Terima kasih!")