from django.shortcuts import render
from .forms import LoginForm
from .models import Contacto
from django.contrib.auth.models import User
from .forms import RegisterForm
from .forms import ContactoForm

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def galeria(request):
    return render(request, 'app/galeria.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje guardado"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)

def login(request):
    form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.create_user(email=email)
            user.save()
            # Aquí puedes hacer cualquier otra acción necesaria para la creación de la cuenta
            return ('home') # Redirige al usuario a la página principal después de crear la cuenta
    else:
        form = RegisterForm()
    return render(request, 'app/registro.html', {'form': form})

