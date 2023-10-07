from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Principal 

def index(request):
    return render(request, 'index/index.html')

def usuario(request):
    return render(request, 'vistas/usuario.html')

def productos(request):
    return render(request, 'vistas/productos.html')

#Productos
def electronica(request):
    return render(request, 'vistas/electronica.html')

def juguetes(request):
    return render(request, 'vistas/juguetes.html')

def ropa(request):
    return render(request, 'vistas/ropa.html')

#Descripcion
def desc_computador(request):
    return render(request, 'vistas/electronica_desc/desc_computador.html')