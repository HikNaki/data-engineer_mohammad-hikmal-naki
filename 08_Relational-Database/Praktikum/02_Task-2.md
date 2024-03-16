# Data Definition Language

### 1. Create database alta_online_shop.

### 2. Create table di database

a. Create table user.

```
CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    address VARCHAR(50),
    date_of_birth DATE,
    user_status VARCHAR(50) NOT NULL,
    gender ENUM('Pria', 'Wanita') NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

b. Create table product, product type, operators, product description, payment_method.

```
CREATE TABLE product_type (
    product_type_id INT AUTO_INCREMENT PRIMARY KEY,
    product_type VARCHAR(50)
);

CREATE TABLE product_description (
    product_description_id INT AUTO_INCREMENT PRIMARY KEY,
    product_description TEXT
);

CREATE TABLE operator (
    operator_id INT AUTO_INCREMENT PRIMARY KEY,
    operator_name VARCHAR(50)
);

CREATE TABLE payment_method (
    payment_method_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_method VARCHAR(50)
);

CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    product_type_id INT NOT NULL,
    product_description_id INT NOT NULL,
    operator_id INT NOT NULL,
    payment_method_id INT NOT NULL,
    FOREIGN KEY (product_type_id)
        REFERENCES product_type (product_type_id),
    FOREIGN KEY (product_description_id)
        REFERENCES product_description (product_description_id),
    FOREIGN KEY (operator_id)
        REFERENCES operator (operator_id),
    FOREIGN KEY (payment_method_id)
        REFERENCES payment_method (payment_method_id)
);
```

c. Create table transaction, transaction detail.

```
CREATE TABLE transaction (
transaction_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
transaction_date DATE NOT NULL,
total_amount DECIMAL(10 , 2 ) NOT NULL,
FOREIGN KEY (user_id)
REFERENCES user (user_id)
);

CREATE TABLE transaction_detail (
detail_id INT AUTO_INCREMENT PRIMARY KEY,
transaction_id INT NOT NULL,
product_id INT NOT NULL,
quantity INT,
unit_price DECIMAL(10 , 2 ),
subtotal DECIMAL(10 , 2 ),
FOREIGN KEY (transaction_id)
REFERENCES transaction (transaction_id),
FOREIGN KEY (product_id)
REFERENCES product (product_id)
);

```

### 3. Create tabel kurir dengan field id, name, created_at, updated_at.
```
CREATE TABLE kurir (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

```

### 4. Tambahkan ongkos_dasar column di tabel kurir.
```
ALTER TABLE kurir
ADD ongkos_dasar DECIMAL(10, 2);
```
### 5. Rename tabel kurir menjadi shipping.
```
RENAME TABLE kurir TO shipping;

```
### 6. Hapus / Drop tabel shipping karena ternyata tidak dibutuhkan.
```
DROP TABLE IF EXISTS shipping;
```
### 7. Silahkan menambahkan entity baru dengan relation 1-to-1, 1-to-many, many-to-many. Seperti:
a. 1-to-1: payment method description.
```
CREATE TABLE Payment_Method_Description (
    payment_method_id INT PRIMARY KEY,
    description TEXT,
    FOREIGN KEY (payment_method_id) REFERENCES payment_method(payment_method_id)
);

```
b. 1-to-many: user dengan alamat.
```
CREATE TABLE address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    address VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

```
c. many-to-many: user dengan payment method menjadi user_payment_method_detail.
```
CREATE TABLE user_payment_method_detail (
    user_payment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    payment_method_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_method(payment_method_id)
);

```
### Gambar EER Diagram
![EER Diagram](../Screenshots/03_EER-Diagram.png)