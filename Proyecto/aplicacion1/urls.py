
from django.urls import path
from aplicacion1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('preguntas/', views.preguntas, name='preguntas'),

    path("agregar/", views.agregar_producto, name="agregar"),
    path('modificar-producto/<id>/', views.modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', views.eliminar_producto, name="eliminar_producto"),

    path('modificar_pedido/<id>/', views.modificar_pedido, name='modificar_pedido'),
    path("mostrar_estado/<username>", views.mostrar_estado, name="mostrar_estado"),
    path('mostrar-clientes/', views.mostrar_clientes, name='mostrar_clientes'),
    path("estado_transito/<id>", views.estado_transito, name="estado_transito"),
    path("estado_entregado/<id>", views.estado_entregado, name="estado_entregado"),

    path("agregar_cliente/", views.agregar_cliente, name="agregar_cliente"),
    path('modificar-clientes/<id>/', views.modificar_cliente, name="modificar_cliente"),
    path('eliminar-clientes/<id>/', views.eliminar_cliente, name="eliminar_clientes"),

    path('apiclientes', views.Clientes_APIVista.as_view()), 
    path('apiclientes/<int:pk>/', views.Clientes_APIDetalle.as_view()),
    path("consumo-api/", views.hola_usuario, name="consumo_api"),
  
]

