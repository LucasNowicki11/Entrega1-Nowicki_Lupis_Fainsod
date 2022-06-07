from django.urls import path
from app_nutricion.views import listar_clientes, evaluacion_antropometrica, cargar_clientes, recetas

urlpatterns = [
    path('',listar_clientes, name='lista_clientes'),
    path('evaluacion/', evaluacion_antropometrica, name="evaluacion_antropometrica"),
    path('cargar-clientes/', cargar_clientes, name='cargar_clientes'),
    path('recetas/', recetas, name='recetas'),
]
