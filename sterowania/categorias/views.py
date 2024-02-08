#from cotiza_gral.views import create_cotizacion,save_cotizacion,listar_cotizacion,update_cotizacion,delete_cotizacion
import base64
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from .forms import CotizacionForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Cotizacion
from .models import Categoria, Subcategoria, Producto


"""def create_cotizacionCategoria(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cotización realizada con éxito!')
            return JsonResponse({'success': True, 'message': 'Cotización realizada con éxito!'})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return JsonResponse({'success': False, 'message': 'Error al insertar datos. Revise los datos.'}, status=400)
    else:
        form = CotizacionForm()
        return render(request, 'catalogo.html', {'form': form})"""
def create_cotizacionCategoria(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            # Procesar formulario y devolver éxito
            return JsonResponse({'success': True, 'message': 'Cotización realizada con éxito!'})
        else:
            # Return the validation errors
            errors = form.errors
            return JsonResponse({'success': False, 'errors': errors})
def listar_cotizacion(request):
    cotizaciones = Cotizacion.objects.all()
    return render (request, "control-cotiza.html", {"cotizaciones":cotizaciones})
def update_cotizacion(request, id_cotizacion):
    cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)
    data = {
        'nombre_cliente':cotizacion.nombre_cliente,
        'telefono': cotizacion.telefono,
        'email': cotizacion.email,
        'nombre_empresa': cotizacion.nombre_empresa,
        'mensaje': cotizacion.mensaje,
    }
    print(data)
    return JsonResponse(data)
@csrf_exempt
def delete_cotizacion(request, id_cotizacion):
    if request.method == 'POST':
        try:
            cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)
            cotizacion.delete()
            return JsonResponse({'message': 'Cotización eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)



# Create your views here.
"""def semaforos(request):
    return render(request, 'cat-semaforos.html')
"""
def semaforos(request):
     # Obtener la categoría con id_categoria=1
    categoria = Categoria.objects.get(id_categoria=1)

    # Obtener las subcategorías asociadas a la categoría
    subcategorias = Subcategoria.objects.filter(id_categoria=categoria)
    # Obtener todos los productos relacionados con las subcategorías
    productos = Producto.objects.filter(id_subcategoria__in=subcategorias)
    
    return render(request, 'cat-semaforos.html', {'categoria': categoria, 'subcategorias': subcategorias, 'productos': productos})

def postes(request):
     # Obtener la categoría con id_categoria=1
    categoria = Categoria.objects.get(id_categoria=2)

    # Obtener las subcategorías asociadas a la categoría
    subcategorias = Subcategoria.objects.filter(id_categoria=categoria)

    return render(request, 'cat-postes.html', {'categoria': categoria, 'subcategorias': subcategorias})
def senalamientos(request):
    # Obtener la categoría con id_categoria=1
    categoria = Categoria.objects.get(id_categoria=3)

    # Obtener las subcategorías asociadas a la categoría
    subcategorias = Subcategoria.objects.filter(id_categoria=categoria)
    return render(request, 'cat-senalamientos.html', {'categoria': categoria, 'subcategorias': subcategorias})
def complementos(request):
    # Obtener la categoría con id_categoria=1
    categoria = Categoria.objects.get(id_categoria=4)

    # Obtener las subcategorías asociadas a la categoría
    subcategorias = Subcategoria.objects.filter(id_categoria=categoria)
    return render(request, 'cat-complementos.html', {'categoria': categoria, 'subcategorias': subcategorias})
def servicios(request):
    # Obtener la categoría con id_categoria=1
    categoria = Categoria.objects.get(id_categoria=5)

    # Obtener las subcategorías asociadas a la categoría
    subcategorias = Subcategoria.objects.filter(id_categoria=categoria)
    return render(request, 'cat-servicios.html', {'categoria': categoria, 'subcategorias': subcategorias})
def catalogo(request):
    return render(request, 'catalogo.html')