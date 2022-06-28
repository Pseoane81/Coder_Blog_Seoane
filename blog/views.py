from django.http import HttpResponse
from django.shortcuts import redirect, render
from posts.models import Post


# Create your views here.

def home(request):
    post= Post.objects.all()
    print(post[10].imagen)
    return render(request, 'home.html',{"posts":post})