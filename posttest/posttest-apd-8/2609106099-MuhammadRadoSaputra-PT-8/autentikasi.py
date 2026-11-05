import pwinput

import storage
from menu import jeda, pesan_error, pesan_sukses

def cek_login(username, password):
    return username in storage.users and storage.users[username]["password"] == password

def login():
    user_masuk = None
    try:
        username = input("Username: ").strip()
        password = pwinput.pwinput("Password:").strip()
        if not cek_login(username, password):
            raise ValueError("Username atau password salah!")
    except ValueError as e:
        pesan_error(e)
    else:
        user_masuk = username
        pesan_sukses(f"Login berhasil. Selamat datang, {username}!")
    finally:
        jeda()
    return user_masuk

def register():
    try:
        username = input("Username baru: ").strip()
        password = pwinput.pwinput("Password baru:").strip()
        if username == "" or password == "":
            raise ValueError("Username dan password tidak boleh kosong!")
        if username in storage.users:
            raise ValueError("Username sudah dipakai!")
    except ValueError as e:
        pesan_error(e)
    else:
        storage.users[username] = {"password": password, "role": "user"}
        pesan_sukses("Register berhasil, silakan login.")
    finally:
        jeda()