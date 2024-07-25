from django import forms
from TiendaMascotaApp.models import Usuario,Producto
import re

class RegUs(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido','correo', 'contraseña', 'Dir1', 'Dir2','Ciudad']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    exp="^[a-zA-Z]+$"
    expD="^[a-zA-Z0-9-]+$"
    
    def clean_nombre(self):
        nombre=self.cleaned_data.get('nombre')
        
        if not re.match(self.exp, nombre):
            raise forms.ValidationError("Verifica el Nombre no es un Nombre Válido")
        return nombre
    
    def Dir(self):
        Dir1=self.cleaned_data.get('Dir1')
        Dir2=self.cleaned_data.get('Dir2')
        
        if not re.match(self.exp, Dir1):
            raise forms.ValidationError("Verifica la Calle Principal no es una Dirección Válido")
        elif not re.match(self.exp, Dir2):
            raise forms.ValidationError("Verifica la Calle Secundaria no es una Dirección Válido")
            
        return Dir1, Dir2
    
    def clean_apellido(self):
        apellido=self.cleaned_data.get('apellido')
        if not re.match(self.exp, apellido):
            raise forms.ValidationError("Verifica el Apellido no es un Apellido Válido")
        return apellido

    
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 8:
            raise forms.ValidationError("La contraseña debe ser de al menos 8 caracteres.")
        return contraseña

    
    
class RegiProd(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProd', 'marca', 'categoria','descripcion','cantidad','precio', 'foto']

    # def clean_nombreProd(self):
    #     nombreProd = self.cleaned_data.get('nombreProd')
    #     exp = "^[a-zA-Z]+$"
    #     if not re.match(exp, nombreProd):
    #         raise forms.ValidationError("Verifica el Nombre no es un Nombre Válido")
    #     return nombreProd
    
    # def clean_marca(self):
    #     marca=self.cleaned_data.get('marca')
    #     exp="^[a-zA-Z]+$"
    #     if not re.match(exp, marca):
    #         return forms.ValidationError("Verifica la Marca no es un Marca Válido")
    #     return marca
    
    # def clean_desc(self):
    #     exp="^[a-zA-Z0-9\-.,/]+$"
        
    #     descripcion = self.cleaned_data.get('descripcion')
    #     # if not re.match(exp, descripcion):
    #     #     raise forms.ValidationError("Vuelva a verificar la Descripcion.")
    #     return descripcion

    # def clean_cantidad(self):
    #     cantidad=self.cleaned_data.get('cantidad')
    #     if (cantidad<0):
    #         return forms.ValidationError("No permiten valores negativos")
    #     return cantidad
    
    # def clean_precio(self):
    #     precio = self.cleaned_data.get('precio')
    #     if precio is None or precio <= 0:
    #         raise forms.ValidationError("Introduzca un número válido para el precio.")
    #     return precio