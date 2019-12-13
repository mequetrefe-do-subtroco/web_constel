# Generated by Django 2.2.7 on 2019-12-13 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data de cadastro')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='ferramentas_cadastradas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FerramentaSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, null=True, verbose_name='Quantidade')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data de saída')),
                ('observacao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observação')),
                ('ferramenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saidas', to='ferramenta.Ferramenta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saidas', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='retiradas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FerramentaQuantidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0, editable=False, verbose_name='Quantidade')),
                ('ferramenta', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='quantidade', to='ferramenta.Ferramenta')),
            ],
        ),
        migrations.CreateModel(
            name='FerramentaEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, null=True, verbose_name='Quantidade')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data de entrada')),
                ('valor', models.FloatField(default=0, verbose_name='Valor total')),
                ('observacao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observação')),
                ('ferramenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='ferramenta.Ferramenta')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='ferramentas_entradas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
