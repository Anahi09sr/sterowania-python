# Create your models here.
from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'categoria'
class Subcategoria(models.Model):
    id_subcategoria = models.AutoField(primary_key=True)
    nombre_subcategoria = models.CharField(max_length=200)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'subcategoria'