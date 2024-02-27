print("Program menentukan tarif pengiriman paket")

berat = int(input("Berat : "))
jarak = int(input("Jarak : "))

def tarif_berat(berat):
    if berat >= 1 and berat <= 20 :
        a = 10000
        return a
    elif berat >= 21 and berat <= 30 :
        a = 15000
        return a
    elif berat >= 31 and berat <= 60 :
        a = 20000
        return a
    elif berat > 60 :
        a = 45000
        return a
    
def tarif_jarak(jarak):
    if jarak >= 1 and jarak <= 5 :
        a = 2000
        return a
    elif jarak >= 6 and jarak <= 15 :
        a = 5000
        return a
    elif jarak >= 16 and jarak <= 30 :
        a = 10000
        return a
    elif jarak > 30 :
        a = 15000
        return a

tarif_keseluruhan = tarif_berat(berat) + tarif_jarak(jarak)

print(f"Tarif Keseluruhan : {tarif_keseluruhan}")

