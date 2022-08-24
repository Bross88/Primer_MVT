from django.db import models

class Familiar(models.Model):                              
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    empleado = models.BooleanField()
    edad = models.IntegerField()
    fecha = models.DateField()
