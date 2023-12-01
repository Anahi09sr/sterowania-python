from django import forms
from .models import Cotizacion

class Cotizacion(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre_cliente', 'telefono', 'email', 'nombre_empresa','mensaje']