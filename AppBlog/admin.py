from django.contrib import admin
from AppBlog.models import *

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Autor)

