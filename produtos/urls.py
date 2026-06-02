from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    #Criar rota para criar um novo produto
    path('novo/',
         views.produto_novo,
         name='produto_novo'
         ),
    
    #Listar os produtos
    path('',
         views.produto_lista,
         name='produto_lista'
         ),
    
    #Editar um produto
    path('editar/<int:pk>/',
         views.produto_editar,
         name='produto_editar'
          ),
    
    #Deletar um produto
     path('excluir/<int:pk>/',
          views.produto_excluir,
          name='produto_excluir'
          ),
]