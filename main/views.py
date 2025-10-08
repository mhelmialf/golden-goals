import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)
    
    context = {
        'application': 'Golden Goals',
        'tagline': 'Where Football Dreams Become Yours',
        'address': 'Platform 9 ¾, Diagon Alley Football District',
        'instagram': 'Instagram: @golden.goals',
        'npm': '2406402416',
        'name': 'Muhammad Helmi Alfarissi',
        'class': 'PBP D',
        'products_list': products_list,
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)


@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)


@login_required(login_url='/login')
def show_detail_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)


def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'product_name': product.product_name,
            'price': product.price,
            'stock': product.stock,
            'product_views': product.product_views,
            'category': product.category,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in products_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'product_name': product.product_name,
            'price': product.price,
            'stock': product.stock,
            'product_views': product.product_views,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


@csrf_exempt
def register(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Account created successfully."})
        else:
            errors = {k: v for k, v in form.errors.items()}
            return JsonResponse({"status": "error", "errors": errors}, status=400)
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {"form": form})


@csrf_exempt
def login_user(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({"status": "success", "redirect_url": reverse("main:show_main")})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({"status": "error", "message": "Invalid username or password."}, status=400)
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    response = redirect('main:show_main')
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    if not all([product_name, description, category, price, stock]):
        return JsonResponse({"status": "error", "message": "Semua field wajib diisi."}, status=400)

    try:
        valid_price = int(price)
        valid_stock = int(stock)
    except (ValueError, TypeError):
        return JsonResponse({"status": "error", "message": "Harga dan Stok harus berupa angka."}, status=400)

    new_product = Product(
        product_name=product_name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        price=valid_price,
        stock=valid_stock,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return JsonResponse({"status": "success", "message": "Produk berhasil ditambahkan!"}, status=201)


@login_required
@require_POST
def edit_product_ajax(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    form = ProductForm(request.POST, instance=product)

    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success', 'message': 'Product updated successfully.'})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)


@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == "DELETE":
        try:
            product = Product.objects.get(pk=id)
            if request.user != product.user:
                return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)
            product.delete()
            return JsonResponse({"status": "success"})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=400)
