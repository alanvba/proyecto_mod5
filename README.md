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

## documentacion de los endpoint generados por swaggs
puede acceder a la documentacion por siguiente link;
http://localhost:8000/apidoc/

ademas se incluye las pruebas realizadas a los endpoint en postman
modulo5.postman_collection.json 

## seguridad
todos los endpoint estab con jwt