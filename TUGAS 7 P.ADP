print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~~~~~")
print()
print("<PROGRAM FUNCTION>")
print()
print("Menu Pilihan:")
print("1. Tambah Kegiatan")
print("2. Hapus Kegiatan")
print("3. selesai")

jadwal = []

def menambahkan_kegiatan():
    keterangan = input("keterangan: ")
    jammulai = input("Input Jam Mulai: ")
    jamselesai = input("Input Jam Selesai: ")
    jadwal.append([keterangan, jammulai, jamselesai])
    print()
    print("JADWAL DITAMBAHKAN!!!!!!!!")
    print()
    return jadwal

def menghapus_kegiatan():
    if not jadwal:
        print("TIDAK ADA JADWAL")
    else:
        print("JADWAL HARIAN ANDA:")
        print("=" * 51)
        print("| NO |    KETERANGAN    | JAM MULAI | JAM SELESAI |")
        print("=" * 51)
        for i in range(len(jadwal)):
            kolom = jadwal[i]
            print(f"| {i+1}  | {kolom[0]}            | {kolom[1]}     | {kolom[2]}       |")
            print("=" * 51)
        hapuskegiatan = int(input("no. kegiatan yang dihapus: ")) - 1
        if hapuskegiatan < len(jadwal):
            jadwal2 = jadwal[:hapuskegiatan] + jadwal[hapuskegiatan+1:]
            print("KEGIATAN DIHAPUS!!!!!!!!")
            jadwal[:] = jadwal2
            menampilkan_jadwal()
        else:
            print("!!NO. KEGIATAN TIDAK ADA!!")
    return jadwal

def menampilkan_jadwal():
    if len(jadwal) == 0:
        print("Jadwal harian kosong.")
    else:
        print("JADWAL HARIAN ANDA:")
        print("=" * 51)
        print("| NO |    KETERANGAN    | JAM MULAI | JAM SELESAI |")
        print("=" * 51)
        for i in range(len(jadwal)):
            kolom = jadwal[i]
            print(f"| {i+1}  | {kolom[0]}            | {kolom[1]}     | {kolom[2]}       |")
            print("=" * 51)
    return jadwal

while True:
    print()
    pilihan = input("Input Pilihan: ")
    print()

    if pilihan == "1":
        menambahkan_kegiatan()
        menampilkan_jadwal()
    elif pilihan == "2":
        menghapus_kegiatan()
    elif pilihan == "3":
        break
    else:
        print("PILIHAN TIDAK TERSEDIA")
     
