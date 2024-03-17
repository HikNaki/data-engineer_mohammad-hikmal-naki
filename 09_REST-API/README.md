# (9) REST API

## What is API?

API adalah singkatan dari `Application Programming Interface`, yang merupakan kumpulan aturan dan protokol yang memungkinkan aplikasi untuk berkomunikasi satu sama lain. Dengan API, pengembang dapat mengakses fitur dan data dari aplikasi lain tanpa perlu membangunnya sendiri.

### Contoh Penggunaan API 
1. Aplikasi cuaca: Mengakses data cuaca dari layanan cuaca seperti BMKG.
2. Aplikasi media sosial: Mengirim postingan ke Facebook atau Twitter.
3. Aplikasi e-commerce: Memproses pembayaran melalui PayPal.

## API Workflow
1. Client: Sebuah aplikasi atau perangkat lunak yang ingin mengakses data atau fitur dari aplikasi lain.
2. Request: Client mengirimkan request ke API melalui HTTP. Request ini biasanya menyertakan informasi seperti alamat endpoint API, metode HTTP, dan data yang diperlukan.
3. Server: Server API menerima request dan memprosesnya. Server mungkin perlu mengakses database atau layanan lain untuk mendapatkan data yang diminta.
4. Respons: Server mengirimkan respons kembali ke Client. Respons ini biasanya berisi data yang diminta dalam format JSON atau XML.
5. Client: Client menerima respons dan memprosesnya. Client kemudian dapat menggunakan data ini untuk berbagai keperluan.

## REST API
RESTful API adalah jenis API yang didasarkan pada prinsip-prinsip Representational State Transfer (REST), yang merupakan gaya arsitektur untuk merancang sistem berbasis web yang scalable dan fleksibel. RESTful API menggunakan metode HTTP untuk mengakses dan memanipulasi sumber daya, dan menggunakan representasi sederhana seperti JSON atau XML untuk berkomunikasi antara klien dan server.

### HTTP Method
Metode HTTP adalah bagian dari protokol komunikasi HTTP (Hypertext Transfer Protocol) yang digunakan untuk mentransfer data antara klien (seperti browser web) dan server web. Metode HTTP menentukan jenis tindakan yang ingin dilakukan oleh klien terhadap sumber daya yang diidentifikasi oleh URL. Berikut adalah beberapa metode HTTP yang umum digunakan:

1. GET: Metode GET digunakan untuk meminta data dari sumber daya tertentu di server. Permintaan GET hanya mengambil data dari server dan tidak mengubahnya. Metode ini umumnya digunakan untuk mengambil halaman web, gambar, atau file lainnya.

2. POST: Metode POST digunakan untuk mengirim data ke server untuk diproses. Permintaan POST sering digunakan untuk mengirim data formulir dari browser ke server, seperti saat mengirim email atau membuat entri dalam basis data.

3. PUT: Metode PUT digunakan untuk mengirimkan data baru ke server atau memperbarui data yang ada. Permintaan PUT digunakan untuk membuat atau memperbarui sumber daya dengan data yang dikirimkan sebagai bagian dari permintaan.

4. DELETE: Metode DELETE digunakan untuk menghapus sumber daya tertentu dari server. Permintaan DELETE menghapus sumber daya yang diidentifikasi oleh URL dari server.

5. PATCH: Metode PATCH digunakan untuk memperbarui bagian tertentu dari sumber daya yang ada di server. Permintaan PATCH mengirimkan data yang berisi perubahan yang harus diterapkan pada sumber daya yang ditentukan.