# (8) Relational Database

## What is Database?

Database adalah tempat di mana kita bisa menyimpan dan mengatur sejumlah besar data secara terorganisir. Bayangkan seperti rak buku besar di perpustakaan, di mana setiap buku adalah data yang bisa kita simpan. Nah, dalam database, kita bisa menyimpan data-data itu dengan rapi, dan yang paling penting, kita bisa mengaksesnya, mengubahnya, atau menambahkan informasi baru kapan pun kita butuhkan tanpa harus susah-susah mencari di antara tumpukan buku yang berantakan.

## Database Relationship

Database relationship adalah relasi atau hubungan antara beberapa tabel dalam database yang kita miliki. Ada beberapa jenis hubungan antar tabel dalam database relasional, yang paling umum adalah:

### 1. One to One

Jarang digunakan, hubungan ini terjadi ketika satu record pada suatu tabel hanya bisa memiliki hubungan dengan maksimal satu record pada tabel lain. Contohnya, sebuah tabel "Employee" mungkin memiliki hubungan satu-ke-satu dengan tabel "Employee_Details", di mana setiap karyawan memiliki satu dan hanya satu catatan detail karyawan.

### 2. One to Many

Hubungan ini sangat umum, terjadi ketika satu record pada suatu tabel bisa memiliki hubungan dengan banyak record pada tabel lain. Contoh di atas adalah ilustrasi dari hubungan one-to-many. Contohnya, sebuah tabel "Customer" dapat memiliki hubungan satu-ke-banyak dengan tabel "Orders", di mana satu pelanggan dapat memiliki banyak pesanan.

### 3. Many to Many

Hubungan ini terjadi ketika banyak record pada suatu tabel bisa memiliki hubungan dengan banyak record pada tabel lain. Untuk mengakomodasi hubungan ini, biasanya diperlukan tabel tambahan sebagai jembatan (bridge table). Misalnya, sebuah aplikasi e-commerce dapat memiliki hubungan banyak-ke-banyak antara tabel "Products" dan "Customers", di mana satu produk dapat dibeli oleh banyak pelanggan, dan satu pelanggan dapat membeli banyak produk.

## Jenis Perintah SQL

### Data Definition Language

DDL adalah jenis perintah dalam SQL yang digunakan untuk mendefinisikan struktur dan skema dari database. DDL digunakan untuk membuat, mengubah, dan menghapus objek database seperti tabel, indeks, dan view.

### Data Manipulation Language

DML adalah perintah yang digunakan untuk mengelola data dalam database. Ini mencakup perintah-perintah untuk memanipulasi data yang sudah ada di dalam tabel, seperti menambah, mengubah, atau menghapus baris data.

### Data Control Language

DCL adalah perintah yang digunakan untuk mengendalikan hak akses dan izin pengguna terhadap objek dalam database. Ini mencakup perintah-perintah untuk memberikan atau mencabut izin akses, serta mengatur keamanan dan privasi data dalam database.
