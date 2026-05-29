from django.db import models

# Create your models here.

#Criando a tabela de clientes com os referentes campos.
#O campo cpf é único para evitar duplicidade de clientes.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    
    def __str__(self):
        return self.nome