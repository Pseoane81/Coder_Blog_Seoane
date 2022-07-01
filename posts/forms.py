from django import forms
from django.forms import HiddenInput



class PostForm(forms.Form):
    categorias = [("Interes Gral","Interes Gral"), ("Informatica","Informatica"), ("Programacion","Programacion"), ("Tutoriales","Tutoriales")]
    titulo = forms.CharField(max_length=40)
    contenido = forms.CharField(widget=forms.Textarea, max_length=3000)
    genero= forms.CharField(label='Categoria', widget=forms.Select(choices=categorias))
    #autor = forms.CharField(max_length=40)
    fecha = forms.DateField() 
    imagen = forms.ImageField()