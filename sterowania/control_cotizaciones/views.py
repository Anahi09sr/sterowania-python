from django.shortcuts import render

# Create your views here.
def control_cotiza(request):
    return render(request, 'control-cotizaciones.html')