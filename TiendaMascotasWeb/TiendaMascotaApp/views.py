from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from TiendaMascotaApp.models import Usuario, Producto
from TiendaMascotaApp.Forms import RegUs, RegiProd
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Para mensajes de error
from django.http import JsonResponse
from django.db.models import Q
import os
from django.contrib.auth.hashers import make_password
import bcrypt

def var(request):
    rol = request.session.get('usuario_rol', None)
    correo = request.session.get('usuario_correo', None)
    return rol,correo

def home(request):
    rol, correo = var(request)
    return render(request, 'home.html', {'user_role': rol, 'user_correo': correo} )

def Productos(request):
    rol, correo = var(request)
    query = request.GET.get('buscarProd', '')  # Obtén el término de búsqueda desde la query string

    if query:
        productos = Producto.objects.filter(
            Q(nombreProd__icontains=query) |
            Q(marca__icontains=query) |
            Q(categoria__icontains=query)
        )
    else:
        productos = Producto.objects.all()  # Muestra todos los productos si no hay búsqueda

    return render(request, "Productos.html", {'productos': productos, 'user_role': rol, 'user_correo': correo})

def buscProd(request):
    rol, correo = var(request)
    
    if request.method == "POST":
        valProd = request.POST.get('buscarProd')
        print(valProd)
        return redirect('Productos')  # Asegúrate de que la URL 'Productos' esté configurada correctamente en tus URLs
    
    return render (request, "Productos.html",{'user_role':rol,'user_correo':correo})

def DescProd(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    rol, correo = var(request)
    return render(request, "DescProd.html", {'producto':producto,'user_role': rol, 'user_correo': correo} )

def Servicios(request):
    rol, correo = var(request)
    return render(request, "Servicios.html", {'user_role': rol, 'user_correo': correo} )

def Contactos(request):
    rol, correo = var(request)
    correo = request.session.get('usuario_correo', None)
    print(rol)
    print(correo)
    return render(request, "Contactos.html", {'user_role': rol, 'user_correo': correo} )

def Registro(request):
    rol, correo = var(request)
    
    if request.method == "POST":
        form = RegUs(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rol = "Cliente"  # Establece el rol predeterminado si lo necesitas
            

            usuario.save()
            return redirect('Login')
        else:
            # Imprime errores de formulario para depuración
            print("Formulario no válido:", form.errors)
    else:
        form = RegUs()
    
    return render(request, "Registro.html", {'form': form, 'user_role': rol, 'user_correo': correo})


def RegProd(request):
    rol, correo = var(request)
    if request.method=="POST":
        form= RegiProd(request.POST, request.FILES)
        if form.is_valid():
            producto=form.save(commit=False)
            producto.save()
            return redirect('RegProd')
    else:
        form=RegiProd()
    
    return render(request, "RegProd.html", {'form':form, 'user_role': rol, 'user_correo': correo} )



def Login(request):
    
    if request.method == "POST":
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        
        try:
            usuario = Usuario.objects.get(correo=correo)
            
            if usuario.contraseña == contraseña:
                rol = usuario.rol
                print(rol)
                request.session['usuario_id'] = usuario.id
                request.session['usuario_rol'] = rol
                request.session['usuario_correo'] = usuario.correo
                return redirect('home')
            else:
                messages.error(request, 'Error: Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Error: Usuario no existe.')
    
    return render(request, 'Login.html')

def Logout(request):
    try:
        del request.session['usuario_id']
        del request.session['usuario_rol']
        del request.session['usuario_correo']
    except KeyError:
        pass
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('home')


def AdminUs(request):
    rol, correo = var(request)
    roles = ['Admin', 'Cliente']
    if request.method == "POST":
        usuario_id = request.POST.get("usuario_id")
        if usuario_id:  # Actualizar usuario existente
            usuario = get_object_or_404(Usuario, id=usuario_id)
            form = RegUs(request.POST, instance=usuario)
        else:  # Crear nuevo usuario
            form = RegUs(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('AdminUs')
    
    usuarios = Usuario.objects.all()  # Obtiene todos los usuarios
    return render(request, "AdminUs.html", {'usuarios': usuarios,'roles': roles, 'user_role': rol, 'user_correo': correo})

def ElimUs(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('AdminUs')

def ElimProd(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('ModProd')


def ModProd(request):
    rol, correo = var(request)
    categorias = ['Alimentos', 'Aseo', 'Ropa']

    if request.method == "POST":
        producto_id = request.POST.get("producto_id")
        
        if producto_id:  # Actualizar producto existente
            producto = get_object_or_404(Producto, id=producto_id)
            form = RegiProd(request.POST, request.FILES, instance=producto)
        else:  # Crear nuevo producto
            form = RegiProd(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('ModProd')  
        else:
            print(form.errors)  
            
    else:
        form = RegiProd()  

    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'ModProd.html', {'productos': productos,'categorias': categorias,'user_role': rol, 'user_correo': correo, 'form': form,  # Incluye el formulario en el contexto para la vista
    })