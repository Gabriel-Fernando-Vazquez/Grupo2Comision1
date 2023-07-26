from django.urls import path, include
from . import views

app_name='noticias'

urlpatterns = [
    path('Crear', views.CrearNoticiaC.as_view(), name="crear_noticia"),
      # Noticias del usuario 
    path('mis-noticias', views.MisNoticias, name="misNoticias"),
     # Detalle de una noticia
    path('detalle-noticia/<int:pk>', views.DetalleNoticiaF, name='detalle_noticia'),
    
    path('Listar', views.ListarNoticiasF, name="listar_noticias"),

    path('Detalle/<int:pk>', views.DetalleNoticiaF, name="detalle_noticias"),

    path('Filtro/<int:pk>', views.Filtro_Categoria, name="filtro_categoria"),

    path('Borrar/<int:pk>', views.BorrarNoticia.as_view(), name="borrar_noticia"),

    path('Modificar/<int:pk>', views.ModificarNoticia.as_view(), name="modificar_noticia"),
   
    path('categorias', views.Categorias, name='categorias'),

    
   
   

]