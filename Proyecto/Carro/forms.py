
from django import forms
from aplicacion1.models import Productos
from Usuarios.models import UsuarioPersonalizado
from Carro.models import Pedido

class formulario_pedido(forms.ModelForm):
    
    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['usuario_pedido','estado']
        widgets = {'costo':forms.TextInput(attrs={'readonly':'True'}),
                   'producto_nombre':forms.TextInput(attrs={'readonly':'True'}),
                   'usuario':forms.TextInput(attrs={'readonly':'True'})}

class modificar_estado(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('estado',)
    