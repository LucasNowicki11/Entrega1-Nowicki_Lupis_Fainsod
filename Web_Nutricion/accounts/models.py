from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class perfilDeUsuario(models.Model):
    user = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, null=True)
    imagen = models.ImageField('Avatar', upload_to='user', null=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    web = models.URLField()
