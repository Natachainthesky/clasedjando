
from django.urls import path
from AppDesafio.views import familiar


urlpatterns = [
    path('familiar/', familiar),
  
]