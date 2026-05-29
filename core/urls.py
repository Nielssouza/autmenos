"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Importando as views do app de cadastros para mapear as URLs
# (Agora usamos include para delegar ao app)
# from cadastros_guilherme.views import (
#     listar_clientes, 
#     novo_cliente, 
#     editar_cliente,
#     excluir_cliente
# )

urlpatterns = [
    path('', RedirectView.as_view(url='/clientes/', permanent=False), name='home'),
    path('admin/', admin.site.urls),
    
    # Mapear a URL para o app de clientes usando include
    path('clientes/', include('cadastro.urls', namespace='clientes')),
        
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # API browsable (login/logout para o browsable API do DRF)
    path('api-auth/', include('rest_framework.urls')),
    
]
