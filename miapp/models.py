from django.db import models

class RolUsuario(models.Model):
    rol_usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.rol_usuario 

class GeneroUsuario(models.Model):
    genero_usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.genero_usuario 

class NombreRegion(models.Model):
    nombre_region = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_region



class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)

    # Relaciones con otras tablas
    rol = models.ForeignKey(RolUsuario, on_delete=models.CASCADE, null=True, blank=True)
    genero = models.ForeignKey(GeneroUsuario, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(NombreRegion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.usuario}) - {self.correo}"
