# Generated by Django 5.0.6 on 2024-06-20 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_alter_venta_total_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='confirmada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='venta',
            name='en_proceso',
            field=models.BooleanField(default=False),
        ),
    ]
