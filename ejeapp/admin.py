from django.contrib import admin
from .models import hoja_ruta
from .models import usuario
from .models import remision
from .models import tipo_hoja_ruta

class HojaRutaAdmin(admin.ModelAdmin):
    list_display = ('numero','remitente','referencia','tipohoja_ruta','created')
admin.site.register(hoja_ruta,HojaRutaAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','usuario','created','estado')
admin.site.register(usuario,UsuarioAdmin)

class RemisionAdmin(admin.ModelAdmin):
    list_display = ('hoja_ruta','idusuario_origen','idusuario_destino','estado','created')
admin.site.register(remision,RemisionAdmin)

class TipoHojaRutaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','estado')
admin.site.register(tipo_hoja_ruta,TipoHojaRutaAdmin)
