from django.db import models

# Create your models here.

class Clientes(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    age = models.IntegerField()
    sexo = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Evaluacion_Antropometrica(models.Model):
    name_evaluacion = models.CharField(max_length=50)
    age = models.IntegerField()
    size = models.FloatField()
    weight = models.FloatField()
    bodyfat = models.FloatField()
    musclemass = models.FloatField()
    IMC = models.FloatField()

    class Meta: 
        verbose_name = "Evaluacion Antropometrica"
        verbose_name_plural = "Evaluaciones"