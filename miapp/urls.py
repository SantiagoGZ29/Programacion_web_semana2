from django.urls import path
from miapp import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('carrito/', views.carrito, name='carrito'),
    path('perfil/', views.perfil, name='perfil'),
    path('contraseña/', views.contraseña, name='contraseña'),
    path('formulario/', views.formulario, name='formulario'),
    path('admininicio/', views.admininicio, name='admininicio'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_forest2/', views.blog_forest2, name='blog_forest2'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('formulario/', views.registrar_usuario, name='formulario'),
    path('login_usuario/', views.login_usuario, name='login_usuario'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('juegos/', views.juegos, name='juegos'),
    path('juegos/', views.juegos_catalogo, name='juegos_catalogo'),

    path('agregar-al-carrito/<int:juego_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<int:juego_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('eliminar_juego/<int:juego_id>/', views.eliminar_juego, name='eliminar_juego'),
    path('editar_juego/<int:juego_id>/', views.editar_juego, name='editar_juego'),
    path('trivia/', views.trivia_videojuegos, name='trivia'),
]
