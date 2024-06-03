from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm
from base.models import Contato

# inicio
def inicio(request):
    return render(request, 'inicio.html')

# Contato
def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(42) 99937-1559',
        'responsavel': 'Geovane joanico',
        'form': form,
        'sucesso': sucesso
    }
    
    return render(request, 'contato.html', contexto)

# Reserva
def reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }

    return render(request, 'reserva.html', contexto)

