from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Es administrador', default=False)
    is_customer = models.BooleanField('Es cliente', default=False)
    is_employee = models.BooleanField('Es empleado', default=False)


