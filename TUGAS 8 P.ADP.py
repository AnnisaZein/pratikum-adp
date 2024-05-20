print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~~~~~")
print()
print("<<PROGRAM DICTIONARY DAN TEXT FILE>>")
print()
print("[1. SIMPAN DATA]")
print("[2. HAPUS DATA]")
print("[3. TAMPILKAN DATA]")
print("[4. KELUAR]")


def simpan() :
    with open("data.txt", "a") as file :
        file.write("\n")
        for key, value in data.items() :
            file.write(f"{key:<17}: {value}\n")
    print("__DATA TELAH TERSIMPAN__")

def hapus() :
    nama = input("NAMA PASIEN : ")
    print("Hapus data pasien", "[", nama, "]")
    with open("data.txt", "r") as file :
        a = file.readline()
    with open("data.txt", "w") as file :
        for baris in a :
            if nama in baris :
                del line
                print()
                print("__DATA TELAH DIHAPUS__")
            else:
                print()
                print("nama tidak ditemukan")


def tampil() :
    with open("data.txt", "r") as file :
        print()
        print("Data-data Pasien:")
        print(file.read())


while True :
    print()
    pilihan = input("KETIK PILIHAN ANDA : ")

    if pilihan == "1" :
        nama = input("NAMA             : ")
        umur = input("UMUR             : ")
        jenis_kelamin = input("JENIS KELAMIN    : ")
        gol_darah = input("GOL. DARAH       : ")
        riwayat_penyakit = input("RIWAYAT PENYAKIT : ")
        daftar_obat = input("DAFTAR OBAT      : ")

        data = {
                "nama": nama,
                "umur": umur,
                "jenis Kelamin": jenis_kelamin,
                "golongan Darah": gol_darah,
                "riwayat Penyakit": riwayat_penyakit,
                "daftar Obat": daftar_obat
                }   
        print()
        simpan()

    elif pilihan == "2" :
        hapus()
    elif pilihan == "3" :
        tampil()
    elif pilihan == "4" :
        break
    else :
        print("__tidak ada pilihan__")

 