# ✨ GOLDEN GOALS ✨
## *Where Football Dreams Become Yours*

#### Name      : Muhammad Helmi Alfarissi
#### NPM       : 2406402416
#### Class     : PBP D
#### Link Live : [Golden Goals Site](https://muhammad-helmi41-goldengoals.pbp.cs.ui.ac.id/)

### History Tugas
- [**Tugas 2 - PBP 2025/2026**](https://github.com/mhelmialf/golden-goals/wiki/Tugas-2-%E2%80%90-PBP-2025-2026)
- [**Tugas 3 - PBP 2025/2026**](https://github.com/mhelmialf/golden-goals/wiki/Tugas-3-%E2%80%90-PBP-2025-2026)
---

## Tugas 4 - PBP 2025/2026

### 🗃️ Django `AuthenticationForm` beserta kelebihan dan kekurangannya.

`AuthenticationForm` adalah form bawaan Django (dari `django.contrib.auth.forms`) yang dipakai untuk proses login pengguna. Fungsinya adalah untuk memvalidasi apakah Username yang dimasukkan ada di database, Password yang dimasukkan cocok dengan user tersebut. dan Akun user aktif (tidak dinonaktifkan). Berikut ini adalah contoh pemakaian `AuthenticationForm` pada Tugas 4:

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Adapun kelebihan dan kekurangan dari `AuthenticationForm` pada Django adalah sebagai berikut:
1. **Kelebihan `AuthenticationForm`**
   - Built-in Django → langsung bisa dipakai tanpa bikin form sendiri.
   - Aman secara default. Hashing password otomatis. Validasi login hanya untuk akun aktif. Terintegrasi dengan sistem session Django.
   - Cepat digunakan → sangat cocok kalau butuh login sederhana.
   - Terintegrasi dengan sistem user Django → tidak perlu manual query user.
   - Bisa dikustomisasi → bisa di-override untuk menambah field baru (misalnya “Remember me”).

2. **Kekurangan `AuthenticationForm`**
   - Kurang fleksibel untuk UI custom. Kalau mau tampilan login unik, form ini kadang terasa kaku, karena field default-nya hanya username & password.
   - Tidak mendukung login alternatif (misalnya login pakai email, nomor HP, atau OTP) tanpa modifikasi tambahan.
   - Error message default kurang ramah → biasanya terlalu “teknis” buat end-user, jadi sering perlu dikustomisasi.
   - Tidak ada fitur tambahan bawaan seperti “Remember Me”, “Login with Google/Facebook” — harus implementasi manual.

### 🗒️ Perbedaan antara autentikasi dan otorisasi, serta pengimplementasiannya dalam Django
*Autentikasi* adalah proses memverifikasi identitas pengguna, yaitu memastikan apakah seseorang benar-benar adalah dirinya, misalnya melalui login dengan username dan password, email dengan OTP, atau Google Sign-In. Jika berhasil, sistem dapat mengenali pengguna tersebut, misalnya “Oh ini Helmi dengan user id 7.” 

Sementara itu, *otorisasi* adalah proses menentukan hak akses pengguna, yaitu memastikan apa saja yang boleh dilakukan setelah identitasnya terverifikasi. Contohnya, pengguna biasa hanya bisa melihat produk, sedangkan admin bisa menambah atau menghapus produk. Dengan demikian, autentikasi menjawab pertanyaan “Who are you?” sedangkan otorisasi menjawab pertanyaan “What can you do?”

**Implementasi di Django**
1. Autentikasi di Django
   - Django punya authentication system di django.contrib.auth.
   - Komponen penting:
      - User model: menyimpan username, password (hashed), email, dsb.
      - AuthenticationForm: memvalidasi username & password.
      - authenticate(): fungsi untuk cek kredensial.
      - login(request, user): membuat sesi login.
      - logout(request): menghapus sesi login.
   - Setelah login sukses, request.user akan berisi objek User (kalau belum login → AnonymousUser).

2. Otorisasi di Django
   - Django punya sistem permissions & groups.
   - Cara bawaan:
      - is_authenticated → cek apakah user login.
      - is_staff → cek apakah user bisa akses admin site.
      - is_superuser → punya semua izin.
      - Model-level permissions → otomatis dibuat (misalnya add_product, change_product, delete_product).
      - Bisa juga bikin permission custom.

### ✅ Kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web
Cookies adalah data kecil yang disimpan di sisi browser (client), biasanya dipakai untuk menyimpan informasi sederhana.l
1. Kelebihan
   - Mudah diakses client & server → bisa dipakai langsung di browser (JavaScript) maupun dikirim otomatis ke server di setiap request.
   - Tidak butuh penyimpanan server → karena data disimpan di client, server lebih ringan.
   - Bisa digunakan lintas request & domain tertentu → cocok buat tracking atau preferensi user (misalnya bahasa, tema).

2. Kekurangan
   - Ukuran terbatas (± 4KB per cookie).
   - Kurang aman → data bisa dibaca/diedit user, sehingga tidak cocok untuk informasi sensitif (kecuali dienkripsi).
   - Selalu dikirim di setiap request ke domain terkait → bisa memperbesar payload.
   - Rentan serangan (misalnya XSS atau cookie theft).

Session adalah mekanisme penyimpanan state di server, sedangkan client hanya menyimpan ID session (biasanya lewat cookie bernama sessionid).
1. Kelebihan
   - Lebih aman → data sensitif tidak disimpan di client, hanya ID acak.
   - Ukuran lebih fleksibel → data bisa besar karena disimpan di server (database, cache, file system).
   - Cocok untuk autentikasi & state kompleks → misalnya keranjang belanja, data user login.

2. Kekurangan
   - Butuh resource server → semakin banyak user, semakin besar beban penyimpanan.
   - Bergantung pada session management → kalau server down atau tidak konsisten (misalnya load balancing tanpa session sharing), user bisa kehilangan state.
   - Membutuhkan cookie/URL parameter untuk menyimpan session ID → kalau cookie mati, harus pakai cara lain (URL rewriting).

### 🔐 Keamanan penggunaan cookies secara default dalam pengembangan web, serta penanganannya dalam Django
Secara default, cookies tidak sepenuhnya aman, karena:
   - Terlihat & bisa dimodifikasi oleh client → user atau attacker bisa baca/ubah isinya.
   - Terkirim di setiap request → termasuk ke endpoint berbahaya jika domain tidak dibatasi.
   - Risiko serangan XSS (Cross-Site Scripting) → attacker bisa mencuri cookie lewat JavaScript.
   - Risiko CSRF (Cross-Site Request Forgery) → attacker bisa pakai cookie session user untuk menjalankan aksi berbahaya tanpa sepengetahuan user.
Jadi, cookies tidak otomatis aman. Perlu konfigurasi ekstra agar tidak disalahgunakan.

Django memberikan mekanisme keamanan bawaan untuk mengurangi risiko tersebut:
1. Session framework
   - Django tidak menyimpan data sensitif langsung di cookie.
   - Hanya ID session acak (sessionid) yang disimpan di cookie, data sebenarnya ada di server.
2. `HttpOnly` flag (default `True`)
   - Membuat cookie tidak bisa diakses lewat JavaScript (document.cookie), sehingga melindungi dari pencurian via XSS.
3. Secure flag
   - Kalau diaktifkan (`SESSION_COOKIE_SECURE` = `True`), cookie hanya dikirim lewat HTTPS, sehingga tidak bocor lewat HTTP biasa.
4. `SameSite` attribute
   - Django default pakai Lax, mencegah cookie terkirim di request lintas situs yang berpotensi CSRF.
   - Bisa diubah dengan `SESSION_COOKIE_SAMESITE` = `Strict` atau `None` sesuai kebutuhan.
5. CSRF protection
   - Django otomatis menambahkan token CSRF untuk form POST, sehingga walaupun session cookie ada, attacker tetap tidak bisa eksekusi aksi tanpa token valid.

### 💻 Langkah Pengimplementasian Proyek Django Tugas 4 Secara Step-by-Step 

1. **Membuat fungsi registrasi akun pada `views.py`.**
   
   1. Mengimport `UserCreationForm` dan `messages` pada `views.py`
      ```python
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages
      ```

   2. Membuat fungsi `register` pada `views.py` untuk user membuat akun
         ```python
         def register(request):
            form = UserCreationForm()

            if request.method == "POST":
               form = UserCreationForm(request.POST)
               if form.is_valid():
                     form.save()
                     messages.success(request, 'Your account has been successfully created!')
                     return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
         ```

   3. Membuat file `register.html` pada direktori `main/templates` untuk tampilan form user registration, dan mengisinya dengan tampilan HTML untuk form registrasi
      ```html
      {% extends 'base.html' %}

      {% block meta %}
      <title>Register</title>
      {% endblock meta %}

      {% block content %}

      <div>
      <h1>Register</h1>

      <form method="POST">
         {% csrf_token %}
         <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
         </table>
      </form>

      {% if messages %}
      <ul>
         {% for message in messages %}
         <li>{{ message }}</li>
         {% endfor %}
      </ul>
      {% endif %}
      </div>

      {% endblock content %}
      ```
   
   4. Membuat routing URL untuk fungsi `register` yang ditambahkan di `views.py` pada `main/urls.py`
      1. Mengimport fungsi `register` pada `main/urls.py`
         ```python
         from django.urls import path
         from main.views import register
         ```

      2. Menambahkan path URL fungsi `register` ke dalam `urlpatterns` 
         ```python
         app_name = 'main'

         urlpatterns = [
            path('', show_main, name='show_main'),
            path('register/', register, name='register')
         ]
         ```

2. **Membuat fungsi login user pada `views.py`.**
   
   1. Mengimport `authenticate`, `login`, dan `AuthenticationForm` pada `views.py`
      ```python
      from django.contrib.auth.forms import AuthenticationForm
      from django.contrib.auth import authenticate, login
      ```

   2. Membuat fungsi `login_user` pada `views.py` untuk proses login user
      ```python
      def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  return redirect('main:show_main')

         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)
      ```

   3. Membuat file `login.html` pada direktori `main/templates` untuk tampilan form user login, dan mengisinya dengan tampilan HTML untuk form login
      ```html
      {% extends 'base.html' %}

      {% block meta %}
      <title>Login</title>
      {% endblock meta %}

      {% block content %}
      <div class="login">
      <h1>Login</h1>

      <form method="POST" action="">
         {% csrf_token %}
         <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
         </table>
      </form>

      {% if messages %}
      <ul>
         {% for message in messages %}
         <li>{{ message }}</li>
         {% endfor %}
      </ul>
      {% endif %} Don't have an account yet?
      <a href="{% url 'main:register' %}">Register Now</a>
      </div>

      {% endblock content %}
      ```

   4. Membuat routing URL untuk fungsi `login` yang ditambahkan di `views.py` pada `main/urls.py`
      1. Mengimport fungsi `login_user` pada `main/urls.py`
         ```python
         from django.urls import path
         from main.views import login_user
         ```

      2. Menambahkan path URL fungsi `login_user` ke dalam `urlpatterns` 
         ```python
         app_name = 'main'

         urlpatterns = [
            path('', show_main, name='show_main'),
            path('login/', login_user, name='login')
         ]
         ```

3. **Membuat fungsi logout user pada `views.py`**
   
   1. Mengimport `logout` digabungkan dengan import `authenticate` dan `login` pada `views.py`
      ```python
      from django.contrib.auth import authenticate, login, logout
      ```

   2. Membuat fungsi `logout_user` pada `views.py` untuk proses logout user
      ```python
      def logout_user(request):
         logout(request)
         return redirect('main:login')
      ```
   
   3. Menambahkan button `logout` dan display `username` pada file `main.html` 
      ```html
      <h1>✨ {{ application }} ✨</h1>
      <h2><i>{{ tagline }}</i></h2>

      <a href="{% url 'main:logout' %}">
      <button>Logout</button>
      </a>

      <h5>Username: {{ username }}</h5>
      <h5>Sesi terakhir login: {{ last_login }}</h5>

      <h2>⚽ Our Products</h2>
      <a href="{% url 'main:add_product' %}">
         <button>+ Add New Product</button>
      </a>
      ```
   
   4. Membuat routing URL untuk fungsi `logout` yang ditambahkan di `views.py` pada `main/urls.py`
      1. Mengimport fungsi `logout_user` pada `main/urls.py`
         ```python
         from django.urls import path
         from main.views import logout_user
         ```

      2. Menambahkan path URL fungsi `logout_user` ke dalam `urlpatterns` 
         ```python
         app_name = 'main'

         urlpatterns = [
            path('', show_main, name='show_main'),
            path('logout/', logout_user, name='logout')
         ]
         ```

4. **Merestriksi akses halaman Main, Product Details, dan fungsi Add Product**
   
   1. Mengimport `login_required` pada `views.py` untuk merestriksi akses beberapa fungsi
      ```python
      from django.contrib.auth.decorators import login_required
      ```

   2. Menambahkan kode `@login_required(login_url='/login')` di atas fungsi yang ingin dibatasi aksesnya pada `views.py`
      1. Restriksi akses fungsi `show_main`
         ```python
         @login_required(login_url='/login')
         def show_main(request):
            products_list = Product.objects.all()
            
            context = {
               'application' : 'Golden Goals',
               'tagline' : 'Where Football Dreams Become Yours',
               'address' : 'Platform 9 ¾, Diagon Alley Football District',
               'instagram' : 'Instagram: @golden.goals',
               'npm' : '2406402416',
               'name': 'Muhammad Helmi Alfarissi',
               'class':'PBP D',
               'products_list': products_list,
               'username': request.user.username,
            }

            return render(request, "main.html", context)
         ```
      
      2. Restriksi akses fungsi `show_detail_product`
         ```python
         @login_required(login_url='/login')
         def show_detail_product(request, id):
            product = get_object_or_404(Product, pk=id)
            product.increment_views()

            context = {
               'product': product
            }

            return render(request, "product_detail.html", context)
         ```

5. **Melakukan penggunaan data dari cookies untuk user login session.**
   
   1. Mengimport `HttpResponseRedirect`, `reverse`, dan `datetime`  di `views.py` untuk setup cookies
      ```python
      import datetime
      from django.http import HttpResponseRedirect
      from django.urls import reverse
      ```

   2. Menambahkan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context` pada fungsi `show_main`
      ```python
      ...

       context = {
        'application' : 'Golden Goals',
        'tagline' : 'Where Football Dreams Become Yours',
        'address' : 'Platform 9 ¾, Diagon Alley Football District',
        'instagram' : 'Instagram: @golden.goals',
        'npm' : '2406402416',
        'name': 'Muhammad Helmi Alfarissi',
        'class':'PBP D',
        'products_list': products_list,
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
      }

      ...
      ```

   3. Mengubah fungsi `login_user` dan `logout_user` untuk menambahkan cookies `last_login`
      1. Mengubah fungsi `login_user`
         ```python
         def login_user(request):
            if request.method == 'POST':
               form = AuthenticationForm(data=request.POST)

               if form.is_valid():
               user = form.get_user()
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main"))
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response

            else:
               form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'login.html', context)
         ```
      
      2. Mengubah fungsi `logout_user`
         ```python
         def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
         ```

   3. Menambahkan tampilan waktu terakhir pengguna login 
      ```html
      <a href="{% url 'main:logout' %}">
      <button>Logout</button>

      </a>
      <h5>Username: {{ username }}</h5>
      <h5>Sesi terakhir login: {{ last_login }}</h5>
      ```

6. **Menghubungkan model `Product` dengan `User`**

   1. Mengimport `User` pada `models.py`
      ```python
      from django.db import models
      from django.contrib.auth.models import User
      ``` 

   2. Menambahkan variabel `user` pada model `Product`
      ```python
      class Product(models.Model):

         ...

         user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      ```

   3. Restriksi akses fungsi `add_product`
         ```python
         @login_required(login_url='/login')
         def add_product(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
               product_entry = form.save(commit = False)
               product_entry.user = request.user
               product_entry.save()
               return redirect('main:show_main')

            context = {'form': form}
            return render(request, "add_product.html", context)

         ```

   4. Memodifikasi fungsi `show_main` untuk dapat difilter berdasarkan user yang login
      ```python
      @login_required(login_url='/login')
      def show_main(request):
         filter_type = request.GET.get("filter", "all")

         if filter_type == "all":
            products_list = Product.objects.all()
         else:
            products_list = Product.objects.filter(user=request.user)
         
         context = {
            'application' : 'Golden Goals',
            'tagline' : 'Where Football Dreams Become Yours',
            'address' : 'Platform 9 ¾, Diagon Alley Football District',
            'instagram' : 'Instagram: @golden.goals',
            'npm' : '2406402416',
            'name': 'Muhammad Helmi Alfarissi',
            'class':'PBP D',
            'products_list': products_list,
            'username': request.user.username,
            'last_login': request.COOKIES.get('last_login', 'Never')
         }

         return render(request, "main.html", context)
      ```

7. **Mengupdate isi file `README.md` yang berisi jawaban dari beberapa pertanyaan Tugas 4.**
   - Buat file `README.md` yang berisi deskripsi proyek, menyantumkan hisory tugas sebelumnya, serta jawaban dari pertanyaan tentang  Django `AuthenticationForm`, autentikasi dan otorisasi, serta session dan cookies. Selain itu, menjelaskan step-by-step proses pengerjaan Tugas 4. 