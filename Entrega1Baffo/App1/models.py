from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    numero_socio=models.IntegerField()
    email=models.EmailField()

class Personal(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    cargo= models.CharField(max_length=50)
    

class Actividad(models.Model):
    nombre= models.CharField(max_length=50)
    encargado= models.CharField(max_length=50)
    cant_inscriptos= models.IntegerField()

