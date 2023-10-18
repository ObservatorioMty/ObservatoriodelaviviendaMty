# Generated by Django 4.2.5 on 2023-09-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntroViviendaMty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='intro')),
            ],
        ),
        migrations.CreateModel(
            name='Metodologic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodologic', models.TextField(blank=True, null=True, verbose_name='Metodo')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.TextField(blank=True, null=True, verbose_name='quienes somos')),
                ('image', models.ImageField(blank=True, null=True, upload_to='inv', verbose_name='galeria')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='inv', verbose_name='galeria')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='inv', verbose_name='galeria')),
            ],
        ),
    ]
