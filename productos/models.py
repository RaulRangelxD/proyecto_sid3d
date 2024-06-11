from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255, default='1')
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_2 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_3 = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    existencias = models.IntegerField()
    fecha = models.DateField(auto_now=True)
    
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
   
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    cedula = models.CharField(max_length=255)
    cliente_venta = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    proveedor = models.CharField(max_length=255)

class Ingresos(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

class Egresos(models.Model):
    id = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey('Compra', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)


class Cliente(models.Model):
   id = models.AutoField(primary_key=True)
   cliente_cliente = models.ForeignKey('Venta', on_delete=models.CASCADE)