from django.contrib import admin
from .models import mascota, servicio, cliente, cita, Perfil

@admin.register(mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'tipo']

@admin.register(servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre_servicio', 'precio']

@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre_cliente', 'email', 'telefono']

@admin.register(cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ['mascota', 'servicio', 'fecha_hora']

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'telefono', 'email', 'fecha_creacion']