# Generated by Django 4.2.5 on 2023-11-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_remove_team_image1_remove_team_image2_team_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
    ]
