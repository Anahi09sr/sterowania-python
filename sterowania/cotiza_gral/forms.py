from django import forms
from django.forms import ModelForm
from .models import Cotizacion
from django.core.validators import RegexValidator


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ["nombre_cliente", "telefono", "email", "nombre_empresa", "mensaje"]
    #RegexValidator,  es una clase proporcionada por Django para validar campos de texto utilizando expresiones regulares.
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
    
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message="Ingrese una dirección de correo electrónico válida."
    )

    telefono = forms.CharField(validators=[telefono_validator])
    nombre_cliente = forms.CharField(validators=[nombre_cliente_validator])
    nombre_empresa = forms.CharField(validators=[nombre_empresa_validator])
    mensaje = forms.CharField(validators=[mensaje_validator])
    email = forms.CharField(validators=[email_validator])

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        return telefono

    def clean_nombre_cliente(self):
        nombre_cliente = self.cleaned_data.get('nombre_cliente')
        return nombre_cliente

    def clean_nombre_empresa(self):
        nombre_empresa = self.cleaned_data.get('nombre_empresa')
        return nombre_empresa

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        return mensaje

    def clean_email(self):
        correo = self.cleaned_data.get('email')
        return correo