# (13) Data Warehouse and Data Lake Part 1

## What is Data Warehouse and Data Lake?

Data warehouse adalah sebuah sistem yang digunakan untuk menyimpan dan mengelola data dalam jumlah besar dari berbagai sumber yang berbeda, dengan tujuan untuk melakukan analisis data, data mining, artificial intelligence (AI), dan machine learning. Data Lake adalah penyimpanan data skala besar yang memuat data mentah dari berbagai sumber tanpa struktur untuk tujuan yang belum ditentukan, memungkinkan eksplorasi data yang fleksibel.

## Columnar Table 
Kolom tabel (columnar table) pada Citus adalah opsi penyimpanan data per tabel untuk analitik dan beban kerja data warehouse. Ini berbeda dari penyimpanan data berbasis baris tradisional di PostgreSQL.

- Penyimpanan Baris (Row Storage):  Ini adalah metode penyimpanan default di PostgreSQL. Setiap baris data disimpan secara berdekatan di disk, dengan semua kolom untuk baris itu bersebelahan. Ini bekerja dengan baik untuk operasi transaksional tetapi bisa kurang efisien untuk kueri analitik yang hanya membutuhkan subset kolom.

- Penyimpanan Kolom (Columnar Storage): Di sini, Citus menyimpan data menurut kolom alih-alih baris. Semua nilai untuk kolom tertentu disimpan bersama-sama di disk.  

Dengan cara ini, Citus dapat:

- Compress data more effectively: Karena nilai-nilai serupa sering dikelompokkan bersama, kompresi bekerja lebih baik.
- Improve query performance: Saat kueri hanya membutuhkan subset kolom, Citus hanya perlu membaca kolom yang relevan, mengurangi I/O yang diperlukan. Ini dapat secara dramatis meningkatkan kecepatan kueri analitik.

## Table Partition
Table partitioning adalah teknik untuk mengatur data dalam tabel database yang sangat besar.  Dengan partisi, alih-alih menyimpan semua data dalam tabel tunggal yang besar, data dipecah menjadi potongan-potongan yang lebih kecil dan lebih mudah dikelola, yang disebut partisi.

## Replication and Sharding

Dalam Citus, replication dan sharding adalah konsep terpisah yang bekerja sama untuk mencapai skalabilitas dan ketahanan data:

* **Replication (Replikasi):**
  * Replikasi berarti menduplikasi data di seluruh cluster Citus. 
  * Citus menggunakan replikasi streaming PostgreSQL untuk menjaga agar data pada node worker tetap sinkron.
  * Ini memastikan ketersediaan data yang tinggi. Jika sebuah node worker gagal, data tetap tersedia pada replikanya.

* **Sharding (Sharding):**
  * Sharding adalah teknik untuk memecah data menjadi beberapa bagian horizontal berdasarkan kolom tertentu (sharding key).
  * Setiap bagian data disimpan pada node worker terpisah di cluster Citus.
  * Ini memungkinkan kita menskalakan database secara horizontal dengan menambahkan lebih banyak node worker untuk menangani peningkatan volume data.
  * Citus secara otomatis merutekan kueri ke node worker yang relevan berdasarkan sharding key.

**Bekerja Bersama:**

Sharding dan replication saling melengkapi dalam Citus:

  * **Sharding** mendistribusikan data melintasi banyak node worker, meningkatkan performa dan skalabilitas.
  * **Replication** memastikan ketersediaan data yang tinggi pada setiap shard.  Bahkan jika node worker gagal, replikanya dapat melayani permintaan.

**Perbedaan antara keduanya:**

| Fitur                 | Replication             | Sharding                 |
|------------------------|-------------------------|--------------------------|
| Tujuan                 | Ketersediaan data tinggi | Skalabilitas horizontal  |
| Distribusi data        | Seluruh data direplikasi | Data dipecah berdasarkan sharding key |
| Dampak pada kueri        | Sedikit dampak           | Kueri perlu menyertakan sharding key untuk menemukan data yang relevan |