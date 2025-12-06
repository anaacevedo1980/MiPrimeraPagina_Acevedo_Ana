from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),
    
    # MASCOTAS
    path('mascotas/', views.mascotas_list, name='mascotas_list'),
    path('mascotas/crear/', views.mascota_create, name='mascota_create'),
    
    # SERVICIOS
    path('servicios/', views.servicios_list, name='servicios_list'),
    path('servicios/crear/', views.servicio_create, name='servicio_create'),
    
    # CLIENTES
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    
    # CITAS
    path('citas/', views.citas_list, name='citas_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    
    # BÚSQUEDA
    path('buscar/', views.buscar_mascota, name='buscar_mascota'),
]