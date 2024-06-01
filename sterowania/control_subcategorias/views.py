from django.contrib import messages
from django.shortcuts import render
from .models import Subcategoria
from .forms import SubcategoriaForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Categoria

#Vista para crear una nueva subcategoria
# Create your views here.
def create_Subcategoria(request):
    if request.method == 'POST':
        #Si la solicitud es post, se valida el formulario
        form =SubcategoriaForm(request.POST)
        if form.is_valid():
            #Si el formulario e valido se guardan los datos y muestra el mensaje de exito
            form.save()
            messages.success(request, 'Subcategoría creada con éxito.')
            return redirect('listar')
        else:
            #Mensajes que se muestran si llegara a ver un error 
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  #  mensaje de error para obtener más detalles
    else:
        form =SubcategoriaForm()

    return render(request, 'control-subcategoria.html', {'form': form})
def listar_Subcategorias(request):  #Listar las subcategorias 
    subcategorias = Subcategoria.objects.all() #Obtiene todas las subcategorias de la BD
    return render(request, 'control-subcategoria.html', {'subcategorias': subcategorias})
#Vista para actualizar una subcategoria existente 
def update_Subcategoria(request, id_subcategoria): 
    
    subcategoria = get_object_or_404(Subcategoria, id_subcategoria=id_subcategoria)
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST, instance=subcategoria)
        if form.is_valid():
            #Si el fromulario es valido se guardan y se muestran mensajes de exito
            form.save()
            data = {'message': 'Datos actualizados correctamente'}
            return redirect('listar')
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        #Si la salicitud no es post, se devuelven os datos d ela subcateoria en formato JSON paara cargar
        data = {
            'nombre_subcategoria':subcategoria.nombre_subcategoria,
            'id_categoria': subcategoria.id_categoria.id_categoria,  # Accede directamente a 'id_categoria'
        }
        
        return JsonResponse(data)
@csrf_exempt
def delete_Subcategoria(request, id_subcategoria):
    #Vista para eliminar 
    if request.method == 'POST':
        try:
            subcategoria = get_object_or_404(Subcategoria, id_subcategoria=id_subcategoria)
            subcategoria.delete()
            return JsonResponse({'message': 'Cotización eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else: #Si la solicitud no es post, se develeve este mensaje 
        return JsonResponse({'error': 'Método no permitido'}, status=403)

