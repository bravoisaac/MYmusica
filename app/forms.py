from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Contacto

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

class RegisterForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo electrónico ya está registrado')
        return email

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "email", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
