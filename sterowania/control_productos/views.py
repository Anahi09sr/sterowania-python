from django.shortcuts import render

# Create your views here.
def control_productos(request):
    return render(request, 'control-productos.html')