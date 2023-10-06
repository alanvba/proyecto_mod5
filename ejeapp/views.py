from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import tipo_hoja_ruta
from .models import hoja_ruta
from .models import usuario
from .serializers import TipoHojaRutaSerializer
from .serializers import HojaRutaSerializer
from .serializers import UsuarioSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return HttpResponse("Holaa modulo 5")

def tipohojaruta(request):
    tipos = tipo_hoja_ruta.objects.all()
    return render(request,"tipohojaruta.html",{
        "tipos":tipos,
        "titulo":"...::Listado tipos de hojas de rutas::..."
    })

@permission_classes([IsAuthenticated])
class TipoHojaRutaViewSet(viewsets.ModelViewSet):
    queryset = tipo_hoja_ruta.objects.all()
    serializer_class = TipoHojaRutaSerializer

@permission_classes([IsAuthenticated])
class HojaRutaViewSet(viewsets.ModelViewSet):
    queryset = hoja_ruta.objects.all()
    serializer_class = HojaRutaSerializer

@permission_classes([IsAuthenticated])
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer

@permission_classes([IsAuthenticated])
class UsuarioCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def tipohoja_ruta_count(request):
    """
    Cantidad de registros en la tabla tipo de hoja de ruta
    """
    try:
        cantidad = tipo_hoja_ruta.objects.count()
        return JsonResponse(
            {"cantidad": cantidad},
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, safe=False, status=500)