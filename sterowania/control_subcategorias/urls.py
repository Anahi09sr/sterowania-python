from django.urls import path

from . import views
urlpatterns =[
    path('',views.control_subcategoria, name='control-subcategorias') 
]
