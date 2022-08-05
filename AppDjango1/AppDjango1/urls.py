"""AppDjango1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include

from AppDjango1.views import saludar,mostrar_fecha,calculo,calculo2,plantilla1,tareasEnlistadas,tareasEnlistadas2,games,musica,tecnologia,saludo_ej,index
from AppDjango1.views import formulario,home,respuesta,form_bus,resultado,registro,validacion,register,register2,ingresar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludando/',saludar),
    path('fecha/',mostrar_fecha),
    path('plantilla1/',plantilla1),
    path('calculo/<int:fechaNacimiento>/<int:fechaFutura>',calculo),
    path('calculo2/<int:fechaNacimiento>/<int:fechaFutura>',calculo2),
    path('listado/',tareasEnlistadas),
    path('listado2/',tareasEnlistadas2),
    path('games/',games),
    path('musica/',musica),
    path('tecnologia/',tecnologia),
    path('saludo/',saludo_ej),
    path('index/',index),

    path('formulario/', formulario),
    path('home/', home),
    path('respuesta/', respuesta),
    path('formulario-busqueda/', form_bus),
    path('resultado/', resultado),
    path('registro/',registro),
    path('validacion/',validacion),
    path('register/',register),
    path('register2/',register2),
    path('',home),
    path('login/',ingresar),
]
