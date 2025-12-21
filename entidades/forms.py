from django import forms
from .models import mascota, servicio, cliente, cita, Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MascotaForm(forms.ModelForm):
    class Meta:
        model = mascota
        fields = ['cliente', 'nombre', 'raza', 'edad', 'tipo', 'observaciones', 'telefono_contacto']
        labels = {
            'cliente': 'Dueño/Cliente',
            'nombre': 'Nombre de la Mascota',
            'raza': 'Raza',
            'edad': 'Edad (años)',
            'tipo': 'Tipo de Mascota',
            'observaciones': 'Observaciones',
            'telefono_contacto': 'Teléfono de Contacto',
        }
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
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

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'telefono', 'email']