# Generated by Django 5.0.6 on 2024-06-18 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_cedula_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cedula',
            field=models.CharField(default='0', max_length=8, validators=[django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^\\d{1,8}$', 'La cédula debe ser numérica y tener un máximo de 8 dígitos.')]),
        ),
    ]