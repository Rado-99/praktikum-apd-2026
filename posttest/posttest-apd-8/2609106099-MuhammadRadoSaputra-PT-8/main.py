import storage
from autentikasi import login, register
from create import tambah_karyawan
from delete import hapus_karyawan
from menu import bersihkan_layar, jeda, pesan_error, tampilkan_menu
from read import lihat_karyawan
from update import ubah_karyawan

user_aktif = None
jalan = True

def proses_menu_awal():
    global user_aktif, jalan
    bersihkan_layar()
    tampilkan_menu("SISTEM DATA KARYAWAN", [("1", "Login"), ("2", "Register"), ("0", "Keluar")])
    pilih = input("Pilih: ").strip()

    if pilih == "1":
        user_aktif = login()
    elif pilih == "2":
        register()
    elif pilih == "0":
        jalan = False
    else:
        pesan_error("Pilihan tidak valid!")
        jeda()

def proses_menu_utama():
    global user_aktif
    bersihkan_layar()
    role = storage.users[user_aktif]["role"]
    if role == "admin":
        daftar_menu = [("1", "Tambah Karyawan"), ("2", "Lihat Karyawan"),
                    ("3", "Ubah Karyawan"), ("4", "Hapus Karyawan"), ("0", "Logout")]
    else:
        daftar_menu = [("1", "Lihat Karyawan"), ("0", "Logout")]
    tampilkan_menu(f"MENU ({user_aktif} - {role})", daftar_menu)
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
        pesan_error("Pilihan tidak valid!")
        jeda()


if __name__ == "__main__":
    while jalan:
        if user_aktif is None:
            proses_menu_awal()
        else:
            proses_menu_utama()

    bersihkan_layar()
    print("Terima kasih!")