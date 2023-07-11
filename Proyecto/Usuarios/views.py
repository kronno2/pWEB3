from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.views.generic import CreateView
from django.urls import reverse_lazy
from Usuarios.forms import RegistroForm

from Usuarios.models import UsuarioPersonalizado

class RegistroUsuario(CreateView):
    model = UsuarioPersonalizado
    template_name = "registration/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home')






