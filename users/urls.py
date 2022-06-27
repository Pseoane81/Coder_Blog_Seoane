from django.urls import path
from users.views import Registro, salir, entrar, EditarPerfil, borrarperfil, perfiles
from posts.views import *
from users import views


urlpatterns = [
    path('registro/', Registro.as_view(), name='register'),
    path('editarperfil/', EditarPerfil.as_view(), name='editarperfil'),
    path('borrarperfil/<int:id>', borrarperfil, name='borrarperfil'),
    path('perfiles/', perfiles, name='perfiles'),
    path('logout/', salir, name='logout'),
    path('login/', entrar, name='login')
    ]