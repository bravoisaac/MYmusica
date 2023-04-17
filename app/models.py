from django.db import models

# Create your models here.

opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre

