#configuracion de urls de está app
from django.urls import path

#views
from . import views
urlpatterns =[
    path('create',views.create_cotizacion, name='create'), #url original, se decide dejar el espacio vacio ''
    path('save',views.save_cotizacion, name='save'),
    path('control',views.listar_cotizacion, name='control'), #url original, se decide dejar el espacio vacio ''
    path('editar/<int:id_cotizacion>', views.edit_cotizacion, name='editar_cotizacion')
]
#coreViews