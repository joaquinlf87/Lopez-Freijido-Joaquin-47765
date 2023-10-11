from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import *
from AppBlog.forms import *
from datetime import datetime
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

#Vista de del Login
def inicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contrasena)
            if user:
                login(request, user)
                return render(request, "AppBlog/inicio.html", {"mensaje": f"Bienvenido {user}"})
        else:
            return render(request, "AppBlog/inicio.html", {"mensaje":"Los datos de registro son incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "AppBlog/login.html", {"formulario":form})


#Vista de registro
def registro(request):
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":"El Usuario ha sido creado."})
    else:
        form = UsuarioRegistro()

    return render(request, "AppBlog/registro.html", {"formulario":form})


#Vista de Edicion del usuario
def editarUsuario(request):
    usuario = request.user #para saber qué usuario está logueadp
    if request.method == "POST":
        form = FormularioEditar(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()
            return render(request, "AppBlog/inicio.html")
    else:
        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })
    return render(request, "AppBlog/editarPerfil.html", {"formulario":form, "usuario":usuario})



#Vistas de los links
def inicio(request):
    return render(request, "AppBlog/inicio.html")

def about(request):
    return render(request, "AppBlog/about.html")

def recursos(request):
    return render(request, "AppBlog/recursos.html")

def contacto(request):
    return render(request, "AppBlog/contacto.html")


#Vistas de los modelos
def autor(request):
    autor1 = Autor(
        nombre="Juan", 
        bio="Juan es un especialista en renta fija"
        )
    autor1.save()

    return render(request, "AppBlog/autor.html")

def categoria(request):
    categoria1 = Categoria(
        nombre="Renta Fija",
    )
    categoria1.save()

    return render(request, "AppBlog/categoria.html")

# Acá me falta definir algunos argumentos (categoría, fecha)
def post(request):
    post1 = Post(
        titulo="Invirtiendo en renta fija",
        subtitulo="Las mejores estrategias de inversion",
        texto="Acá estamos describiendo las mejores estrategias de inversion",
        #autor=autor,
            )
    post1.save()

    return render(request, "AppBlog/post.html")

def comentario(request):
    comentario1 = Comentario(
        post=post,
        nombre="Carlos",
        email="carlos@gmail.com",
        texto="Estoy dejando este comentario",
    )

    comentario1.save()

    return render(request, "AppBlog/comentario.html")


#Vistas de formularios


def contactoFormulario(request):
    if request.method=="POST":
        formulario1 = ContactoFormulario
        if formulario1.is_valid():
            info = formulario1.cleaned_data #Así nos da el formulario limpio, sin data
            contacto = Contacto(
                        nombre=info["nombre"], 
                        email=info["email"],
                        mensaje=info["mensaje"],
                        )
            contacto.save
            return render(request, "AppBlog/inicio.html")
    else:
        formulario1 = ContactoFormulario()
    return render(request, "AppBlog/contactoFormulario.html")


#Vistas de formularios de búsqueda
def busquedaTitulo(request):

    return render(request, "AppBlog/inicio.html")


#Vistas de formularios de resultados de búsqueda
def resultadosTitulo(request):

    if request.GET["titulo"]:
        
        titulo = request.GET["titulo"]
        post = Post.objects.filter(titulo__icontains=titulo)
        
        return render(request, "AppBlog/inicio.html", {"post":post, "titulo":titulo})
    
    else:
        
        respuesta = "No enviaste datos"
        
    return HttpResponse(respuesta)
         #Entre los corchetes pongo el ID o nombre que hayas puedo en el html correspondiente 



#CRUD POST Con clases
class ListaPost(LoginRequiredMixin, ListView):
    model = Post

class DetallePost(LoginRequiredMixin, DetailView):
    model = Post

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    success_url = "/AppBlog/"
    fields = ["titulo", "subtitulo", "texto"]

class ActualizarPost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = "/AppBlog/post/posts"
    fields = ["titulo", "subtitulo", "texto"]

class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/AppBlog/post/posts"


#CRUD COMENTARIO con Clases
class ListaComentario(ListView):
    model = Comentario

class DetalleComentario(DetailView):
    model = Comentario

class CrearComentario(CreateView):
    model = Comentario
    success_url = "/AppBlog/comentario/list"
    fields = ["nombre", "texto"]

class ActualizarComentario(UpdateView):
    model = Comentario
    success_url = "/AppBlog/comentario/list"
    fields = ["nombre", "texto"]

class EliminarComentario(DeleteView):
    model = Comentario
    success_url = "/AppBlog/comentario/list"


#CRUD RECURSO Con clases
class ListaRecurso(LoginRequiredMixin, ListView):
    model = Recurso

class DetalleRecurso(LoginRequiredMixin, DetailView):
    model = Recurso

class CrearRecurso(LoginRequiredMixin, CreateView):
    model = Recurso
    success_url = "/AppBlog/"
    fields = ["titulo", "link", "texto"]

class ActualizarRecurso(LoginRequiredMixin, UpdateView):
    model = Recurso
    success_url = "/AppBlog/recurso/list"
    fields = ["titulo", "link", "texto"]

class EliminarRecurso(LoginRequiredMixin, DeleteView):
    model = Recurso
    success_url = "/AppBlog/recurso/list"
