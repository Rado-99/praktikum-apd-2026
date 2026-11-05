import os

from colorama import Fore, init
from prettytable import PrettyTable

import storage

init(autoreset=True)

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input(Fore.CYAN + "Tekan Enter untuk lanjut...")

def format_rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")

def pesan_sukses(teks):
    print(Fore.GREEN + str(teks))

def pesan_error(teks):
    print(Fore.RED + str(teks))

def pesan_info(teks):
    print(Fore.YELLOW + str(teks))

def tampilkan_menu(judul, daftar_menu):
    """Menampilkan menu dalam bentuk tabel. daftar_menu berisi pasangan (nomor, nama)."""
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"
    for nomor, nama in daftar_menu:
        tabel.add_row([nomor, nama])
    print(tabel)

def tampilkan_tabel_karyawan():
    tabel = PrettyTable()
    tabel.title = "DATA KARYAWAN"
    tabel.field_names = ["ID", "Nama", "Jabatan", "Gaji"]
    tabel.align["Nama"] = "l"
    tabel.align["Jabatan"] = "l"
    tabel.align["Gaji"] = "r"
    for id_k, k in storage.karyawan.items():
        tabel.add_row([id_k, k["nama"], k["jabatan"], format_rupiah(k["gaji"])])
    print(tabel)

def tampilkan_daftar_singkat():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama"]
    tabel.align["Nama"] = "l"
    for id_k, k in storage.karyawan.items():
        tabel.add_row([id_k, k["nama"]])
    print(tabel)