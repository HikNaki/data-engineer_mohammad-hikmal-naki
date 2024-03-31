# (14) Data Ingestion with Python

## What is Data Ingestion

Data ingestion dalam bidang data engineer adalah proses pengumpulan dan pemindahan data dari berbagai sumber ke tempat penyimpanan data.  Data bisa berasal dari berbagai macam tempat, misalnya database relasional, database NoSQL, perangkat IoT, situs web, layanan streaming, dan lain-lain.  Tujuannya adalah agar data bisa disimpan, diproses, dan dianalisis lebih lanjut.

## Key Component of Data Ingestion

Key component dari proses data ingestion terdiri :

1. **Data Source**:
   Data source merujuk pada sumber asli dari mana data diambil. Sumber data ini bisa beragam, mulai dari database relasional, file teks, cloud, hingga aliran data real-time dari sensor atau perangkat IoT (Internet of Things). Data source adalah titik awal dalam proses pengumpulan data, dan kualitas serta aksesibilitasnya sangat penting untuk memastikan keberhasilan proses data ingestion.

2. **Data Target**:
   Data target adalah tempat tujuan di mana data akan dimuat setelah melewati proses ingestion. Tempat tujuan ini bisa berupa basis data, data warehouse, data lake, atau sistem penyimpanan lainnya yang sesuai dengan kebutuhan bisnis atau analisis yang dimaksud. Penting bagi data target untuk memiliki kapasitas penyimpanan yang cukup, performa yang baik, dan kemampuan untuk menyimpan dan mengelola berbagai jenis data yang diinginkan.

3. **Data Pipeline**:
   Data pipeline merujuk pada rangkaian langkah-langkah atau alur kerja yang digunakan untuk mentransfer, mentransformasi, dan memuat (ETL) data dari sumber ke target. Data pipeline dapat terdiri dari serangkaian proses yang terotomatisasi dan dijalankan secara berkala atau secara real-time, tergantung pada kebutuhan bisnis. Data pipeline memainkan peran kunci dalam menjaga kelancaran aliran data dan memastikan bahwa data yang dimuat ke dalam sistem target adalah data yang berkualitas dan bermakna.

## Technique and Best Practices
Terkait dengan proses data ingestion, berikut adalah beberapa teknik dan best practices:

1. **Optimisasi dan Penanganan Kesalahan**:
   - *Optimisasi*: Gunakan teknologi dan alat yang tepat untuk meningkatkan kinerja proses data ingestion.
   - *Penanganan Kesalahan*: Siapkan mekanisme untuk mendeteksi, mencatat, dan menangani kesalahan dengan cepat.

2. **Transformasi Data Selama Ingestion**:
   - Lakukan transformasi data untuk mengubah format, struktur, atau nilai-nilai data sesuai kebutuhan bisnis.
   - Pastikan transformasi dilakukan dengan benar, mempertahankan konsistensi data, dan memperhatikan kinerja proses.

3. **Keamanan Selama Data Ingestion**:
   - Lindungi data selama perpindahannya dengan menggunakan enkripsi, protokol komunikasi yang aman, dan kontrol akses yang kuat.
   - Pastikan infrastruktur seperti server dan sistem penyimpanan juga dilindungi dari serangan atau akses tidak sah.