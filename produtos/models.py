from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Tabela de Produtos
class Produto(models.Model):
    codigo = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Código'
    )
    
    descricao = models.CharField(
        max_length=200,
        verbose_name='Descrição'
    )
    
    grupo = models.CharField(
        max_length=100,
        verbose_name='Grupo'
    )
    
    marca = models.CharField(
        max_length=100,
        verbose_name='Marca'
    )
    
    unidade = models.CharField(
        max_length=10,
        verbose_name='Unidade'
    )
    
    valor_custo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Valor de Custo'
    )
    
    valor_venda = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Valor de Venda'
    )
    
    estoque = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Estoque'
    )
    
    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )
    
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'

class MovimentacaoEstoque(models.Model):
    
    TIPOS = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )
    
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE
    )
    
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS
    )
    
    quantidade = models.IntegerField()
    
    observacao = models.CharField(
        max_length=255
    )
    
    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    
class HistoricoProduto(models.Model):
    
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE
    )
    
    descricao = models.TextField()
    
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    
    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    
    @property
    def status_estoque(self):

        if self.estoque <= 5:
            return 'Baixo'

        elif self.estoque <= 10:
            return 'Atenção'

        return 'Normal'