from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def cargar_clientes(request):
    return render(request, 'cargar_clientes.html')