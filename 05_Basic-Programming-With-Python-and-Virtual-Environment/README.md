# (5) Basic Programming With Python and Virtual Environment

### What is Virtual Environment?
Virtual Environment adalah lingkungan terisolasi yang memungkinkan kita untuk mengisolasi project Python dengan dependency dan package tertentu. Dengan adanya virtual environment kita dapat memiliki versi package yang berbeda untuk setiap project, tanpa konflik antar project. Ini membantu menghindari masalah di mana satu project menggunakan versi tertentu dari sebuah package, sementara project lain menggunakan versi yang berbeda.

### Why do we need Virtual Environment?
1. Dependency Isolation
2. Version Control
3. Cleaner Global Environment
4. Reproducibility
5. Security
6. Efficient Resource Management
7. Collaboration
8. Cross-Platform Compatibility

## Creating Virtual Environment with Windows
Berikut adalah langkah-langkah untuk membuat Virtual Environment di windows 11 :
1. Kita dapat membuat virtual environment dengan menjalankan perintah berikut di CMD :
```
python -m venv myenv
```
`myenv` adalah nama direktori untuk virtual environment yang baru saja dibuat. Kita dapat menggantinya dengan nama apa pun yang kita inginkan.

2. Untuk mengaktifkan virtual environment yang baru saja kita buat, jalankan perintah berikut di CMD :
```
myenv\Scripts\activate
```
Ini akan mengubah prompt perintah, menambahkan nama virtual environment di depannya, menandakan bahwa virtual environment aktif.

3. Untuk keluar dari virtual environment, Anda dapat menjalankan perintah:
```
deactivate
```
Ini akan mengembalikan prompt perintah ke keadaan semula.
