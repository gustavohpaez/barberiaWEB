from django.shortcuts import render, HttpResponse
from tienda.models import CategoriaProd, Producto
from carro.carro import Carro

def home(request):

    carro=Carro(request)

    categoria=CategoriaProd.objects.all()
    productos=Producto.objects.all()

    return render(request, "core/home.html", {"categoria":categoria, "productos":productos})

def base(request):    

    categoria=CategoriaProd.objects.all()
    
    return render(request, "core/base.html", {"categoria":categoria})
