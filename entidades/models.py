from django.db import models

# Create your models here.
class mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre      
class servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_servicio         
class cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_cliente
class cita(models.Model):
    mascota = models.ForeignKey(mascota, on_delete=models.CASCADE)
    servicio = models.ForeignKey(servicio, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Cita para {self.mascota.nombre} - {self.servicio.nombre_servicio} en {self.fecha_hora}"    


        
