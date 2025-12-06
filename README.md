# Guardería de Mascotas

Una aplicación web en Django para gestionar una guardería de mascotas con herencia de plantillas, múltiples modelos y formularios.

## Funcionalidades

- **Gestión de Mascotas**: Crear, ver listado de mascotas
- **Gestión de Servicios**: Crear, ver listado de servicios disponibles
- **Gestión de Clientes**: Crear, ver listado de clientes
- **Gestión de Citas**: Agendar citas para mascotas
- **Búsqueda**: Buscar mascotas por nombre
- **Panel Admin**: Administrar todos los datos desde Django Admin

## Tecnologías

- Django 5.2.8
- Python 3.13
- Bootstrap 5
- SQLite

## Instalación

1. **Clonar el repositorio**
```bash
   git https://github.com/anaacevedo1980/MiPrimeraPagina_Acevedo_Ana.git
   cd MiPrimeraPagina_Acevedo_Ana
```

2. **Instalar dependencias**
```bash
   pip install django
```

3. **Hacer migraciones**
```bash
   python manage.py migrate
```

4. **Crear superusuario (admin)**
```bash
   python manage.py createsuperuser
```

5. **Ejecutar el servidor**
```bash
   python manage.py runserver
```

## Cómo usar

### Página Principal
- Accede a `http://localhost:8000/`
- Verás la página de bienvenida con información sobre los servicios

### Gestión de Mascotas
1. Ve a `http://localhost:8000/mascotas/`
2. Haz clic en **"+ Agregar Mascota"**
3. Completa el formulario (nombre, edad, tipo)
4. Verás la lista de todas las mascotas registradas

### Gestión de Servicios
1. Ve a `http://localhost:8000/servicios/`
2. Haz clic en **"+ Agregar Servicio"**
3. Completa el formulario (nombre, descripción, precio)
4. Verás el listado de servicios

### Gestión de Clientes
1. Ve a `http://localhost:8000/clientes/`
2. Haz clic en **"+ Agregar Cliente"**
3. Completa el formulario (nombre, email, teléfono)
4. Verás el listado de clientes

### Agendar Citas
1. Ve a `http://localhost:8000/citas/`
2. Haz clic en **"+ Agendar Cita"**
3. Selecciona mascota, servicio y fecha/hora
4. Verás el listado de citas

### Editar y Eliminar Registros
En todas las listas (Mascotas, Servicios, Clientes, Citas) encontrarás dos botones por cada registro:

- **Botón Editar (amarillo)**: Permite modificar los datos del registro
  - Haz clic en "Editar"
  - Modifica los campos que desees
  - Haz clic en "Guardar"

- **Botón Eliminar (rojo)**: Elimina el registro
  - Haz clic en "Eliminar"
  - Se abrirá una página de confirmación
  - Haz clic en "Sí, Eliminar" para confirmar
  - El registro será eliminado permanentemente


### Buscar Mascotas
1. Ve a `http://localhost:8000/buscar/`
2. Ingresa el nombre de la mascota
3. Verás los resultados de la búsqueda

### Panel Admin
1. Ve a `http://localhost:8000/admin/`
2. Ingresa con las credenciales de superusuario
3. Aquí puedes ver, crear, editar y eliminar todos los datos

## Estructura de carpetas
```
mascotas/
├── entidades/
│   ├── templates/
│   │   └── entidades/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── mascota_list.html
│   │       ├── mascota_form.html
│   │       ├── servicio_list.html
│   │       ├── servicio_form.html
│   │       ├── cliente_list.html
│   │       ├── cliente_form.html
│   │       ├── cita_list.html
│   │       ├── cita_form.html
│   │       └── buscar.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── mascotas/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── servicios.db
└── README.md
```

## Modelos

### Mascota
- nombre (CharField)
- edad (IntegerField)
- tipo (CharField)

### Servicio
- nombre_servicio (CharField)
- descripcion (TextField)
- precio (DecimalField)

### Cliente
- nombre_cliente (CharField)
- email (EmailField)
- telefono (CharField)

### Cita
- mascota (ForeignKey a Mascota)
- servicio (ForeignKey a Servicio)
- fecha_hora (DateTimeField)

## Autor

Ana Acevedo

## Licencia

MIT
