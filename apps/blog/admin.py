from django.contrib import admin

from .models import *
#para generar los documentos 
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    #barra de busqueda
    search_fields = ['nombre']
    #importante coma al final
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = CategoriaResource



class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #barra de busqueda
    search_fields = ['nombres','apellidos', 'correo']
    #importante coma al final
    list_display = ('nombres','apellidos','correo','estado','fecha_creacion',)
    resource_class = AutorResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)




