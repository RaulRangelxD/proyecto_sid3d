from django.core.validators import MaxLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cedula = models.CharField(
        max_length=8,
        validators=[
            MaxLengthValidator(8), 
            RegexValidator(r'^\d{1,8}$', 'La cédula debe ser numérica y tener un máximo de 8 dígitos.')
        ],
        default='0'
    )
    is_admin = models.BooleanField('Es administrador', default=False)
    is_customer = models.BooleanField('Es cliente', default=False)
    is_employee = models.BooleanField('Es empleado', default=False)
    profile = models.IntegerField('Perfil', default=False)
