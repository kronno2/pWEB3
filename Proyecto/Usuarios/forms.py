from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Usuarios.models import UsuarioPersonalizado

class RegistroForm(UserCreationForm):
    
    class Meta:
        model = UsuarioPersonalizado
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'telefono',
        ] 
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'telefono': 'Telefono',
        }

