from django.db import models


class Cadastro(models.Model):

    TIPO_CADASTRO = [
        ('CLIENTE', 'Cliente'),
        ('FORNECEDOR', 'Fornecedor'),
        ('FUNCIONARIO', 'Funcionário'),
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

    nome = models.CharField(
    max_length=100,
    blank=True,
    null=True
)

    razao_social = models.CharField(
    max_length=200,
    blank=True,
    null=True
)

    nome_fantasia = models.CharField(
    max_length=200,
    blank=True,
    null=True
)

    email = models.EmailField()

    telefone = models.CharField(max_length=20)

    logradouro = models.CharField(max_length=200)

    bairro = models.CharField(max_length=100)

    cidade = models.CharField(max_length=100)

    estado = models.CharField(max_length=2)

    cep = models.CharField(
    max_length=9,
    blank=True,
    null=True
)

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

    # Campos específicos para funcionários

    cargo = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    salario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    data_admissao = models.DateField(
        blank=True,
        null=True
    )

    matricula = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome