from django.shortcuts import render

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