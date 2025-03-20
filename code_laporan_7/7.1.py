def is_prima(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prima_terdekat(n):
    for i in range(n-1, 1, -1):  # Mulai dari n-1 dan turun ke bawah
        if is_prima(i):
            return i
    return None  # Jika tidak ada bilangan prima yang ditemukan

# Input dari pengguna
n = int(input("Masukkan bilangan n: "))

# Mencari bilangan prima terdekat
hasil = prima_terdekat(n)

if hasil:
    print(f"Bilangan prima terdekat < {n} adalah {hasil}")
else:
    print("Tidak ada bilangan prima yang lebih kecil dari", n)
