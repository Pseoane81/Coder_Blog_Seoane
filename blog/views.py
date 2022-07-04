from ast import Not
from django.http import HttpResponse
from django.shortcuts import redirect, render
from posts.models import Post
from users.models import User, avatar


# Create your views here.

def home(request):
    post= Post.objects.all()
    user = request.user
    avatares = avatar.objects.filter(user=request.user.id)
    if len(avatares) > 0:
        return render(request, 'home.html',{"posts":post, "user":user.username,"img":avatares[0].image.url})
    else:
        return render(request, 'home.html',{"posts":post})


def about(request):
    return render(request, 'about.html')
    
    
  