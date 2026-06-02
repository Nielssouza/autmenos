from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = [
            'codigo',
            'descricao',
            'grupo',
            'marca',
            'unidade',
            'valor_custo',
            'valor_venda',
            'estoque',
            'ativo',
        ]