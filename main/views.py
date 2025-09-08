from django.shortcuts import render

def show_main(request):
    context = {
        'application' : 'Golden Goals',
        'tagline' : 'Where Football Dreams Become Yours',
        'address' : 'Platform 9 ¾, Diagon Alley Football District',
        'instagram' : 'Instagram: @golden.goals',
        'npm' : '2406402416',
        'name': 'Muhammad Helmi Alfarissi',
        'class':'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
