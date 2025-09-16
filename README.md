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

### 🗃️ Pentingnya Data Delivery dalam Pengimplementasian Sebuah Platform

Data delivery diperlukan dalam sebuah platform karena memastikan informasi dapat berpindah dengan cepat, aman, dan konsisten antar komponen seperti database, server, antarmuka pengguna, maupun sistem eksternal. Tanpa mekanisme ini, data bisa terlambat, usang, atau tidak sinkron sehingga mengganggu kinerja sistem, merusak pengalaman pengguna, dan menimbulkan risiko keamanan. Dengan data delivery yang andal, platform dapat berfungsi optimal, mendukung integrasi layanan, serta memberikan akses informasi real-time yang meningkatkan kepercayaan dan kepuasan pengguna.

### 🗒️ Perbandingan XML dan JSON serta Faktor Popularitas JSON

Menurut pandangan saya pribadi, JSON terasa lebih nyaman sekaligus relevan untuk digunakan saat ini dibandingkan XML, dengan beberapa alasan utama sebagai berikut:
   - Struktur yang sederhana dan ringkas: Sintaks JSON lebih mudah dibaca serta ditulis oleh manusia maupun mesin, berbeda dengan XML yang cenderung verbose karena penggunaan tag pembuka dan penutup.
   - Efisiensi ukuran data: JSON menghasilkan file berukuran lebih kecil, sehingga mampu menghemat bandwidth sekaligus mempercepat proses transmisi data.
   - Kinerja pemrosesan yang lebih baik: Proses parsing JSON lebih cepat dan ringan, sehingga mendukung performa aplikasi yang menuntut pertukaran data secara intensif, seperti API maupun layanan real-time.
   - Integrasi yang natural dengan JavaScript: JSON dapat diproses secara native tanpa memerlukan library tambahan, sehingga memperkuat kemudahan implementasi pada pengembangan aplikasi web.
Meskipun XML tetap memiliki keunggulan dalam hal validasi skema dan dukungan namespace, secara keseluruhan JSON lebih banyak dipilih karena menawarkan efisiensi, kecepatan, serta kemudahan integrasi yang sejalan dengan kebutuhan teknologi informasi masa kini.

### ✅ Fungsi dan Pentingnya Method `is_valid()` pada Form Django

`is_valid()` adalah method pada form Django yang digunakan untuk memvalidasi data yang dikirimkan pengguna. Method ini memeriksa apakah data yang masuk melalui `request.POST` sudah sesuai dengan aturan yang ditentukan dalam `ProductForm`, seperti jenis data, panjang karakter, maupun kelengkapan field yang wajib diisi. Jika seluruh data sesuai, method ini akan mengembalikan nilai `True` sehingga data dapat diproses lebih lanjut, misalnya disimpan ke database. Namun, jika terdapat data yang tidak valid, method ini akan mengembalikan `False` sekaligus menampilkan pesan error yang relevan. Dengan demikian, `is_valid()` berperan sebagai filter utama yang menjaga keamanan aplikasi serta memastikan integritas data dengan hanya memperbolehkan penyimpanan data yang valid.

### 🔐 Peran dan Pentingnya CSRF Token dalam Keamanan Form Django

`csrf_token` adalah komponen keamanan penting dalam Django yang berfungsi melindungi form dari serangan CSRF (_Cross-Site Request Forgery_). Token ini merupakan nilai unik yang disisipkan pada setiap form untuk memastikan bahwa request yang dikirim ke server benar-benar berasal dari aplikasi kita, bukan dari sumber eksternal yang berbahaya.

Tanpa `csrf_token`, server tidak mampu membedakan apakah sebuah request benar-benar dibuat oleh pengguna melalui situs kita atau dipicu oleh situs lain. Hal ini membuka peluang bagi penyerang untuk mengeksploitasi session pengguna yang masih aktif.

Alur serangan CSRF biasanya berlangsung seperti berikut:
   1. Pengguna login ke situs kita (misalnya `GoldenGoals.com`), sehingga browser menyimpan session cookie sebagai bukti autentikasi.
   2. Penyerang membuat situs berbahaya (misalnya `malicious-web.com`) dengan form tersembunyi yang mengirimkan request ke endpoint sah milik `GoldenGoals.com` (contohnya `/add-to-cart/`).
   3. Pengguna yang masih login mengunjungi `malicious-web.com`.
   4. Browser pengguna secara otomatis mengeksekusi form tersembunyi tersebut tanpa sepengetahuan mereka.
   5. Karena tidak ada validasi `csrf_token`, server akan menganggap request tersebut sah dan mengeksekusinya, sehingga penyerang dapat memanipulasi data atau melakukan aksi tertentu atas nama pengguna.

Dengan demikian, `csrf_token` berperan sebagai lapisan pertahanan yang mencegah penyerang memanfaatkan kredensial pengguna untuk menjalankan aksi berbahaya di aplikasi kita.

### 💻 Langkah Pengimplementasian Proyek Django Secara Step-by-Step 

1. **Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**
   Step-by-Step:
   1. Mengimport `HttpResponse` dan `Serializer` pada `views.py`
      ```python
      from django.http import HttpResponse
      from django.core import serializers
      ```

   2. Menambahkan 4 fungsi baru pada `views.py` untuk format JSON dan XML
      - Fungsi untuk melihat objek dalam format JSON
         ```python
         def show_json(request):
            products_list = Product.objects.all()
            json_data = serializers.serialize("json", products_list)
            return HttpResponse(json_data, content_type="application/json")
         ```

      - Fungsi untuk melihat objek dalam format XML
         ```python
         def show_xml(request):
            data = Product.objects.all()
            xml_data = serializers.serialize("xml", data)
            return HttpResponse(xml_data, content_type="application/xml")
         ```

      - Fungsi untuk melihat objek dalam format JSON by ID
      ```python
         def show_json_by_id(request, product_id):
            try:
               product_item = Product.objects.get(pk=product_id)
               json_data = serializers.serialize("json", [product_item])
               return HttpResponse(json_data, content_type="application/json")
            except Product.DoesNotExist:
               return HttpResponse(status=404)
      ```

      - Fungsi untuk melihat objek dalam format XML by ID
      ```python
         def show_xml_by_id(request, product_id):
            try:
               product_item = Product.objects.filter(pk=product_id)
               xml_data = serializers.serialize("xml", product_item)
               return HttpResponse(xml_data, content_type="application/xml")
            except Product.DoesNotExist:
               return HttpResponse(status=404)
      ```

2. **Membuat routing URL untuk masing-masing fungsi yang telah ditambahkan di `views.py`**
   Step-by-Step:
   1. Mengimport fungsi yang telah ditambahkan di `views.py` pada `main/urls.py`
      ```python
      from django.urls import path
      from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id
      ```

   2. Menambahkan path URLs ke dalam `urlpatterns` untuk masing-masing fungsi dalam format JSON dan XML
      ```python
      urlpatterns = [
      path('', show_main, name='show_main'),
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
      ]
      ```

3. **Membuat halaman daftar objek model dengan tombol "Add" untuk menuju form dan tombol "Detail" untuk melihat rincian objek.**
   Step-by-Step:
   1. Membuat file dan direktori baru `templates/base.html` dan mengisi file tersebut dengan kerangka umum halaman web
      '''html
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
      <head>
         <meta charset="UTF-8" />
         <meta name="viewport" content="width=device-width, initial-scale=1.0" />
         {% block meta %} {% endblock meta %}
      </head>

      <body>
         {% block content %} {% endblock content %}
      </body>
      </html>
      '''

   2. Memasukkan file `base.html` ke dalam `settings.py` pada variable `TEMPLATE`
      ```python
      TEMPLATES = [
         {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                  'context_processors': [
                     'django.template.context_processors.request',
                     'django.contrib.auth.context_processors.auth',
                     'django.contrib.messages.context_processors.messages',
                  ],
            },
         },
      ]
      ```
   
   3. Mengubah file `main.html` dengan mengimplementasikan `base.html` dan menambahkan button "Add" dan "Details" pada setiap product
   ```html
   {% extends 'base.html' %}
   {% block content %}
   <h1>✨ {{ application }} ✨</h1>
   <h2><i>{{ tagline }}</i></h2>

   <h2>⚽ Our Products</h2>
   <a href="{% url 'main:add_product' %}">
      <button>+ Add New Product</button>
   </a>

   <hr>

   {% if not products_list %}
   <p>No products have been conjured yet. A little magic may bring them forth soon.</p>
   {% else %}

   {% for product in products_list %}
   <div>
   <h2><a href="{% url 'main:show_detail_product' product.id %}">{{ product.product_name }}</a></h2>

   <p>
      <b>📌 {{ product.get_category_display }}</b> |
      <b>💲 Rp{{ product.price }}</b>
      {% if product.is_featured %} 
            | <b>✨ Featured Product</b>
      {% endif %}
      {% if product.is_product_hot %}  
            | <b>🔥 Hot Product</b>
      {% endif %} 
      </p>

   {% if product.thumbnail %}
      <img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">
      <br />
   {% endif %}

   <p>{{ product.description|truncatewords:20 }}...</p>

   <p><a href="{% url 'main:show_detail_product' product.id %}"><button>Details</button></a></p>
   </div>

   <hr>
   {% endfor %}

   {% endif %}

   <br>
   <h3>📍 Visit us Here</h3>
   <p>{{ address }}</p>
   <h3>📱 Find us Here</h3>
   <p>{{ instagram }}</p>
   <br>
   <h4>Credit to:</h4>
   <p>NPM: {{ npm }}</p>
   <p>Name: {{ name }}</p>
   <p>Class: {{ class }}</p>

   {% endblock content %}
   ```

4. **Membuat page form yg di redirect dari tombol "Add" untuk menampilkan form penambahan produk**
   Step-by-Step:
   1. Membuat file `forms.py` untuk model `Product` menggunakan `ModelForm`
      ```python
      from django.forms import ModelForm
      from main.models import Product

      class ProductForm(ModelForm):
         class Meta:
            model = Product
            fields = ["product_name", "price", "stock", "description", "category", "thumbnail", "is_featured"]
      ```

   2. Membuat fungsi baru di `views.py` untuk tampilan input form
      ```python
      def add_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         form.save()
         return redirect('main:show_main')

      context = {'form': form}
      return render(request, "add_product.html", context)
      ```

   3. Membuat file `add_product.html` sebagai page untuk mengakses form
      ```html
      {% extends 'base.html' %} 
      {% block content %}
      <h1>Add Product</h1>

      <form method="POST">
      {% csrf_token %}
      <table>
         {{ form.as_table }}
         <tr>
            <td></td>
            <td>
            <input type="submit" value="Add Product" />
            </td>
         </tr>
      </table>
      </form>

      {% endblock %}
      ```

   4. Mengimport fungsi dan menambahkan path di `urls.py` untuk routing URL form 
      ```python
      from django.urls import path
      from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id

      app_name = 'main'

      urlpatterns = [
         path('', show_main, name='show_main'),
         path('add-product/', add_product, name='add_product'),
         ...
      ]
      ```

5. **Membuat page product detail yang diredirect dari button "Details" untuk menampilkan detail tiap produk.**
   Step-by-Step:
   1. Membuat fungsi baru di `views.py` untuk menampilkan detail informasi produk
      ```python
      def show_detail_product(request, id):
      product = get_object_or_404(Product, pk=id)
      product.increment_views()

      context = {
         'product': product
      }

      return render(request, "product_detail.html", context)
      ```

   2. Membuat file `product_detail.html` sebagai page untuk melihat informasi detail tiap produk
      ```html
      {% extends 'base.html' %}
      {% block content %}
      <p><a href="{% url 'main:show_main' %}"><button>← Back</button></a></p>

      <h1>{{ product.product_name }}</h1>

      {% if product.thumbnail %}
         <img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">
         <br /><br />
      {% endif %} 

      <p><b>💲 Price: </b> Rp{{ product.price }}</p>
      <p><b>⚽ Category: </b>{{ product.get_category_display }}</p>
      <p><b>📝 Decription: </b>{{ product.description}}</p>
         
      {% if product.is_featured %} 
         <b>✨ Featured Product</b>
      {% endif %}
         
      {% if product.is_product_hot %} 
         <b>🔥 Hot Product</b>
      {% endif %}

      {% endblock content %}
      ```

   3. Mengimport fungsi dan menambahkan path di `urls.py` untuk routing URL form 
      ```python
      from django.urls import path
      from main.views import show_main, add_product, show_detail_product, show_xml, show_json, show_xml_by_id, show_json_by_id

      app_name = 'main'

      urlpatterns = [
         path('', show_main, name='show_main'),
         path('product/<str:id>/', show_detail_product, name='show_detail_product'),
         ...
      ]
      ```
   
6. **Mengupdate isi file `README.md` yang berisi jawaban dari beberapa pertanyaan Tugas 3.**
   - Buat file `README.md` yang berisi deskripsi proyek, menyantumkan hisory tugas sebelumnya, serta jawaban dari pertanyaan tentang data delivery, XMl, JSON, dan pentingnya CSRF serta method `is_valid()` pada form Django.

### 📝 Feedback Asisten Dosen Tutorial 2

Asisten dosen pada tutorial 2 memberikan pendampingan yang sangat optimal. Materi dan dokumen tutorial yang disusun bersifat komprehensif serta mudah dipahami, sehingga mahasiswa yang belum memiliki pengalaman dasar dalam web development tetap dapat mengikuti setiap langkah dengan baik. Selain itu, meskipun pelaksanaan tutorial dilakukan secara daring, asisten dosen tetap fast response untuk membantu ketika peserta mengalami kesulitan dalam pengerjaan.

### 📮 Hasil API Call berupa JSON dan XML melalui Postman

**1. Hasil JSON (All)**
      
**2. Hasil XML (All)**

**3. Hasil JSON (By ID)**

**4. Hasil XML (By ID)**