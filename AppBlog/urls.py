from django.urls import path
from AppBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('recursos/', recursos, name="Recursos"),
    path('contacto/', contacto, name="Contacto"),
    path('login/', inicioSesion, name="Login"),
    path('registro/', registro, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="AppBlog/logout.html"), name="Logout"),
    path('editar/', editarUsuario, name="EditarUsuario"),
   
    path('autor/', autor),
    path('categoria/', categoria),
    path('post/', post),
    path('comentario/', comentario),

    #Formularios
    #path('postFormulario/', postFormulario, name="FormularioPost"),
    path('contactoFormulario/', contactoFormulario, name="FormularioContacto"),

    #Formularios busqueda
    path('busquedaTitulo/', busquedaTitulo, name="BusquedaTitulo"), #Este puedo eliminarlo (chequear todo primero)  
    path('resultadosTitulo/', resultadosTitulo, name="ResultadosBusquedaTitulo"), #Este puedo eliminarlo (chequear todo primero)

    
    #CRUD Post
    #path('leerPost/', leerPost, name="PostLeer"),
    #path('crearPost/', crearPost, name="PostCrear"),
    #path('editarPost/<postTitulo>/', editarPost, name="PostEditar"),
    #path('eliminarPost/<postTitulo>/', eliminarPost, name="PostEliminar"),

    #CRUD Post usando Clases
    path('post/posts/', ListaPost.as_view(), name="PostLeer"),
    path('post/<int:pk>', DetallePost.as_view(), name="PostDetalle"),
    path('post/crear/', CrearPost.as_view(), name="PostCrear"),
    path('post/editar/<int:pk>', ActualizarPost.as_view(), name="PostEditar"),
    path('post/eliminar/<int:pk>', EliminarPost.as_view(), name="PostEliminar"),

    #CRUD Comentario usando Clases
    path('comentario/list/', ListaComentario.as_view(), name="ComentarioLeer"),
    path('comentario/<int:pk>', DetalleComentario.as_view(), name="ComentarioDetalle"),
    path('comentario/crear/', CrearComentario.as_view(), name="ComentarioCrear"),
    path('comentario/editar/<int:pk>', ActualizarComentario.as_view(), name="ComentarioEditar"),
    path('comentario/eliminar/<int:pk>', EliminarComentario.as_view(), name="ComentarioEliminar"),    

    #CRUD Recurso usando Clases
    path('recurso/list/', ListaRecurso.as_view(), name="RecursoLeer"),
    path('recurso/<int:pk>', DetalleRecurso.as_view(), name="RecursoDetalle"),
    path('recurso/crear/', CrearRecurso.as_view(), name="RecursoCrear"),
    path('recurso/editar/<int:pk>', ActualizarRecurso.as_view(), name="RecursoEditar"),
    path('recurso/eliminar/<int:pk>', EliminarRecurso.as_view(), name="RecursoEliminar"),

]