from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cedula = models.IntegerField(max_length=8, default=0)
    is_admin = models.BooleanField('Es administrador', default=False)
    is_customer = models.BooleanField('Es cliente', default=False)
    is_employee = models.BooleanField('Es empleado', default=False)
    profile = models.IntegerField('Perfil', default=False)



