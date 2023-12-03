from django.shortcuts import render
from .forms import CotizacionForm
from django.contrib import messages

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