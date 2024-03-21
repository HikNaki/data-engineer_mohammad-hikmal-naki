# Soal Prioritas 2

## Melakukan containerization dengan docker compose

### 1. Menyiapkan file project aplikasi

Project Structure
![Gambar 1](../Screenshots/02/01_Gambar.png)

### 2. Code
- **app.py**

```
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello Guys! I have been seen {} times.\n'.format(count)
```

- **requirements.txt**

```
flask
redis
```

- **Dockerfile**

```
FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

- **compose.yml**

```
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_DEBUG: "true"
  redis:
    image: "redis:alpine"
```

### 3.Run container via docker compose
Melakukan build app dalam container via docker compose dengan perintah berikut:

```
docker compose up -d
```
![Gambar 2](../Screenshots/02/02_Gambar.png)

Memverifikasi container yang telah dibuat menggunakan perintah berikut:
```
docker container ls
```
![Gambar 3](../Screenshots/02/03_Gambar.png)

### 4. Run the application
Menjalankan aplikasi web python pada browser dengan url berikut:

```
http://127.0.0.1:8000/
```

![Gambar 4](../Screenshots/02/04_Gambar.png)
Refresh halaman web untuk melakukan increment pada angka.

### 5. Stop the application
Menghentikan aplikasi dengan menggunakan perintah berikut:
```
docker compose down
```
![Gambar 5](../Screenshots/02/05_Gambar.png)
