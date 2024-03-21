# (11) Docker

## What is Docker?

Docker adalah platform perangkat lunak yang memungkinkan kita untuk mengemas, mendistribusikan, dan menjalankan aplikasi di lingkungan yang terisolasi yang disebut sebagai "kontainer". Kontainer Docker mengizinkan kita untuk memisahkan aplikasi kita dari infrastruktur, sehingga kita dapat mengemas aplikasi beserta semua dependensinya ke dalam unit yang dapat dipindahkan antara lingkungan developeran, pengujian, dan produksi tanpa mengalami perubahan.

## Virtual Machine and Container

**Container:**

- Mirip kotak berisi semua yang dibutuhkan aplikasi untuk berjalan.
- Ringan dan hemat sumber daya.
- Cocok untuk aplikasi sederhana yang tidak memerlukan sistem operasi khusus.

**Virtual Machine:**

- Mirip komputer virtual dengan sistem operasi sendiri.
- Lebih berat dan membutuhkan banyak sumber daya.
- Cocok untuk aplikasi kompleks yang memerlukan sistem operasi khusus.

## Docker Network

Docker Network adalah fitur yang memungkinkan kontainer Docker untuk berkomunikasi satu sama lain dan dengan resource lainnya di dalam atau di luar lingkungan Docker. Dengan Docker Network, kontainer dapat terhubung ke jaringan internal ataupun eksternal. Hal ini memungkinkan aplikasi yang berjalan di kontainer Docker untuk berinteraksi dengan layanan lainnya, seperti database, layanan API, atau kontainer lainnya.
Keuntungan:
- Isolasi: Container tidak terhubung dengan sembarang jaringan.
- Komunikasi: Memudahkan container saling bertukar data dan berinteraksi satu sama lain.
- Skalabilitas: Jaringan virtual dapat dengan mudah ditambahkan container baru.

## Docker Volume

Docker Volume adalah mekanisme yang memungkinkan data persisten disimpan di luar siklus hidup kontainer Docker. Saat kontainer Docker dihapus atau dihentikan, data yang disimpan dalam volume akan tetap ada dan tersedia untuk kontainer lain yang terhubung ke volume yang sama. Hal ini memungkinkan developer untuk menyimpan data seperti file konfigurasi, database, atau berkas log dengan aman dan efisien di dalam kontainer Docker.
Keuntungan:
- Backup dan migrasi lebih mudah.
- Dapat dibagi lebih aman dengan kontainer lainnya.
- Menambahkan fungsionalitas lain.

## Container Orchestration

Container Orchestration adalah proses mengelola aplikasi yang dijalankan dalam kontainer secara otomatis. Ini melibatkan manajemen siklus hidup kontainer, penjadwalan, otomatisasi tugas, dan pemantauan aplikasi yang berjalan dalam lingkungan kontainer. Container Orchestration memungkinkan pengelolaan efisien dan skalabilitas aplikasi yang terdiri dari beberapa kontainer, memastikan ketersediaan, keandalan, dan kinerja optimal.

## Docker Compose

Docker Compose adalah tool yang memungkinkan developer untuk mendefinisikan dan menjalankan aplikasi yang terdiri dari beberapa kontainer Docker dengan mudah. Docker Compose menggunakan berkas konfigurasi YAML yang sederhana untuk menentukan layanan, jaringan, dan volume yang diperlukan oleh aplikasi. Ini memungkinkan developer untuk mendefinisikan konfigurasi aplikasi sekali dan menjalankannya dengan perintah sederhana, mengurangi kompleksitas dalam pengelolaan aplikasi berbasis kontainer.
