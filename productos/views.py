from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

def index(request):
    if request.user.is_authenticated:
        if  request.user.is_admin == True:
            print('Admin')
        if  request.user.is_customer == True:
            print('Customer')
        if  request.user.is_employee == True:
            print('Employee')
    form = Producto.objects.all()
    categoria = Categoria.objects.all()
    for items in categoria:
        print(items.nombre)
    return render(request, 'productos.html', {'form': form, 'categoria': categoria})

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

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/crear/')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

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

def busqueda(request, categoria):
    productos = Producto.objects.all()
    filtro=[]
    for producto in productos:
        print(producto.categoria.nombre.lower())
        print(categoria.lower())
        print('--------------')
        if producto.categoria.nombre.lower() == categoria.lower():
            filtro.append(producto)
        
    return render(request, 'busqueda.html', {'productos': filtro})