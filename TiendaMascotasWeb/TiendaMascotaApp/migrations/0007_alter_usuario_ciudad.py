# Generated by Django 5.0.6 on 2024-07-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaMascotaApp', '0006_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Ciudad',
            field=models.CharField(default='Quito', max_length=15),
        ),
    ]