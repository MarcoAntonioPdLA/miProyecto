from django.db import models

# Create your models here.
class Persona(models.Model):
  nombres = models.CharField(max_length = 100)
  apellidos = models.CharField(max_length = 100)
  edad = models.IntegerField()
  donador = models.BooleanField()

  def __str__(self):
    return f'{self.apellidos}, {self.nombres}'

