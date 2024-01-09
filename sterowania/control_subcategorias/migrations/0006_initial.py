# Generated by Django 4.2.7 on 2023-12-21 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('control_subcategorias', '0005_remove_subcategoria_id_categoria_delete_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categoria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id_subcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('id_categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.DO_NOTHING, to='control_subcategorias.categoria')),
            ],
            options={
                'db_table': 'subcategoria',
                'managed': True,
            },
        ),
    ]