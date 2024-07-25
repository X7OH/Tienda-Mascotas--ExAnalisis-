from django.contrib.auth.hashers import check_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Usuario(models.Model):
    nombre = models.CharField(max_length=15,null=False)
    apellido = models.CharField(max_length=15,null=False)
    correo = models.EmailField(max_length=50,null= False)
    contraseña = models.CharField(max_length=80,null=False)
    Dir1= models.CharField(max_length=30,default="N/A")
    Dir2= models.CharField(max_length=30,default="N/A")
    Ciudad= models.CharField(max_length=15,default="Quito")
    rol = models.CharField(max_length=20, default="Cliente")
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def check_password(self, raw_password):
        # Usa check_password para verificar la contraseña
        return check_password(raw_password, self.contraseña)
    
class Producto(models.Model):
    nombreProd = models.CharField(max_length=50,null=True)
    marca=models.CharField(max_length=20,null=False,default="N/A")
    categoria = models.CharField(max_length=20,null=False)
    descripcion = models.CharField(max_length=100,default="N/A")
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True, blank=True)
    foto= models.ImageField(upload_to="fotos", default="fotos/default.png")
