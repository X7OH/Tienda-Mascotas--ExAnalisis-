# Generated by Django 5.0.6 on 2024-07-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaMascotaApp', '0013_alter_usuario_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(max_length=128),
        ),
    ]
