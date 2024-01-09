from django.contrib import messages
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def create_Producto(request):
    if request.method == 'POST':
        form =ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos insertados correctamente.')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega este mensaje de error para obtener más detalles
    else:
        form =ProductoForm()

    return render(request, 'control-productos.html', {'form': form})
def listar_Producto(request):
    productos = Producto.objects.all()
    return render(request, 'control-productos.html', {'productos': productos})
def update_Producto(request, id_producto):
    producto = get_object_or_404(Producto,id_producto=id_producto)
    data = {
       'nombre_producto':producto.nombre_producto,
       'clave':producto.clave,
       'descripcion':producto.descripcion,
       'imagen':producto.imagen,
       'extract':producto.extract,

    }

    return JsonResponse(data)
@csrf_exempt
def delete_Producto(request, id_producto):
    if request.method == 'POST':
        try:
            subcategoria = get_object_or_404(Producto, id_producto=id_producto)
            subcategoria.delete()
            return JsonResponse({'message': 'Cotización eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)