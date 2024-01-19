import base64
from django.contrib import messages
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
from control_subcategorias .models import Subcategoria

def create_Producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto_instance = form.save(commit=False)
            
            # Asignar las llaves foráneas desde el formulario
            producto_instance.id_categoria = form.cleaned_data['id_categoria']
           # producto_instance.id_subcategoria = form.cleaned_data['id_subcategoria']

            if 'imagen' in request.FILES:
                imagen = request.FILES['imagen']
                
                # Aquí conviertes los datos binarios de la imagen y los asignas al campo imagen del modelo
                producto_instance.imagen = imagen.read()
                
            producto_instance.save()
            

            messages.success(request, 'Datos insertados correctamente.')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)
    else:
        form = ProductoForm()

    return render(request, 'control-productos.html', {'form': form})
def listar_Producto(request):
    productos = Producto.objects.all()
    return render(request, 'control-productos.html', {'productos': productos})
"""def update_Producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    # Serializa la imagen a su formato base64
    imagen_base64 = None
    if producto.imagen and isinstance(producto.imagen, bytes):
         imagen_base64 = base64.b64encode(producto.imagen).decode('utf-8')


    data = {
       'nombre_producto': producto.nombre_producto,
       'clave': producto.clave,
       'descripcion': producto.descripcion,
       'extract': producto.extract,
       'imagen_base64': imagen_base64,  # Agregamos la imagen serializada como base64
    }

    return JsonResponse(data)"""
"""def update_Producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    imagen_base64 = None

    if producto.imagen and isinstance(producto.imagen, bytes):
         imagen_base64 = base64.b64encode(producto.imagen).decode('utf-8')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto_instance = form.save(commit=False)

            if 'imagen' in request.FILES:
                imagen = request.FILES['imagen']
                producto_instance.imagen = imagen.read()

            producto_instance.save()
            
            data = {'message': 'Datos actualizados correctamente'}
            return redirect('listar')
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre_producto': producto.nombre_producto,
            'clave': producto.clave,
            'descripcion': producto.descripcion,
            'extract': producto.extract,
            'imagen_base64': imagen_base64,
            
            
        }
        

        return JsonResponse(data)"""
def update_Producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    imagen_base64 = None

    if producto.imagen and isinstance(producto.imagen, bytes):
        imagen_base64 = base64.b64encode(producto.imagen).decode('utf-8')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto_instance = form.save(commit=False)

            if 'imagen' in request.FILES:
                imagen = request.FILES['imagen']
                producto_instance.imagen = imagen.read()

            producto_instance.save()

            # Incluye el ID de la categoría en la respuesta
            data = {
                'message': 'Datos actualizados correctamente',
                'id_categoria': producto_instance.id_categoria_id,
                'id_subcategoria': producto_instance.id_subcategoria_id,
            }
            return redirect('listar_producto')

        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre_producto': producto.nombre_producto,
            'clave': producto.clave,
            'descripcion': producto.descripcion,
            'extract': producto.extract,
            'imagen_base64': imagen_base64,
            'id_categoria': producto.id_categoria_id,
            #'id_subcategoria': producto.id_subcategoria_id,
            #'id_categoria': producto.id_categoria.nombre_categoria,
            #'id_categoria': producto.id_categoria.nombre_categoria if producto.id_categoria else None,

        }

        return JsonResponse(data)

@csrf_exempt    
def delete_Producto(request, id_producto):
    # Obtiene la instancia del producto
    producto = get_object_or_404(Producto, id_producto=id_producto)

    # Elimina el producto
    producto.delete()

    return JsonResponse({'message': 'Registro eliminado correctamente'})

def obtener_subcategorias(request):
    try:
        id_categoria = request.GET.get('id_categoria')
        
        if id_categoria is not None:
            subcategorias = Subcategoria.objects.filter(id_categoria_id=id_categoria)
            data = [{'id': sub.id_subcategoria, 'nombre': sub.nombre_subcategoria} for sub in subcategorias]
            # Cambiado el nombre del campo de 'id_subcategoria_id' a 'id_subcategoria'
        else:
            data = []

        return JsonResponse(data, safe=False)
    except Exception as e:
        print('Error:', str(e))
        return JsonResponse({'error': str(e)}, status=500)
