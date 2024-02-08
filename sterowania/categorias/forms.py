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
        message="Ingrese un número de teléfono válido."
    )
    
    nombre_cliente_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message="El nombre del cliente debe contener solo letras y espacios."
    )
    
    nombre_empresa_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9\s]+$',
        message="El nombre de la empresa solo puede contener letras y números."
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
        # Puedes realizar validaciones adicionales aquí si es necesario
        return telefono

    def clean_nombre_cliente(self):
        nombre_cliente = self.cleaned_data.get('nombre_cliente')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return nombre_cliente

    def clean_nombre_empresa(self):
        nombre_empresa = self.cleaned_data.get('nombre_empresa')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return nombre_empresa

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return mensaje

    def clean_email(self):
        correo = self.cleaned_data.get('email')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return correo