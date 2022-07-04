from django.contrib import admin
from app_nutricion.models import Clientes, Evaluacion_Antropometrica, Recetas, Avatar
# Register your models here.

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "sexo" , "age"]

@admin.register(Evaluacion_Antropometrica)
class Evaluacion_AntropometricaAdmin(admin.ModelAdmin):
    list_display = ["name_evaluacion", "age", "size", "IMC"]

@admin.register(Recetas)
class RecetasAdmin(admin.ModelAdmin):
    list_display = ["recipe_name", "ingredients", "number_of_grams"]
