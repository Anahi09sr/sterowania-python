from django.db import models
#from control_subcategorias.models import Categoria, Subcategoria
# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # The composite primary key (id_producto, clave) found, that is not supported. The first column is selected.
    clave = models.CharField(max_length=45)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    #nombre_img = models.CharField(max_length=250)
    imagen = models.BinaryField()
    extract = models.CharField(max_length=50)
    #id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    #id_subcategoria = models.ForeignKey('control_subcategorias.Subcategoria', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'producto'
       # unique_together = (('id_producto', 'clave'),)
