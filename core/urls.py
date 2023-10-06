from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ejeapp/',include('ejeapp.urls')),
    path("api/token",TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path("api/token/refresh",TokenRefreshView.as_view(),name="token_refresh"),
]

schema_view = get_schema_view(
    openapi.Info(
        title="EjeApp API",
        default_version="v1",
        description="API para el manejo de Correspondencia",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alanvba@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^apidoc/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="redoc-ui",
        ),
    ]