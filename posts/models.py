from django.db import models


class Post(models.Model): 

    titulo = models.CharField(max_length=40)
    contenido = models.TextField(max_length=3000)
    fecha = models.DateField() 

    def __str__(self):
        return f'Titulo: {self.titulo} -- Contenido: {self.contenido[:10]} -- Fecha de publicacion: {self.fecha}'