from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario, RolUsuario, GeneroUsuario, NombreRegion, Juego, Categoria
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as auth_logout
from .forms import EditarPerfilForm, CambiarContrasenaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .forms import JuegoForm
from django.views.decorators.csrf import csrf_exempt
from .decoradores import usuario_logueado_requerido, admin_requerido
import requests
from django.http import JsonResponse
from .serializers import JuegoSerializer, NombreRegionSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response





# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def categorias(request):
    return render(request, 'categorias.html')

@usuario_logueado_requerido
def carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

def login(request):
    form = UsuarioForm()
    roles = RolUsuario.objects.all()
    return render(request, 'login.html', {
        'form': form,
        'roles': roles,
    })

def perfil(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')  # Redirige si no hay sesión

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('login')
    
    # Verificar si el usuario tiene el rol de administrador
    es_administrador = usuario.rol.rol_usuario == 'administrador'

    if request.method == 'POST':
        if 'guardar_perfil' in request.POST:
            perfil_form = EditarPerfilForm(request.POST, instance=usuario)
            contrasena_form = CambiarContrasenaForm()  # necesario para renderizar el otro form

            if perfil_form.is_valid():
                perfil_form.save()
                messages.success(request, 'Perfil actualizado correctamente.')
                return redirect('perfil')

        elif 'cambiar_contrasena' in request.POST:
            perfil_form = EditarPerfilForm(instance=usuario)  # necesario para renderizar el otro form
            contrasena_form = CambiarContrasenaForm(request.POST)

            if contrasena_form.is_valid():
                actual = contrasena_form.cleaned_data['contrasena_actual']
                nueva = contrasena_form.cleaned_data['nueva_contrasena']
                confirmar = contrasena_form.cleaned_data['confirmar_contrasena']

                if actual != usuario.password:
                    messages.error(request, 'La contraseña actual es incorrecta.')
                elif nueva != confirmar:
                    messages.error(request, 'Las contraseñas no coinciden.')
                else:
                    usuario.password = nueva
                    usuario.save()
                    messages.success(request, 'Contraseña actualizada correctamente.')
                    return redirect('perfil')
    else:
        perfil_form = EditarPerfilForm(instance=usuario)
        contrasena_form = CambiarContrasenaForm()

    context = {
        'usuario': usuario,
        'perfil_form': perfil_form,
        'contrasena_form': contrasena_form,
        'es_administrador': es_administrador,
    }
    return render(request, 'perfil.html', context)

def formulario(request):
    # Recuperar datos para los selects
    roles = RolUsuario.objects.all()
    generos = GeneroUsuario.objects.all()
    regiones = NombreRegion.objects.all()
    form = UsuarioForm()

    return render(request, 'formulario.html', {
        'form': form,
        'roles': roles,
        'generos': generos,
        'regiones': regiones,
    })

@admin_requerido
def admininicio(request):
    roles = RolUsuario.objects.all()
    generos = GeneroUsuario.objects.all()
    regiones = NombreRegion.objects.all()
    usuarios = Usuario.objects.all()
    juegos = Juego.objects.all()
    categorias = Categoria.objects.all()

    usuario_form = UsuarioForm()
    juego_form = JuegoForm()

    if request.method == 'POST':
        if 'submit_game' in request.POST:
            juego_form = JuegoForm(request.POST, request.FILES)
            if juego_form.is_valid():
                juego_form.save()
                messages.success(request, "Juego creado exitosamente.")
                return redirect('admininicio')
            else:
                messages.error(request, "Por favor corrige los errores en el formulario del juego.")
        
        elif 'submit_user' in request.POST:
            usuario_form = UsuarioForm(request.POST)
            if usuario_form.is_valid():
                usuario_form.save()
                messages.success(request, "Usuario registrado exitosamente.")
                return redirect('admininicio')
            else:
                messages.error(request, "Por favor corrige los errores en el formulario del usuario.")

    context = {
        'form_juego': juego_form,
        'form_usuario': usuario_form,
        'usuarios': usuarios,
        'roles': roles,
        'generos': generos,
        'regiones': regiones,
        'juegos': juegos,
        'categorias': categorias,
    }

    return render(request, 'admininicio.html', context)



def blogs(request):
    return render(request, 'blogs.html') 

@usuario_logueado_requerido
def blog_forest2(request):
    return render(request, 'blog_forest2.html') 

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, RolUsuario, GeneroUsuario, NombreRegion

def registrar_usuario(request):
    # Recuperar datos para los selects
    roles = RolUsuario.objects.all()
    generos = GeneroUsuario.objects.all()
    regiones = NombreRegion.objects.all()

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            correo = form.cleaned_data['correo']

            # Verificar si el usuario o correo ya existen
            if Usuario.objects.filter(usuario=usuario).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
            elif Usuario.objects.filter(correo=correo).exists():
                messages.error(request, 'El correo ya está registrado.')
            else:
                form.save()
                messages.success(request, 'Usuario registrado exitosamente.')
                return redirect('login')  # Redirigir a otra página, si lo deseas
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = UsuarioForm()

    # Retornar la respuesta con el formulario y los datos de los selects
    return render(request, 'login.html', {
        'form': form,         # El formulario
        'roles': roles,       # Los roles para el select
        'generos': generos,   # Los géneros para el select
        'regiones': regiones, # Las regiones para el select
    })


def login_usuario(request):
    # Si el usuario ya está logueado, redirigir a la vista que pidió originalmente (si existe)
    if 'usuario_id' in request.session:
        next_url = request.GET.get('next') or request.POST.get('next')
        return redirect(next_url or 'perfil')

    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        next_url = request.POST.get('next')  # Obtener la URL a la que redirigir tras login

        try:
            usuario = Usuario.objects.get(correo=correo)

            if usuario.password == password:
                # Guardar datos en sesión
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                request.session['usuario_rol'] = usuario.rol.rol_usuario

                return redirect(next_url or 'perfil')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'El correo no está registrado.')

    # Si es GET o hubo errores, renderizar login con next (para que no se pierda)
    next_url = request.GET.get('next', '')
    return render(request, 'login.html', {'next': next_url})



def logout_usuario(request):
    # Cerrar sesión
    auth_logout(request)
    # Eliminar datos de la sesión manualmente
    request.session.flush()
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')  


def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    # Opcional: protección para evitar que se borre a sí mismo
    if request.session.get('usuario_id') == usuario_id:
        messages.error(request, "No puedes eliminar tu propio usuario.")
        return redirect('admininicio')

    usuario.delete()
    messages.success(request, "Usuario eliminado exitosamente.")
    return redirect('admininicio')

def juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos.html', {'juegos': juegos})

def juegos_catalogo(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos.html', {'juegos': juegos})

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Juego


def agregar_al_carrito(request, juego_id):
    if 'usuario_id' not in request.session:
        # Si no está logeado, redirigir al login con la URL a la que se quería acceder (next)
        return redirect(f"{reverse('login_usuario')}?next={request.path}")
    
    juego = get_object_or_404(Juego, id=juego_id)
    
    # Obtener el carrito de la sesión, si no existe, inicializarlo como un diccionario vacío
    carrito = request.session.get('carrito', {})
    if not isinstance(carrito, dict):  # Verificar que el carrito sea un diccionario
        carrito = {}
    
    # Verificar si el juego ya está en el carrito
    if str(juego.id) in carrito:
        carrito[str(juego.id)]['cantidad'] += 1  # Si ya está, aumentamos la cantidad
    else:
        carrito[str(juego.id)] = {
            'nombre': juego.nombre,
            'precio': float(juego.precio),  # Convertir a float para evitar problemas con Decimal
            'imagen': juego.imagen.url if juego.imagen else None,
            'cantidad': 1
        }
    
    # Guardar el carrito actualizado en la sesión
    request.session['carrito'] = carrito
    
    return redirect('carrito')  # Redirigir al carrito

def eliminar_del_carrito(request, juego_id): 
    # Obtener el carrito de la sesión
    carrito = request.session.get('carrito', {})
    
    # Eliminar el juego del carrito si existe
    if str(juego_id) in carrito:
        del carrito[str(juego_id)]
    
    # Guardar el carrito actualizado en la sesión
    request.session['carrito'] = carrito
    
    return redirect('carrito')  # Redirigir al carrito


def finalizar_compra(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('carrito')

    juegos_comprados = []
    total = 0

    for juego_id, item in carrito.items():
        juegos_comprados.append({
            'nombre': item['nombre'],
            'cantidad': item['cantidad'],
            'precio': item['precio'],
            'subtotal': item['cantidad'] * item['precio'],
            'imagen': item['imagen'],
        })
        total += item['cantidad'] * item['precio']

    # Vaciar el carrito
    request.session['carrito'] = {}

    context = {
        'juegos_comprados': juegos_comprados,
        'total': total,
    }
    return render(request, 'compra_realizada.html', context)

def eliminar_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    juego.delete()  # Elimina el juego de la base de datos
    messages.success(request, "Juego eliminado exitosamente.")
    return redirect('admininicio')  # Redirige al panel de administración

@csrf_exempt
def editar_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)

    if request.method == 'POST':
        juego.nombre = request.POST.get('nombre')
        juego.precio = request.POST.get('precio')
        juego.descripcion = request.POST.get('descripcion')
        juego.categoria_id = request.POST.get('categoria')

        if 'imagen' in request.FILES:
            juego.imagen = request.FILES['imagen']

        juego.save()
        return redirect('admininicio')  # Cambia a tu URL principal

    return redirect('admininicio')

def contraseña(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        nueva_contrasena = request.POST.get('nueva_contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')

        try:
            # Buscar al usuario por el correo
            usuario = Usuario.objects.get(correo=correo)

            # Verificar si las contraseñas coinciden
            if nueva_contrasena != confirmar_contrasena:
                messages.error(request, 'Las contraseñas no coinciden.')
            else:
                # Guardar la nueva contraseña tal cual sin encriptar
                usuario.password = nueva_contrasena
                usuario.save()

                messages.success(request, 'Contraseña actualizada correctamente. Ahora puedes iniciar sesión.')
                return redirect('login')
        except Usuario.DoesNotExist:
            messages.error(request, 'El correo no está registrado.')

    return render(request, 'contraseña.html')

#API CheapShark 
def buscar_juegos(request):
    query = request.GET.get('query', '')  
    juegos = []

    if query:
        url = f'https://www.cheapshark.com/api/1.0/games?title={query}'
        response = requests.get(url)
        if response.status_code == 200:
            juegos = response.json() 

    return render(request, 'buscar_juegos.html', {'juegos': juegos, 'query': query})

#Trivia API
def trivia_videojuegos(request):
    url = 'https://opentdb.com/api.php?amount=10&category=15'
    response = requests.get(url)
    data = response.json()
    preguntas = data['results']
    return render(request, 'trivia.html', {'preguntas': preguntas})

# Crear APIS
@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_juegos(request):
    juegos = Juego.objects.all()
    serializer = JuegoSerializer(juegos, many=True) 
    return Response(serializer.data)  

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_nombre_region(request):
    regiones = NombreRegion.objects.all()
    serializer = NombreRegionSerializer(regiones, many=True) 
    return Response(serializer.data)