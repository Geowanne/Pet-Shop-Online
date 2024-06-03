from django import forms
from base.models import Contato, Reserva


# Formulario de Contato
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

# Formulario Reserva de banho 
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome_pet', 'telefone', 'data', 'observacao']