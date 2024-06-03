from django.test.client import Client
from pytest_django.asserts import assertTemplateUsed
import pytest
from datetime import date, timedelta
from reserva.models import Reserva

@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client: Client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')


@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client: Client):
    amanha = date.today() + timedelta(days=5)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'O tom esta bem fedorento.'
    }
    response = client.post('/reserva/criar/', dados)
    
    assert response.status_code == 200
    assert 'Reserva realizada com sucesso' in str(response.content)

@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client: Client):
    amanha = date.today() + timedelta(days=5)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 1,
        'observacoes': 'O tom esta bem fedorento.'
    }
    varialvel = client.post('/reserva/criar/', dados)
    print (varialvel.content)


    assert Reserva.objects.all().count() == 1

    reserCriada = Reserva.objects.first()
    assert reserCriada.nome_pet == 'Tom'
