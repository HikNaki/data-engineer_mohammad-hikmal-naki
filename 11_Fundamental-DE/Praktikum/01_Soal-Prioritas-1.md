# Soal Prioritas 1

### 1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.

Data terstruktur adalah data yang memiliki format yang terorganisir dengan baik, biasanya dalam bentuk tabel atau kolom, dengan definisi yang jelas untuk setiap elemen datanya. Contoh data terstruktur adalah data dalam basis data relasional, di mana informasi disimpan dalam tabel dengan kolom-kolom yang telah ditentukan sebelumnya seperti nama, alamat, dan nomor telepon. Data terstruktur biasanya disimpan dalam basis data atau file dengan format yang terdefinisi sebelumnya, seperti format tabel dalam basis data relasional atau file CSV.

Sementara itu, data tidak terstruktur adalah data yang tidak memiliki format yang terorganisir dengan baik, sehingga sulit untuk dianalisis secara langsung. Contoh data tidak terstruktur termasuk teks bebas, file audio, dan video. Data ini tidak memiliki skema atau struktur yang terdefinisi sebelumnya, sehingga mereka sering disimpan dalam format file mentah seperti dokumen teks, file audio dalam format WAV, atau video dalam format MP4. Prosesing data tidak terstruktur biasanya melibatkan teknik-teknik seperti pemrosesan bahasa alami untuk teks, atau pemrosesan sinyal digital untuk audio dan video.

### 2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.

Basis data relasional adalah jenis basis data yang menggunakan model relasional untuk menyimpan dan mengelola data. Dalam model relasional, data disimpan dalam bentuk tabel yang terdiri dari baris dan kolom. Setiap tabel mewakili entitas tertentu, dan hubungan antara tabel-tabel tersebut ditentukan oleh kunci-kunci primer dan kunci asing. Contoh penggunaan basis data relasional adalah dalam sistem manajemen basis data seperti MySQL, PostgreSQL, atau Oracle.

Misalnya, sebuah perusahaan menggunakan basis data relasional untuk mengelola informasi pelanggannya. Mereka dapat memiliki tabel "Pelanggan" yang berisi informasi seperti nama pelanggan, alamat, dan nomor telepon. Kemudian, mereka bisa memiliki tabel terpisah untuk pesanan, yang terkait dengan tabel "Pelanggan" melalui kunci asing yang mengidentifikasi pelanggan yang melakukan pesanan.

### 3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.

Normalisasi basis data adalah proses desain yang bertujuan untuk mengorganisir struktur data relasional agar meminimalkan redundansi dan anomali data. Tujuannya adalah untuk mencapai basis data yang memenuhi persyaratan integritas data dan efisiensi penyimpanan. Normalisasi mencapai ini dengan membagi tabel besar menjadi beberapa tabel yang lebih kecil dan lebih terorganisir, dan mengatur hubungan antara tabel-tabel tersebut.

Konsep normalisasi penting dalam basis data relasional karena dapat menghindari masalah seperti anomali penyimpanan, update, dan delete, serta memungkinkan konsistensi data yang lebih baik. Misalnya, dengan normalisasi yang tepat, informasi pelanggan hanya perlu disimpan sekali dalam basis data, bahkan jika mereka melakukan banyak pesanan. Ini mengurangi redundansi data dan memudahkan pemeliharaan serta pembaruan informasi pelanggan.

Referensi :
[structured-data vs unstrucctured-data](https://aws.amazon.com/id/compare/the-difference-between-structured-data-and-unstructured-data/)

[relational-database](https://aws.amazon.com/id/relational-database/)
