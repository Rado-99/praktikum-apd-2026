import storage
from menu import jeda, pesan_error, pesan_sukses

def tambah_karyawan():
    try:
        nama = input("Nama    : ").strip()
        jabatan = input("Jabatan : ").strip()
        gaji_teks = input("Gaji    : ").strip()
        if nama == "" or jabatan == "":
            raise ValueError("Nama dan jabatan tidak boleh kosong!")
        gaji = storage.validasi_gaji(gaji_teks)
    except ValueError as e:
        pesan_error(e)
    else:
        storage.karyawan[storage.buat_id_baru()] = {"nama": nama, "jabatan": jabatan, "gaji": gaji}
        pesan_sukses("Data berhasil ditambahkan.")
    finally:
        jeda()