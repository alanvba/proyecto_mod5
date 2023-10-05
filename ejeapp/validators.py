from django.core.exceptions import ValidationError

def validar_tipo_hoja_ruta(value):
    if value == "":
        raise ValidationError('%(value) tiene que ingresar el nombre del tipo de hoja de ruta',params={'value':value})

def validar_numero_hoja_ruta(value):
    if not value:
        raise ValidationError('%(value)s ingrese el numero de cite',params={'value':value})