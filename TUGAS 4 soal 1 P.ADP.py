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

def is_perfect_number(n):
    factors_sum = sum([i for i in range(1, n) if n % i == 0])
    return factors_sum == n

def is_even_or_odd(n):
    return n % 2 == 0

number = int(input("Masukkan bilangan bulat positif : "))

if is_perfect_number(number):
    print(f"{number} adalah bilangan sempurna.")
else:
    print(f"{number} bukan bilangan sempurna.")

if is_even_or_odd(number):
    print(f"{number} adalah bilangan genap.")
else:
    print(f"{number} adalah bilangan ganjil.")