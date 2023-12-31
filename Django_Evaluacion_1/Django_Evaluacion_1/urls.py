"""
URL configuration for Django_Evaluacion_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('usuario/', views.usuario),
    path('productos/', views.productos),
    path('productos/electronica/', views.electronica),
    path('productos/juguetes/', views.juguetes),
    path('productos/ropa/', views.ropa),
    path('productos/electronica/desc_computador/', views.desc_computador),
    path('productos/electronica/desc_consola/', views.desc_consola),
    path('productos/electronica/desc_parlantes/', views.desc_parlantes),
    path('productos/juguetes/desc_juguetebebe/', views.desc_juguetebebe),
    path('productos/juguetes/desc_jugueteagua/', views.desc_jugueteagua),
    path('productos/juguetes/desc_juguetepokemon/', views.desc_juguetepokemon),
    path('productos/ropa/desc_ropainvierno/', views.desc_ropainvierno),
    path('productos/ropa/desc_ropaverano/', views.desc_ropaverano),
    path('productos/ropa/desc_ropacalzado/', views.desc_ropacalzado),
    ]
