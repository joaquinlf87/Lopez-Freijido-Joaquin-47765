from django.urls import path
from AppBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('recursos/', recursos, name="Recursos"),
    path('login/', inicioSesion, name="Login"),
    path('registro/', registro, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="AppBlog/logout.html"), name="Logout"),
    path('editar/', editarUsuario, name="EditarUsuario"),
    path('agregarAvatar/', agregarAvatar, name="Avatar"),

    #Formularios busqueda
    path('resultadosTitulo/', resultadosTitulo, name="ResultadosBusquedaTitulo"), #Este puedo eliminarlo (chequear todo primero)

    #CRUD Post usando Clases
    path('post/posts/', ListaPost.as_view(), name="PostLeer"),
    path('post/<int:pk>', DetallePost.as_view(), name="PostDetalle"),
    path('post/crear/', CrearPost.as_view(), name="PostCrear"),
    path('post/editar/<int:pk>', ActualizarPost.as_view(), name="PostEditar"),
    path('post/eliminar/<int:pk>', EliminarPost.as_view(), name="PostEliminar"),

    #CRUD Recurso usando Clases
    path('recurso/list/', ListaRecurso.as_view(), name="RecursoLeer"),
    path('recurso/<int:pk>', DetalleRecurso.as_view(), name="RecursoDetalle"),
    path('recurso/crear/', CrearRecurso.as_view(), name="RecursoCrear"),
    path('recurso/editar/<int:pk>', ActualizarRecurso.as_view(), name="RecursoEditar"),
    path('recurso/eliminar/<int:pk>', EliminarRecurso.as_view(), name="RecursoEliminar"),

    #CRUD Contacto usando Clases
    path('contacto/list/', ListaContacto.as_view(), name="ContactoLeer"),
    path('contacto/<int:pk>', DetalleContacto.as_view(), name="ContactoDetalle"),
    path('contacto/crear/', CrearContacto.as_view(), name="ContactoCrear"),
    path('contacto/editar/<int:pk>', ActualizarContacto.as_view(), name="ContactoEditar"),
    path('contacto/eliminar/<int:pk>', EliminarContacto.as_view(), name="ContactoEliminar"),

 
]