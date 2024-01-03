#configuracion de urls de está app
from django.urls import path
from django.contrib.auth.decorators import login_required
from login.views import login_user 
#views
from . import views
urlpatterns =[
    path('create_producto',views.create_Producto, name='create_producto'),
    path('listar_producto', login_required (views.listar_Producto), name='listar_producto'),
    path('editar_producto/<int:id_producto>', login_required (views.update_Producto), name='editar_producto'),
    path('eliminar_producto/<int:id_producto>', views.delete_Producto, name='eliminar_producto'),
]
