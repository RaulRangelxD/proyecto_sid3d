from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255, default='1')
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    existencias = models.IntegerField()
    eliminado = models.BooleanField(default=False)
    
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
   
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('login.User', on_delete=models.CASCADE, default=1)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cedula_venta = models.CharField(max_length=255)
    sector_venta = models.CharField(max_length=255)
    telefono_venta = models.CharField(max_length=255)
    fecha_venta = models.DateField(auto_now_add=True)
    en_proceso = models.BooleanField(default=False)
    confirmada = models.BooleanField(default=False)

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    rif_cedula_compra = models.CharField(max_length=255,default='1')
    sector_compra = models.CharField(max_length=255,default='1')
    telefono_compra = models.CharField(max_length=255,default='1')
    fecha = models.DateField(auto_now_add=True)
    proveedor = models.CharField(max_length=255)

class Venta_Producto(models.Model):
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Ingresos(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    total_ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

class Egresos(models.Model):
    id = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey('Compra', on_delete=models.CASCADE)
    total_egresos = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

class Cliente(models.Model):
   id = models.AutoField(primary_key=True)
   cliente_cliente = models.ForeignKey('Venta', on_delete=models.CASCADE)