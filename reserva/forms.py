from datetime import date
from django import forms
from reserva.models import Reserva


class ReservaForm(forms.ModelForm):
    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possível realizar uma reserva para o passado!')
        
        quntidadeAtualdereservas = Reserva.objects.filter(data=data).count()

        if quntidadeAtualdereservas >= 4:
            raise forms.ValidationError('Já existem muitas reservas para este dia, por favor escolha outra data')

        return data
    


    class Meta:
        model = Reserva
        fields = [
            'nome', 'categoria', 'email', 'nome_pet', 'data', 'turno', 'tamanho', 'petshop',  'observacoes'
        ]