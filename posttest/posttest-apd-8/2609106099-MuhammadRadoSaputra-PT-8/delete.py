import storage
from menu import jeda, pesan_error, pesan_sukses, tampilkan_daftar_singkat

def hapus_karyawan():
    try:
        tampilkan_daftar_singkat()
        id_hapus = storage.baca_id()
    except KeyError:
        pesan_error("ID tidak ditemukan!")
    except ValueError as e:
        pesan_error(e)
    else:
        del storage.karyawan[id_hapus]
        pesan_sukses("Data berhasil dihapus.")
    finally:
        jeda()