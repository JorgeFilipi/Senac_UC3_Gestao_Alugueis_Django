from  django import forms
from .models import Imovel

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