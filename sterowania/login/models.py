"""# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Agrega campos adicionales específicos si es necesario
    # username, password, email, etc., ya están incluidos en AbstractUser
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=12)
    class Meta:
        managed = True
        db_table = 'usuario' 
    """
