from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from accounts.models import perfilDeUsuario
from accounts.forms import actualizarPerfil, actualizarUsuario

# Create your views here.
@login_required
def perfil_view(request):
    return render(request, 'accounts/account.html')

@login_required
def cambiar_perfil_view(request):
    try:
        usuario = perfilDeUsuario.objects.get(user=request.user)
    except:
        usuario = perfilDeUsuario.objects.create(
            user = request.user,
            nombre = 'John',
            apellido = 'Doe',
        )
    if request.method == 'POST':
        form = actualizarPerfil(request.POST, request.FILES)
        passwordForm = actualizarUsuario(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            usuario.nombre = form.cleaned_data['nombre']
            usuario.apellido = form.cleaned_data['apellido']
            usuario.telefono = form.cleaned_data['telefono']
            if form.cleaned_data['imagen']:
                usuario.imagen = form.cleaned_data['imagen']
            usuario.descripcion = form.cleaned_data['descripcion']
            usuario.web = form.cleaned_data['web']
            usuario.save()
            return redirect('/accounts')
        else:
            form = actualizarPerfil(initial={
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'telefono': usuario.telefono,
                'imagen': usuario.imagen,
                'descripcion': usuario.descripcion,
                'web': usuario.web,
                'email': request.user.email,
            })
            passwordForm = actualizarUsuario()
            errores = form.errors.items()
            passError = passwordForm.errors.items()
            context = {'errores':errores, 'passError':passError,'form':form, 'passwordForm':passwordForm}
            return render(request, 'accounts/profile.html', context=context)
    else:
        form = actualizarPerfil(initial={
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'telefono': usuario.telefono,
        'imagen': usuario.imagen,
        'descripcion': usuario.descripcion,
        'web': usuario.web,
        'email': request.user.email,
        })
        passwordForm = actualizarUsuario()
        context = {'form':form, 'passwordForm':passwordForm}
        return render(request, 'accounts/profile.html', context=context)
    
@login_required
def borrar_imagen(request):
    request.user.perfil.imagen.delete()
    return redirect('/accounts')

@login_required
def actualizar_contrasenia(request):
    usuario = perfilDeUsuario.objects.get(user=request.user)
    if request.method == 'POST':
        form = actualizarUsuario(request.POST)
        if form.is_valid():
            username = request.user
            password = form.cleaned_data['password1']
            username.ser_password(password)
            username.save()
            usuario = authenticate(username=username, password=password)
            login(request, usuario)
            return redirect('/accounts')
        else:
            form = actualizarPerfil(initial={
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'telefono': usuario.telefono,
                'imagen': usuario.imagen,
                'descripcion': usuario.descripcion,
                'web': usuario.web,
                'email': request.user.email,
            })
            passwordForm = actualizarUsuario()
            passError = passwordForm.errors
            print(passError)
            context = {'passError':passError, 'form':form, 'passwordForm':passwordForm}
            return render(request, 'accounts/profile.html', context=context)
    else:
        form = actualizarPerfil(initial={
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'telefono': usuario.telefono,
        'imagen': usuario.imagen,
        'descripcion': usuario.descripcion,
        'web': usuario.web,
        'email': request.user.email,
        })
        passwordForm = actualizarUsuario()
        context = {'form':form, 'passwordForm':passwordForm}
        return render(request, 'accounts/profile.html', context=context)