"""
URL configuration for levelup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('categorias/', views.categorias, name='categorias'),
    path('accion/', views.accion, name='accion'),
    path('carrito/', views.carrito, name='carrito'),
    path('deporte/', views.deporte, name='deporte'),
    path('aventura/', views.aventura, name='aventura'),
    path('terror/', views.terror, name='terror'),
    path('estrategia/', views.estrategia, name='estrategia'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('recuperar_contraseña/', views.recuperar_contraseña, name='recuperar_contraseña'),
    path('contraseña/', views.contraseña, name='contraseña'),
    path('formulario/', views.formulario, name='formulario'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admininicio/', views.admininicio, name='admininicio'),
    path('blog_forest/', views.blog_forest, name='blog_forest'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_forest2/', views.blog_forest2, name='blog_forest2'),
]
