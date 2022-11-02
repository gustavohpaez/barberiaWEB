from django.shortcuts import render, HttpResponse

from servicios.models import servicio


def servicios(request):
    servicios=servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})

