from django import forms
from .models import mascota, servicio, cliente, cita

class MascotaForm(forms.ModelForm):
    class Meta:
        model = mascota
        fields = ['nombre', 'edad', 'tipo']
        labels = {
            'nombre': 'Nombre de la mascota',
            'edad': 'Edad',
            'tipo': 'Tipo de mascota',
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = servicio
        fields = ['nombre_servicio', 'descripcion', 'precio']
        labels = {
            'nombre_servicio': 'Nombre del servicio',
            'descripcion': 'Descripción',
            'precio': 'Precio',
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre_cliente', 'email', 'telefono']
        labels = {
            'nombre_cliente': 'Nombre del cliente',
            'email': 'Email',
            'telefono': 'Teléfono',
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = cita
        fields = ['mascota', 'servicio', 'fecha_hora']
        labels = {
            'mascota': 'Mascota',
            'servicio': 'Servicio',
            'fecha_hora': 'Fecha y hora',
        }
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }