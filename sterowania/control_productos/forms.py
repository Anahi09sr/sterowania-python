# control_productos/forms.py
from django import forms
from .models import Producto
import binascii
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['clave','nombre_producto', 'descripcion', 'extract']
        exclude = ['imagen']  # Excluir el campo imagen del formulario
    