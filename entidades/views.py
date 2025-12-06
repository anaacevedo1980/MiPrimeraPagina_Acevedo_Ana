from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import mascota, servicio, cliente, cita
from .forms import MascotaForm, ServicioForm, ClienteForm, CitaForm

def home(request):
    return render(request, 'entidades/index.html')

# MASCOTAS
def mascotas_list(request):
    mascotas = mascota.objects.all()
    return render(request, 'entidades/mascota_list.html', {'mascotas': mascotas})

def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm()
    return render(request, 'entidades/mascota_form.html', {'form': form, 'title': 'Crear Mascota'})

# SERVICIOS
def servicios_list(request):
    servicios = servicio.objects.all()
    return render(request, 'entidades/servicio_list.html', {'servicios': servicios})

def servicio_create(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios_list')
    else:
        form = ServicioForm()
    return render(request, 'entidades/servicio_form.html', {'form': form, 'title': 'Crear Servicio'})

# CLIENTES
def clientes_list(request):
    clientes = cliente.objects.all()
    return render(request, 'entidades/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm()
    return render(request, 'entidades/cliente_form.html', {'form': form, 'title': 'Crear Cliente'})

# CITAS
def citas_list(request):
    citas = cita.objects.all()
    return render(request, 'entidades/cita_list.html', {'citas': citas})

def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm()
    return render(request, 'entidades/cita_form.html', {'form': form, 'title': 'Crear Cita'})

# BÚSQUEDA
def buscar_mascota(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = mascota.objects.filter(nombre__icontains=query)
    return render(request, 'entidades/buscar.html', {'resultados': resultados, 'query': query})


