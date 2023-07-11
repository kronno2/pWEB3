from django.db import models
from Usuarios.models import UsuarioPersonalizado

ESTADO = (
    ("ingresado", "Ingresado"),
    ("transito", "En transito"),
    ("entregado", "Entregado"),
)

class Pedido(models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50,null = False)
    apellido = models.CharField(max_length=50)
    producto_nombre = models.CharField(max_length=50 ,null = False)
    direccion = models.CharField(max_length=200 ,null = False)
    costo = models.PositiveIntegerField(null = False)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO,null = False,default='ingresado')

    def __str__(self):
        return self.usuario


