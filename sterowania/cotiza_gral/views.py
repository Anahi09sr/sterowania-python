from django.shortcuts import render
from .forms import CotizacionForm
from django.contrib import messages
from .models import Cotizacion
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def validate_recaptcha(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': '6LfaUE8pAAAAABDGh9Euv8iZY-43VJpSRPDZ5a1y',
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    response = r.json()
    return response['success']

def create_cotizacion(request):
    form = CotizacionForm()  # Mueve la creación del formulario fuera del bloque condicional

    if request.method == 'POST':
        if validate_recaptcha(request):
            # El reCAPTCHA es válido
            form = CotizacionForm(request.POST)  # Crea el formulario con los datos del POST
            if form.is_valid():
                form.save()
                messages.success(request, 'Datos insertados correctamente.')
                return redirect('create_cotizacion')
            else:
                messages.error(request, 'Error al insertar datos. Revise los datos.')
                messages.error(request, form.errors)  # Agrega este mensaje de error para obtener más detalles
        else:
            # El reCAPTCHA no es válido
            messages.error(request, 'Captcha no válido. Por favor, inténtalo de nuevo.')

    return render(request, 'cotiza_gral.html', {'form': form})

def listar_cotizacion(request):
    cotizaciones = Cotizacion.objects.all()
    return render (request, "control-cotiza.html", {"cotizaciones":cotizaciones})
"""def update_cotizacion(request, id_cotizacion):
    cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)
    data = {
        'nombre_cliente':cotizacion.nombre_cliente,
        'telefono': cotizacion.telefono,
        'email': cotizacion.email,
        'nombre_empresa': cotizacion.nombre_empresa,
        'mensaje': cotizacion.mensaje,
    }
    print(data)
    return JsonResponse(data)"""

def update_cotizacion(request, id_cotizacion):
    cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)

    if request.method == 'POST':
        form = CotizacionForm(request.POST, instance=cotizacion)
        if form.is_valid():
            form.save()
            data = {'message': 'Datos actualizados correctamente'}
            return JsonResponse(data)
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre_cliente': cotizacion.nombre_cliente,
            'telefono': cotizacion.telefono,
            'email': cotizacion.email,
            'nombre_empresa': cotizacion.nombre_empresa,
            'mensaje': cotizacion.mensaje,
        }
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