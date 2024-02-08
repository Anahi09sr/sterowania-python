"""from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

#Este código me permitió craar al usario y su contraseña

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Crear un nuevo usuario
        user = User.objects.create_user(username='Sterowania', password='12Abc')
         # Autenticar al usuario
        user = auth.authenticate(username='Sterowania', password='12Abc')

        if user is not None:
             # El usuario es autenticado, iniciar sesión
            auth.login(request, user)
            return redirect('control')
        else:
             # El usuario no es autenticado, mostrar un mensaje de error
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')



    else:
        return render(request, 'login.html')"""
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import requests

def validate_recaptcha(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': '6LfaUE8pAAAAABDGh9Euv8iZY-43VJpSRPDZ5a1y',
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    response = r.json()
    return response['success']
def login_user(request):
    if request.method == 'POST':
        if validate_recaptcha(request):
            username = request.POST['username']
            password = request.POST['password']

            # Autenticar al usuario con las credenciales proporcionadas
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # El usuario es autenticado, iniciar sesión
                login(request, user)
                return redirect('control')
            else:
                # El usuario no es autenticado, mostrar un mensaje de error
                messages.error(request, 'El nombre de usuario o contrseña no son correctos.')
                return redirect('login')
        else:
            # El reCAPTCHA no es válido
            messages.error(request, 'Captcha no válido. Por favor, inténtalo de nuevo.')
            return render(request, 'login.html') 
    else:
        return render(request, 'login.html')
def logout_user(request):
    # Cerrar sesión del usuario
    logout(request)
    return redirect('login')