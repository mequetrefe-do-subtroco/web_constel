# Generated by Django 2.2.7 on 2019-12-13 16:27

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
            name='Patrimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data de entrada')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='patrimonios_cadastrados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatrimonioEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0, unique=True, verbose_name='Código')),
                ('observacao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observação')),
                ('valor', models.FloatField(default=0)),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data de entrada')),
                ('patrimonio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patrimonio_entrada', to='patrimonio1.Patrimonio')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='entrada_patrimonio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatrimonioSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observação')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data de saída')),
                ('entrada', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='entrada_saida', to='patrimonio1.PatrimonioEntrada')),
                ('patrimonio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patrimonio_saida', to='patrimonio1.Patrimonio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patrimonio_saidas', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patrimonio_retiradas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
