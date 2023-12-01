#configuracion de urls de está app
from django.urls import path

#views
from . import views
urlpatterns =[
    path('semaforos',views.semaforos, name='semaforos'),
    path('postes',views.postes, name='postes'),
    path('senalamientos',views.senalamientos, name='senalamientos'),
    path('complementos',views.complementos, name='complementos'),
    path('servicios',views.servicios, name='servicios'),
]