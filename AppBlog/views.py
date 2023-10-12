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
                return render(request, "AppBlog/inicio.html", {"mensaje": f"Los datos de registro son incorrectos"})
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
@login_required
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

#Vista para agregar Avatar
@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()

            return render(request, "AppBlog/inicio.html")
    else:
        form = AvatarFormulario()
    return render(request, "AppBlog/agregarAvatar.html", {"formulario":form})

#Vistas de formularios de resultados de búsqueda
def resultadosTitulo(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        post = Post.objects.filter(titulo__icontains=titulo)
        return render(request, "AppBlog/resultadosTitulo.html", {"post":post, "titulo":titulo})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)


#CRUD POST Con clases
class ListaPost(LoginRequiredMixin, ListView):
    model = Post

class DetallePost(LoginRequiredMixin, DetailView):
    model = Post

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    success_url = "/AppBlog/"
    fields = ["titulo", "subtitulo", "texto", "imagen"]

class ActualizarPost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = "/AppBlog/post/posts"
    fields = ["titulo", "subtitulo", "texto", "imagen"]

class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/AppBlog/post/posts"


#CRUD RECURSO Con clases
class ListaRecurso(LoginRequiredMixin, ListView):
    model = Recurso

class DetalleRecurso(LoginRequiredMixin, DetailView):
    model = Recurso

class CrearRecurso(LoginRequiredMixin, CreateView):
    model = Recurso
    success_url = "/AppBlog/recurso/list"
    fields = ["titulo", "link", "texto", "imagen"]

class ActualizarRecurso(LoginRequiredMixin, UpdateView):
    model = Recurso
    success_url = "/AppBlog/recurso/list"
    fields = ["titulo", "link", "texto", "imagen"]

class EliminarRecurso(LoginRequiredMixin, DeleteView):
    model = Recurso
    success_url = "/AppBlog/recurso/list"


#Formulario de Contacto
class ListaContacto(LoginRequiredMixin, ListView):
    model = Contacto

class DetalleContacto(LoginRequiredMixin, DetailView):
    model = Contacto

class CrearContacto(CreateView):
    model = Contacto
    success_url = "/AppBlog/"
    fields = ["nombre", "email", "mensaje"]

class ActualizarContacto(LoginRequiredMixin, UpdateView):
    model = Contacto
    success_url = "/AppBlog/comentario/list/"
    fields = ["nombre", "email", "mensaje"]

class EliminarContacto(LoginRequiredMixin, DeleteView):
    model = Contacto
    success_url = "/AppBlog/comentario/list/"


@login_required
def inicio(request):
    return render(request, "AppBlog/inicio.html")

def about(request):
    return render(request, "AppBlog/about.html")

@login_required
def recursos(request):
    return render(request, "AppBlog/recursos.html")











