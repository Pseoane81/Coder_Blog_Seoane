from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import View
from users.forms import UsuarioModelForm, UserEditForm
from users.models import User, avatar
from posts.models import Post



class Registro(View):
    def get(self, request):
        form = UsuarioModelForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UsuarioModelForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            img = avatar(image=request.FILES['imagen'],user_id=user.id)
            img.save()
            login(request, user)
            return redirect('home')
        else:
            form = UsuarioModelForm()
            return render(request, 'register.html', {'form': form})


def entrar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form = AuthenticationForm
                return render(request, 'login.html', {'form': form, "error":1})

    form = AuthenticationForm
    return render(request, 'login.html', {'form': form})


@login_required
def editarperfil(request, id):
    usuario = User.objects.get(id=id)
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            usuario.username = informacion["username"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            password = informacion["password1"]
            password1 = informacion["password2"]
            if password == password1:
                usuario.set_password(password)
            usuario.save()
            borrarimg = avatar.objects.get(user_id=id)
            borrarimg.delete()
            img = avatar(image=request.FILES['imagen'],user_id=usuario.id)
            img.save()
                
            return redirect('home')
        else:
            form = UserEditForm()
            return render(request, 'editarperfilerror.html', {'form': form})
    else:        
        form = UserEditForm(initial={"username":usuario.username})
        return render(request, 'editperfil.html', {'form': form,"usuario":usuario})

    

    



@login_required
def salir(request):
    logout(request)
    return redirect('home')


@login_required
def borrarperfil(request,id):
    perfil= User.objects.get(id=id)
    perfil.delete()
    perfil= User.objects.all()
    form = UsuarioModelForm()
    return render(request, "register.html",{"form":form})

@login_required
def perfiles(request):
    user= User.objects.all()

    return render(request, 'userstable.html',{"user":user})


@login_required
def userpost(request, id):
    user= User.objects.get(id=id)
    ps= Post.objects.filter(autor=user.username)
    avatares = avatar.objects.filter(user=id)
    if len(ps) > 0:
        return render(request, 'usuariopost.html',{"usuario":user,"posts":ps,"avatar":avatares[0].image.url,"cant":1})
    else:
        return render(request, 'usuariopost.html',{"usuario":user,"posts":ps,"avatar":avatares[0].image.url,"cant":0})




