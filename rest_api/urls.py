from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import AgendamentoModelViewSet, hello_world, PetshopModelViewSet, CategoriaModelViewSet
from rest_api.views import ContatoModelViewSet, contato_api

app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet, 'reserva')
router.register('contatos', ContatoModelViewSet) #teste
router.register('petshop', PetshopModelViewSet)
router.register('categoria', CategoriaModelViewSet)


urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api',),
    path('contato_api', contato_api, name='contata_ap_api',)
]

urlpatterns += router.urls