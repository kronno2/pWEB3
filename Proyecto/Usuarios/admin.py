from django.contrib import admin
from Usuarios.models import UsuarioPersonalizado


class UsuarioAdmin(admin.ModelAdmin):
    list_display=("username", "first_name", "last_name", "email","telefono","is_staff","is_superuser")
    search_fields=("username", "first_name")


admin.site.register(UsuarioPersonalizado,UsuarioAdmin)


