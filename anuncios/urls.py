from django.urls import path
from .views import home, categoria, anuncio, buscar

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<slug:slug>/', categoria, name='categoria'),
    path('anuncio/<slug:categoria_slug>/<slug:anuncio_slug>/', anuncio, name='anuncio'),
    path('buscar/', buscar, name='buscar')

]
