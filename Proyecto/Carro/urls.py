from django.urls import path
from Carro.views import agregar_producto, eliminar_producto,restar_producto,limpiar_carro,orden_pedido

#app_name = 'carro'

urlpatterns = [
    path('agregar_producto/<int:producto_id>/', agregar_producto, name="agregar_producto_carro"),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name="eliminar_producto_carro"),
    path('restar_producto/<int:producto_id>/', restar_producto, name="restar_producto_carro"),
    path('limpiar_producto/<int:producto_id>/', limpiar_carro, name="limpiar_producto_carro"),
    path('datos-envio/<int:producto_id>', orden_pedido, name="datos_envio"),
]


    