# Generated by Django 4.2.7 on 2023-12-21 02:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cotiza_gral', '0002_formcotizar_delete_cotizar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id_cotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=100, verbose_name='nombre_cliente')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('telefono', models.CharField(max_length=10, verbose_name='telefono')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('nombre_empresa', models.CharField(blank=True, max_length=50, null=True, verbose_name='nombre_empresa')),
                ('mensaje', models.CharField(blank=True, max_length=360, null=True, verbose_name='mensaje')),
                ('estatus', models.CharField(blank=True, max_length=20, null=True, verbose_name='status')),
            ],
            options={
                'db_table': 'cotizacion',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='FormCotizar',
        ),
    ]