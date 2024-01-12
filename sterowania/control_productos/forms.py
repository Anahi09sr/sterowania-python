from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    # Agrega un campo personalizado para manejar la imagen
    

    class Meta:
        model = Producto
        fields =  '__all__'

    