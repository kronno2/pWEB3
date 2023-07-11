
from django import forms
from aplicacion1.models import Productos
from Usuarios.models import UsuarioPersonalizado


class formContacto(forms.Form):
    nombre = forms.CharField(required=True, max_length=20)
    asunto = forms.CharField(max_length=20) 
    correo = forms.EmailField(required=True, max_length=20)
    telefono = forms.CharField(required=True, max_length=12)
    mensaje = forms.CharField(help_text="Escriba su mensaje aqui", required=True, 
    max_length=200, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    
    def __str__(self):
        return self.nombre  + ' ' + self.correo   
        
class FormProducto(forms.ModelForm):

    class Meta: 
        model= Productos
        fields = ['nombre','categoria','precio', 'descripcion', 'foto']




