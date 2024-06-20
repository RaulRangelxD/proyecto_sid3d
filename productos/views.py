from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto, Categoria, Venta_Producto, Venta
from .forms import ProductoForm, CategoriaForm, VentaForm, VentaProductoForm
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from random import sample
from django.http import JsonResponse
from django.db.models import Sum, F
from django.contrib.auth import logout
import sys

venta_actual = None

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

def index(request):
    usuario = indentificar_usuario(request)
    form = Producto.objects.all()
    productos = Producto.objects.all()
    categorias=Categoria.objects.all()
    nombre_categorias = []
    no_categorias = False
    print(len(categorias))
    if len(categorias) > 2:
        print(False)
        no_categorias = False
        for cat in categorias:
            nombre_categorias.append(cat.nombre.lower())
        nombre_categorias = sample(nombre_categorias, 3)
        filtro1=[]
        for producto in productos:
            if producto.categoria.nombre.lower() == nombre_categorias[0]:
                filtro1.append(producto)
        filtro2=[]
        for producto in productos:
            if producto.categoria.nombre.lower() == nombre_categorias[1]:
                filtro2.append(producto)
        filtro3=[]
        for producto in productos:
            if producto.categoria.nombre.lower() == nombre_categorias[2]:
                filtro3.append(producto)
    else:
        no_categorias = True
        print(True)
    categoria = Categoria.objects.all()
    return render(request, 'index.html', {'form': form, 'categoria': categoria, 'no_categorias': no_categorias,'filtro1': filtro1, 'filtro2': filtro2, 'filtro3': filtro3, 'usuario': usuario})

def productos(request):
    usuario = indentificar_usuario(request)
    form = Producto.objects.all()
    categoria = Categoria.objects.all()
    if request.method == 'POST':
        venta_producto_form = VentaProductoForm()
        producto_id = request.POST.get('producto_id')
        cantidad = request.POST.get('cantidad', 1)
        global venta_actual
        print(venta_actual)
        if venta_actual is None:
            venta = Venta.objects.create(id_cliente=request.user)
            venta_actual = venta

        Venta_Producto.objects.create(id_venta=venta_actual, id_producto_id=producto_id, cantidad=cantidad)
        return JsonResponse({'status': 'success', 'message': 'Producto agregado correctamente'}, status=200)
    else:
        venta_producto_form = VentaProductoForm()
    return render(request, 'productos.html', {'form': form, 'categoria': categoria, 'usuario': usuario,'venta_producto_form': venta_producto_form})

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

def carrito(request):
    usuario = indentificar_usuario(request)
    global venta_actual
    usuario = indentificar_usuario(request)
    
    if request.method == 'POST':
        if 'cancelar_compra' in request.POST:
            venta_actual = None
            return redirect('carrito')
        else:
            form = VentaForm(request.POST, request.FILES)
            if form.is_valid():
                total = Venta_Producto.objects.filter(id_venta=venta_actual).aggregate(total=Sum(F('cantidad') * F('id_producto__precio')))['total'] or 0
                venta_actual.total_venta = total
                venta_actual.cedula_venta = request.user.cedula
                venta_actual.sector_venta = 'Establecimiento unico'
                venta_actual.telefono_venta = '1234' #cambiar cuando se agregue al usuario: request.user.celular
                venta_actual.save()

                form.instance = venta_actual
                form.save()
                venta_actual = None
                return redirect('productos')
    else:
        form = VentaForm()
    
    categoria = Categoria.objects.all()
    venta_producto = Venta_Producto.objects.all()
    articulos_carrito = []

     # Calcular el total de la venta antes de guardar
    
    
    if venta_actual is not None:
        total = Venta_Producto.objects.filter(id_venta=venta_actual).aggregate(total=Sum(F('cantidad') * F('id_producto__precio')))['total'] or 0
        
        # Actualizar el total de la venta
        venta_actual.total_venta = total
        venta_actual.save()
        for producto in venta_producto:
            if producto.id_venta.id == venta_actual.id:
                articulos_carrito.append(producto.id_producto)
    return render(request, 'carrito.html', {'form': form, 'categoria': categoria, 'usuario': usuario, 'venta_actual': venta_actual, 'articulos_carrito': articulos_carrito})

def logout_view(request):
    global venta_actual
    venta_actual = None
    logout(request)
    return redirect('productos')