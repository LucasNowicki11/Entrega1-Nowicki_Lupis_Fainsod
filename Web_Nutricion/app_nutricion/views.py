from django.shortcuts import render
from app_nutricion.models import Clientes, Evaluacion_Antropometrica, Recetas
from app_nutricion.forms import Client_form, Evaluacion_form

# Create your views here.


def listar_clientes(request):
    lista_clientes = Clientes.objects.all()
    context = {'lista_clientes': lista_clientes}
    return render(request, 'lista_clientes.html', context=context)

def cargar_clientes(request):
    if request.method == 'GET':
        form = Client_form()
        context = {'form':form}
        return render(request, 'cargar_clientes.html', context=context)
    else:
        form = Client_form(request.POST)
        if form.is_valid():
            new_client = Clientes.objects.create(
                name = form.cleaned_data['name'],
                last_name = form.cleaned_data['last_name'],
                age = form.cleaned_data['age'],
                birth_date = form.cleaned_data['birth_date'],
                sexo = form.cleaned_data['sexo'],
                email = form.cleaned_data['email'],
            )
            context ={'new_client':new_client}
        return render(request, 'cargar_clientes.html', context=context)


def evaluacion_antropometrica(request):
    evaluacion_antropometrica = Evaluacion_Antropometrica.objects.all()
    context = {"evaluacion_antropometrica": evaluacion_antropometrica}
    return render(request, "evaluacion_antropometrica.html", context=context)


def cargar_evaluacion(request):
    if request.method == 'GET':
        form = Evaluacion_form()
        context = {'form':form}
        return render(request, 'cargar_evaluacion.html', context=context)
    else:
        form = Evaluacion_form(request.POST)
        if form.is_valid():
            new_evaluacion = Evaluacion_Antropometrica.objects.create(
                age = form.cleaned_data['age'],
                size = form.cleaned_data['size'],
                weight = form.cleaned_data['weight'],
                bodyfat = form.cleaned_data['bodyfat'],
                musclemass = form.cleaned_data['musclemass'],
                IMC = form.cleaned_data['IMC'],
            )
            context ={'new_evaluacion':new_evaluacion}
        return render(request, 'cargar_evaluacion.html', context=context)


def recetas(request):
    recetas = Recetas.objects.all()
    context = {"recetas": recetas}
    return render(request, "recetas.html", context=context)


def search_client_view(request):
    print(request.GET)
    #cliente = Clientes.objects.get()
    clientes=Clientes.objects.filter(name__icontains= request.GET['search'])
    context = {'clientes': clientes}
    return render(request,'search_client.html', context=context)