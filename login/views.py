from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistroForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/productos/')
        else:
            error_message = 'Usuario o contraseña incorrectos'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/iniciar_sesion/')
    else:
        form = RegistroForm()
    return render(request, 'registro_usuario.html', {'form': form})