from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406402416',
        'name': 'Muhammad Helmi Alfarissi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
