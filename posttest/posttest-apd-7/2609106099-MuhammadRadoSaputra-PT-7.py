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

user_aktif = None
jalan = True 

def buat_id_baru():
    "Mengembalikan ID baru untuk karyawan."
    if len(karyawan) == 0:
        return 1
    return max(karyawan) + 1

def baca_id():
    "Meminta ID dari user, memvalidasi, lalu mengembalikan ID (int)."
    teks = input("ID karyawan: ").strip()
    if not teks.isdecimal():
        raise ValueError("ID harus berupa angka!")
    id_k = int(teks)
    if id_k not in karyawan:
        raise KeyError(id_k)
    return id_k

def validasi_gaji(teks):
    "Memvalidasi input gaji, mengembalikan gaji dalam bentuk int."
    if not teks.isdecimal():
        raise ValueError("Gaji harus berupa angka bulat!")
    gaji = int(teks)
    if gaji <= 0:
        raise ValueError("Gaji harus lebih dari 0!")
    return gaji

def cek_login(username, password):
    "Mengembalikan True jika username dan password cocok."
    return username in users and users[username]["password"] == password

def total_gaji(daftar_id):
    """Menjumlahkan gaji semua ID pada daftar_id secara rekursif."""
    # Base case: daftar kosong
    if len(daftar_id) == 0:
        return 0
    return karyawan[daftar_id[0]]["gaji"] + total_gaji(daftar_id[1:])

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input("Enter...")

def tampilkan_daftar_singkat():
    for id_k, k in karyawan.items():
        print(id_k, "-", k["nama"])

def lihat_karyawan():
    try:
        if len(karyawan) == 0:
            raise ValueError("Belum ada data.")
        for id_k, k in karyawan.items():
            print("ID      :", id_k)
            print("Nama    :", k["nama"])
            print("Jabatan :", k["jabatan"])
            print("Gaji    :", k["gaji"])
            print("-" * 25)
    except ValueError as e:
        print(e)
    else:
        print(f"Total gaji seluruh karyawan: {total_gaji(list(karyawan))}")
    finally:
        jeda()

def tambah_karyawan():
    try:
        nama = input("Nama    : ").strip()
        jabatan = input("Jabatan : ").strip()
        gaji_teks = input("Gaji    : ").strip()
        if nama == "" or jabatan == "":
            raise ValueError("Nama dan jabatan tidak boleh kosong!")
        gaji = validasi_gaji(gaji_teks)
    except ValueError as e:
        print(e)
    else:
        karyawan[buat_id_baru()] = {"nama": nama, "jabatan": jabatan, "gaji": gaji}
        print("Data berhasil ditambahkan.")
    finally:
        jeda()

def ubah_karyawan():
    try:
        tampilkan_daftar_singkat()
        id_ubah = baca_id()
        print("Kosongkan (Enter) jika tidak diubah.")
        nama = input("Nama baru    : ").strip()
        jabatan = input("Jabatan baru : ").strip()
        gaji_teks = input("Gaji baru    : ").strip()
        gaji_baru = validasi_gaji(gaji_teks) if gaji_teks != "" else None
    except KeyError:
        print("ID tidak ditemukan!")
    except ValueError as e:
        print(e, "Perubahan dibatalkan.")
    else:
        if nama != "":
            karyawan[id_ubah]["nama"] = nama
        if jabatan != "":
            karyawan[id_ubah]["jabatan"] = jabatan
        if gaji_baru is not None:
            karyawan[id_ubah]["gaji"] = gaji_baru
        print("Data berhasil diubah.")
    finally:
        jeda()

def hapus_karyawan():
    try:
        tampilkan_daftar_singkat()
        id_hapus = baca_id()
    except KeyError:
        print("ID tidak ditemukan!")
    except ValueError as e:
        print(e)
    else:
        del karyawan[id_hapus]
        print("Data berhasil dihapus.")
    finally:
        jeda()

def login():
    global user_aktif
    try:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if not cek_login(username, password):
            raise ValueError("Username atau password salah!")
    except ValueError as e:
        print(e)
    else:
        user_aktif = username
    finally:
        if user_aktif is None:
            jeda()

def register():
    try:
        username = input("Username baru: ").strip()
        password = input("Password baru: ").strip()
        if username == "" or password == "":
            raise ValueError("Username dan password tidak boleh kosong!")
        if username in users:
            raise ValueError("Username sudah dipakai!")
    except ValueError as e:
        print(e)
    else:
        users[username] = {"password": password, "role": "user"}
        print("Register berhasil, silakan login.")
    finally:
        jeda()

def menu_awal():
    global jalan
    bersihkan_layar()
    print("=== SISTEM DATA KARYAWAN ===")
    print("1. Login\n2. Register\n0. Keluar")
    pilih = input("Pilih: ").strip()

    if pilih == "1":
        login()
    elif pilih == "2":
        register()
    elif pilih == "0":
        jalan = False
    else:
        print("Pilihan tidak valid!")
        jeda()

def menu_utama():
    global user_aktif
    bersihkan_layar()
    role = users[user_aktif]["role"]
    print(f"=== MENU ({user_aktif} - {role}) ===")
    if role == "admin":
        print("1. Tambah\n2. Lihat Karyawan\n3. Ubah\n4. Hapus")
    else:
        print("1. Lihat Karyawan")
    print("0. Logout")
    pilih = input("Pilih: ").strip()

    if pilih == "0":
        user_aktif = None
    elif role == "user" and pilih == "1":
        lihat_karyawan()
    elif role == "admin" and pilih == "1":
        tambah_karyawan()
    elif role == "admin" and pilih == "2":
        lihat_karyawan()
    elif role == "admin" and pilih == "3":
        ubah_karyawan()
    elif role == "admin" and pilih == "4":
        hapus_karyawan()
    else:
        print("Pilihan tidak valid!")
        jeda()

if __name__ == "__main__":
    while jalan:
        if user_aktif is None:
            menu_awal()
        else:
            menu_utama()

    bersihkan_layar()
    print("Terima kasih!")