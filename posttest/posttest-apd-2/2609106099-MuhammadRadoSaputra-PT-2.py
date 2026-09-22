# 1.List harga merchandise
harga_merchandise = [45000, 50000, 60000, 75000, 90000, 120000]

merchandise_1 = harga_merchandise[0]
merchandise_2 = harga_merchandise[1]
merchandise_3 = harga_merchandise[2]
merchandise_4 = harga_merchandise[3]
merchandise_5 = harga_merchandise[4]
merchandise_6 = harga_merchandise[5]

# 2. Total harga 
biaya_kado = 7500
total_harga = (merchandise_1 + merchandise_2 + merchandise_3 +
merchandise_4 + merchandise_5 + merchandise_6 + biaya_kado)

# 3. Rata-rata 
rata_rata = total_harga / len(harga_merchandise)

# 4. NIM (2 digit terakhir)
nim = 99

# 5. Bolean: apakah nim > rata-rata
bolean = nim > rata_rata

# 6. Tampilkan semua variabel
print("Daftar harga merchandise :", harga_merchandise)
print("Merchandise 1            :", merchandise_1)
print("Merchandise 2            :", merchandise_2)
print("Merchandise 3            :", merchandise_3)
print("Merchandise 4            :", merchandise_4)
print("Merchandise 5            :", merchandise_5)
print("Merchandise 6            :", merchandise_6)
print("Total harga              :", total_harga)
print("Rata-rata                :", rata_rata)
print("NIM                      :", nim)
print("Apakah NIM > Rata-rata   :", bolean)

# --- Poin Plus ---

# Konversi total_harga ke USD 
kurs_usd = 17800
total_harga_usd = total_harga / kurs_usd
print("Total harga (USD)        :", total_harga_usd)

# Slice index negatif: tampilkan barang_2 hingga barang_4
barang_2_sampai_4 = harga_merchandise[-5:-2]
print("Barang 2 s/d 4 (slice neg):", barang_2_sampai_4)