from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def categorias(request):
    return render(request, 'categorias.html')

def accion(request):
    return render(request, 'accion.html')

def carrito(request):
    return render(request, 'carrito.html')

def deporte(request):
    return render(request, 'deporte.html')

def aventura(request):
    return render(request, 'aventura.html')

def terror(request):
    return render(request, 'terror.html')

def estrategia(request):
    return render(request, 'estrategia.html')

def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')

def contraseña(request):
    return render(request, 'contraseña.html')

def recuperar_contraseña(request):
    return render(request, 'recuperar_contraseña.html')

def formulario(request):
    return render(request, 'formulario.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')


def admininicio(request):
    return render(request, 'admininicio.html')

def blog_forest(request):
    return render(request, 'blog_forest.html')

def blogs(request):
    return render(request, 'blogs.html') 

def blog_forest2(request):
    return render(request, 'blog_forest2.html')   