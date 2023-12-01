"""
URL configuration for sterowania project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
 
#Django settings
from django.conf import settings
#para trabajar con archivos estaticos, imagenes
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('core.urls')),
    path('catalogo/',include('catalogo.urls')),
    path('categorias/',include('categorias.urls')),
    path('cotizacion/',include('cotiza_gral.urls')),
    path('login/',include('login.urls')),
    path('control-cotizaciones/',include('control_cotizaciones.urls')),
    path('control-productos/',include('control_productos.urls')),
    path('control-subcategorias/',include('control_subcategorias.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 