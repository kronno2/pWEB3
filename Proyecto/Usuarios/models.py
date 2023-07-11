from django.db import models
from django.contrib.auth.models import AbstractUser
from aplicacion1.models import Productos
from django.core.validators import RegexValidator

class UsuarioPersonalizado(AbstractUser):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    telefono = models.CharField(validators = [phoneNumberRegex], max_length = 12, unique = True)




