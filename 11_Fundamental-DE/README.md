# (12) Fundamental DE

## Structured, Semi-Structured, and Unstructured Data

Data terstruktur adalah tipe data di mana informasi tersusun dengan jelas dalam format yang terorganisir, sering kali menggunakan skema yang telah ditentukan sebelumnya. Data ini biasanya disimpan dalam basis data relasional atau dalam format file yang mengikuti format tertentu, seperti tabel dalam spreadsheet atau basis data SQL.

Data semi-terstruktur adalah tipe data di mana informasi disajikan dalam format yang tidak sepenuhnya terstruktur atau tidak mengikuti skema yang ketat, tetapi memiliki beberapa struktur yang dapat diidentifikasi.

Data tak terstruktur adalah tipe data di mana informasi tidak diatur dalam format yang terstruktur atau tidak memiliki skema yang jelas. Data ini sering kali disajikan dalam bentuk teks bebas, audio, video, atau gambar. Karakteristik utama data tak terstruktur adalah kurangnya format atau struktur yang konsisten, membuatnya sulit untuk diorganisir dan diolah secara otomatis.

## Relational and NoSQL Database

Database relasional adalah jenis database yang paling umum digunakan. Data disimpan dalam tabel yang terdiri dari baris dan kolom, seperti spreadsheet. Setiap tabel memiliki skema yang mendefinisikan struktur data. Skema ini menentukan nama kolom, tipe data, dan hubungan antar tabel.

Database NoSQL adalah jenis database yang lebih baru dan tidak menggunakan tabel. Data disimpan dalam format yang lebih fleksibel, seperti dokumen, key-value, atau graph. NoSQL database dirancang untuk skalabilitas dan kinerja tinggi.

## OLTP and OLAP

OLTP singkatan dari (Online Transaction Processing) yang merujuk pada sistem database yang dirancang untuk mengelola transaksi yang dilakukan oleh organisasi secara real-time. Dalam lingkungan bisnis, OLTP berfungsi untuk mendukung operasi sehari-hari seperti penjualan, pembelian, dan penyimpanan data pelanggan. Sistem OLTP cenderung memiliki struktur basis data yang sederhana dan dioptimalkan untuk menangani sejumlah besar transaksi yang bersifat operasional dan transaksional.

Sementara itu, OLAP (Online Analytical Processing) yang merujuk pada sistem database yang digunakan untuk menganalisis dan melaporkan data secara lebih mendalam dan kompleks. OLAP digunakan untuk menganalisis tren, pola, dan hubungan di dalam data dengan cara yang lebih terstruktur dan mendalam daripada yang bisa dilakukan oleh sistem OLTP. Sistem OLAP memungkinkan pengguna untuk melihat data dari berbagai sudut pandang, melakukan analisis multidimensional, dan membuat laporan yang lebih kaya secara analisis.

## Data Warehouse, Data Lake and Data Mart
Data Warehouse adalah repositori terstruktur yang menyimpan data yang telah diproses dan disaring dari berbagai sumber untuk mendukung analisis bisnis. Data Lake adalah penyimpanan data skala besar yang memuat data mentah dari berbagai sumber tanpa struktur sebelumnya, memungkinkan eksplorasi data yang fleksibel. Data Mart adalah subset dari Data Warehouse yang disesuaikan dengan kebutuhan departemen tertentu, menyediakan data yang dioptimalkan untuk analisis spesifik.