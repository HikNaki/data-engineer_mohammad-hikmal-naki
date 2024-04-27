# Data Ingestion Code Breakdown

## 1. **Import:**
   - Mengimpor library yang diperlukan untuk manipulasi data (`pandas`), penjadwalan (`Airflow`), logging (`logging`), dan penanganan file path (`os`).

## 2. **DatalakeBuilder Class:**
   - Mendefinisikan metode untuk berbagai tugas pemrosesan data:
     - `read_csv_data`: Membaca file CSV ke dalam Pandas DataFrame.
     - `handle_missing_values`: Mengisi nilai yang hilang dalam DataFrame menggunakan modus (nilai yang paling sering muncul).
     - `handle_outliers` (opsional): Menghapus outlier dari kolom tertentu (hanya diterapkan pada data "transaksi").
     - `save_to_parquet`: Menyimpan DataFrame sebagai file Parquet.
     - `validate_data`: Membaca dan menampilkan beberapa baris pertama dari file Parquet untuk validasi.

## 3. **Logging Configuration:**
   - Mengatur logging dasar dengan level INFO dan format tertentu.

## 4. **Default Arguments:**
   - Mendefinisikan argumen default untuk task Airflow, seperti owner (`hikmal`), retries (`5`), dan retry delay (`2 menit`).

## 5. **DAG Definition:**
   - Membuat DAG dengan properti berikut:
     - `dag_id`: `data_lake_pipeline_dag` (unique identifier).
     - `default_args`: Menerima argumen default yang ditetapkan sebelumnya.
     - `start_date`: Menentukan tanggal awal untuk menjalankan pipeline (20 April 2024).
     - `schedule_interval`: Menjalankan pipeline setiap hari (`@daily`).
     - `catchup=False`: Mencegah backfilling data untuk tanggal eksekusi yang terlewat.
     - `description`: Memberikan deskripsi singkat tentang tujuan DAG.

## 6. **DAG Tasks:**
   - `logger`: Mendapatkan instance logger untuk logging di dalam DAG.
   - `datalake_builder`: Membuat instance dari kelas `DatalakeBuilder`.
   - `folder_path`: Mendefinisikan lokasi file CSV sumber.
   - `file_types`: Daftar berbagai jenis file data yang akan diproses.

   - **Task Dictionaries:**
     - `read_tasks`, `handle_missing_tasks`, `handle_outliers_tasks` (opsional), `save_tasks`, dan `validate_tasks`: Kamus ini menyimpan task individual untuk setiap tipe file data, memungkinkan pembuatan DAG secara dinamis.

   - **Task Creation Loop:**
     - Melakukan iterasi melalui setiap tipe file.
     - Membuat entri `read_tasks` menggunakan `PythonOperator` untuk membaca file CSV terkait.
     - Membuat entri `handle_missing_tasks` untuk menangani nilai yang hilang.
     - Secara opsional membuat entri `handle_outliers_tasks` untuk data "transaksi" guna menghilangkan outlier.
     - Membuat entri `save_tasks` untuk menyimpan DataFrame yang telah diproses sebagai file Parquet.
     - Membuat entri `validate_tasks` untuk memvalidasi file Parquet yang disimpan.

   - **Setting Task Dependencies:**
     - Menetapkan dependensi antar task menggunakan `set_downstream`:
       - Output dari `read_tasks` menjadi input untuk `handle_missing_tasks`.
       - Output dari `handle_missing_tasks` menjadi input untuk `save_tasks`.
       - Untuk data "transaksi", output dari `handle_missing_tasks` menuju ke `handle_outliers_tasks`, lalu ke `save_tasks`.
       - Output dari `save_tasks` menjadi input untuk `validate_tasks`.


**Secara Keseluruhan, kode data ingestion ini mendefinisikan pipeline data lake menggunakan Airflow. Kode ini membaca file CSV, menangani nilai yang hilang dan outlier (opsional), menyimpan data dalam format Parquet, dan memvalidasi data yang disimpan. DAG mengelola dependensi antar task untuk memastikan data diproses dalam urutan yang benar.**