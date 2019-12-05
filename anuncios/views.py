from django.shortcuts import render, get_object_or_404

from .models import Categoria, Anuncio

def home(request):
    categorias = Categoria.objects.all()
    ultimos_anuncios = Anuncio.objects.all()[:12]
    count_anuncios = []
    for c in range(categorias.count()):
        count_anuncios.append(Anuncio.objects.filter(categoria=categorias[c]).count())

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': ultimos_anuncios,
                                         'count_anuncios': count_anuncios,
                                         })


def categoria(request, slug):
    categorias = Categoria.objects.all()
    categoria_slug = get_object_or_404(Categoria, slug=slug)

    anuncios = Anuncio.objects.filter(categoria=categoria_slug)
    count_anuncios = []
    for c in range(categorias.count()):
        count_anuncios.append(Anuncio.objects.filter(categoria=categorias[c]).count())

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': anuncios,
                                         'count_anuncios': count_anuncios,
                                         'categoria': categoria_slug})


def anuncio(request, anuncio_slug, categoria_slug):
    categorias = Categoria.objects.all()
    get_object_or_404(Categoria, slug=categoria_slug)
    get_object_or_404(Anuncio, slug=anuncio_slug)

    anuncio = Anuncio.objects.get(slug=anuncio_slug)
    count_anuncios = []
    for c in range(categorias.count()):
        count_anuncios.append(Anuncio.objects.filter(categoria=categorias[c]).count())

    return render(request, 'anuncio.html', {'categorias': categorias,
                                            'count_anuncios': count_anuncios,
                                            'anuncio': anuncio})


def buscar(request):
    string = request.GET.get('q')
    categorias = Categoria.objects.all()
    count_anuncios = []
    for c in range(categorias.count()):
        count_anuncios.append(Anuncio.objects.filter(categoria=categorias[c]).count())

    resultado_busca = Anuncio.objects.all().filter(titulo__icontains=string)

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': resultado_busca,
                                         'count_anuncios': count_anuncios})
# Create your views here.
