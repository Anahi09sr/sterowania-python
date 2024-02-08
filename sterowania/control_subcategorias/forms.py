from django import forms
from django.forms import ModelForm
from .models import Subcategoria, Categoria
from django.core.validators import RegexValidator

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ['nombre_subcategoria', 'id_categoria']

    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=None)
    nombre_subcategoria_validator = RegexValidator(
        regex=r'^[a-zA-Z\sñáéíóúüÁÉÍÓÚÜ]+$',
        message="El nombre debe contener solo letras y espacios."
    )
    nombre_subcategoria = forms.CharField(validators=[nombre_subcategoria_validator])
    def clean_nombre_subcategoria(self):
        nombre_subcategoria = self.cleaned_data.get('nombre_subcategoria')
        return nombre_subcategoria