from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserChangeForm
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
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
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request,user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request,user)
                return redirect('employee')
            else:
                msg='credenciales invalidas'
        else:
            msg = 'Formulario inválido'
    return render(request, 'login.html', {'form':form, 'msg':msg})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return redirect('/productos/')

def admin(request):
    return render(request, 'admin.html')

def customer(request):
    return render(request, 'customer.html')

def employee(request):
    return render(request, 'employee.html')


def edit_user_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('login_view')  
    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'user_edit.html', {'form': form})