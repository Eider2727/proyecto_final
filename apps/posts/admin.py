from django.contrib import admin
from .models import Categoria, Post
# Register your models here.



@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','subtitulo','fecha','texto',  # campos que se listan en el administrador
                    'activo','categoria','imagen','publicado')  
    
    
admin.site.register(Categoria)
        