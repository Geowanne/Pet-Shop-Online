from django.contrib import admin
from django.contrib import messages

from base.models import Contato

@admin.action(description='Marcar Formulario(s) de Contato como lido(s)')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulario(s) de Contato(s) marcado(s) como lido(s)', messages.SUCCESS)


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'lido', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido]


