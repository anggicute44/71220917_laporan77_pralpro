# suhu = 36 #inputan
# if suhu > 30: #kondisi 1
#     if suhu > 35:# kondisi 2
#         print("Sangat Panas")
#     else:
#         print("Panas")
# else:
#     print("Sejuk atau Dingin")


######################UG1###########################################

def capitalH(baris, kolom):
    # Validasi kondisi baris dan kolom
    if baris < 3 or kolom < 3 or baris % 2 == 0:
        print("dimensi tidak sesuai")
        return
    
    tengah = baris // 2  # Menentukan baris tengah untuk garis horizontal
    
    for i in range(baris):
        for j in range(kolom):
            # Cetak "#" di kolom pertama dan terakhir
            if j == 0 or j == kolom - 1:
                print("#", end="")
            # Cetak "#" di baris tengah untuk membuat garis horizontal
            elif i == tengah:
                print("#", end="")
            else:
                print(" ", end="")  # Spasi untuk bagian kosong dalam huruf H
        print()  # Pindah ke baris berikutnya

# Contoh Penggunaan
capitalH(5, 4)

##################################################UG2#########################################

def polaular(angka):
    if angka <= 0:
        print("tidak terdefinisikan")
        return
    
    nilai = 1
    for i in range(angka):
        if i % 2 == 0:
            # Jika baris genap (0, 2, 4, ...), cetak dari kecil ke besar
            for j in range(angka):
                print(f"{nilai:02}", end=" ")
                nilai += 1
        else:
            # Jika baris ganjil (1, 3, 5, ...), cetak dari besar ke kecil
            nilai += angka - 1
            for j in range(angka):
                print(f"{nilai:02}", end=" ")
                nilai -= 1
            nilai += angka + 1  # Mengatur nilai agar tetap berurutan
        print()  # Pindah ke baris baru

# Contoh penggunaan
polaular(4)
polaular(5)
polaular(0)
###############################################################################################


def tampilkan_kursi(rows, cols, booked_seats):
    for i in range(1, rows + 1):  # Loop baris
        for j in range(1, cols + 1):  # Loop kolom
            if (i, j) in booked_seats:  # Cek apakah kursi dipesan
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()  # Pindah ke baris baru

# Pemanggilan fungsi dengan kursi yang dipesan (2,9) dan (3,1)
tampilkan_kursi(5, 9, [(2, 9), (3, 1)])


#################################################################
def tampilkan_kursi(rows, cols, booked_seats=[]):
    for i in range(1, rows + 1):  # Loop baris
        for j in range(1, cols + 1):  # Loop kolom
            if j in [2, 3]:  # Kursi nomor 2 dan 3 di setiap baris
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()  # Pindah ke baris baru
    print()  # Spasi antar pemanggilan fungsi

# Pemanggilan fungsi untuk memesan kursi nomor 2 dan 3 di semua baris (5x5)
tampilkan_kursi(5, 5)

##################################################################################################
def pola_anyaman(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:  # Pola silang
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()  # Pindah ke baris baru
    print()  # Spasi antar pemanggilan fungsi

# Contoh pemanggilan untuk pola anyaman 7x7
pola_anyaman(7, 7)
#########################################################################################3333
def pola_bulat(size):
    r = size // 2  # Jari-jari lingkaran
    for i in range(size):
        for j in range(size):
            # Gunakan formula lingkaran: (x - r)^2 + (y - r)^2 <= r^2
            if (i - r) ** 2 + (j - r) ** 2 <= r ** 2:
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()  # Pindah ke baris baru
    print()  # Spasi antar pemanggilan fungsi

# Contoh pemanggilan untuk pola lingkaran ukuran 11x11
pola_bulat(11)
######################################################################################################3
def pola_love(size=11):
    for i in range(size):  # Loop baris
        for j in range(size):  # Loop kolom
            # Persamaan untuk membentuk hati
            if (
                ((i == 0 and j % (size - 1) != 0) or  # Bagian atas hati
                (i == 1 and j in [1, size - 2]) or  # Lengkungan hati
                (i - j == 2 or i + j == size + 2))  # Segitiga bawah hati
            ):
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()  # Pindah ke baris baru
    print()  # Spasi antar pemanggilan fungsi

# Pemanggilan fungsi untuk membuat pola love
pola_love()
#############################################################################################################3

def segitiga_ganjil(n):
    num = 1  # Bilangan ganjil pertama
    for i in range(1, n + 1):  # Loop baris
        for j in range(i):  # Loop kolom
            print(num, end=" ")
            num += 2  # Increment ke bilangan ganjil berikutnya
        print()  # Pindah ke baris baru

# Contoh pemanggilan untuk segitiga bilangan ganjil dengan tinggi 5
segitiga_ganjil(5)
###############################################################################################
def segitiga_samakaki_ganjil(n):
    num = 1  # Mulai dari angka ganjil pertama
    for i in range(1, n + 1):  # Loop baris
        print(" " * (n - i), end="")  # Spasi untuk menyusun segitiga simetris
        for j in range(2 * i - 1):  # Loop angka di setiap baris
            print(num, end=" ")
            num += 2  # Tambah angka ganjil berikutnya
        print()  # Pindah ke baris baru

# Contoh pemanggilan dengan tinggi 5
segitiga_samakaki_ganjil(5)
############################################################################################################
def segitiga_samakaki_genap(n):
    num = 2  # Mulai dari angka genap pertama
    for i in range(1, n + 1):  # Loop baris
        print(" " * (n - i), end="")  # Spasi untuk membuat segitiga simetris
        for j in range(2 * i - 1):  # Loop angka di setiap baris
            print(num, end=" ")
            num += 2  # Tambah angka genap berikutnya
        print()  # Pindah ke baris baru

# Contoh pemanggilan dengan tinggi 5
segitiga_samakaki_genap(5)
#######################################################################################################
def segitiga_genap(n):
    num = 2  # Bilangan genap pertama
    for i in range(1, n + 1):  # Loop baris
        for j in range(i):  # Loop kolom
            print(num, end=" ")
            num += 2  # Increment ke bilangan genap berikutnya
        print()  # Pindah ke baris baru

# Contoh pemanggilan untuk segitiga bilangan genap dengan tinggi 5
segitiga_genap(5)

