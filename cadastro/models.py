from django.db import models


class Cadastro(models.Model):

    TIPO_CADASTRO = [
        ('CLIENTE', 'Cliente'),
        ('FORNECEDOR', 'Fornecedor'),
    ]

    TIPO_PESSOA = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    tipo_cadastro = models.CharField(
        max_length=20,
        choices=TIPO_CADASTRO
    )

    tipo_pessoa = models.CharField(
        max_length=2,
        choices=TIPO_PESSOA
    )

    nome = models.CharField(max_length=100)

    email = models.EmailField()

    telefone = models.CharField(max_length=20)

    endereco = models.CharField(max_length=200)

    cpf = models.CharField(
        max_length=14,
        blank=True,
        null=True
    )

    cnpj = models.CharField(
        max_length=18,
        blank=True,
        null=True
    )

    data_nascimento = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome