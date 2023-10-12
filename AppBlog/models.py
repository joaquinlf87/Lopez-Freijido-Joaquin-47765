from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import User


#Create your models here.
#Modelo Post: representará las articulos (posts) en el blog
class Post(models.Model):

    def __str__(self):
        return f"Titulo: {self.titulo} ----- Subtitulo: {self.subtitulo}"
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen=models.ImageField(upload_to = 'posts', null=True)

    def __str__(self):
        return self.titulo


#Modelo Contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

#Modelo Recurso
class Recurso(models.Model):
    def __str__(self):
        return f"Titulo: {self.titulo}"

    titulo = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    texto = models.TextField()
    imagen=models.ImageField(upload_to = 'recursos', null=True)

    def __str__(self):
        return self.titulo
    
#Modelo de avatar
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)






