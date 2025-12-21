from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import mascota, servicio, cliente, cita
from .forms import MascotaForm, ServicioForm, ClienteForm, CitaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Perfil
from .forms import RegistroForm, LoginForm, PerfilForm

def home(request):
    return render(request, 'entidades/index.html')

########################################################## MASCOTAS #####################################################################

# LISTAR MASCOTAS
@login_required(login_url='login')
def mascotas_list(request):
    mascotas = mascota.objects.all()
    return render(request, 'entidades/mascota_list.html', {'mascotas': mascotas})


# CREAR MASCOTAS
@login_required(login_url='login')
def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.usuario = request.user
            m.save()
            return redirect('mascotas_list')
    else:
        form = MascotaForm()
    return render(request, 'entidades/mascota_form.html', {'form': form, 'title': 'Crear Mascota'})


# EDITAR MASCOTAS
@login_required(login_url='login')
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
@login_required(login_url='login')
def mascota_delete(request, pk):
    m = mascota.objects.get(pk=pk)
    
    if request.method == 'POST':
        m.delete()
        return redirect('mascotas_list')
    return render(request, 'entidades/mascota_confirm_delete.html', {'objeto': m})


########################################################## SERVICIOS #####################################################################

# SERVICIOS
def servicios_list(request):
    servicios = servicio.objects.all()
    return render(request, 'entidades/servicio_list.html', {'servicios': servicios})


# CREAR SERVICIOS
@login_required(login_url='login')
def servicio_create(request):
    if not request.user.is_staff:
        return redirect('servicios_list')
    
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios_list')
    else:
        form = ServicioForm()
    return render(request, 'entidades/servicio_form.html', {'form': form, 'title': 'Crear Servicio'})


# EDITAR SERVICIOS
@login_required(login_url='login')
def servicio_edit(request, pk):
    if not request.user.is_staff:
        return redirect('servicios_list')
    
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
@login_required(login_url='login')
def servicio_delete(request, pk):
    if not request.user.is_staff:
        return redirect('servicios_list')
    
    s = servicio.objects.get(pk=pk)
    if request.method == 'POST':
        s.delete()
        return redirect('servicios_list')
    return render(request, 'entidades/servicio_confirm_delete.html', {'objeto': s})


########################################################## CLIENTES #####################################################################

# CLIENTES
@login_required(login_url='login')
def clientes_list(request):
    clientes = cliente.objects.all()
    return render(request, 'entidades/cliente_list.html', {'clientes': clientes})


# CREAR CLIENTES
@login_required(login_url='login')
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm()
    return render(request, 'entidades/cliente_form.html', {'form': form, 'title': 'Crear Cliente'})


# EDITAR CLIENTES
@login_required(login_url='login')
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

@login_required(login_url='login')
def cliente_delete(request, pk):
    c = cliente.objects.get(pk=pk)
    if request.method == 'POST':
        c.delete()
        return redirect('clientes_list')
    return render(request, 'entidades/cliente_confirm_delete.html', {'objeto': c})


########################################################## CITAS #####################################################################

# CITAS
@login_required(login_url='login')
def citas_list(request):
    if request.user.is_staff:  # Si es admin
        citas = cita.objects.all()
    else:  # Si es usuario normal, solo sus citas
        citas = cita.objects.filter(mascota__usuario=request.user)
    return render(request, 'entidades/cita_list.html', {'citas': citas})


# CREAR CITAS
@login_required(login_url='login')
def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            # Verificar que la mascota pertenece al usuario
            if form.cleaned_data['mascota'].usuario != request.user and not request.user.is_staff:
                return redirect('citas_list')
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm()
        # Filtrar mascotas según el usuario
        if not request.user.is_staff:
            form.fields['mascota'].queryset = mascota.objects.filter(usuario=request.user)
    return render(request, 'entidades/cita_form.html', {'form': form, 'title': 'Crear Cita'})


# EDITAR CITAS
@login_required(login_url='login')
def cita_edit(request, pk):
    ci = cita.objects.get(pk=pk)
    # Verificar permisos
    if ci.mascota.usuario != request.user and not request.user.is_staff:
        return redirect('citas_list')
    
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=ci)
        if form.is_valid():
            form.save()
            return redirect('citas_list')
    else:
        form = CitaForm(instance=ci)
        if not request.user.is_staff:
            form.fields['mascota'].queryset = mascota.objects.filter(usuario=request.user)
    return render(request, 'entidades/cita_form.html', {'form': form, 'title': 'Editar Cita'})

# ELIMINAR CITAS
@login_required(login_url='login')
def cita_delete(request, pk):
    ci = cita.objects.get(pk=pk)
    # Verificar permisos
    if ci.mascota.usuario != request.user and not request.user.is_staff:
        return redirect('citas_list')
    
    if request.method == 'POST':
        ci.delete()
        return redirect('citas_list')
    return render(request, 'entidades/cita_confirm_delete.html', {'objeto': ci})



########################################################## BUSQUEDA #####################################################################

# BÚSQUEDA
@login_required(login_url='login')
def buscar_mascota(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        if request.user.is_staff:
            resultados = mascota.objects.filter(nombre__icontains=query)
        else:
            resultados = mascota.objects.filter(usuario=request.user, nombre__icontains=query)
    return render(request, 'entidades/buscar.html', {'resultados': resultados, 'query': query})



@login_required(login_url='login')
def mascotas_por_cliente(request, pk):
    cliente_obj = cliente.objects.get(pk=pk)
    mascotas = mascota.objects.filter(cliente=cliente_obj)
    return render(request, 'entidades/mascotas_por_cliente.html', {'cliente': cliente_obj, 'mascotas': mascotas})

@login_required(login_url='login')
def citas_por_cliente(request, pk):
    cliente_obj = cliente.objects.get(pk=pk)
    mascotas_cliente = mascota.objects.filter(cliente=cliente_obj)
    citas = cita.objects.filter(mascota__in=mascotas_cliente)
    return render(request, 'entidades/citas_por_cliente.html', {'cliente': cliente_obj, 'citas': citas})


########################################################## REGISTRO #####################################################################

# REGISTRO
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'entidades/registro.html', {'form': form})


########################################################## LOGIN #####################################################################

# LOGIN
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'entidades/login.html', {'form': form})


########################################################## LOGOUT #####################################################################

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')



########################################################## PERFIL #####################################################################

# EDITAR PERFIL
@login_required(login_url='login')
def editar_perfil(request):
    # Crear Perfil si no existe
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'entidades/editar_perfil.html', {'form': form, 'perfil': perfil})


########################################################## ACERCA DE MI #####################################################################

# ACERCA DE MÍ
# ACERCA DE MÍ

def acerca_de_mi(request):
    datos = {
        'nombre': 'Ana',
        'apellido': 'Acevedo',
        'email': 'anaacevedo@gmail.com',
        'ciudad': 'Concepción del Uruguay',
        'pais': 'Argentina',
        'descripcion': [
            'Soy Ingeniera en Sistemas de Información, graduada en la UTN – Regional Concepción del Uruguay, con sólida experiencia en el sector asegurador, donde actualmente desempeño funciones en el área de Estadísticas y Prospectivas. Mi rol se centra en transformar datos en insights accionables, aportando valor estratégico a la toma de decisiones del negocio.',
            'Con una clara orientación al futuro, me encuentro profundizando mi formación en Ciencia de Datos y Machine Learning, con el objetivo de potenciar modelos predictivos, automatizar procesos analíticos y escalar soluciones basadas en datos dentro de entornos corporativos complejos. Creo firmemente en la analítica como motor de eficiencia, anticipación y ventaja competitiva, especialmente en industrias intensivas en información como la del seguro.',
            'A nivel técnico, cuento con experiencia en Power BI, Qlik Sense y base de datos relacionales, combinando desarrollo, análisis y automatización en soluciones integrales y escalables.',
            'Más allá del ámbito profesional, el running es una parte fundamental de mi identidad. Desde hace más de diez años practico esta disciplina con constancia y enfoque, habiendo completado tres maratones de 42 km en la ciudad de Buenos Aires, además de múltiples competencias de trail y montaña en distintas provincias del país.',
            'Esta mentalidad de resistencia, disciplina y mejora continua se refleja directamente en mi forma de trabajar. Complemento esta actividad con crossfit, lo que refuerza mi equilibrio físico y mental, y potencia mi rendimiento diario.',
            'Me definen la curiosidad permanente, la orientación a resultados, y la capacidad de conectar tecnología, datos y negocio para generar impacto real.'
        ],
        'skills': ['Base de datos', 'Git', 'Machine Learning', 'Power BI', 'Qlik Sense', 'SQL'],
    }
    return render(request, 'entidades/acerca_de_mi.html', {'datos': datos})




