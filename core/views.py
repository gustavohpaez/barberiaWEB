from django.shortcuts import render, HttpResponse
from tienda.models import CategoriaProd
from carro.carro import Carro

def home(request):

    carro=Carro(request)

    categoria=CategoriaProd.objects.all()

    return render(request, "core/home.html", {"categoria":categoria})

