from django.contrib import messages
from django.shortcuts import render
from .models import Subcategoria
from .forms import SubcategoriaForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def create_Subcategoria(request):
    if request.method == 'POST':
        form =SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategoría creada con éxito.')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega este mensaje de error para obtener más detalles
    else:
        form =SubcategoriaForm()

    return render(request, 'control-subcategoria.html', {'form': form})
def listar_Subcategorias(request):
    subcategorias = Subcategoria.objects.all()
    return render(request, 'control-subcategoria.html', {'subcategorias': subcategorias})
def update_Subcategoria(request, id_subcategoria):
    subcategoria = get_object_or_404(Subcategoria, id_subcategoria=id_subcategoria)
    data = {
        'nombre_subcategoria':subcategoria.nombre_subcategoria,
        'id_categoria': subcategoria.id_categoria.id_categoria,  # Accede directamente a 'id_categoria'
    }
    
    return JsonResponse(data)
@csrf_exempt
def delete_Subcategoria(request, id_subcategoria):
    if request.method == 'POST':
        try:
            subcategoria = get_object_or_404(Subcategoria, id_subcategoria=id_subcategoria)
            subcategoria.delete()
            return JsonResponse({'message': 'Cotización eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)