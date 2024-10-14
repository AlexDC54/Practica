from django.urls import path
from . import views

urlpatterns = [
    path('pagina/', views.mi_imagen, name='mi_imagen'),
]