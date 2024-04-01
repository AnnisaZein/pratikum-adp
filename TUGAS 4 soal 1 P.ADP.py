print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~~~~~")
print()
print("<BILANGAN SEMPURNA>")
print()

def bilangan_sempurna(n):
    factors_sum = sum([i for i in range(1, n) if n % i == 0])
    return factors_sum == n

def is_even_or_odd(n):
    return n % 2 == 0

angka = int(input("Masukkan bilangan bulat positif : "))

if bilangan_sempurna(angka):
    print(f"{angka} adalah bilangan sempurna.")
else:
    print(f"{angka} bukan bilangan sempurna.")

if is_even_or_odd(angka):
    print(f"{angka} adalah bilangan genap.")
else:
    print(f"{angka} adalah bilangan ganjil.")
print()