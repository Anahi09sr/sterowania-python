# Generated by Django 4.2.7 on 2023-12-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=1),
        ),
    ]
