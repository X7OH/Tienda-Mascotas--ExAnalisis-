from django import forms
from TiendaMascotaApp.models import Usuario,Producto
import re

class RegUs(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido','correo', 'contraseña', 'Dir1', 'Dir2','Ciudad','rol']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean_nombre(self):
        nombre=self.cleaned_data.get('nombre')
        exp="^[a-zA-Z]+$"
        if not re.match(exp, nombre):
            raise forms.ValidationError("Verifica el Nombre no es un Nombre Válido")
        return nombre

    
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 8:
            raise forms.ValidationError("La contraseña debe ser de al menos 8 caracteres.")
        return contraseña

    
    
class RegiProd(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProd', 'marca', 'categoria','descripcion','cantidad','precio', 'foto']

    def nombrPr(self):
        nombreProd=self.cleaned_data.get('nombreProd')
        exp="^[a-zA-Z]+$"
        if not re.match(exp, nombreProd):
            return forms.ValidationError("Verifica el Nombre no es un Nombre Válido")
        return nombreProd
    
    def clean_desc(self):
        exp="^[a-zA-Z0-9\-.,/]+$"
        
        descripcion = self.cleaned_data.get('descripcion')
        if not re.match(exp, descripcion):
            raise forms.ValidationError("La descripcion debe ser de al menos 8 caractéres.")
        return descripcion

    def cantidad(self):
        cantidad=self.cleaned_data.get('cantidad')
        if (cantidad<0):
            return forms.ValidationError("No permiten valores negativos")
        return cantidad
    
    def precio(self):
        exp="^[0-9.,]+$"
        precio=self.cleaned_data.get('precio')
        if not re.match(exp, precio):
            return forms.ValidationError("Verifica el precio, valor Incorrecto")
        elif(","in precio):
            preciof=precio.replace(",",".")
            return preciof
        return precio
