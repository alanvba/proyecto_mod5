from rest_framework import serializers
from .models import tipo_hoja_ruta
from .models import hoja_ruta
from .models import usuario

class TipoHojaRutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_hoja_ruta
        fields = "__all__"

class HojaRutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = hoja_ruta
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = "__all__"