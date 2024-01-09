from django.contrib import messages
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import uuid

# views.py

def create_Producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            # Procesar la imagen y guardar la ruta
            if 'imagen' in request.FILES:
                producto.imagen = handle_uploaded_image(request.FILES['imagen'])
            producto.save()
            messages.success(request, 'Datos insertados correctamente.')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)
    else:
        form = ProductoForm()

    return render(request, 'control-productos.html', {'form': form})

"""def handle_uploaded_image(file):
    # Lógica para guardar la imagen y obtener la ruta
    # Puedes utilizar la biblioteca `uuid` para generar un nombre único para la imagen
    import uuid
    filename = str(uuid.uuid4()) + '.' + file.name.split('.')[-1]
    filepath = 'sterowania/media' + filename
    with open(filepath, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return filepath"""
def handle_uploaded_image(file):
    # Generar un nombre único para la imagen utilizando uuid
    filename = str(uuid.uuid4()) + '.' + file.name.split('.')[-1]
    # Construir la ruta completa utilizando MEDIA_ROOT
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    # Guardar la imagen en la ruta especificada
    with open(filepath, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return filepath

def listar_Producto(request):
    productos = Producto.objects.all()
    return render(request, 'control-productos.html', {'productos': productos})
def update_Producto(request, id_producto):
    producto = get_object_or_404(Producto,id_producto=id_producto)
    data = {
       'nombre_producto':producto.nombre_producto,
       'clave':producto.clave,
       'descripcion':producto.descripcion,
       'imagen_url':producto.imagen,
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