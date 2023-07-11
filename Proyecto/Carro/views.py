from django.shortcuts import render, redirect
from Carro.carro import Carro
from Carro.models import Pedido
from aplicacion1.models import Productos
from Carro.forms import formulario_pedido
from django.views.generic import CreateView
from django.contrib import messages

from Usuarios.models import UsuarioPersonalizado

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect('home')
        
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('home')

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('home')

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('home')

def orden_pedido(request, producto_id):
    producto = Productos.objects.get(id=producto_id)
    if request.user.is_authenticated:
        cliente = UsuarioPersonalizado.objects.get(id = request.user.id)
        data = {
        'pedido' : formulario_pedido({'producto_nombre' : producto,
        'costo' : producto.precio,
        'usuario': cliente.username})
        }
    else:
        data = {
            'pedido' : formulario_pedido({'producto_nombre' : producto,
            'costo' : producto.precio,
            'usuario': 'cliente externo'})
             }

    if request.method == 'POST':
        formulario = formulario_pedido(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "!Compra exitosa!")
            return redirect('home')

    return render(request, 'carro/datos_envio.html', data)

