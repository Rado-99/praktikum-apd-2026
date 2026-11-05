import storage
from menu import format_rupiah, jeda, pesan_error, pesan_info, tampilkan_tabel_karyawan

def total_gaji(daftar_id):
    "Menjumlahkan gaji semua ID pada daftar_id secara rekursif."
    # Base case: daftar kosong
    if len(daftar_id) == 0:
        return 0
    # Recursive case: gaji pertama + total gaji sisanya
    return storage.karyawan[daftar_id[0]]["gaji"] + total_gaji(daftar_id[1:])

def lihat_karyawan():
    try:
        if len(storage.karyawan) == 0:
            raise ValueError("Belum ada data.")
        tampilkan_tabel_karyawan()
    except ValueError as e:
        pesan_error(e)
    else:
        pesan_info(f"Total gaji seluruh karyawan: {format_rupiah(total_gaji(list(storage.karyawan)))}")
    finally:
        jeda()