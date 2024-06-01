from django import forms
from .models import Producto
from control_subcategorias.models import Categoria,Subcategoria

class ProductoForm(forms.ModelForm):
    #Esto perite que el administrador pueda seleccionar en la lista despelgable 
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=None)
    id_subcategoria = forms.ModelChoiceField(queryset=Subcategoria.objects.all(), empty_label=None)

    class Meta:
        model = Producto
        fields =  '__all__' #Se inluyen todos los campos del modelo producto
    def __init__(self, *args, **kwargs):
        """ Se personaliza la inicialización del formulario para actualizar
            dinámicamente las opciones de los campos id_categoria e id_subcategoria
            presentes en la base de datos."""
        super().__init__(*args, **kwargs)
        # se utilizan para obtener todos los objetos de modelo de las categorías y subcategorías, respectivamente.
        self.fields['id_categoria'].queryset = Categoria.objects.all()
        self.fields['id_subcategoria'].queryset = Subcategoria.objects.all()

   

    