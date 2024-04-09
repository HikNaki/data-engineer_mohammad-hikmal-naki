# (15) Data Transformation

## What is Data Transformation?
Data transformation dalam bidang data engineering merujuk pada proses mengubah data dari satu bentuk atau format ke bentuk atau format lainnya untuk tujuan analisis, penyimpanan, atau visualisasi. Ini merupakan langkah kunci dalam alur kerja pengolahan data yang melibatkan serangkaian operasi untuk membersihkan, memformat ulang, menggabungkan, membagi, atau menghitung data.

__Tujuan utama transformasi data:__
- Meningkatkan kualitas data: Mengatasi missing value, inkonsistensi, dan kesalahan dalam data.
- Mempermudah analisis: Mengubah data menjadi format yang kompatibel dengan alat analisis dan model machine learning.
- Meningkatkan efisiensi: Menyimpan data dalam format yang ringkas dan mudah diakses.

## Types of Data Transformation
- Normalization : Normalisasi adalah proses untuk mengubah nilai-nilai dalam dataset agar berada dalam rentang standar tertentu. normalisasi dapat dilakukan pada semua tipe data. Contohnya, dalam normalisasi, nilai-nilai dapat diubah agar berkisar antara 0 dan 1 atau -1 hingga 1.
- Encoding : Encoding adalah proses mengubah data kategori menjadi bentuk numerik. Hal ini diperlukan karena banyak algoritma machine learning memerlukan input numerik. Misalnya, jika kita memiliki data kategori seperti jenis kelamin (pria, wanita), maka encoding dapat mengubahnya menjadi nilai numerik seperti 0 dan 1, di mana 0 mewakili pria dan 1 mewakili wanita.
- Aggregation : Agregasi adalah proses merangkum data menjadi bentuk yang lebih sederhana atau ringkas untuk analisis lebih lanjut. Agregasi digunakan untuk menghitung rata-rata, median, atau modus. Misalnya, jika kita memiliki data transaksi harian, kita bisa mengagregasikannya menjadi total penjualan bulanan atau tahunan untuk melihat tren secara lebih luas.

## Challenges in Data Transformation
1. Handling missing values : Salah satu tantangan dalam data transformation adalah mengatasi missing value. Misalnya, jika ada data yang hilang atau tidak lengkap, dapat dilakukan dengan mengisi data yang hilang dengan metode yang sesuai. Seperti mengisi nilai yang hilang dengan nilai rata-rata, nilai median, atau menggunakan teknik imputasi data lainnya.
2. Dealing with outliers: Outlier adalah data yang tidak sesuai dengan kriteria yang ditentukan. Data outlier dapat menjadi salah satu tantangan dalam data transformation. Misalnya, jika ada data yang terlalu tinggi atau terlalu rendah, dapat dilakukan dengan mengatasi outlier dengan metode yang sesuai.
3. Ensuring data integrity and avoiding data loss: Menjaga integritas data dan menghindari kehilangan data adalah tantangan penting dalam proses transformasi data. Hal ini melibatkan langkah-langkah untuk memastikan bahwa data yang ditransformasi tetap akurat dan relevan dengan kebutuhan analisis. Selain itu, perlu juga mempertimbangkan cara untuk mencegah kehilangan data selama proses transformasi, seperti dengan membuat cadangan data dan menggunakan mekanisme pengamanan yang sesuai.

## ETL (Extract, Transform, Load) Tools
1. Apache Airflow.
2. Informatica.
3. Talend.
4. Microsoft SQL Server Integration Services.