"""# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Usuario

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario  # O auth.User si decides usarlo directamente
        fields = ['username', 'password']
    
    
"""