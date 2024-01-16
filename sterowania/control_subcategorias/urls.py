from django.urls import path
from django.contrib.auth.decorators import login_required
from login.views import login_user 

from . import views
urlpatterns =[
    path('create',views.create_Subcategoria, name='create'),
    path('listar', login_required (views.listar_Subcategorias), name='listar'),
    path('editar_subcategoria/<int:id_subcategoria>', login_required (views.update_Subcategoria), name='editar_subcategoria'),
    path('eliminar/<int:id_subcategoria>', views.delete_Subcategoria, name='eliminar_subcategoria'),
]

