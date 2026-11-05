users = {
    "admin": {"password": "admin123", "role": "admin"},
    "rado": {"password": "rado123", "role": "user"},
}

karyawan = {
    1: {"nama": "Andi Pratama", "jabatan": "Manager", "gaji": 12000000},
    2: {"nama": "Ahmad Rizki", "jabatan": "Staff", "gaji": 6000000},
    3: {"nama": "Rudi", "jabatan": "Programmer", "gaji": 8000000},
}

def buat_id_baru():
    """Mengembalikan ID baru untuk karyawan."""
    if len(karyawan) == 0:
        return 1
    return max(karyawan) + 1

def validasi_gaji(teks):
    """Memvalidasi input gaji, mengembalikan gaji dalam bentuk int."""
    if not teks.isdecimal():
        raise ValueError("Gaji harus berupa angka bulat!")
    gaji = int(teks)
    if gaji <= 0:
        raise ValueError("Gaji harus lebih dari 0!")
    return gaji

def baca_id():
    """Meminta ID dari user, memvalidasi, lalu mengembalikan ID (int)."""
    teks = input("ID karyawan: ").strip()
    if not teks.isdecimal():
        raise ValueError("ID harus berupa angka!")
    id_k = int(teks)
    if id_k not in karyawan:
        raise KeyError(id_k)
    return id_k