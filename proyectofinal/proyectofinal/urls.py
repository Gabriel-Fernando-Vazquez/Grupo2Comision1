
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name = 'home'),
    path('sobre-nosotros', views.SobreNosotros, name = 'sobre-nosotros'),
    path('contacto', views.Contacto, name = 'contacto'),

    #URLS DE AUTH
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),

    #URLS DE USUARIOS
    path('usuarios/', include('apps.usuarios.urls')),
    #URLS DE NOTICIAS
    path('noticias/', include('apps.noticias.urls')),
    # NOTICIAS ORDENADAS SEGUN...
    path('ord-fecha-desc/', views.OrdFechaDesc, name="ord-fecha-desc"),
    path('ord-tit-asc/', views.OrdTitAsc, name="ord-tit-asc"),
    path('ord-tit-desc/', views.OrdTitDesc, name="ord-tit-desc"),

     #URLS DE COMENTARIOS
    path('comentarios/', include('apps.comentarios.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)