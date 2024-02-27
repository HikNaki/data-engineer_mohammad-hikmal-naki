# (4) Basic Programming With Python
### What is Python?
Python adalah bahasa pemrograman tingkat tinggi yang memiliki sintaksis yang sederhana dan mudah dipahami, serta digunakan secara luas dalam berbagai bidang . Python sering dijadikan bahasa pemrograman pertama bagi pemula karena sintaksisnya yang bersahabat dan mudah dipahami, serta tersedianya banyak sumber belajar daring dan buku yang mendukung proses pembelajaran.

### Variabel & Data Types
Variabel dalam Python digunakan sebagai wadah untuk menyimpan nilai atau data dalam program. Penggunaan variabel diawali dengan penamaan variabel yang bersifat deskriptif dan relevan dengan nilai yang akan disimpan.
Tipe data dalam Python :
1. `Numeric` : `Integer`, `Float`, & `Complex No`.
2. `Dictionary`
3. `Boolean`
4. `Set`
5. `Sequence` : `String`, `List`, & `Tuple`.

### Expression & Operator
Expression adalah kombinasi dari nilai, variabel, operator, dan panggilan fungsi yang dievaluasi untuk menghasilkan nilai tunggal. Operator, di sisi lain, adalah simbol atau karakter khusus yang digunakan untuk melakukan operasi tertentu pada operand. Berikut adalah beberapa contoh umum dari Expression dan Operators dalam Python:
1. Arithmetic Expressions : `2 + 3`
2. String Expressions : `'Hello' + ' ' + 'World'`
3. Arithmetic Operators :
```
+ (penjumlahan), - (pengurangan), * (perkalian), / (pembagian)
% (modulus), ** (pangkat), // (pembagian bulat)
```
4. Comparison Operators :
```
== (sama dengan), != (tidak sama dengan), < (kurang dari), > (lebih dari)
<= (kurang dari atau sama dengan), >= (lebih dari atau sama dengan)
```

### Control Structure Branching & Looping

Control Structures adalah konstruksi atau mekanisme yang memungkinkan pengendalian aliran eksekusi program. Mereka memungkinkan kita untuk mengontrol bagaimana dan kapan sebuah blok kode dieksekusi berdasarkan kondisi tertentu. Terdapat beberapa jenis control structures yang umum digunakan dalam Python:
1. Branching
```
if condition1:
    # Eksekusi jika condition1 benar
elif condition2:
    # Eksekusi jika condition1 salah dan condition2 benar
else:
    # Eksekusi jika kedua kondisi sebelumnya salah
```
2. Looping
```
for item in sequence:
# Eksekusi blok kode untuk setiap item dalam sequence
      
while condition:
# Eksekusi blok kode selama kondisi terpenuhi
```

### Function
Function adalah blok kode yang terorganisir dan dapat digunakan ulang yang dirancang untuk melakukan tugas tertentu. Function mengambil input (argumen), melakukan operasi tertentu, dan mengembalikan output (nilai kembalian) jika diperlukan. Berikut adalah contoh Function dalam Python:
```
def nama_fungsi(parameter1, parameter2):
    # Blok kode fungsi
    hasil = parameter1 + parameter2
    return hasil
```

### List
List adalah salah satu tipe data yang paling umum digunakan untuk menyimpan kumpulan elemen atau nilai. List adalah struktur data yang dapat diubah (mutable) dan dapat menampung berbagai tipe data, termasuk integer, float, string, serta bahkan list lainnya. Berikut adalah contoh List dalam Python:
```
my_list = [1, 2, 3, 4, 5]
nama_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
campuran = [1, 'dua', 3.0, 'empat', 5]
print(my_list[0])  # Output: 1
print(nama_hari[2])  # Output: Rabu
print(campuran[1])  # Output: dua
```

### String Manipulation
String Manipulation adalah proses memanipulasi, mengubah, atau memanipulasi teks dalam string sesuai dengan kebutuhan aplikasi atau program.  Dalam Python, ada banyak metode bawaan yang memungkinkan kita untuk melakukan berbagai operasi string manipulation. Berikut adalah beberapa operasi umum yang sering dilakukan dalam string manipulation:
```
string1 = "Hello"
string2 = "World"
gabung = string1 + " " + string2
print(gabung)  # Output: Hello World

nama = "John"
umur = 30
kalimat = "Nama: %s, Umur: %d" % (nama, umur)
print(kalimat)  # Output: Nama: John, Umur: 30

kalimat = "Nama: {}, Umur: {}".format(nama, umur)
print(kalimat)  # Output: Nama: John, Umur: 30

kalimat = f"Nama: {nama}, Umur: {umur}"
print(kalimat)  # Output: Nama: John, Umur: 30
```

