print()
nama    = "NABILLA"
nim     = "2310431014"
PROGRAM = "<PROGRAM PEMESANAN MENU>"
print('~~~~~~~~~~~~~~~~~~')
print("NAMA = " + nama)
print("NIM  = " + nim)
print('~~~~~~~~~~~~~~~~~~')
print()
print(PROGRAM)
print()
print("JENIS MENU : ")
print("1. MAKANAN")
print("2. MINUMAN")
print("3. MAKANAN DAN MINUMAN")
print()
h1 = "====================================="
jenis1 = "|         DAFTAR MENU MAKANAN       |"
h2 = "|===================================|"
m1 = "| 1. Nasi Goreng     | Rp 18.000,00 |"
m2 = "| 2. Mie Goreng      | Rp 18.000,00 |"
m3 = "| 3. Nasi Ayam Goreng| Rp 20.000,00 |"
h4 = "====================================="
h5 = "====================================="
jenis2 = "|         DAFTAR MENU MINUMAN       |"
h6 = "|===================================|"
m11 = "| 1. Teh Es         | Rp 5.000,00   |"
m22 = "| 2. Es Jeruk       | Rp 6.000,00   |"
m33 = "| 3. Aqua           | Rp 4.000,00   |"
h7 = "====================================="

menu = int(input('Jenis Menu Yang Dipilih : '))
print()
if menu == 1 :
    print(h1)
    print(jenis1)
    print(h2)
    print(m1)
    print(m2)
    print(m3)
    print(h4)
    pesan = "MENU PESANAN"
    print()
    pesanan = float(input('Nomor menu yang dipesan = '))
    print()
    if pesanan == 1  :
        print(pesan)
        print(m1)
        jumlah = int(input("| JUMLAH              | = "))
        p1 = 18 * jumlah
        print()
        print("TOTAL HARGA =", p1, "ribu")
        print()
    elif pesanan == 2 :
        print(pesan)
        print(m2)
        jumlah = int(input("| JUMLAH              | = "))
        p1 = 18 * jumlah
        print()
        print("TOTAL HARGA =", p1, "ribu")
        print()
    elif pesanan == 3 :
        print(pesan)
        print(m3)
        jumlah = int(input("| JUMLAH              | = "))
        p2 = 20 * jumlah
        print()
        print("TOTAL HARGA =", p2, "ribu")
        print()
    elif pesanan ==  12 :
        print(pesan)
        print(m1)
        jumlah1 = int(input("| JUMLAH             | = "))
        print(m2)
        jumlah2 = int(input("| JUMLAH             | = "))
        p1 = 18 * jumlah1
        p3 = 18 * jumlah2
        total = p1 + p3
        print()
        print("TOTAL HARGA =", total, "ribu")
        print()
    elif pesanan ==  13 :
        print(pesan)
        print(m1)
        jumlah1 = int(input("| JUMLAH             | = "))
        print(m3)
        jumlah3 = int(input("| JUMLAH             | = "))
        p1 = 18 * jumlah1
        p4 = 20 * jumlah3
        total = p1 + p4
        print()
        print("TOTAL HARGA =", total, "ribu")
        print()
    elif pesanan ==  23 :
        print(pesan)
        print(m2)
        jumlah1 = int(input("| JUMLAH             | = "))
        print(m3)
        jumlah3 = int(input("| JUMLAH             | = "))
        p1 = 18 * jumlah1
        p4 = 20 * jumlah3
        total = p1 + p4
        print()
        print("TOTAL HARGA =", total, "ribu")
        print()
    elif pesanan == 123 :
        print(pesan)
        print(m1)
        jumlah1 = int(input("| JUMLAH             | = ")) 
        print(m2)
        jumlah2 = int(input("| JUMLAH             | = "))
        print(m3)
        jumlah3 = int(input("| JUMLAH             | = "))
        p1 = 18 * jumlah1
        p2 = 18 * jumlah2
        p3 = 20 * jumlah3
        total = p1 + p2 + p3
        print()
        print("TOTAL HARGA =",total, "ribu" )
        print()
    else :
        print("Tidak Valid")
elif menu == 2:
    print(h5)
    print(jenis2)
    print(h6)
    print(m11)
    print(m22)
    print(m33)
    print(h7)
    pesan = "MENU PESANAN"
    print()
    pesanan = float(input('PESANAN = '))
    print()
    if pesanan == 1  :
        print(pesan)
        print(m11)
        jumlah = int(input("| JUMLAH             | = "))
        p1 = 5 * jumlah
        print()
        print("TOTAL HARGA =", p1, "ribu")
        print()
    elif pesanan == 2 :
        print(pesan)
        print(m22)
        jumlah = int(input("| JUMLAH             | = "))
        p1 = 6 * jumlah
        print()
        print("TOTAL HARGA =", p1, "ribu")
        print()
    elif pesanan == 3 :
        print(pesan)
        print(m33)
        jumlah = int(input("| JUMLAH             | = "))
        p2 = 4 * jumlah
        print()
        print("TOTAL HARGA =", p2, "ribu")
        print()
    elif pesanan ==  12 :
        print(pesan)
        print(m11)
        jumlah1 = int(input("| JUMLAH            | = "))
        print(m22)
        jumlah2 = int(input("| JUMLAH            | = "))
        p1 = 5 * jumlah1
        p3 = 6 * jumlah2
        total = p1 + p3
        print()
        print("TOTAL HARGA =", total, "ribu")
        print()
    elif pesanan ==  13 :
        print(pesan)
        print(m11)
        jumlah1 = int(input("| JUMLAH            | = "))
        print(m33)
        jumlah3 = int(input("| JUMLAH            | = "))
        p1 = 5 * jumlah1
        p4 = 4 * jumlah3
        total = p1 + p4
        print()
        print("TOTAL HARGA =", total, "ribu")
        print()
    elif pesanan ==  23 :
        print(pesan)
        print(m22)
        jumlah1 = int(input("| JUMLAH            | = "))
        print(m33)
        jumlah4 = int(input("| JUMLAH            | = "))
        p5 = 6 * jumlah1
        p6 = 4 * jumlah4
        total = p5 + p6
        print("TOTAL HARGA =", total, "ribu")
        print()
    elif pesanan == 123 :
        print(pesan)
        print(m11)
        jumlah1 = int(input("| JUMLAH            | = "))
        print(m22)
        jumlah2 = int(input("| JUMLAH            | = "))
        print(m33)
        jumlah3 = int(input("| JUMLAH            | = "))
        p1 = 5 * jumlah1
        p2 = 6 * jumlah2
        p3 = 4 * jumlah3
        total = p1 + p2 + p3
        print()
        print("TOTAL HARGA =", total, "ribu")
        print()
    else :
        print("Tidak Valid")

elif menu == 3:
    print(h1)
    print(jenis1)
    print(h2)
    print(m1)
    print(m2)
    print(m3)
    print(h4)
    print()
    print(h5)
    print(jenis2)
    print(h6)
    print(m11)
    print(m22)
    print(m33)
    print(h7)
    print()
    pesanan = float(input('MENU MAKANAN = '))
    if pesanan == 1  :
        jumlah = int(input("JUMLAH      = "))
        p1 = 18 * jumlah
        total1 = p1
        print()
    elif pesanan == 2 :
        jumlah = int(input("JUMLAH      = "))
        p1 = 18 * jumlah
        total1 = p1
        print()
    elif pesanan == 3 :
        jumlah = int(input("JUMLAH      = "))
        p2 = 20 * jumlah
        total1 = p2
        print()
    elif pesanan ==  12 :
        jumlah1 = int(input("JUMLAH 1     = "))
        jumlah2 = int(input("JUMLAH 2     = "))
        p1 = 18 * jumlah1
        p3 = 18 * jumlah2
        total1 = p1 + p3
        print()
    elif pesanan ==  13 :
        jumlah1 = int(input("JUMLAH 1     = "))
        jumlah3 = int(input("JUMLAH 3     = "))
        p1 = 18 * jumlah1
        p4 = 20 * jumlah3
        total1 = p1 + p4
        print()
    elif pesanan ==  23 :
        jumlah1 = int(input("JUMLAH 2     = "))
        jumlah3 = int(input("JUMLAH 3     = "))
        p1 = 18 * jumlah1
        p4 = 20 * jumlah3
        total1 = p1 + p4
        print()
    elif pesanan == 123 :
        jumlah1 = int(input("JUMLAH 1     = "))
        jumlah2 = int(input("JUMLAH 2     = "))
        jumlah3 = int(input("JUMLAH 3     = "))
        p1 = 18 * jumlah1
        p2 = 18 * jumlah2
        p3 = 20 * jumlah3
        total1 = p1 + p2 + p3
    else :
        print("Tidak Valid")
    pesanan = float(input('MENU MINUMAN = '))
    if pesanan == 1  :
        jumlah = int(input("JUMLAH      = "))
        p1 = 5 * jumlah
        total2 = p1
        print()
    elif pesanan == 2 :
        jumlah = int(input("JUMLAH      = "))
        p1 = 6 * jumlah
        total2 = p1
        print()
    elif pesanan == 3 :
        jumlah = int(input("JUMLAH      = "))
        p2 = 4 * jumlah
        total2 = p2
        print()
    elif pesanan ==  12 :
        jumlah1 = int(input("JUMLAH 1     = "))
        jumlah2 = int(input("JUMLAH 2     = "))
        p1 = 5 * jumlah1
        p3 = 6 * jumlah2
        total2 = p1 + p3
        print()
    elif pesanan ==  13 :
        jumlah1 = int(input("JUMLAH 1     = "))
        jumlah3 = int(input("JUMLAH 3     = "))
        p1 = 5 * jumlah1
        p4 = 4 * jumlah3
        tota2 = p1 + p4
        print()
    elif pesanan ==  23 :
        jumlah1 = int(input("JUMLAH 2     = "))
        jumlah4 = int(input("JUMLAH 3     = "))
        p5 = 6 * jumlah1
        p6 = 4 * jumlah4
        total2 = p5 + p6
        print()
    elif pesanan == 123 :
        jumlah1 = int(input("JUMLAH 1     = "))
        jumlah2 = int(input("JUMLAH 2     = "))
        jumlah3 = int(input("JUMLAH 3     = "))
        p1 = 5 * jumlah1
        p2 = 6 * jumlah2
        p3 = 4 * jumlah3
        total2 = p1 + p2 + p3
        print()
    else :
        print("Tidak Valid")
    TOTAL = total1 + total2
    print("TOTAL HARGA =", TOTAL, "ribu")
else :
    print("Kode Pesanan Tidak Valid")
print()