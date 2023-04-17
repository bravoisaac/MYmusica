from django.urls import path
from .views import home ,contacto,galeria, login, registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]
