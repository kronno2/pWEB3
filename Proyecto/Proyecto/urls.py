
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Usuarios
import Carro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion1.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("usuario/", include('Usuarios.urls'), name="urls_usuarios"),
    path("carro/", include('Carro.urls'), name="urls_carro"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    
