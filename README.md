# ✨ GOLDEN GOALS ✨
## *Where Football Dreams Become Yours*

#### Name      : Muhammad Helmi Alfarissi
#### NPM       : 2406402416
#### Class     : PBP D
#### Link Live : [Golden Goals Site](https://muhammad-helmi41-goldengoals.pbp.cs.ui.ac.id/)

### History Tugas
- [**Tugas 2 - PBP 2025/2026**](https://github.com/mhelmialf/golden-goals/wiki/Tugas-2-%E2%80%90-PBP-2025-2026)

---

## Tugas 3 - PBP 2025/2026

### 💻 Langkah Pengimplementasian Proyek Django Secara Step-by-Step 

1. **Membuat repository baru di GitHub dan menyiapkan virtual environment.**
   - Buat repository baru di GitHub untuk menyimpan proyek.
   - Buat virtual environment di perangkat lokal agar dependencies proyek terisolasi dari package dan proyek lain, menggunakan perintah `python -m venv env` dan mengaktifkannya `env\Scripts\activate`.
   - Hubungkan repository GitHub dengan repository lokal menggunakan Git.

2. **Menyiapkan _dependencies_ dan membuat sebuah proyek Django baru.**
   - Membuat file `requirements.txt` yang berisikan _dependencies_ yang diperlukan dalam proyek Django. Lalu melakukan instalasi menggunakan perintah `pip install -r requirements.txt`.
   - Menginisialisasi proyek Django baru dengan perintah `django-admin startproject golden_goals` untuk membuat proyek dengan struktur direktori dasar Django.

3. **Membuat aplikasi dengan nama `main` pada proyek tersebut.**
   - Setelah proyek dibuat, tambahkan aplikasi baru bernama `main` dengan perintah `python manage.py startapp main` yang akan menampung logika dan fitur yang dikembangkan dalam proyek.

4. **Menyesuaikan credential database dengan schema `tugas_individu`.**
   - Membuat file `.env.prod` di proyek Django, lalu sesuaikan konfigurasi `DATABASES` dengan username, password, nama database, dan host sesuai schema `tugas_individu` yang sudah disediakan.

5. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
   - Dalam berkas `urls.py` proyek, tambahkan rute (route) untuk mengarahkan permintaan (request) ke aplikasi `main`. Ini memastikan aplikasi `main` terhubung dan dapat dijalankan.

6. **Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**
   - Pada `models.py` di dalam aplikasi "main", buat model `Product` yang mewakili entitas produk. Model ini akan memiliki atribut yang wajib seperti `name`, `description`, `price`, dan sebagainya, yang akan digunakan untuk menyimpan data produk ke dalam database.

7. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi dan data diri.**
   - Di `views.py`, buat fungsi yang akan merender template HTML. Template ini akan menampilkan informasi seperti nama aplikasi, nama kamu, dan kelas, yang akan diambil oleh fungsi tersebut.

8. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
   - Di `urls.py` pada aplikasi "main", tambahkan rute baru yang akan memetakan URL ke fungsi di `views.py`. Hal ini memungkinkan pengguna untuk mengakses halaman yang telah dibuat melalui URL yang sesuai.

9. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga dapat diakses melalui Internet.**
   - Setelah aplikasi selesai, lakukan deployment ke Pacil Web Service (PWS). Ini melibatkan mengunggah proyek ke server PWS sehingga aplikasi dapat diakses melalui Internet. Dan menjalankan beberapa perintah deployment seperti `git push pws master`

10. **Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan Tugas 2.**
   - Buat file `README.md` yang berisi deskripsi proyek, tautan ke aplikasi yang sudah dideploy di PWS, serta jawaban dari pertanyaan tentang Django dan fungsionalitasnya.

### 🔁 Bagan & Penjelasan Alur Django
<img width="2388" height="1002" alt="Django Workflow" src="https://github.com/user-attachments/assets/bba7ace0-995d-4b1b-b1d4-732fe3e002d8" />

1. **Client Side**
   - Proses dimulai ketika client (misalnya browser pengguna) mengirimkan HTTP Request melalui Internet untuk mengakses aplikasi web.
2. **Internet → Webserver Side (Django)**
   - Request tersebut sampai ke server yang menjalankan framework Django. Django kemudian memproses request tersebut melalui beberapa tahapan.
3. **`manage.py`**
   - File `manage.py` bertugas menjalankan perintah Django, termasuk menyalurkan request ke sistem URL routing.
4. **`urls.py`**
   - File `urls.py` menentukan rute (URL pattern) yang sesuai dengan request dari client. Jika ada kecocokan, request diteruskan ke fungsi yang ada di `views.py`.
5. **`views.py`**
   - `views.py` berisi logika untuk menangani request. Jika membutuhkan data, `views.py` akan berkomunikasi dengan `models.py`.
6. **`models.py` & Database**
   - `models.py` merepresentasikan struktur tabel di database. Jika `views.py` membutuhkan data, ia akan memanggil `models.py`, yang kemudian mengakses database untuk mengambil, menambah, atau mengubah data.
7. **`templates`**
   - Setelah logika selesai dijalankan, `views.py` akan merender template HTML dari folder templates. Data yang diambil dari database dapat dimasukkan ke dalam template ini.
8. **Response ke Client**
   - Django kemudian mengirimkan hasil render template (berupa halaman web) kembali melalui Internet.
   - Client menerima HTTP Response berupa halaman web yang bisa dilihat di browser.

### ⚙️ Peran `settings.py` dalam Proyek Django

Dalam proyek Django, `settings.py` berperan sebagai pusat konfigurasi utama. File ini dibuat otomatis saat menjalankan   `django-admin startproject`. Semua pengaturan yang mengatur perilaku proyek ada di sini. Berikut ini adalah beberapa peran penting `settings.py`:
1. **Konfigurasi Database**
   - Menentukan jenis database (PostgreSQL, MySQL, SQLite, dll.), nama database, username, password, host, dan port.
2. **Aplikasi yang Digunakan (`INSTALLED_APPS`)**
   - Menyimpan daftar aplikasi bawaan Django maupun aplikasi kustom (misalnya main) yang dipakai di proyek.
3. **Middleware**
   - Mengatur middleware, yaitu lapisan yang memproses request/response secara global sebelum masuk ke view atau setelah keluar dari view.
4. **Konfigurasi Template**
   - Menentukan direktori template HTML dan cara Django merendernya.
5. **Konfigurasi Static & Media Files**
   - Menentukan lokasi file statis (CSS, JS, gambar) serta file yang di-upload pengguna.
6. **Security & Debugging**
   - Menyimpan `SECRET_KEY` untuk keamanan, serta flag `DEBUG` (True/False) untuk mengatur mode pengembangan atau produksi.
   - Menentukan `ALLOWED_HOSTS` agar hanya domain tertentu yang bisa mengakses aplikasi.
7. **Pengaturan Internasionalisasi**
   - Zona waktu (`TIME_ZONE`), bahasa (`LANGUAGE_CODE`), dan pengaturan format lokal lain.

### 🗃️ Cara Kerja Migrasi Database di Django

Migrasi database di Django adalah mekanisme untuk memastikan struktur database selalu selaras dengan definisi model di `models.py`. Saat developer menambahkan atau mengubah model, Django tidak langsung mengubah database, melainkan membuat file migrasi terlebih dahulu dengan perintah `python manage.py makemigrations`. File ini berisi instruksi perubahan, misalnya membuat tabel baru atau menambah kolom. Setelah itu, perintah `python manage.py migrate` digunakan untuk mengeksekusi instruksi tersebut sehingga database benar-benar diperbarui. Riwayat migrasi juga dicatat pada tabel khusus `django_migrations`, sehingga Django dapat melacak migrasi mana yang sudah diterapkan. Dengan begitu, migrasi berperan sebagai penghubung otomatis antara model Python dan struktur database, sekaligus memudahkan pengelolaan perubahan skema tanpa menulis query SQL manual.

### 💡 Alasan Framework Django dijadikan Permulaan Pembelajaran Pengembangan *Software*

Django sering dijadikan permulaan dalam pembelajaran pengembangan _software_ karena mudah dipahami, memiliki dokumentasi yang lengkap, serta sudah menyediakan banyak fitur bawaan (_batteries included_) seperti autentikasi, ORM, dan manajemen routing. Framework ini berbasis Python yang ramah pemula, sehingga transisi dari belajar dasar bahasa pemrograman ke membangun aplikasi web menjadi lebih mudah. Selain itu, Django mengajarkan konsep penting seperti MVT pattern, pengelolaan database, dan praktik software development yang baik, sehingga cocok sebagai dasar sebelum mempelajari framework lain yang lebih kompleks.

### 📝 Feedback Asisten Dosen Tutorial 1

Asisten dosen pada tutorial 1 memberikan pendampingan yang sangat baik. Dokumen tutorial yang disusun sudah komprehensif dan mudah dipahami, sehingga mahasiswa yang belum memiliki dasar web development pun dapat mengikuti langkah-langkahnya dengan baik. Selain itu, meskipun sesi tutorial dilakukan secara daring, asisten dosen tetap stand by dan selalu siap membantu ketika kami mengalami kesulitan dalam pengerjaan.

