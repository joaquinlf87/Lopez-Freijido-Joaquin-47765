from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

#Modelo Autor: representará a los autores de las publicaciones del blog
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nombre

#Modelo Categoría:  representará las categorías en las que se pueden clasificar los Posts
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#Modelo Post: representará las publicaciones (posts) en el blog
class Post(models.Model):

    def __str__(self):
        return f"Titulo: {self.titulo} ----- Subtitulo: {self.subtitulo}"

    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField()
    #autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    #fecha_post = models.DateTimeField(auto_now_add=True)
    #categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo

#Modelo Comentario: Representará los comentarios en los posts
class Comentario(models.Model):
    comentario = models.ForeignKey(Post, related_name ='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    #email = models.EmailField()
    texto = models.TextField()
    #fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario por {self.nombre, self.comentario}'
    

#Modelo Contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensaje = models.TextField()
    #fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

#Modelo Recurso
class Recurso(models.Model):
    def __str__(self):
        return f"Titulo: {self.titulo}"

    titulo = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        return self.titulo