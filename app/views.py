from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def galeria(request):
    return render(request, 'app/galeria.html')

def contacto(request):
    return render(request, 'app/contacto.html')