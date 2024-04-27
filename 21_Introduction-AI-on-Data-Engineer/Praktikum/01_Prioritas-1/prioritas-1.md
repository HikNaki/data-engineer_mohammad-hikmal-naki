# Soal Prioritas 1

## Prompt Input

- **Model AI** : `CHATGPT`
- **Prompt** : buatkan saya schema database peminjaman buku di perpustakaan dan buatkan juga query create table nya

## Response Output

- **Output** :
    Tentu, berikut adalah contoh skema database untuk peminjaman buku di perpustakaan beserta query untuk membuat tabelnya:

    Skema Database:

    1. Tabel Buku:
        - ID_Buku (Kunci Utama)
        - Judul_Buku
        - Penulis
        - Tahun_Terbit
        - Ketersediaan
    2. Tabel Anggota:
        - ID_Anggota (Kunci Utama)
        - Nama_Anggota
        - Alamat
        - Nomor_Telepon
    3. Tabel Peminjaman:
        - ID_Peminjaman (Kunci Utama)
        - ID_Buku (Kunci Asing dari Tabel Buku)
        - ID_Anggota (Kunci Asing dari Tabel Anggota)
        - Tanggal_Peminjaman
        - Tanggal_Pengembalian
    
    Query untuk Membuat Tabel (MySQL Syntax):
    ```
    CREATE TABLE Buku (
    ID_Buku INT AUTO_INCREMENT PRIMARY KEY,
    Judul_Buku VARCHAR(255) NOT NULL,
    Penulis VARCHAR(100),
    Tahun_Terbit YEAR,
    Ketersediaan BOOLEAN DEFAULT TRUE
    );

    CREATE TABLE Anggota (
        ID_Anggota INT AUTO_INCREMENT PRIMARY KEY,
        Nama_Anggota VARCHAR(100) NOT NULL,
        Alamat VARCHAR(255),
        Nomor_Telepon VARCHAR(15)
    );

    CREATE TABLE Peminjaman (
        ID_Peminjaman INT AUTO_INCREMENT PRIMARY KEY,
        ID_Buku INT,
        ID_Anggota INT,
        Tanggal_Peminjaman DATE,
        Tanggal_Pengembalian DATE,
        FOREIGN KEY (ID_Buku) REFERENCES Buku(ID_Buku),
        FOREIGN KEY (ID_Anggota) REFERENCES Anggota(ID_Anggota)
    );

    ```
    Dengan skema dan query tersebut, Anda dapat menyimpan informasi tentang buku, anggota, dan transaksi peminjaman di perpustakaan Anda.

## Penjelasan Hasil

Model AI ChatGPT menggunakan algoritma pemrosesan bahasa untuk memahami input yang saya berikan. Selanjutnya, AI tersebut mengenali permintaan saya untuk membuat skema database peminjaman buku di perpustakaan beserta query untuk membuat tabelnya. Setelah memahami permintaan saya, AI menggunakan pengetahuannya tentang struktur database dan SQL untuk merancang skema database yang sesuai dan menyusun query yang diperlukan.

Untuk membuat skema database, AI mengidentifikasi entitas yang terlibat, seperti buku, anggota, dan peminjaman, serta atribut-atribut yang diperlukan untuk masing-masing entitas. Setelah itu, AI menentukan primary key dan foreign key yang diperlukan untuk membangun relasi antara tabel-tabel tersebut.

Setelah merancang skema database, AI menggunakan sintaks SQL untuk membuat tabel-tabel tersebut. Sintaks SQL ini dibuat sesuai dengan standar bahasa SQL yang umum digunakan, dalam hal ini menggunakan sintaks MySQL. Setiap tabel memiliki kolom-kolom yang sesuai dengan atribut-atribut yang telah ditentukan dalam skema database.