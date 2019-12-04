from django.shortcuts import render
from django.http import HttpResponse

from .models import Categoria, Anuncio

def home(request):
    categorias = Categoria.objects.all()
    ultimos_anuncios = Anuncio.objects.all()[:12]

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': ultimos_anuncios})
# Create your views here.
