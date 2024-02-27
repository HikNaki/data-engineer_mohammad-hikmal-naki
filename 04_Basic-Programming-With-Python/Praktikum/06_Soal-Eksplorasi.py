print("Program memeriksa kata anagram")
def cek_anagram(kata1, kata2):
    frekuensi_kata1 = sorted(kata1)
    frekuensi_kata2 = sorted(kata2)
    
    if frekuensi_kata1 == frekuensi_kata2:
        return True
    else:
        return False

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("Anagram")
else:
    print("Bukan Anagram")
