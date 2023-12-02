from django.shortcuts import render
from .forms import CotizacionForm
from django.contrib import messages


def create_cotizacion(request):
    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            form.save()
            messages.success(request, 'Datos insertados correctamente.')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
    else:
        # If it's a GET request, create a new form
        form = CotizacionForm()

    # Render the template with the form
    return render(request, 'cotiza_gral.html', {'form': form})
