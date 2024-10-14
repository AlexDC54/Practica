from django.shortcuts import render

# Create your views here.
def mi_imagen(request):
    return render(request, 'imagenprueba/contenido/Templates/contenido/imagen.html')