# 1.Validasi login
masukkan_nama_panggilan = input("Masukkan nama panggilan: ")
masukkan_nim = input("Masukkan NIM: ")
if masukkan_nama_panggilan == "Rado" and masukkan_nim == "99":
    print("Login berhasil!")
else:
    print("Login gagal! Silahkan coba lagi.")
    exit()

# 2.Pilih jenis konsol
harga_konsol = [10000, 15000, 20000]

PS4 = harga_konsol[0]
PS4Pro = harga_konsol[1]
PS5 = harga_konsol[2]

print("=== Pilih Jenis Konsol ===")
print("1. PS4     : Rp 10.000/jam")
print("2. PS4 Pro : Rp 15.000/jam")
print("3. PS5     : Rp 20.000/jam")

pilihan = int(input("Pilih konsol (1-3): "))
if pilihan == 1:
    jenis_konsol = "PS4"
    harga_per_jam = PS4
elif pilihan == 2:
    jenis_konsol = "PS4 Pro"
    harga_per_jam = PS4Pro
elif pilihan == 3:
    jenis_konsol = "PS5"
    harga_per_jam = PS5
else:
    print("Pilihan tidak benar.")
    exit()

jumlah_jam = int(input("Masukkan jumlah jam sewa: "))

# 3.Diskon
if jumlah_jam >= 5:
    persen_diskon = 0.08
elif jumlah_jam >= 3:
    persen_diskon = 0.05
else:
    persen_diskon = 0

# 4.Total harga dan total bayar
total_harga = harga_per_jam * jumlah_jam
diskon_sewa = persen_diskon * total_harga

# 5.Waktu sewa
waktu_sewa = input("apakah sewa dilakukan saat weekend? (ya/tidak): ")
if waktu_sewa == "ya":
    biaya_weekend = 0.10 * total_harga
else:
    biaya_weekend = 0
total_bayar = total_harga - diskon_sewa + biaya_weekend

# 6.Hasil output
print("=====================")
print("Nama          :", masukkan_nama_panggilan)
print("NIM           :", masukkan_nim)
print("Jenis Konsol  :", jenis_konsol)
print("Jumlah Jam    :", jumlah_jam, "jam")
print("Total Harga   : Rp", total_harga)
print("Diskon Sewa   : Rp", diskon_sewa)
print("Total Bayar   : Rp", total_bayar)