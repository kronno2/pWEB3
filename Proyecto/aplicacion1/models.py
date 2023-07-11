
from django.db import models
from django import forms
from model_utils.models import TimeStampedModel, SoftDeletableModel

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "CategoriaProducto"
        verbose_name_plural = "CategoriasProductos"
    
    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    precio = models.PositiveIntegerField(null=False)
    disponibilidad = models.BooleanField(default=True)
    descripcion = models.TextField(max_length=100, null=True)
    foto = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
    
