from django.contrib import admin
from Carro.models import Pedido


class PedidoAdmin(admin.ModelAdmin):
    list_display=("usuario","nombre", "apellido", "direccion", "estado","fecha_solicitud","costo")
    search_fields=("usuario", "nombre","apellido","fecha_solicitud")

admin.site.register(Pedido, PedidoAdmin)
