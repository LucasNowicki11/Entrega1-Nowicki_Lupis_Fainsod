# Generated by Django 4.0.4 on 2022-07-03 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_nutricion', '0011_avatar_imagen2_avatar_imagen3_avatar_imagen4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='imagen2',
        ),
        migrations.RemoveField(
            model_name='avatar',
            name='imagen3',
        ),
        migrations.RemoveField(
            model_name='avatar',
            name='imagen4',
        ),
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
    ]
