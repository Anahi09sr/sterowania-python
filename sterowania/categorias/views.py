#from cotiza_gral.views import create_cotizacion,save_cotizacion,listar_cotizacion,update_cotizacion,delete_cotizacion
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .forms import CotizacionForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Cotizacion
from .models import Categoria, Subcategoria

def create_cotizacionCategoria(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos insertados correctamente.')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega este mensaje de error para obtener más detalles
    else:
        form = CotizacionForm()

    return render(request, 'catalogo.html', {'form': form})
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

    return render(request, 'cat-semaforos.html', {'categoria': categoria, 'subcategorias': subcategorias})

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