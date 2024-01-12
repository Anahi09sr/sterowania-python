#configuracion de urls de está app
from django.urls import path
from django.contrib.auth.decorators import login_required
from login.views import login_user 

#views
from . import views
urlpatterns = [
    path('create_cotizacion',views.create_cotizacion, name='create_cotizacion'),
    path('save', login_required(views.save_cotizacion), name='save'),
    path('control', login_required(views.listar_cotizacion), name='control'),
    path('editar/<int:id_cotizacion>', login_required(views.update_cotizacion), name='editar_cotizacion'),
    path('eliminar/<int:id_cotizacion>', views.delete_cotizacion, name='eliminar_cotizacion'),
    
]
#coreViews