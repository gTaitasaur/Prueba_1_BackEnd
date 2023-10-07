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

def desc_consola(request):
    return render(request, 'vistas/electronica_desc/desc_consola.html')

def desc_parlantes(request):
    return render(request, 'vistas/electronica_desc/desc_parlantes.html')


def desc_juguetebebe(request):
    return render(request, 'vistas/juguetes_desc/desc_juguetebebe.html')

def desc_jugueteagua(request):
    return render(request, 'vistas/juguetes_desc/desc_jugueteagua.html')

def desc_juguetepokemon(request):
    return render(request, 'vistas/juguetes_desc/desc_juguetepokemon.html')


def desc_ropainvierno(request):
    return render(request, 'vistas/ropa_desc/desc_ropainvierno.html')

def desc_ropaverano(request):
    return render(request, 'vistas/ropa_desc/desc_ropaverano.html')

def desc_ropacalzado(request):
    return render(request, 'vistas/ropa_desc/desc_ropacalzado.html')