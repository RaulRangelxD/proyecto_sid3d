from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def indentificar_usuario(request):
    if request.user.is_authenticated:
        if  request.user.is_admin == True:
            print('Admin')
        if  request.user.is_customer == True:
            print('Customer')
        if  request.user.is_employee == True:
            print('Employee')
        usuario = request.user
        usuario.profile = str(usuario.profile)
    else:
        usuario = None
    return usuario

def productos(request):
    usuario = indentificar_usuario(request)
    form = Producto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'productos.html', {'form': form, 'categoria': categoria, 'usuario': usuario})

def ver(request, nombre):
    usuario = indentificar_usuario(request)
    producto = get_object_or_404(Producto, nombre=nombre)
    categoria = Categoria.objects.all()
    return render(request, 'ver_producto.html', {'producto': producto, 'categoria': categoria, 'usuario': usuario})

def crear(request):
    usuario = indentificar_usuario(request)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            imagen = request.FILES['imagen']

            img = Image.open(imagen)
            img = ImageOps.exif_transpose(img)
            img = img.resize((500, 500))
            img_io = BytesIO()
            img.save(img_io, format='WEBP')
            img_file = InMemoryUploadedFile(img_io, 'ImageField', f"{producto.nombre}.webp", 'image/webp', sys.getsizeof(img_io), None)

            producto.imagen = img_file
            producto.save()
            return redirect('productos')
    else:
        form = ProductoForm()
        categoria = Categoria.objects.all()
    return render(request, 'cargar_producto.html', {'form': form, 'categoria': categoria, 'usuario': usuario})

def crear_categoria(request):
    usuario = indentificar_usuario(request)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crear')
    else:
        form = CategoriaForm()
        categoria = Categoria.objects.all()
    return render(request, 'crear_categoria.html', {'form': form, 'categoria': categoria, 'usuario': usuario})

def borrar(request, nombre):
    usuario = indentificar_usuario(request)
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        producto.imagen.delete()
        producto.delete()
        return redirect('productos')
    categoria = Categoria.objects.all()
    return render(request, 'confirmar_eliminacion.html', {'producto': producto, 'categoria': categoria, 'usuario': usuario})

def editar(request, nombre):
    usuario = indentificar_usuario(request)
    producto = get_object_or_404(Producto, nombre=nombre)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            try:
                imagen = request.FILES['imagen']
                
                img = Image.open(imagen)
                img = ImageOps.exif_transpose(img)
                img = img.resize((500, 500))
                img_io = BytesIO()
                img.save(img_io, format='WEBP')
                img_file = InMemoryUploadedFile(img_io, 'ImageField', f"{producto.nombre}.webp", 'image/webp', sys.getsizeof(img_io), None)

                producto.imagen = img_file
                form.save()
            except:
                form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
        categoria = Categoria.objects.all()
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto, 'categoria': categoria, 'usuario': usuario})

def busqueda(request, categoria):
    usuario = indentificar_usuario(request)
    productos = Producto.objects.all()
    filtro=[]
    for producto in productos:
        if producto.categoria.nombre.lower() == categoria.lower():
            filtro.append(producto)
    categoria = Categoria.objects.all()
    return render(request, 'busqueda.html', {'productos': filtro, 'categoria': categoria, 'usuario': usuario})