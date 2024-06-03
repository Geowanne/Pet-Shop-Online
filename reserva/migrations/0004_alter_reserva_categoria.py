# Generated by Django 4.2.5 on 2024-01-11 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0003_categoria_reserva_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='reserva.categoria'),
        ),
    ]
