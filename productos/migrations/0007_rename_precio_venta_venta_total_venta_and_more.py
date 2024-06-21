# Generated by Django 5.0.6 on 2024-06-20 02:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_remove_producto_precio_2_remove_producto_precio_3'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='precio_venta',
            new_name='total_venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente_venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_producto',
        ),
        migrations.AddField(
            model_name='venta',
            name='id_cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Venta_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.venta')),
            ],
        ),
    ]