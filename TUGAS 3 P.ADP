print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~")
print()
print("MENU :")
print("1. TABEL PERKALIAN")
print("2. TABEL PENJUMLAHAN")
print("3. KELUAR")
print()

n = int(input("input nilai n (1 <= n <= 10) : "))
while (1 <= n <= 10):
    print()
    MENU = int(input("input menu yang dipilih : "))
    if MENU == 1 :
        print("TABEL PERKALIAN")
        print()
        for i in range (1, n+1):
            for j in range (1, n+1):
                print("|  ", i*j, end="\t")
            print()
    elif MENU == 2 :
        print("TABEL PENJUMLAHAN")
        print()
        for i in range (n+1):
            for j in range (n+1):
                print("|  ", i+j, end="\t")
            print()
    elif MENU == 3 :
        break
    else :
        print("input ulang menu")

else :
    n = int(input("input nilai n (1 <= n <= 10) : "))
while (1 <= n <= 10):
    exit()
    print()
    MENU = int(input("input menu yang dipilih : "))
    if MENU == 1 :
        print("TABEL PERKALIAN")
        print()
        for i in range (1, n+1):
            for j in range (1, n+1):
                print("|  ", i*j, end="\t")
            print()
    elif MENU == 2 :
        print("TABEL PENJUMLAHAN")
        print()
        for i in range (n+1):
            for j in range (n+1):
                print("|  ", i+j, end="\t")
            print()
    elif MENU == 3 :
        break
    else :
        print("input ulang menu")

