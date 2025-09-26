from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Swagger/OpenAPI schema
schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de IGVA Veterinaria",
        default_version='v1',
        description="Listado de endpoints disponibles",
        terms_of_service="https://www.IGVAveterinaria.com.ar",
        contact=openapi.Contact(email="veterinariaigva@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', lambda request: redirect('admin/')),  # Redirigir '/' a admin
    path('admin/', admin.site.urls),

    # APIs
    path('api/v1/user/', include('User.urls')),    
    # path('api/v1/pet/', include('Pet.urls')),  # Descomentar cuando Pet.urls exista

    # JWT Auth
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger / Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
