from django.shortcuts import render
from django.forms.models import model_to_dict
from posts.models import Post, MsgPost
from users.models import User
from posts.forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def nuevopost(request): #agrega nuevos posteos
    
    if request.method == 'POST':
        user= User.objects.all()
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data
            print(request.POST)
            blog = Post(titulo=info['titulo'], contenido=info['contenido'],autor=request.user.username, fecha=info['fecha'],genero=info['genero'])
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
    msg = MsgPost.objects.filter(post=id)
    if len(msg) > 0:
        return render(request, 'post.html',{"posts":post[0],"msg":msg, "cant":1})
    else:
        return render(request, 'post.html',{"posts":post[0],"msg":msg, "cant":0})

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
            post.autor = request.user.username
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
        if data:
            return render(request, "busqueda.html", {"posts": data})
        else:
            return render(request, "busqueda404.html")

def msg(request, id): #agrega nuevos posteos
    post = Post.objects.get(id=id)
    print(post)
    if request.method == 'POST':
        
        form = MsgForm(request.POST)
        print(request)
        
        if form.is_valid():

            info = form.cleaned_data
            msg = MsgPost(titulo=info['titulo'], contenido=info['contenido'],autor=request.user.username,post=post.id)
            msg.save()

            post= Post.objects.all()
            
            return render(request, 'posttable.html',{"posts":post})
