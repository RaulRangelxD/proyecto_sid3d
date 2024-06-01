from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_2 = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    precio_3 = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    existencias = models.IntegerField(default=0)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
