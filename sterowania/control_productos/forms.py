from django import forms
from .models import Producto
from control_subcategorias.models import Categoria,Subcategoria

class ProductoForm(forms.ModelForm):
    # Agrega un campo personalizado para manejar la imagen
    
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=None)
    id_subcategoria = forms.ModelChoiceField(queryset=Subcategoria.objects.all(), empty_label=None)

    class Meta:
        model = Producto
        fields =  '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Asegúrate de que los campos de llaves foráneas estén correctamente vinculados a los objetos de la base de datos
        self.fields['id_categoria'].queryset = Categoria.objects.all()
        self.fields['id_subcategoria'].queryset = Subcategoria.objects.all()

   

    