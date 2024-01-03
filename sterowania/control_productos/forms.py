# control_productos/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['clave','nombre_producto', 'descripcion', 'extract']
        exclude = ['imagen']
