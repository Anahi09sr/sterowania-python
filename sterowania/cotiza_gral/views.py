from django.shortcuts import render
from .forms import Cotizacion
from django.contrib import messages

def nueva_cotizacion(request):
    form = Cotizacion(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, 'Datos insertados correctamente.')
        form = Cotizacion()
    else:
         messages.error(request, 'Error al insertar datos. Revise los datos.')
    context = {'form': form }   
        
    return render(request, 'cotiza_gral.html', context)


