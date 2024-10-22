from django.shortcuts import render
from imoveis.models import Imovel, Inquilino

def index(request):
    return render(request, 'imoveis/index.html')

def list_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imoveis/list_imoveis.html', {'imoveis':imoveis})

def list_inquilinos(request):
    inquilinos = Inquilino.objects.all()
    return render(request, 'imoveis/list_inquilinos.html', {'inquilinos':inquilinos})
