from django.shortcuts import render
from app_nutricion.models import Clientes, Evaluacion_Antropometrica
# Create your views here.


def listar_clientes(request):
    lista_clientes = Clientes.objects.all()
    context = {'lista_clientes': lista_clientes}
    return render(request, 'lista_clientes.html', context=context)
    