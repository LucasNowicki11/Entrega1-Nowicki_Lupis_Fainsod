from django.shortcuts import render
from app_nutricion.models import Clientes, Evaluacion_Antropometrica
# Create your views here.


def listar_clientes(request):
    lista_clientes = Clientes.objects.all()
    context = {'lista_clientes': lista_clientes}
    return render(request, 'lista_clientes.html', context=context)

def evaluacion_antropometrica(request):
    evaluacion_antropometrica = Evaluacion_Antropometrica.objects.all()
    context = {"evaluacion_antropometrica": evaluacion_antropometrica}
    return render(request, "evaluacion_antropometrica.html", context=context)

def cargar_clientes(request):
    return render(request, 'cargar_clientes.html')
    