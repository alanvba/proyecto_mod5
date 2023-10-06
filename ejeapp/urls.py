from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"tipohojaruta", views.TipoHojaRutaViewSet)
router.register(r"hojaruta", views.HojaRutaViewSet)
router.register(r"usuario", views.UsuarioViewSet)

urlpatterns = [
    path("templates/",views.tipohojaruta,name="tipohojaruta"),
    #path("",views.index,name="index")
    path("",include(router.urls)),
]