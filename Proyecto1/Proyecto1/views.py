from email.policy import HTTP
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("hola mundo asdf!")