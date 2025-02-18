from django import forms
from .models import Categoriapalavrachave, Palavrachave

class CategoriaPalavraChaveForm(forms.ModelForm):
    class Meta:
        model = Categoriapalavrachave
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da categoria'
            })
        }
        labels = {
            'nome': 'Nome da Categoria'
        }

class PalavraChaveForm(forms.ModelForm):
    class Meta:
        model = Palavrachave
        fields = ['id_cliente', 'id_categoria', 'palavra',]
        widgets = {
            'id_cliente': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Selecione o cliente'
            }),
            'id_categoria': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Selecione a categoria'
            }),
            'palavra': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a palavra-chave'
            }),
        }
        labels = {
            'id_cliente': 'Cliente',
            'id_categoria': 'Categoria',
            'palavra': 'Palavra-chave',
        }