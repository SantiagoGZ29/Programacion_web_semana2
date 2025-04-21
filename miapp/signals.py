from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import RolUsuario, GeneroUsuario, NombreRegion, Categoria, Juego
from django.conf import settings
import os

@receiver(post_migrate)
def insertar_datos_iniciales(sender, **kwargs):
    print("Cargando datos iniciales...")  # Para verificar si se ejecuta el signal

    roles = ['administrador', 'usuario']
    generos = ['masculino', 'femenino', 'otro']
    regiones = [
        'Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama',
        'Coquimbo', 'Valparaíso', 'Metropolitana', 'O’Higgins',
        'Maule', 'Ñuble', 'Biobío', 'La Araucanía', 'Los Ríos',
        'Los Lagos', 'Aysén', 'Magallanes'
    ]
    categorias = ['Acción', 'Deporte', 'Aventura', 'Terror', 'Estrategia']

    # Insertar roles
    for nombre in roles:
        RolUsuario.objects.get_or_create(rol_usuario=nombre)

    # Insertar géneros
    for nombre in generos:
        GeneroUsuario.objects.get_or_create(genero_usuario=nombre)

    # Insertar regiones
    for nombre in regiones:
        NombreRegion.objects.get_or_create(nombre_region=nombre)

    # Insertar categorías
    for nombre in categorias:
        Categoria.objects.get_or_create(categoria=nombre)

    # Insertar juegos con las imágenes correctas
    juegos = [
        {"nombre": "Call of Duty", "categoria": "Acción", "precio": 39990, "descripcion": "Un juego de disparos en primera persona, con modos multijugador y campaña.", "imagen": "call_of_duty.jpg"},
        {"nombre": "GTA V", "categoria": "Acción", "precio": 29990, "descripcion": "Juego de mundo abierto con acción, crimen y aventura.", "imagen": "gta_v.jpg"},
        {"nombre": "FIFA 25", "categoria": "Deporte", "precio": 39990, "descripcion": "Simulador de fútbol con licencias oficiales y modos de juego realistas.", "imagen": "fifa_25.jpg"},
        {"nombre": "NBA 24", "categoria": "Deporte", "precio": 39990, "descripcion": "Simulador de baloncesto con equipos y jugadores actuales.", "imagen": "nba_24.jpg"},
        {"nombre": "The Legend of Zelda", "categoria": "Aventura", "precio": 49990, "descripcion": "Juego de aventuras en un mundo fantástico con puzzles y acción.", "imagen": "the_legend_of_zelda.jpg"},
        {"nombre": "Uncharted 5", "categoria": "Aventura", "precio": 49990, "descripcion": "Juego de acción y aventura con exploración y acción trepidante.", "imagen": "uncharted_5.jpg"},
        {"nombre": "The Callisto Protocol", "categoria": "Terror", "precio": 39990, "descripcion": "Juego de terror y supervivencia en una estación espacial.", "imagen": "The_callisto_protocol.jpg"},
        {"nombre": "Resident Evil 4", "categoria": "Terror", "precio": 29990, "descripcion": "Remake del clásico juego de terror con elementos de supervivencia.", "imagen": "resident_evil_4.jpg"},
        {"nombre": "Age of Empires", "categoria": "Estrategia", "precio": 29990, "descripcion": "Juego de estrategia en tiempo real en el que los jugadores gestionan civilizaciones.", "imagen": "age_of_empires.jpg"},
        {"nombre": "Total War", "categoria": "Estrategia", "precio": 39990, "descripcion": "Juego de estrategia en tiempo real con batallas masivas en tiempo real.", "imagen": "total_war.jpg"},
    ]

    for juego_data in juegos:
        categoria = Categoria.objects.get(categoria=juego_data["categoria"])  # Buscar la categoría por nombre
        imagen_path = os.path.join('juegos', juego_data["imagen"])  # Crear la ruta correcta de la imagen
        Juego.objects.get_or_create(
            nombre=juego_data["nombre"],
            categoria=categoria,
            precio=juego_data["precio"],
            descripcion=juego_data["descripcion"],
            imagen=imagen_path  # Guardar la ruta correcta de la imagen
        )

    print("Datos iniciales cargados con éxito.")  # Para confirmar que los datos se han insertado correctamente
