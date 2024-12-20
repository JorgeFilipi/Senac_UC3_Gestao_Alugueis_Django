from  django import forms
from .models import Imovel, Inquilino

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['endereco', 'cidade', 'preco_aluguel', 'descricao']
        widgest = {
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o endereço'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o estado'}),
            'preco_aluguel': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite uma descrição do imóvel (opcional)', 'rows': 3, 'maxlength':150})
        }

    def clean_preco_aluguel(self):
        preco_aluguel = self.cleaned_data['preco_aluguel']
        if preco_aluguel <= 0:
            raise forms.ValidationError("O preço de aluguel deve ser um valor positivo")
            return preco_aluguel
class InquilinoForm(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = ['nome', 'telefone', 'email', 'imovel']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o e-mail'}),
            'cidade': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escolha o imóvel'}),
        }