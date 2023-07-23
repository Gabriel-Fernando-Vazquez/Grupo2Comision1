from django.shortcuts import render
from django.views.generic import CreateView, ListView,DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Noticia,Categoria
from .forms import Form_Alta,Form_Modificacion

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearNoticiaC(LoginRequiredMixin, CreateView):
	model = Noticia
	form_class = Form_Alta
	template_name = 'noticias/crear.html'
	success_url = reverse_lazy('noticias:listar_noticias')
	
	
	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticiaC, self).form_valid(form)


class ListarNoticias(ListView):
	model = Noticia
	template_name = 'noticias/listar.html'
	#POR DEFECTO ESTA VISTA MANDA AL TEMPLATE UNA VARIABLE
	#LLAMADA OBJECT_LIST, CON LA LISTA DE TODAS LAS NOTICIAS




def ListarNoticiasF(request):
	ctx = {}
	todas_noticias = Noticia.objects.all()
	ctx['object_list'] = todas_noticias
	#ctx['nombre'] = 'Nicolas'
	return render(request, 'noticias/listar.html', ctx)

def DetalleNoticiaF(request, pk):
	ctx = {}
	noti = Noticia.objects.get(id = pk)
	ctx['noticia'] = noti
	return render(request, 'noticias/detalle.html', ctx)

#
#ctx = {'object_list': [lista de objectos], 'nombre':'Nicolas'}
# CUANDO EL HTML RECIBE EL DICCIONARIO CTX, AUTOMATICAMENTE LO DESARMA EN VARIABLES
# EN EL HTML
# object_list = [lista de objectos]
# nombre = 'Nicolas'

#ORM
# CONSULTA PARA TRAER TODOS LOS DATOS
# select * from Noticia  SQL
# Noticia.objects.all()   ORM

#CONSuLTA PARA TRAER SOLO UN DATO (POR CLAVE)
# select * from Noticia where id = algo
# Noticia.objects.get(id = algo)

#CONSuLTA PARA TRAER SOLO Algunos datos (POR filtro)
# select * from Noticia where categororia = deportes
# Noticia.objects.filter(categoria = deportes)

class Categorias(ListView):
	model = Categoria
	template_name = 'noticias/categorias.html'

def CategoriasF(request):
    ctx = {}
    lista_cat = []
    categorias = Categoria.objects.all()
    for categoria in categorias:
        nombre = categoria.nombre
        imagen = categoria.imagen
        lista_cat.append((nombre, imagen))
    ctx['object_list'] = lista_cat
    return render(request, 'noticias/categoria-lista.html', ctx)

		

def Filtro_Categoria(request, pk):
	ctx = {}
	cate = Categoria.objects.get(id = pk)
	filtadas = Noticia.objects.filter(categoria = cate)
	ctx['object_list'] = filtadas
	return render(request, 'noticias/listar.html', ctx)

class BorrarNoticia(DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:listar_noticias')


def MisNoticias(request):
	ctx = {}
	lista_noticias = Noticia.objects.filter(autor = request.user)
	print(lista_noticias)
	ctx['object_list'] = lista_noticias

	return render(request, 'noticias/misNoticias.html', ctx)


class ModificarNoticia(UpdateView):
	model = Noticia
	form_class = Form_Modificacion
	template_name = 'noticias/Modificar.html'
	success_url = reverse_lazy('noticias:listar_noticias')


class Listarcategorias(ListView):
	model = Categoria
	template_name = 'noticias/crear.html'


