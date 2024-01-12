#configuracion de urls de está app
from django.urls import path
#from .views import save_cotizacion, create_cotizacion, listar_cotizacion, update_cotizacion, delete_cotizacion
#views
from . import views
urlpatterns =[
    path('semaforos',views.semaforos, name='semaforos'),
    path('postes',views.postes, name='postes'),
    path('senalamientos',views.senalamientos, name='senalamientos'),
    path('complementos',views.complementos, name='complementos'),
    path('servicios',views.servicios, name='servicios'),
    path('create_cotizacionCatalogo',views.create_cotizacionCatalogo, name='create_cotizacionCatalogo'),
]