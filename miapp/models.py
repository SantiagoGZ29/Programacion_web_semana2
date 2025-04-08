from django.db import models

# Create your models here.
class estudiante(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellidop = models.CharField(max_length=100)
    apellidom = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.apellidop}) - {self.correo}"