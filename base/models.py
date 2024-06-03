from django.db import models

# Modelo de Formulário para contato
class Contato(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='E-mail', max_length=75)
    mensagem = models.TextField(verbose_name='Mensagem')
    data = models.DateField(verbose_name='Data do Envio', auto_now_add=True)
    lido = models.BooleanField(verbose_name='Lido', default=False, blank=True)

    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']

# Modelo de Formuláriio para Reserva
class Reserva(models.Model):
    nome_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    data = models.CharField(max_length=10)
    observacao = models.TextField()