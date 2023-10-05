from django.urls import path
from . import views

urlpatterns = [
    path("templates/",views.tipohojaruta,name="tipohojaruta"),
    path("",views.index,name="index")
]