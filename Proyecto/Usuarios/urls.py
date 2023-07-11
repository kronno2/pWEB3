
from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("registrar/", views.RegistroUsuario.as_view(), name="registrar"),
    path("login/",LoginView.as_view(), {'template_name':'registration/login.html'}, name="login")
    ]