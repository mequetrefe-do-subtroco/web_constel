# Generated by Django 2.2.6 on 2019-10-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_gc', '0008_auto_20191028_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregatalao',
            name='asd',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
