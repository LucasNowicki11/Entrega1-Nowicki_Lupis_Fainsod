# Generated by Django 4.0.4 on 2022-06-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nutricion', '0002_recetas'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='clientes'),
        ),
        migrations.AddField(
            model_name='recetas',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recetas'),
        ),
    ]
