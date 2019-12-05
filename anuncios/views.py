from django.shortcuts import render
from django.http import HttpResponse

from .models import Categoria, Anuncio

def home(request):
    categorias = Categoria.objects.all()
    ultimos_anuncios = Anuncio.objects.all()[:12]

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': ultimos_anuncios})


def categoria(request, slug):
    categorias = Categoria.objects.all()
    categoria_slug = Categoria.objects.filter(slug=slug).get()

    anuncios = Anuncio.objects.filter(categoria=categoria_slug)

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': anuncios})
# Create your views here.
