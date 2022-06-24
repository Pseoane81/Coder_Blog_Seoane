from django import forms


class PostForm(forms.Form):
    
    titulo = forms.CharField(max_length=40)
    contenido = forms.CharField(widget=forms.Textarea, max_length=3000)
    fecha = forms.DateField() 