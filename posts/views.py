from django.shortcuts import render
from django.forms.models import model_to_dict
from posts.models import Post
from users.models import User
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def nuevopost(request): #agrega nuevos posteos
    
    if request.method == 'POST':
        user= User.objects.all()
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data
            blog = Post(titulo=info['titulo'], contenido=info['contenido'], fecha=info['fecha'],autor=info['autor'],genero=info['genero'])
            blog.imagen = request.FILES['imagen']

            blog.save()

            post= Post.objects.all()
            
            return render(request, 'home.html',{"posts":post})

    else:

        form = PostForm()

    return render(request, 'formpost.html', {"form":form})


@login_required
def tablapost(request):
    post= Post.objects.all()

    return render(request, 'posttable.html',{"posts":post})

@login_required
def post(request,id):
    
    post = Post.objects.filter(id=id)
    
    
    return render(request, 'post.html',{"posts":post[0]})

@login_required
def deletepost(request,id):
    
    post  = Post.objects.get(id=id)
    post.delete()

    post= Post.objects.all()
    
    return render(request, 'posttable.html',{"posts":post})

@login_required
def editpost(request,id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            post.titulo = info["titulo"] 
            post.contenido = info["contenido"]
            post.fecha = info["fecha"]
            post.autor = info["autor"]
            post.genero = info["genero"]
            post.imagen = request.FILES['imagen']
            post.save()
            post= Post.objects.all()
            return render(request, 'posttable.html',{"posts":post})
    else:
        form = PostForm()
    return render(request, 'editpost.html', {"form":form})


@login_required
def tutoriales(request):
    
    post = Post.objects.filter(genero="Tutoriales")
    
    
    return render(request, 'filter.html',{"posts":post})


@login_required
def informatica(request):
    
    post = Post.objects.filter(genero="Informatica")
    
    
    return render(request, 'filter.html',{"posts":post})


@login_required
def programacion(request):
    
    post = Post.objects.filter(genero="Programacion")
    
    
    return render(request, 'filter.html',{"posts":post})


@login_required
def integral(request):
    
    post = Post.objects.filter(genero="Interes Gral")
    
    
    return render(request, 'filter.html',{"posts":post})

def res_busqueda(request):
    if request.GET['contenido']:
        contenido=request.GET['contenido']
        data= Post.objects.filter(contenido__icontains = contenido)
        return render(request, "busqueda.html", {"posts": data})
    else:
        return render(request, "busqueda404.html")

