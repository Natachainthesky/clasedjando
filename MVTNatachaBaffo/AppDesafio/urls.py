
from django.urls import path
from AppDesafio.views import familiar


urlpatterns = [
    path('familiar/<str:name>/<int:age>/<int:ano>/<int:mes>/<int:dia>', familiar),
  
]