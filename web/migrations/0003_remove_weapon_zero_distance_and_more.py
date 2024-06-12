# Generated by Django 5.0.4 on 2024-04-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_ammo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='zero_distance',
        ),
        migrations.AlterField(
            model_name='weapon',
            name='sight_height',
            field=models.FloatField(help_text='Height of the sight above the bore axis (centimeters)'),
        ),
    ]
