from rest_framework import serializers
from Usuarios.models import UsuarioPersonalizado

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['id','username','first_name','last_name','email','telefono','is_active']
        #exclude = ['']
