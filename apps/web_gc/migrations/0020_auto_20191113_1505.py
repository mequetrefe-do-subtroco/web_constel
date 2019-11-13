# Generated by Django 2.2.7 on 2019-11-13 18:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_gc', '0019_auto_20191110_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregatalao',
            name='user_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='talao_user_to', to=settings.AUTH_USER_MODEL, verbose_name='Para'),
        ),
        migrations.AlterField(
            model_name='entregavale',
            name='user_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='vale_user_to', to=settings.AUTH_USER_MODEL, verbose_name='Para'),
        ),
        migrations.AlterField(
            model_name='talao',
            name='status',
            field=models.IntegerField(choices=[(0, 'Disponível'), (1, 'Em uso'), (2, 'Usado')], default=0),
        ),
        migrations.AlterField(
            model_name='talao',
            name='talao',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(100, 'Talão inválido'), django.core.validators.MaxValueValidator(999999, 'Talão inválido')], verbose_name='Talao'),
        ),
        migrations.AlterField(
            model_name='vale',
            name='status',
            field=models.IntegerField(choices=[(0, 'Indisponível'), (1, 'Disponível'), (2, 'Usado')], default=0),
        ),
    ]
