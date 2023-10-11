from django import forms
from AppBlog.models import *
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario de Post
class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    texto = forms.CharField(widget=forms.Textarea)
    #autor = forms.ForeignKey(Autor, on_delete=models.CASCADE)
    #fecha_post = forms.DateTimeField(auto_now_add=True)
    #categorias = forms.ManyToManyField(Categoria)

#Formulario de comentarios
class ComentarioFormulario(forms.Form):
    post = forms.ModelChoiceField(queryset=Post.objects.all())
    nombre = forms.CharField(max_length=100)
    #email = forms.EmailField()
    texto = forms.CharField(widget=forms.Textarea)
    #fecha_comentario = forms.DateTimeField(initial=datetime.datetime.now)

#Formulario de contacto
class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea)

#Formulario para el registro de un usuario
class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

#Formulario para edicion de usuarios
class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"] #El username no se va a poder editar

