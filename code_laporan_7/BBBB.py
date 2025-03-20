def tampilkan_kursi(teater):
    for baris in teater:
        print(" ".join(baris))
    print()

# Ukuran bioskop
baris, kolom = 4, 5
teater = [[f"{chr(65 + i)}{j+1}" for j in range(kolom)] for i in range(baris)]

print("\n=== Kursi Sebelum Pemesanan ===")
tampilkan_kursi(teater)

# Simulasi pemesanan kursi (tanpa input dari pengguna)
pemesanan_skenario = [
    ["A1", "B3", "C4"],  # Skenario 1
    ["A2", "A3", "D5"],  # Skenario 2
    ["B1", "C2", "C3", "D4"],  # Skenario 3
]

# Pilih skenario yang akan dijalankan
kursi_dipesan = pemesanan_skenario[1]  # Ganti indeks sesuai skenario yang diinginkan

# Tandai kursi yang sudah dipesan
for i in range(baris):
    for j in range(kolom):
        if teater[i][j] in kursi_dipesan:
            teater[i][j] = "[X]"

print("\n=== Kursi Setelah Pemesanan ===")
tampilkan_kursi(teater)
########################################################################################################

# Ukuran bioskop
baris, kolom = 4, 5

# Buat tampilan kursi awal
teater = [[f"{chr(65 + i)}{j+1}" for j in range(kolom)] for i in range(baris)]

# Tampilkan kursi sebelum pemesanan
print("\n=== Kursi Sebelum Pemesanan ===")
for row in teater:
    print(" ".join(row))

# Skenario kursi yang sudah dipesan (tanpa input)
kursi_dipesan = ["A1", "B3", "C4", "D5"]

# Tandai kursi yang sudah dipesan dengan "[X]"
for i in range(baris):
    for j in range(kolom):
        if teater[i][j] in kursi_dipesan:
            teater[i][j] = "[X]"

# Tampilkan kursi setelah pemesanan
print("\n=== Kursi Setelah Pemesanan ===")
for row in teater:
    print(" ".join(row))
######################################################################################################


def hitung_diskon(jumlah, harga_per_barang=10000):
    total_harga = jumlah * harga_per_barang

    # Menentukan diskon
    if jumlah <= 2:
        diskon_persen = 5
    elif jumlah <= 5:
        diskon_persen = 10
    else:
        diskon_persen = 20

    # Hitung harga setelah diskon
    diskon = total_harga * diskon_persen / 100
    harga_setelah_diskon = total_harga - diskon

    # Tampilkan hasil
    print(f"Beli {jumlah} barang, total harga: Rp{total_harga:,}, diskon {diskon_persen}%, bayar: Rp{harga_setelah_diskon:,}")

# Menampilkan hasil untuk berbagai jumlah barang
jumlah_barang_list = [1, 2, 3, 4, 5, 6, 7]
for jumlah in jumlah_barang_list:
    hitung_diskon(jumlah)


#####################################################################################################

