# Generated by Django 3.0.7 on 2020-06-10 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cont', '0002_tabelateste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ontdefeito',
            name='ont',
        ),
        migrations.RemoveField(
            model_name='ontdefeito',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ontdefeitodevolucao',
            name='defeito',
        ),
        migrations.RemoveField(
            model_name='ontdefeitodevolucao',
            name='fornecedor',
        ),
        migrations.RemoveField(
            model_name='ontdefeitodevolucao',
            name='ont',
        ),
        migrations.RemoveField(
            model_name='ontdefeitodevolucao',
            name='ordem',
        ),
        migrations.RemoveField(
            model_name='ontdefeitodevolucao',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ontdefeitohistorico',
            name='ont',
        ),
        migrations.RemoveField(
            model_name='ontdefeitohistorico',
            name='user',
        ),
        migrations.DeleteModel(
            name='TabelaTeste',
        ),
        migrations.DeleteModel(
            name='OntDefeito',
        ),
        migrations.DeleteModel(
            name='OntDefeitoDevolucao',
        ),
        migrations.DeleteModel(
            name='OntDefeitoHistorico',
        ),
    ]
