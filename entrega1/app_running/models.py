from datetime import datetime
from django.db import models
from django.forms import DateField, EmailField

# Create your models here.
class Corredor (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    modalidad = models.CharField(max_length=10)
    email = models.EmailField()
    team = models.CharField(max_length=10)

class Carreras (models.Model):
    nombre = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=10)
    distancia= models.IntegerField()
    fecha = models.DateField()

class Teams (models.Model):
    nombre = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=10)
    email = models.EmailField()

# Create your models here.
