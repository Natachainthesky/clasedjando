from email.policy import HTTP
from django.http import HttpResponse
import datetime 
from django.template import Context, Template, loader

nom="Natacha"
ap="Baffo"
lista_de_notas= [3, 8 ,6]
diccionario={'nombre':nom, 'apellido':ap, 'lista':lista_de_notas}

def saludar(request):
    return HttpResponse("hola mundo asdf!")

def segunda_vista(request):
    return HttpResponse("segunda vista")

def dia_de_hoy(request):

    dia=datetime.datetime.today()
    cadena= "Hoy es: " +str(dia)
    return HttpResponse(cadena)

def saludo_nombre(self,nombre):
    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"<h1>")

def probandoHtml(self):
  #  miArchivo=open("C:/Natacha/Cursos y capacitaciones/Python-CoderHouse/RepoDjango/Proyecto1/Proyecto1/test.html")
    #miArchivo=open("C:/Natacha/Cursos y capacitaciones/Python-CoderHouse/RepoDjango/Proyecto1/Plantillas/template1.html")
    #con esta no sé porqué no anda

   # plantilla=Template(miArchivo.read())#Leemos el archivo y lo guardamos en una variable
   # miArchivo.close()

   plantilla=loader.get_template('template1.html')

   #contexto=Context() #Creamos un contexto vacío
    
   documento=plantilla.render(diccionario)
    
   return HttpResponse(documento)


