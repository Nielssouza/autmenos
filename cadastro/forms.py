from django import forms
from validate_docbr import CPF, CNPJ

from .models import Cadastro


class ClienteForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()

        tipo_pessoa = cleaned_data.get('tipo_pessoa')
        cpf = cleaned_data.get('cpf')
        cnpj = cleaned_data.get('cnpj')

        if tipo_pessoa == 'PF':

            if not cpf:
                raise forms.ValidationError(
                    'CPF é obrigatório para Pessoa Física.'
                )

            cpf_limpo = cpf.replace('.', '').replace('-', '')

            if not CPF().validate(cpf_limpo):
                raise forms.ValidationError(
                    'CPF inválido.'
                )

        elif tipo_pessoa == 'PJ':

            if not cnpj:
                raise forms.ValidationError(
                    'CNPJ é obrigatório para Pessoa Jurídica.'
                )

            cnpj_limpo = (
                cnpj.replace('.', '')
                .replace('/', '')
                .replace('-', '')
            )

            if not CNPJ().validate(cnpj_limpo):
                raise forms.ValidationError(
                    'CNPJ inválido.'
                )

        return cleaned_data

    class Meta:
        model = Cadastro

        fields = [
            'tipo_cadastro',
            'tipo_pessoa',
            'nome',
            'razao_social',
            'nome_fantasia',
            'email',
            'telefone',
            'cep',
            'logradouro',
            'bairro',
            'cidade',
            'estado',
            'data_nascimento',
            'cpf',
            'cnpj',
            'cargo',
            'salario',
            'data_admissao',
            'matricula',
        ]

        widgets = {
            'tipo_cadastro': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'tipo_pessoa': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'nome': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),

            'telefone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'cep': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '00000-000'
            }
            ),

            'logradouro': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'bairro': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'cidade': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'maxlength': '2'
                }
            ),

            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'cpf': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'cnpj': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'cargo': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'salario': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'data_admissao': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'matricula': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'nome': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'razao_social': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'nome_fantasia': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }