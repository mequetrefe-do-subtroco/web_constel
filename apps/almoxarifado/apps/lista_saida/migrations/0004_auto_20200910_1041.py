# Generated by Django 3.0.7 on 2020-09-10 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lista_saida', '0003_manutencaoontitem_manutencaoontlista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manutencaoontitem',
            name='lista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cont_manutencao_lista_itens', to='lista_saida.ManutencaoOntLista'),
        ),
    ]
