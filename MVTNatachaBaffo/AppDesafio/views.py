import imp
from django.http import HttpResponse
from django.shortcuts import render
from models import Familiar
from django.http import HttpResponse
from django.template import Context, Template
from AppDesafio.models import Familiar

# Create your views here.
def familiar(self):
    familiar= Familiar(nombre="Malena", edad=23, fecha_nac='%d26-%m02-%y99') 
    familiar.save()
    texto= f'Nombre: {familiar.nombre} Edad: {familiar.edad} Fecha de Nacimiento: {familiar.fecha_nac}'

    return HttpResponse(texto)

def usotemplate (self):
    miArchivo=open("C:/Natacha/Cursos y capacitaciones/Python-CoderHouse/RepoDjango/MVTNatachaBaffo/Plantillas/template.html")
    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto=Context()
    documento=plantilla.render(contexto)

    return HttpResponse(documento)