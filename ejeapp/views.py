from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .models import tipo_hoja_ruta
from .models import hoja_ruta
from .models import usuario
from .serializers import TipoHojaRutaSerializer
from .serializers import HojaRutaSerializer
from .serializers import UsuarioSerializer
# Create your views here.

def index(request):
    return HttpResponse("Holaa modulo 5")

def tipohojaruta(request):
    tipos = tipo_hoja_ruta.objects.all()
    return render(request,"tipohojaruta.html",{
        "tipos":tipos,
        "titulo":"...::Listado tipos de hojas de rutas::..."
    })

class TipoHojaRutaViewSet(viewsets.ModelViewSet):
    queryset = tipo_hoja_ruta.objects.all()
    serializer_class = TipoHojaRutaSerializer

class HojaRutaViewSet(viewsets.ModelViewSet):
    queryset = hoja_ruta.objects.all()
    serializer_class = HojaRutaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer