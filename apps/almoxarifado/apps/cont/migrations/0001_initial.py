# Generated by Django 3.0.7 on 2020-06-10 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('almoxarifado', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porta', models.CharField(default='vazio', max_length=255)),
                ('estado_link', models.CharField(default='vazio', max_length=255)),
                ('nivel_ont', models.FloatField(default=0)),
                ('nivel_olt', models.FloatField(default=0)),
                ('nivel_olt_tx', models.FloatField(default=0)),
                ('contrato', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('descricao', models.TextField(max_length=500)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Estoque'), (1, 'Campo'), (2, 'Aplicada'), (3, 'Defeito'), (4, 'Devolvida')], default=0, editable=False)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ont_modelo', to='cont.Modelo')),
            ],
        ),
        migrations.CreateModel(
            name='OntEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('ont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrada_ont', to='cont.Ont')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entrada_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Secao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('descricao', models.TextField(max_length=500)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OntSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('entrada', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='saida_entrada_ont', to='cont.OntEntrada')),
                ('ont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saida_ont', to='cont.Ont')),
                ('ordem', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saida_ordem_ont', to='almoxarifado.Ordem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saida_user', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saida_user_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OntEntradaHistorico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_ont', to='cont.Ont')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entrada_historico_ont', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OntAplicado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aplicado_cliente', to='cont.Cliente')),
                ('ont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aplicado_ont', to='cont.Ont')),
                ('saida', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='aplicado_saida_ont', to='cont.OntSaida')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aplicado_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ont',
            name='secao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ont_secao', to='cont.Secao'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ont',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cliente_ont', to='cont.Ont'),
        ),
    ]
