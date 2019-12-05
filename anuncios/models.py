from django.db import models
from django.utils.text import slugify
from .utils import generate_unique_slug

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.titulo) != self.slug:
                self.slug = generate_unique_slug(Categoria, self.titulo)
        else:  # create
            self.slug = generate_unique_slug(Categoria, self.titulo)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']


class Anuncio(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.titulo) != self.slug:
                self.slug = generate_unique_slug(Anuncio, self.titulo)
        else:  # create
            self.slug = generate_unique_slug(Anuncio, self.titulo)
        super(Anuncio, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-id']