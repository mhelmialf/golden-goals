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
---

## Tugas 5 - PBP 2025/2026

### 📈 Urutan prioritas pengambilan CSS selector pada elemen HTML!

1. **Inline style**: Style yang ditulis langsung pada atribut style di elemen HTML memiliki prioritas tertinggi dibandingkan selector lainnya, sehingga selalu diterapkan kecuali ada `!important` yang lebih spesifik.
2. **ID selector**: Selector yang menggunakan ID (#id) memiliki prioritas lebih tinggi dibanding class, pseudo-class, attribute selector, atau type selector.
3. **Class, pseudo-class, dan attribute selector**: Selector seperti `.class`, `atribut="value"`, atau pseudo-class `:hover` memiliki prioritas menengah, lebih rendah dari ID tetapi lebih tinggi dari type selector.
4. **Type selector dan pseudo-element**: Selector berdasarkan tag HTML (`div`, `p`, `h1`) atau pseudo-element (`::before`, `::after`) memiliki prioritas lebih rendah daripada class atau ID selector.
5. **Universal selector dan kombinator**: Selector `*` atau kombinasi seperti `div p` memiliki prioritas paling rendah, sehingga hanya diterapkan jika tidak ada aturan lain yang lebih spesifik.
6. **`!important`**: Deklarasi yang menggunakan `!important` akan mengalahkan semua aturan lain, kecuali ada inline style `!important` yang lebih spesifik.
- **Urutan deklarasi**: Jika dua selector memiliki specificity yang sama, maka aturan yang dideklarasikan terakhir di CSS akan diterapkan pada elemen.

### 🗒️ Pentingnya *responsive design* pada pengembangan Website dan Contoh Aplikasinya
Responsive design menjadi konsep penting dalam pengembangan aplikasi web karena memungkinkan tampilan dan fungsionalitas situs menyesuaikan diri secara otomatis dengan berbagai ukuran layar dan perangkat, seperti desktop, tablet, dan smartphone. Dengan responsive design, pengguna mendapatkan pengalaman yang konsisten, nyaman, dan mudah diakses tanpa harus melakukan zoom atau scroll horizontal yang merepotkan. Selain itu, responsive design juga meningkatkan aksesibilitas, SEO, dan retensi pengguna, karena website dapat diakses dengan baik di berbagai kondisi.

**_Contoh aplikasi yang sudah menerapkan responsive design:_**
- **Instagram Web**: Tampilan otomatis menyesuaikan dengan ukuran layar. Pada desktop, menampilkan layout grid dan sidebar; pada smartphone, layout berubah menjadi satu kolom dengan navigasi yang lebih sederhana. Ini membuat pengguna dapat mengakses semua fitur dengan nyaman di perangkat manapun.

**_Contoh aplikasi yang belum menerapkan responsive design:_**
- **Website pemerintah lama atau beberapa portal universitas lama**: Banyak situs hanya dioptimalkan untuk desktop. Saat dibuka di smartphone, kontennya sering melebar, teks sulit dibaca, tombol sulit ditekan, dan harus melakukan scroll horizontal. Kurangnya responsive design membuat pengalaman pengguna buruk dan mengurangi aksesibilitas.

Intinya, tanpa responsive design, website akan sulit diakses di perangkat modern yang beragam, sementara dengan responsive design, aplikasi web menjadi fleksibel, efisien, dan lebih user-friendly.

### 🪟 Margin, Border, dan Padding dalam CSS Box Model
Margin, border, dan padding adalah konsep dasar dalam CSS Box Model, yang mengatur ruang di sekitar elemen HTML. Berikut penjelasannya:
1. **Margin**:
   Margin adalah ruang di luar border elemen. Fungsinya untuk memberi jarak antara elemen dengan elemen lain di sekitarnya.

   _Implementasi:_
   ```css
   div {margin: 20px; /* memberi jarak 20px di semua sisi */}
   ```
   Bisa juga spesifik per sisi: margin-top, margin-right, margin-bottom, margin-left.
2. **Border**:
   Border adalah garis tepi di sekitar elemen, yang memisahkan padding dan margin. Bisa berupa warna, ketebalan, dan gaya (solid, dashed, dotted, dll).

   _Implementasi:_
   ```css
   div {border: 2px solid black; /* garis tepi hitam tebal 2px */}
   ```
   Bisa juga diatur per sisi: border-top, border-right, dll.
3. **Padding**:
   Padding adalah ruang di dalam elemen, antara konten dan border. Berguna agar konten tidak menempel ke tepi elemen.

   _Implementasi:_
   ```css
   div { padding: 15px; /* memberi jarak 15px antara konten dan border */}
   ```
   Bisa juga diatur per sisi: padding-top, padding-right, dll.

### 📝 Flexbox dan Grid Layout pada CSS
Flexbox dan Grid Layout adalah dua metode modern dalam CSS untuk mengatur layout dan posisi elemen secara responsif dan efisien. Meskipun keduanya digunakan untuk mengatur tata letak, konsep dan penggunaannya berbeda:

1. **Flexbox (Flexible Box)**
   - Konsep: Flexbox dirancang untuk mengatur elemen dalam satu arah, baik baris (row) maupun kolom (column). Elemen anak bisa menyesuaikan ukuran, urutan, dan spasi secara fleksibel di dalam kontainer.
   - Kegunaan:
      - Menyusun menu navigasi horizontal atau vertikal.
      - Mengatur tombol atau card agar merata secara otomatis.
      - Mengatur elemen agar tetap seimbang ketika ukuran layar berubah.
   - Contoh implementasi:
      ```css
      .container {
      display: flex;        /* mengaktifkan flexbox */
      justify-content: space-between; /* mengatur spasi antar elemen */
      align-items: center;  /* mengatur posisi vertikal */
      }
      ```
2. **Grid Layout**
   - Konsep: Grid Layout digunakan untuk mengatur elemen dalam dua dimensi: baris dan kolom sekaligus. Memberikan kontrol lebih presisi untuk membuat layout kompleks seperti dashboard, galeri, atau halaman web multi-kolom.
   - Kegunaan:
      - Membuat layout website dengan beberapa kolom dan baris.
      - Menyusun elemen yang tidak selalu searah, seperti grid produk e-commerce.
      - Mengatur ukuran elemen secara proporsional atau otomatis.
   - Contoh implementasi:
      ```css
      .container {
      display: grid;              
      grid-template-columns: repeat(3, 1fr); /* 3 kolom dengan lebar sama */
      gap: 20px;                     /* jarak antar elemen */
      }
      ```
### 💻 Langkah Pengimplementasian Proyek Django Tugas 5 Secara Step-by-Step 

1. **Mengimport Tailwind ke Aplikasi pada `base.html`.**
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      {% block meta %} {% endblock meta %}
      <script src="https://cdn.tailwindcss.com"></script>
   </head>
   <body>
      {% block content %} {% endblock content %}
   </body>
   </html>
   ```

2. **Membuat fitur Edit Product pada `views.py`.**
   
   1. Membuat fungsi `Edit Product` pada `views.py` untuk proses mengubah detail produk
      ```python
      def edit_product(request, id):
         product = get_object_or_404(Product, pk=id)
         form = ProductForm(request.POST or None, instance=product)
         if form.is_valid() and request.method == 'POST':
            form.save()
            return redirect('main:show_main')

         context = {
            'form': form
         }

         return render(request, "edit_product.html", context)
      ```

   2. Membuat file `edit_product.html` pada direktori `main/templates` untuk tampilan form data produk yang ingin diubah/edit
      ```html
      {% extends 'base.html' %}

      {% load static %}

      {% block content %}

      <h1>Edit Product</h1>

      <form method="POST">
         {% csrf_token %}
         <table>
            {{ form.as_table }}
            <tr>
                  <td></td>
                  <td>
                     <input type="submit" value="Edit Product"/>
                  </td>
            </tr>
         </table>
      </form>

      {% endblock %}
      ```

   3. Membuat routing URL untuk fungsi `edit_product` yang ditambahkan di `views.py` pada `main/urls.py`
      1. Mengimport fungsi `edit_product` pada `main/urls.py`
         ```python
         from django.urls import path
         from main.views import edit_product
         ```

      2. Menambahkan path URL fungsi `edit_product` ke dalam `urlpatterns` 
         ```python
         app_name = 'main'

         urlpatterns = [
            path('', show_main, name='show_main'),
            path('product/<uuid:id>/edit', edit_product, name='edit_product'),
         ]
         ```
   4. Update page `main.html` pada subdirektori `main/templates`, tepatnya pada loop `product_list`, di mana menambahkan button edit
   ```html
   ...
   <a href="{% url 'main:edit_product' product.pk %}">
        <button>
            Edit
        </button>
    </a>
   ...
   ```

3. **Membuat fitur Hapus Product pada `views.py`**
   
   1. Membuat fungsi `delete_product` pada `views.py` untuk proses menghapus produk yang sudah dibuat
      ```python
      def delete_product(request, id):
         product = get_object_or_404(Product, pk=id)
         product.delete()
         return HttpResponseRedirect(reverse('main:show_main'))
      ```
   
   3. Membuat routing URL untuk fungsi `delete_product` yang ditambahkan di `views.py` pada `main/urls.py`
      1. Mengimport fungsi `delete_product` pada `main/urls.py`
         ```python
         from django.urls import path
         from main.views import delete_product
         ```

      2. Menambahkan path URL fungsi `logout_user` ke dalam `urlpatterns` 
         ```python
         app_name = 'main'

         urlpatterns = [
            path('', show_main, name='show_main'),
            path('product/<uuid:id>/delete', delete_product, name='delete_product'),
         ]
         ```
   4. Update page `main.html` pada subdirektori `main/templates`, tepatnya pada loop `product_list`, di mana menambahkan button delete
   ```html
   ...
   <a href="{% url 'main:delete_product' product.pk %}">
      <button>
          Delete
      </button>
   </a>
   ...
   ```

4. **Menambahkan Navigation Bar pada aplikasi**
   
   1. Membuat file `navbar.html` pada direktori `templates/` di roots dan mengisinya dengan file berikut
      ```html
      <nav>
      <h1>Golden Goals</h1>

      <ul>
         <li><a href="/">Home</a></li>
         <li><a href="{% url 'main:add_product' %}">Add Product</a></li>
      </ul>

      {% if user.is_authenticated %}
         <div>
            <span>Welcome, {{ username|default:user.username }}</span>
            <span>{{ npm|default:"Student" }} - {{ class|default:"Class" }}</span>
            <a href="{% url 'main:logout' %}">Logout</a>
         </div>
      {% else %}
         <div>
            <a href="{% url 'main:login' %}">Login</a>
            <a href="{% url 'main:register' %}">Register</a>
         </div>
      {% endif %}
      </nav>
      ```

   2. Mentautkan Navigation Bar pada `main.html` di subdirektori `main/templates/`
   ```html
   {% extends 'base.html' %}
   {% block content %}
   {% include 'navbar.html' %}
   ...
   {% endblock content%}
   ```

5. **Mengkonfigurasi static files pada aplikasi**
   
   1. Menambahkan midlleware whitenoise pada `settings.py` 
      ```python
            ...
      MIDDLEWARE = [
         'django.middleware.security.SecurityMiddleware',
         'whitenoise.middleware.WhiteNoiseMiddleware', #Menambahkan tepat di bawah SecurityMiddleware
         ...
      ]
      ...
      ```

   2. Menambahkan variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` pada `settings.py`
      ```python
      ...
      STATIC_URL = '/static/'
      if DEBUG:
         STATICFILES_DIRS = [
            BASE_DIR / 'static' # merujuk ke /static root project pada mode development
         ]
      else:
         STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
      ...
      ```

6. **Styling aplikasi dengan Tailwind dan External CSS**

   1. Membuat file `global.css` pada `/static/css` lalu menghubungkannya ke `base.html`
      ```html
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
      <head>
         <meta charset="UTF-8" />
         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
         {% block meta %} {% endblock meta %}
         <script src="https://cdn.tailwindcss.com"></script>
         <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
      </head>
      <body>
         {% block content %} {% endblock content %}
      </body>
      </html>
      ``` 

   2. Menambahkan custom styling ke `global.css`
   ```css
      .form-style form input, form textarea, form select {
         width: 100%;
         padding: 0.5rem;
         border: 1px solid #bcbcbc;
         border-radius: 0.375rem;
      }
      .form-style form input:focus, form textarea:focus, form select:focus {
         outline: none;
         border-color: #FFD700;
         box-shadow: 0 0 0 1px #FFD700;
      }

      .form-style input[type="checkbox"] {
         width: 1.25rem;
         height: 1.25rem;
         padding: 0;
         border: 1px solid #d1d5db;
         border-radius: 0.375rem;
         background-color: white;
         cursor: pointer;
         position: relative;
         appearance: none;
         -webkit-appearance: none;
         -moz-appearance: none;
      }

      .form-style input[type="checkbox"]:checked {
         background-color: #FFD700;
         border-color: #FFD700;
      }

      .form-style input[type="checkbox"]:checked::after {
         content: '✓';
         position: absolute;
         top: 50%;
         left: 50%;
         transform: translate(-50%, -50%);
         color: white;
         font-weight: bold;
         font-size: 0.875rem;
      }

      .form-style input[type="checkbox"]:focus {
         outline: none;
         border-color: #FFD700;
         box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1);
      }
      ```

7. **Melakukan styling pada Navigation Bar**
   ```html
      <nav class="fixed top-0 left-0 w-full bg-blue-900 border-b border-gray-200 shadow-sm z-50">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-xl font-semibold text-white">
            <span class="text-yellow-400">Golden</span> Goals ✨
          </h1>
        </div>
        
        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <a href="/" class="text-white hover:text-yellow-400 font-medium transition-colors">
            Home
          </a>
          <a href="{% url 'main:add_product' %}" class="text-white hover:text-yellow-400 font-medium transition-colors">
            Add Product
          </a>
        </div>
        
        <!-- Desktop User Section -->
        <div class="hidden md:flex items-center space-x-6">
          {% if user.is_authenticated %}
            <div class="text-right">
              <div class="text-sm font-medium text-white">{{ username|default:user.username }}</div>
              <div class="text-xs text-yellow-400">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
            </div>
            <a href="{% url 'main:logout' %}" class="text-red-500 hover:text-red-600 font-medium transition-colors">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-white hover:text-yellow-400 font-medium transition-colors">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="bg-yellow-400 hover:bg-yellow-400 text-blue-900 px-4 py-2 rounded font-medium transition-colors">
              Register
            </a>
          {% endif %}
        </div>
        
        <!-- Mobile Menu Button -->
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button p-2 text-white hover:text-yellow-400 transition-colors">
            <span class="sr-only">Open menu</span>
            <div class="w-6 h-6 flex flex-col justify-center items-center">
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm my-0.5"></span>
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
            </div>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile Menu -->
    <div class="mobile-menu hidden md:hidden bg-blue-900 border-t border-gray-200">
      <div class="px-6 py-4 space-y-4">
        <!-- Mobile Navigation Links -->
        <div class="space-y-1">
          <a href="/" class="block text-white hover:text-yellow-400 font-medium py-3 transition-colors">
            Home
          </a>
          <a href="{% url 'main:add_product' %}" class="block text-white hover:text-yellow-400 font-medium py-3 transition-colors">
            Add Product
          </a>
        </div>
        
        <!-- Mobile User Section -->
        <div class="border-t border-gray-200 pt-4">
          {% if user.is_authenticated %}
            <div class="mb-4">
              <div class="font-medium text-white">{{ username|default:user.username }}</div>
              <div class="text-sm text-yellow-400">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
            </div>
            <a href="{% url 'main:logout' %}" class="block text-red-500 hover:text-red-600 font-medium py-3 transition-colors">
              Logout
            </a>
          {% else %}
            <div class="space-y-3">
              <a href="{% url 'main:login' %}" class="block text-white hover:text-yellow-400 font-medium py-3 transition-colors">
                Login
              </a>
              <a href="{% url 'main:register' %}" class="block bg-yellow-400 hover:bg-yellow-400 text-blue-900 font-medium py-3 px-4 rounded text-center transition-colors">
                Register
              </a>
            </div>
          {% endif %}
        </div>
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
   ```

8. **Melakukan styling Halaman Login user**
   ```html
   {% extends 'base.html' %}

   {% block meta %}
   <title>Login - Golden Goals ✨</title>
   {% endblock meta %}

   {% block content %}
   <div class="bg-gray-50 w-full min-h-screen flex items-center justify-center p-8">
   <div class="max-w-md w-full">
      <div class="bg-blue-900 rounded-lg border border-gray-200 p-6 sm:p-8 form-style text-white">
         <div class="text-center mb-8">
         <h1 class="text-2xl text-yellow-400 font-bold mb-2">Sign In</h1>
         <p>Welcome back to Golden Goals ✨</p>
         </div>

         <!-- Form Errors Display -->
         {% if form.non_field_errors %}
         <div class="mb-6">
            {% for error in form.non_field_errors %}
               <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700">
               {{ error }}
               </div>
            {% endfor %}
         </div>
         {% endif %}

         {% if form.errors %}
         <div class="mb-6">
            {% for field, errors in form.errors.items %}
               {% if field != '__all__' %}
               {% for error in errors %}
                  <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                     <strong>{{ field|title }}:</strong> {{ error }}
                  </div>
               {% endfor %}
               {% endif %}
            {% endfor %}
         </div>
         {% endif %}

         <form method="POST" action="" class="space-y-6">
         {% csrf_token %}
         
         <div>
            <label for="username" class="block text-sm font-medium mb-2">Username</label>
            <input 
               id="username" 
               name="username" 
               type="text" 
               required 
               class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-yellow-400 transition-colors bg-white text-black" 
               placeholder="Enter your username">
         </div>

         <div>
            <label for="password" class="block text-sm font-medium mb-2">Password</label>
            <input 
               id="password" 
               name="password" 
               type="password" 
               required 
               class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-yellow-400 transition-colors bg-white text-black" 
               placeholder="Enter your password">
         </div>

         <button 
            type="submit" 
            class="w-full bg-yellow-400 text-blue-900 font-medium py-3 px-4 rounded-md hover:bg-yellow-300 transition-colors">
            Sign In
         </button>
         </form>

         <!-- Messages Display -->
         {% if messages %}
         <div class="mt-6">
            {% for message in messages %}
               <div 
               class="
                  px-4 py-3 rounded-md text-sm border
                  {% if message.tags == 'success' %}
                     bg-green-50 border-green-200 text-green-700
                  {% elif message.tags == 'error' %}
                     bg-red-50 border-red-200 text-red-700
                  {% else %}
                     bg-gray-50 border-gray-200 text-gray-700
                  {% endif %}
               ">
               {{ message }}
               </div>
            {% endfor %}
         </div>
         {% endif %}

         <div class="mt-6 text-center pt-6 border-t border-gray-700">
         <p class="text-sm">
            Don't have an account? 
            <a href="{% url 'main:register' %}" class="text-yellow-400 hover:text-yellow-300 font-medium">
               Register Now
            </a>
         </p>
         </div>
      </div>
   </div>
   </div>
   {% endblock content %}
   ```

9. **Melakukan styling halaman Register user**
   ```html
   {% extends 'base.html' %}

   {% block meta %}
   <title>Register - Golden Goals ✨</title>
   {% endblock meta %}

   {% block content %}
   <div class="form-style">
   <div class="min-h-screen bg-gray-50 flex items-center justify-center p-8">
      <div class="max-w-md w-full relative z-10">
         <div class="bg-blue-900 border border-gray-200 rounded-lg p-8 shadow-sm text-white">
         <div class="text-center mb-8">
            <h2 class="text-2xl text-yellow-400 font-bold mb-2">Join Us</h2>
            <p>Create your Golden Goals ✨ account</p>
         </div>

         <!-- Form Errors Display -->
         {% if form.non_field_errors %}
            <div class="mb-6">
               {% for error in form.non_field_errors %}
               <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700">
                  {{ error }}
               </div>
               {% endfor %}
            </div>
         {% endif %}

         {% if form.errors %}
            <div class="mb-6">
               {% for field, errors in form.errors.items %}
               {% if field != '__all__' %}
                  {% for error in errors %}
                     <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                     <strong>{{ field|title }}:</strong> {{ error }}
                     </div>
                  {% endfor %}
               {% endif %}
               {% endfor %}
            </div>
         {% endif %}

         <form method="POST" action="" class="space-y-5">
            {% csrf_token %}
            
            <div>
               <label for="username" class="block text-sm font-medium mb-2">Username</label>
               <input 
               id="username" 
               name="username" 
               type="text" 
               required 
               class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-yellow-400 transition duration-200 bg-white text-black" 
               placeholder="Choose a username">
            </div>

            <div>
               <label for="password1" class="block text-sm font-medium mb-2">Password</label>
               <input 
               id="password1" 
               name="password1" 
               type="password" 
               required 
               class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-yellow-400 transition duration-200 bg-white text-black" 
               placeholder="Create a password">
            </div>

            <div>
               <label for="password2" class="block text-sm font-medium mb-2">Confirm Password</label>
               <input 
               id="password2" 
               name="password2" 
               type="password" 
               required 
               class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-yellow-400 transition duration-200 bg-white text-black" 
               placeholder="Confirm your password">
            </div>

            <button 
               type="submit" 
               class="w-full bg-yellow-400 text-blue-900 font-medium py-3 px-4 rounded hover:bg-yellow-300 focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:ring-offset-2 transition duration-200">
               Create Account
            </button>
         </form>

         <!-- Messages Display -->
         {% if messages %}
            <div class="mt-6">
               {% for message in messages %}
               <div 
                  class="
                     px-4 py-3 rounded text-sm border
                     {% if message.tags == 'success' %}
                     bg-green-50 border-green-200 text-green-700
                     {% elif message.tags == 'error' %}
                     bg-red-50 border-red-200 text-red-700
                     {% else %}
                     bg-gray-50 border-gray-200 text-gray-700
                     {% endif %}
                  ">
                  {{ message }}
               </div>
               {% endfor %}
            </div>
         {% endif %}

         <div class="mt-6 text-center">
            <p class="text-sm">
               Already have an account? 
               <a href="{% url 'main:login' %}" class="text-yellow-400 hover:text-yellow-300 font-medium">
               Sign In
               </a>
            </p>
         </div>
         </div>
      </div>
   </div>
   </div>
   {% endblock content %}
   ```

10. **Melakukan styling Halaman Home**
   1. Membuat file `card_product.html` di direktori `main/templates`
   ```html
   {% load static %}
   <article class="bg-blue-900 rounded-lg border border-white hover:shadow-lg transition-shadow duration-300 overflow-hidden text-white">
   <!-- Thumbnail -->
   <div class="aspect-[3/4] relative overflow-hidden">
      {% if product.thumbnail %}
         <img src="{{ product.thumbnail }}" alt="{{ product.product_name }}" class="w-full h-full object-cover">
      {% else %}
         <div class="w-full h-full bg-blue-800"></div>
      {% endif %}

      <!-- Category Badge -->
      <div class="absolute top-3 left-3">
         <span class="inline-flex items-center px-2.5 py-0.5 rounded-md text-xs font-medium bg-white text-blue-900 font-bold">
         {{ product.get_category_display }}
         </span>
      </div>

      <!-- Status Badges -->
      <div class="absolute top-3 right-3 flex space-x-2">
         {% if product.is_featured %}
         <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-yellow-400 text-blue-900 font-semibold">
            Featured
         </span>
         {% endif %}
         {% if product.is_product_hot %}
         <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-red-500 text-white font-semibold">
            Hot
         </span>
         {% endif %}
      </div>
   </div>

   <!-- Content -->
   <div class="p-5">
      <div class="flex items-center text-sm text-gray-300 mb-3">
         <time datetime="{{ product.created_at|date:'c' }}">
         {{ product.created_at|date:"M j, Y" }}
         </time>
         <span class="mx-2">•</span>
         <span>{{ product.product_views }} views</span>
      </div>

      <h3 class="text-lg font-semibold text-white mb-3 line-clamp-2 leading-tight">
         <a href="{% url 'main:show_detail_product' product.id %}" class="hover:text-yellow-400 transition-colors">
         {{ product.product_name }}
         </a>
      </h3>

      <h2 class="text-xl font-bold text-yellow-400 mb-2">
         Rp {{ product.price|floatformat:0 }} </h2>

      <p class="text-gray-200 text-sm leading-relaxed line-clamp-3 mb-4">
         {{ product.description|truncatewords:20 }}
      </p>

      <!-- Action Buttons -->
      {% if user.is_authenticated and product.user == user %}
         <div class="flex items-center justify-between pt-4 border-t border-white">
         <a href="{% url 'main:show_detail_product' product.id %}" class="text-yellow-400 hover:text-yellow-300 font-medium text-sm transition-colors">
            Read more →
         </a>
         <div class="flex space-x-2">
         <form action="{% url 'main:edit_product' product.id %}" method="get">
               <button type="submit" 
                     class="bg-gray-400 text-white text-sm px-3 py-1 rounded hover:bg-gray-300 transition-colors">
               Edit
               </button>
         </form>
         
         <form action="{% url 'main:delete_product' product.id %}" method="post">
               {% csrf_token %}
               <button type="submit" 
                     class="bg-red-500 text-white text-sm px-3 py-1 rounded hover:bg-red-400 transition-colors">
               Delete
               </button>
         </form>
         </div>
         </div>
      {% else %}
         <div class="pt-4 border-t border-white">
         <a href="{% url 'main:show_detail_product' product.id %}" class="text-yellow-400 hover:text-yellow-300 font-medium text-sm transition-colors">
            Read more →
         </a>
         </div>
      {% endif %}
   </div>
   </article>
   ```

   2. Menambahkan file `no-product-found.png` pada direktori `static/image` sebagai tampilan jika produk belum ada 

   3. Mengupdate `main.html` dengan menambahkan page `card_product.html` dan file `no-product-found.png`
   ```html
   {% extends 'base.html' %}
   {% load static %}

   {% block meta %}
   <title>Golden Goals ✨</title>
   {% endblock meta %}

   {% block content %}
   {% include 'navbar.html' %}
   <div class="bg-gray-50 w-full pt-16 min-h-screen">
   <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

      <!-- Header Section -->
      <div class="mb-8 text-center">
         <h1 class="text-3xl font-bold text-blue-900 mb-2">Latest Football Products</h1>
         <p class="text-gray-600">Stay updated with the latest football products and magic</p>
      </div>

      <!-- Filter Section -->
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8 bg-blue-900 rounded-lg border border-white p-4 text-white">
         <div class="flex space-x-3 mb-4 sm:mb-0 flex items-center justify-center">
         <a href="?" class="{% if request.GET.filter == 'all' or not request.GET.filter  %} bg-yellow-400 text-blue-900{% else %}bg-white text-blue-900 border border-white{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-yellow-300 flex items-center">
            All Products
         </a>
         <a href="?filter=my" class="{% if request.GET.filter == 'my' %} bg-yellow-400 text-blue-900{% else %}bg-white text-blue-900 border border-white{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-yellow-300 flex items-center justify-center">
            My Products
         </a>
         </div>
         {% if user.is_authenticated %}
         <div class="text-sm text-gray-100">
            Last login: {{ last_login }}
         </div>
         {% endif %}
      </div>

      <!-- News Grid -->
      {% if not products_list %}
         <div class="bg-blue-900 rounded-lg border border-white p-12 text-center text-white">
         <div class="w-32 h-32 mx-auto mb-4">
            <img src="{% static 'image/no-product-found.png' %}" alt="No news available" class="w-full h-full object-contain">
         </div>
         <h3 class="text-lg font-medium mb-2">No product found</h3>
         <p class="text-gray-200 mb-6">Be the first to share football product with the community.</p>
         <a href="{% url 'main:add_product' %}" class="inline-flex items-center px-4 py-2 bg-yellow-400 text-blue-900 rounded-md hover:bg-yellow-300 transition-colors font-semibold">
            Add Product
         </a>
         </div>
      {% else %}
         <!-- 1 row bisa 4 card -->
         <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
         {% for product in products_list %}
            {% include 'card_product.html' with product=product %}
         {% endfor %}
         </div>
      {% endif %}
   </div>
   </div>
   {% endblock content %}
   ```

11. **Styling halaman Detail Product**
   ```html
   {% extends 'base.html' %}
   {% load static %}

   {% block meta %}
   <title>{{ product.product_name }} - Golden Goals</title>
   {% endblock meta %}

   {% block content %}
   <div class="bg-gray-50 w-full min-h-screen">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
         
         <!-- Back Navigation -->
         <div class="mb-6">
               <a href="{% url 'main:show_main' %}" class="text-blue-900 hover:text-blue-700 font-medium transition-colors">
                  ← Back to Products
               </a>
         </div>
         
         <!-- Article -->
         <article class="bg-blue-900 rounded-lg border border-gray-200 overflow-hidden">
               
               <!-- Konten Utama -->
               <div class="p-6 sm:p-8 flex flex-col md:flex-row gap-8">
                  
                  <!-- Thumbnail -->
                  {% if product.thumbnail %}
                  <div class="md:w-1/3 w-full">
                     <img src="{{ product.thumbnail }}" 
                           alt="{{ product.product_name }}" 
                           class="w-full h-auto object-cover rounded-lg border border-gray-200">
                  </div>
                  {% endif %}
                  
                  <!-- Product Info -->
                  <div class="flex-1">
                     
                     <!-- Kategori + Status -->
                     <div class="flex flex-wrap items-center gap-2 mb-4">
                           <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-white text-blue-900">
                              {{ product.get_category_display }}
                           </span>
                           {% if product.is_featured %}
                              <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-yellow-400 text-blue-900">
                                 Featured
                              </span>
                           {% endif %}
                           {% if product.is_product_hot %}
                              <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-red-200 text-red-700">
                                 Hot
                              </span>
                           {% endif %}
                     </div>

                     <!-- Nama Produk -->
                     <h1 class="text-3xl sm:text-4xl font-bold text-white leading-tight mb-4">
                           {{ product.product_name }}
                     </h1>

                     <!-- Harga dan Stok -->
                     <div class="mb-4">
                           <p class="text-2xl font-bold text-yellow-400">Rp {{ product.price|floatformat:0 }}</p>
                           <p class="text-md text-white">Stock: {{ product.stock }}</p>
                     </div>

                     <!-- Tanggal & Views -->
                     <div class="flex flex-wrap items-center text-sm text-gray-100 gap-4 mb-6">
                           <time datetime="{{ product.created_at|date:'c' }}">
                              {{ product.created_at|date:"M j, Y g:i A" }}
                           </time>
                           <span>{{ product.product_views }} views</span>
                     </div>

                     <!-- Deskripsi -->
                     <div class="prose prose-lg max-w-none">
                           <div class="text-white leading-relaxed whitespace-pre-line text-base sm:text-lg">
                              {{ product.description }}
                           </div>
                     </div>

                  </div>
               </div>

               <!-- Author Info -->
               <div class="border-t border-gray-200 p-6 sm:p-8 bg-yellow-400">
                  <div class="flex items-center justify-between">
                     <div>
                           <div class="font-medium text-blue-900">
                              {% if product.user %}
                                 <p>Creator: {{ product.user.username }}</p>
                              {% else %}
                                 <p>Creator: Anonymous</p>
                              {% endif %}
                           </div>
                           <p class="text-sm text-gray-500">Creator</p>
                     </div>
                  </div>
               </div>
         </article>
      </div>
   </div>
   {% endblock content %}
   ```
12. **Styling halaman Add Product**
   ```html
   {% extends 'base.html' %}
   {% block meta %}
   <title>Add Product - Golden Goals</title>
   {% endblock meta %}

   {% block content %}
   <div class="bg-gray-50 w-full min-h-screen">
   <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      
      <!-- Back Navigation -->
      <div class="mb-6">
         <a href="{% url 'main:show_main' %}" class="text-blue-900 hover:text-blue-700 font-medium transition-colors">
         ← Back to Products
         </a>
      </div>
      
      <!-- Form -->
      <div class="bg-blue-900 rounded-lg border border-gray-200 p-6 sm:p-8 form-style text-black">
         <div class="mb-8">
         <h1 class="text-2xl text-yellow-400 font-bold mb-2">Add New Product</h1>
         <p class="text-white">Share your football product and accessories with the community</p>
         </div>
         
         <form method="POST" class="space-y-6">
         {% csrf_token %}
         {% for field in form %}
         <div>
            <label for="{{ field.id_for_label }}" class="block text-white font-medium mb-2">
               {{ field.label }}
               </label>
               <div class="w-full">
               {{ field }}
               </div>
               {% if field.help_text %}
               <p class="mt-1 text-sm text-gray-200">{{ field.help_text }}</p>
               {% endif %}
               {% for error in field.errors %}
               <p class="mt-1 text-sm text-red-400">{{ error }}</p>
               {% endfor %}
            </div>
         {% endfor %}
         
         <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-700">
            <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-gray-300 text-white rounded-md font-medium hover:bg-blue-800 transition-colors text-center">
               Cancel
            </a>
            <button type="submit" class="order-1 sm:order-2 flex-1 bg-yellow-400 text-blue-900 px-6 py-3 rounded-md font-medium hover:bg-yellow-300 transition-colors">
               Publish Product
            </button>
         </div>
         </form>
      </div>
   </div>
   </div>
   {% endblock %}
   ```

13. **Styling halaman Edit Product**
   ```html
   {% extends 'base.html' %}
   {% load static %}

   {% block meta %}
   <title>Edit Product - Golden Goals</title>
   {% endblock meta %}

   {% block content %}
   <div class="bg-gray-50 w-full min-h-screen">
   <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      
      <!-- Back Navigation -->
      <div class="mb-6">
         <a href="{% url 'main:show_main' %}" class="text-blue-900 hover:text-yellow-400 font-medium transition-colors">
         ← Back to Products
         </a>
      </div>
      
      <!-- Form -->
      <div class="bg-blue-900 rounded-lg border border-white p-6 sm:p-8 form-style text-black">
         <div class="mb-8">
         <h1 class="text-2xl font-bold text-white mb-2">Edit Product</h1>
         <p class="text-white">Update your football product details</p>
         </div>
         
         <form method="POST" class="space-y-6">
         {% csrf_token %}
         {% for field in form %}
               <label for="{{ field.id_for_label }}" class="block text-white font-medium text-yellow-400 mb-2">
               {{ field.label }}
               </label>
               <div class="w-full">
               {{ field }}
               </div>
               {% if field.help_text %}
               <p class="mt-1 text-sm text-gray-300">{{ field.help_text }}</p>
               {% endif %}
               {% for error in field.errors %}
               <p class="mt-1 text-sm text-red-400">{{ error }}</p>
               {% endfor %}
         {% endfor %}
         
         <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-white">
            <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-white text-white rounded-md font-medium hover:bg-white hover:text-blue-900 transition-colors text-center">
               Cancel
            </a>
            <button type="submit" class="order-1 sm:order-2 flex-1 bg-yellow-400 text-blue-900 px-6 py-3 rounded-md font-semibold hover:bg-yellow-300 transition-colors">
               Update Product
            </button>
         </div>
         </form>
      </div>
   </div>
   </div>
   {% endblock %}
   ```
14. **Mengupdate isi file `README.md` yang berisi jawaban dari beberapa pertanyaan Tugas 5.**
   - Buat file `README.md` yang berisi deskripsi proyek, menyantumkan history tugas sebelumnya, serta jawaban dari pertanyaan tentang CSS selector untuk elemen HTML, pentingnya responsive design, perbedaan margin, border, dan padding. Serta konsep flex box dan grid layout beserta kegunaannya. Selain itu, menjelaskan step-by-step proses pengerjaan Tugas 5. 