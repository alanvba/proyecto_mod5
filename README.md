## base de datos
postgresql

## config settings.py
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "nombre_base_datos",
        "USER": "postgres",
        "PASSWORD": "contrasenia",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }

## Nota
se adjunta el archivo db.sql para insertar datos a la DB