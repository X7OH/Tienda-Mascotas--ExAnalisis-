# Generated by Django 5.0.6 on 2024-07-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=50)),
                ('contraseña', models.CharField(max_length=12)),
                ('Dir1', models.CharField(max_length=30, default="N/A")),
                ('Dir2', models.CharField(max_length=30, default="N/A")),
                ('Ciudad', models.CharField(max_length=15, default="N/A")),
                ('rol', models.CharField(max_length=20)),
            ],
        ),
    ]
