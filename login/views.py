from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile = form.cleaned_data.get('profile')
            user.save()
            msg = 'El usuario ha sido creado'
            return redirect('login_view')  
        else:
            msg = 'No es válido el formulario'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg })

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            Username = form.cleaned_data.get('username') 
            Password = form.cleaned_data.get('password') 
            user = authenticate(username=Username, password=Password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('productos')
            elif user is not None and user.is_customer:
                login(request,user)
                return redirect('productos')
            elif user is not None and user.is_employee:
                login(request,user)
                return redirect('productos')
            elif user is not None:
                login(request,user)
                return redirect('productos')
            else:
                msg='credenciales invalidas'
        else:
            msg = 'Formulario inválido'
    return render(request, 'login.html', {'form':form, 'msg':msg})

def edit_user_view(request):
    usuario = request.user
    avatar = str(f'images/{usuario.profile}.jpg')
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile = form.cleaned_data.get('profile')
            user.save()
            return redirect('login_view')  
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'user_edit.html', {'form': form, 'avatar' : avatar})
    
def profile(request):
    usuario = request.user
    avatar = str(f'images/{usuario.profile}.jpg')
    return render(request, 'perfil.html', {'usuario': usuario, 'avatar' : avatar})

@login_required
def edit_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para mantener la sesión del usuario
            messages.success(request, '¡Tu contraseña ha sido actualizada exitosamente!')
            return redirect('productos')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'edit_password.html', {'form': form})
