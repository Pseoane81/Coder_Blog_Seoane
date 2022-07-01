from django.urls import path
from users.views import *
from posts.views import *
from users import views


urlpatterns = [
    path('registro/', Registro.as_view(), name='register'),
    path('editarperfil/<int:id>', editarperfil, name='editarperfil'),
    path('borrarperfil/<int:id>', borrarperfil, name='borrarperfil'),
    path('perfiles/', perfiles, name='perfiles'),
    path('logout/', salir, name='logout'),
    path('login/', entrar, name='login'),
    path('userpost/<int:id>', userpost, name='userpost')
    ]