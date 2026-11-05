import storage
from menu import jeda, pesan_error, pesan_sukses, tampilkan_daftar_singkat

def ubah_karyawan():
    try:
        tampilkan_daftar_singkat()
        id_ubah = storage.baca_id()
        print("Kosongkan (Enter) jika tidak diubah.")
        nama = input("Nama baru    : ").strip()
        jabatan = input("Jabatan baru : ").strip()
        gaji_teks = input("Gaji baru    : ").strip()
        gaji_baru = storage.validasi_gaji(gaji_teks) if gaji_teks != "" else None
    except KeyError:
        pesan_error("ID tidak ditemukan!")
    except ValueError as e:
        pesan_error(f"{e} Perubahan dibatalkan.")
    else:
        if nama != "":
            storage.karyawan[id_ubah]["nama"] = nama
        if jabatan != "":
            storage.karyawan[id_ubah]["jabatan"] = jabatan
        if gaji_baru is not None:
            storage.karyawan[id_ubah]["gaji"] = gaji_baru
        pesan_sukses("Data berhasil diubah.")
    finally:
        jeda()