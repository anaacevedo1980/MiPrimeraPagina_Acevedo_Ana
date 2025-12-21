from django.db import models
from django.contrib.auth.models import User

class cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_cliente
        
class mascota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=30)
    observaciones = models.TextField(blank=True, null=True)
    telefono_contacto = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.nombre 
    
class servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_servicio 

  
    
class cita(models.Model):
    mascota = models.ForeignKey(mascota, on_delete=models.CASCADE)
    servicio = models.ForeignKey(servicio, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Cita para {self.mascota.nombre} - {self.servicio.nombre_servicio} en {self.fecha_hora}"


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

        
