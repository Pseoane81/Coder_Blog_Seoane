from distutils.command.upload import upload
from django.db import models
from django import forms
from users.models import User


class Post(models.Model): 
    
    titulo = models.CharField(max_length=40)
    contenido = models.TextField(max_length=3000)
    genero= models.CharField(max_length=40)
    autor= models.CharField(max_length=40)
    fecha = models.DateField() 
    imagen = models.ImageField(upload_to="imgposts",null=True, blank=True)

    def __str__(self):
        return f'Titulo: {self.titulo} -- Contenido: {self.contenido[:10]} -- Fecha de publicacion: {self.fecha}'

class Msg(models.Model): 
    
    titulo = models.CharField(max_length=40)
    contenido = models.TextField(max_length=3000)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Titulo: {self.titulo} -- Contenido: {self.contenido[:10]} -- Autor: {self.autor}'


class MsgPost(models.Model): 
    
    titulo = models.CharField(max_length=40)
    contenido = models.TextField(max_length=3000)
    autor = models.CharField(max_length=40)
    post = models.IntegerField()
    
    def __str__(self):
        return f'Titulo: {self.titulo} -- Contenido: {self.contenido[:10]} -- Autor: {self.autor}'