from django.db import models

# Create your models here.
class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100, verbose_name="nombre_cliente")
    telefono = models.CharField(max_length=10, verbose_name="telefono")
    email = models.CharField(max_length=50, blank=True, null=True, verbose_name="email")
    nombre_empresa = models.CharField(max_length=50, blank=True, null=True, verbose_name="nombre_empresa")
    mensaje = models.CharField(max_length=360, blank=True, null=True, verbose_name="mensaje")
    class Meta:
        db_table = 'cotizacion'
