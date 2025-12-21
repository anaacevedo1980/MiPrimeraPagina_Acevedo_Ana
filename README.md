# Guardería de Mascotas

Una aplicación web completa en Django para gestionar una guardería de mascotas con sistema de autenticación, roles de usuario y CRUD completo de mascotas, servicios, clientes y citas.

## Características Principales

###  Sistema de Autenticación
- Registro de nuevos usuarios
- Login/Logout
- Perfil de usuario con avatar
- Cambio de contraseña
- Dos niveles de acceso: Admin (Dueño/Gerente) y Empleados

###  Gestión de Usuarios
- **Admin (is_staff=True)**: Acceso completo a todas las funcionalidades
- **Empleados**: Pueden crear/editar/ver información de clientes y mascotas

###  Gestión de Mascotas
- Crear, ver, editar y eliminar mascotas
- Campos: Nombre, Raza, Edad, Tipo, Observaciones, Teléfono de contacto
- Relación con Cliente (dueño de la mascota)
- Búsqueda de mascotas por nombre
- Vista de mascotas por cliente

###  Gestión de Clientes
- Crear, ver, editar y eliminar clientes
- Información: Nombre, Email, Teléfono
- Ver todas las mascotas de un cliente
- Ver todas las citas de un cliente

###  Servicios
- Listado de servicios disponibles
- Solo admin puede crear, editar y eliminar servicios
- Campos: Nombre, Descripción, Precio

###  Gestión de Citas
- Crear, ver, editar y eliminar citas
- Relación con Mascota y Servicio
- Fecha y hora de la cita
- Filtro por usuario/mascota

###  Acerca de Mí
- Página con información del creador de la aplicación
- Datos personales y profesionales
- Habilidades técnicas

## Tecnologías Utilizadas

- **Backend**: Django 5.2.8
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Base de Datos**: SQLite
- **Autenticación**: Django Auth
- **Gestión de Imágenes**: Pillow

## Instalación

### Requisitos Previos
- Python 3.8+
- pip

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
   git clone https://github.com/Mi_USUARIO/MiPrimeraPagina_Acevedo_Ana.git
   cd MiPrimeraPagina_Acevedo_Ana
```

2. **Instalar dependencias**
```bash
   pip install -r requirements.txt
```

3. **Realizar migraciones**
```bash
   python manage.py migrate
```

4. **Crear superusuario (Admin)**
```bash
   python manage.py createsuperuser
```
   Ingresa:
   - Username:  admin
   - Email: anaacevedo@gmail.com
   - Password: Feli10

5. **Ejecutar el servidor**
```bash
   python manage.py runserver
```

6. **Acceder a la aplicación**
```
   http://localhost:8000
```

## Uso de la Aplicación

### Para Usuarios Admin

**Acceso Completo a:**
- Crear/Editar/Eliminar Clientes
- Crear/Editar/Eliminar Mascotas
- Crear/Editar/Eliminar Servicios
- Crear/Editar/Eliminar Citas
- Ver Panel Admin: http://localhost:8000/admin/
- Ver mascotas y citas de cada cliente

### Para Empleados

**Funcionalidades Disponibles:**
- Ver todos los clientes
- Ver todas las mascotas
- Crear/Editar/Eliminar mascotas
- Ver y crear citas
- Buscar mascotas
- Ver mascotas y citas por cliente

### Navegación Principal

- **Home** (`/`): Página principal con información de la guardería
- **Mascotas** (`/mascotas/`): Listado de todas las mascotas
- **Servicios** (`/servicios/`): Servicios disponibles
- **Clientes** (`/clientes/`): Gestión de clientes
- **Citas** (`/citas/`): Gestión de citas
- **Buscar** (`/buscar/`): Buscar mascotas por nombre
- **Acerca de Mí** (`/acerca-de-mi/`): Información del creador
- **Mi Perfil** (`/perfil/editar/`): Editar perfil personal
- **Login** (`/login/`): Iniciar sesión
- **Registro** (`/registro/`): Crear nueva cuenta

## Estructura del Proyecto
```
mascotas/
├── entidades/
│   ├── migrations/
│   ├── templates/entidades/
│   │   ├── base.html (plantilla base)
│   │   ├── index.html (página principal)
│   │   ├── mascota_list.html
│   │   ├── mascota_form.html
│   │   ├── mascota_confirm_delete.html
│   │   ├── servicio_list.html
│   │   ├── servicio_form.html
│   │   ├── cliente_list.html
│   │   ├── cliente_form.html
│   │   ├── cita_list.html
│   │   ├── cita_form.html
│   │   ├── buscar.html
│   │   ├── login.html
│   │   ├── registro.html
│   │   ├── editar_perfil.html
│   │   ├── acerca_de_mi.html
│   │   ├── mascotas_por_cliente.html
│   │   └── citas_por_cliente.html
│   ├── static/ (CSS, JS, imágenes)
│   ├── models.py (Modelos de datos)
│   ├── forms.py (Formularios)
│   ├── views.py (Vistas)
│   ├── urls.py (Rutas)
│   └── admin.py (Configuración admin)
├── mascotas/
│   ├── settings.py (Configuración)
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Modelos de Datos

### mascota
- usuario (ForeignKey a User)
- cliente (ForeignKey a cliente)
- nombre (CharField)
- raza (CharField)
- edad (IntegerField)
- tipo (CharField)
- observaciones (TextField)
- telefono_contacto (CharField)

### servicio
- nombre_servicio (CharField)
- descripcion (TextField)
- precio (DecimalField)

### cliente
- nombre_cliente (CharField)
- email (EmailField)
- telefono (CharField)

### cita
- mascota (ForeignKey a mascota)
- servicio (ForeignKey a servicio)
- fecha_hora (DateTimeField)

### Perfil
- usuario (OneToOneField a User)
- avatar (ImageField)
- telefono (CharField)
- email (EmailField)
- fecha_creacion (DateTimeField)

## Funcionalidades Detalladas

###  Búsqueda de Mascotas
- Busca mascotas por nombre
- Filtra por usuario (empleados ven solo sus mascotas, admin ve todas)
- Muestra: Nombre, Raza, Edad, Tipo, Cliente, Teléfono, Observaciones

###  Gestión de Clientes
- Botón "Mascotas": Ver todas las mascotas de un cliente
- Botón "Citas": Ver todas las citas de las mascotas del cliente
- Botones "Editar" y "Eliminar": Solo para admin

###  Gestión de Mascotas
- Cada mascota está asociada a un cliente
- Empleados pueden crear/editar mascotas de cualquier cliente
- Admin tiene control total

###  Gestión de Citas
- Filtro automático de mascotas por usuario (empleados) o todas (admin)
- Relación directa entre Mascota, Servicio y fecha/hora

###  Herencia de Templates
- base.html: Plantilla principal con navbar y footer
- Todos los templates heredan de base.html
- NavBar con acceso a todas las secciones
- Navbar oscuro en páginas de contenido, transparente en home

## Seguridad

- Autenticación requerida para todas las funciones
- Validación de permisos en vistas
- Contraseñas hasheadas en la base de datos
- CSRF protection en formularios
- Solo usuarios logueados pueden ver/editar datos

## Próximas Mejoras (Opcionales)

- Sistema de disponibilidad de horarios para citas
- Notificaciones por email
- Reportes de citas
- Sistema de pagos
- Aplicación mobile
- API REST

## Autor

Ana Acevedo  
anaacevedo@gmail.com  
Concepción del Uruguay, Argentina

## Licencia

MIT License

---

**Versión**: 1.0.0  
**Última actualización**: Diciembre 2025
