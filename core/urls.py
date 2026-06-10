"""
URL configuration for core project.
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

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='home'),

    path('admin/', admin.site.urls),

    # Apps
    path('cadastro/', include('cadastro.urls', namespace='cadastro')),
    path('ajuda/', include('ajuda.urls')),
    path('produtos/', include('produtos.urls', namespace='produtos')),

    # Dashboard
    path('dashboard/admin/', dashboard, name='dashboard'),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # DRF
    path('api-auth/', include('rest_framework.urls')),
]