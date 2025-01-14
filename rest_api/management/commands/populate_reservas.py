from typing import Any
from django.core.management.base import BaseCommand
from model_bakery import baker

from reserva.models import Reserva


class Command(BaseCommand):
    help = 'Criar dados fake para testar API de agendamento'

    def handle(self, *args: Any, **options: Any):
        total = 50
        self.stdout.write(
            self.style.WARNING(f'Criando {total} agendamentos')
        )
        for i in range(total):
            reserva = baker.make(Reserva)
            reserva.save()
        
        self.stdout.write(
            self.style.SUCCESS('Agendamentos criados')
        )