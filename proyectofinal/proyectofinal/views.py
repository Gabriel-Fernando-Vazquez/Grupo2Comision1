from django.shortcuts import render, get_object_or_404
from apps.noticias.models import Noticia, Categoria, Objetivo

def Home(request):
	#ctx = {}
	#lista_noticias = Noticia.objects.order_by('-creado')
    #ctx['object_list'] = lista_noticias[0:3]
	#ctx['sola'] = lista_noticias[1]
	#ctx['otras'] = lista_noticias[4:9] 
	return render(request, 'inicio.html') #, ctx)

def SobreNosotros(request):
	return render(request,'sobre-nosotros.html')


def Contacto(request):
	return render(request,'contacto.html')


def OrdFechaDesc(request):
	ctx = {}
	lista_noticias = Noticia.objects.order_by('creado')
	ctx['object_list'] = lista_noticias[0:6]
	return render(request, 'ord-fecha-desc.html', ctx)


def OrdTitAsc(request):
	ctx = {}
	lista_noticias = Noticia.objects.order_by('titulo')
	ctx['object_list'] = lista_noticias[0:6]
	return render(request, 'ord-tit-asc.html', ctx)


def OrdTitDesc(request):
	ctx = {}
	lista_noticias = Noticia.objects.order_by('-titulo')
	ctx['object_list'] = lista_noticias[0:6]
	return render(request, 'ord-tit-desc.html', ctx)


def Categorias_objetivos(request):
    ctx = {}
    lista_cate = Categoria.objects.all()
    ctx['object_list'] = lista_cate
    return render(request, 'categorias-objetivos.html', ctx)


def objetivos_por_categoria(request, categoria_id):
    categoria_seleccionada = get_object_or_404(Categoria, pk=categoria_id)
    objetivos = Objetivo.objects.filter(categoria=categoria_seleccionada)
    
    return render(request, 'objetivos.html', {'categoria': categoria_seleccionada, 'objetivos': objetivos})

