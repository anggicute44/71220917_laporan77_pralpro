#############
def spiral(n):
    mat = [[0] * n for _ in range(n)]
    num, top, left, bottom, right = 1, 0, 0, n - 1, n - 1

    while num <= n * n:
        for i in range(left, right + 1):  # Kanan
            mat[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):  # Bawah
            mat[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):  # Kiri
            mat[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):  # Atas
            mat[i][left] = num
            num += 1
        left += 1

    for row in mat:
        print(" ".join(str(x).rjust(2) for x in row))

# Contoh pemanggilan
spiral(5)

###########################################################################
def belah_ketupat(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)

# Contoh pemanggilan
belah_ketupat(7)
############################################################
def tangga_ganjil(n):
    angka = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(angka, end=" ")
            angka += 2  # Hanya bilangan ganjil
        print()

# Contoh pemanggilan
tangga_ganjil(5)
############################################################################
def papan_catur(n, char1, char2):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print(char1, end=" ")
            else:
                print(char2, end=" ")
        print()

# Contoh pemanggilan
papan_catur(6, "*", "#")
##################################################################################
def pola_zigzag(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print("#" * i)
        else:
            print("*" * i)

# Contoh pemanggilan
pola_zigzag(5)
##########################################################
def segitiga_terbalik(n, angka_awal):
    for i in range(n, 0, -1):
        for j in range(i):
            print(angka_awal, end=" ")
        print()
        angka_awal += 1  # Meningkatkan angka setiap baris

# Contoh pemanggilan
segitiga_terbalik(5, 3)
###############################################################
def segitiga_terbalik():
    n = 5
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

segitiga_terbalik()
#############################################################################
def piramida_angka():
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i), end="")  # Spasi untuk perataan tengah
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

piramida_angka()

########################################################################

def matriks_checkerboard():
    n = 6
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()

matriks_checkerboard()
###########################################################
def matriks_X():
    n = 5
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()

matriks_X()
#########################
def segitiga_pascal():
    baris = 5
    for i in range(baris):
        angka = 1
        for j in range(i + 1):
            print(angka, end=" ")
            angka = angka * (i - j) // (j + 1)
        print()

segitiga_pascal()


###################################################################
def matriks_segitiga():
    angka = 1
    for i in range(5, 0, -1):
        for j in range(i):
            print(angka, end=" ")
            angka += 1
        print()

matriks_segitiga()



#Menampilkan Deret Faktorial & Penurunan Angka
import math

def tampilkan_deret(n):
    for i in range(n, 0, -1):
        faktorial = math.factorial(i)
        print(faktorial, end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()  # Pindah ke baris berikutnya

# Nilai n ditentukan langsung
n = 6  
tampilkan_deret(n)
############################################################################################
#Menampilkan Matriks Angka
def tampilkan_matriks(tinggi, lebar):
    angka = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(angka, end=" ")
            angka += 1
        print()  # Pindah ke baris berikutnya

# Nilai tinggi dan lebar ditentukan langsung
tinggi = 5  # Ganti sesuai keinginan
lebar = 4   # Ganti sesuai keinginan

tampilkan_matriks(tinggi, lebar)


#################################################
def kotak_spiral(n):
    angka = 1
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print(angka, end=" ")
            else:
                print(" ", end=" ")
        angka += 1
        print()

# Contoh pemanggilan
kotak_spiral(5)
###########################################################
def diamond(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Contoh pemanggilan
diamond(7)
##########################################################################################
def zigzag(n):
    for i in range(1, n + 1):
        if i % 2 == 1:  # Baris ganjil: urut ke kanan
            for j in range(1, n + 1):
                print(j, end=" ")
        else:  # Baris genap: urut ke kiri
            for j in range(n, 0, -1):
                print(j, end=" ")
        print()

# Contoh pemanggilan
zigzag(5)
############################################################################
def pola_huruf(n):
    huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indeks = 0
    for i in range(1, n + 1):
        for j in range(i):
            print(huruf[indeks % 26], end=" ")
            indeks += 1
        print()

# Contoh pemanggilan
pola_huruf(5)
###########################################################################

def segitiga_pascal(n):
    for i in range(n):
        angka = 1
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print(angka, end=" ")
            angka = angka * (i - j) // (j + 1) if j < i else 1
        print()

# Contoh pemanggilan
segitiga_pascal(6)








############################################################################################
def piramida_terbalik(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            print(j, end=" ")
        print()

# Contoh pemanggilan
piramida_terbalik(5)






############################################################################################