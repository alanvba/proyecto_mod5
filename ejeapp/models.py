from django.db import models
from .validators import validar_tipo_hoja_ruta
from .validators import validar_numero_hoja_ruta

class tipo_hoja_ruta(models.Model):
    descripcion = models.CharField(max_length=500,unique=False,validators=[validar_tipo_hoja_ruta])
    estado = models.BooleanField(blank=True, default=True)

class hoja_ruta(models.Model):
    numero = models.IntegerField(validators=[validar_numero_hoja_ruta])
    remitente = models.CharField(max_length=500,unique=False)
    referencia = models.CharField(max_length=500,unique=False)
    prioritario = models.BooleanField(blank=True, default=False)
    tipohoja_ruta = models.ForeignKey(tipo_hoja_ruta, on_delete=models.CASCADE)
    fechahora = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class usuario(models.Model):
    usuario = models.CharField(max_length=500,unique=False)
    passwords = models.CharField(max_length=500,unique=False)
    nombres = models.CharField(max_length=500,unique=False)
    apellidos = models.CharField(max_length=500,unique=False)
    estado = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class RemisionEstado(models.TextChoices):
    ENVIADO = 'ev', 'Enviado'
    PENDIENTE = 'pd', 'Pendiente'
    RECIBIDO = 're', 'Recibido'

class remision(models.Model):
    hoja_ruta = models.ForeignKey(hoja_ruta, on_delete=models.CASCADE)
    idusuario_origen = models.IntegerField()
    idusuario_destino = models.IntegerField()
    estado = models.CharField(
        max_length=2,
        choices=RemisionEstado.choices,
        default=RemisionEstado.ENVIADO
    )
    habilitado = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class seguimiento_remision(models.Model):
    remision = models.ForeignKey(remision, on_delete=models.CASCADE)
    idusuario_origen = models.IntegerField()
    idusuario_destino = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)