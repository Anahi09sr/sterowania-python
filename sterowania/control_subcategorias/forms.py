from django import forms
from django.forms import ModelForm
from .models import Subcategoria, Categoria
""""
class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ['nombre_subcategoria', 'id_categoria']
    def __init__(self, *args, **kwargs):
        super(SubcategoriaForm, self).__init__(*args, **kwargs)
        # Modificar el widget del campo id_categoria para que sea un select
        self.fields['id_categoria'].widget = forms.Select(choices=[(c.id_categoria, c.nombre_categoria) for c in Categoria.objects.all()])"""
class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ['nombre_subcategoria', 'id_categoria']

    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=None)
