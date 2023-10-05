from django.shortcuts import render
from django.http import HttpResponse
from .models import tipo_hoja_ruta
# Create your views here.

def index(request):
    return HttpResponse("Holaa modulo 5")

def tipohojaruta(request):
    tipos = tipo_hoja_ruta.objects.all()
    return render(request,"tipohojaruta.html",{
        "tipos":tipos,
        "titulo":"...::Listado tipos de hojas de rutas::..."
    })
