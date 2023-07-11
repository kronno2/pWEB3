from django.contrib import admin
from aplicacion1.models import Productos, CategoriaProducto


class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio",
                    "disponibilidad", "descripcion", "foto", "created", "update")
    search_fields = ("id", "nombre","categoria")
    

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created", "update")
    search_fields = ("nombre", "created")
    readonly_fields=("created","update")


admin.site.register(Productos, ProductosAdmin)
admin.site.register(CategoriaProducto, CategoriasAdmin)
