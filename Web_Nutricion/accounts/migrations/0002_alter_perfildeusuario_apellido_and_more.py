# Generated by Django 4.0.4 on 2022-07-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfildeusuario',
            name='apellido',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perfildeusuario',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
