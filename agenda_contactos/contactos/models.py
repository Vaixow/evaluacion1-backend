from django.db import models

class Contacto(models.Model): ##creamos el modelo del formato para el futuro formulario
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"