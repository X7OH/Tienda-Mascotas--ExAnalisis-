# Generated by Django 5.0.6 on 2024-07-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaMascotaApp', '0008_alter_producto_descripcion_alter_producto_nombreprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]