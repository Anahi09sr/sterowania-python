#configuracion de urls de está app
from django.urls import path

#views
from . import views
urlpatterns =[
    path('',views.control_productos, name='control-productos') 
]
