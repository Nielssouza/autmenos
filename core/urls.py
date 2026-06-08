"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from cadastro.views import dashboard
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
    path('', TemplateView.as_view(template_name='landing.html'), name='home'),
    path('admin/', admin.site.urls),

    path('cadastro/', include('cadastro.urls', namespace='cadastro')),
    path('dashboard/admin/', dashboard, name='dashboard'),


    

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api-auth/', include('rest_framework.urls')),
]
