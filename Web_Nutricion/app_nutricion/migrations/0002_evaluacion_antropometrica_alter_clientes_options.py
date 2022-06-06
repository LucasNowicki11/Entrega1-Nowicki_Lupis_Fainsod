# Generated by Django 4.0.4 on 2022-06-06 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nutricion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion_Antropometrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('size', models.FloatField()),
                ('weight', models.FloatField()),
                ('bodyfat', models.FloatField()),
                ('musclemass', models.FloatField()),
                ('caloricvalue', models.FloatField()),
            ],
            options={
                'verbose_name': 'Evaluacion Antropometrica',
                'verbose_name_plural': 'Evaluaciones',
            },
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]