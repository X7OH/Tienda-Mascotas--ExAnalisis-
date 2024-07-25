from django.contrib import admin
from TiendaMascotaApp.models import Usuario, Producto
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","correo","contraseña", "Dir1", "Dir2", "Ciudad", "rol")

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombreProd","marca","categoria","descripcion", "cantidad", "precio", "foto")


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)

