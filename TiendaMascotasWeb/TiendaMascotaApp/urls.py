from django.urls import path,include

from django.contrib import admin
from TiendaMascotasWeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('TiendaMascotasApp.urls')),
]