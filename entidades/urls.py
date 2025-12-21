from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    
    # AUTENTICACIÓN
    path('registro/', views.registro, name='registro'),
    
    # MASCOTAS
    path('mascotas/', views.mascotas_list, name='mascotas_list'),
    path('mascotas/crear/', views.mascota_create, name='mascota_create'),
    path('mascotas/<int:pk>/editar/', views.mascota_edit, name='mascota_edit'),
    path('mascotas/<int:pk>/eliminar/', views.mascota_delete, name='mascota_delete'),
    
    # SERVICIOS
    path('servicios/', views.servicios_list, name='servicios_list'),
    path('servicios/crear/', views.servicio_create, name='servicio_create'),
    path('servicios/<int:pk>/editar/', views.servicio_edit, name='servicio_edit'),
    path('servicios/<int:pk>/eliminar/', views.servicio_delete, name='servicio_delete'),
    
    # CLIENTES
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_edit, name='cliente_edit'),
    path('clientes/<int:pk>/eliminar/', views.cliente_delete, name='cliente_delete'),
    
    # CITAS
    path('citas/', views.citas_list, name='citas_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/<int:pk>/editar/', views.cita_edit, name='cita_edit'),
    path('citas/<int:pk>/eliminar/', views.cita_delete, name='cita_delete'),
    
    # BÚSQUEDA
    path('buscar/', views.buscar_mascota, name='buscar_mascota'),
    
    # AUTENTICACIÓN
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    
    # MASCOTAS
    path('mascotas/', views.mascotas_list, name='mascotas_list'),
    path('mascotas/crear/', views.mascota_create, name='mascota_create'),
    path('mascotas/<int:pk>/editar/', views.mascota_edit, name='mascota_edit'),
    path('mascotas/<int:pk>/eliminar/', views.mascota_delete, name='mascota_delete'),
    
    # SERVICIOS
    path('servicios/', views.servicios_list, name='servicios_list'),
    path('servicios/crear/', views.servicio_create, name='servicio_create'),
    path('servicios/<int:pk>/editar/', views.servicio_edit, name='servicio_edit'),
    path('servicios/<int:pk>/eliminar/', views.servicio_delete, name='servicio_delete'),
    
    # CLIENTES
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_edit, name='cliente_edit'),
    path('clientes/<int:pk>/eliminar/', views.cliente_delete, name='cliente_delete'),
    path('clientes/<int:pk>/mascotas/', views.mascotas_por_cliente, name='mascotas_por_cliente'),
    path('clientes/<int:pk>/citas/', views.citas_por_cliente, name='citas_por_cliente'),
    
    # CITAS
    path('citas/', views.citas_list, name='citas_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/<int:pk>/editar/', views.cita_edit, name='cita_edit'),
    path('citas/<int:pk>/eliminar/', views.cita_delete, name='cita_delete'),
    
    # BÚSQUEDA
    path('buscar/', views.buscar_mascota, name='buscar_mascota'),
]