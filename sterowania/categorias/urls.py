#configuracion de urls de está app
from django.urls import path
#from .views import save_cotizacion, create_cotizacion, listar_cotizacion, update_cotizacion, delete_cotizacion
#from control_subcategorias  .views import catalogo
#views
from . import views
urlpatterns =[
    path('semaforos',views.semaforos, name='semaforos'),
    path('postes',views.postes, name='postes'),
    path('senalamientos',views.senalamientos, name='senalamientos'),
    path('complementos',views.complementos, name='complementos'),
    path('servicios',views.servicios, name='servicios'),
    path('create_cotizacionCategoria',views.create_cotizacionCategoria, name='create_cotizacionCategoria'),
    path('catalogo', views.catalogo ,name='catalogo'),
]