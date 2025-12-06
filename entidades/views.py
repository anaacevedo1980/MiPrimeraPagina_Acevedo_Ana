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


# EDITAR MASCOTAS
def mascota_edit(request, pk):
    m = mascota.objects.get(pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=m)
        if form.is_valid():
            form.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm(instance=m)
    return render(request, 'entidades/mascota_form.html', {'form': form, 'title': 'Editar Mascota'})

# ELIMINAR MASCOTAS
def mascota_delete(request, pk):
    m = mascota.objects.get(pk=pk)
    if request.method == 'POST':
        m.delete()
        return redirect('mascotas_list')
    return render(request, 'entidades/mascota_confirm_delete.html', {'objeto': m})


# EDITAR SERVICIOS
def servicio_edit(request, pk):
    s = servicio.objects.get(pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return redirect('servicios_list')
    else:
        form = ServicioForm(instance=s)
    return render(request, 'entidades/servicio_form.html', {'form': form, 'title': 'Editar Servicio'})

# ELIMINAR SERVICIOS
def servicio_delete(request, pk):
    s = servicio.objects.get(pk=pk)
    if request.method == 'POST':
        s.delete()
        return redirect('servicios_list')
    return render(request, 'entidades/servicio_confirm_delete.html', {'objeto': s})

# EDITAR CLIENTES
def cliente_edit(request, pk):
    c = cliente.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm(instance=c)
    return render(request, 'entidades/cliente_form.html', {'form': form, 'title': 'Editar Cliente'})

# ELIMINAR CLIENTES
def cliente_delete(request, pk):
    c = cliente.objects.get(pk=pk)
    if request.method == 'POST':
        c.delete()
        return redirect('clientes_list')
    return render(request, 'entidades/cliente_confirm_delete.html', {'objeto': c})

# EDITAR CITAS
def cita_edit(request, pk):
    ci = cita.objects.get(pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=ci)
        if form.is_valid():
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm(instance=ci)
    return render(request, 'entidades/cita_form.html', {'form': form, 'title': 'Editar Cita'})

# ELIMINAR CITAS
def cita_delete(request, pk):
    ci = cita.objects.get(pk=pk)
    if request.method == 'POST':
        ci.delete()
        return redirect('citas_list')
    return render(request, 'entidades/cita_confirm_delete.html', {'objeto': ci})




