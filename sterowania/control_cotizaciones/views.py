from django.shortcuts import render
#from django.contrib.auth.decorators import login_required


# Create your views here.
def control_cotiza(request):
    return render(request, 'control-cotizaciones.html')
