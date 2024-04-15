print()
nama ="NABILLA"
nim = "2310431014"
print("~~~~~~~~~~~~~~~~~")
print("NAMA :" + nama)
print("NIM  :" + nim)
print("~~~~~~~~~~~~~~~~~")
print()
print("<PROGRAM CAESAR CIPHER>")
print()
def caesar_cipher(teks1, k):
    huruf = 'abcdefghijklmnopqrstuvwxyz'
    teks2 = ''
    
    for char in teks1:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if char in huruf:
                idx = (huruf.index(char) + k) % 26
                if is_upper:
                    teks2 += huruf[idx].upper()
                else:
                    teks2 += huruf[idx]
            else:
                teks2 += char
        else:
            teks2 += char
    
    return teks2

k = int(input("Masukkan nilai k : "))
teks1 = input("Teks awal: ")

teks2 = caesar_cipher(teks1, k)
print("Teks akhir: ", teks2)
print()