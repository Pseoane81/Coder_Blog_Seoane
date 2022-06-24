from django.shortcuts import render
from django.forms.models import model_to_dict
from posts.models import Post
from posts.forms import PostForm


# Create your views here.
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
