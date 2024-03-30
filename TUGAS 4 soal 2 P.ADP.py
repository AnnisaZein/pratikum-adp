print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~~~~~")
print()
print("<program segitiga angka>")
print()
def cetak_segitiga(tinggi):
   for i in range(1, tinggi + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

tinggi = int(input("Masukkan tinggi segitiga : "))
print()
cetak_segitiga(tinggi)
print()