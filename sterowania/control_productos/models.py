
import binascii
from io import BytesIO
from tkinter import Image
from django.db import models
from PIL import Image as PILImage
from django.forms import ValidationError


#from control_subcategorias.models import Categoria, Subcategoria
# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # The composite primary key (id_producto, clave) found, that is not supported. The first column is selected.
    clave = models.CharField(max_length=45)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    #nombre_img = models.CharField(max_length=250)
    #imagen = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.BinaryField()
    extract = models.CharField(max_length=50)
    #id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    #id_subcategoria = models.ForeignKey('control_subcategorias.Subcategoria', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        super(Producto, self).save(*args, **kwargs)
    """def validate_image(self):
        if self.imagen:
            # Abre la imagen para validar su formato
            try:
                image = Image.open(BytesIO(self.imagen))
                valid_formats = ('JPEG', 'PNG', 'GIF')  # Agrega los formatos que deseas permitir
                if image.format not in valid_formats:
                    raise ValidationError('Formato de imagen no permitido.')
            except Exception as e:
                raise ValidationError('Error al abrir la imagen.')
    def save(self, *args, **kwargs):
        super(Producto, self).save(*args, **kwargs)
        # Convertir datos binarios a BytesIO antes de abrir la imagen
        if self.imagen:
            image_data = BytesIO(self.imagen)
            image = Image.open(image_data)
            
            # Resto de tu lógica para procesar la imagen
        # Verifica si el campo imagen es una cadena de texto y conviértelo a bytes
        if isinstance(self.imagen, str):
            self.imagen = self.imagen.encode('utf-8')

        # Convierte los datos hexadecimales de vuelta a bytes
        binary_data = binascii.unhexlify(self.imagen)

        try:
            # Abre la imagen desde los datos binarios
            image = PILImage.open(BytesIO(binary_data))

            # Aquí puedes realizar cualquier manipulación de la imagen necesaria

            # Guarda los datos binarios en el campo BinaryField
            self.imagen = binary_data
            self.save(update_fields=['imagen'])
        except PILImage.UnidentifiedImageError:
            # Maneja la excepción de imagen no identificada
            print("Error: No se pudo identificar la imagen.")"""


    class Meta:
        managed = True
        db_table = 'producto'
       # unique_together = (('id_producto', 'clave'),)
