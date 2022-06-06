from django.urls import path
from app_nutricion.views import listar_clientes, evaluacion_antropometrica

urlpatterns = [
    path('',listar_clientes, name='lista_clientes'),
    path("", evaluacion_antropometrica, name="evaluacion_antropometrica"),
]
