from django.urls import path
from app_nutricion.views import listar_clientes
urlpatterns = [
    path('',listar_clientes, name='lista_clientes')
]