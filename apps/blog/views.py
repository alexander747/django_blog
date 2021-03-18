from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

#iexact que no importe minusculas y maysculas
#get_object_or_404 valida igual que un try catch 
#Q es un o en la consulta sql
#__icontains es igual a like en las consultas sql 
#Paginator recibe la lista y la cantidad que sera mostrado por pagina


def Home(request):
    # hacemos la consulta del buscar
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter( 
            Q( titulo__icontains = queryset ) |
            Q( descripcion__icontains= queryset)
         ).distinct()
    else:    
        posts = Post.objects.filter( estado=True )

    paginator = Paginator( posts, 3 )
    page = request.GET.get('page') #para saber en que pagina me encuentro actualmente para hacer el paginator
    posts = paginator.get_page(page) #solo enviamos la lista segun la pagina donde nos encontremos
    return render(request, 'index.html', {'posts':posts})



def DetallePost(request, slug):
    # post = Post.objects.get(slug=slug) sin validar esta linea
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detalle_post':post})    


def Generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter( estado=True, categoria=Categoria.objects.get(nombre__iexact='General') ) 
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q( descripcion__icontains = queryset ),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact='General')
        ).distinct()
    paginator = Paginator( posts, 3 )
    page = request.GET.get('page') 
    posts = paginator.get_page(page)     
    return render(request, 'generales.html',{'posts':posts})


def Programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter( estado=True, categoria=Categoria.objects.get(nombre__iexact='Programacion') )
    if queryset:
         posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q( descripcion__icontains = queryset ),
            estado=True, categoria=Categoria.objects.get(nombre__iexact='Programacion') 
            ).distinct()

    paginator = Paginator( posts, 1 )
    page = request.GET.get('page') 
    posts = paginator.get_page(page)        
    return render(request, 'programacion.html',{'posts':posts})



def Tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter( estado=True, categoria=Categoria.objects.get(nombre__iexact='Tutoriales') )
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) |
        Q( descripcion__icontains = queryset ), 
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Tutoriales')
        )
    paginator = Paginator( posts, 3 )
    page = request.GET.get('page') 
    posts = paginator.get_page(page)    
    return render(request, 'tutoriales.html', {'posts':posts})    



def Tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter( estado=True, categoria=Categoria.objects.get(nombre__iexact='Tecnologia') )
    if queryset:
         posts = Post.objects.filter(
              Q(titulo__icontains = queryset) |
              Q( descripcion__icontains = queryset ), 
              estado=True,
              categoria=Categoria.objects.get(nombre__iexact='Tecnologia')
         )
    paginator = Paginator( posts, 3 )
    page = request.GET.get('page') 
    posts = paginator.get_page(page)     
    return render(request, 'tecnologia.html',{'posts':posts})        



def Videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter( estado=True, categoria=Categoria.objects.get(nombre__iexact='Videojuegos') )
    if queryset:
       posts = Post.objects.filter( 
            Q(titulo__icontains = queryset) |
            Q( descripcion__icontains = queryset ), 
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Videojuegos') 
       )
    paginator = Paginator( posts, 3 )
    page = request.GET.get('page') 
    posts = paginator.get_page(page)   
    return render(request, 'videojuegos.html', {'posts':posts})        