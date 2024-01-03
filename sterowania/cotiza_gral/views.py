from django.shortcuts import render
from .forms import CotizacionForm
from django.contrib import messages
from .models import Cotizacion
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def create_cotizacion(request):
    # If the request method is POST, process the form data
    return render(request, 'cotiza_gral.html')

def save_cotizacion(request):
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

    return render(request, 'cotiza_gral.html', {'form': form})
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