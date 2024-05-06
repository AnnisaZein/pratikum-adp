print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~~~~~")
print()
print("<PROGRAM ARRAY DUA DIMENSI>")

#SOAL A
print()
jadwal_penerbangan = ([["NOMOR RUTE", "KOTA ASAL", "KOTA TUJUAN", "WAKTU KEBERANGKATAN", "WAKTU KEDATANGAN", "JARAK TEMPUH"],
                       ["1", "Jakarta", "Padang", "08:00", "09:00", "105 menit"],
                       ["2", "Padang", "Bali", "11:30", "13:15", "280 menit"],
                       ["3", "Bali", "Jakarta", "17:30", "18:00", "100 menit"]])

print("Jadwal Penerbangan :")
print()
print("-" * 96) 
for i in jadwal_penerbangan :
    print("{:10} | {:11} | {:12} | {:19} | {:16} | {:17} ".format(i[0], i[1], i[2], i[3], i[4], i[5]))
    if jadwal_penerbangan :
        print("-" * 96)
print()

#SOAL B
print("Rute Tercepat : //mohon masukkan secara berurutan")
print()
rute1 = int(input("RUTE PERTAMA : ")) 
rute2 = int(input("RUTE KEDUA   : "))
print()
if rute1 == 1 and rute2 == 2 :
    print("Rute tercepat adalah", jadwal_penerbangan[1][1], jadwal_penerbangan[1][2], "dengan jarak tempuh", jadwal_penerbangan[1][5])
elif rute1 == 1 and rute2 == 3 :
    print("Rute tercepat adalah", jadwal_penerbangan[3][1], jadwal_penerbangan[3][2], "dengan jarak tempuh", jadwal_penerbangan[3][5])
elif rute1 == 2 and rute2 == 3 :
    print("Rute tercepat adalah", jadwal_penerbangan[3][1], jadwal_penerbangan[3][2], "dengan jarak tempuh", jadwal_penerbangan[3][5])
else :
    print("RUTE TIDAK DITEMUKAN")
print()
