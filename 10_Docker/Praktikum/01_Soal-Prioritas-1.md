# Soal Prioritas 1

## Melakukan containerization pada aplikasi Python

### 1. Menyiapkan file project aplikasi
**Project Structure**
![Gambar 1](../Screenshots/01/01_Gambar.png)

### 2. Code
- **app.py**

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

- **requirements.txt**

```
flask
```

- **Dockerfile**

```
FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt
RUN pip install --no-cache /wheels/*
EXPOSE 5000
CMD ["python","app.py"]
```

### 3. Build docker image
Membangun docker image menggunakan perintah berikut:

```
docker build -t py-app .
```

![Gambar 2](../Screenshots/01/02_Gambar.png)

Memverifikasi image yang telah di buat, menggunakan perintah berikut:
![Gambar 3](../Screenshots/01/03_Gambar.png)

### 4. Run docker container

- Menjalankan aplikasi python pada container.
- Menambahkan flag `--name` untuk memberikan nama pada container.
- Menambahkan flag `-p` untuk mengatur port yang berjalan di container dengan host.

```
docker run --name pythonapp  -p 5000:5000 py-app
```

![Gambar 4](../Screenshots/01/04_Gambar.png)

### 5. Test the application

Menjalankan aplikasi web python pada browser dengan url berikut:

```
http://127.0.0.1:5000/
```

![Gambar 5](../Screenshots/01/05_Gambar.png)
