from django.urls import path
from Web_Nutricion.app_nutricion.views import cargar_receta
from app_nutricion.views import listar_clientes, evaluacion_antropometrica, cargar_clientes, recetas, cargar_evaluacion, search_client_view

urlpatterns = [
    path('',listar_clientes, name='lista_clientes'),
    path('evaluacion/', evaluacion_antropometrica, name="evaluacion_antropometrica"),
    path('cargar-clientes/', cargar_clientes, name='cargar_clientes'),
    path('recetas/', recetas, name='recetas'),
    path('cargar-evaluacion/',cargar_evaluacion, name='cargar_evaluacion'),
    path('cargar-receta/',cargar_receta, name='cargar_receta'),
    path('search-client/', search_client_view, name='search_client')
]
