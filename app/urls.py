"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ARCHIVO GENERAL DE DIRECCIONES QUE TOMARA COMO REFERENCIA LAS URL DE CADA APP
    path('',include(('bases.urls','bases'), namespace='bases')), # LLAMADA DE URLS DE LA VISTA PRINCIPAL
    path('inv/',include(('inv.urls','inv'), namespace='inv')), # LLAMADA DE URLS DE EL INVENTARIO
    path('cmp/', include(('cmp.urls', 'cmp'), namespace='cmp')), # LLAMADA DE URLS DE LAS COMPRAS Y MOVIMIENTOS
    path('fac/', include(('fac.urls', 'fac'), namespace='fac')), # LLAMAD DE URLS DE LAS FACTURAS
    path('api/', include(('api.urls', 'api'), namespace='api')), # LLAMADA DE URLS DE LOS REPORTES Y AUXILIARES
    # ARCHIVO DEL LOGIN ADMINISTRADOR
    path('admin/', admin.site.urls),
]
