# (14) Data Warehouse and Data Lake Part 2

## Replication dan Sharding

1. **Replikasi**: Replikasi dalam Citus membuat salinan data dari satu node ke node lain dalam cluster. Tujuannya adalah meningkatkan toleransi terhadap kesalahan dan meningkatkan ketersediaan sistem. Dengan replikasi, jika satu node gagal, operasi database dapat diarahkan ke node yang masih beroperasi, mengurangi dampak downtime pada aplikasi.

2. **Sharding**: Sharding adalah teknik yang digunakan untuk membagi data menjadi sejumlah kecil bagian yang disebut shard, dan mendistribusikannya di beberapa node dalam cluster. Setiap node dalam cluster bertanggung jawab atas satu atau beberapa shard data. Tujuannya adalah untuk memperluas kapasitas sistem secara horizontal dengan memperbesar infrastruktur secara linear saat jumlah data meningkat. Dengan sharding, Citus dapat menangani beban kerja yang sangat besar dengan mendistribusikan data di sepanjang beberapa node.

Jadi, ketika digabungkan, replikasi dan sharding memungkinkan Citus untuk mengelola basis data yang besar dengan menggabungkan paralelisme dan distribusi data. Replikasi memberikan keandalan dan ketersediaan yang tinggi, sementara sharding memungkinkan skala secara horizontal untuk menangani volume data yang besar. Keduanya berkontribusi pada kinerja dan skalabilitas Citus di lingkungan produksi yang besar dan kompleks.

## Colocation

Colocation dalam PostgreSQL mengacu pada penyimpanan data yang disusun dalam urutan yang sama atau dekat dalam disk. Misalnya, ketika dua tabel memiliki hubungan yang kuat dan sering bergabung dalam kueri yang sama, colocation dapat meningkatkan kinerja dengan memastikan bahwa data dari kedua tabel disimpan dalam blok yang sama atau blok yang berdekatan dalam disk. Ini mengurangi waktu yang dibutuhkan untuk mengakses data dan meningkatkan efisiensi operasi database.

## What is Bigquery?

BigQuery adalah layanan **gudang data cloud** dari Google Cloud Platform. Kita dapat menyimpan, mengelola, dan menganalisis data besar dengan BigQuery. Keunggulannya meliputi skalabilitas elastis, analitik SQL yang kuat, keamanan tinggi, dan biaya yang hemat. Singkatnya, BigQuery adalah solusi ideal untuk analitik data berbiaya efektif pada skala besar.

## Google Cloud Storage

Google Cloud Storage (GCS) adalah layanan penyimpanan online untuk menyimpan data dalam jumlah besar, seperti gambar, video, dan dokumen. Dengan GCS, kita dapat menyimpan dan mengakses data kita dari mana saja dengan aman dan mudah. GCS cocok untuk bisnis yang membutuhkan penyimpanan yang skalabel dan hemat biaya.
