from django.contrib import admin

from .models import Categoria, Noticia , Objetivo

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Objetivo)