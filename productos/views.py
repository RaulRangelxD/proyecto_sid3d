from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto
from .forms import ProductoForm

def index(request):
    form = Producto.objects.all()
    return render(request, 'productos.html', {'form': form})

def ver(request):
    form = Producto.objects.all()
    return render(request, 'ver_producto.html', {'form': form})

def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm()
    return render(request, 'cargar_producto.html', {'form': form})

def borrar(request, nombre):
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        producto.imagen.delete()
        producto.delete()
        return redirect('/productos/')
    return render(request, 'confirmar_eliminacion.html', {'producto': producto})

def editar(request, nombre):
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})