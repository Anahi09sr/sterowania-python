import logging
from django.shortcuts import render
from .forms import CotizacionForm
from django.contrib import messages
from .models import Cotizacion
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
#from django.core.mail import send_mail
from django.core.mail import EmailMessage

logger = logging.getLogger(__name__)
#Función que permite validar el captcha
def validate_recaptcha(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': '6LfaUE8pAAAAABDGh9Euv8iZY-43VJpSRPDZ5a1y',
        'response': recaptcha_response
    }
     # Envío de la solicitud para verificar la respuesta del reCAPTCHA
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    response = r.json()
    return response['success']
def create_cotizacion(request):
    form = CotizacionForm()  # inicializacion del formulario
    if request.method == 'POST':
        if validate_recaptcha(request):
            # El reCAPTCHA es válido
            form = CotizacionForm(request.POST)  # Crea el formulario con los datos del POST
            if form.is_valid():
                form.save() #Guarda la cotizacion si el captcha y datos del formulario son validos
                messages.success(request, 'Datos insertados correctamente.')
                return redirect('create_cotizacion')
            else:
                #Errores si el formulario no es valido
                messages.error(request, 'Error al insertar datos. Revise los datos.')
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        else:
            # El reCAPTCHA no es válido
            messages.error(request, 'Captcha no válido. Por favor, inténtalo de nuevo.')
    return render(request, 'cotiza_gral.html', {'form': form})
#deshabilita la porteccion, se debe haer cuando se requiera aceptar solicitudes post desde el ajax.
@csrf_exempt 
def atender_cotizacion(request, id_cotizacion):
    if request.method == 'POST':
        try:
            # Obtener la cotización a través del ID
            cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion) 
            cotizacion.estatus = 'atendida' #Marcar la cotizacion como atendida
            cotizacion.save()  #  guardar los cambios
            return JsonResponse({'message': 'Cotización marcada como atendida'})
        except Exception as e:
            print('Error al atender la cotización:', str(e))
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)

def listar_cotizacion(request):
    cotizaciones = Cotizacion.objects.all() #obtiene todas las cotizaciones de la BD
    return render (request, "control-cotiza.html", {"cotizaciones":cotizaciones})

def update_cotizacion(request, id_cotizacion):
    #obtiene la cotizacion respecto al id
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
        # Enviar los datos de la cotización para su visualización en la interfaz de usuario
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