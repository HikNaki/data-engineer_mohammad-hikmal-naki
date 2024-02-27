#Program Luas Persegi Panjang
print("Program Even dan Odd Rectangle")
p = int(input("Input panjang: "))
l = int(input("Input lebar: "))

L = p * l
if L % 2 == 0 :
    print("Even Rectangle")
else:
    print("Odd Rectangle")