from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=15,null=False)
    apellido = models.CharField(max_length=15,null=False)
    correo = models.EmailField(max_length=50,null= False)
    contraseña = models.CharField(max_length=12,null=False)
    Dir1= models.CharField(max_length=30,default="N/A")
    Dir2= models.CharField(max_length=30,default="N/A")
    Ciudad= models.CharField(max_length=15,default="N/A")
    rol = models.CharField(max_length=20, default="Cliente")
    
class Producto(models.Model):
    nombreProd = models.CharField(max_length=50,null=False)
    marca=models.CharField(max_length=20,null=False,default="N/A")
    categoria = models.CharField(max_length=20,null=False)
    descripcion = models.CharField(max_length=100,null=False)
    cantidad = models.IntegerField(default="0")
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    foto= models.ImageField(upload_to="fotos", default="fotos/default.png")
