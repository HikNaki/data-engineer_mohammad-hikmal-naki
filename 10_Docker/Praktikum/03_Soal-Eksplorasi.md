# Soal Eksplorasi

## Membuat aplikasi ETL dengan python dan docker

### 1. Menyiapkan file project aplikasi

**Project Structure**
![Gambar 1](../Screenshots/03/01_Gambar.png)

File project: [dev-etl](https://github.com/HikNaki/dev-etl.git)

- Folder mysql terdapat file `init.sql` untuk create database baru.
- Folder mysql_data digunakan sebagai volume untuk database.
- File `.env` digunakan untuk menyimpan environment variables.
- File `requirements.txt` berisi list dependencies python yang dibutuhkan.
- File `main.py` berisi kode aplikasi ETL python.
- File `Dockerfile` berisi script untuk membuat sebuah image.
- File `compose.yml` berisi konfigurasi layanan aplikasi yang ingin dibuat.

### 2. Build app via docker compose

Setelah membuat file docker-compose.yml, selanjutnya menjalankan Docker Compose dengan perintah:

```
docker compose up -d
```

![Gambar 2](../Screenshots/03/02_Gambar.png)
Untuk memastikan aplikasi telah berhasil dijalankan via Docker Compose, tuliskan perintah berikut:

```
docker compose ps
```

![Gambar 3](../Screenshots/03/03_Gambar.png)

### 3. Test the application
Memeriksa output logs dari aplikasi apakah berhasil berjalan dengan baik menggunakan perintah berikut:
```
docker logs <nama container>
```
1. Output logs dari container database
![Gambar 4](../Screenshots/03/04_Gambar.png)

2. Output logs dari container aplikasi ETL
![Gambar 5](../Screenshots/03/05_Gambar.png)

Memeriksa database mysql untuk memeriksa apakah data telah berhasil dimasukkan.
![Gambar 6](../Screenshots/03/06_Gambar.png)
![Gambar 7](../Screenshots/03/07_Gambar.png)
![Gambar 8](../Screenshots/03/08_Gambar.png)


### 4. Stop the application
Menghentikan aplikasi dengan menggunakan perintah berikut:
```
docker compose down
```
![Gambar 9](../Screenshots/03/09_Gambar.png)