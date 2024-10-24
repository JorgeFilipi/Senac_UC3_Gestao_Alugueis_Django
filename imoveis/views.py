from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from imoveis.forms import ImovelForm
from imoveis.models import Imovel, Inquilino


def index(request):
    return render(request, 'imoveis/index.html')

def list_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imoveis/list_imoveis.html', {'imoveis':imoveis})

@login_required
def list_inquilinos(request):
    inquilinos = Inquilino.objects.all()
    return render(request, 'imoveis/list_inquilinos.html', {'inquilinos':inquilinos})

@login_required
def editar_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)

    if request.method == 'POST':
        form = ImovelForm(request.POST, InstanceCheckMeta=imovel)
        form.save()
        return redirect('lista_imoveis')
    else:
        form = ImovelForm(instance=imovel)

    return render_template(request, 'imoveis/editar_imovel.html', {'form':form})

@login_required
def excluir_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)

    if request.methid ==  'POST':
        imovel.delete()
        return redirect('list_imoveis')

    return render(request, 'imoveis/excluir_imovel.html', {'imovel':imovel})


def user_login(request):

    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'imoveis/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))