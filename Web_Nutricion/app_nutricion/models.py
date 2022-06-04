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