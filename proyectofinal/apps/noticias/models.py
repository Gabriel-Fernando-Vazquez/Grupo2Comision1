from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	nombre = models.CharField(max_length=80)
	imagen = models.ImageField(upload_to= 'categoria')

	def __str__(self):
		return self.nombre

class Noticia(models.Model):
	creado = models.DateTimeField(
		'creado',
		auto_now_add=True
	)
	modificado = models.DateTimeField(
		'modificado',
		auto_now=True
	)
	titulo = models.CharField(max_length = 250)
	contenido = models.TextField()
	autor = models.ForeignKey(User, on_delete = models.CASCADE)
	imagen = models.ImageField(upload_to = 'noticias')
	categoria = models.ManyToManyField(Categoria, blank=True)

	def MisComentarios(self):
		return self.comentario_set.all()

	def __str__(self):
		return self.titulo