## Data Transformation Code Breakdown

## 1. **Import:**

   - Mengimpor library yang diperlukan untuk manipulasi data (`pandas`), penjadwalan (`Airflow`), logging (`logging`), penanganan file path (`os`), dan Firebase Admin SDK untuk berinteraksi dengan Google Storage (`firebase_admin`).

## 2. **DataWarehouseLoader Class:**

   - Mendefinisikan metode untuk tugas pemuatan gudang data:
        - `load_data`: Membaca file Parquet ke dalam Pandas DataFrame.
        - `transform_data`: Menggabungkan dan mengubah data dari sumber berbeda:
            - Menggabungkan transaksi dan tiket berdasarkan `ticket_id`.
            - Menggabungkan data yang digabung dengan peristiwa berdasarkan `event_id`.
            - Menghitung tiket terjual dan pendapatan per acara.
            - Menggabungkan data dengan pelanggan berdasarkan `customer_id`.
            - Menggabungkan umpan balik pelanggan dengan transaksi berdasarkan `transaction_id`.
            - Menghitung peringkat rata-rata per acara.
        - `save_to_warehouse`: Menyimpan data yang ditransformasikan sebagai file Parquet dan mengunggahnya ke Firebase Storage:
            - Menginisialisasi aplikasi Firebase Admin jika belum dilakukan.
            - Membuat file Parquet lokal untuk setiap DataFrame yang ditransformasikan.
            - Mengunggah file Parquet ke Firebase Storage dengan awalan tanggal.

## 3. **Logging Configuration:**
   - Mengatur logging dasar dengan level INFO dan format tertentu.

## 4. **Default Arguments:**
   - Mendefinisikan argumen default untuk task Airflow, seperti owner (`hikmal`), retries (`5`), dan retry delay (`2 menit`).

## 5. **DAG Definition:**
   - Membuat DAG dengan properti berikut:
        - `dag_id`: `data_warehouse_pipeline_dag` (unique identifier).
        - `default_args`: Menerima argumen default yang ditetapkan sebelumnya.
        - `start_date`: Menentukan tanggal awal untuk menjalankan pipeline (21 April 2024).
        - `schedule_interval`: Menjalankan pipeline setiap hari (`@daily`).
        - `catchup=False`: Mencegah backfilling data untuk tanggal eksekusi yang terlewat.
        - `description`: Memberikan deskripsi singkat tentang tujuan DAG.

## 6. **DAG Tasks:**
   - `logger`: Mendapatkan instance logger untuk logging di dalam DAG.
   - `loader`: Membuat instance dari kelas `DataWarehouseLoader`.

   - **Path dan Table Names:**
        - `folder_path`: Mendefinisikan lokasi file Parquet.
        - `table_name`: Daftar nama tabel untuk data yang ditransformasikan di Google Storage.

   - **Load Data Task (Independent):**
        - Task `PythonOperator` terpisah  didefinisikan untuk setiap file data:
            - `load_transactions`
            - `load_tickets`
            - `load_events`
            - `load_customer_feedback`
            - `load_customers`
        - Setiap task menggunakan `load_data` dari `DataWarehouseLoader` untuk membaca file Parquet terkait.

   - **Transform Data Task:**
        - `transform_data`:
            - Mengambil output dari semua task `load_data` sebagai input menggunakan `op_args`.
            - Menggabungkan dan mengubah data seperti yang dijelaskan di`DataWarehouseLoader` class.

   - **Save to Warehouse Task:**
        - `save_to_warehouse`:
            - Mengambil output dari task `transform_data` (daftar DataFrame) dan daftar `table_name` sebagai input.
            - Menyimpan setiap DataFrame sebagai file Parquet secara lokal.
            - Mengunggah file Parquet ke Google Storage dengan struktur folder berdasarkan tanggal.

   - **Task Dependencies:**
        - Semua task `load_data` ditetapkan sebagai dependensi upstream untuk task `transform_data`, memastikan data dimuat sebelum transformasi.
        - Task `transform_data` ditetapkan sebagai dependensi upstream untuk task `save_to_warehouse`, memastikan transformasi terjadi sebelum data diunggah.

**Secara keseluruhan, kode data transformation ini mendefinisikan pipeline data warehouse menggunakan Airflow. Kode ini memuat data dari file Parquet, mentransformasinya dengan menggabungkan dan menghitung metrik, dan akhirnya menyimpan data yang ditransformasikan di Google Cloud Storage.**