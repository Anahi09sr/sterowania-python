#configuracion de urls de está app
from django.urls import path

#views
from . import views
urlpatterns =[
    path('',views.nueva_cotizacion, name='cotiza_gral') #url original, se decide dejar el espacio vacio ''
]
#coreViews