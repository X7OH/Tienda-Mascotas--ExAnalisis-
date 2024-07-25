
from django.contrib import admin
from django.urls import path, re_path
from TiendaMascotaApp import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('Servicios', views.Servicios, name="Servicios"),
    path('Productos', views.Productos, name="Productos"),
    path('Contactos', views.Contactos, name="Contactos"),
    path('Registro', views.Registro, name="Registro"),
    path('Login', views.Login, name="Login"),
    path('RegProd', views.RegProd, name="RegProd"),
    path('logout', views.Logout, name='Logout'),
    path('Producto/<int:producto_id>',views.DescProd, name='DescProd'),
    path('AdminUs', views.AdminUs, name="AdminUs"),
    path('AdminUs/eliminar/<int:usuario_id>', views.ElimUs, name="ElimUs"),
    path('buscar/', views.buscProd, name='buscProd'),
    path('ModProd', views.ModProd, name='ModProd'),
    path('ModProd/eliminar/<int:producto_id>', views.ElimProd, name="ElimProd"),
]

urlpatterns +=[
    re_path(r'^media/(?P<path>.*)$',serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]