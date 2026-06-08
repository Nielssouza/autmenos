from django.urls import path
from .views import (
    login_view,
    logout_view,
    cadastro_publico,
    cadastro_admin,
    excluir_cadastro,
    editar_cadastro
)

app_name = 'cadastro'

urlpatterns = urlpatterns = [
    path('', cadastro_publico, name='publico'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('admin/', cadastro_admin, name='admin'),
    path('cadastro/admin/excluir/<int:id>/', excluir_cadastro, name='excluir_cadastro'),
    path('cadastro/admin/editar/<int:id>/', editar_cadastro, name='editar_cadastro'),
]