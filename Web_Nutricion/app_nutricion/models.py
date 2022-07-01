from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models



# Create your models here.

class Clientes(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    age = models.IntegerField()
    sexo = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to = "clientes", blank=True, null=True)



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

class Recetas(models.Model):
    recipe_name = models.CharField(max_length=40)
    ingredients = models.CharField(max_length=200)
    number_of_grams = models.FloatField()
    amount_of_cholesterol = models.FloatField()
    vitamins = models.CharField(max_length=300)
    image = models.ImageField(upload_to = "recetas", blank=True, null=True)
    
    class Meta: 
        verbose_name = "Recetas Saludables"
        verbose_name_plural = "Recetas"