from rest_framework import serializers
from miapp.models import Juego,NombreRegion

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['nombre', 'categoria', 'precio', 'descripcion', 'imagen']

class NombreRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NombreRegion
        fields = ['nombre_region']