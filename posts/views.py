from django.shortcuts import render
from django.forms.models import model_to_dict
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def nuevopost(request): #agrega nuevos posteos
    
    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            blog = Post(titulo=info['titulo'], contenido=info['contenido'], fecha=info['fecha'])

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
        form = PostForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            post.titulo = info["titulo"] 
            post.contenido = info["contenido"]
            post.fecha = info["fecha"]
            post.save()
            post= Post.objects.all()
            return render(request, 'posttable.html',{"posts":post})
    else:
        form = PostForm()
    return render(request, 'editpost.html', {"form":form})
