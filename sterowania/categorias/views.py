#from cotiza_gral.views import create_cotizacion,save_cotizacion,listar_cotizacion,update_cotizacion,delete_cotizacion
from django.shortcuts import render
from .forms import CotizacionForm
from django.contrib import messages
from .models import Cotizacion

def create_cotizacionCatalogo(request):
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


# Create your views here.
def semaforos(request):
    return render(request, 'cat-semaforos.html')
def postes(request):
    return render(request, 'cat-postes.html')
def senalamientos(request):
    return render(request, 'cat-senalamientos.html')
def complementos(request):
    return render(request, 'cat-complementos.html')
def servicios(request):
    return render(request, 'cat-servicios.html')
def catalogo(request):
    return render(request, 'catalogo.html')