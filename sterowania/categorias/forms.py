from django import forms
from django.forms import ModelForm
from .models import Cotizacion
from django.core.validators import RegexValidator

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ["nombre_cliente", "telefono", "email", "nombre_empresa", "mensaje"]
    #RegexValidator, que es una clase proporcionada por Django para validar campos de texto utilizando expresiones regulares.
    telefono_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Ingrese un número de teléfono válido (puede incluir el código de país)."
    )
    nombre_cliente_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message="El nombre debe contener solo letras y espacios."
    )
    nombre_empresa_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9\s]+$',
        message="Este campo solo puede contener letras y números."
    )
    mensaje_validator = RegexValidator(
        regex=r'^[a-zA-Z\s\.,\'"-]+$',
        message="El mensaje debe contener solo letras, espacios y caracteres permitidos."
    )
    #Se le está aplicando la validación
    telefono = forms.CharField(validators=[telefono_validator])
    nombre_cliente = forms.CharField(validators=[ nombre_cliente_validator])
    nombre_empresa = forms.CharField(validators=[ nombre_empresa_validator])
    mensaje = forms.CharField(validators=[ mensaje_validator])
#los métodos clean_<campo> son utilizados para realizar validaciones personalizadas para un campo específico.
def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
def clean_cliente(self):
        nombre_cliente = self.cleaned_data.get('nombre_cliente')
def clean_empresa(self):
        nombre_empresa = self.cleaned_data.get('nombre_empresa')
def clean_mensaje(self):
        mensaje= self.cleaned_data.get('mensaje')
def clean_correo(self):
        correo = self.cleaned_data.get('correo')