from django import forms
from django.forms import ModelForm
from .models import Subcategoria, Categoria
from django.core.validators import RegexValidator

#Formulario del modelo Subcategoria
class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ['nombre_subcategoria', 'id_categoria'] #Se definen lso campos del formulario
    #Define un campo de opcion de mode
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=None)
    #Validacion para el nombre subactegoria
    nombre_subcategoria_validator = RegexValidator(
        regex=r'^[a-zA-Z\sñáéíóúüÁÉÍÓÚÜ]+$',
        message="El nombre debe contener solo letras y espacios."
    )
    #Define el campo de texto para el nombre de la subcategoria y aplica la validacion
    nombre_subcategoria = forms.CharField(validators=[nombre_subcategoria_validator])
    #define un metodo para validar y limpiar el valor del campo
    def clean_nombre_subcategoria(self):
        nombre_subcategoria = self.cleaned_data.get('nombre_subcategoria')
        return nombre_subcategoria