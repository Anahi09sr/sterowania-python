""#configuracion de urls de está app
from django.urls import path

#views
from . import views
urlpatterns =[
    path('',views.catalogo, name='catalogo') #url original, se decide dejar el espacio vacio ''
]
#coreViews""