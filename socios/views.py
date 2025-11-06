from django.shortcuts import render, get_object_or_404
from .models import Socio

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, './template/lista_soc.html', {'socios': socios})

def detalhe_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    return render(request, './template/detalhes_soc.html', {'socio': socio})

