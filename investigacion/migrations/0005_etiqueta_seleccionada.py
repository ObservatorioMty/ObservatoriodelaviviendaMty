# Generated by Django 4.2.5 on 2023-10-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigacion', '0004_investigation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='etiqueta',
            name='seleccionada',
            field=models.BooleanField(default=False),
        ),
    ]
