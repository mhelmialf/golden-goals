# ✨ GOLDEN GOALS ✨
## *Where Football Dreams Become Yours*

#### Name      : Muhammad Helmi Alfarissi
#### NPM       : 2406402416
#### Class     : PBP D
#### Link Live : [Golden Goals Site](https://muhammad-helmi41-goldengoals.pbp.cs.ui.ac.id/)

### History Tugas
- [**Tugas 2 - PBP 2025/2026**](https://github.com/mhelmialf/golden-goals/wiki/Tugas-2-%E2%80%90-PBP-2025-2026)
- [**Tugas 3 - PBP 2025/2026**](https://github.com/mhelmialf/golden-goals/wiki/Tugas-3-%E2%80%90-PBP-2025-2026)
- [**Tugas 4 - PBP 2025/2026**](https://github.com/mhelmialf/golden-goals/wiki/Tugas-4-%E2%80%90-PBP-2025-2026)
- - [**Tugas 5 - PBP 2025/2026**](https://github.com/mhelmialf/golden-goals/wiki/Tugas-5-%E2%80%90-PBP-2025-2026)
---

## Tugas 5 - PBP 2025/2026

## 🔄 Perbedaan Antara Synchronous dan Asynchronous Request
   Synchronous dan asynchronous adalah dua model komunikasi antara client (browser) dan server, dengan perbedaan utama pada cara mereka menangani alur kerja.
   1. Synchronous Request (Blocking):
   - Alur Kerja: Saat client mengirim request, ia akan berhenti dan menunggu sampai server mengirimkan response secara penuh. Selama menunggu, pengguna tidak dapat berinteraksi dengan halaman web (UI akan "freeze").
   - Analogi: Seperti menelepon seseorang dan harus menunggu di telepon sampai orang tersebut selesai berbicara sebelum Anda bisa melakukan hal lain.
   - Contoh: Klik sebuah link yang membuka halaman baru. Browser akan memuat dari awal, dan Anda tidak bisa melakukan apa-apa sampai halaman selesai dimuat.

   2. Asynchronous Request (Non-blocking):
   - Alur Kerja: Saat client mengirim request, ia tidak perlu menunggu response dari server. Pengguna dapat terus berinteraksi dengan halaman web sementara proses berjalan di latar belakang. Ketika response diterima, hanya bagian tertentu dari halaman yang akan diperbarui.
   - Analogi: Seperti mengirim pesan teks (chat). Anda bisa mengirim pesan lalu melanjutkan aktivitas lain. Notifikasi akan muncul saat pesan balasan tiba.
   - Contoh: Infinite scroll di media sosial, di mana konten baru dimuat di bagian bawah tanpa me-reload seluruh halaman.

## ⚙️ Alur Kerja AJAX di Django (Request-Response Flow)
   AJAX (Asynchronous JavaScript and XML) memungkinkan halaman web untuk berkomunikasi dengan server secara asynchronous. Di Django, alurnya adalah sebagai berikut:
   - Client (Browser) Memicu Event:
   - Aksi pengguna (misalnya, klik tombol, mengisi form) memicu sebuah fungsi JavaScript.
   - JavaScript Mengirim Request:
      - JavaScript, menggunakan fetch() API atau XMLHttpRequest, mengirim request HTTP (biasanya GET atau POST) ke sebuah URL spesifik di aplikasi Django. Data dari form dapat dikirim bersama request ini.
   - Django Menerima dan Memproses Request:
   - URL Routing: File urls.py Django mencocokkan URL dari AJAX request dan meneruskannya ke fungsi view yang sesuai.   
   - View Logic: View di views.py memproses request tersebut. Ini bisa berupa mengambil data dari database, memvalidasi input, atau melakukan operasi lainnya.
   - Mengembalikan Response: Alih-alih me-render template HTML lengkap, view mengembalikan data dalam format yang ringan seperti JSON menggunakan JsonResponse.
   - Client Menerima Response dan Memperbarui UI:
   - Fungsi JavaScript yang tadi mengirim request menerima data JSON dari Django.   
   - JavaScript kemudian menggunakan data ini untuk memanipulasi DOM (Document Object Model), yaitu memperbarui atau mengubah bagian tertentu dari halaman HTML tanpa perlu me-reload seluruh halaman.

## ✨ Keuntungan Menggunakan AJAX Dibandingkan Render Biasa
   Menggunakan AJAX di Django memberikan beberapa keuntungan signifikan dibandingkan dengan metode render halaman tradisional:
   - Pengalaman Pengguna (UX) yang Lebih Baik: Aplikasi terasa lebih cepat dan responsif karena tidak ada full page reload yang mengganggu alur kerja pengguna.
   - Mengurangi Beban Server & Bandwidth: Hanya data yang relevan (biasanya dalam format JSON yang ringan) yang ditransfer antara client dan server, bukan seluruh file HTML dan asetnya.
   - Interaksi Real-time: Memungkinkan pengembangan fitur dinamis seperti notifikasi live, chat, auto-complete pada kolom pencarian, dan validasi form secara instan.
   - Pemisahan Logika yang Lebih Jelas: Memisahkan antara logika backend (yang hanya menyediakan data via API) dan frontend (yang mengatur tampilan dan interaksi pengguna).

## 🔒 Keamanan AJAX untuk Fitur Login dan Register di Django
   Mengamankan fitur otentikasi yang menggunakan AJAX sangat penting. Berikut adalah langkah-langkah kunci yang harus diterapkan di Django:
   - Gunakan HTTPS: Selalu gunakan koneksi terenkripsi (HTTPS/SSL) untuk melindungi data sensitif seperti password dari serangan man-in-the-middle saat transit.
   - Manfaatkan CSRF Protection Django:
      - Pastikan AJAX request (terutama POST) menyertakan CSRF token. JavaScript dapat mengambil token ini dari cookie atau dari elemen tersembunyi di dalam form dan mengirimkannya sebagai header (X-CSRFToken).
   - Selalu Gunakan Method POST: Kirim data kredensial (username, password) menggunakan metode HTTP POST, bukan GET, agar tidak terekspos di URL atau log server.
   - Validasi di Sisi Server: Jangan pernah percaya input dari sisi client. Lakukan validasi ulang semua data (format email, kekuatan password, dll.) di dalam view Django sebelum memprosesnya.
   - Gunakan Framework Otentikasi Bawaan Django: Manfaatkan django.contrib.auth untuk menangani hashing password, manajemen sesi, dan proses otentikasi lainnya karena sudah teruji keamanannya.

## 🧑‍💻 Pengaruh AJAX pada User Experience (UX)
   AJAX secara fundamental mengubah cara pengguna berinteraksi dengan website, menghasilkan UX yang jauh lebih baik dan modern:
   - Responsivitas Instan: Aksi pengguna seperti menyukai postingan, menambahkan item ke keranjang belanja, atau mengirim komentar dapat terjadi seketika tanpa jeda untuk memuat ulang halaman. Ini membuat website terasa seperti aplikasi desktop.
   - Alur Kerja yang Tidak Terputus: Pengguna tetap berada di konteks yang sama. Misalnya, saat mengisi form yang panjang, validasi error bisa ditampilkan per-kolom tanpa harus me-reload dan kehilangan data yang sudah diisi.
   - Mengurangi Waktu Tunggu: Dengan memuat data di latar belakang, pengguna dapat terus menavigasi halaman sementara konten tambahan (seperti gambar atau data) sedang disiapkan.
   - Meningkatkan Keterlibatan Pengguna: Fitur interaktif seperti live search (hasil pencarian muncul saat mengetik) atau infinite scroll membuat pengguna lebih terlibat dan menghabiskan lebih banyak waktu di situs.

   Singkatnya, AJAX adalah kunci untuk menciptakan aplikasi web yang dinamis, cepat, dan modern yang memenuhi ekspektasi pengguna saat ini.