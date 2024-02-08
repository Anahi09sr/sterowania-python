
import binascii
from io import BytesIO
from tkinter import Image
from django.db import models
from PIL import Image as PILImage
from django.forms import ValidationError
from control_subcategorias.models import Categoria, Subcategoria
#Modelo de productos
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # The composite primary key (id_producto, clave) found, that is not supported. The first column is selected.
    clave = models.CharField(max_length=45)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.BinaryField()
    extract = models.CharField(max_length=50)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    id_subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, null=True)
    def save(self, *args, **kwargs):
        super(Producto, self).save(*args, **kwargs)
   

    class Meta:
        managed = True
        db_table = 'producto'
       
