print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~~~~~")
print()
print("<PROGRAM SEGITIGA ANGKA>")
print()
def cetak_segitiga(tinggi):

    if tinggi <= 0 or not isinstance(tinggi,int):
        print("tinggi segitiga harus bilangan bulat positif")
    else :   
        for i in range(1, tinggi + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

tinggi = int(input("Masukkan tinggi segitiga : "))
print()
try:
   tinggi_segitiga = int(tinggi)
   cetak_segitiga(tinggi)
except ValueError:
    print("tinggi segitiga harus bilangan bulat positif")

print()