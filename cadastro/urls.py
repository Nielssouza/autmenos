from django.urls import path
from .views import listar_clientes, novo_cliente, editar_cliente, excluir_cliente

app_name = 'clientes'

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('novo/', novo_cliente, name='novo_cliente'),
    path('<int:id>/editar/', editar_cliente, name='editar_cliente'),
    path('<int:id>/excluir/', excluir_cliente, name='excluir_cliente'),
]
