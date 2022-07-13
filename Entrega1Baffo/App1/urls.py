from django.urls import path 
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('socios/', socios, name='socios'),
    path('personal/', personal, name='personal'),
    path('actividades/', actividades, name='actividades'),
    
]