# Generated by Django 4.2.7 on 2024-01-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotiza_gral', '0003_cotizacion_delete_formcotizar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='estatus',
            field=models.CharField(blank=True, choices=[('pendiente', 'Pendiente'), ('atendida', 'Atendida')], max_length=20, null=True, verbose_name='status'),
        ),
    ]
