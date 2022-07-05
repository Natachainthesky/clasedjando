import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from AppDesafio.models import Familiar
from datetime import datetime

# Create your views here.
def familiar(self):
    familiar= Familiar(nombre="Malena", edad=23, fecha_nac=datetime(1999,2,26)) 
    familiar.save()
    
    miArchivo=open("C:/Natacha/Cursos y capacitaciones/Python-CoderHouse/RepoDjango/MVTNatachaBaffo/Plantillas/template.html")
    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto=Context({'nombre':familiar.nombre, 'edad': familiar.edad, 'fecha_nac': familiar.fecha_nac})
    documento=plantilla.render(contexto)

    return HttpResponse(documento)