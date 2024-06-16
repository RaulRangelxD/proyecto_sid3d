from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

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
    return render(request, 'productos.html', {'form': form, 'categoria': categoria})

def ver(request):
    form = Producto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'ver_producto.html', {'form': form, 'categoria': categoria})

def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            imagen = request.FILES['imagen']
            
            img = Image.open(imagen)
            img = img.resize((500, 500))
            img_io = BytesIO()
            img.save(img_io, format='WEBP')
            img_file = InMemoryUploadedFile(img_io, 'ImageField', f"{producto.nombre}.webp", 'image/webp', sys.getsizeof(img_io), None)

            producto.imagen = img_file
            producto.save()
            return redirect('home_productos')
    else:
        form = ProductoForm()
        categoria = Categoria.objects.all()
    return render(request, 'cargar_producto.html', {'form': form, 'categoria': categoria})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crear')
    else:
        form = CategoriaForm()
        categoria = Categoria.objects.all()
    return render(request, 'crear_categoria.html', {'form': form, 'categoria': categoria})

def borrar(request, nombre):
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        producto.imagen.delete()
        producto.delete()
        return redirect('home_productos')
    categoria = Categoria.objects.all()
    return render(request, 'confirmar_eliminacion.html', {'producto': producto, 'categoria': categoria})

def editar(request, nombre):
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home_productos')
    else:
        form = ProductoForm(instance=producto)
        categoria = Categoria.objects.all()
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto, 'categoria': categoria})

def busqueda(request, categoria):
    productos = Producto.objects.all()
    filtro=[]
    for producto in productos:
        if producto.categoria.nombre.lower() == categoria.lower():
            filtro.append(producto)
    categoria = Categoria.objects.all()
    return render(request, 'busqueda.html', {'productos': filtro, 'categoria': categoria})