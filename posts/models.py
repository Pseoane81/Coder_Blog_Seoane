from django.db import models
from django import forms


class Post(models.Model): 
    categorias = ["Interes Gral", "Informatica", "Programacion", "Tutoriales"]
    titulo = models.CharField(max_length=40)
    contenido = models.TextField(max_length=3000)
    genero= forms.CharField(label='Seleccione Categoria', widget=forms.Select(choices=categorias))
    fecha = models.DateField() 

    def __str__(self):
        return f'Titulo: {self.titulo} -- Contenido: {self.contenido[:10]} -- Fecha de publicacion: {self.fecha}'