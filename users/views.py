from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import View
from users.forms import UsuarioModelForm, UserEditForm
from users.models import User



class Registro(View):
    def get(self, request):
        form = UsuarioModelForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UsuarioModelForm(request.POST)
        if form.is_valid():
            user = form.save()
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
                return HttpResponse(f"Usuario Incorrecto")

    form = AuthenticationForm
    return render(request, 'login.html', {'form': form})




class EditarPerfil(View):
    
    def get(self, request):
        usuario = request.user
        form = UserEditForm(initial={"username":usuario.username})
        print(form)
        return render(request, 'editperfil.html', {'form': form,"usuario":usuario})

    
    def post(self, request):
        usuario = request.user
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data

            usuario.username = informacion["username"]
            usuario.last_name = informacion["last_name"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            
            return redirect('home')
        else:
            form = UserEditForm()
            return render(request, 'editperfil.html', {'form': form})



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




