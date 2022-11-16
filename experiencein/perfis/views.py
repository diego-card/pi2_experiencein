# editando o arquivo experiencein/perfis/views.py
from ast import If
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil, Convite
# importando redirect
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html', {'perfis' : Perfil.objects.all() , 'perfil_logado' : get_perfil_logado(request)})

def exibir(request, perfil_id):

    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_e_contato = perfil in perfil_logado.contatos.all()
    return render(request, 'perfil.html', {'perfil' : perfil, 'perfil_logado' : get_perfil_logado(request), 'ja_e_contato' : ja_e_contato})

def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)
    # ATENÇÃO, TROQUE O ID POR UM QUE ESTEJA CADASTRADO

def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')
