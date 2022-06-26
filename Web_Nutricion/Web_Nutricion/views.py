from django.http import HttpResponse
from django.shortcuts import render, redirect

#login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from Web_Nutricion.forms import User_registration_form


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = UserCreationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)

def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)


def index(request):
    print(request.user)
#    print(request.user.is_authenticated)
#    print(request.user.user_profile.phone)
    return render(request, 'index.html')

