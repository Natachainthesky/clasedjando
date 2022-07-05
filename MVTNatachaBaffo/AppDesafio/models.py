from django.db import models

# Create your models here.

class Familiar (models.Model):
    nombre=models.CharField()
    edad=models.IntegerField()
    fecha_nac=models.DateField()
    
