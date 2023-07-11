from django.shortcuts import render, redirect
from aplicacion1.models import Productos, CategoriaProducto
from aplicacion1.forms import formContacto, FormProducto
from Usuarios.forms import RegistroForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse
from Usuarios.models import UsuarioPersonalizado
from Carro.models import Pedido
from Carro.forms import modificar_estado

#API
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClienteSerializers
from rest_framework import status
from django.http import Http404

#CONSUMO
from .services import get_user

#Vistas generales
def home(request):
    productos = Productos.objects.all()
    categoria = CategoriaProducto.objects.all()
    diccionario = {'producto': productos}
    return render(request, 'index.html', diccionario)


def preguntas(request):
    return render(request, 'app1/preguntas.html')

def contacto(request):
    if request.method == 'POST':
        formulario = formContacto(request.POST)
        if formulario.is_valid():
            subject = "Mensaje de pagina"
            body = {
                'nombre': formulario.cleaned_data['nombre'],
                'asunto': formulario.cleaned_data['asunto'],
                'correo': formulario.cleaned_data['correo'],
                'telefono': formulario.cleaned_data['telefono'],
                'mensaje': formulario.cleaned_data['mensaje'],
            }
            mensaje = "\n".join(body.values())
            try:
                send_mail(subject, mensaje, 'Ani Mall',
                          ['contacto@animall.cl'])
                messages.success(request, 'Correo enviado con éxito.')
            except BadHeaderError:
                return HttpResponse('Error de encabezado.')
            return redirect("home")
    formulario = formContacto()
    return render(request, 'app1/contacto.html', {'formulario': formulario})


                                 #PRODUCTOS

def agregar_producto(request):
    if request.method=='POST':
        formu_producto = FormProducto(request.POST, files=request.FILES)
        if formu_producto.is_valid():
            formu_producto.save()
            messages.success(request, 'Producto agregado con exito')
            return redirect('mostrar_clientes')
    else:
        formu_producto = FormProducto()
    return render(request, 'app1/agregar.html', {'formu_producto': formu_producto})

def modificar_producto(request, id):
    producto = Productos.objects.get(id = id)
    data = {
        'form':FormProducto(instance = producto)
    }
    if request.method == 'POST':
        formulario = FormProducto(data=request.POST,files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto actualizado con exito')
            return redirect('mostrar_clientes')
    return render(request, 'app1/modificar.html', data)

def eliminar_producto(request, id):
    producto = Productos.objects.get(id = id)
    if request.user.is_staff:
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente')
        return redirect('mostrar_clientes')
    else:
        return HttpResponse('Recurso no encontrado')

                                  #ESTADO CLIENTES
def mostrar_estado(request,username):
    if request.user.is_authenticated and request.user.username == username:
        pedidos = Pedido.objects.filter(usuario=username)
        data = {'pedidos':pedidos}
        return render(request, 'app1/mostrar_estado.html',data)
    else:
        return HttpResponse("Pagina no disponible.")
                    
                                     
                                     #CLIENTES
def agregar_cliente(request):
    if request.method=='POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cliente agregado con exito')
            return redirect('mostrar_clientes')
    else:
        formulario = RegistroForm()
    return render(request, 'app1/agregar_cliente.html', {'formulario': formulario})

def mostrar_clientes(request):
    if request.user.is_staff:
        pedidos = Pedido.objects.all()
        clientes = UsuarioPersonalizado.objects.all()
        articulos = Productos.objects.all()
        data = {'clientes': clientes,
                'pedidos' : pedidos,
                'articulos':articulos}
        return render(request,'app1/mostrar_clientes.html',data)
    else:
        return HttpResponse("No puedes ingresar aqui")


def modificar_pedido(request, id):
    if request.user.is_staff:
        pedido = Pedido.objects.get(id = id)
        data = {
            'formulario_estado':modificar_estado(instance = pedido)
        }    
        if request.method == 'POST':
            formulario_estado = modificar_estado(data=request.POST, instance=pedido)
            if formulario_estado.is_valid():
                formulario_estado.save()
                messages.success(request, 'Modificacion de estado realizada')
                return redirect('mostrar_clientes')
        return render(request, 'app1/modificar_estado.html', data)
    else:
        return HttpResponse("No se puede acceder.")

    #BOTONES DE ESTADO DE PEDIDO

def estado_transito(request,id):
    if request.user.is_staff:
        pedido = Pedido.objects.get(id=id)
        pedido.estado = 'en transito'
        pedido.save()
        return redirect('mostrar_clientes')
    else:
        return HttpResponse('No disponible')

def estado_entregado(request,id):
    if request.user.is_staff:
        pedido = Pedido.objects.get(id=id)
        pedido.estado = 'entregado'
        pedido.save()
        return redirect('mostrar_clientes')
    else:
        return HttpResponse('No disponible')

def modificar_cliente(request, id):
    if request.user.is_staff:
        clientes = UsuarioPersonalizado.objects.get(id = id)
        data = {
        'formulario':RegistroForm(instance = clientes)
        }

        if request.method == 'POST':
            formulario = RegistroForm(data=request.POST, instance=clientes)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, 'Cliente actualizado con exito')
                return redirect('mostrar_clientes')
        return render(request, 'app1/modificar_clientes.html', data)

def eliminar_cliente(request, id):
    cliente = UsuarioPersonalizado.objects.get(id = id)
    if request.user.is_staff:
        cliente.delete()
        messages.success(request, 'Cliente eliminado correctamente')
        return redirect('mostrar_clientes')
    else:
        return HttpResponse('Necesitas los permisos.')

#CONSUMO API
def hola_usuario(requests):
    resultados = get_user()
    data = {
        'nombre': resultados.get('name').get('first'),
        'genero': resultados.get('gender'),
        'ciudad': resultados.get('location').get('city'),
        'email': resultados.get('email'),
        'usuario': resultados.get('login').get('username'),
        'pass': resultados.get('login').get('password'),
        'fotito': resultados.get('picture').get('large'),
    }
    return render(requests, 'api/api_consumo_usuario.html', data)

#API WEB   
class Clientes_APIVista(APIView):

    def get(self, request, format=None, *args, **kwargs):
        if request.user.is_authenticated:
            clientes = UsuarioPersonalizado.objects.all()
            serializer = ClienteSerializers(clientes, many=True)
            return Response(serializer.data)
        else:
            return Response("Alto ahi rufia")
              
    def post(self, request, format=None):
        serializer = ClienteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Clientes_APIDetalle(APIView):
    
    def get_object(self, pk):
        try:
            return UsuarioPersonalizado.objects.get(pk=pk)
        except UsuarioPersonalizado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializers(cliente)  
        return Response(serializer.data)

